# Hannah Hodges
# CS 151, Dr. Rajeev
# Lab 8
# 11/10/2021

import random


def main():
    load_name_list()
    pop_random_name(name)
    print("Do you want to continue? Yes or No:")
    answer = input("")
    if answer == 'Yes':
        name = random.randrange(name)
        while used_names == name:
            name = random.randrange(name)
            print("Random name :", name)
            used_names = name
    if answer == 'No':
        break


def load_name_list():
    file_name = str(input("Enter file name:"))
    opn = open(file_name, 'r')
    file_data = opn.read()
    opn.close()


def pop_random_name(name):
    used_names = ""
    names = ""
    name = random.randrange(name)
    print("Random name :", name)
    used_names = name
    return name

main()



