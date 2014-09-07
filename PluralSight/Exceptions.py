__author__ = 'navodissa'
import sys


def convert(s):
    """Convert to an integer"""
    try:
        return int(s)
      #  print("Conversion successful! x =", x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
      #  print("Conversion failed!")
        raise
        #return -1


convert("33")
convert("Navoda")
convert([1, 2, 3])
