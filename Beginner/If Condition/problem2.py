'''Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"'''    

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

city_name = input("Enter a city name: ").strip().lower()

if city_name in city_to_country:
    print(f"{city_name.title()} is in {city_to_country[city_name]}")
else:
    print("City not found in any country.")
