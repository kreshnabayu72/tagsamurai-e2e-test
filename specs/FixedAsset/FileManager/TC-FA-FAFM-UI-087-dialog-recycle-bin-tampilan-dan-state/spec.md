---
id: TC-FA-FAFM-UI-087-dialog-recycle-bin-tampilan-dan-state
title: "Dialog Recycle Bin: info retensi, format sel, nilai kosong, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-05a", "S-04", "S-28a", "S-28b", "T-FAFM-03", "§4.2#p6", "§4.8#p1", "§4.8#p2", "EB-TBL-1@tabel-recycle-bin", "EB-TBL-2@tabel-recycle-bin", "EB-TBL-4@tabel-recycle-bin", "EB-TBL-5@checkbox-tabel-recycle-bin", "EB-SRC-6@filter-group-tabel-recycle-bin", "EB-FLT-6@tabel-recycle-bin"]
smoke: []
dependsOn: []
trace:
  "INV-05a": 5
  "S-04": [41, 44]
  "S-28a": [40, 41, 43, 44, 58, 59]
  "S-28b": [47, 48]
  "T-FAFM-03": [9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 86]
  "§4.2#p6": [2, 3, 4, 5, 7]
  "§4.8#p1": 38
  "§4.8#p2": 38
  "EB-TBL-1@tabel-recycle-bin": [40, 43, 47, 50, 51, 53, 58]
  "EB-TBL-2@tabel-recycle-bin": 17
  "EB-TBL-4@tabel-recycle-bin": [23, 24, 25, 26, 27, 28, 29, 31, 33, 35]
  "EB-TBL-5@checkbox-tabel-recycle-bin": 38
  "EB-SRC-6@filter-group-tabel-recycle-bin": [64, 65, 67, 68]
  "EB-FLT-6@tabel-recycle-bin": [73, 74, 78, 79, 80, 82, 83]
anchor: [77]
coverage:
  web: automated
---

# Dialog Recycle Bin: info retensi, format sel, nilai kosong, dan state data

