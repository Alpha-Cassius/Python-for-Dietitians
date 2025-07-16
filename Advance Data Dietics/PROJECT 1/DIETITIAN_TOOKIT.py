import csv
import math
from datetime import datetime

class DietitianToolkit:
    """Complete toolkit for dietitian calculations and assessments"""
    
    def __init__(self):
        self.food_database = self.load_food_database()
        self.client_records = {}
    
    def load_food_database(self):
        """Load food database from CSV file"""
        # This would load from an actual file in practice
        return {
            'chicken breast': {'calories': 165, 'protein': 31.0, 'carbs': 0, 'fat': 3.6},
            'brown rice': {'calories': 123, 'protein': 2.6, 'carbs': 23, 'fat': 0.9},
            'broccoli': {'calories': 34, 'protein': 2.8, 'carbs': 7, 'fat': 0.4},
            'salmon': {'calories': 208, 'protein': 20.4, 'carbs': 0, 'fat': 12.4},
            'quinoa': {'calories': 368, 'protein': 14.1, 'carbs': 64.2, 'fat': 6.1}
        }
    
    def calculate_bmi(self, weight_kg, height_m):
        """Calculate BMI with classification"""
        bmi = weight_kg / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return {'bmi': round(bmi, 1), 'category': category}
    
    def calculate_caloric_needs(self, weight, height, age, gender, activity_level):
        """Calculate daily caloric needs using Harris-Benedict equation"""
        
        # BMR calculation
        if gender.lower() == 'male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
        
        # Activity multipliers
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        
        tdee = bmr * activity_factors.get(activity_level, 1.2)
        
        return {
            'bmr': round(bmr, 0),
            'tdee': round(tdee, 0),
            'activity_factor': activity_factors.get(activity_level, 1.2)
        }
    
    def create_meal_plan(self, daily_calories, dietary_restrictions=None):
        """Create a balanced meal plan"""
        
        if dietary_restrictions is None:
            dietary_restrictions = []
        
        # Macronutrient distribution
        protein_calories = daily_calories * 0.20
        carb_calories = daily_calories * 0.50
        fat_calories = daily_calories * 0.30
        
        # Convert to grams
        protein_grams = protein_calories / 4
        carb_grams = carb_calories / 4
        fat_grams = fat_calories / 9
        
        # Meal distribution (3 meals + 2 snacks)
        meal_calories = daily_calories * 0.25  # 25% per main meal
        snack_calories = daily_calories * 0.125  # 12.5% per snack
        
        meal_plan = {
            'daily_totals': {
                'calories': daily_calories,
                'protein': round(protein_grams, 1),
                'carbohydrates': round(carb_grams, 1),
                'fat': round(fat_grams, 1)
            },
            'meal_structure': {
                'breakfast': round(meal_calories, 0),
                'lunch': round(meal_calories, 0),
                'dinner': round(meal_calories, 0),
                'snack_1': round(snack_calories, 0),
                'snack_2': round(snack_calories, 0)
            },
            'dietary_restrictions': dietary_restrictions
        }
        
        return meal_plan
    
    def analyze_food_intake(self, food_items):
        """Analyze nutritional content of food intake"""
        
        total_nutrition = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0
        }
        
        detailed_analysis = []
        
        for item in food_items:
            food_name = item['food'].lower()
            quantity_g = item['quantity']
            
            if food_name in self.food_database:
                food_data = self.food_database[food_name]
                multiplier = quantity_g / 100  # Database values are per 100g
                
                item_nutrition = {
                    'food': item['food'],
                    'quantity': quantity_g,
                    'calories': food_data['calories'] * multiplier,
                    'protein': food_data['protein'] * multiplier,
                    'carbs': food_data['carbs'] * multiplier,
                    'fat': food_data['fat'] * multiplier
                }
                
                detailed_analysis.append(item_nutrition)
                
                # Add to totals
                for nutrient in total_nutrition:
                    total_nutrition[nutrient] += item_nutrition[nutrient]
        
        return {
            'detailed_analysis': detailed_analysis,
            'total_nutrition': {k: round(v, 1) for k, v in total_nutrition.items()}
        }
    
    def generate_assessment_report(self, client_data):
        """Generate comprehensive assessment report"""
        
        # Extract client information
        name = client_data['name']
        weight = client_data['weight']
        height = client_data['height']
        age = client_data['age']
        gender = client_data['gender']
        activity_level = client_data['activity_level']
        
        # Perform calculations
        bmi_results = self.calculate_bmi(weight, height)
        caloric_needs = self.calculate_caloric_needs(weight, height, age, gender, activity_level)
        meal_plan = self.create_meal_plan(caloric_needs['tdee'])
        
        # Generate report
        report = {
            'client_info': {
                'name': name,
                'assessment_date': datetime.now().strftime('%Y-%m-%d')
            },
            'anthropometric': bmi_results,
            'energy_needs': caloric_needs,
            'meal_plan': meal_plan,
            'recommendations': self.generate_recommendations(bmi_results, caloric_needs)
        }
        
        return report
    
    def generate_recommendations(self, bmi_results, caloric_needs):
        """Generate personalized recommendations"""
        
        recommendations = []
        
        # BMI-based recommendations
        if bmi_results['category'] == 'Underweight':
            recommendations.append("Focus on calorie-dense, nutrient-rich foods")
            recommendations.append("Consider adding healthy fats like nuts and avocados")
        elif bmi_results['category'] == 'Overweight':
            recommendations.append("Aim for gradual weight loss of 1-2 pounds per week")
            recommendations.append("Increase physical activity and reduce portion sizes")
        elif bmi_results['category'] == 'Obese':
            recommendations.append("Consult with healthcare provider for weight management")
            recommendations.append("Consider structured weight loss program")
        
        # General recommendations
        recommendations.append("Consume 5-9 servings of fruits and vegetables daily")
        recommendations.append("Choose whole grains over refined grains")
        recommendations.append("Include lean protein sources with each meal")
        recommendations.append("Stay hydrated with at least 8 glasses of water daily")
        
        return recommendations

