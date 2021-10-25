from random import choice

fastfood = ["McD", "KFC", "Burger King", "Wendys", "Pizza Hut", 
            "CFC", "BurgerLawe"]

def pick():
    """Return random fast food palce."""
    return choice(fastfood)

print("This is from fastfood.py")
print(fastfood)