def bankDataEntity(item) -> dict:
    return {
        "agency": item["agency"],
        "account": item["account"],
        "bank": item["bank"]
    }
def bankDataEntityList(entity) -> list:
    return [bankDataEntity(item) for item in entity]