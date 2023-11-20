#!/usr/bin/python3

def raise_exception():
    try:

        result = "string" + 42
    except TypeError as e:
        # Handling the raised type exception
        print("Type Error: {}".format(e))
    finally:
        print("Exception raised and handled")
