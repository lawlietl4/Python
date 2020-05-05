# take in at least three inputs that are at least two different data types
# prompt the user for the necessary values, read it and and convert it to the correct type
name = str(input("What name do you want to use? "))
thing = str(input("What did you buy at the store? "))
age = int(input("Tell me the age you want to use "))
numFriends = int(input("How many friends do you want? "))
time = float(
    input("What time is the party? (float input) "))
verb = str(input("Please give me a verb "))
verb1 = str(input("Please give another verb "))
noun = str(input("Give me a person, place or thing "))
noun1 = str(input("Please give another person, place or thing "))

paragraph = f"""
One day {name} went to the store to get {thing} for their {age}th birthday.
They invited {numFriends} friends to their birthday party.
{name} must be back at their house by {time:.2f} to be on time for their party.
When {name} opened their presents they were so {verb} to see a {noun} in the first present.
In the next present was a {noun1} and they were so {verb1}.
"""
print(paragraph)
