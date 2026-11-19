---
id: TC-FA-BORROW-UI-049-form-borrow-request-baris-aset-kelayakan
title: "Baris aset di form Borrow Request menampilkan state Ready atau Not ready, hint batas, dan blok Approval"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-20", "FI-BRW-21", "FI-BRW-22", "FI-BRW-23", "FI-BRW-24", "FI-BRW-25", "FI-BRW-26", "FI-BRW-27", "FI-BRW-28", "FI-BRW-34", "FI-BRW-35", "FLD-BRW-05", "§4.3#r1", "§4.3#r2", "§4.3#r3", "§4.3#r7", "§4.4#r1", "§4.4#r2", "§9.5#r12"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-20": [3, 18, 45]
  "FI-BRW-21": 2
  "FI-BRW-22": 3
  "FI-BRW-23": [8, 9, 11, 60, 62]
  "FI-BRW-24": 4
  "FI-BRW-25": [5, 67]
  "FI-BRW-26": 14
  "FI-BRW-27": [18, 19]
  "FI-BRW-28": [20, 23, 24]
  "FI-BRW-34": [51, 52, 56, 66, 71, 74, 75]
  "FI-BRW-35": [50, 51]
  "FLD-BRW-05": 28
  "§4.3#r1": 5
  "§4.3#r2": [3, 19]
  "§4.3#r3": [16, 18]
  "§4.3#r7": [3, 19]
  "§4.4#r1": [33, 34, 35]
  "§4.4#r2": [56, 57, 66, 71, 74]
  "§9.5#r12": [41, 44]
anchor: [22, 40, 65]
coverage:
  web: automated
---
# Baris aset di form Borrow Request menampilkan state Ready atau Not ready, hint batas, dan blok Approval

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request.
- Komponen: Tabel aset form Borrow Request
- Data:
  - DU-049-1: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Max Duration `3 days`, Approval `Auto (≤ 3 days)`, lolos kelayakan untuk Borrower `Rudi Hartono`.
  - DU-049-2: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Max Duration `14 days`, Approval `Needs approval`, tidak layak karena aset sudah dihapus dan Allowed borrower tidak terpenuhi oleh Borrower `Rudi Hartono`. Alasan tooltip yang diharapkan `This asset has been deleted.`, penyebab dengan prioritas tertinggi.
  - DU-049-3: Aset `Kursi B - 1`, Asset ID `CHR-2026-0101`, Group `Branch Surabaya`, Max Duration `3 days`, Approval `Needs approval`, tidak layak hanya karena Allowed borrower tidak terpenuhi oleh Borrower `Rudi Hartono`. Alasan tooltip yang diharapkan `Rudi Hartono can't borrow assets from Branch Surabaya.`, dari template `[Borrower] can't borrow assets from [Group].`.
  - DU-049-4: Aset `Meeting Mic Set - 2`, Asset ID `MIC-2026-0002`, Group `Head Office`, Max Duration `7 days`, Approval `Auto (≤ 2 days)`, Purpose terisi `Pengukuran lokasi proyek`.
  - DU-049-5: Aset `Projector Epson EB-X06 - 14`, Asset ID `PRJ-2026-0014`, Group `Head Office`, Max Duration `3 days`, Approval `Needs approval`, Purpose terisi `Pengambilan gambar proyek`.
  - DU-049-6: Borrower `Rudi Hartono`, Position `Supervisor`, Division `Warehouse`, Home Group `Head Office`, Active Borrows `5 assets`, batas Max assets `10`, Eligibility `Can borrow`. Teks bantu yang diharapkan `5 of 10 borrowed`, dari template `[Used] of [Max] borrowed`.
  - DU-049-7: Aset `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Group `Head Office`, Max Duration `7 days`, Approval `Needs approval (all must approve)`, lolos kelayakan untuk Borrower `Rudi Hartono`, kandidat di dialog Select Asset.
  - Teks blok Approval yang diharapkan: `No approval needed: Meeting Mic Set - 2.`, `Needs approval: Meeting Mic Set - 2.`, dan `Needs approval: Projector Epson EB-X06 - 14.`, dari template `No approval needed: [Asset].` dan `Needs approval: [Asset].`.
- Kondisi:
  - K1: Draft dibuka dengan Borrower DU-049-6 dan baris aset DU-049-1, DU-049-2, dan DU-049-3, dengan evaluasi kelayakan saat Draft dibuka.
  - K2: form baru dengan Borrower DU-049-6 sudah dipilih dan baris aset DU-049-4 dan DU-049-5, Duration kedua baris belum diisi.
  - K3: form baru, Borrower belum dipilih, berisi baris aset DU-049-1 dan DU-049-3; dialog Select Borrower memuat DU-049-6.
  - K4: form baru dengan Borrower DU-049-6 sudah dipilih dan tanpa baris aset; dialog Select Asset memuat DU-049-7.
  - K5: form dengan Borrower DU-049-6 sudah dipilih dan satu baris aset DU-049-3 yang tidak layak.

## Test Steps

### Baris yang tidak layak tetap tampil dengan tanda di sel Name
1. Tampilkan Tabel aset form Borrow Request dengan kondisi K1
2. Verifikasi baris `Toyota Avanza - 6` tampil di tabel aset walaupun tidak layak
3. Verifikasi sel Name baris `Toyota Avanza - 6` memuat ikon ⚠ dan caption `This asset can no longer be borrowed.`
4. Verifikasi sel Duration baris `Toyota Avanza - 6` tidak dipakai untuk tanda itu dan tidak memuat caption `This asset can no longer be borrowed.`
5. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tampil tanpa ikon ⚠ dan tanpa caption `This asset can no longer be borrowed.`

### Tooltip tanda memuat satu alasan dengan prioritas tertinggi
6. Tampilkan Tabel aset form Borrow Request dengan kondisi K1
7. Arahkan kursor ke ikon ⚠ pada baris `Toyota Avanza - 6`
8. Verifikasi alasan `This asset has been deleted.` tersampaikan pada ikon ⚠ baris `Toyota Avanza - 6`
9. Verifikasi alasan `Rudi Hartono can't borrow assets from Branch Surabaya.` tidak tersampaikan pada baris `Toyota Avanza - 6` karena hanya satu alasan yang ditampilkan
10. Arahkan kursor ke ikon ⚠ pada baris `Kursi B - 1`
11. Verifikasi alasan `Rudi Hartono can't borrow assets from Branch Surabaya.` tersampaikan pada ikon ⚠ baris `Kursi B - 1`

