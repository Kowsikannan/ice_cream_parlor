# Ice Cream Parlor Management Application  

## Overview
A simple Python application using SQLite to manage ice cream flavors, ingredients, and customer suggestions.

## Setup Instructions

### 1. Clone the repository:
Clone this repository to your local machine using the following command:
https://github.com/Kowsikannan/ice_cream_parlor.git


### 2. Install dependencies:
Make sure you have Python 3.x installed on your machine. Then, install the required packages by running:


### 3. Run the application:
You can run the application using the following command:python main.py


The application will allow you to:
- Add and manage ice cream flavors.
- Manage ingredient stock levels.
- Add customer suggestions.
- Add products to the cart.

## Docker Setup:
See the **Docker Setup** section for building and running the app in a container.

### Build Docker Image:
To build the Docker image for the application, run the following command:docker build -t ice_cream_parlor 


### Run Docker Container:
To run the application in a Docker container, use the following command:docker run -t ice_cream_parlor 


## Testing

Here are the steps to validate the application:

### 1. Test Flavor Addition:
- Run the application.
- Choose option `1` to add a new flavor.
- Verify that the flavor is added by checking the database or querying the `flavors` table.

### 2. Test Ingredient Addition:
- Choose option `2` to add a new ingredient.
- Verify that the ingredient is added by checking the `ingredients` table.

### 3. Test Customer Suggestion:
- Choose option `3` to add a customer suggestion.
- Verify that the suggestion appears in the `suggestions` table.

### 4. Test Cart Addition:
- Choose option `4` to add a product to the cart.
- Verify that the product and quantity are correctly added to the `cart` table.

### 5. Test Exit:
- Choose option `5` to exit the application.
- Ensure that the application exits correctly without errors.
