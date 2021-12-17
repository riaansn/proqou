#! /usr/bin/python3
# -*- coding: utf-8 -*-
LIMIT = 1000


def reading_number(limit):
    if limit <= LIMIT:
        for n in range(limit + 1):
            if n % 5 == 0 and not n % 20 == 0:
                print("beep")
            elif n % 20 == 0 and not n % 100 == 0:
                print("boop")
            elif n % 100 == 0 and n > 0:
                print("beep boop")
            else:
                continue
    else:
        print(
            f"Your value: {limit} is to large! We only accept numbers up to {LIMIT}..."
        )


def main():
    print("Please set the limit for printing beep, boop, beep boop...")
    try:
        reading_number(int(input("Enter your limit: ")))
    except Exception as e:
        print("We only accept valid integer numbers...")
    print("Thank you for playing...")


if __name__ == "__main__":
    main()
