# the first code is the error One so I commented it out, scroll down to see corrected version one (2nd codes)

# import json

# business = "X-Clinic"

# services = [
#         {"name": "consultation", "price": 500},
#         {"name": "x-ray", "price": 700},
#         {"name": "check-up", "price": 400}
#     ]

# try:
#     with open("leads.json", "r") as file:
#             leads = json.load(file)
# except:
#      leads = []

# def save_leads():
#         with open("leads.json", "w") as file:
#             json.dump(leads, file, indent=4)


# def generate_reply(msg):
#         msg = msg.lower()

#         # admin command
#         if msg == " show leads":
#             return json.dumps(leads, indent=4)
        
        
#         #booking detection
#         if "book" in msg:
#             for service in services:
#                 if service ["name"] in msg:

#                    name = input("Enter your name: ")
#                    gmail = input("Enter your Gmail: ")                  
 

#                    leads.append({
#                         "name": name,
#                         "gmail": gmail,
#                         "service": service["name"],
#                         "price": service["price"]
#                     })
#                    save_leads()

#                    return f"Chatpal: Booking confirmed for {service['name']} at rs {service["price"]}"
                
            
#                 return "Chatpal: Please mention a valid service."
        

# print("Welcome to", business )

# while True:
#         users = input('Customer:')
#         if users.lower() == "exit":
#             print("Chatpal: Goodbye, have a nice day!")
#             break
#         print(generate_reply(users))
            


                

import json

business = "X-Clinic"

services = [
    {"name": "consultation", "price": 500},
    {"name": "x-ray", "price": 700},
    {"name": "check-up", "price": 400}
]

# Load leads
try:
    with open("leads.json", "r") as file:
        leads = json.load(file)
except:
    leads = []

def save_leads():
    with open("leads.json", "w") as file:
        json.dump(leads, file, indent=4)

def generate_reply(msg):
    msg = msg.lower()

    # Show leads
    if msg == "show leads":
        return json.dumps(leads, indent=4)

    # Booking
    if "book" in msg:
        matched = False

        for service in services:
            if service["name"] in msg:
                matched = True

                name = input("Enter your name: ")
                gmail = input("Enter your Gmail: ")

                leads.append({
                    "name": name,
                    "gmail": gmail,
                    "service": service["name"],
                    "price": service["price"]
                })

                save_leads()

                return f"Chatpal: Booking confirmed for {service['name']} at rs {service['price']}"

        if not matched:
            return "Chatpal: Please mention a valid service."

    # If user just types service name without booking
    for service in services:
        if service["name"] in msg:
            return f"Chatpal: {service['name'].title()} costs rs {service['price']}"

    return "Chatpal: Type 'book + service name'"

print("Welcome to", business)

while True:
    user = input("Customer: ")

    if user.lower() == "exit":
        print("Chatpal: Goodbye, have a nice day!")
        break

    print(generate_reply(user))
    