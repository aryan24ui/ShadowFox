'''In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using 
the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in 
the pond = Pond Area Water per Square Meter'''

pi=3.14
radius=84
area=(pi)*(radius**2)
print("Area of the pond is:", area)
#bonus question
water_in_pond=area*1.4
print("Total amount of water in the pond is:", int(water_in_pond))