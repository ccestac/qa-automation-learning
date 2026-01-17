# Interactive Program - Day 2
# Author: Carlos Cestac

print("=== QA AUTOMATION SALARY CALCULATOR ===\n")

# Get user input
print("Entr your current information:")
name = input("Your name: ")
current_salary = int(input("Current monthly salary (USD): "))
city = input("Current city: ")

print("\nEnter your target job information:")
target_country = input("Target country: ")
target_salary = int(input("Target monthly salary (EUR/USD): "))
months_to_move = int(input("Months untill you move: "))

#  Calculations
total_savings_possible = current_salary * months_to_move
salary_increase = target_salary - current_salary
percentage_increase = (salary_increase / current_salary) * 100

# Display results
print("\n" + "="*50)
print(f"CAREER TRANSITION PLAN FOR {name.upper()}")
print("="*50)
print(f"CAREER TRANSITION PLAN FOR {name.upper()}")
print("="*50)

print(f"\nCurrent situation:")
print(f" Location: {city}")
print(f" Salary: ${current_salary}/month")

print(f"\nTarget situation:")
print(f" Location: {target_country}")
print(f" Salary: ${target_salary}/month")
print(f" Increase: ${salary_increase}/month ({percentage_increase:.1f}%)")

print(f"\nTimeline:")
print(f" Months until transition: {months_to_move}")
print(f" Possible savings: ${total_savings_possible}")

print(f"\nYearly comparison:")
print(f" Current annual: ${current_salary * 12}")
print(f" Target annual: ${target_salary * 12}")
print(f" Annual difference: ${(target_salary - current_salary) * 12}")

# Motivational message
if percentage_increase > 200:
    print(f"\n🚀 WOW! That's a {percentage_increase:.0f}% increase!")
    print("  Your quality of life will transform completely.")
elif percentage_increase > 100:
    print(f"\n✔️ Excellent! {percentage_increase:.0f}% increase!")
    print("  This will significantly improve your life.")
else:
    print(f"\n👍 Good! {percentage_increase:.0f}% increase!")
    print("  Every step forward counts.")

    print("\n" + "="*50)
    print("Keep learning. You're on the right path! 💪")
    print("="*50)
