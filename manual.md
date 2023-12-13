# Bunker Marketplace User Manual

## Introduction

Welcome to Bunker Marketplace, a peer-to-peer marketplace application that allows users to buy and sell both digital and physical goods using Monero cryptocurrency. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use the application effectively.

## Installation

To install Bunker Marketplace, follow these steps:

1. Clone the repository from GitHub to your Ubuntu22 server.
2. Make sure you have Python installed on your server.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Set up a MySQL database and configure the connection details in the `main.py` file.
5. Start the application by running the following command:
   ```
   python main.py
   ```
6. Access the marketplace by opening a web browser and entering the server's IP address or domain name.

## Main Functions

### Registration

To register as a user on Bunker Marketplace, follow these steps:

1. Access the marketplace using the provided URL.
2. Click on the "Register" link.
3. Enter your desired username and password.
4. Click the "Register" button.

### Login

To log in to Bunker Marketplace, follow these steps:

1. Access the marketplace using the provided URL.
2. Click on the "Login" link.
3. Enter your username and password.
4. Click the "Login" button.

### Buying and Selling Products

To buy or sell products on Bunker Marketplace, follow these steps:

1. Log in to your account.
2. Browse the available products on the marketplace.
3. Click on a product to view its details.
4. If you want to buy the product, click the "Buy" button and follow the instructions for completing the transaction.
5. If you want to sell a product, click the "Sell" button and provide the necessary details, such as product name, description, price, and category.

### User Withdrawals

To request a withdrawal of your Monero balance, follow these steps:

1. Log in to your account.
2. Go to the "Withdrawals" section.
3. Enter your Monero address and the amount you want to withdraw.
4. Click the "Submit" button to request the withdrawal.
5. Wait for the admin to process your withdrawal request.

### Admin Dashboard

The admin dashboard provides control over various aspects of the marketplace. To access the admin dashboard, follow these steps:

1. Log in to your account using the admin credentials.
2. Click on the "Admin Dashboard" link.

From the admin dashboard, you can perform the following actions:

- Edit hostname and port settings.
- Manage user withdrawal requests.
- Manage users (delete, ban, create, add user balance).
- View all transactions in the marketplace.

## Conclusion

Congratulations! You have successfully installed Bunker Marketplace and learned how to use its main functions. Enjoy buying and selling products in a secure and user-friendly environment. If you have any further questions or need assistance, please contact the admin for support.