def ft_count_harvest_recursive():
    limit_day = int(input("Days until harvest: "))
    actual_day = 1

    def helper(actual_day):
        if actual_day > limit_day:
            return
        print(actual_day)
        helper(actual_day + 1)
    helper(actual_day)
    print("Harvest time!")
