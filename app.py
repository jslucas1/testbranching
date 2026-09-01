def calculate_miles(steps):
    miles = steps/2500
    return miles

def get_total_steps():
    steps = int(input("How many steps did you take today? "))
    return steps

def display_total_miles(miles, name):
    print(f"Great job {name}, it looks like you walked {miles} miles today")

def get_user_name():
    return input("Hi, what is your name? ")

# main flow of control 
name = get_user_name()
steps = get_total_steps()
miles = calculate_miles(steps)
display_total_miles(miles, name)