# Example usage of the complete system
if __name__ == "__main__":
    # Initialize toolkit
    toolkit = DietitianToolkit()
    
    # Sample client data
    client_data = {
        'name': 'Jane Smith',
        'weight': 65,  # kg
        'height': 1.65,  # meters
        'age': 30,
        'gender': 'female',
        'activity_level': 'moderate'
    }
    
    # Generate comprehensive assessment
    assessment = toolkit.generate_assessment_report(client_data)
    
    # Display results
    print("=== COMPREHENSIVE NUTRITIONAL ASSESSMENT ===")
    print(f"Client: {assessment['client_info']['name']}")
    print(f"Assessment Date: {assessment['client_info']['assessment_date']}")
    print()
    
    print("ANTHROPOMETRIC ASSESSMENT:")
    print(f"BMI: {assessment['anthropometric']['bmi']} ({assessment['anthropometric']['category']})")
    print()
    
    print("ENERGY NEEDS:")
    print(f"Basal Metabolic Rate: {assessment['energy_needs']['bmr']:.0f} calories")
    print(f"Total Daily Energy Expenditure: {assessment['energy_needs']['tdee']:.0f} calories")
    print()
    
    print("MEAL PLAN STRUCTURE:")
    for meal, calories in assessment['meal_plan']['meal_structure'].items():
        print(f"{meal.capitalize()}: {calories:.0f} calories")
    print()
    
    print("MACRONUTRIENT TARGETS:")
    totals = assessment['meal_plan']['daily_totals']
    print(f"Protein: {totals['protein']}g")
    print(f"Carbohydrates: {totals['carbohydrates']}g")
    print(f"Fat: {totals['fat']}g")
    print()
    
    print("RECOMMENDATIONS:")
    for i, rec in enumerate(assessment['recommendations'], 1):
        print(f"{i}. {rec}")
    
    # Example food intake analysis
    print("\n=== FOOD INTAKE ANALYSIS EXAMPLE ===")
    daily_intake = [
        {'food': 'Chicken Breast', 'quantity': 120},
        {'food': 'Brown Rice', 'quantity': 80},
        {'food': 'Broccoli', 'quantity': 150},
        {'food': 'Salmon', 'quantity': 100}
    ]
    
    intake_analysis = toolkit.analyze_food_intake(daily_intake)
    
    print("Food Items Consumed:")
    for item in intake_analysis['detailed_analysis']:
        print(f"• {item['food']} ({item['quantity']}g): {item['calories']:.0f} cal, {item['protein']:.1f}g protein")
    
    totals = intake_analysis['total_nutrition']
    print(f"\nTotal Intake: {totals['calories']:.0f} calories, {totals['protein']:.1f}g protein")
    print(f"Percentage of daily needs: {(totals['calories'] / assessment['energy_needs']['tdee']) * 100:.1f}%")
