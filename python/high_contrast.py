# -*- coding: utf-8 -*-
"""High Contrast Calculator

Use the W3 definitions for colour contrasting to calculate the optimal
RGB tuples that provide the highest contrast to a provided RGB color.
"""
import click

__version__ = "0.1"
__author__ = "Aaron J. Maxwell <ajmax@paladin.ai>"
MAX = 255  # Max RGB colour channel.
MIN = 7.0  # Minimum Contrast Ratio.


def standardize(x):
    """Define the standardization function for the channel.

    :param x: Colour channel value. :type int

    :return: Standardized colour channel value. :type float
    """
    x /= MAX
    if x <= 0.03928:
        x /= 12.92
    else:
        x = ((x + 0.055) / 1.055) ** 2.4
    return x


def rel_lum(rgb):
    """Compute the relative luminance.

    :param rgb: The RGB colour tuple. :type tuple
    """
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]


def contrast(u, d):
    """Compute the contrast between two colours.

    :param u: Numerator :type float

    :param d: Denominator :type float

    :return c: contrast :type float
    """
    return (u + 0.05) / (d + 0.05)


def hexkey(r, g, b):
    """Helper to turn RGB tuple to a hex value."""
    return hex(r)[3:] + hex(g)[3:] + hex(b)[3:]


@click.command()
@click.argument('rgb', nargs = 1)
@click.option('--hex', prompt = 'Y/N',
              help = 'Use this if passing a colour as hex instead of RGB tuple.')
def brightest(**kw):
    """Compute the brightest contrasts for a given RGB tuple.

    :param kw: RGB as a tuple or as a hex colour code. :type dict
    """
    if kw['hex'].lower() != "y":
        rgb = tuple(int(x) for x in kw["rgb"].split(","))
    else:
        rgb = tuple((int(kw["rgb"][:2], base = 16), int(kw["rgb"][2:4], base = 16),
                     int(kw["rgb"][4:], base = 16)))

    choices = dict()
    rgb = tuple(standardize(x) for x in rgb)
    rl = rel_lum(rgb)

    for i in range(0, MAX + 1):
        r = standardize(i)
        x = rel_lum((r, 0, 0))

        if contrast(rl, x) < MIN:
            break
        else:
            for j in range(0, MAX + 1):
                g = standardize(j)
                x = rel_lum((r, g, 0))

                if contrast(rl, x) < MIN:
                    break
                else:
                    s = "rgb({},{},{}-".format(i, j, 0)
                    for k in range(0, MAX + 1):
                        b = standardize(k)
                        x = rel_lum((r, g, b))

                        if len(choices) < 5:
                            choices[hexkey(i, j, k)] = dict(l = x, r = i, g = j, b = k)
                        else:
                            y = [v['l'] for v in choices.values()]
                            if x > min(y):
                                for q in choices.keys():
                                    if choices[q]["l"] == min(y):
                                        break
                                    choices.pop(q)
                                    choices[hexkey(i, j, k)] = dict(l = x, r = i, g = j, b = k)
    print(choices)


if __name__ == "__main__":
    brightest()
