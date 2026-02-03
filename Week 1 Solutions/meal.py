def main():
    clock = input("What time is it? ")
    time = convert(clock)

    if 7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    num_hours = float(hours)
    num_minutes = float(minutes)
    result = num_hours + (num_minutes / 60)
    return result

if __name__ == "__main__":
    main()
