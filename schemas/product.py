def prodEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name": item["name"],
        "category": item['category'],
        "quantity": item["quantity"],
        "packprice": item["packprice"],
        "unitprice": item["unitprice"]
    }
    
def productsEntity(entity) -> list:
    return [prodEntity(item) for item in entity]