# ATM System

This project is a command-line-based ATM (Automated Teller Machine) simulation implemented in Python. It allows users to perform basic banking operations such as checking their balance, depositing funds, and withdrawing funds.

## Features

- **Check Balance**: View the current account balance.
- **Deposit Funds**: Add money to your account.
- **Withdraw Funds**: Withdraw money from your account, with validation to prevent overdrafts.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/reddynalamari/ATM.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd ATM
   ```

## Usage

1. **Run the Program**:

   ```bash
   python main.py
   ```

2. **Interact with the ATM**:

   Follow the on-screen prompts to:
   - Check your balance
   - Deposit funds
   - Withdraw funds
   - Exit the application

## Code Overview

The main components of the code include:

- **ATM Class**: Encapsulates the ATM functionalities:
  - `check_balance()`: Displays the current balance.
  - `deposit(amount)`: Adds the specified amount to the balance.
  - `withdraw(amount)`: Deducts the specified amount from the balance if sufficient funds are available.

- **Main Function**: Provides a menu-driven interface for users to interact with the ATM.


## Future Enhancements

- **Authentication**: Implement user authentication to simulate multiple user accounts.
- **Data Persistence**: Save transaction history and balances to a file or database to maintain state between sessions.
- **GUI**: Develop a graphical user interface for improved user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- **Nalamari Shashidhar Reddy**  
  Passionate developer with expertise in Python and GUI application development.
