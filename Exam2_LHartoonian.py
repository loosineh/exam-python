from statistics import *
def aveTemp(temp):
    new_list = [(x[0], round((x[1]+x[2]+x[3])/3),2) for x in temp]
    return new_list


def main():
    weekDays = ('Mo', 'Tu', 'We', 'Th', 'Fr')
    am = [72, 75, 68, 69, 70]
    noon = [77, 78, 70, 69, 75]
    pm = [71, 76, 72, 65, 73]
    dailyTemp = list(zip(weekDays,am,noon,pm))
    print(dailyTemp)
    print(aveTemp(dailyTemp))

main()

'''
Test run:
[('Mo', 72, 77, 71), ('Tu', 75, 78, 76), ('We', 68, 70, 72), ('Th', 69, 69, 65), ('Fr', 70, 75, 73)]
[('Mo', 73.33333333333333), ('Tu', 76.33333333333333), ('We', 70.0), ('Th', 67.66666666666667), ('Fr', 72.66666666666667)]
'''