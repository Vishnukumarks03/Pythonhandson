#Assign a variable in python and read from function declration
#Customer on boarding
name= "ABC"
age = 30

def customer_onboarding(name, age):
    print(f"Customer {name},age {age} subscribed")
    user_input = input("enter your skills\n")
    print(f"Skills {user_input}")

customer_onboarding(name,age)
customer_onboarding("XYZ",60)

