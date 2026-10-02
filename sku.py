from pyscript import document


def generate_sku(event):

    category = document.querySelector("#category").value  
    product_name = document.querySelector("#product_name").value 
    stock_text = document.querySelector("#stock_quantity").value 

    if product_name == "" or stock_text == "":
        document.querySelector("#result").innerText = "Please fill in all fields."
        return

    stock_quantity = int(stock_text) 

    category_code = category[:3].upper()  
    product_code = product_name[:3].upper() 

    sku = category_code + product_code + str(stock_quantity)
    
    document.querySelector("#result").innerText = f"Generated SKU: {sku}"
