from repositories.item_repository import ItemRepository

class ItemService:
    def __init__(self):
        self.repo = ItemRepository()

    def daftar(self):
        return self.repo.load()

    def tambah(self, item):
        items = self.repo.load()
        items.append(item)
        self.repo.save(items)

    def update_stok(self, item_id, jumlah):
        items = self.repo.load()
        for item in items:
            if item.id == item_id:
                item.stok += jumlah
        self.repo.save(items)

    def get_by_id(self, item_id):
        items = self.repo.load()
        for item in items:
            if item.id == item_id:
                return item
        return None