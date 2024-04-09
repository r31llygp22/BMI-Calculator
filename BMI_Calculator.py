try:
    measurement_system = input("Choose the measurement system, metric or imperial: ")

    weight_unit_imperial = "kilograms" if measurement_system == "metric" else "pounds"
    height_unit_imperial = "meters" if measurement_system == "metric" else "inches"

    conversion_factors = {
        "metric": (1, 1),  
        "imperial": (0.453592, 0.0254)
    }


    weight = float(input(f"Enter your weight in {weight_unit_imperial}: "))
    height = float(input(f"Enter your height in {height_unit_imperial}: "))

    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight. Eat more.")
    elif 18.5 <= bmi < 24.9:
        print("Your weight is normal. Stay like that.")
    elif 25 <= bmi < 29.9:
        print("You are overweight. Eat less.")
    else:
        print("You are obese. Stop going to McDonald's.")

except ValueError as exception:
    print(exception)
except ZeroDivisionError:
    print("You can not be shorter than o feet or meters.")
except Exception as exception:
    print("Something went wrong", exception)


