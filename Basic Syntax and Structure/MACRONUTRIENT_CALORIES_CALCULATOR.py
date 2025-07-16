# Basic function structure for nutritional calculations
def calculate_macronutrient_calories(protein_grams, carb_grams, fat_grams):
    """
    Calculate total calories from macronutrients
    
    Parameters:
    protein_grams (float): Grams of protein
    carb_grams (float): Grams of carbohydrates
    fat_grams (float): Grams of fat
    
    Returns:
    dict: Breakdown of calories by macronutrient
    """
    protein_calories = protein_grams * 4
    carb_calories = carb_grams * 4
    fat_calories = fat_grams * 9
    total_calories = protein_calories + carb_calories + fat_calories
    
    return {
        'protein_calories': protein_calories,
        'carb_calories': carb_calories,
        'fat_calories': fat_calories,
        'total_calories': total_calories
    }

# Example usage
meal_macros = calculate_macronutrient_calories(25, 45, 15)
print(f"Total calories: {meal_macros['total_calories']}")
print(f"Protein: {meal_macros['protein_calories']} calories")
