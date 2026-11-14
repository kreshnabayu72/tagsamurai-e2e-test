---
id: TC-FA-DAMAGED-UI-111-dialog-report-damaged-validasi
title: "Validasi Dialog Report Damaged: What happened wajib dan maksimal 360 karakter, Damaged Photo wajib per aset dengan caption di bawah picker, dan filter format foto"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FI-DMG-02, FI-DMG-06, FI-DMG-07, "§9.9#r1", "§9.9#r2", "§9.9#p4", EB-FRM-4@what-happened]
smoke: []
dependsOn: []
trace:
  FI-DMG-02: [3, 4]
  FI-DMG-06: [20]
  FI-DMG-07: [24, 25]
  "§9.9#r1": [3, 8, 11, 13, 15, 17]
  "§9.9#r2": [4, 29, 34, 40, 45, 46]
  "§9.9#p4": [30, 35, 38, 41, 42, 47]
  EB-FRM-4@what-happened: [11, 13, 17]
anchor: []
coverage:
  web: automated
---

# Validasi Dialog Report Damaged: What happened wajib dan maksimal 360 karakter, Damaged Photo wajib per aset dengan caption di bawah picker, dan filter format foto

## Prerequisites
- Aktor: Pelapor admin (Aktor Damaged pada Group aset).
- Layar awal: Dialog Report Damaged belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Report Damaged (D-DMG-01)
- Data:
  - DU-111-1: Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`.
  - DU-111-2: Asset `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`.
  - DU-111-3: Asset `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, Group `Head Office`.
  - DU-111-4: What happened dibiarkan kosong, foto tidak dipilih.
  - DU-111-5: What happened berisi tiga spasi saja.
  - DU-111-6: What happened sepanjang 360 karakter.
  - DU-111-7: What happened sepanjang 361 karakter.
  - DU-111-8: What happened sepanjang 360 karakter dengan spasi ganda di tengah teks.
  - DU-111-9: What happened sepanjang 360 karakter dengan huruf beraksen dan satu karakter non-BMP.
  - DU-111-10: berkas foto JPEG `kerusakan-layar.jpeg`, ukuran 512 KB.
  - DU-111-11: berkas foto PNG `kerusakan-layar.png`, ukuran 1 MB.
  - DU-111-12: berkas PDF `catatan-kerusakan.pdf`.
  - DU-111-13: berkas foto JPEG `kerusakan-layar-besar.jpeg`, ukuran 2 MB.
- Kondisi:
  - K1: satu aset terpilih (DU-111-1), What happened dan foto belum diisi.
  - K2: dua aset terpilih dari Asset List (DU-111-2 dan DU-111-3), What happened dan foto belum diisi.

## Test Steps

### Field wajib kosong menampilkan caption di bawah masing-masing field
1. Tampilkan Dialog Report Damaged dengan kondisi K1
2. Klik `[Report Damaged]` tanpa mengisi What happened dan tanpa memilih foto
3. Verifikasi caption `What happened must not be empty` tampil di bawah isian `What happened*`
4. Verifikasi caption `Damaged photo must not be empty` tampil di bawah pemilih foto `Damaged Photo*`

### What happened yang hanya berisi spasi diperlakukan kosong
5. Tampilkan Dialog Report Damaged dengan kondisi K1
6. Isi `What happened*` dengan tiga spasi (`   `)
7. Klik `[Report Damaged]`
8. Verifikasi caption `What happened must not be empty` tampil di bawah isian `What happened*`

