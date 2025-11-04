from playwright.sync_api import Page

class Goto:
    def __init__(self, page: Page) -> None:
        self.page = page

    def heroku_go_to(self, testpage: str) -> None:
        URL = "https://the-internet.herokuapp.com/"
        self.page.goto(f"{URL}{testpage}")

    def academy_go_to(self, testpage: str) -> None:
        URL = "https://academybugs.com/"
        self.page.goto(f"{URL}{testpage}")
