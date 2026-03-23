def validate_ingredients(ingredients: str) -> str:
    valid_keywords = ["fire", "water", "earth", "air"]

    if any(keyword in ingredients.lower() for keyword in valid_keywords):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
