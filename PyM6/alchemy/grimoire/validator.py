def validate_ingredients(ingredients: str) -> str:
    valid_keywords = ["fire", "water", "earth", "air"]

    for keyword in valid_keywords:
        if keyword in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
