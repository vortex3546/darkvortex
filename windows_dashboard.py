import os
import time
import platform

# Function to set the title of the Command Prompt window
def set_cmd_title(title):
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the dashboard menu
def display_dashboard():
    clear_screen()
    print("\033[94m=== Dashboard ===\033[0m")
    print("\033[94m1. Option 1\033[0m")
    print("\033[94m2. Option 2\033[0m")
    print("\033[94m3. Option 3\033[0m")
    print("\033[94m4. Exit\033[0m")
    print("\033[94m=================\033[0m")

# Function to simulate a back-and-forth loading animation
def loading_animation():
    direction = 1
    position = 0
    for _ in range(10):
        loading_bar = "[" + " " * position + "=" + " " * (8 - position) + "]"
        print("\033[94mLoading...\033[0m " + loading_bar, end="\r")
        time.sleep(0.2)
        position += direction
        if position == 8 or position == 0:
            direction *= -1

# Main function
def main():
    set_cmd_title("Vortex")

    while True:
        display_dashboard()
        choice = input("\033[94mEnter your choice: \033[0m")

        if choice == '1':
            print("\033[94mYou selected Option 1\033[0m")
            loading_animation()
            print("\n\033[94mDone!\033[0m")
            # Add functionality for Option 1 here
        elif choice == '2':
            print("\033[94mYou selected Option 2\033[0m")
            # Add functionality for Option 2 here
        elif choice == '3':
            print("\033[94mYou selected Option 3\033[0m")
            # Add functionality for Option 3 here
        elif choice == '4':
            print("\033[94mExiting...\033[0m")
            break
        else:
            print("\033[94mInvalid choice. Please try again.\033[0m")

        input("\033[94mPress Enter to continue...\033[0m")

if __name__ == "__main__":
    main()
