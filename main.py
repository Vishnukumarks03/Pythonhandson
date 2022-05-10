calculation_to_units = 24
name_of_unit = "hours"
custom_message ='Days to hours calculation done'

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_unit}")
    return custom_message

var=days_to_units(21, custom_message)
#days_to_units(42,"OneVill Tribe")

def scope_ident(num_of_days,custom_message):
    print(f"{num_of_days} days do {custom_message}")

#scope_ident(100,"Viability")
user_input=input("Hi User, enter something\n")
print(f"Value entered {user_input} {var}")

