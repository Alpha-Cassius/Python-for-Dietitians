# Nutritional assessment using comparison operators
def assess_nutrient_intake(actual_intake, recommended_intake, nutrient_name):
    if actual_intake > recommended_intake:
        status = "Exceeds recommendation"
        recommendation = f"Consider reducing {nutrient_name} intake"
    elif actual_intake == recommended_intake:
        status = "Meets recommendation"
        recommendation = f"Maintain current {nutrient_name} intake"
    else:
        status = "Below recommendation"
        recommendation = f"Increase {nutrient_name} intake"
    
    return status, recommendation

# Example assessments
sodium_assessment = assess_nutrient_intake(3500, 2300, "sodium")
protein_assessment = assess_nutrient_intake(45, 50, "protein")
fiber_assessment = assess_nutrient_intake(35, 25, "fiber")

print(f"Sodium: {sodium_assessment[0]} - {sodium_assessment[1]}")
print(f"Protein: {protein_assessment[0]} - {protein_assessment[1]}")
print(f"Fiber: {fiber_assessment[0]} - {fiber_assessment[1]}")
