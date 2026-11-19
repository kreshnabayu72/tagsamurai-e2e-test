---
id: TC-FA-BORROW-UI-048-dialog-set-duration-purpose-bulk
title: "Dialog bulk Set Duration & Purpose menyamakan nilai antar aset terpilih menurut satuan"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-BRW-11", "FI-BRW-12", "FI-BRW-13", "FI-BRW-14", "FI-BRW-15", "FI-BRW-16", "FLD-BRW-12", "V-BRW-17"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-11": [2, 13, 33]
  "FI-BRW-12": [3, 4, 32, 35, 36]
  "FI-BRW-13": [14, 20]
  "FI-BRW-14": [5, 15, 19]
  "FI-BRW-15": [2, 7, 8]
  "FI-BRW-16": [29, 30]
  "FLD-BRW-12": [11, 24, 25, 40]
  "V-BRW-17": [24, 25, 40]
anchor: []
coverage:
  web: automated
---
# Dialog bulk Set Duration & Purpose menyamakan nilai antar aset terpilih menurut satuan

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request dengan baris aset tercentang dan dialog Set Duration & Purpose sudah terbuka.
- Komponen: Dialog Set Duration & Purpose
- Data:
  - DU-048-1: Baris `Laptop Dell Latitude 5420 - 10`, Group `Head Office`, satuan `days`, Max Duration `3 days`, Duration `1`, Purpose `Rapat koordinasi`.
  - DU-048-2: Baris `Projector Epson EB-X06 - 14`, Group `Head Office`, satuan `days`, Max Duration `3 days`, Duration `2`, Purpose `Survei lapangan`.
  - DU-048-3: Baris `Excavator PC200 - 4`, satuan `days`, Max Duration `7 days`, Duration dan Purpose kosong.
  - DU-048-4: Baris `Camera Sony A7 IV - 1`, satuan `hours`, Max Duration `4 hours`, Duration `4`, Purpose `Dokumentasi acara`.
  - Teks tombol terapkan yang diharapkan: `[Apply to 4 assets]` untuk empat baris tercentang dan `[Apply to 1 asset]` untuk satu baris tercentang, dari template `[Apply to [N] assets]`.
  - DU-048-9: Baris `Meja Rapat Oval - 3`, Group `Branch Surabaya`, satuan `days`, Max Duration `7 days`, Duration dan Purpose kosong.
  - Label input Duration yang diharapkan: `Daily assets (3)` untuk tiga baris `days` dan `Hourly assets (1)` untuk satu baris `hours`. Untuk dua baris `days` labelnya `Daily assets (2)`, dari label `Daily assets (3)` dengan jumlah dua.
  - Untuk satu baris `days` label input Duration yang diharapkan `Daily assets (1)`, dari label `Daily assets (3)` dengan jumlah satu.
  - Teks tombol terapkan yang diharapkan untuk dua baris tercentang: `[Apply to 2 assets]`, dari template `[Apply to [N] assets]`.
- Kondisi:
  - K1: dialog dibuka untuk baris tercentang DU-048-1 sampai DU-048-4 (tiga baris `days`, satu baris `hours`).
  - K2: dialog dibuka untuk satu baris tercentang, DU-048-1.
  - K3: dialog dibuka sesudah Select all di header kelompok Group `Head Office` memilih baris DU-048-1 dan DU-048-2; baris DU-048-9 dari Group `Branch Surabaya` tidak tercentang.

## Test Steps

### Dialog memuat satu input Duration per satuan dan input Purpose
1. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
2. Verifikasi tombol `[Apply to 4 assets]` tampil sehingga dialog berlaku untuk keempat baris tercentang
3. Verifikasi dialog memuat input Duration berlabel `Daily assets (3)` dengan satuan `days`
4. Verifikasi dialog memuat input Duration berlabel `Hourly assets (1)` dengan satuan `hours`
5. Verifikasi dialog memuat input Purpose berupa input teks

### Dialog untuk satu baris memakai tombol bernama menurut jumlah baris
6. Tampilkan Dialog Set Duration & Purpose dengan kondisi K2
7. Verifikasi tombol `[Cancel]` tampil
8. Verifikasi tombol `[Apply to 1 asset]` tampil

