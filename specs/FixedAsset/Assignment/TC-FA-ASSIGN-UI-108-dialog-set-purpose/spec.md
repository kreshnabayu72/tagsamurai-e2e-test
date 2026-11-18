---
id: TC-FA-ASSIGN-UI-108-dialog-set-purpose
title: "Dialog Set Purpose: terapkan Purpose ke baris tercentang"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-27, FI-ASG-05]
smoke: []
dependsOn: []
trace:
  D-ASG-27: [2, 10, 16, 23, 29]
  FI-ASG-05: [3, 5, 6, 11, 12, 13, 17, 18, 19, 24, 26, 30, 31, 32]
anchor: []
coverage:
  web: automated
---
# Dialog Set Purpose: terapkan Purpose ke baris tercentang

## Prerequisites
- Aktor: Asset Admin dengan cakupan Group `Head Office` dan `Branch Surabaya`.
- Layar awal: form Assignment Request dengan baris aset tercentang; dialog Set Purpose dibuka dari bulk `[Set Purpose]`.
- Komponen: Dialog Set Purpose
- Data:
  - DU-108-1: Baris aset `Proyektor Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, Purpose `Kerja dari rumah`.
  - DU-108-2: Baris aset `Kamera Canon EOS - 1`, Asset ID `CAM-2026-0001`, Group `Branch Surabaya`, Purpose `Kunjungan klien`.
  - DU-108-3: Baris aset `Genset Perkins 20kVA - 1`, Asset ID `GEN-2026-0001`, Group `Head Office`, Purpose `Proyek tambang`.
  - DU-108-5: Baris aset `Laptop Dell Latitude 5420 - 14`, Asset ID `LPT-2026-0014`, Group `Head Office`, Purpose `Rapat bulanan`.
- Kondisi:
  - K1: satu baris aset tercentang di form, yaitu DU-108-1.
  - K2: tiga baris aset tercentang di form, yaitu DU-108-1 sampai DU-108-3.
  - K3: tiga baris aset ada di form; DU-108-1 dan DU-108-3 tercentang, DU-108-5 tidak tercentang.

## Test Steps

### Dialog Set Purpose untuk satu baris tercentang
1. Tampilkan Dialog Set Purpose dengan kondisi K1
2. Verifikasi dialog `Set Purpose` tampil dengan satu input Purpose
3. Verifikasi dialog memuat tombol `[Cancel]` dan `[Apply to 1 asset]`

### Dialog Set Purpose untuk beberapa baris tercentang
4. Tampilkan Dialog Set Purpose dengan kondisi K2
5. Verifikasi dialog memuat tombol `[Cancel]` dan `[Apply to 3 assets]`
6. Verifikasi input Purpose kosong dan hanya ada satu input

### Apply mengisi Purpose ke semua baris tercentang
7. Tampilkan Dialog Set Purpose dengan kondisi K2
8. Isi Purpose `Survei lokasi`
9. Klik `[Apply to 3 assets]`
10. Verifikasi dialog Set Purpose tertutup
11. Verifikasi Purpose baris `Proyektor Epson EB-X06 - 2` bernilai `Survei lokasi`
12. Verifikasi Purpose baris `Kamera Canon EOS - 1` bernilai `Survei lokasi`
13. Verifikasi Purpose baris `Genset Perkins 20kVA - 1` bernilai `Survei lokasi`

### Purpose kosong tidak mengubah Purpose baris
14. Tampilkan Dialog Set Purpose dengan kondisi K2
15. Klik `[Apply to 3 assets]`
16. Verifikasi dialog Set Purpose tertutup
17. Verifikasi Purpose baris `Proyektor Epson EB-X06 - 2` tetap `Kerja dari rumah`
18. Verifikasi Purpose baris `Kamera Canon EOS - 1` tetap `Kunjungan klien`
19. Verifikasi Purpose baris `Genset Perkins 20kVA - 1` tetap `Proyek tambang`

### Cancel menutup dialog tanpa mengubah Purpose
20. Tampilkan Dialog Set Purpose dengan kondisi K2
21. Isi Purpose `Survei lokasi`
22. Klik `[Cancel]`
23. Verifikasi dialog Set Purpose tertutup
24. Verifikasi Purpose baris `Proyektor Epson EB-X06 - 2` tetap `Kerja dari rumah`

### Apply hanya mengenai baris tercentang
25. Tampilkan Dialog Set Purpose dengan kondisi K3
26. Verifikasi dialog memuat tombol `[Cancel]` dan `[Apply to 2 assets]`
27. Isi Purpose `Survei lokasi`
28. Klik `[Apply to 2 assets]`
29. Verifikasi dialog Set Purpose tertutup
30. Verifikasi Purpose baris `Proyektor Epson EB-X06 - 2` bernilai `Survei lokasi`
31. Verifikasi Purpose baris `Genset Perkins 20kVA - 1` bernilai `Survei lokasi`
32. Verifikasi Purpose baris `Laptop Dell Latitude 5420 - 14` yang tidak tercentang tetap `Rapat bulanan`
