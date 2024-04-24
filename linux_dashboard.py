import os
import time

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to display the dashboard menu
def display_dashboard():
    clear_screen()
    print("=== Dashboard ===")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    print("=================")

# Function to simulate a back-and-forth loading animation
def loading_animation():
    direction = 1
    position = 0
    for _ in range(10):
        loading_bar = "[" + " " * position + "=" + " " * (8 - position) + "]"
        print("Loading... " + loading_bar, end="\r")
        time.sleep(0.2)
        position += direction
        if position == 8 or position == 0:
            direction *= -1

# Main function
def main():
    while True:
        display_dashboard()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("You selected Option 1")
            loading_animation()
            print("\nDone!")
            # Add functionality for Option 1 here
        elif choice == '2':
            print("You selected Option 2")
            # Add functionality for Option 2 here
        elif choice == '3':
            print("You selected Option 3")
            # Add functionality for Option 3 here
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
