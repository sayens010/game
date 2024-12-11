def main():
    teka_teki = [
        {"pertanyaan": "Apa ibu kota Indonesia?", "jawaban": "Jakarta"},
        {"pertanyaan": "Sebutkan planet terbesar di tata surya?", "jawaban": "Jupiter"},
        {"pertanyaan": "Siapa penulis Harry Potter?", "jawaban": "J.K. Rowling"},
        {"pertanyaan": "Apa hasil dari 9 + 10?", "jawaban": "19"},
        {"pertanyaan": "Benda apa yang bisa terbang tanpa mesin?", "jawaban": "Burung"},
        {"pertanyaan": "Siapa yang membuat permainan ini?", "jawaban": "Prof. Azwar"},
        {"pertanyaan": "Siapa penemu bom atom?", "jawaban": "Oppenheimer"},
        {"pertanyaan": "Pemain asia barat yang pernah bermain di MU?", "jawaban": "Zidane iqbal"},
        {"pertanyaan": "Ikan bernafas dengan?", "jawaban": "Izin ALLAh"},
        {"pertanyaan": "Kapan tragedi pembantaian MU dilakukan?", "jawaban": "5/3/2023"},
    ]

    print("Selamat datang di permainan Teka-Teki!")
    skor = 0

    for i, teka_teki_item in enumerate(teka_teki):
        print(f"Teka-Teki {i+1}: {teka_teki_item['pertanyaan']}")
        jawaban_pemain = input("Jawabanmu: ")

        if jawaban_pemain.lower() == teka_teki_item['jawaban'].lower():
            print("Jawaban benar!")
            skor += 1
        else:
            print(f"Jawaban salah. Jawaban yang benar adalah: {teka_teki_item['jawaban']}")

    print(f"\nPermainan selesai! Skor akhir kamu adalah: {skor}/{len(teka_teki)}")

if __name__ == "__main__":
    main()
