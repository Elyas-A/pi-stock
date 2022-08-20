import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet
from notify import send_notification


class CanPi:
    """
    CanPi class
    """
    def __init__(self, name: str, url: str) -> None:
        """
        parameters: name - str, required
                           the name of the product
                    url - str, required
                          the url of the product
        """
        self.__name: str = name
        self.__url: str = url
        self.__alerted: bool = False

    def check_stock(self) -> None:
        """
        checks if the item is in stock

        parameters: None
        returns: None
        """
        # gets the current status of the product
        page: requests.Response = requests.get(self.__url)
        soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        results: BeautifulSoup = soup.find("div", id="ProductAddToCartDiv")

        # if the product is in stock, send a notification to the user
        if results.text.strip() != "Pre-Orders Sold Out":
            self.alert()
        else:
            self.__alerted = False

    def alert(self) -> None:
        """
        sends out alert when product is in stock

        parameters: None
        returns: None
        """
        # if user has already been notified, then do not send a notification again
        if not self.__alerted:
            send_notification(f"{self.__name} is in stock", self.__url)
        self.__alerted = True


class BuyAPi:

    def __init__(self, name: str, url: str) -> None:
        """
        parameters: name - str, required
                           the name of the product
                    url - str, required
                          the url of the product
        """
        self.__name: str = name
        self.__url: str = url
        self.__alerted: bool = False

    def check_stock(self) -> None:
        """
        checks if the item is in stock

        parameters: None
        returns: None
        """
        # gets the current status of the product
        page: requests.Response = requests.get(self.__url)
        soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        results: BeautifulSoup = soup.find("div", class_="form-action")

        # if product is in stock, send a notification to the user
        if str(results.find("input", value=True)['value']) != "Out of stock":
            self.alert()
        else:
            self.__alerted = False

    def alert(self) -> None:
        """
        send in stock alert message

        parameters: None
        returns: None
        """
        # if user has already been notified, then do not send a notification again
        if not self.__alerted:
            send_notification(f"{self.__name} is in stock", self.__url)
        self.__alerted = True
        pass