## Prerequisites
- Aktor: pemegang capability Manage files dengan Read pada group `Branch Bandung`, serta Read dan Delete pada group `Head Office` beserta descendant (termasuk `Fleet`).
- Layar awal: Settings > File Manager.
- Komponen: Dialog Recycle Bin
- Data:
  - DU-087-1: File di Recycle Bin `laptop-old.png`, Category `Asset Photo`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`, Size `1048576` byte, Deleted Date `2026-11-02 14:30`, Deleted By `System`, batas purge `T0 + 28 hari 12 jam`.
    - Deleted Date yang diharapkan tampil `02/11/26 14:30`, dari `2026-11-02 14:30` dengan Date Format `dd/MM/yy` dan Time Format `HH:mm`.
    - Size yang diharapkan tampil `1.0 MB`, dari `1048576` byte.
    - Auto-Purge In yang diharapkan tampil `29 days`, dari batas purge `T0 + 28 hari 12 jam` dibulatkan ke atas.
  - DU-087-2: File di Recycle Bin `damage-01.jpg`, Category `Damaged`, Source `Damaged Photo`, Asset `Toyota Avanza - 2`, Group `Branch Bandung`, Size `921600` byte, Deleted Date `2026-11-01 10:00`, Deleted By `Rina Anggraini`, batas purge `T0 + 27 hari 6 jam`. Group `Branch Bandung` bukan descendant `Head Office` dan aktor hanya memiliki Read di sana, sehingga di luar group Delete aktor.
    - Deleted By yang diharapkan tampil `Rina A`, dengan nama lengkap `Rina Anggraini` saat hover.
    - Auto-Purge In yang diharapkan tampil `28 days`, dari batas purge `T0 + 27 hari 6 jam` dibulatkan ke atas.
  - DU-087-3: File di Recycle Bin `maint-before-0031.jpg`, Category `Maintenance`, Source `Maintenance Before Photo`, Asset `Printer HP M404 - 1`, Group `Branch Bandung`, Size `768000` byte, Deleted Date `2026-10-05 09:00`, Deleted By `Rina Anggraini`, batas purge `T0 + 18 jam`.
    - Auto-Purge In yang diharapkan tampil `1 day`, dari batas purge `T0 + 18 jam` dibulatkan ke atas.
  - DU-087-4: File di Recycle Bin `repair-02.jpg`, Category `Damaged`, Source `Repair Photo`, Asset `Toyota Avanza - 2`, Group `Branch Bandung`, Size `901120` byte, Deleted Date `2026-10-04 16:00`, Deleted By `Dodi Pratama`, batas purge `T0 - 2 jam` (sudah lewat).
    - Deleted By yang diharapkan tampil `Dodi P`, dengan nama lengkap `Dodi Pratama` saat hover.
    - Auto-Purge In yang diharapkan tampil `0 days`, karena batas purge sudah lewat.
  - DU-087-5: File Draft di Recycle Bin `draft-photo-01.jpg`, Category `Asset Photo`, Source `Asset Photo`, tanpa Asset, Group `Head Office`, Size `655360` byte, Deleted Date `2026-11-10 08:15`, Deleted By `Budi`, batas purge `T0 + 29 hari 20 jam`.
  - DU-087-6: File di Recycle Bin `calibration-cert.pdf`, Category `Asset Documents`, Source `Attachment`, Asset `Laptop Dell Latitude 5420 - 9`, Group `Fleet` dengan hierarki `Head Office > Fleet`, Size `317440` byte, Deleted Date `2026-10-20 13:45`, Deleted By `Alexander Graham Bell`, batas purge `T0 + 10 hari 3 jam`.
    - Deleted By yang diharapkan tampil `Alexander G`, dengan nama lengkap `Alexander Graham Bell` saat hover.
    - Group yang diharapkan menampilkan hierarki `Head Office > Fleet` saat hover.
  - DU-087-7: File di Recycle Bin `warranty-card-mon0007.pdf`, Category `Asset Documents`, Source `Custom Field Document`, Asset `Monitor LG 24 - 7`, Group `Head Office`, Size `307200` byte, Deleted Date `2026-10-18 09:10`, Deleted By `Buzzlightyear Sumardi`, batas purge `T0 + 8 hari 1 jam`.
    - Deleted By yang diharapkan tampil `Buzzlightyear S`.
  - DU-087-8: File di Recycle Bin `handover-brw0150.jpg`, Category `Borrow`, Source `Handover Photo`, Asset `Laptop Dell Latitude 5420 - 9`, Group `Head Office`, Size `655360` byte, Deleted Date `2026-10-22 11:20`, Deleted By `Dewi Anggraini`, batas purge `T0 + 12 hari 5 jam`.
    - Deleted By yang diharapkan tampil `Dewi A`, dengan nama lengkap `Dewi Anggraini` saat hover.
  - DU-087-9: File di Recycle Bin `handover-brw0151.jpg`, Category `Borrow`, Source `Handover Photo`, Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`, Size `675840` byte, Deleted Date `2026-10-22 11:40`, Deleted By `Dewi Anggreni`, batas purge `T0 + 12 hari 5 jam`.
    - Deleted By yang diharapkan tampil `Dewi A`, dengan nama lengkap `Dewi Anggreni` saat hover.
  - DU-087-10: Daftar Recycle Bin entitas tanpa file terhapus.
  - DU-087-11: File di Recycle Bin `old-label.png` pada group `Branch Surabaya`, di luar seluruh group yang bisa dibaca aktor.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.
  - Retensi Recycle Bin bernilai `30 hari`.
  - K1: daftar berisi DU-087-1 sampai DU-087-9, dan pohon Group di Filter Panel memuat `Head Office` (dengan descendant `Fleet`) dan `Branch Bandung` sebagai dua node tingkat atas yang terpisah.
  - K2: daftar berisi DU-087-1 dan Retensi Recycle Bin bernilai `1 hari`.
  - K3: daftar kosong, entitas tanpa file terhapus (DU-087-10), tanpa Search dan Filter aktif.
  - K4: daftar kosong untuk aktor, karena satu-satunya file (DU-087-11) berada di luar group aktor.
  - K5: daftar berisi DU-087-1 sampai DU-087-9, dan Search `foto-tidak-ada.png` tidak cocok dengan satu pun baris sehingga respons kosong.
  - K6: memuat daftar gagal karena error server pada percobaan pertama, dan percobaan berikutnya berhasil memuat DU-087-1.
  - K7: daftar hanya berisi DU-087-5, Permanently Delete atas DU-087-5 berhasil, dan daftar yang dimuat ulang kosong.

## Test Steps

