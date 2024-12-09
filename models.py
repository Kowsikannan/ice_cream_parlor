from database import create_connection

class Flavor:
    @staticmethod
    def add_flavor(name, description, is_seasonal):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO flavors (name, description, is_seasonal) VALUES (?, ?, ?)",
            (name, description, is_seasonal)
        )
        conn.commit()
        conn.close()

class Ingredient:
    @staticmethod
    def add_ingredient(name, stock_level):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ingredients (name, stock_level) VALUES (?, ?)", 
            (name, stock_level)
        )
        conn.commit()
        conn.close()

class Suggestion:
    @staticmethod
    def add_suggestion(flavor_name, allergy_concerns):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO suggestions (flavor_name, allergy_concerns) VALUES (?, ?)", 
            (flavor_name, allergy_concerns)
        )
        conn.commit()
        conn.close()

class Cart:
    @staticmethod
    def add_to_cart(product_id, quantity):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cart (product_id, quantity) VALUES (?, ?)", 
            (product_id, quantity)
        )
        conn.commit()
        conn.close()
