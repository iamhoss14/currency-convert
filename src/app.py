import streamlit as st
from constans import CURRENCIES
from currency_convertor import get_exchange_rate, convert_currency
st.title(":dollar: Currency Converter ")
st.markdown(
    """This tool is allows you to instantly convert amounts between diffrent currencies. Enter the amount and choose the currencies to see the result.
"""
)
base_currency = st.selectbox("From currency (Base): ", CURRENCIES)
target_currency = st.selectbox("To currency (Target): ", CURRENCIES)
amount  = st.number_input("Enter amount: ", min_value=0.0, value=100.0)
if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount,exchange_rate)
    if exchange_rate: 
            converted_amountr = convert_currency(amount,exchange_rate)
            st.success(f"✅Exchange Rate: {exchange_rate:.4f}")
            col1,col2,col3 = st.columns(3)
            col1.metric(label="Base Currency", value=f"{amount:.4f}{base_currency}")
            col2.markdown(
    """
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 70px;
        font-size: 32px;
        font-weight: bold;
    ">
        ➜
    </div>
    """,
    unsafe_allow_html=True
)
            col3.metric(label="Target Currency", value=f"{converted_amount:.4f}{target_currency}")

        
    else: 
        st.error("Error fetching exchange rate.")


st.markdown("---")

st.markdown(
    """
    ## 💱 About This Tool

    🌍 **Currency Converter** is a simple and fast tool for converting
    amounts between different currencies.

    💰 Enter the amount you want to convert, select your **base currency**
    and **target currency**, and the tool will calculate the converted
    amount using the current exchange rate.

    ### ✨ Features

    - 💵 Convert between multiple currencies
    - 🔄 Get exchange rates automatically
    - ⚡ Fast and simple conversion
    - 🎯 Easy-to-use interface
    - 📊 Clear and readable results

    ### 🛠️ Built With

    🐍 **Python**  
    🎈 **Streamlit**  
    🌐 **Exchange Rate API**

    > 💡 **Tip:** Exchange rates can change over time, so the result should
    > be considered an estimate based on the rate available when the
    > conversion is performed.

    🚀 **Built to make currency conversion simple, quick, and accessible.**
    """,
    unsafe_allow_html=True
)
