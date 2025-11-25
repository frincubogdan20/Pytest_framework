from datetime import datetime, timedelta, timezone
from playwright.sync_api import Page, expect
import re
import time


class KiwiHomePage:
    URL = "https://www.kiwi.com/en/"

    # Kiwi page locators
    COOKIE_CLOSE_BUTTON = "button[aria-label='Close']"
    SEARCH_MODE = "[data-test^='SearchFormModesPicker-active-"
    ONE_WAY_BUTTON = "[data-test='ModePopupOption-oneWay']"
    FROM_INPUT = "input[id='origin']"
    FROM_INPUT_CLEAR = "[data-test='PlacePickerInputPlace-close']"
    TO_INPUT = "input[id='destination']"
    DEPARTURE_DATE_FIELD = "input[id='outboundDate']"
    DEPARTURE_DATE = "[data-test='CalendarDay']"
    SET_DATES = "button[data-test='SearchFormDoneButton']"
    ACCOMMODATION_CHECKBOX_LABEL = "[data-test='accommodationCheckbox']"
    SEARCH_BUTTON = "[data-test='LandingSearchButton']"
    QUALITY_BUTTON = "button[data-test='SortBy-quality']"

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(self.URL)
        # Close cookie banner if present
        try:
            self.page.wait_for_selector(self.COOKIE_CLOSE_BUTTON, timeout=10000)
            cookie_btn = self.page.locator(self.COOKIE_CLOSE_BUTTON)
            if cookie_btn.count() > 0:
                cookie_btn.first.click()
        except Exception:
            pass
        

    def select_one_way(self):
        # Click one-way if not already selected
        if self.page.locator(f"{self.SEARCH_MODE}oneWay']").count() == 0:
            self.page.locator(f"{self.SEARCH_MODE}']").first.click()
            self.page.locator(self.ONE_WAY_BUTTON).click()


    def set_departure_airport(self, airport_name: str):
        # Clear and type airport code

        self.page.locator(self.FROM_INPUT_CLEAR).click()
        self.page.locator(self.FROM_INPUT).click()
        self.page.locator(self.FROM_INPUT).fill(airport_name)
        # wait for suggestion and press Enter to pick top result
        self.page.wait_for_timeout(500)
        self.page.keyboard.press("Enter")

    def set_arrival_airport(self, airport_name: str):
        self.page.locator(self.TO_INPUT).click()
        self.page.locator(self.TO_INPUT).fill(airport_name)
        self.page.wait_for_timeout(500)
        self.page.keyboard.press("Enter")
        self.page.keyboard.press("Escape")

    def set_departure_date_offset_days(self, offset_days: int = 7):
        """Set departure date to today + offset_days."""
        target_date = datetime.now(timezone.utc).date() + timedelta(days=offset_days)

        # Open date picker and select date
        self.page.locator(self.DEPARTURE_DATE_FIELD).click()
        self.page.wait_for_timeout(500)
        # Select the date in the calendar
        self.page.locator(f"{self.DEPARTURE_DATE}[data-value='{str(target_date)}']").click()
        self.page.locator(self.SET_DATES).click()

    def uncheck_accommodation_with_booking(self):
        # Find accomodation checkbox and make sure it is unchecked.
        self.page.locator(self.ACCOMMODATION_CHECKBOX_LABEL).click()

    def click_search(self):
        self.page.locator(self.SEARCH_BUTTON).first.click()
        # Wait for results to load
        self.page.wait_for_timeout(10000)

    def is_on_results_page(self) -> bool:
        url = self.page.url
        return self.page.locator(self.QUALITY_BUTTON).is_visible() and "search" in url
