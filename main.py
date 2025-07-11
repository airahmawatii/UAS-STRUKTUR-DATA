# === main.py ===

# Import fungsi dari modul lain
from tambah_transaksi import tambah_transaksi # untuk menambahkan data transaksi
from tampilkan_transaksi import tampilkan_transaksi # untuk menampilkan semua transaksi   
from hapus_transaksi import hapus_transaksi   # untuk menghapus transaksi berdasarkan nomor/urutan         
from ubah_transaksi import ubah_transaksi     # untuk mengedit data transaksi
from laporan import laporan_bulanan_tahunan  # tampilkan rekap per bulan & tahun
from saldo import cek_saldo                  # hitung dan tampilkan saldo akhir

# Fungsi utama menampilkan menu dan menangani pilihan user
def menu():
    while True:
        print("=== SISTEM MANAJEMEN KEUANGAN PRIBADI ===")
        print("1. Tambah Catatan Transaksi")
        print("2. Lihat Semua Catatan Transaksi")
        print("3. Hapus Catatan Transaksi")
        print("4. Ubah Catatan Transaksi")
        print("5. Laporan Bulanan dan Tahunan")
        print("6. Cek Saldo")
        print("0. Keluar")

        # Input pilihan dari user
        pilih = input("Pilih menu (1-6): ")

        # Sesuaikan aksi berdasarkan pilihan user
        if pilih == '1':
            tambah_transaksi()               # Tambah data baru
        elif pilih == '2':
            tampilkan_transaksi()            # Tampilkan semua transaksi
        elif pilih == '3':
            hapus_transaksi()                # Hapus transaksi tertentu
        elif pilih == '4':
            ubah_transaksi()                 # Edit transaksi tertentu
        elif pilih == '5':
            laporan_bulanan_tahunan()        # Tampilkan rekap bulanan/tahunan
        elif pilih == '6':
            cek_saldo()                      # Hitung dan tampilkan saldo
        elif pilih == '0':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break                             # Keluar dari program
        else:
            print("Pilihan tidak valid.")     # Jika input tidak sesuai menu

# Program dijalankan dari sini
if __name__ == "__main__":
    menu()  # panggil fungsi utama saat file dijalankan langsung
