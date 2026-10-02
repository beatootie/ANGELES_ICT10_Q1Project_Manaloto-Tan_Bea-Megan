from pyscript import document


def create_order(event):

    customer_name = document.querySelector("#customer_name").value 

    espresso_price = 89
    latte_price = 119
    iced_tea_price = 79
    brownie_price = 99

    order_list = "" 
    total = 0 

    if document.querySelector("#item1").checked:
        order_list += f"Espresso - ₱{espresso_price}<br>"
        total += espresso_price

    if document.querySelector("#item2").checked:
        order_list += f"Latte - ₱{latte_price}<br>"
        total += latte_price

    if document.querySelector("#item3").checked:
        order_list += f"Iced Tea - ₱{iced_tea_price}<br>"
        total += iced_tea_price

    if document.querySelector("#item4").checked:
        order_list += f"Brownie - ₱{brownie_price}<br>"
        total += brownie_price

    if customer_name == "":
        document.querySelector("#result").innerHTML = "Please enter your name."
        return

    if order_list == "":
        document.querySelector("#result").innerHTML = "Please select at least one item."
        return

    document.querySelector("#result").innerHTML = f"""
    Customer: {customer_name}<br><br>
    {order_list}<br>
    
    Total: ₱{total}
    """
