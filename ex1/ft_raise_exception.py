def input_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)

        if temp < 0:
            print(
                f"Input data is '{temp}'\n"
                f"Caught input_temperature error: {temp}°C is too "
                f"cold for plants (min 0°C)"
            )
            return None
        
        elif temp > 40:
            print(
                f"Input data is '{temp}'\n"
                f"Caught input_temperature error: {temp}°C is "
                f"too hot for plants (max 40°C)"
            )
            return None

        else:
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

    inputs = ["25", "abc", "100", "-50"]

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
