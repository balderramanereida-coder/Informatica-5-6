def main():

    day1 = [26,26,25,25,24,22,21,21,20]
    day2 = [20,19,19,18,17,17,17,17,18,20,22,24,26,27,27,28,28,28,27,26,24,22,21,21]
    day3 = [20,19,18,18,17,17,16,16,18,20,22,24,25,26,27,27]
    # TO-DO: Print daily headers and call max_temperature / min_temperature

    print("Today")
    max_temperature(day1)
    min_temperature(day1)
    print()
    print("Tomorrow")
    max_temperature(day2)
    min_temperature(day2)
    print()
    print("Day after tomorrow")
    max_temperature(day3)
    min_temperature(day3)

def max_temperature(temperatures):
    highest_temp = temperatures[0]
    for hour in temperatures:
        if hour > highest_temp:
            highest_temp = hour
    print(f"High {highest_temp}°")

def min_temperature(temperatures):

    lowest_temp = temperatures[0]
    for hour in temperatures:
        if hour < lowest_temp:
            lowest_temp = hour
    print(f"High {lowest_temp}°")



if __name__ == "__main__":
    main()
