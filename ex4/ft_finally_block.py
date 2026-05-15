class PlantError(Exception):
    def __init__(self, err: str = "Unknown plant error"):
        super().__init__(err)


def water_plant(plant_name: str) -> None:
    if not (plant_name == plant_name.capitalize()):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    valid_list = ["Tomato", "Lettuce", "Carrots"]
    invalid_list = ["Tomato", "lettuce"]

    try:
        print("Testing valid plants...")
        print("Opening watering system")

        for plant in valid_list:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")

    finally:
        print("Closing watering system")
        print()

    try:
        print("Testing invalid plants...")
        print("Opening watering system")

        for plant in invalid_list:
            water_plant(plant)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")

    finally:
        print("Closing watering system")

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
