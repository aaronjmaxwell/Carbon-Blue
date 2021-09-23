def window(N, name = 'blackman', half = False):
    # we need half the window so we double the amount of sampling points
    if half:
        N = 2 * N

    if name == 'blackman':
        print('Not using _exact_ Blackman')
        alpha = 0.16
        a = [(1 - alpha) / 2, 0.5, alpha / 2]
        w = [a[0] - a[1] * np.cos(2 * np.pi * n / N) + a[2] * np.cos(4 * np.pi * n / N) for n in
             range(N)]

    # toss away the left half of the windo
    if half:
        w = w[int(N // 2):]
    return w


def low_pass(fc=0.1, b=0.08, name='blackman'):
    # define window length using the transition band size as a fraction of sampling rate
    N = int(np.ceil((4 / b)))
    # ensure the window length is odd
    if not N % 2:
        N += 1
    n = np.arange(N)
    w = window(N, name=name)
    # create an infinite impulse response filter using the sinc function
    iir = np.sinc(2 * fc * (n - (N - 1) / 2.))
    # Pass the iir through the window function
    fir = iir * w
    # normalize and return to be convolved with array
    return fir / np.sum(fir)


def fft_filter(x, f_w = 0.1):
    v = None
    if x.size % 2:
        print("input cannot be odd, removing last data point for FFT")
        v = x[-1]
        x = x[:-1]
    f_max = 0.5
    # Generate the FFT of the array, the FFT relative frequencies (to the sampling frequency),
    # and the bin size
    y = np.fft.rfft(x)
    p = y ** 2
    nu = np.linspace(0, f_max, y.size, endpoint = False)
    b = 1 / y.size
    # Ensure the frequency filter width is not too large
    if ((f_w >= f_max) or (f_w <= 0)):
        print('frequency bin width too wide, setting to default')
        f_w = 0.1
    # Generate the window size and apply to everything beyond the peak power
    N = int(f_w // b)
    Z = (y.size - N - p.argmax()) * [0]

    y_f = np.array(p.argmax() * [1] + window(N, half = True) + Z) * y

    x_f = np.fft.irfft(y_f)
    if v is not None:
        print("adding last data point back on")
        x_f = np.append(x_f, v)
    return x_f


def find_ingress(p, q, push, min_roll = 3.0, lim = 0.025):
    # Find where the running average first goes below zero
    i = np.where(np.abs(p) < min_roll)[0]
    j = np.diff(i)
    k = np.where(j > 1)[0]
    if k.size == 0:
        k = i[-1]
    else:
        k = k[0]

    idx = np.where(np.abs(q[:k]) < lim)[0]
    if idx.size > 0:
        return idx[-1] + push
    else:
        return push


def find_turn(p, q, push, max_roll = 35, lim = 0.5):
    # Grab the
    i = np.where(np.abs(p) > max_roll)[0]
    j = np.diff(i)
    k = np.where(j > 1)[0]
    if k.size == 0:
        k = i[-1]
    else:
        k = k[0]

    idx = np.where(np.abs(q[i[:k]]) < lim)[0]
    return (i[0] + idx[0] + push, i[0] + idx[-1] + push)


def find_end(p, vP, loc, push, max_roll = 35, min_roll = 3, lim = 0.5):
    if abs(vP[loc]) > min_roll:
        # we didn't complete two symmetric turns
        if p[loc] < 0:
            i = np.where(p[loc:] <= max_roll)[0] + loc
        else:
            i = np.where(p[loc:] >= -max_roll)[0] + loc
        j = np.diff(i)
        k = np.where(j > 1)[0]
        if k.size == 0:
            k = i[-1]
        else:
            k = k[0]

        idx = np.where(np.abs(p[i[:k]]) < min_roll)[0] + i[0]
        return idx[0] + push
    else:
        if p[loc] < 0:
            i = np.where(p[loc:] <= -min_roll)[0] + loc
        else:
            i = np.where(p[loc:] >= min_roll)[0] + loc
        j = np.diff(i)
        k = np.where(j > 1)[0]
        if k.size == 0:
            k = -1
        else:
            k = k[0]

        return i[k] + push


F = flights[0]
x = df[(df.session_id == F['session']) & (df.run_id == F['run']) & (df.activity_started_at == F['started_at'])]
t, phi, phi_dot = x.index.values, x.roll.values, x.roll_rate.values
Phi, Phi_dot = np.convolve(phi, low_pass(fc = 0.01), mode = 'same'), fft_filter(phi_dot)
varphi = np.cumsum(phi) / (np.arange(len(phi)) + 1)

fig, ax = plt.subplots(2, figsize = figsize)

idx = np.where(np.abs(varphi) < 3)[0]
if idx[0] != 0:
    print('we are not at beginning of steep turn')
n = turn_number(phi)
occurences = []

for o in range(n):
    if len(occurences) == 0:
        push, ingress = 0, None
    else:
        push = occurences[-1]['end']
    O = {'start': push, 'ingress': ingress, 'turn': None, 'egress': None, 'end': None}
    if ingress is None:
        if o // 2:
            O['ingress'] = find_ingress(varphi[push:], Phi_dot[push:], push)
        else:
            O['ingress'] = find_ingress(phi[push:], Phi_dot[push:], push)
    O['turn'], O['egress'] = find_turn(Phi[push:], Phi_dot[push:], push)
    O['end'] = find_end(phi[push:], varphi[push:], O['egress'] - push, push)
    occurences.append(O)

ax[0].plot(t, phi, '.', ms = 3)
ax[0].plot(t, varphi, '.', ms = 3)

ax[0].plot(t[push:], Phi[push:], lw = 1, color = 'k')

for o in occurences[:2]:
    ax[0].plot(t[o['start']:o['ingress']], phi[o['start']:o['ingress']], lw = 2, color = 'r')
    ax[0].plot(t[o['ingress']:o['turn']], phi[o['ingress']:o['turn']], lw = 2, color = 'g')
    ax[0].plot(t[o['turn']:o['egress']], phi[o['turn']:o['egress']], lw = 2, color = 'b')
    ax[0].plot(t[o['egress']:o['end']], phi[o['egress']:o['end']], lw = 2, color = 'cyan')

ax[0].plot(t[693:710], Phi[693:710], lw = 1, color = 'magenta')

ax[1].plot(t, phi_dot, '.', ms = 3, mec = 'none', label = r'd$\phi$/dt')
# ax[1].plot(t[:loc[0]['start']], phi_dot[:loc[0]['start']], '.', ms = 5, mec = 'none', label = r'd$\phi$/dt')
# ax[1].plot(t[loc[0]['main_start']:loc[0]['main_end']], phi_dot[loc[0]['main_start']:loc[0]['main_end']], '.', ms = 5, mec = 'none', label = r'd$\phi$/dt')
# ax[1].plot(t, Phi_dot, alpha = 0.8, label = r'd$\Phi$/dt')
# ax[1].legend()
# ax[1].set_ylim(-3.5, 3.5)
# ax[1].set_yticks(np.linspace(-3.5, 3.5, 15))
# ax[1].grid()

for a, c in zip((3, 35, 43, 47), ('b', 'r', 'g', 'g')):
    ax[0].axhline(a, color = c, alpha = 0.25, ls = '--')
    ax[0].axhline(-a, color = c, alpha = 0.25, ls = '--')

for a, c in zip((0.025, 0.5, 1.5, 3), ('b', 'r', 'y', 'g')):
    ax[1].axhline(a, color = c, alpha = 0.25, ls = '--')
    ax[1].axhline(-a, color = c, alpha = 0.25, ls = '--')