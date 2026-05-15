def input_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)
        return temp

    except ValueError:
        print(
            f"Input data is '{temp_str}'\n"
            f"Caught input_temperature error: invalid literal "
            f"for int() with base 10: '{temp_str}'"
        )
        return None


def test_temperature() -> int | None:
    print("=== Garden Temperature ===\n")

    inputs = ["25", "abc"]

    for temp in inputs:
        result = input_temperature(temp)
        if result is not None:
            print(
                f"Input data is '{result}'\n"
                f"Temperature is now {result}°C"
            )
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
