M = 255
C = 7.0 # Minimum contrast ratio
R, G, B = 242, 129, 61 #f2813d
brightest = list()

def stand(x):
    x = x / M
    if x <= 0.03928:
        x = x / 12.92
    else:
        x = ((x + 0.055) / 1.055)**2.4
    return x

def rel_lum(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def cont(u, d):
    return (u + 0.05) / (d + 0.05)

L = rel_lum(stand(R), stand(G), stand(B))

for r in range(0, M + 1):
    R = stand(r)
    X = rel_lum(R, 0, 0)
    if cont(L, X) < C:
        break
    else:
        for g in range(0, M + 1):
            G = stand(g)
            X = rel_lum(R, G, 0)
            if cont(L, X) < C:
                break
            else:
                s = "rgb({},{},{}-".format(r, g, 0)
                for b in range(0, M + 1):
                    B = stand(b)
                    X = rel_lum(R, G, B)
                    if len(brightest) == 0:
                       brightest.append((X, [r, g, b]))
                    else:
                        if 
                    if cont(L, X) < C:
                        print(s + "{})".format(b-1))
                        break

