# Currency Converter

A simple Python currency converter that fetches current exchange rates from the ExchangeRate-API and converts an amount from one currency to another.

## Features

- Converts between supported currencies
- Retrieves exchange rates from an online API
- Supports command-line input
- Includes a Streamlit application interface
- Uses Python and the `requests` library

## Project Structure

```text
currency-convert/
├── src/
│   ├── main.py
│   ├── app.py
│   └── currency-convertor.py
└── README.md
```

## Requirements

- Python 3.8 or later
- Internet connection
- `requests`
- `streamlit` if using the Streamlit interface

## Installation

Clone the repository:

```bash
git clone https://github.com/iamhoss14/currency-convert.git
cd currency-convert
```

Install the required dependencies:

```bash
pip install requests streamlit
```

## Usage

### Command-Line Converter

Run the command-line application:

```bash
python src/main.py
```

Enter the requested values:

```text
Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., CAD): CAD
Enter the amount in USD: 100
```

The program will retrieve the exchange rate and display the converted amount.

### Streamlit Application

Run the Streamlit application with:

```bash
streamlit run src/app.py
```

This will open the application in your browser.

## Supported Currency Codes

Use standard three-letter currency codes, such as:

- `USD` - United States Dollar
- `CAD` - Canadian Dollar
- `EUR` - Euro
- `GBP` - British Pound
- `JPY` - Japanese Yen
- `AUD` - Australian Dollar
- `INR` - Indian Rupee

The available currencies depend on the exchange-rate API.

## API

This project uses the following endpoint:

```text
https://api.exchangerate-api.com/v4/latest/{BASE_CURRENCY}
```

For example:

```text
https://api.exchangerate-api.com/v4/latest/USD
```

## Notes

- The converter requires an active internet connection.
- Currency codes should be entered in uppercase.
- Exchange rates may change over time.
- The API may return an error for unsupported currency codes or unavailable services.

## License

This project is available for personal and educational use.
