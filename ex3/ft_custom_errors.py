class GardenError(Exception):
    def __init__(self, err: str = "Unknown garden error") -> None:
        self.err = err


class PlantError(GardenError):
    def __init__(self, err: str = "Unknown plant error"):
        super().__init__(err)


class WaterError(GardenError):
    def __init__(self, err: str = "Unknown water error"):
        super().__init__(err)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_specific_errors() -> None:
    print("Testing PlantError...")

    try:
        check_plant()
    except PlantError as e:
        print(
            f"Caught PlantError: {e}"
        )
    print()

    print("Testing WaterError...")

    try:
        check_water()
    except WaterError as e:
        print(
            f"Caught WaterError: {e}"
        )
        print()


def test_all_garden_errors() -> None:
    print("Testing catching all garden errors...")

    for function in (check_plant, check_water):
        try:
            function()

        except GardenError as e:
            print(
                f"Caught GardenError: {e}"
            )


def display() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_specific_errors()
    test_all_garden_errors()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    display()
