import json
import os
from models.item import Item

class ItemRepository:
    FILE = "data/items.json"

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.FILE, "r") as f:
            data = json.load(f)
            return [Item.from_dict(x) for x in data]

    def save(self, items):
        with open(self.FILE, "w") as f:
            json.dump([x.to_dict() for x in items], f, indent=2)