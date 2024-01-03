populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 13, "name" : "Brice" },
    { "id" : 14, "name" : "Alice" },
    { "id" : 15, "name" : "Sophia" },
    { "id" : 16, "name" : "Rasmus" },
    { "id" : 18, "name" : "Taylor" },
    { "id" : 19, "name" : "Olivia" },
    { "id" : 20, "name" : "Jessica" },
    { "id" : 21, "name" : "Anna" },
    { "id" : 22, "name" : "Samantha" },
    { "id" : 23, "name" : "Grace" },
    { "id" : 24, "name" : "Anna" },
    { "id" : 25, "name" : "Alexis" },
    { "id" : 26, "name" : "Madison" },
    { "id" : 27, "name" : "Nicole" },
    { "id" : 28, "name" : "Amanda" },
    { "id" : 29, "name" : "Haley" }  
]

print(len(populations))
# question 1
for person in populations:
    person["lenChar"] = len(person["name"])

# question 2
from random import randint

for person in populations:
    person["rate"] = randint(1, 100)

# question 3
fourbestRate = []
def getFourBestRate():
    for i in range(100, 1, -1):
        for person in populations:
            if(person["rate"] == i): fourbestRate.append(person)
            if(len(fourbestRate) == 4): break

getFourBestRate()
print(fourbestRate)

# question 4
def increaseRate():
    for person in  populations:
        person["rate"] = round(person["rate"] * (1 + 0.1), 2)

increaseRate()
#print(populations)

# question 5
def getRandomPerson(): 
    person = populations[randint(0, len(populations)-1)]
    return person

print(getRandomPerson())

# question 6
def sortPopulations():
    s = sorted(populations, key=lambda person: person["rate"])
    return s
populations = sortPopulations()
print(list(map(lambda person: (person["name"], person["rate"]), populations)))

# question 7
from statistics import median
def getMedianValue(popList):
    values = []
    for person in popList:
        values.append(person["rate"])
    medianVal = median(values)
    return medianVal

mediane = getMedianValue(populations)
#print(mediane)

# question 8
def partition(med, popList):
    p1, p2 = [], []
    for person in popList:
        if med <= person["rate"]: p1.append(person)
        else: p2.append(person)
    return p1, p2

#calcul des 2 premières parties
p2, p1 = partition(mediane, populations)
#calcul des médianes respectives de p1 et p2
m1 = getMedianValue(p1)
m2 = getMedianValue(p2)

p1_1, p1_2 = partition(m1, p1)
p2_1, p2_2 = partition(m2, p2)

print("================================")
print(p1_2)
print("========= \n")
print(p1_1)
print("========= \n")
print(p2_2)
print("========= \n")
print(p2_1)
