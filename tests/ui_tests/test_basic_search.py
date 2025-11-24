import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.kiwi_home_page import KiwiHomePage

# connect the feature file
scenarios("../../features/basic_search.feature")

pytestmark = [pytest.mark.ui, pytest.mark.basic_search]

@given(
        parsers.parse("As an not logged user navigate to homepage https://www.kiwi.com/en/"),
        target_fixture="open_homepage"
    )
def open_homepage(page):
    home = KiwiHomePage(page)
    home.load()
    return home


@when("I select one-way trip type")
def select_one_way(open_homepage):
    open_homepage.select_one_way()


@when(parsers.parse("Set as departure airport RTM"))
def set_departure(open_homepage, airport="Rotterdam The Hague"):
    open_homepage.set_departure_airport(airport)


@when(parsers.parse("Set the arrival Airport MAD"))
def set_arrival(open_homepage, airport="Adolfo Suarez"):
    open_homepage.set_arrival_airport(airport)


@when(parsers.parse("Set the departure time 1 week in the future starting current date"))
def set_departure_time_one_week(open_homepage):
    open_homepage.set_departure_date_offset_days(7)


@when("Uncheck the `Check accommodation with booking.com` option")
def uncheck_accommodation(open_homepage):
    open_homepage.uncheck_accommodation_with_booking()


@when("Click the search button")
def click_search(open_homepage):
    open_homepage.click_search()


@then("I am redirected to search results page")
def then_on_results_page(open_homepage, page):
    # check that we are on results page
    assert open_homepage.is_on_results_page(), "Route not found in results page"