### Submit gagal dan aset tidak layak bisa dikeluarkan
12. Tampilkan Tabel aset form Borrow Request dengan kondisi K1
13. Klik ikon `⋯` pada baris `Toyota Avanza - 6`
14. Verifikasi aksi `Remove from List` tersedia pada menu baris itu
15. Tekan Esc
16. Verifikasi tombol `[Submit]` tidak disabled
17. Klik `[Submit]`
18. Verifikasi caption `Remove the unavailable assets to continue.` tampil di atas deretan tombol aksi
19. Verifikasi dialog `Submit Borrow` tidak tampil sehingga Submit gagal sampai aset dikeluarkan
20. Verifikasi tombol `[Remove Unavailable]` tampil karena ada baris yang tidak layak
21. Klik `[Remove Unavailable]`
22. Verifikasi baris `Laptop Dell Latitude 5420 - 10` masih tampil di tabel aset
23. Verifikasi baris `Toyota Avanza - 6` dan baris `Kursi B - 1` tidak ada lagi di tabel aset
24. Verifikasi tombol `[Remove Unavailable]` tidak tampil karena tidak ada baris yang tidak layak

### Aset wajib ada setelah semua baris tidak layak dikeluarkan
25. Tampilkan Tabel aset form Borrow Request dengan kondisi K5
26. Klik `[Remove Unavailable]`
27. Klik `[Submit]`
28. Verifikasi Submit ditolak dengan caption `You must pick an asset` setelah semua baris dikeluarkan

### Memilih Borrower menampilkan teks bantu dan menandai aset yang tidak boleh dipinjam
29. Tampilkan Tabel aset form Borrow Request dengan kondisi K3
30. Klik `[Select Borrower]`
31. Pilih baris `Rudi Hartono` pada dialog Select Borrower
32. Klik tombol konfirmasi pada dialog Select Borrower
33. Verifikasi teks bantu `5 of 10 borrowed` tampil di bawah Borrower
34. Verifikasi baris `Kursi B - 1` ditandai ⚠ karena aset itu tidak boleh dipinjam Borrower terpilih
35. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tidak ditandai ⚠

### Aset yang baru ditambahkan dinilai dan mulai dengan Duration dan Purpose kosong
36. Tampilkan Tabel aset form Borrow Request dengan kondisi K4
37. Klik `[+ Asset]`
38. Centang baris `Excavator PC200 - 4` pada dialog Select Asset
39. Klik `[Select]` pada dialog Select Asset
40. Verifikasi baris `Excavator PC200 - 4` tampil di tabel aset
41. Verifikasi Duration dan Purpose baris `Excavator PC200 - 4` kosong
42. Centang baris `Excavator PC200 - 4`
43. Buka menu aksi pada bar bulk
44. Verifikasi menu bulk memuat aksi `Set Duration & Purpose` untuk menyamakan nilai baris aset yang baru ditambahkan
45. Verifikasi baris `Excavator PC200 - 4` tidak memuat caption `This asset can no longer be borrowed.` karena lolos evaluasi kelayakan

