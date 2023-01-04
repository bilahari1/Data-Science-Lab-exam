import matplotlib.pyplot as plt
year = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
value = [24000, 22500, 19700, 17500, 15600, 12700, 10500]
plt.plot(year, value)
plt.title('Value change per year')
plt.xlabel('Year')
plt.ylabel('Value')
plt.show()