from pages.go_to import Goto
from playwright.sync_api import Page, expect

# def test_add_remove(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a basic add/remove elements test
#     heroku.heroku_go_to("add_remove_elements/")
#     page.click("text=Add Element")
#     assert page.locator("text=Delete").is_visible()
#     page.click("text=Delete")
#     assert not page.locator("text=Delete").is_visible()

# def test_checkboxes(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a basic checkboxes test
#     heroku.heroku_go_to("checkboxes")
#     checkboxes = page.locator("input[type='checkbox']")
#     expect(checkboxes).to_have_count(2)
#     checkboxes.nth(0).check()
#     expect(checkboxes.nth(0)).to_be_checked()
#     checkboxes.nth(1).uncheck()
#     expect(checkboxes.nth(1)).not_to_be_checked()

# def test_dynamic_content(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a dynamic content test
#     heroku.heroku_go_to("dynamic_content")
#     contents_before = page.locator(".large-10.columns").all_text_contents()
#     page.reload()
#     contents_after = page.locator(".large-10.columns").all_text_contents()
#     assert contents_before != contents_after

# def test_form_authentication(page: Page) -> None:
#     heroku = Goto(page)
    
#     # This is a placeholder for a form authentication test
#     heroku.heroku_go_to("login")
#     page.fill("input#username", "tomsmith")
#     page.fill("input#password", "SuperSecretPassword!")
#     page.click("button[type='submit']")
#     expect(page.locator("div.flash.success")).to_contain_text("You logged into a secure area!")
    
# def test_dropdown(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a dropdown test
#     heroku.heroku_go_to("dropdown")
#     page.select_option("select#dropdown", "1")
#     expect(page.locator("select#dropdown")).to_have_value("1")
#     page.select_option("select#dropdown", "2")
#     expect(page.locator("select#dropdown")).to_have_value("2")

# def test_dynamic_loading(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a dynamic loading test
#     heroku.heroku_go_to("dynamic_loading/1")
#     page.click("button")
#     expect(page.locator("#finish")).to_have_text("Hello World!")

# def test_floating_menu(page: Page) -> None:
#     heroku = Goto(page)

#     # This is a placeholder for a floating menu test
#     heroku.heroku_go_to("floating_menu")
#     menu = page.locator("#menu")
#     expect(menu).to_be_visible()
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     expect(menu).to_be_visible()

def test_horizontal_slider(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a horizontal slider test
    heroku.heroku_go_to("horizontal_slider")
    slider = page.locator("input[type='range']")
    slider.fill("4")
    expect(page.locator("#range")).to_have_text("4")