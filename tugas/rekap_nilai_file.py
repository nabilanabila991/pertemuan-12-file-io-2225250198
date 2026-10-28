
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai.strip())
                    nim = nim.strip()

                    if not nim:
                        raise ValueError

                    data.append({
                        "nim": nim,
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Baris {nomor_baris} tidak valid: {baris}")
                    continue

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("====================\n")

        if not data:
            file.write("Tidak ada data valid.\n")
            return

        jumlah = len(data)
        total = sum(item["nilai"] for item in data)
        rata_rata = total / jumlah
        minimum = min(item["nilai"] for item in data)
        maksimum = max(item["nilai"] for item in data)
        lulus = sum(1 for item in data if item["nilai"] >= 60)

        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {minimum:.2f}\n")
        file.write(f"Nilai maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {lulus}\n")
        file.write(f"Jumlah belum lulus: {jumlah - lulus}\n")

        file.write("\nDETAIL NILAI\n")
        for item in data:
            status = "Lulus" if item["nilai"] >= 60 else "Belum lulus"
            file.write(
                f"{item['nim']}, {item['nilai']:.2f}, {status}\n"
            )


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    try:
        tulis_rekap(output_file, data)
        print("Rekap berhasil ditulis ke", output_file)
        print("Jumlah data valid:", len(data))

    except OSError as error:
        print("Gagal menulis file rekap:", error)
