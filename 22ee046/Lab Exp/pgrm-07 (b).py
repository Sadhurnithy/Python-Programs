def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")

def get_details():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = []
    for i in range(6):
        marks.append(int(input("Enter marks for subject {}: ".format(i + 1))))
    return name, age, marks

def main():
    try:
        name, age, marks = get_details()
        if age >= 0:
            dict = {"name": name, "age": age, "marks": marks}
            print(dict)
    except NegativeAgeError as e:
        print(e)

if __name__ == "__main__":
    main()
