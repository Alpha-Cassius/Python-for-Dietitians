# Advanced function for comprehensive nutritional assessment
def comprehensive_nutrition_assessment(weight, height, age, gender, activity_level, health_conditions=None):
    """
    Comprehensive nutritional assessment and recommendations
    
    Parameters:
    weight (float): Weight in kg
    height (float): Height in meters
    age (int): Age in years
    gender (str): 'male' or 'female'
    activity_level (str): 'sedentary', 'light', 'moderate', 'active', 'very_active'
    health_conditions (list): List of health conditions
    
    Returns:
    dict: Complete nutritional assessment
    """
    if health_conditions is None:
        health_conditions = []Benedict
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Calculate BMR using Harris- equation
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    
    # Activity multipliers
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }
    
    # Calculate total daily energy expenditure
    tdee = bmr * activity_multipliers.get(activity_level, 1.2)
    
    # Macronutrient recommendations
    protein_per_kg = 0.8  # Default protein requirement
    if 'diabetes' in health_conditions:
        protein_per_kg = 1.0
    elif 'kidney_disease' in health_conditions:
        protein_per_kg = 0.6
    
    protein_grams = weight * protein_per_kg
    protein_calories = protein_grams * 4
    
    # Carbohydrate recommendations (45-65% of calories)
    carb_percentage = 0.50  # Default 50%
    if 'diabetes' in health_conditions:
        carb_percentage = 0.45  # Lower for diabetes
    
    carb_calories = tdee * carb_percentage
    carb_grams = carb_calories / 4
    
    # Fat recommendations (20-35% of calories)
    fat_percentage = 0.30
    if 'heart_disease' in health_conditions:
        fat_percentage = 0.25  # Lower for heart disease
    
    fat_calories = tdee * fat_percentage
    fat_grams = fat_calories / 9
    
    # BMI classification
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal weight"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"
    
    # Compile results
    assessment = {
        'bmi': round(bmi, 1),
        'bmi_category': bmi_category,
        'bmr': round(bmr, 0),
        'tdee': round(tdee, 0),
        'macronutrients': {
            'protein': {
                'grams': round(protein_grams, 1),
                'calories': round(protein_calories, 0),
                'percentage': round((protein_calories / tdee) * 100, 1)
            },
            'carbohydrates': {
                'grams': round(carb_grams, 1),
                'calories': round(carb_calories, 0),
                'percentage': round((carb_calories / tdee) * 100, 1)
            },
            'fat': {
                'grams': round(fat_grams, 1),
                'calories': round(fat_calories, 0),
                'percentage': round((fat_calories / tdee) * 100, 1)
            }
        },
        'health_considerations': health_conditions
    }
    
    return assessment

# Example comprehensive assessment
client_assessment = comprehensive_nutrition_assessment(
    weight=70,
    height=1.65,
    age=35,
    gender='female',
    activity_level='moderate',
    health_conditions=['diabetes']
)

print("=== Comprehensive Nutritional Assessment ===")
print(f"BMI: {client_assessment['bmi']} ({client_assessment['bmi_category']})")
print(f"Daily Calorie Needs: {client_assessment['tdee']:.0f} calories")
print("\nMacronutrient Recommendations:")
for macro, values in client_assessment['macronutrients'].items():
    print(f"{macro.capitalize()}: {values['grams']}g ({values['percentage']}%)")
