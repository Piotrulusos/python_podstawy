# if statements = a block of code what will execute if it's condition is true
# instrukcje if = blok kodu, który zostanie wykonany, jeśli jego warunek jest spełniony

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
if age >= 18:
    print("You are an adult!")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
