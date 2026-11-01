
import random
import datetime


# Generate one random birthday
def getBirthday():
    start = datetime.date(2001, 1, 1)
    random_days = datetime.timedelta(days=random.randint(0, 364))
    birthday = start + random_days
    return birthday


# Find a matching birthday
def getMatch(birthdays):
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]

    return None


# Generate 23 random birthdays
birthdays = []

for i in range(23):
    birthdays.append(getBirthday())


# Display all birthdays
print("Here are 23 birthdays:")

for birthday in birthdays:
    print(birthday)


# Check for matching birthdays
match = getMatch(birthdays)

if match is not None:
    print("Matching birthday found:", match)
else:
    print("No matching birthdays")


print("Total birthdays:", len(birthdays))
