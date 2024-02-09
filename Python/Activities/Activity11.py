fruit_shop = {
    "apple": 100,
    "banana": 15,
    "orange": 82,
    "peaches": 15
}

Fruitname = input("What are you looking for? ").lower()

if(Fruitname in fruit_shop):
    print("Yes, this is available")
else:
    print("No, this is not available")