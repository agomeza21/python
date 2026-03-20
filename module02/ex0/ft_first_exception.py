def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    temperatures = ["25", "abc"]

    print("=== Garden Temperature ===")
    print("")
    for temperature in temperatures:
        print(f"Input data is '{temperature}'")
        try:
            result = input_temperature(temperature)
            print(f"Temperature is now {result}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
