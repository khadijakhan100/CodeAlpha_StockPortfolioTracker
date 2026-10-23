import streamlit as st

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Portfolio Tracker")
st.subheader("Manage your stock investments in one place")

st.info("Welcome! Add your stocks to calculate your total investment.")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

st.write("### Available Stocks")

for stock, price in stock_prices.items():
    st.write(f"**{stock}** — ${price} per share")

st.caption("Note: These are sample prices for demonstration, not live market prices.")

st.divider()
st.header("💼 Add Your Investment")

stock = st.selectbox(
    "Select a stock",
    list(stock_prices.keys())
)

quantity = st.number_input(
    "Enter quantity",
    min_value=1,
    step=1
)

investment = stock_prices[stock] * quantity

st.metric(
    label=f"Investment in {stock}",
    value=f"${investment:,.2f}"
)

st.caption("Select a stock and change the quantity to calculate its investment value.")

import pandas as pd

if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

if st.button("➕ Add to Portfolio"):
    st.session_state.portfolio.append({
        "Stock": stock,
        "Quantity": int(quantity),
        "Price": stock_prices[stock],
        "Investment": stock_prices[stock] * quantity
    })

st.divider()
st.header("📊 Your Portfolio")

if st.session_state.portfolio:
    df = pd.DataFrame(st.session_state.portfolio)

    st.dataframe(df, use_container_width=True)

    total = df["Investment"].sum()
    st.metric("💰 Total Portfolio Investment", f"${total:,.2f}")

    st.download_button(
        "⬇️ Download Portfolio CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="stock_portfolio.csv",
        mime="text/csv"
    )
else:
    st.info("Your portfolio is empty. Select a stock and click Add to Portfolio.")
