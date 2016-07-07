# Learn Python the Hard Way
# Exercise 39 - Dictionary

# Adding and Deleting entries in a dictionary
profile = {"name": "Wayne", "age": 39, "height": 36 * 5}
print profile["name"]
print profile["age"]
print profile["height"]

profile["city"] = "Singapore"
print profile["city"]

profile[1] = "First"
profile[2] = "Second"
print profile[1]
print profile[2]

print profile

del profile["city"]
del profile[1]
del profile[2]

print profile

# Simple dictionary mapping states to its abbreviations and state abbreviations to cities

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Print out some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Do it by using the state then cities dictionary
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s." % (state, abbrev)

# Print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s." % (abbrev, city)

# Now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has the city %s" % (
        state, abbrev, cities[abbrev]
    )

print '-' * 10
# Safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is:  %s." % city
