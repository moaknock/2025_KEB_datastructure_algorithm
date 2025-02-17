# import numpy as np
#
# narray = np.array[1,3.1,2,9]
# print(type(narray),type(narray[2],type(narray[3])))
#
# array = [9,-11,'8',7]
# print(array[0],array[1],array[2],array[3])
# print(type(array),type(array[2]),type(array[3]))
# print(id(array[0],id(array[1]),id(array[2]),id(array[3])))

import random

students = []

try:
    file = input("File name : ")
    fp = open(file, 'r')
    readme_list = fp.readline()
    rls = readme_list = list[0].split('_')
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f"{file} is not exist.{err}")