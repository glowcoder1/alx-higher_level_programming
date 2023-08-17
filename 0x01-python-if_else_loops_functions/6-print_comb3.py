#!/usr/bin/python3

for i in range(9):
     print(" ".join("{},".format(str(i) + str(j)) for j in range(i + 1, 10)), end=" ")
print("")
