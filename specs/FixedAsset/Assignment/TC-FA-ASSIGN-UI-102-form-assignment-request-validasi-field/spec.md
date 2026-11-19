---
id: TC-FA-ASSIGN-UI-102-form-assignment-request-validasi-field
title: "Form Assignment Request: validasi Assignee, PIC, Purpose, Note, dan Assets"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FLD-ASG-01", "FLD-ASG-02", "FLD-ASG-03", "FI-ASG-06", "FI-ASG-08", "V-ASG-09", "V-ASG-12", "V-ASG-14", "V-ASG-15", "§9.5#r9", "EB-FRM-4@purpose", "EB-FRM-4@note"]
smoke: []
dependsOn: []
trace:
  "FLD-ASG-01": [3, 6]
  "FLD-ASG-02": [9, 12]
  "FLD-ASG-03": [24, 27, 32, 34, 40, 42, 57]
  "FI-ASG-06": 9
  "FI-ASG-08": [3, 9, 21, 24]
  "V-ASG-09": [3, 6]
  "V-ASG-12": [9, 12, 15, 18]
  "V-ASG-14": 21
  "V-ASG-15": [24, 27, 30]
  "§9.5#r9": [30, 45]
  "EB-FRM-4@purpose": [30, 32, 34, 36, 38]
  "EB-FRM-4@note": [45, 47, 49, 51, 53]
anchor: []
coverage:
  web: automated
---

# Form Assignment Request: validasi Assignee, PIC, Purpose, Note, dan Assets

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: halaman Assignment Request pada level Full.
- Komponen: Form Assignment Request
- Data:
  - DU-102-1: Assignee Employee `Dewi Kartika`, Email `dewi.kartika@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`.
  - DU-102-2: Assignee Division `Finance`, Code `FIN`, Users `4`.
  - DU-102-3: PIC `Sari Dewi`, Email `sari.dewi@example.com`, anggota Division `Finance`.
  - DU-102-4: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-102-5: Purpose awal `Operasional kantor pusat` pada baris DU-102-4.
  - DU-102-6: Purpose awal kosong pada baris DU-102-4.
  - DU-102-7: Assignee belum dipilih.
  - DU-102-8: PIC belum dipilih.
- Kondisi:
  - K1: Assignee DU-102-1 dipilih; tabel berisi DU-102-4 dengan Purpose DU-102-6; Note kosong.
  - K2: Assignee DU-102-7; tabel berisi DU-102-4 dengan Purpose DU-102-5.
  - K3: Assignee DU-102-2 dipilih; PIC DU-102-8; tabel berisi DU-102-4 dengan Purpose DU-102-5.
  - K4: Assignee DU-102-1 dipilih; tabel aset kosong.
  - K5: Assignee DU-102-2 dipilih dan PIC DU-102-3 terpilih, tetapi PIC itu bukan lagi anggota aktif Division `Finance`, sehingga simpan ditolak; tabel berisi DU-102-4 dengan Purpose DU-102-5.
  - K6: Assignee DU-102-1 dipilih; tabel berisi DU-102-4 dengan Purpose DU-102-6; Note kosong; simpan draft berhasil.

## Test Steps

### Assignee wajib diisi saat Submit
1. Tampilkan Form Assignment Request dengan kondisi K2
2. Klik `[Submit]`
3. Verifikasi `You must pick an assignee` tampil di bawah isian Assignee

### Assignee wajib diisi saat Save Draft
4. Tampilkan Form Assignment Request dengan kondisi K2
5. Klik `[Save Draft]`
6. Verifikasi `You must pick an assignee` tampil di bawah isian Assignee

### PIC wajib untuk Assignee Division saat Submit
7. Tampilkan Form Assignment Request dengan kondisi K3
8. Klik `[Submit]`
9. Verifikasi `You must pick a PIC` tampil di bawah isian PIC

### PIC wajib untuk Assignee Division saat Save Draft
10. Tampilkan Form Assignment Request dengan kondisi K3
11. Klik `[Save Draft]`
12. Verifikasi `You must pick a PIC` tampil di bawah isian PIC

