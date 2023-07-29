def userEntity(item) -> dict:
    return {
        "social_reason": item["social_reason"],
        "telephone": item["telephone"],
        "address": item["address"],
        "register_date": item["register_date"],
        "bank_data": item["bank_data"]
    }

def userEntityList(entity) -> list:
    return [userEntity(item) for item in entity]