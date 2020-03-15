# This is python program to just create fack information.
import random

first_name = ["Jake","Mike","Kate","Henry","Schotty","Gimmy","Charles","Black","Karlie","Timmy"]

last_name = ["smith","doe","jankens","robinson","davis","jaffarson","jacob","wright","peterson","micheal"]

street_name = ["Main","High","Pearl","Maple","Park","Pine","Oak","kadle","Elm"]

fake_cities = ["Metroplois","Eerie","King's landing","Sunnydale","Bedrock","South park","Atlantis"]

States = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE"]

for n in range(20):
    f_name = random.choice(first_name)
    l_name = random.choice(last_name)

    phone_number = f"{random.randint(100,999)}-555-{random.randint(1000,9999)}"

    street_number = random.randint(100,999)

    street = random.choice(street_name)

    city = random.choice(fake_cities)
    state = random.choice(States)
    zipcode = random.randint(10000,99999)

    address = f"{street_number} {street} St., {city} {state} {zipcode}"

    email = f"{f_name.lower()}{l_name.lower()}@gmail.com"

    print(f"name: {f_name} {l_name}")
    print(f"Phone number: {phone_number}")
    print(f"Address: {address}")
    print(f"Email address: {email}")
    print("--------------------------------")
