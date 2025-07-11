import csv, os

FILENAME = 'keuangan.csv'
FIELDNAMES = ['tanggal', 'jenis', 'kategori', 'deskripsi', 'nominal']

def baca_data():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []

        for row in reader:
            if all(k in row for k in FIELDNAMES):
                try:
                    row['nominal'] = int(row['nominal'])
                    row['jenis'] = row['jenis'].strip().lower()  # ❗Bersihkan spasi & kecilkan
                    row['kategori'] = row['kategori'].strip()
                    row['deskripsi'] = row['deskripsi'].strip()
                    row['tanggal'] = row['tanggal'].strip()
                    data.append(row)
                except ValueError:
                    continue
        return data

def simpan_data(data):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def tambah_data_baru(data_baru):
    file_baru = (not os.path.exists(FILENAME)) or os.path.getsize(FILENAME) == 0

    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file_baru:
            writer.writeheader()

        writer.writerow(data_baru)