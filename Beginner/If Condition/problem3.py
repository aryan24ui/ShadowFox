'''Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print 
whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country" '''

city_to_country = {
    "sydney": "Australia",
    "melbourne": "Australia",
    "brisbane": "Australia",
    "perth": "Australia",
    "dubai": "UAE",
    "abu dhabi": "UAE",
    "sharjah": "UAE",
    "ajman": "UAE",
    "mumbai": "India",
    "bangalore": "India",
    "chennai": "India",
    "delhi": "India"
}


city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()


if city1 in city_to_country and city2 in city_to_country:
    if city_to_country[city1] == city_to_country[city2]:
        print(f"Both cities are in {city_to_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found in the list.")
