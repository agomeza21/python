def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 100 / 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
       _ = "temperature" + 25  # type: ignore


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
