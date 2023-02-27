user = {
    "name": "John",
    "age": 23,
    "friends": ["Mike", "Bob", "Joe"],
    "skills": ("HTML", "CSS", "JS"),
}
print("|user_data|", user)
#print("|user_friends|", user["friends"])
print("|user_age|", user["age"])
import datetime
current_yaer = datetime.datetime.now().year
print("yaer of user birth", int(current_yaer) - int(user["age"]))

#print("Mike" in user)

if "Mike" in user["friends"]:
    print("Mike best_friend")
    best_friend = "Mike"
#print(best_friend)

user["skills"] = ["Python", "QA", "Selenium"]
print("|user_data|", user)

user["friends"] = sorted(user["friends"])
#print(user)

print("|index_Bob|", user["friends"].index("Bob"))

#new_friends = "Taras", "Dania", "Bidden"
#print(new_friends)
#user["friends"].append(new_friends)
#print(user)

user["friends"].append("Taras")
user["friends"].append("Dania")
user["friends"].append("Bidden")
print("|user_new_data|", user)

#prin(user["skills"])
print("|number_of_user_skills|", len(user["skills"]))