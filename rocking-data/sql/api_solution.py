import requests

# Make 3 requests for notebook sales analysis
products_response = []
for product_query in ["notebook acer", "notebook samsung", "notebook apple"]:
    products_response.append(
        requests.get(
            "https://api.mercadolibre.com/sites/MLA/search?"
            + "q="
            + product_query
            + "&limit=50#json"
        )
    )


items_response = []
for response in products_response:
    items_query_response = []
    for item in response.json()["results"]:
        items_query_response.append(
            requests.get("https://api.mercadolibre.com/items/" + item["id"])
        )
    items_response.append(items_query_response)

items_list_product = []
for items_response_list in items_response:
    item_results = []
    for item_response in items_response_list:
        item_results.append(item_response.json())
    items_list_product.append(item_results)

items_list_data = []
for item_results in items_list_product:
    items_data = []
    for item in item_results:
        items_data.append(
            {
                "id": item["id"],
                "title": item["title"],
                "price": item["price"],
                "available_quantity": item["available_quantity"],
                "sold_quantity": item["sold_quantity"],
                "condition": item["condition"],
            }
        )
    items_list_data.append(items_data)

acer_data = items_list_data[0]
samsung = items_list_data[1]
apple_data = items_list_data[2]
