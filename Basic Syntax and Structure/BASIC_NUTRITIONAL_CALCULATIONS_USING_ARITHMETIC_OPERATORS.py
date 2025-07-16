# Basic nutritional calculations using arithmetic operators
def calculate_daily_needs(weight, activity_factor):
    # Addition: Basic calorie calculation
    base_calories = 1200
    additional_calories = weight * 15
    total_calories = base_calories + additional_calories
    
    # Multiplication: Adjust for activity level
    adjusted_calories = total_calories * activity_factor
    
    # Division: Calculate meal distribution
    calories_per_meal = adjusted_calories / 3
    
    # Subtraction: Account for snacks
    snack_calories = 400
    main_meal_calories = adjusted_calories - snack_calories
    
    # Exponentiation: Calculate BMI
    height = 1.70  # meters
    bmi = weight / (height ** 2)
    
    # Modulo: Check if even number of meals
    meal_count = 6
    has_even_meals = meal_count % 2 == 0
    
    return {
        'total_calories': adjusted_calories,
        'calories_per_meal': calories_per_meal,
        'bmi': bmi,
        'even_meals': has_even_meals
    }

# Example calculation
results = calculate_daily_needs(70, 1.6)
print(f"Daily calorie needs: {results['total_calories']:.0f}")
print(f"BMI: {results['bmi']:.1f}")
