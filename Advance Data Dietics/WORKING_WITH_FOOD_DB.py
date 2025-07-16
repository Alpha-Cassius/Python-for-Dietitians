import csv
import os

# Working with CSV files for nutritional data
def create_food_database():
    """Create a sample food database CSV file"""
    
    foods_data = [
        ['Food Item', 'Calories per 100g', 'Protein (g)', 'Carbs (g)', 'Fat (g)', 'Fiber (g)'],
        ['Chicken Breast', 165, 31.0, 0, 3.6, 0],
        ['Brown Rice', 123, 2.6, 23, 0.9, 1.8],
        ['Broccoli', 34, 2.8, 7, 0.4, 2.6],
        ['Salmon', 208, 20.4, 0, 12.4, 0],
        ['Quinoa', 368, 14.1, 64.2, 6.1, 7.0],
        ['Avocado', 160, 2.0, 8.5, 14.7, 6.7],
        ['Sweet Potato', 86, 1.6, 20.1, 0.1, 3.0],
        ['Greek Yogurt', 59, 10.0, 3.6, 0.4, 0],
        ['Almonds', 579, 21.2, 21.6, 49.9, 12.5],
        ['Spinach', 23, 2.9, 3.6, 0.4, 2.2]
    ]
    
    with open('food_database.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(foods_data)
    
    print("Food database created successfully!")

def read_food_database():
    """Read and display food database"""
    
    if not os.path.exists('food_database.csv'):
        create_food_database()
    
    foods = []
    with open('food_database.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            foods.append(row)
    
    return foods

def search_food_database(food_name):
    """Search for specific food in database"""
    
    foods = read_food_database()
    food_name_lower = food_name.lower()
    
    for food in foods:
        if food_name_lower in food['Food Item'].lower():
            return food
    
    return None

def calculate_recipe_nutrition(recipe_ingredients):
    """Calculate nutrition for a recipe using food database"""
    
    foods = read_food_database()
    
    # Create a lookup dictionary for faster searching
    food_lookup = {food['Food Item'].lower(): food for food in foods}
    
    total_nutrition = {
        'calories': 0,
        'protein': 0,
        'carbs': 0,
        'fat': 0,
        'fiber': 0
    }
    
    recipe_details = []
    
    for ingredient in recipe_ingredients:
        food_name = ingredient['food'].lower()
        quantity_grams = ingredient['quantity']
        
        if food_name in food_lookup:
            food_data = food_lookup[food_name]
            
            # Calculate nutrition per serving (quantity/100g)
            multiplier = quantity_grams / 100
            
            ingredient_nutrition = {
                'food': ingredient['food'],
                'quantity': quantity_grams,
                'calories': float(food_data['Calories per 100g']) * multiplier,
                'protein': float(food_data['Protein (g)']) * multiplier,
                'carbs': float(food_data['Carbs (g)']) * multiplier,
                'fat': float(food_data['Fat (g)']) * multiplier,
                'fiber': float(food_data['Fiber (g)']) * multiplier
            }
            
            recipe_details.append(ingredient_nutrition)
            
            # Add to totals
            total_nutrition['calories'] += ingredient_nutrition['calories']
            total_nutrition['protein'] += ingredient_nutrition['protein']
            total_nutrition['carbs'] += ingredient_nutrition['carbs']
            total_nutrition['fat'] += ingredient_nutrition['fat']
            total_nutrition['fiber'] += ingredient_nutrition['fiber']
    
    return {
        'recipe_details': recipe_details,
        'total_nutrition': total_nutrition
    }

# Example usage
create_food_database()

# Search for a specific food
chicken_data = search_food_database("chicken")
if chicken_data:
    print(f"Found: {chicken_data['Food Item']}")
    print(f"Calories: {chicken_data['Calories per 100g']} per 100g")
    print(f"Protein: {chicken_data['Protein (g)']}g per 100g")

# Calculate nutrition for a recipe
recipe = [
    {'food': 'Chicken Breast', 'quantity': 150},  # 150g
    {'food': 'Brown Rice', 'quantity': 80},       # 80g
    {'food': 'Broccoli', 'quantity': 100},        # 100g
    {'food': 'Avocado', 'quantity': 50}           # 50g
]

recipe_nutrition = calculate_recipe_nutrition(recipe)

print("\n=== Recipe Nutrition Analysis ===")
for ingredient in recipe_nutrition['recipe_details']:
    print(f"{ingredient['food']} ({ingredient['quantity']}g): "
          f"{ingredient['calories']:.0f} cal, "
          f"{ingredient['protein']:.1f}g protein")

totals = recipe_nutrition['total_nutrition']
print(f"\nTotal Recipe Nutrition:")
print(f"Calories: {totals['calories']:.0f}")
print(f"Protein: {totals['protein']:.1f}g")
print(f"Carbohydrates: {totals['carbs']:.1f}g")
print(f"Fat: {totals['fat']:.1f}g")
print(f"Fiber: {totals['fiber']:.1f}g")
