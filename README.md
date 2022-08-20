# pi-stock
 Get a notification when a raspberry pi 4 or pi zero 2 comes in stock on PiShop.ca or canakit.com .

## Setup
This program runs on python3.10.

Using pip, download the following packages:
- beautifulsoup4
- requests
- python-dotenv

Alternatively, you may create a virtual environment using the requirements.txt file.

## Usage
You will need a gmail account with 2-Step Verification activately. This email will be used to send the notifications.

Once your gmail account is setup, head over to your [google account](https://myaccount.google.com/security) page, and create an app password.

Create a .env file in the repository. In the .env file you will need to enter the email of the account that will be used to send notification, the app password for it, and the email of the recipient of the notification. Check the .env.example file on how to input that information.

Finally, simply run main.py and you will get a email notification if a raspberry pi is in stock.