### Duration baris menentukan blok Approval pada dialog konfirmasi
46. Tampilkan Tabel aset form Borrow Request dengan kondisi K2
47. Isi Duration baris `Meeting Mic Set - 2` dengan `1`
48. Isi Duration baris `Projector Epson EB-X06 - 14` dengan `3`
49. Klik `[Submit]`
50. Verifikasi dialog `Submit Borrow` tampil
51. Verifikasi blok Approval memuat `No approval needed: Meeting Mic Set - 2.` karena Duration baris itu `1`
52. Verifikasi blok Approval memuat `Needs approval: Projector Epson EB-X06 - 14.` karena Duration baris itu `3`
53. Klik `[Cancel]` pada dialog Submit Borrow
54. Ganti isi Duration baris `Meeting Mic Set - 2` dengan `4`
55. Klik `[Submit]`
56. Verifikasi blok Approval memuat `Needs approval: Meeting Mic Set - 2.` karena Duration baris itu `4`
57. Verifikasi blok Approval tidak memuat `No approval needed: Meeting Mic Set - 2.`

### Fokus keyboard pada ⚠ membuka tooltip alasan
58. Tampilkan Tabel aset form Borrow Request dengan kondisi K1
59. Arahkan fokus keyboard ke ikon ⚠ pada baris `Toyota Avanza - 6`
60. Verifikasi alasan `This asset has been deleted.` tersampaikan pada ikon ⚠ baris `Toyota Avanza - 6`
61. Arahkan fokus keyboard ke ikon ⚠ pada baris `Kursi B - 1`
62. Verifikasi alasan `Rudi Hartono can't borrow assets from Branch Surabaya.` tersampaikan pada ikon ⚠ baris `Kursi B - 1`

### Mengubah Duration menghitung ulang kelayakan baris itu tanpa mengubah baris lain
63. Tampilkan Tabel aset form Borrow Request dengan kondisi K2
64. Isi Duration baris `Meeting Mic Set - 2` dengan `4`
65. Verifikasi baris `Meeting Mic Set - 2` tampil dengan Duration `4`
66. Verifikasi ikon ⚠ dan caption `This asset can no longer be borrowed.` tidak tampil pada baris `Meeting Mic Set - 2` sesudah Duration berubah
67. Verifikasi ikon ⚠ dan caption `This asset can no longer be borrowed.` tetap tidak tampil pada baris `Projector Epson EB-X06 - 14`

### Batas Duration dihitung per baris saat Duration berubah
68. Tampilkan Tabel aset form Borrow Request dengan kondisi K2
69. Isi Duration baris `Meeting Mic Set - 2` dengan `10`
70. Pindahkan fokus keluar dari Duration baris `Meeting Mic Set - 2`
71. Verifikasi Duration baris `Meeting Mic Set - 2` berisi `7` sesuai Max Duration `7 days` baris itu[^drift-1]
72. Isi Duration baris `Projector Epson EB-X06 - 14` dengan `10`
73. Pindahkan fokus keluar dari Duration baris `Projector Epson EB-X06 - 14`
74. Verifikasi Duration baris `Projector Epson EB-X06 - 14` berisi `3` sesuai Max Duration `3 days` baris itu[^drift-1]
75. Verifikasi Duration baris `Meeting Mic Set - 2` tetap `7` sesudah Duration baris `Projector Epson EB-X06 - 14` berubah

[^drift-1]: Drift PRD vs kontrak komponen. PRD §4.4 (Ubah Duration: kelayakan, hint batas, dan blok Approval dihitung ulang), §6 V-BRW-16, dan §9.9 FLD-BRW-02: Duration bilangan bulat `1` sampai Max duration aset itu, dengan caption `Max. [Limit] [Unit] for [Category]` langsung di bawah field saat Duration melewati batas. Kontrak komponen `NumberInput#1`: min dan max adalah rentang, saat blur atau Enter nilai di atas max dijepit ke max; `NumberInput#15`: tidak ada pesan rentang dan tidak ada invalid state untuk nilai di luar min/max. Diasersi: kontrak, karena field Duration dirender NumberInput (SB-7).
