# Boolean variables for dietary tracking
is_vegetarian = True
has_diabetes = False
meets_calorie_goal = True
exceeds_sodium_limit = False

# Using booleans in nutritional assessment
def recommend_meal_plan(is_vegetarian, has_diabetes):
    if is_vegetarian and has_diabetes:
        return "Plant-based, low-glycemic meal plan"
    elif is_vegetarian:
        return "Balanced vegetarian meal plan"
    elif has_diabetes:
        return "Diabetic-friendly meal plan"
    else:
        return "Standard balanced meal plan"

recommendation = recommend_meal_plan(True, False)
print(f"Meal plan recommendation: {recommendation}")
