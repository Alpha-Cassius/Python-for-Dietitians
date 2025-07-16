# Comprehensive dietary assessment using if-elif-else
def provide_dietary_guidance(bmi, blood_pressure, cholesterol_level):
    guidance = []
    
    # BMI-based recommendations
    if bmi < 18.5:
        guidance.append("Increase calorie intake with nutrient-dense foods")
        guidance.append("Consider adding healthy fats like nuts and avocados")
    elif bmi >= 18.5 and bmi < 25:
        guidance.append("Maintain current weight with balanced nutrition")
    elif bmi >= 25 and bmi < 30:
        guidance.append("Aim for gradual weight loss of 1-2 pounds per week")
        guidance.append("Reduce portion sizes and increase physical activity")
    else:
        guidance.append("Consult with healthcare provider for weight management")
        guidance.append("Consider structured weight loss program")
    
    # Blood pressure considerations
    if blood_pressure >= 140:
        guidance.append("Limit sodium intake to less than 2,300mg daily")
        guidance.append("Increase potassium-rich foods like bananas and spinach")
    elif blood_pressure >= 130:
        guidance.append("Monitor sodium intake and choose low-sodium options")
    
    # Cholesterol management
    if cholesterol_level >= 240:
        guidance.append("Limit saturated fat to less than 7% of total calories")
        guidance.append("Include soluble fiber from oats, beans, and apples")
    elif cholesterol_level >= 200:
        guidance.append("Choose lean proteins and limit processed foods")
    
    return guidance

# Example assessment
client_guidance = provide_dietary_guidance(28.5, 135, 220)
print("Dietary Recommendations:")
for i, recommendation in enumerate(client_guidance, 1):
    print(f"{i}. {recommendation}")
