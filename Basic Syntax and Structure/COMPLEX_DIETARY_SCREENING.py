# Complex dietary screening using logical operators
def screen_dietary_eligibility(age, bmi, has_diabetes, is_pregnant):
    # AND operator: Multiple conditions must be true
    eligible_for_weight_loss = age >= 18 and bmi > 25 and not is_pregnant
    
    # OR operator: Any condition can be true
    needs_special_diet = has_diabetes or is_pregnant or bmi > 30
    
    # NOT operator: Negating conditions
    can_fast = not has_diabetes and not is_pregnant and age >= 18
    
    return {
        'weight_loss_eligible': eligible_for_weight_loss,
        'special_diet_needed': needs_special_diet,
        'fasting_suitable': can_fast
    }

# Example screening
client_screening = screen_dietary_eligibility(28, 27.5, False, False)
print(f"Weight loss program eligible: {client_screening['weight_loss_eligible']}")
print(f"Special diet needed: {client_screening['special_diet_needed']}")
print(f"Intermittent fasting suitable: {client_screening['fasting_suitable']}")
