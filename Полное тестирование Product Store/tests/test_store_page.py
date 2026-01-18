import allure

from playwright.sync_api import expect
from pages.product_page import CartProduct
from pages.homepage import HomePage


@allure.title("Переход на страницу карточки товара Sony xperia z5 из главного меню")
def test_store(driver):
    store_page = HomePage(driver)
    with allure.step("Открываем страницу каталога"):
        store_page.open()

    with allure.step("Клик на название продукт Sony xperia z5"):
        store_page.product_click_by_title("Sony xperia z5")

    expect(driver).to_have_url("https://www.demoblaze.com/prod.html?idp_=6")

# Не знала какой сделать отрицательный тест, поэтому придумала тот, где после нажатия на кнопку осуществляется переход в корзину
@allure.title("Переход на страницу корзины из карточки товара Sony xperia z5")
def test_product_page(driver):
    product_page = CartProduct(driver)
    with allure.step("Открываем страницу продукта Sony xperia z5"):
        product_page.open()

    with allure.step("Нажимаем кнопку 'Add to cart'"):
        product_page.product_add_to_cart_click()

    expect(driver).to_have_url("https://www.demoblaze.com/cart.html#")
