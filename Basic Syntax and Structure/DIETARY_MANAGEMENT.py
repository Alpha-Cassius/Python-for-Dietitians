# String examples for dietary management
client_name = "Vaibhav"
food_item = "Grilled Salmon"
dietary_restriction = "Lactose intolerant"
meal_plan_notes = "Prefers Mediterranean-style meals"

# String operations for food categorization
food_category = "Protein"
full_description = food_item + " - " + food_category
print(f"Food item: {full_description}")

# Checking dietary restrictions
if "lactose" in dietary_restriction.lower():
    print("Avoid dairy products")
