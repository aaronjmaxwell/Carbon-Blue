def linfit(x, y):
    """Ordinary Least Squares.

    Computes the OLS fit to the equation y = m * x + b.

    Arguments
    ---------
    x: `array`
        The ordinate data.
    y: `array`
        The abscissa data.

    Returns
    -------
    ols: `tuple`
        The OLS parameters for the linear data: slope, slope error,
        intercept, intercept error, and chi^2 or least squares error.
    """
    n = len(x)
    if (n != len(y)):
        raise ValueError("Lengths of x, y arrays must be equal.")

    sx = sum(x)
	sy = sum(y)
	sxx = sum(x * x)
	syy = sum(y * y)
	sxy = sum(x * y)

    m = (n * sxy - sx * sy) / (n * sxx - sx * sx)
	b = sy / n - m * sx / n
	e = y - b - m * x

    chi = sum(e * e)
	s = (n * syy - sy * sy - m * m * (n * sxx - sx * sx)) / n / (n - 2)
	dm = n * s / (n * sxx - sx * sx)
	db = dm * sxx / n

    return (m, dm, b, db, chi)
