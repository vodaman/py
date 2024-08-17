buildings_db = ["home1", "home2", "home3"]
clients_db = ["Amy", "Emma", "Jack"]
price = 200000

with open("main.txt", "w", encoding="UTF-8") as f:
    for i in range(len(clients_db)):
        f.write(f"{clients_db[i]} wants {buildings_db[i]}!\n")

f = open("main.txt", "a")
while True:
    if input("do you want to add more clients? (y/n) ").lower() == "y":
        new_client = input("What is your name? ")
        new_home = input("What house do you want? ")
        if new_home in buildings_db:
            print(f"sorry {new_client}, the home is already reserved.")
        else:
            f.write(f"{new_client} wants a {new_home}! The market is growing! The house costs {price}.\n")
            price += 20000
    else:
        break

f.close()
f = open("main.txt", "r", encoding="UTF-8")
for line in f:
    print(line, end="\n")
