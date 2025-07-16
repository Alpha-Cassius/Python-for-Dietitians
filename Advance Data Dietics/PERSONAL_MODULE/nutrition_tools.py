# Save this as 'nutrition_tools.py'
"""
Custom nutrition tools module for dietitians
Contains commonly used nutritional calculations and assessments
"""

import math

def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index"""
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_ideal_weight_range(height_m):
    """Calculate ideal weight range based on BMI 18.5-24.9"""
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight

def calculate_daily_water_needs(weight_kg, activity_level='moderate'):
    """Calculate daily water needs based on weight and activity"""
    base_water = weight_kg * 30  # 30ml per kg body weight
    
    activity_multipliers = {
        'low': 1.0,
        'moderate': 1.2,
        'high': 1.5
    }
    
    multiplier = activity_multipliers.get(activity_level, 1.2)
    return base_water * multiplier

def calculate_protein_needs(weight_kg, activity_level='moderate', age=30):
    """Calculate protein needs based on various factors"""
    base_protein = 0.8  # RDA for adults
    
    if activity_level == 'high':
        base_protein = 1.2
    elif activity_level == 'very_high':
        base_protein = 1.6
    
    # Adjust for age (older adults need more protein)
    if age >= 65:
        base_protein += 0.2
    
    return weight_kg * base_protein

# Example of using the custom module
if __name__ == "__main__":
    # This code runs when the module is executed directly
    print("Nutrition Tools Module Test")
    
    # Test calculations
    weight = 70  # kg
    height = 1.75  # meters
    
    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)
    ideal_range = calculate_ideal_weight_range(height)
    water_needs = calculate_daily_water_needs(weight, 'moderate')
    protein_needs = calculate_protein_needs(weight, 'moderate', 35)
    
    print(f"BMI: {bmi:.1f} ({bmi_category})")
    print(f"Ideal weight range: {ideal_range[0]:.1f} - {ideal_range[1]:.1f} kg")
    print(f"Daily water needs: {water_needs:.0f} ml")
    print(f"Daily protein needs: {protein_needs:.1f} g")
