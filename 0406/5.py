#5번
logs = [
    ("user1", "login"),
    ("user2", "login"),
    ("user1", "view"), 
    ("user1", "logout"),
    ("user2", "view"), 
    ("user2", "logout"), 
    ("user1", "login"), 
]

user1Count = 0 
user2Count = 0 

for i in range(7):
    user, action = logs[i]

    if user == "user1":
        user1Count += 1

    elif user == "user2":
        user2Count += 1

a = {'user1' : user1Count, 'user2' : user2Count}
print(a)

if user1Count > user2Count:
    b = 'user1'
    print(b)
    print([b])

else:
    c = 'use2'
    print(c)
    print([c])