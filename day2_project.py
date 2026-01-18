# Day 2 Final Project: QA Learning Progress Tracker
# Author: Carlos Cestac

print("="*60)
print("      QA AUTOMATION LEARNING - PROGRESS TRACKER")
print("="*60)

# Student information
name = input("\nEnter your name: ")
target_country = input("Target country for work: ")
target_months =int(input("Months until you want to be job-ready: "))

print(f"\nWelcome {name}! Let´s plan your journey to {target_country}. \n")

# Define learning path
weeks_needed = target_months * 4
hours_per_day = 6
total_hours = weeks_needed * 7 * hours_per_day

print("="*60)
print("LEARNING PATH CALCULATION")
print("="*60)
print(f"Timeline: {target_months} months ({weeks_needed} weeks)")
print(f"Study commitment: {hours_per_day} hours/day")
print(f"Total study hours: {total_hours} hours")

# Skills breakdown
skills = [
    "Python Fundamentals",
    "Git & GitHub",
    "Test Automation Basics",
    "Selenium WebDriver",
    "Test Frameworks (pytest)",
    "CI/CD Basics",
    "Project Portfolio"
    ]

print(f"\n{'='*60}")
print("SKILLS TO MASTER")
print("="*60)

for i, skill in enumerate(skills, start=1):
    weeks_per_skill = weeks_needed // len(skills)
    print(f"{i}. {skill} - {weeks_per_skill} weeks")

    # Daily schedule
    print(f"\n{'='*60}")
    print("DAILY SCHEDULE EXAMPLE")
    print("="*60)

    daily_tasks = [
        ("Morning", "Theory & Concepts", 2),
        ("Afternoon", "Coding Practice", 3),
        ("Evening", "Projects & Review", 1),
        ]
    
    total_daily = 0
    for period, task, hours in daily_tasks:
        print(f"{period:12} | {task:20} | {hours} hours")
        total_daily += hours

        print(f"{'Total':12} | {'':20} | {total_daily} hours")

        # Salary projection
        print(f"\n{'='*60}")
        print("SALARY PROJECTION")
        print("="*60)

        current_salary = 800
        target_salary = 2000
        months_list = list(range(0, target_months + 1, 3))
        salary_growth = []

        for month in months_list: 
            if month == 0:
                salary = current_salary
            elif month == target_months:
                salary = target_salary
            else: 
                progress = month / target_months
                salary = int(current_salary + (target_salary - current_salary) * progress)
                salary_growth.append(salary)
                print(f"Month {month:2}: ${salary}/month")

                # Final summary
                print(f"\n{'='*60}")
                print("SUMMARY")
                print("="*60)
                print(f"Student: {name}")
                print(f"Goal: QA Automation Engineer in {target_country}")
                print(f"Timeline: {target_months} months")
                print(f"Skills to master: {len(skills)}")
                print(f"Total study hours: {total_hours}")
                print(f"Salary increase: ${target_salary - current_salary}/month")

                print(f"\n{'='*60}")
                print(f"You can do this, {name}! Start today. 💪")
                print("="*60)
                