# Processing nutritional data with for loops
def analyze_weekly_intake(daily_intakes):
    """Analyze a week's worth of nutritional data"""
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    print("Daily Nutritional Analysis:")
    for day, intake in enumerate(daily_intakes, 1):
        calories = intake['calories']
        protein = intake['protein']
        carbs = intake['carbs']
        fat = intake['fat']
        
        # Calculate percentages
        protein_percent = (protein * 4) / calories * 100
        carbs_percent = (carbs * 4) / calories * 100
        fat_percent = (fat * 9) / calories * 100
        
        print(f"Day {day}: {calories} cal, "
              f"P: {protein_percent:.1f}%, "
              f"C: {carbs_percent:.1f}%, "
              f"F: {fat_percent:.1f}%")
        
        # Accumulate totals
        total_calories += calories
        total_protein += protein
        total_carbs += carbs
        total_fat += fat
    
    # Calculate weekly averages
    avg_calories = total_calories / len(daily_intakes)
    avg_protein = total_protein / len(daily_intakes)
    avg_carbs = total_carbs / len(daily_intakes)
    avg_fat = total_fat / len(daily_intakes)
    
    return {
        'avg_calories': avg_calories,
        'avg_protein': avg_protein,
        'avg_carbs': avg_carbs,
        'avg_fat': avg_fat
    }

# Example weekly data
weekly_data = [
    {'calories': 1850, 'protein': 85, 'carbs': 220, 'fat': 65},
    {'calories': 1920, 'protein': 90, 'carbs': 240, 'fat': 70},
    {'calories': 1780, 'protein': 80, 'carbs': 200, 'fat': 62},
    {'calories': 1900, 'protein': 88, 'carbs': 230, 'fat': 68},
    {'calories': 1750, 'protein': 82, 'carbs': 195, 'fat': 60},
    {'calories': 2000, 'protein': 95, 'carbs': 250, 'fat': 75},
    {'calories': 1800, 'protein': 85, 'carbs': 210, 'fat': 65}
]

averages = analyze_weekly_intake(weekly_data)
print(f"\nWeekly Averages:")
print(f"Calories: {averages['avg_calories']:.0f}")
print(f"Protein: {averages['avg_protein']:.1f}g")
print(f"Carbs: {averages['avg_carbs']:.1f}g")
print(f"Fat: {averages['avg_fat']:.1f}g")
