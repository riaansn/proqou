#! /usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, date


def read_file(file):
    """Reading file with error checking.

    Parameters: file string: filename and extention.
    Returns: list: containing file lines as list items.

    """
    try:
        with open(file) as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"No file named: {file} was found!")
    return []


def clean_data(file_list):
    """clean data separates data at the deliminator and strips string quotes

    Parameters: list - list of lines read from file
    Returns: list of tuples
    """
    clean_list = []
    for item in file_list:
        name, dob = item.split("|")
        clean_list.append((name.strip('"'), dob.strip('"\n')))
    return clean_list


def calculate_avg_age(file_list):
    """Calculates the average age of individuals in file

    Parameters:
        file_list list: includes name and date of birth.

    Returns:
        int: average age from dates in the file.
    """
    total_age = 0
    clean_list = clean_data(file_list)
    for item in clean_list:
        total_age += calculate_age(item[1])
    return total_age // len(file_list)


def calculate_age(file_item):
    """Calculates age from string provided.

    Args:
        file_item string: date of birth.

    Returns:
        int: age calculated for date of birth.
    """
    item_date = datetime.strptime(file_item, "%Y-%m-%d").date()
    return int(date.today().year - item_date.year)


def main():
    print("Welcome to calculate average age file reader...")
    file_name = input("Please enter the filename that contains your data: ")
    file_list = read_file(file_name)
    if not file_list:
        print(
            "The file is either empty or does not exist, please try again with another file."
        )
        return
    avg_age = calculate_avg_age(file_list)
    print(f"The average age of individuals in the file is: {avg_age}")


if __name__ == "__main__":
    main()
