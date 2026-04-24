from core.item_service import ItemService
from core.mutasi_service import MutasiService
from models.item import Item

class ConsoleUI:
    def __init__(self):
        self.item_service = ItemService()
        self.mutasi_service = MutasiService()

    def run(self):
        while True:
            print("\n=== Sistem Manajemen Gudang ===")
            print("1. Lihat Barang")
            print("2. Tambah Barang")
            print("3. Stok Masuk")
            print("4. Stok Keluar")
            print("5. Lihat Mutasi Stok")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.menu_daftar_barang()
            elif pilihan == "2":
                self.menu_tambah_barang()
            elif pilihan == "3":
                self.menu_stok_masuk()
            elif pilihan == "4":
                self.menu_stok_keluar()
            elif pilihan == "5":
                self.menu_daftar_mutasi()
            elif pilihan == "0":
                break
            else:
                print("Pilihan tidak valid.")

    def menu_daftar_barang(self):
        items = self.item_service.daftar()
        print("\n--- Daftar Barang ---")
        for i in items:
            print(f"{i.id} | {i.nama} | Stok: {i.stok}")

    def menu_tambah_barang(self):
        id_item = input("ID Barang: ")
        nama = input("Nama Barang: ")
        kategori = input("Kategori: ")
        min_stok = int(input("Minimal Stok: "))

        item = Item(id_item, nama, kategori, 0, min_stok)
        self.item_service.tambah(item)
        print("Barang ditambahkan.")

    def menu_stok_masuk(self):
        item_id = input("ID Barang: ")
        jumlah = int(input("Jumlah: "))

        self.item_service.update_stok(item_id, jumlah)
        self.mutasi_service.catat_mutasi(item_id, "masuk", jumlah)

        print("Stok masuk berhasil dicatat.")

    def menu_stok_keluar(self):
        item_id = input("ID Barang: ")
        jumlah = int(input("Jumlah: "))

        self.item_service.update_stok(item_id, -jumlah)
        self.mutasi_service.catat_mutasi(item_id, "keluar", jumlah)

        print("Stok keluar berhasil dicatat.")

    def menu_daftar_mutasi(self):
        mutasi = self.mutasi_service.semua()
        print("\n--- Riwayat Mutasi ---")
        for m in mutasi:
            print(f"{m.id} | {m.barang_id} | {m.jenis} | {m.jumlah} | {m.tanggal}")