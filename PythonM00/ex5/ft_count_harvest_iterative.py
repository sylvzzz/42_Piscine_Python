def ft_count_harvest_iterative(day=1, days=5):
    days = int(input("Days until harvest: "))
    while (day <= days):
        print(f"Day {day}")
        day += 1
    print("Harvest time")
