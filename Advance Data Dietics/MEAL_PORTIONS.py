import math

# Using math module for nutritional calculations
def calculate_meal_portions(total_servings, people_count):
    """Calculate meal portions with mathematical precision"""
    
    # Basic division
    base_portion = total_servings / people_count
    
    # Round up to ensure everyone gets enough
    portion_rounded_up = math.ceil(base_portion)
    
    # Round down for conservative estimates
    portion_rounded_down = math.floor(base_portion)
    
    # Standard rounding
    portion_rounded = round(base_portion, 2)
    
    # Calculate percentage of daily value
    daily_value_percentage = (base_portion / 8) * 100  # Assuming 8 servings per day
    
    return {
        'exact_portion': base_portion,
        'conservative_portion': portion_rounded_down,
        'generous_portion': portion_rounded_up,
        'standard_portion': portion_rounded,
        'daily_value_percent': round(daily_value_percentage, 1)
    }

# Advanced calculations using math functions
def calculate_nutrient_absorption_rate(initial_amount, time_hours, half_life_hours):
    """Calculate nutrient absorption using exponential decay"""
    
    # Exponential decay formula: A = A₀ * e^(-λt)
    # where λ = ln(2) / half_life
    decay_constant = math.log(2) / half_life_hours
    remaining_amount = initial_amount * math.exp(-decay_constant * time_hours)
    
    return {
        'initial_amount': initial_amount,
        'remaining_amount': round(remaining_amount, 2),
        'absorbed_amount': round(initial_amount - remaining_amount, 2),
        'absorption_percentage': round(((initial_amount - remaining_amount) / initial_amount) * 100, 1)
    }

# Example calculations
portion_results = calculate_meal_portions(24, 6)
print("Meal Portion Calculations:")
print(f"Exact portion per person: {portion_results['exact_portion']:.2f}")
print(f"Recommended portion: {portion_results['generous_portion']}")
print(f"Daily value percentage: {portion_results['daily_value_percent']}%")

# Vitamin absorption example
vitamin_absorption = calculate_nutrient_absorption_rate(1000, 4, 6)
print(f"\nVitamin Absorption after 4 hours:")
print(f"Absorbed: {vitamin_absorption['absorbed_amount']}mg ({vitamin_absorption['absorption_percentage']}%)")
