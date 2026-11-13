---
id: TC-FA-FAREG-BE-130-download-isi-berkas
title: "Download: isi berkas per tipe kolom"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-DL-4]
smoke: []
dependsOn: []
trace:
  EB-DL-4: [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 21, 24, 27, 29]
owner: BE
---
# Download: isi berkas per tipe kolom

## Prerequisites
- Aktor: Rina (Total Control, seluruh client).
- Data:
  - DU-130-1: Group `Server Room Berkas {runId}`, Assignable, path penuh `Jakarta Office {runId} > Floor 2 Berkas {runId} > Server Room Berkas {runId}`.
  - DU-130-2: Group `Floor 2 Berkas {runId}`, Assignable, path penuh `Bandung Office {runId} > Floor 2 Berkas {runId}`.
  - DU-130-3: Group `Floor 2 Berkas {runId}`, Assignable, path penuh `Jakarta Office {runId} > Floor 2 Berkas {runId}`.
  - DU-130-4: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-130`, TAG Type `Non-TAG`; isi setiap batch Draft di bawah adalah aset `Meja Kerja {runId}` sebanyak Total Asset.
  - DU-130-5: batch Draft Group DU-130-1, Origin `—`, Total Asset `12` (Ready `0`), Progress `0%`, Requested By `Rina Wulandari`, Last Updated `T0 − 1 jam`.
  - DU-130-6: batch Draft Group DU-130-2, Origin `REG-20261105-00007`, Total Asset `5` (Ready `3`), Progress `60%`, Requested By `Siti Nur Rahmawati` (tampil `Siti N`), Last Updated `T0 − 2 jam`.
  - DU-130-7: batch Draft Group DU-130-3, Origin `—`, Total Asset `30` (Ready `30`), Progress `100%`, Requested By `Rina Wulandari`, Last Updated `T0 − 3 jam`.
- Kondisi:
  - Semua kolom tabel Draft tampil (Column Visibility default).

## Test Steps

### Berkas CSV: encoding dan isi sel
1. Rina mencari di sub tab Draft dengan kata kunci `Berkas {runId}`
2. Verifikasi tabel memuat tepat tiga baris data uji dengan urutan default Last Updated terbaru di atas: batch DU-130-5, DU-130-6, DU-130-7
3. Rina mengunduh tabel Draft dengan pilihan `Download as CSV`
4. Verifikasi berkas CSV berenkode UTF-8 dengan BOM dan berpemisah koma
5. Verifikasi berkas CSV memuat tiga baris data uji dengan urutan batch DU-130-5, DU-130-6, DU-130-7
6. Verifikasi kolom Group batch DU-130-5 berisi hierarki penuh dari root `Jakarta Office {runId} > Floor 2 Berkas {runId} > Server Room Berkas {runId}`
7. Verifikasi kolom Group batch DU-130-6 berisi `Bandung Office {runId} > Floor 2 Berkas {runId}` dan kolom Group batch DU-130-7 berisi `Jakarta Office {runId} > Floor 2 Berkas {runId}`, sehingga kedua batch ber-leaf `Floor 2 Berkas {runId}` sama tetap dapat dibedakan
8. Verifikasi kolom Requested By batch DU-130-6 berisi nama lengkap `Siti Nur Rahmawati`, bukan `Siti N`
9. Verifikasi kolom Origin batch DU-130-5 dan DU-130-7 berisi tanda hubung tunggal `-`, bukan sel kosong, bukan `—`, dan bukan `null`
10. Verifikasi kolom Origin batch DU-130-6 berisi `REG-20261105-00007`
11. Verifikasi kolom Total Asset berisi angka `12`, `5`, dan `30` tanpa pemisah format tampilan
12. Verifikasi kolom Progress batch DU-130-6 berisi angka `60` tanpa simbol `%`

### Berkas XLSX: satu sheet dan tipe sel
13. Rina mengunduh tabel Draft dengan pilihan `Download as XLSX`
14. Verifikasi berkas XLSX berisi tepat satu sheet bernama `Sheet1`
15. Verifikasi sel Total Asset ketiga baris data uji bertipe angka (number) bernilai `12`, `5`, dan `30`, bukan teks
16. Verifikasi sel Progress batch DU-130-6 bertipe angka (number) bernilai `60`, bukan teks `60%`
17. Verifikasi sel Origin batch DU-130-5 berisi teks `-` dan sel Requested By batch DU-130-6 berisi teks `Siti Nur Rahmawati`
18. Verifikasi sel Group batch DU-130-5, DU-130-6, dan DU-130-7 berisi hierarki penuh yang sama dengan berkas CSV

### Urutan baris berkas mengikuti Sort aktif
19. Rina mengurutkan kolom Total Asset secara menaik
20. Rina mengunduh tabel Draft dengan pilihan `Download as CSV`
21. Verifikasi baris berkas berurutan menurut Sort aktif: batch DU-130-6 (Total Asset `5`), DU-130-5 (`12`), lalu DU-130-7 (`30`)
22. Rina mengurutkan kolom Total Asset secara menurun
23. Rina mengunduh tabel Draft dengan pilihan `Download as XLSX`
24. Verifikasi baris berkas berurutan menurut Sort aktif: batch DU-130-7 (Total Asset `30`), DU-130-5 (`12`), lalu DU-130-6 (`5`)

### Nol baris menghasilkan berkas berisi header saja
25. Rina mencari dengan kata kunci `zzz-tidak-ada {runId}`
26. Rina mengunduh tabel Draft dengan pilihan `Download as CSV`
27. Verifikasi berkas CSV hanya berisi satu baris header dengan kolom `Group`, `Origin`, `Total Asset`, `Progress`, `Requested By`, dan `Last Updated`
28. Rina mengunduh tabel Draft dengan pilihan `Download as XLSX`
29. Verifikasi sheet `Sheet1` berkas XLSX hanya berisi satu baris header yang sama
