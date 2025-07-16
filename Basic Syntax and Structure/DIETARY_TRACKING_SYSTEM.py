# Interactive dietary tracking system using while loops
def dietary_tracking_system():
    daily_calories = 0
    calorie_goal = 2000
    foods_eaten = []
    
    print(f"Daily Calorie Goal: {calorie_goal} calories")
    print("Enter foods consumed (type 'done' to finish):")
    
    while daily_calories < calorie_goal:
        food_input = input("Food item: ")
        
        if food_input.lower() == 'done':
            break
        
        try:
            calories = int(input(f"Calories in {food_input}: "))
            daily_calories += calories
            foods_eaten.append({'food': food_input, 'calories': calories})
            
            remaining_calories = calorie_goal - daily_calories
            print(f"Total calories: {daily_calories}")
            
            if remaining_calories > 0:
                print(f"Remaining calories: {remaining_calories}")
            else:
                print("Calorie goal reached!")
                break
                
        except ValueError:
            print("Please enter a valid number for calories")
    
    # Summary report
    print("\n=== Daily Summary ===")
    print(f"Total calories consumed: {daily_calories}")
    print(f"Calorie goal: {calorie_goal}")
    
    if daily_calories >= calorie_goal:
        print("✓ Calorie goal achieved!")
    else:
        print(f"⚠ {calorie_goal - daily_calories} calories below goal")
    
    print("\nFoods consumed:")
    for food in foods_eaten:
        print(f"- {food['food']}: {food['calories']} calories")

# Example monitoring session (commented out for demonstration)
# dietary_tracking_system()
