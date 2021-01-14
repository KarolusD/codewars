def bmi(weight, height):
    bmi = weight / (height * height)

    if bmi <= 18.5:
        return "Underweight"

    if bmi <= 25.0:
        return "Normal"

    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"




print("Basic tests")
print(bmi(50, 1.80), "Underweight")
print(bmi(80, 1.80), "Normal")
print(bmi(90, 1.80), "Overweight")
print(bmi(110, 1.80), "Obese")

print("Our tests")
print(bmi(88, 1.88), "Dave")


print(bmi(82, 1.88), "Me")
print(bmi(100, 1.92), "Raf")
