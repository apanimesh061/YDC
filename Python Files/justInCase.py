import json
import sys
from pprint import pprint

option = input("Enter the option number: ")

temp = []
all_categories = []
all_set = []

if option == 1:
    file1 = open('allRestCategories.dat', 'w+')

    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            all_categories.append(json_data['categories'])

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        file1.write(c + "\n")

    file1.close()

elif option == 2:
    file1 = open('allRestAttributes.dat', 'w+')

    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            all_categories.append(json_data['attributes'].keys())

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        file1.write(c + "\n")

    file1.close()

elif option == 3:
    file1 = open('allRestAttributes_Music.dat', 'w+')
    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            try:
                all_categories.append(json_data['attributes']['Music'].keys())
            except:
                pass

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        file1.write(c + "\n")

    file1.close()

elif option == 4:
    file1 = open('allRestAttributes_Ambience.dat', 'w+')

    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            try:
                all_categories.append(json_data['attributes']['Ambience'].keys())
            except:
                pass

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        file1.write(c + "\n")

    file1.close()

elif option == 5:
    file1 = open('allRestAttributes_GoodFor.dat', 'w+')

    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            try:
                all_categories.append(json_data['attributes']['Good For'].keys())
            except:
                pass

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        if c != 'none':
            file1.write(c + "\n")

    file1.close()

elif option == 6:
    file1 = open('allRestAttributes_Parking.dat', 'w+')

    with open('business.json') as f:
        for l in f:
            line = l.strip()
            json_data = json.loads(line)
            temp.append(line)
            try:
                all_categories.append(json_data['attributes']['Parking'].keys())
            except:
                pass

    set_of_all_categories = set(sum(all_categories, []))

    for c in set_of_all_categories:
        if c != 'none':
            file1.write(c + "\n")

    file1.close()

else:
    pass