### Batas 360 karakter pada What happened
9. Tampilkan Dialog Report Damaged dengan kondisi K1
10. Isi `What happened*` dengan `Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipakai bekerja. Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipaka` (361 karakter)
11. Verifikasi pesan `Max. 360 characters` tampil di bawah isian `What happened*` tanpa menunggu submit
12. Ganti isi `What happened*` dengan `Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipakai bekerja. Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipak` (360 karakter)
13. Verifikasi pesan `Max. 360 characters` tidak tampil lagi
14. Ganti isi `What happened*` dengan `Layar  laptop  retak  di  bagian  tengah  setelah  terjatuh  dari  meja  rapat  lantai  tiga  saat  dipindahkan  oleh  staf  gudang,  sehingga  tampilan  bergaris  dan  perangkat  tidak  dapat  dipakai  bekerja.  Layar  laptop  retak  di  bagian  tengah  setelah  terjatuh  dari  meja  rapat  lantai  tiga  saat  dipindahkan  oleh  staf  gudang,  sehingga  tam` (360 karakter)
15. Verifikasi pesan `Max. 360 characters` tidak tampil
16. Ganti isi `What happened*` dengan `Lénsa kaméra Cañon retak sesudah terjatuh dari rak Gudang Pusat Jakarta 𝒜 dan bingkai logam melengkung hingga penutup lensa tidak dapat dipasang kembali oleh teknisi lapangan Ünit Perawatan, sehingga perangkat dinyatakan tidak layak dipakai untuk pengambilan foto aset di lokasi. Lénsa kaméra Cañon retak sesudah terjatuh dari rak Gudang Pusat Jakarta 𝒜 dan bi` (360 karakter)
17. Verifikasi pesan `Max. 360 characters` tidak tampil

### Satu isian What happened untuk beberapa aset
18. Tampilkan Dialog Report Damaged dengan kondisi K2
19. Klik `[Report Damaged]` tanpa mengisi What happened dan tanpa memilih foto
20. Verifikasi caption `What happened must not be empty` tampil satu kali saja untuk kedua aset

### Satu foto per aset
21. Tampilkan Dialog Report Damaged dengan kondisi K2
22. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
23. Klik `Apply` pada dialog `Adjust photo`
24. Verifikasi pemilih foto aset `Projector Epson EB-X06 - 2` menampilkan foto yang dipilih
25. Verifikasi pemilih foto aset `Scanner Fujitsu fi-7160 - 2` tetap kosong

### Foto JPEG di bawah 1 MB diterima tanpa pesan error
26. Tampilkan Dialog Report Damaged dengan kondisi K1
27. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
28. Klik `Apply` pada dialog `Adjust photo`
29. Verifikasi foto `kerusakan-layar.jpeg` tampil pada pemilih foto `Damaged Photo*`
30. Verifikasi tidak ada pesan error di bawah pemilih foto `Damaged Photo*`

### Foto PNG tepat 1 MB diterima tanpa pesan error
31. Tampilkan Dialog Report Damaged dengan kondisi K1
32. Pilih berkas foto `kerusakan-layar.png` pada pemilih foto `Damaged Photo*`
33. Klik `Apply` pada dialog `Adjust photo`
34. Verifikasi foto `kerusakan-layar.png` tampil pada pemilih foto `Damaged Photo*`
35. Verifikasi tidak ada pesan error di bawah pemilih foto `Damaged Photo*`

### Foto di atas 1 MB diperkecil otomatis tanpa pesan error
36. Tampilkan Dialog Report Damaged dengan kondisi K1
37. Pilih berkas foto `kerusakan-layar-besar.jpeg` pada pemilih foto `Damaged Photo*`
38. Verifikasi dialog `Adjust photo` terbuka untuk berkas `kerusakan-layar-besar.jpeg`
39. Klik `Apply` pada dialog `Adjust photo`
40. Verifikasi foto `kerusakan-layar-besar.jpeg` tampil pada pemilih foto `Damaged Photo*`
41. Verifikasi ukuran foto yang diteruskan sesudah `Apply` tidak lebih dari 1 MB
42. Verifikasi tidak ada pesan error di bawah pemilih foto `Damaged Photo*`

### Berkas selain JPEG dan PNG disaring tanpa pesan error
43. Tampilkan Dialog Report Damaged dengan kondisi K1
44. Pilih berkas `catatan-kerusakan.pdf` pada pemilih foto `Damaged Photo*`
45. Verifikasi pemilih foto `Damaged Photo*` masih menampilkan tombol unggah tanpa foto
46. Verifikasi dialog `Adjust photo` tidak terbuka
47. Verifikasi tidak ada pesan error di bawah pemilih foto `Damaged Photo*`
