"""
Simple Python Application
"""

def greet(name):
    """Greet a user by name."""
    return f"Hello, {name}! Welcome to your Python app."

def main():
    """Main entry point of the application."""
    print("=" * 50)
    print("Python Application")
    print("=" * 50)
    
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(f"\n{message}\n")
    
    print("Your virtual environment is working correctly!")

if __name__ == "__main__":
    main()
