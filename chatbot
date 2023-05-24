def greet():
    print("Hello! Welcome to our fruit shop. How can I assist you today?")

def get_fruit():
    fruits = ["apple", "banana", "orange", "grape", "watermelon"]
    fruit = input("Which fruit would you like to buy? ")
    fruit = fruit.lower()
    while fruit not in fruits:
        print("Sorry, we don't have that fruit. Please choose from the available options.")
        fruit = input("Which fruit would you like to buy? ")
        fruit = fruit.lower()
    return fruit

def get_quantity():
    quantity = input("How many fruits would you like to buy? ")
    while not quantity.isdigit() or int(quantity) <= 0:
        print("Please enter a valid quantity.")
        quantity = input("How many fruits would you like to buy? ")
    return int(quantity)

def calculate_price(fruit, quantity):
    prices = {"apple": 0.5, "banana": 0.3, "orange": 0.4, "grape": 0.8, "watermelon": 2.0}
    price = prices[fruit] * quantity
    return price

def main():
    greet()
    fruit = get_fruit()
    quantity = get_quantity()
    price = calculate_price(fruit, quantity)
    print(f"The total price for {quantity} {fruit}(s) is ${price:.2f}.")
    print("Thank you for shopping with us!")

# Run the chatbot
main()
