---
id: TC-FA-DAMAGED-UI-110-dialog-report-damaged-tampilan-awal
title: "Dialog Report Damaged: judul per jumlah aset, blok per aset, field, placeholder, kotak dampak per jenis pelapor dan pemegang, keterangan aset yang dikeluarkan, isian awal, dan aksesibilitas"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-01, "§4.1#r5", "§4.2.3#p1", "§4.2.3#p2", "§4.2.3#b2", "§4.2.3#b3", "§4.2.3#b4", "§4.2.3#b5", FI-DMG-01, FI-DMG-04, FI-DMG-05, S-DMG-21, S-DMG-22, EB-FRM-7@report-damaged]
smoke: []
dependsOn: []
trace:
  D-DMG-01: [2, 6, 7, 14]
  "§4.1#r5": [4, 5, 7, 8]
  "§4.2.3#p1": [41, 42]
  "§4.2.3#p2": [2, 3, 4, 5, 8, 9, 11, 12, 14, 15, 45, 46]
  "§4.2.3#b2": [16, 17, 29, 30, 31]
  "§4.2.3#b3": [18, 19, 20, 21]
  "§4.2.3#b4": [37, 38]
  "§4.2.3#b5": [33, 34, 35, 36, 37, 38, 39]
  FI-DMG-01: [7]
  FI-DMG-04: [41, 42, 43]
  FI-DMG-05: [48, 50]
  S-DMG-21: [56, 57]
  S-DMG-22: [37, 38]
  EB-FRM-7@report-damaged: [59, 60, 61, 62, 64, 66, 68, 70, 72]
anchor: []
coverage:
  web: automated
---

# Dialog Report Damaged: judul per jumlah aset, blok per aset, field, placeholder, kotak dampak per jenis pelapor dan pemegang, keterangan aset yang dikeluarkan, isian awal, dan aksesibilitas

## Prerequisites
- Aktor: Pelapor admin (Aktor Damaged pada Group aset); pada K4 dan K5 pelapor umum.
- Layar awal: Dialog Report Damaged belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Report Damaged (D-DMG-01)
- Data:
  - DU-110-1: Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, tanpa pemegang.
  - DU-110-2: Asset `Tablet Samsung Tab A8 - 3`, Asset ID `TAB-2026-0003`, Group `Head Office`, sedang dipinjam oleh pemegang `Dewi A`.
  - DU-110-3: Asset `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`, sedang dipinjam oleh pemegang `Sari D`.
  - DU-110-4: Asset `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`, sedang dipinjam oleh pemegang `Sari D`.
  - DU-110-5: Asset `Handheld Scanner Zebra TC21 - 2`, Asset ID `HSC-2026-0002`, Group `Head Office`, sedang ditugaskan kepada pemegang `Tono R`.
  - DU-110-6: Asset `Office Chair Ergo - 31`, Asset ID `CHR-2026-0031`, Group `Branch Surabaya`, tanpa pemegang.
  - DU-110-7: Asset `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Group `Head Office`, layak dilaporkan.
  - DU-110-8: Asset `Drill Bosch GSB - 6`, Asset ID `DRL-2026-0006`, Group `Head Office`, sudah punya record berjalan.
  - DU-110-9: Asset `Forklift Toyota 8FD - 1`, Asset ID `FLT-2026-0001`, Group `Head Office`, berstatus Disposed.
  - DU-110-10: Asset `Office Chair Ergo - 18`, Asset ID `CHR-2026-0018`, Group `Branch Surabaya`, di luar Group tempat pengguna memegang Update.
  - DU-110-11: isian awal What happened `Layar retak setelah terjatuh dari meja`.
  - DU-110-12: What happened yang diketik `Layar retak dan perangkat tidak menyala`.
  - DU-110-13: berkas foto yang dipilih `kerusakan-proyektor.jpg`, `kerusakan-handheld.jpg`, dan `kerusakan-laptop.jpg`.
- Kondisi:
  - K1: satu aset terpilih (DU-110-1), pelapor admin, dialog dibuka dari Asset List.
  - K2: satu aset terpilih (DU-110-2), pelapor admin.
  - K3: empat aset terpilih dari Asset List (DU-110-3, DU-110-4, DU-110-5, DU-110-6), seluruhnya layak, pelapor admin.
  - K4: satu aset terpilih (DU-110-1), pelapor umum, dialog dibuka dari My Asset.
  - K5: satu aset terpilih (DU-110-1), pelapor umum, dialog dibuka dari titik masuk selain My Asset.
  - K6: empat aset terpilih saat klik dari Asset List, pelapor admin yang memegang Update pada Group `Head Office`: DU-110-7 layak, DU-110-8, DU-110-9, dan DU-110-10 tidak layak.
  - K7: satu aset terpilih (DU-110-1), titik masuk mengisi awal What happened dengan DU-110-11.
  - K8: satu aset terpilih (DU-110-1), pelapor admin; respons simpan menyatakan aset itu baru saja dilaporkan orang lain.

## Test Steps

### Isi dialog satu aset oleh pelapor admin
1. Tampilkan Dialog Report Damaged dengan kondisi K1
2. Verifikasi judul dialog `Report Damaged`
3. Verifikasi blok aset memuat `Laptop Dell Latitude 5420 - 4` dan `LPT-2026-0004`
4. Verifikasi isian `What happened*` tampil dengan placeholder `Enter what happened`
5. Verifikasi satu pemilih foto berlabel `Damaged Photo*` tampil
6. Verifikasi tombol `[Cancel]` tampil
7. Verifikasi tombol `[Report Damaged]` tampil dan aktif
8. Verifikasi kotak dampak `The asset will be marked Damaged.` tampil
9. Verifikasi kotak dampak tidak memuat keterangan pemegang aset

### Kotak dampak aset yang sedang dipinjam
10. Tampilkan Dialog Report Damaged dengan kondisi K2
11. Verifikasi kotak dampak `The asset will be marked Damaged.` tampil
12. Verifikasi `Dewi A keeps the asset until it's returned.` tampil pada kotak dampak

