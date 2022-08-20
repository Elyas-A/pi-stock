from pi import CanPi
from pi import BuyAPi
from time import sleep


def main():

    can_pi_list: list[CanPi] = []
    buya_pi_list: list[BuyAPi] = []

    # raspberry pi 4's
    can_pi_list.append(CanPi("Raspberry Pi 4 - 1gb", "https://www.canakit.com/raspberry-pi-pico-w.html"))
    can_pi_list.append(CanPi("Raspberry Pi 4 - 2gb", "https://www.canakit.com/raspberry-pi-4-2gb.html"))
    can_pi_list.append(CanPi("Raspberry Pi 4 - 4gb", "https://www.canakit.com/raspberry-pi-4-4gb.html"))
    can_pi_list.append(CanPi("Raspberry Pi 4 - 8gb", "https://www.canakit.com/raspberry-pi-4-8gb.html"))
    buya_pi_list.append(BuyAPi("Raspberry Pi 4 - 1gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-1gb/"))
    buya_pi_list.append(BuyAPi("Raspberry Pi 4 - 2gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-2gb/"))
    buya_pi_list.append(BuyAPi("Raspberry Pi 4 - 4gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-4gb/"))
    buya_pi_list.append(BuyAPi("Raspberry Pi 4 - 1gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/"))

    # raspberry pi zero 2's
    can_pi_list.append(CanPi("Raspberry Pi Zero 2", "https://www.canakit.com/raspberry-pi-zero-2-w.html"))
    buya_pi_list.append(BuyAPi("Raspberry Pi Zero 2", "https://www.pishop.ca/product/raspberry-pi-zero-2-w/"))

    # checks stock every 30 min
    while True:
        for pi in can_pi_list:
            pi.check_stock()
        for pi in buya_pi_list:
            pi.check_stock()
        sleep(1800)


if __name__ == "__main__":
    main()
