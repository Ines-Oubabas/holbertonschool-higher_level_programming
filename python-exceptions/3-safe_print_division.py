#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: Error, division by zero.")
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        elif result is None and b != 0:
            print("Inside result: Error in division.")
        return result
