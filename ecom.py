import streamlit as st

def initialize_session_state():
    # Initialize the cart if it doesn't exist
    if 'cart' not in st.session_state:
        st.session_state.cart = {}

def add_to_cart(product, quantity):
    # Add or update the product quantity in the cart
    if product in st.session_state.cart:
        st.session_state.cart[product] += quantity
    else:
        st.session_state.cart[product] = quantity

def remove_from_cart(product):
    # Remove the product from the cart
    if product in st.session_state.cart:
        del st.session_state.cart[product]

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

    # Initialize session state for the shopping cart
    initialize_session_state()

    # --- Sidebar: Product Selection ---
    st.sidebar.header("Add Product to Cart")
    selected_product = st.sidebar.selectbox("Select a product", list(products.keys()))
    quantity = st.sidebar.number_input("Quantity", min_value=1, value=1, step=1)

    if st.sidebar.button("Add to Cart"):
        add_to_cart(selected_product, quantity)
        st.sidebar.success(f"Added {quantity} x {selected_product} to your cart.")

    # --- Main Area: Shipping Address ---
    st.header("Checkout Information")
    st.subheader("Shipping Address")
    shipping_name = st.text_input("Name")
    shipping_address = st.text_input("Address")
    shipping_city = st.text_input("City")
    shipping_state = st.text_input("State/Province")
    shipping_zip = st.text_input("Zip/Postal Code")
    shipping_country = st.text_input("Country")

    # --- Main Area: Shopping Cart ---
    st.header("Shopping Cart")
    if st.session_state.cart:
        total_cost = 0
        for product, qty in st.session_state.cart.items():
            cost = products[product] * qty
            total_cost += cost
            st.write(f"**{product}**: {qty} x ${products[product]} = ${cost}")
            # Button to remove each product from the cart
            if st.button(f"Remove {product}", key=product):
                remove_from_cart(product)
                st.experimental_rerun()  # Rerun to update the cart immediately

        st.write("---")
        st.write(f"### Total: ${total_cost}")
    else:
        st.write("Your cart is empty. Please add some products from the sidebar.")

    # --- Place Order Section ---
    if st.button("Place Order"):
        # Check if all shipping details are provided and cart is not empty
        if (st.session_state.cart and shipping_name and shipping_address and 
            shipping_city and shipping_state and shipping_zip and shipping_country):
            st.success("Order placed successfully!")
            st.write("**Shipping Information:**")
            st.write(f"Name: {shipping_name}")
            st.write(f"Address: {shipping_address}")
            st.write(f"City: {shipping_city}")
            st.write(f"State/Province: {shipping_state}")
            st.write(f"Zip/Postal Code: {shipping_zip}")
            st.write(f"Country: {shipping_country}")
            # Optionally clear the cart after placing the order
            st.session_state.cart = {}
        else:
            st.error("Please ensure your cart is not empty and all shipping details are provided.")

if __name__ == "__main__":
    main()
