# Function with default parameters for meal planning
def create_meal_plan(calories_per_day, meals_per_day=3, snacks_per_day=2, 
                    protein_percentage=0.20, carb_percentage=0.50, fat_percentage=0.30):
    """
    Create a balanced meal plan with flexible parameters
    
    Parameters:
    calories_per_day (int): Total daily calories
    meals_per_day (int): Number of main meals (default: 3)
    snacks_per_day (int): Number of snacks (default: 2)
    protein_percentage (float): Percentage of calories from protein (default: 0.20)
    carb_percentage (float): Percentage of calories from carbs (default: 0.50)
    fat_percentage (float): Percentage of calories from fat (default: 0.30)
    
    Returns:
    dict: Detailed meal plan structure
    """
    # Validate percentages
    if protein_percentage + carb_percentage + fat_percentage != 1.0:
        raise ValueError("Macronutrient percentages must sum to 1.0")
    
    # Calculate calories per meal and snack
    snack_calories = 150  # Fixed snack calories
    total_snack_calories = snacks_per_day * snack_calories
    meal_calories = (calories_per_day - total_snack_calories) / meals_per_day
    
    # Calculate macronutrients for main meals
    meal_protein_calories = meal_calories * protein_percentage
    meal_carb_calories = meal_calories * carb_percentage
    meal_fat_calories = meal_calories * fat_percentage
    
    # Convert to grams
    meal_protein_grams = meal_protein_calories / 4
    meal_carb_grams = meal_carb_calories / 4
    meal_fat_grams = meal_fat_calories / 9
    
    # Snack macronutrients (balanced approach)
    snack_protein_grams = (snack_calories * 0.15) / 4
    snack_carb_grams = (snack_calories * 0.60) / 4
    snack_fat_grams = (snack_calories * 0.25) / 9
    
    meal_plan = {
        'daily_totals': {
            'calories': calories_per_day,
            'protein': round((meal_protein_grams * meals_per_day) + 
                           (snack_protein_grams * snacks_per_day), 1),
            'carbohydrates': round((meal_carb_grams * meals_per_day) + 
                                 (snack_carb_grams * snacks_per_day), 1),
            'fat': round((meal_fat_grams * meals_per_day) + 
                        (snack_fat_grams * snacks_per_day), 1)
        },
        'main_meals': {
            'count': meals_per_day,
            'calories_per_meal': round(meal_calories, 0),
            'protein_grams': round(meal_protein_grams, 1),
            'carb_grams': round(meal_carb_grams, 1),
            'fat_grams': round(meal_fat_grams, 1)
        },
        'snacks': {
            'count': snacks_per_day,
            'calories_per_snack': snack_calories,
            'protein_grams': round(snack_protein_grams, 1),
            'carb_grams': round(snack_carb_grams, 1),
            'fat_grams': round(snack_fat_grams, 1)
        }
    }
    
    return meal_plan

# Example meal plans with different parameters
standard_plan = create_meal_plan(2000)
high_protein_plan = create_meal_plan(2000, protein_percentage=0.30, 
                                   carb_percentage=0.40, fat_percentage=0.30)
frequent_meals = create_meal_plan(2000, meals_per_day=4, snacks_per_day=1)

print("=== Standard Meal Plan ===")
print(f"Main meals: {standard_plan['main_meals']['count']} x {standard_plan['main_meals']['calories_per_meal']} calories")
print(f"Snacks: {standard_plan['snacks']['count']} x {standard_plan['snacks']['calories_per_snack']} calories")
print(f"Daily protein: {standard_plan['daily_totals']['protein']}g")

print("\n=== High Protein Meal Plan ===")
print(f"Daily protein: {high_protein_plan['daily_totals']['protein']}g")
print(f"Daily carbs: {high_protein_plan['daily_totals']['carbohydrates']}g")
