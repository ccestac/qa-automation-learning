# Lists and Loops Practice - Day 2
# Author: Carlos Cestac

print("=== LISTS BASICS ===\n")

# Job search target cities
target_cities = ["Warsaw", "Krakow", "Berlin", "Amsterdam", "Tallinn"]

print("Target cities for job search:")
for city in target_cities:
    print(f" - {city}")

    print(f"\nTotal cities: {len(target_cities)}")

    # Add more cities
    target_cities.append("Barcelona")
    target_cities.append("Lisbon")
    print(f"\nUpdated list: {target_cities}")

    print("\n" + "="*50)
    print("=== SKILLS TO LERN ===\n")

    # QA skills checklist
    skills = ["Python", "Selenium", "Git", "Test Automation", "CI/CD"]

    print("skills to master:")
    for index, skills in enumerate(skills, start=1):
        print(f"{index}. {skills}")

        print("\n" + "="*50)
        print("=== SALARY PROGRSSION ===\n")

        # Salary projection over 5 years
        years = [1, 2, 3, 4, 5]
        salaries = [25000, 35000, 45000, 55000, 65000] # EUR

        print("Expected salary growth (QA Engineer in Europe):")
        for year, salary in zip(years, salaries):
            print(f"Year {year}: €{salary:,}")

            total_earnings = sum(salaries)
            print(f"\nTotal earnings over 5 years: €{total_earnings:,}")

            print("\n" + "="*50)
            print("=== DAILY STUDY PLAN ===\n")

            # Study schedule for 9 months
            topics_week1 = [
                "Python basics",
                "Variables and data types",
                "Lists and loops",
                "Functions",
                "File handling"
                ]
            
            print("Week 1 - Python Fundamentals:")
            for day, topic in enumerate(topics_week1, start=1):
                print(f" Day {day}: {topic}")

                print("\n" + "="*50)
                print("=== AUTOMATION PRACTICE ===\n")

                # Simulate testing multiple user logins
                test_users = [
                    "carlos.cestac@gmail.com" ,
                    "test.user1@example.com",
                    "test.user2@example.com",
                    "admin@company.com"
                    ]
                
                print("Running automated login tests:")
                for i, email in enumerate(test_users, start=1):
                    print(f"Test {i}: Testing login for {email}... ✔ PASS")

                    print(f"\nTotal tests executed: {len(test_users)}")
                    print("All tests passed! ✔️")

                    print("\n" + "="*50)
                    print("=== LOOP EXERCISES ===\n")

                    # Print multiplication table
                    number = 7
                    print(f"Multiplication table for{number}:")
                    for i in range(1, 11):
                        result = number * i
                        print(f"{number} x {i} = {result}")

                        # Count down
                        print("\nCountdown:")
                        for i in range(10, 0, -1):
                            print(i, end=" ")
                            print ("🚀 Launch!")

                            print("\n\n" + "="*50)
                            print("Day 2 Complete! 💪")
                            print("="*50)
