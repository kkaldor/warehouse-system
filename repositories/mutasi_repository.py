import json
import os
from models.mutasi import Mutasi

class MutasiRepository:
    FILE = "data/mutasi.json"

    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.FILE, "r") as f:
            data = json.load(f)
            return [Mutasi.from_dict(x) for x in data]

    def save(self, mutasi_list):
        with open(self.FILE, "w") as f:
            json.dump([x.to_dict() for x in mutasi_list], f, indent=2)