### Input kosong tidak mengubah baris
9. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
10. Isi input `Daily assets (3)` dengan `2`
11. Verifikasi tombol `[Apply to 4 assets]` tidak disabled karena nilai `2` adalah bilangan bulat di atas 1
12. Klik `[Apply to 4 assets]`
13. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10`, baris `Projector Epson EB-X06 - 14`, dan baris `Excavator PC200 - 4` berisi `2`
14. Verifikasi Duration baris `Camera Sony A7 IV - 1` tetap `4` karena input `Hourly assets (1)` dibiarkan kosong
15. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10` tetap `Rapat koordinasi` karena input Purpose dibiarkan kosong

### Purpose yang diisi diterapkan ke semua baris tercentang
16. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
17. Isi input Purpose dengan `Pelatihan karyawan baru`
18. Klik `[Apply to 4 assets]`
19. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 10`, baris `Projector Epson EB-X06 - 14`, baris `Excavator PC200 - 4`, dan baris `Camera Sony A7 IV - 1` berisi `Pelatihan karyawan baru`
20. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` tetap `1` karena input Duration dibiarkan kosong

### Duration bulk `0` dijepit ke batas bawah 1
21. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
22. Isi input `Daily assets (3)` dengan `0`
23. Pindahkan fokus keluar dari input `Daily assets (3)`
24. Verifikasi input `Daily assets (3)` berisi `1` sesuai batas bawah Duration `1`[^drift-1]
25. Verifikasi tombol `[Apply to 4 assets]` tidak disabled karena nilai `1` adalah bilangan bulat ≥ 1[^drift-1]

### Baris yang hasilnya melewati batas tetap diisi dan ditandai
26. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
27. Isi input `Daily assets (3)` dengan `5`
28. Klik `[Apply to 4 assets]`
29. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` dan baris `Projector Epson EB-X06 - 14` terisi, dan kedua baris itu ditandai ⚠ karena hasilnya melewati Max Duration `3 days`
30. Verifikasi baris `Excavator PC200 - 4` tidak ditandai ⚠ karena hasilnya masih dalam Max Duration `7 days`

### Select all di header kelompok memilih baris kelompok itu untuk dialog bulk
31. Tampilkan Dialog Set Duration & Purpose dengan kondisi K3
32. Verifikasi dialog memuat input Duration berlabel `Daily assets (2)` dengan satuan `days`
33. Verifikasi tombol `[Apply to 2 assets]` tampil sehingga dialog berlaku untuk kedua baris kelompok `Head Office` yang dipilih lewat Select all, bukan baris `Meja Rapat Oval - 3` dari Group lain

### Dialog satu baris days hanya memuat input Duration satuan days
34. Tampilkan Dialog Set Duration & Purpose dengan kondisi K2
35. Verifikasi dialog memuat input Duration berlabel `Daily assets (1)` dengan satuan `days`
36. Verifikasi dialog tidak memuat input Duration berlabel `Hourly assets`

### Karakter bukan angka pada input Duration bulk dibuang
37. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
38. Isi input `Daily assets (3)` dengan `abc`
39. Pindahkan fokus keluar dari input `Daily assets (3)`
40. Verifikasi input `Daily assets (3)` tetap kosong karena karakter bukan angka dibuang saat diketik[^drift-1]

[^drift-1]: Drift PRD vs kontrak komponen. PRD §9.9 FLD-BRW-12 dan §6 V-BRW-17: nilai `0` atau tidak valid (misalnya `abc`) pada input Duration bulk menampilkan caption `Enter a duration of at least 1` di bawah input dan tombol terapkan nonaktif. Kontrak komponen `NumberInput#1`: min dan max adalah rentang, saat blur atau Enter nilai di bawah min dijepit ke min (`0` menjadi `1`); `NumberInput#15`: tidak ada pesan rentang dan tidak ada invalid state untuk nilai di luar min/max; `NumberInput#5`: karakter bukan angka dibuang saat diketik dan kolom yang hanya menerima karakter itu tetap kosong, juga sesudah blur. Diasersi: kontrak, karena input Duration bulk dirender NumberInput (SB-7).
