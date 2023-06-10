"""Aim:Draw the histogram of the following data:
Height of students(m) 135-140 140-145 145-150 150-155
No: of students 4 12 16 8"""

import matplotlib.pyplot as plt
heights = ['135-140', '140-145', '145-150', '150-155']
students = [4, 12, 16, 8]
plt.hist(heights, bins=len(heights), weights=students)
plt.title('Height of Students')
plt.xlabel('Height (in cm)')
plt.ylabel('Number of Students')
plt.show()
