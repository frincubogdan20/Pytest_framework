from playwright.sync_api import Page, expect
import pytest

pytestmark = [pytest.mark.heroku, pytest.mark.ui]

def test_add_remove(page: Page, heroku_base_url) -> None:

    # This is a basic add/remove elements test
    page.goto(f"{heroku_base_url}/add_remove_elements/")
    page.click("text=Add Element")
    assert page.locator("text=Delete").is_visible()
    page.click("text=Delete")
    assert not page.locator("text=Delete").is_visible()

def test_checkboxes(page: Page, heroku_base_url) -> None:

    # This is a basic checkbox test
    page.goto(f"{heroku_base_url}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    expect(checkboxes).to_have_count(2)
    checkboxes.nth(0).check()
    expect(checkboxes.nth(0)).to_be_checked()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(1)).not_to_be_checked()

def test_dynamic_content(page: Page, heroku_base_url) -> None:

    # This is a dynamic content test
    page.goto(f"{heroku_base_url}/dynamic_content")
    contents_before = page.locator(".large-10.columns").all_text_contents()
    page.reload()
    contents_after = page.locator(".large-10.columns").all_text_contents()
    assert contents_before != contents_after

def test_form_authentication(page: Page, heroku_base_url) -> None:
    
    # This is a form authentication test
    page.goto(f"{heroku_base_url}/login")
    page.fill("input#username", "tomsmith")
    page.fill("input#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page.locator("div.flash.success")).to_contain_text("You logged into a secure area!")
    
def test_dropdown(page: Page, heroku_base_url) -> None:

    # This is a dropdown test
    page.goto(f"{heroku_base_url}/dropdown")
    page.select_option("select#dropdown", "1")
    expect(page.locator("select#dropdown")).to_have_value("1")
    page.select_option("select#dropdown", "2")
    expect(page.locator("select#dropdown")).to_have_value("2")

def test_dynamic_loading(page: Page, heroku_base_url) -> None:

    # This is a dynamic loading test
    page.goto(f"{heroku_base_url}/dynamic_loading/1")
    page.click("button")
    expect(page.locator("#finish")).to_have_text("Hello World!")

def test_floating_menu(page: Page, heroku_base_url) -> None:

    # This is a floating menu test
    page.goto(f"{heroku_base_url}/floating_menu")
    menu = page.locator("#menu")
    expect(menu).to_be_visible()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(menu).to_be_visible()

def test_horizontal_slider(page: Page, heroku_base_url) -> None:

    # This is a horizontal slider test
    page.goto(f"{heroku_base_url}/horizontal_slider")
    slider = page.locator("input[type='range']")
    slider.fill("4")
    expect(page.locator("#range")).to_have_text("4")

def test_hovers(page: Page, heroku_base_url) -> None:

    # This is a hovers test
    page.goto(f"{heroku_base_url}/hovers")
    avatars = page.locator(".figure")
    expect(avatars).to_have_count(3)
    avatars.nth(0).hover()
    expect(avatars.nth(0).locator("h5")).to_have_text("name: user1")
    avatars.nth(1).hover()
    expect(avatars.nth(1).locator("h5")).to_have_text("name: user2")
    avatars.nth(2).hover()
    expect(avatars.nth(2).locator("h5")).to_have_text("name: user3")

def test_drag_and_drop(page: Page, heroku_base_url) -> None:

    # This is a drag and drop test
    page.goto(f"{heroku_base_url}/drag_and_drop")
    box_a = page.locator("#column-a")
    box_b = page.locator("#column-b")
    box_a.drag_to(box_b)
    expect(box_a).to_have_text("B")
    expect(box_b).to_have_text("A")
