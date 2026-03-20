def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    temperatures = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
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