### PIC yang bukan anggota aktif Division ditolak
13. Tampilkan Form Assignment Request dengan kondisi K5
14. Klik `[Submit]`
15. Verifikasi `Sari Dewi isn't an active member of Finance.` tampil
16. Tampilkan Form Assignment Request dengan kondisi K5
17. Klik `[Save Draft]`
18. Verifikasi `Sari Dewi isn't an active member of Finance.` tampil

### Assets minimal satu aset saat Submit
19. Tampilkan Form Assignment Request dengan kondisi K4
20. Klik `[Submit]`
21. Verifikasi `You must pick an asset` tampil di bawah tabel aset

### Purpose kosong dan Purpose berisi spasi saja ditolak saat Submit
22. Tampilkan Form Assignment Request dengan kondisi K1
23. Klik `[Submit]`
24. Verifikasi `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`
25. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan tiga spasi `   `
26. Klik `[Submit]`
27. Verifikasi `Purpose must not be empty` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10` untuk Purpose berisi spasi saja

### Batas panjang Purpose 120 karakter
28. Tampilkan Form Assignment Request dengan kondisi K1
29. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan ba` (121 karakter)
30. Verifikasi `Max. 120 characters` tampil di bawah Purpose baris `Laptop Dell Latitude 5420 - 10`
31. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan b` (120 karakter)
32. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose tepat di batas
33. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Penggunaan laptop untuk kegiatan survei aset tetap dan inventarisasi lapangan di kantor cabang tahun 2026 cabang Medan b  `, yaitu 120 karakter dengan dua spasi di tiap tepi
34. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose dengan spasi tepi
35. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Pinjam pakai laptop dan printer untuk tim audit internal selama kunjungan ke cabang Medan Binjai tahun 2026 cabang Medan` (120 karakter)
36. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose yang memuat spasi tengah
37. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `Kantor Cabang Medan Élan 𝒜  tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (120 karakter)
38. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose yang memuat huruf beraksen dan karakter di luar BMP
39. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `P` (1 karakter)
40. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose satu karakter
41. Ganti Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Operasional kantor pusat  ` dengan dua spasi di tiap tepi
42. Verifikasi `Max. 120 characters` tidak tampil untuk Purpose pendek dengan spasi tepi

### Batas panjang Note 360 karakter
43. Tampilkan Form Assignment Request dengan kondisi K1
44. Isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian um` (361 karakter)
45. Verifikasi `Max. 360 characters` tampil di bawah Note
46. Ganti isi Note dengan `Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian u` (360 karakter)
47. Verifikasi `Max. 360 characters` tidak tampil untuk Note tepat di batas
48. Ganti isi Note dengan `  Peminjaman perangkat kerja untuk proyek pemetaan aset di kantor cabang selama satu semester tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian u  `, yaitu 360 karakter dengan dua spasi di tiap tepi
49. Verifikasi `Max. 360 characters` tidak tampil untuk Note dengan spasi tepi
50. Ganti isi Note dengan `Peminjaman  perangkat kerja untuk proyek pemetaan aset dan  survei lapangan di cabang Medan selama semester genap tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026` (360 karakter)
51. Verifikasi `Max. 360 characters` tidak tampil untuk Note yang memuat spasi tengah
52. Ganti isi Note dengan `Peminjaman perangkat Élan untuk proyek 𝒜 pemetaan aset di kantor cabang Medan  tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk survei dan audit tahun 2026 cabang Medan bagian umum untuk sur` (360 karakter)
53. Verifikasi `Max. 360 characters` tidak tampil untuk Note yang memuat huruf beraksen dan karakter di luar BMP

### Purpose dengan spasi tepi dikirim tanpa spasi tepi
54. Tampilkan Form Assignment Request dengan kondisi K6
55. Isi Purpose baris `Laptop Dell Latitude 5420 - 10` dengan `  Operasional kantor pusat  ` dengan dua spasi di tiap tepi
56. Klik `[Save Draft]`
57. Verifikasi Purpose yang dikirim pada permintaan simpan draft adalah `Operasional kantor pusat` tanpa spasi tepi
