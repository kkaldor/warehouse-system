from repositories.mutasi_repository import MutasiRepository
from models.mutasi import Mutasi
import uuid

class MutasiService:
    def __init__(self):
        self.repo = MutasiRepository()

    def catat_mutasi(self, barang_id, jenis, jumlah):
        mutasi = Mutasi(
            mutasi_id=str(uuid.uuid4())[:8],
            barang_id=barang_id,
            jenis=jenis,
            jumlah=jumlah
        )
        mutasi_list = self.repo.load()
        mutasi_list.append(mutasi)
        self.repo.save(mutasi_list)

    def semua(self):
        return self.repo.load()