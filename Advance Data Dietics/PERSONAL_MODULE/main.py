# Using the custom nutrition_tools module
import nutrition_tools

# Client assessment using custom module
def complete_client_assessment(weight, height, age, activity_level):
    """Complete nutritional assessment using custom tools"""
    
    # Basic calculations
    bmi = nutrition_tools.calculate_bmi(weight, height)
    bmi_category = nutrition_tools.classify_bmi(bmi)
    ideal_range = nutrition_tools.calculate_ideal_weight_range(height)
    water_needs = nutrition_tools.calculate_daily_water_needs(weight, activity_level)
    protein_needs = nutrition_tools.calculate_protein_needs(weight, activity_level, age)
    
    # Comprehensive assessment
    assessment = {
        'anthropometric': {
            'bmi': round(bmi, 1),
            'bmi_category': bmi_category,
            'ideal_weight_range': (round(ideal_range[0], 1), round(ideal_range[1], 1)),
            'weight_status': 'within range' if ideal_range[0] <= weight <= ideal_range[1] else 'outside range'
        },
        'daily_needs': {
            'water_ml': round(water_needs, 0),
            'protein_g': round(protein_needs, 1)
        },
        'recommendations': []
    }
    
    # Generate recommendations
    if bmi < 18.5:
        assessment['recommendations'].append("Consider weight gain strategies")
    elif bmi >= 25:
        assessment['recommendations'].append("Consider weight management program")
    
    if weight < ideal_range[0]:
        assessment['recommendations'].append("Focus on healthy weight gain")
    elif weight > ideal_range[1]:
        assessment['recommendations'].append("Focus on healthy weight loss")
    
    return assessment

# Example client assessment
client_results = complete_client_assessment(
    weight=72,
    height=1.68,
    age=28,
    activity_level='moderate'
)

print("=== Client Assessment Results ===")
print(f"BMI: {client_results['anthropometric']['bmi']} ({client_results['anthropometric']['bmi_category']})")
print(f"Ideal weight range: {client_results['anthropometric']['ideal_weight_range'][0]}-{client_results['anthropometric']['ideal_weight_range'][1]} kg")
print(f"Daily water needs: {client_results['daily_needs']['water_ml']:.0f} ml")
print(f"Daily protein needs: {client_results['daily_needs']['protein_g']} g")

if client_results['recommendations']:
    print("\nRecommendations:")
    for rec in client_results['recommendations']:
        print(f"• {rec}")
