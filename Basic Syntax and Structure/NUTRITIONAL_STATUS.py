# Note: All code within the function must be indented
def assess_nutritional_status(bmi):
    if bmi < 18.5:
        return "Underweight - consider calorie-dense foods"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight - maintain balanced diet"
    elif bmi >= 25 and bmi < 30:
        return "Overweight - consider portion control"
    else:
        return "Obese - consult healthcare provider"
