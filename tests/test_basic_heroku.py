from pages.go_to import Goto
from playwright.sync_api import Page, expect
import pytest

pytestmark = pytest.mark.ui

def test_add_remove(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a basic add/remove elements test
    heroku.heroku_go_to("add_remove_elements/")
    page.click("text=Add Element")
    assert page.locator("text=Delete").is_visible()
    page.click("text=Delete")
    assert not page.locator("text=Delete").is_visible()

def test_checkboxes(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a basic checkboxes test
    heroku.heroku_go_to("checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    expect(checkboxes).to_have_count(2)
    checkboxes.nth(0).check()
    expect(checkboxes.nth(0)).to_be_checked()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(1)).not_to_be_checked()

def test_dynamic_content(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a dynamic content test
    heroku.heroku_go_to("dynamic_content")
    contents_before = page.locator(".large-10.columns").all_text_contents()
    page.reload()
    contents_after = page.locator(".large-10.columns").all_text_contents()
    assert contents_before != contents_after

def test_form_authentication(page: Page) -> None:
    heroku = Goto(page)
    
    # This is a placeholder for a form authentication test
    heroku.heroku_go_to("login")
    page.fill("input#username", "tomsmith")
    page.fill("input#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator("div.flash.success")).to_contain_text("You logged into a secure area!")
    
def test_dropdown(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a dropdown test
    heroku.heroku_go_to("dropdown")
    page.select_option("select#dropdown", "1")
    expect(page.locator("select#dropdown")).to_have_value("1")
    page.select_option("select#dropdown", "2")
    expect(page.locator("select#dropdown")).to_have_value("2")

def test_dynamic_loading(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a dynamic loading test
    heroku.heroku_go_to("dynamic_loading/1")
    page.click("button")
    expect(page.locator("#finish")).to_have_text("Hello World!")

def test_floating_menu(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a floating menu test
    heroku.heroku_go_to("floating_menu")
    menu = page.locator("#menu")
    expect(menu).to_be_visible()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(menu).to_be_visible()

def test_horizontal_slider(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a horizontal slider test
    heroku.heroku_go_to("horizontal_slider")
    slider = page.locator("input[type='range']")
    slider.fill("4")
    expect(page.locator("#range")).to_have_text("4")

def test_hovers(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a hovers test
    heroku.heroku_go_to("hovers")
    avatars = page.locator(".figure")
    expect(avatars).to_have_count(3)
    avatars.nth(0).hover()
    expect(avatars.nth(0).locator("h5")).to_have_text("name: user1")
    avatars.nth(1).hover()
    expect(avatars.nth(1).locator("h5")).to_have_text("name: user2")
    avatars.nth(2).hover()
    expect(avatars.nth(2).locator("h5")).to_have_text("name: user3")

def test_drag_and_drop(page: Page) -> None:
    heroku = Goto(page)

    # This is a placeholder for a drag and drop test
    heroku.heroku_go_to("drag_and_drop")
    box_a = page.locator("#column-a")
    box_b = page.locator("#column-b")
    box_a.drag_to(box_b)
    expect(box_a).to_have_text("B")
    expect(box_b).to_have_text("A")