# List of 5 cities
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Hyderabad"]

# Print middle city
print(cities[2])

# Print first 3 cities
print(cities[:3])

# Sort and print
cities.sort()
print(cities)

# Add a new city
cities.append("Bangalore")
print(cities)

# Remove first city
cities.pop(0)
print(cities)

# Function to find length of list
def count_cities(city_list):
    return len(city_list)

# Test function
print(count_cities(cities))