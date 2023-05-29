def bubble_sort(Nilai_ujian_siswa):
    n = len(Nilai_ujian_siswa)
    for i in range(n-1):
        for j in range(n-i-1):
            if Nilai_ujian_siswa[j] > Nilai_ujian_siswa[j+1]:
                Nilai_ujian_siswa[j], Nilai_ujian_siswa[j+1] = Nilai_ujian_siswa[j+1], Nilai_ujian_siswa[j]
                
Nilai_ujian_siswa = [78,65,90,82,70]
bubble_sort(Nilai_ujian_siswa)
print("Urutan nilai siswa : ",Nilai_ujian_siswa)