from pi import BuyAPi
from time import sleep


def main():

    buya_pi_list: list[BuyAPi] = [
        BuyAPi("Raspberry Pi 4 - 1gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-1gb/"),
        BuyAPi("Raspberry Pi 4 - 2gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-2gb/"),
        BuyAPi("Raspberry Pi 4 - 4gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-4gb/"),
        BuyAPi("Raspberry Pi 4 - 1gb", "https://www.pishop.ca/product/raspberry-pi-4-model-b-8gb/"),
        BuyAPi("Raspberry Pi Zero 2", "https://www.pishop.ca/product/raspberry-pi-zero-2-w/")]

    # checks stock every 30 min
    while True:
        for pi in buya_pi_list:
            pi.check_stock()
        sleep(1800)  # change this value to adjust frequency


if __name__ == "__main__":
    main()
