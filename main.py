import time
valid_coin = False 



values = {
    "£2 Coin bag": {
        "bag value (£)": 20.00,
        "weight of one coin (g)": 12.00
    },
    "£1 Coin bag": {
        "bag value (£)": 20.00,
        "weight of one coin (g)": 8.75
    },
    "£0.50 Coin bag": {
        "bag value (£)": 10.00,
        "weight of one coin (g)": 8.00
    },
    "£0.20 Coin bag": {
        "bag value (£)": 10.00,
        "weight of one coin (g)": 5.00
    },
    "£0.10 Coin bag": {
        "bag value (£)": 5.00,
        "weight of one coin (g)": 6.50
    },
    "£0.05 Coin bag": {
        "bag value (£)": 5.00,
        "weight of one coin (g)": 3.25
    },
    "£0.02 Coin bag": {
        "bag value (£)": 1.00,
        "weight of one coin (g)": 7.12
    },
    "£0.01 Coin bag": {
        "bag value (£)": 1.00,
        "weight of one coin (g)": 3.56
    }
}



with open("CoinCount.txt", "r") as STORAGE_TXT:
    PRINT_STORED = STORAGE_TXT.read()

names = []

for line in PRINT_STORED.splitlines():
    parts = line.split(" - ")

    name = parts[0]
    coin_type = parts[1]
    weight_of_bag = parts[2]

    names.append((name, coin_type, weight_of_bag))

names.sort()
number = 1



time.sleep(0.25)
print()
print("1 - Add a new data")
print("2 - Show table")
print("3 - Remove data")
print()
time.sleep(0.50)

user_input = input("Please select your chosen option: ")
print()

if user_input == "1":
    time.sleep(0.25)
    print()
    name_input = input("Please enter your name: ")
    print()
    while (not valid_coin):
        coin_input = input("Please enter your coin type: ")
        print()
        if f"{coin_input} Coin bag" in values:
            print("Valid coin type!")
            valid_coin = True
        else:
            print("Invalid coin type!")
            print()
            valid_coin = False 

    print()
    weight_input_int = int(input("Please enter weight of the bag: "))  # makes it so users can only input numbers(int) for weight 
    weight_input = str(weight_input_int)  # converts the weight from a int to a str so it can be written into the txt file
    print()

    with open("CoinCount.txt", "a") as STORAGE_TXT:
        STORAGE_TXT.write(name_input + " - " + coin_input + " - " + weight_input + "\n")

elif user_input == "2":
    print(f"| {'No.':<4} | {'Name':<18} | {'Coin Type':<12} | {'Weight of Bag (g)':<15} |")
    print("-" * 64)

    for name, coin_type, weight_of_bag in names:
        print(f"| {number:<4} | {name:<18} | {coin_type:<12} | {weight_of_bag:<15} |")
        number += 1

elif user_input == "3":
    print(f"| {'No.':<4} | {'Name':<18} | {'Coin Type':<12} | {'Weight of Bag (g)':<15} |")
    print("-" * 64)
    
    for name, coin_type, weight_of_bag in names:
        print(f"| {number:<4} | {name:<18} | {coin_type:<12} | {weight_of_bag:<15} |")
        number += 1

    print()
    num_selection = int(input("Enter the number of the data to remove: "))
    remove_data = names[num_selection -1]
    names.remove(remove_data)

    with open("CoinCount.txt", "w") as STORAGE_TXT:
        for name, coin_type, weight_of_bag in names:
            STORAGE_TXT.write(f"{name} - {coin_type} - {weight_of_bag}\n")
            print("Data successfully removed!")
            print()
