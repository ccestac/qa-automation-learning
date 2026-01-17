# Operators Practice - Day 2
# Author: Carlos Cestac

# Math operations
print("=== MATH OPERATIONS ===")
salary_monthly = 800 # Current salary in USD
months = 9  # Months to save
target_savings = 3000

total_saved = salary_monthly *months
print(f"Monthly salary: ${salary_monthly}")
print(f"Saving for {months} months: ${total_saved}")
print(f"Target: ${target_savings}")

remaining = target_savings - total_saved
print(f"Still need: ${remaining}")

# Calculate Europ salary comparison
europe_salary = 3000 # EUR per month
argentina_salary = 800 # USD per month
difference = europe_salary - argentina_salary
percentage = (difference / argentina_salary) * 100

print("\n=== SALARY COMPARISON ===")
print(f"Argentina: ${argentina_salary}/month")
print(f"Europe (Poland): €{europe_salary}/month")
print(f"Europe salary is {percentage:.0f}% higher")

# String manipulation
print("\n=== STRING PRACTICE ===")
first_name = "Carlos"
last_name = "Cestac"
job_tittle = "QA Automation engineer"

# Concatenation
full_name = first_name + " " + last_name
print("Full name:", full_name)

# f-strings (modern way)
intro = f"Hello! I'm {full_name}, a {job_tittle}."
print(intro)

# String methods
email_domain = "gmail.com"
email = f"{first_name.lower()}. {last_name.lower()}@{email_domain}"
print(f"Email: {email}")

# Linkedin URL
linkedin = f"linkedin.com/in/{first_name.lower()}-{last_name.lower()}"
print(f"Linkedin: {linkedin}")

print("\n=== LENGTH CALCULATIONS ===")
print(f"My full name has {len(full_name)} characters")
print(f"My email has {len(email)} characters")
