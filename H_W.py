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
#   "best_friend" = user["friends" : "Mike"] 
#    best_friend = ("Mike")
#    print("best_friend")
     print("Mike best_friend")

user["skills"] = ["Python", "QA", "Selenium"]
print("|user_data|", user)

user["friends"] = sorted(user["friends"])
print(user)

print(user["friends"].index("Bob"))

new_friends = {
    "friends": ["Taras", "Danya", "Bidden"]
}
print(new_friends)

#user["friends"] = user.update({"friends" : "Taras", "Danya", "Bidden"})
#print("user")
#prin(user["skills"])

print(len(user["skills"]))