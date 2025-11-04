from pages.go_to import Goto
from playwright.sync_api import Page, expect
import pytest

pytestmark = [pytest.mark.academy, pytest.mark.ui]

def test_academy_facebook_share(page: Page) -> None:
    academy = Goto(page)

    # This is a placeholder for a borken Facebook share button test
    academy.academy_go_to("articles/")
    with page.expect_popup(timeout=3000) as popup_info:
        page.click("#square-share-a1")

    popup = popup_info.value
    assert "facebook.com" in popup.url, "Facebook share button did not open the correct URL"

def test_academy_contact_form(page: Page) -> None:
    academy = Goto(page)

    # This is a placeholder for a broken contact form test
    academy.academy_go_to("contact-us-form/")
    page.fill("input#first_name", "academy")
    page.get_by_placeholder("Last Name").fill("bugs")
    page.get_by_placeholder("Email").fill("academybugs@bugs.com")
    page.get_by_placeholder("Subject").fill("Testing contact form")
    page.fill("textarea#input-message", "This is a test message for the contact form.")
    page.click("button#submit-contact-form")
    expect(page.locator("div#wpforms-confirmation-1122")).to_contain_text("Thank you for your message")

def test_article_links(page: Page) -> None:
    academy = Goto(page)

    # This is a placeholder for a broken article links test
    academy.academy_go_to("articles/")
    article_links = page.locator("h2.entry-title > a")

    with page.expect_navigation():
        article_links.nth(0).click()
    assert "Why Do I Need To Use Financial Consulting Service?" in page.title()

def test_academy_book_table(page: Page) -> None:
    academy = Goto(page)

    # This is a placeholder for a broken book a table test
    academy.academy_go_to("my-bookings/")
    page.click("input#rtb-date")
    page.locator("[aria-label='November 15, 2025']").click()
    page.click("input#rtb-time")
    page.locator("[aria-label='10:00 PM']").click()
    page.locator("select#rtb-party").select_option("4")
    page.fill("input#rtb-name", "admin")
    page.fill("input#rtb-email", "admin@academybugs.com")
    page.fill("input#rtb-phone", "1234567890")
    page.locator("div.add-message > a").click()
    page.fill("textarea#rtb-message", "Table with a view please.")
    page.click("button#academy-booking-submit")
    expect(page.locator("div.rtb-confirmation-message")).to_contain_text("Thank you for your booking request")
