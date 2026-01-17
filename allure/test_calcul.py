import allure

@allure.title("Сложение в калькуляторе")
@allure.description("Сложение в калькуляторе, где a=10,b=5")
def test_addition(a=10,b=5):
    with allure.step("Сложение 10 + 5"):
        print(a + b)

@allure.title("Вычитание в калькуляторе")
@allure.description("Вычитание в калькуляторе, где a=10,b=5")
def test_subtraction(a=10,b=5):
    with allure.step("Вычитание 10 - 5"):
        print(a - b)

@allure.title("Умножение в калькуляторе")
@allure.description("Умножение в калькуляторе, где a=10,b=5")
def test_multiplication(a=10,b=5):
    with allure.step("Умножение 10 * 5"):
        print(a * b)

@allure.title("Деление в калькуляторе")
@allure.description("Деление в калькуляторе, где a=10,b=0")
def test_division(a=10,b=0):
    with allure.step("Деление без остатка 10 // 0"):
        if b==0:
            print("На 0 делить нельзя")
            return None
        else:
            print(a // b)