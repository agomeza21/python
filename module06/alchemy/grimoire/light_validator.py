'#alchemy/grimoire/light_validator.py'


def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    ingredients_lower = ingredients.lower()
    for ingredient in allowed:
        if ingredient in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