### Dialog Recycle Bin memuat judul, info retensi, toolbar, dan tabel
1. Tampilkan Dialog Recycle Bin dengan kondisi K1
2. Verifikasi judul dialog `Recycle Bin`
3. Verifikasi info `Files are permanently deleted after 30 days.`
4. Verifikasi Search, Filter, dan Download tampil pada toolbar dialog
5. Verifikasi tabel dengan baris `laptop-old.png` tampil di dalam dialog

### Info retensi bentuk tunggal
6. Tampilkan Dialog Recycle Bin dengan kondisi K2
7. Verifikasi info `Files are permanently deleted after 1 day.`

### Format sel baris file
8. Tampilkan Dialog Recycle Bin dengan kondisi K1
9. Verifikasi baris `laptop-old.png` menampilkan `PNG` pada kolom `File Format`
10. Verifikasi baris `laptop-old.png` menampilkan `Head Office` pada kolom `Group`
11. Verifikasi baris `laptop-old.png` menampilkan `1.0 MB` pada kolom `Size`
12. Verifikasi baris `laptop-old.png` menampilkan `02/11/26 14:30` pada kolom `Deleted Date`
13. Verifikasi baris `laptop-old.png` menampilkan `System` pada kolom `Deleted By`
14. Verifikasi baris `damage-01.jpg` menampilkan `Damaged` pada kolom `Category`
15. Verifikasi baris `damage-01.jpg` menampilkan `Damaged Photo` pada kolom `Source`
16. Verifikasi baris `damage-01.jpg` menampilkan `Toyota Avanza - 2` pada kolom `Asset`
17. Verifikasi baris `draft-photo-01.jpg` menampilkan `—` pada kolom `Asset`
18. Verifikasi baris `laptop-old.png` menampilkan `29 days` pada kolom `Auto-Purge In`
19. Verifikasi baris `damage-01.jpg` menampilkan `28 days` pada kolom `Auto-Purge In`
20. Verifikasi baris `maint-before-0031.jpg` menampilkan `1 day` pada kolom `Auto-Purge In`
21. Verifikasi baris `repair-02.jpg` menampilkan `0 days` pada kolom `Auto-Purge In`

### Nama pengguna pada Deleted By tampil singkat dan lengkap saat hover
22. Tampilkan Dialog Recycle Bin dengan kondisi K1
23. Verifikasi baris `damage-01.jpg` menampilkan `Rina A` pada kolom `Deleted By`
24. Verifikasi baris `repair-02.jpg` menampilkan `Dodi P` pada kolom `Deleted By`
25. Verifikasi baris `calibration-cert.pdf` menampilkan `Alexander G` pada kolom `Deleted By`
26. Verifikasi baris `warranty-card-mon0007.pdf` menampilkan `Buzzlightyear S` pada kolom `Deleted By`
27. Verifikasi baris `draft-photo-01.jpg` menampilkan `Budi` pada kolom `Deleted By`
28. Verifikasi baris `handover-brw0150.jpg` menampilkan `Dewi A` pada kolom `Deleted By`
29. Verifikasi baris `handover-brw0151.jpg` menampilkan `Dewi A` pada kolom `Deleted By`
30. Arahkan kursor ke `Alexander G` pada baris `calibration-cert.pdf`
31. Verifikasi nama lengkap `Alexander Graham Bell` tampil pada kolom `Deleted By`
32. Arahkan kursor ke `Dewi A` pada baris `handover-brw0150.jpg`
33. Verifikasi nama lengkap `Dewi Anggraini` tampil pada kolom `Deleted By`
34. Arahkan kursor ke `Dewi A` pada baris `handover-brw0151.jpg`
35. Verifikasi nama lengkap `Dewi Anggreni` tampil pada kolom `Deleted By`

### Checkbox baris di luar group Delete aktor disabled dengan alasan baku
36. Tampilkan Dialog Recycle Bin dengan kondisi K1
37. Arahkan kursor ke checkbox baris `damage-01.jpg`
38. Verifikasi alasan `You don't have permission to do this.` tersampaikan pada checkbox baris `damage-01.jpg` yang disabled

### Recycle Bin kosong karena entitas tanpa file terhapus
39. Tampilkan Dialog Recycle Bin dengan kondisi K3
40. Verifikasi judul empty state `Recycle bin is empty`
41. Verifikasi deskripsi empty state `Deleted files will appear here before being permanently removed.`

