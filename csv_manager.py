"""
	This module update history list csv for $LINE_NUMBER elements
	Is putting the new element preppend in list
"""
import csv
PATH = 'src/static/historique.csv'
LINE_NUMBER = 20

def update_csv_history(newLine):
    """preppend newLine in list"""
    the_file = open(PATH, 'r')
    reader = csv.reader(the_file)
    i = 0
    tab = []
    for row in reader:
        if i == 0:
            print("entete")
            print(row)
            entete = row

        if 0 < i < LINE_NUMBER:
            print(row)
            tab.append(row)
        i = i+1

    the_file.close()
    print(entete)
    print(tab)


    the_file = csv.writer(open(PATH, "w"))
    the_file.writerow(entete)
    the_file.writerow(newLine)
    print(len(tab))
    for i in range(len(tab)):
        the_file.writerow(tab[i])


if __name__ == '__main__':
    NEW = ["T3", "02/03", "25:25", "9", "1", "1", "d1024", "d256", "d64", "final", "bina", "V1"]
    update_csv_history(NEW)

