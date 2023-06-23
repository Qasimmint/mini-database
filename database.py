email_ess = ["@", ".", "com"]

def names():
    name = input("Enter name: ")
    age = int(input("Enter your age: "))
    phonenumber = input("Enter phonenumber: ")
    email = input("Enter E-mail: ")

    if not isinstance(name, str):
        raise ValueError("Please enter your name")
    
    if type(age) == str:
        raise ValueError("Enter a valid age")
    
    if age < 20:
        print("Not qualifying")
        quit()
    
    if not phonenumber.isdigit() and len(phonenumber) != 11:
        # raise ValueError("Enter a valid 11-digit phone number")
        print("Enter valid phone number")
    
    if not any(substr in email for substr in email_ess):
        raise ValueError("Enter a valid email address")

    return {
        "name": name,
        "age": str(age),
        "phonenumber": str(phonenumber),
        "email": email
    }

person_info = names()

with open("database.txt", 'a') as file:
    file.write(",".join(person_info.values()))
    print("Data written to the file successfully.")