### Recycle Bin kosong karena file di luar group aktor
42. Tampilkan Dialog Recycle Bin dengan kondisi K4
43. Verifikasi judul empty state `Recycle bin is empty`
44. Verifikasi deskripsi empty state `Deleted files will appear here before being permanently removed.`

### Search tanpa hasil menampilkan empty state tersaring
45. Tampilkan Dialog Recycle Bin dengan kondisi K5
46. Ketik Search `foto-tidak-ada.png`, tekan Enter
47. Verifikasi judul empty state `No results found` pada dialog Recycle Bin
48. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada dialog Recycle Bin

### Gagal memuat bukan empty state dan bisa dimuat ulang
49. Tampilkan Dialog Recycle Bin dengan kondisi K6
50. Verifikasi pesan `Unable to load this data.` pada dialog Recycle Bin
51. Verifikasi tombol `[Try Again]` pada dialog Recycle Bin
52. Klik `[Try Again]`
53. Verifikasi baris `laptop-old.png` tampil

### Recycle Bin menjadi kosong setelah file terakhir dihapus permanen
54. Tampilkan Dialog Recycle Bin dengan kondisi K7
55. Klik `⋯` pada baris `draft-photo-01.jpg`
56. Klik `Permanently Delete`
57. Klik `[Permanently Delete]` pada dialog konfirmasi
58. Verifikasi judul empty state `Recycle bin is empty`
59. Verifikasi deskripsi empty state `Deleted files will appear here before being permanently removed.`

### Pencarian di tree Group menyaring saat mengetik dan Enter tidak mengubah hasil
60. Tampilkan Dialog Recycle Bin dengan kondisi K1
61. Klik ikon `Filter` pada toolbar dialog
62. Klik field `Group` pada Filter Panel
63. Ketik `Head Office` pada kotak pencarian tree tanpa menekan Enter
64. Verifikasi node `Head Office` tampil pada tree Group dialog Recycle Bin[^drift-1]
65. Verifikasi node `Branch Bandung` tidak tampil pada tree Group dialog Recycle Bin[^drift-1]
66. Tekan Enter pada kotak pencarian tree
67. Verifikasi node `Head Office` tetap tampil pada tree Group dialog Recycle Bin[^drift-1]
68. Verifikasi node `Branch Bandung` tetap tidak tampil pada tree Group dialog Recycle Bin[^drift-1]

### Menyembunyikan kolom tidak menghapus field filter dan tidak membatalkan filter ter-Apply
69. Tampilkan Dialog Recycle Bin dengan kondisi K1
70. Klik ikon `Filter` pada toolbar dialog
71. Pilih `Damaged Photo` pada field `Source` di Filter Panel
72. Klik `[Apply]`
73. Verifikasi baris `damage-01.jpg` tampil pada tabel
74. Verifikasi baris `laptop-old.png` tidak tampil pada tabel
75. Klik header kolom Actions `⋯`
76. Hilangkan centang kolom `Source` pada panel Column Visibility
77. Verifikasi header kolom `File Name` tetap tampil pada tabel
78. Verifikasi header kolom `Source` tidak tampil pada tabel
79. Verifikasi baris `damage-01.jpg` tetap tampil pada tabel
80. Verifikasi baris `laptop-old.png` tetap tidak tampil pada tabel
81. Klik ikon `Filter` pada toolbar dialog
82. Verifikasi field `Source` tetap ada pada Filter Panel dengan pilihan `Damaged Photo`
83. Verifikasi titik penanda filter aktif tetap tampil pada ikon `Filter` dialog Recycle Bin

### Hover badge Group menampilkan hierarki lengkap
84. Tampilkan Dialog Recycle Bin dengan kondisi K1
85. Arahkan kursor ke badge Group `Fleet` pada baris `calibration-cert.pdf`
86. Verifikasi hierarki `Head Office > Fleet` tampil

[^drift-1]: Drift PRD/foundation vs kontrak komponen. PRD ekspektasi baku EB-SRC-6 dan foundation `prd-conventions.md` §31.3: pencarian tree berjalan saat Enter, bukan real-time. Kontrak `TreeSelect#9`: kotak cari di dialog tree picker menyaring node saat mengetik, node cocok tampil bersama ancestor-nya; `TreeSelect#42`: kotak cari menerima Enter sebagai no-op. Diasersi: kontrak, karena field Group di Filter Panel adalah tree picker dan aturan Enter §31.3 milik kotak cari sidebar tree (SB-7).
