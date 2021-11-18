# Hannah Hodges
# CS 151, Dr. Rajeev
# Lab 8
# 11/10/2021

import random


def main():
    load_name_list()
    pop_random_name(names)
    while 1:
        print("Do you want to continue? Yes or No:")
        choice = input("")
        if choice == 'No':
            break
        if choice == 'Yes':
            name = random.choice(names)
            while used_names == name:
                name = random.choice(names)
                print("Random name :", name)
                used_names = name

def load_name_list():
    file_name = str(input("Enter file name:"))
    opn = open(file_name, 'r+')
    file_data = opn.read()
    opn.close()
    names = file_data.split("\n")


def pop_random_name(names):
    used_names = ""
    name = ""
    name = random.choice(names)
    print("Random name :", name)
    used_names = name






main()



