import datetime

class Mutasi:
    def __init__(self, mutasi_id, barang_id, jenis, jumlah, tanggal=None):
        self.id = mutasi_id
        self.barang_id = barang_id
        self.jenis = jenis
        self.jumlah = jumlah
        self.tanggal = tanggal or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "barang_id": self.barang_id,
            "jenis": self.jenis,
            "jumlah": self.jumlah,
            "tanggal": self.tanggal
        }

    @staticmethod
    def from_dict(data):
        return Mutasi(
            data["id"],
            data["barang_id"],
            data["jenis"],
            data["jumlah"],
            data["tanggal"]
        )