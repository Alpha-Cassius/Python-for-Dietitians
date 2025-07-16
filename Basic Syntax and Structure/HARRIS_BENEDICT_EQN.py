# Harris-Benedict equation for calculating BMR
# Using comments
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        # BMR for males: 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        # BMR for females: 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr
