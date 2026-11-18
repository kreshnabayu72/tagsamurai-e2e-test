---
id: TC-FA-BORROW-UI-048-dialog-set-duration-purpose-bulk
title: "Dialog bulk Set Duration & Purpose menyamakan nilai antar aset terpilih menurut satuan"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FI-BRW-11", "FI-BRW-12", "FI-BRW-13", "FI-BRW-14", "FI-BRW-15", "FI-BRW-16", "FLD-BRW-12", "V-BRW-17"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-11": [2, 13]
  "FI-BRW-12": [3, 4]
  "FI-BRW-13": [14, 20]
  "FI-BRW-14": [5, 15, 19]
  "FI-BRW-15": [2, 7, 8]
  "FI-BRW-16": [28, 29]
  "FLD-BRW-12": [11, 23, 24]
  "V-BRW-17": [23, 24]
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
  - DU-048-1: Baris `Laptop Dell Latitude 5420 - 10`, satuan `days`, Max Duration `3 days`, Duration `1`, Purpose `Rapat koordinasi`.
  - DU-048-2: Baris `Projector Epson EB-X06 - 14`, satuan `days`, Max Duration `3 days`, Duration `2`, Purpose `Survei lapangan`.
  - DU-048-3: Baris `Excavator PC200 - 4`, satuan `days`, Max Duration `7 days`, Duration dan Purpose kosong.
  - DU-048-4: Baris `Camera Sony A7 IV - 1`, satuan `hours`, Max Duration `4 hours`, Duration `4`, Purpose `Dokumentasi acara`.
  - Teks tombol terapkan yang diharapkan: `[Apply to 4 assets]` untuk empat baris tercentang dan `[Apply to 1 asset]` untuk satu baris tercentang, dari template `[Apply to [N] assets]`.
  - Label input Duration yang diharapkan: `Daily assets (3)` untuk tiga baris `days` dan `Hourly assets (1)` untuk satu baris `hours`.
- Kondisi:
  - K1: dialog dibuka untuk baris tercentang DU-048-1 sampai DU-048-4 (tiga baris `days`, satu baris `hours`).
  - K2: dialog dibuka untuk satu baris tercentang, DU-048-1.

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

### Duration bulk di bawah 1 ditolak
21. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
22. Isi input `Daily assets (3)` dengan `0`
23. Verifikasi caption `Enter a duration of at least 1` tampil di bawah input `Daily assets (3)`
24. Verifikasi tombol `[Apply to 4 assets]` disabled

### Baris yang hasilnya melewati batas tetap diisi dan ditandai
25. Tampilkan Dialog Set Duration & Purpose dengan kondisi K1
26. Isi input `Daily assets (3)` dengan `5`
27. Klik `[Apply to 4 assets]`
28. Verifikasi Duration baris `Laptop Dell Latitude 5420 - 10` dan baris `Projector Epson EB-X06 - 14` terisi, dan kedua baris itu ditandai ⚠ karena hasilnya melewati Max Duration `3 days`
29. Verifikasi baris `Excavator PC200 - 4` tidak ditandai ⚠ karena hasilnya masih dalam Max Duration `7 days`
