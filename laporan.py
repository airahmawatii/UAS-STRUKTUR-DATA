from data import baca_data
from collections import defaultdict
from saldo import cek_saldo

def laporan_bulanan_tahunan() -> None:
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return

    bulanan_in = defaultdict(int)
    bulanan_out = defaultdict(int)
    tahunan_in = defaultdict(int)
    tahunan_out = defaultdict(int)

    for d in data:
        tahun, bulan, *_ = d["tanggal"].split("-")
        jenis = d["jenis"].strip().lower()  # ❗Tambahan penting

        if jenis == "pemasukan":
            bulanan_in[f"{tahun}-{bulan}"] += d["nominal"]
            tahunan_in[tahun] += d["nominal"]
        elif jenis == "pengeluaran":
            bulanan_out[f"{tahun}-{bulan}"] += d["nominal"]
            tahunan_out[tahun] += d["nominal"]

    print("\n📅 Laporan Bulanan:")
    print(f"{'Bulan':<10} | {'Pemasukan':>12} | {'Pengeluaran':>13}")
    print("-" * 42)

    semua_bulan = sorted(set(bulanan_in) | set(bulanan_out))
    for bln in semua_bulan:
        masuk = bulanan_in.get(bln, 0)
        keluar = bulanan_out.get(bln, 0)
        print(f"{bln:<10} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    print("\n📆 Laporan Tahunan:")
    print(f"{'Tahun':<6} | {'Pemasukan':>12} | {'Pengeluaran':>13}")
    print("-" * 42)

    semua_tahun = sorted(set(tahunan_in) | set(tahunan_out))
    for thn in semua_tahun:
        masuk = tahunan_in.get(thn, 0)
        keluar = tahunan_out.get(thn, 0)
        print(f"{thn:<6} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    print("\n💰 Saldo Akhir:")
    cek_saldo()