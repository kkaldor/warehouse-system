class Item:
    def __init__(self, item_id, nama, kategori, stok=0, min_stok=0):
        self.id = item_id
        self.nama = nama
        self.kategori = kategori
        self.stok = stok
        self.min_stok = min_stok

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "kategori": self.kategori,
            "stok": self.stok,
            "min_stok": self.min_stok
        }

    @staticmethod
    def from_dict(data):
        return Item(
            data["id"],
            data["nama"],
            data["kategori"],
            data["stok"],
            data["min_stok"]
        )