def display_main_menu():
    print("Welcome to Astro Quiz!")
    print("Please select a category:")
    print("1. Planets")
    print("2. Stars")
    print("3. Space Missions")
    print("4. Black Holes")
    print("5. Galaxies")

    while True:
        try:
            choice = int(input("Enter the number of the category: "))
            if 1 <= choice <= 5:

                categories = {
                    1: "Planets",
                    2: "Stars",
                    3: "Space Missions",
                    4: "Black Holes",
                    5: "Galaxies"
                }
                return categories[choice]
            else:
                print("Please enter a valid category number (1-5).")
        except ValueError:
            print("Invalid input! Please enter a number.")


