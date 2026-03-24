import math


def get_player_pos() -> tuple:
    while True:
        user_input = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ")
        user_list = user_input.split(",")
        if len(user_list) == 3:
            try:
                float_list = []
                for i in user_list:
                    float_list.append(float(i))
            except ValueError:
                print(f"Error on parameter '{i}':"
                      f" could not convert string to float: '{i}'")
                continue
            coordinates = tuple(float_list)
            return coordinates
        else:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    coordinates = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    x, y, z = coordinates
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance = math.sqrt(x**2 + y**2 + z**2)
    rdistance = round(distance, 4)
    print(f"Distance to center: {rdistance}")
    print("")
    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    x2, y2, z2 = coordinates2
    distance2 = math.sqrt((x2-x)**2 + (y2-y)**2 + (z2-z)**2)
    rdistance2 = round(distance2, 4)
    print(f"Distance between the 2 sets of coordinates: {rdistance2}")


if __name__ == "__main__":
    main()
