user = {
    "name": "John",
    "age": 23,
    "friends": ["Mike", "Bob", "Joe"],
    "skills": ("HTML", "CSS", "JS"),
}
#print("|user_data|", user)
#print("|user_friends|", user["friends"])
print("|user_age|", user["age"])
#user_age = int(user["age"])
import datetime
current_yaer = datetime.datetime.now().year
print("yaer of user birth", int(current_yaer) - int(user["age"]))

#user_age = input("How old are you ? ")
#import datetime
#current_yaer = datetime.datetime.now().year
#print("year of your birth", int(current_yaer) - int(user_age))

print("Mike" in user)

#if "Mike" in user,
#    best_friend = "Mike"
#    print("Mike best_friend")