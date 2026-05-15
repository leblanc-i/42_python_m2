def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        return int("abc")

    elif operation_number == 1:
        return 1 / 0

    elif operation_number == 2:
        file = open("/non/existent/file", "r")
        return file.read()

    elif operation_number == 3:
        return "abc" + 1

    else:
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    operation_numbers = [0, 1, 2, 3, 4]

    for num in operation_numbers:
        print(f"Testing operation {num}...")

        try:
            result = garden_operations(num)
            if result is None:
                print("Operation completed successfully")

        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")

        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print()

    print("=== Catching multiple error types together ===")

    for i in range(5):
        try:
            garden_operations(i)

        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught one of the expected errors: {e}")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
