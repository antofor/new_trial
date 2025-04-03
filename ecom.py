import streamlit as st

def main():
    st.title("E-commerce Website Simulator")

    # Product catalog with prices (in USD)
    products = {
        "Laptop": 1200,
        "Smartphone": 800,
        "Headphones": 150,
        "Smartwatch": 250,
        "Tablet": 600,
    }

    # Sidebar for selecting products and quantity
    st.sidebar.header("Add Product to Cart")
    selected_product = st.sidebar.selectbox("Select a product", list(products.keys()))
    quantity = st.sidebar.number_input("Quantity", min_value=1, value=1, step=1)

    # Initialize or update the shopping cart using Streamlit's session state
    if 'cart' not in st.session_state:
        st.session_state.cart = {}

    if st.sidebar.button("Add to Cart"):
        if selected_product in st.session_state.cart:
            st.session_state.cart[selected_product] += quantity
        else:
            st.session_state.cart[selected_product] = quantity
        st.sidebar.success(f"Added {quantity} x {selected_product}(s) to your cart.")

    # Main area: Display the shopping cart summary
    st.write("## Shopping Cart")
    if st.session_state.cart:
        total_cost = 0
        for product, qty in st.session_state.cart.items():
            cost = products[product] * qty
            total_cost += cost
            st.write(f"**{product}**: {qty} x ${products[product]} = ${cost}")
        st.write("---")
        st.write(f"### Total: ${total_cost}")
    else:
        st.write("Your cart is empty. Please add some products from the sidebar.")

if __name__ == "__main__":
    main()
