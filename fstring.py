# This is the string format which is doing using format string
txt = "My name is {} and I live in {}"
name = "Anisha"
country = "India"
print(txt.format(name, country))

# this is done using f-string
print(f" Hey my name is {name} and I live in {country}")
# When we want some digits only
money = 48.6789
txt1 = (f"Hey I have recived this much {money:.3f} money")
print(txt1)
# when we can calculate using string
print(f"{3*4}")