### Judul jamak dan blok per aset
13. Tampilkan Dialog Report Damaged dengan kondisi K3
14. Verifikasi judul dialog `Report Damaged Assets`
15. Verifikasi blok aset `Projector Epson EB-X06 - 2`, `Scanner Fujitsu fi-7160 - 2`, `Handheld Scanner Zebra TC21 - 2`, dan `Office Chair Ergo - 31` tampil seluruhnya tanpa diringkas
16. Verifikasi tepat satu isian `What happened*` tampil untuk seluruh aset
17. Verifikasi setiap blok aset memuat satu pemilih foto berlabel `Damaged Photo*` di bawah header aset itu
18. Verifikasi kotak dampak `The assets will be marked Damaged.` tampil
19. Verifikasi `Sari D keeps the asset until it's returned.` tampil satu kali pada kotak dampak
20. Verifikasi `Tono R keeps the asset until it's returned.` tampil satu kali pada kotak dampak
21. Verifikasi kotak dampak memuat tepat dua baris pemegang, tanpa baris untuk `Office Chair Ergo - 31`

### Caption foto kosong hanya di bawah pemilih foto aset yang fotonya kosong
22. Tampilkan Dialog Report Damaged dengan kondisi K3
23. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
24. Pilih berkas foto `kerusakan-proyektor.jpg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
25. Klik `Apply` pada dialog `Adjust photo`
26. Pilih berkas foto `kerusakan-handheld.jpg` pada pemilih foto aset `Handheld Scanner Zebra TC21 - 2`
27. Klik `Apply` pada dialog `Adjust photo`
28. Klik `[Report Damaged]`
29. Verifikasi caption `Damaged photo must not be empty` tampil tepat di bawah pemilih foto aset `Scanner Fujitsu fi-7160 - 2`
30. Verifikasi caption `Damaged photo must not be empty` tampil tepat di bawah pemilih foto aset `Office Chair Ergo - 31`
31. Verifikasi tidak ada caption di bawah pemilih foto aset `Projector Epson EB-X06 - 2` dan `Handheld Scanner Zebra TC21 - 2`

### Aset yang dikeluarkan dari dialog beserta keterangannya
32. Tampilkan Dialog Report Damaged dengan kondisi K6
33. Verifikasi judul dialog `Report Damaged Assets`
34. Verifikasi blok aset `Toyota Avanza - 2` tampil
35. Verifikasi tepat satu pemilih foto berlabel `Damaged Photo*` tampil
36. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Drill Bosch GSB - 6` di bawah daftar aset
37. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Forklift Toyota 8FD - 1` di bawah daftar aset
38. Verifikasi keterangan `Can't be reported damaged` tampil untuk aset `Office Chair Ergo - 18` di bawah daftar aset
39. Verifikasi `Drill Bosch GSB - 6`, `Forklift Toyota 8FD - 1`, dan `Office Chair Ergo - 18` tidak dirender sebagai blok aset

