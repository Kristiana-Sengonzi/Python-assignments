import random

countries = ["USA", "Mexico", "Canada", "Argentina", "Brazil", "France", "Spain", "England"]

print("=== Welcome to the 2026 World Cup Winner Simulator ===")

while True:
    print("\nAvailable Options:")
    print("1. Simulate the tournament winner")
    print("2. View participating contender countries")
    print("3. Exit program")
    
    user_input = input("Enter your choice (1-3): ").strip()
    
    if user_input == "3":
        print("Exiting the simulator. Enjoy the World Cup 2026!")
        break
        
    if user_input not in ["1", "2", "3"]:
        print("Invalid choice! Please select a valid option from the menu.")
        continue  
   
    if user_input == "1":
        winner = random.choice(countries)
        print(f"\n🏆 Evaluating match data... The simulated winner of World Cup 2026 is: **{winner}**! 🏆")
        
   
    elif user_input == "2":
        print("\nContender countries in this simulation:")
        for country in countries:
            print(f"- {country}")
            
    
    elif user_input == "3":
        print("\n[INFO] This feature is currently under construction...")
        pass  