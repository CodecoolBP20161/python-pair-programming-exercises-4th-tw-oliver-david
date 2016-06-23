import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name) as csvfile:
        phone_numbers = csv.reader(csvfile)
        person_list = []
        for numbers in phone_numbers:
            person_list.append(Person(numbers[0], numbers[1]))
    return person_list


def get_csv_file_name(argv_list):
    try:
        return argv_list[1]
    except:
        return None


def format_output(person):
    if person is None:
        return "No match found."
    else:
        return "This number belongs to: %s" % person.get_name()


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if person.is_phone_number_matching(user_input_phone_number):
            return person


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