### Dibuka dari My Asset: kotak dampak tidak tampil
40. Tampilkan Dialog Report Damaged dengan kondisi K4
41. Verifikasi isian `What happened*` dan pemilih foto `Damaged Photo*` tampil
42. Verifikasi tombol `[Cancel]` dan `[Report Damaged]` tampil
43. Verifikasi kotak dampak tidak tampil

### Kotak dampak pelapor umum
44. Tampilkan Dialog Report Damaged dengan kondisi K5
45. Verifikasi kotak dampak `The asset admins will review your report.` tampil
46. Verifikasi kotak dampak `The asset will be marked Damaged.` tidak tampil

### Isian awal What happened tetap dapat diubah
47. Tampilkan Dialog Report Damaged dengan kondisi K7
48. Verifikasi isian `What happened*` berisi `Layar retak setelah terjatuh dari meja`
49. Ganti isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
50. Verifikasi isian `What happened*` berisi `Layar retak dan perangkat tidak menyala`

### Aset yang baru dilaporkan orang lain tampil dengan keterangan dan dialog tetap terbuka
51. Tampilkan Dialog Report Damaged dengan kondisi K8
52. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
53. Pilih berkas foto `kerusakan-laptop.jpg` pada pemilih foto aset `Laptop Dell Latitude 5420 - 4`
54. Klik `Apply` pada dialog `Adjust photo`
55. Klik `[Report Damaged]`
56. Verifikasi dialog Report Damaged tetap terbuka
57. Verifikasi keterangan `Already reported damaged` tampil untuk aset `Laptop Dell Latitude 5420 - 4`

### Aksesibilitas dialog
58. Tampilkan Dialog Report Damaged dengan kondisi K1
59. Verifikasi fokus berada pada elemen di dalam dialog Report Damaged
60. Verifikasi isian `What happened*` pada dialog Report Damaged memiliki penanda wajib untuk teknologi bantu
61. Verifikasi tombol tutup dialog Report Damaged memiliki nama aksesibel `Close dialog`
62. Verifikasi tombol unggah foto pada dialog Report Damaged memiliki nama aksesibel `Upload image`
63. Tekan `Tab` sebanyak 10 kali
64. Verifikasi fokus tetap berada pada elemen di dalam dialog Report Damaged
65. Klik `[Report Damaged]`
66. Verifikasi pesan error di bawah isian `What happened*` terhubung sebagai deskripsi aksesibel isian itu
67. Klik `[Cancel]`
68. Verifikasi fokus kembali ke elemen yang membuka dialog Report Damaged

### Aksesibilitas pemilih foto wajib
69. Tampilkan Dialog Report Damaged dengan kondisi K1
70. Verifikasi pemilih foto `Damaged Photo*` pada dialog Report Damaged memiliki penanda wajib untuk teknologi bantu
71. Klik `[Report Damaged]`
72. Verifikasi caption `Damaged photo must not be empty` terhubung sebagai deskripsi aksesibel pemilih foto `Damaged Photo*`
