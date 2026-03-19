def process_data(data):
    match data:
        case {"type": "user", "name": name, "id": user_id}:
            print(f"Processing user: {name} (ID: {user_id})")
        case {"type": "product", "item_id": item_id, "price": price}:
            print(f"Processing product: {item_id} (Price: ${price})")
        case [first, second, *rest]:
            print(
                f"Processing a list with at least two elements: {first}, {second}, and {len(rest)} more."
            )
        case {"text": text}:
            print(text)
        case _:
            print("Unknown data type.")


process_data({"type": "user", "name": "Asus", "id": 123})
process_data({"type": "product", "item_id": "ABC", "price": 99.99})
process_data([1, 2, 3, 4])
process_data({"text": "hello"})
