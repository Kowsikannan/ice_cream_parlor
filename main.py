from database import create_connection, create_tables
from models import Flavor, Ingredient, Suggestion, Cart

def main():
    # Ensure tables are created (if running for the first time)
    create_tables()

    while True:
        print("\nIce Cream Parlor Menu:")
        print("1. Add Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. Add to Cart")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter flavor name: ")
            description = input("Enter description: ")
            is_seasonal = input("Is it seasonal? (yes/no): ").lower() == "yes"
            Flavor.add_flavor(name, description, is_seasonal)
            print("Flavor added successfully!")

        elif choice == "2":
            name = input("Enter ingredient name: ")
            stock_level = int(input("Enter stock level: "))
            Ingredient.add_ingredient(name, stock_level)
            print("Ingredient added successfully!")

        elif choice == "3":
            flavor_name = input("Enter suggested flavor: ")
            allergy_concerns = input("Enter allergy concerns: ")
            Suggestion.add_suggestion(flavor_name, allergy_concerns)
            print("Suggestion submitted!")

        elif choice == "4":
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            Cart.add_to_cart(product_id, quantity)
            print("Added to cart!")

        elif choice == "5":
            print("Thank you for using the Ice Cream Parlor system!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
