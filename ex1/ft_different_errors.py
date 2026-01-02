#!/usr/bin/python3


def garden_operations(error: str) -> bool:
    if (error == "ValueError"):
        try:
            value = int("abc")
            print(value)
        except ValueError:
            raise ValueError("Caught ValueError: invalid literal for int()")
    if (error == "ZeroDivisionError"):
        try:
            value = 5 / 0
            print(value)
        except ZeroDivisionError:
            raise ZeroDivisionError("Caught ZeroDivisionError: division by zero")
    if (error == "FileNotFoundError"):
        try:
            file = open("missing.txt", "r")
            content = file.read()
            print(content)
        except FileNotFoundError:
            raise FileNotFoundError("Caught FileNotFoundError: No such file 'missing.txt'")
    if (error == "KeyError"):
        try:
            dictionnary = {'_height': 1, '_score': 2}
            print(dictionnary['missing\\_plant'])
        except KeyError:
            raise KeyError("missing_plant")
        


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    errors = ['ValueError', 'ZeroDivisionError', 'FileNotFoundError',
              'KeyError']
    for error in errors:
        try:
            print(f"Testing {error}...")
            garden_operations(error)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                KeyError) as e:
            if (error == 'KeyError'):
                print(f"Caught KeyError: {e}")
            else:
                print(e)
        print("")
    print("Testing multiple errors together...")
    for error in errors:
        try:
            garden_operations(error)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                KeyError):
            raise Exception("Caught an error, but program continues!")

try:
    test_error_types()
except Exception as e:
    print(e)
print("\nAll error types tested successfully!")