#practicing with python
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of countries.")

print("-------")

#practicing ifel
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

print("-------")

#practicing while loops
x = 0
while x<= 5:
    print(x)
    x = x + 1

print("------")

#Hello World
count = 7
while count < 1:
    print("Yo World")

# Iterate through lists and tuples
for county in counties:
    print(counties)

# Counties dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

print("now with the keys function")

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

print("-------")

for county in counties_dict:
    print(counties_dict.get(county))

print("------")

for county, voters in counties_dict.items():
    print("county, voters")

# Print the name of the county pus the registered votes they have
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

print("------")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("------")

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

print("------")

# Using f-strings with dictionaries
## Preliminary example before using f-strings with dictionaries
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

## Now, compare this to the previous example
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of tht total votes. ")

print(message_to_candidate)