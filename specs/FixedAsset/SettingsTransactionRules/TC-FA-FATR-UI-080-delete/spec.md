---
id: TC-FA-FATR-UI-080-delete
title: "Dialog Delete override dan Dialog Blok"
layer: ui-client
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - "§4.1#r13"
  - "§4.1#r376"
  - "§4.1#r377"
  - "§4.1#r378"
  - "§4.1#r379"
  - "§4.5#b4"
  - "§6#r3"
  - "§6#r27"
  - "§6#r28"
  - "§7#r5"
  - "§7#r6"
  - "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f"
  - "D-06"
  - "D-07"
  - "§9.2#b108"
  - "§9.2#b113"
  - "§9.2#b119"
  - "§9.2#b177"
  - "§9.2#b179"
  - "§9.2#b186"
  - "§9.2#b191"
  - "§9.4.2#r33"
  - "§9.4.2#r83"
  - "§9.4.2#r84"
  - "§9.4.2#r88"
  - "§9.4.2#r122"
  - "§9.4.4#r31"
  - "§9.6#r30"
  - "§9.9#r22"
  - "EB-FB-1@delete-override"
  - "EB-FB-2@delete-override"
  - "EB-ERR-1@delete-override"
  - "EB-ERR-2@delete-override"
  - "EB-BLK-3"
  - "§4.4#r19"
  - "§9.6#r3"
smoke: []
dependsOn: []
trace:
  §4.1#r13: [2, 8]
  §4.1#r376: 14
  §4.1#r377: 15
  §4.1#r378: 16
  §4.1#r379: [4, 10, 14]
  §4.5#b4: [23, 25, 84, 86, 88]
  §6#r3: [56, 66]
  §6#r27: [54, 56, 57, 60, 63]
  §6#r28: [58, 67]
  §7#r5: [32, 36]
  §7#r6: [43, 50]
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": 57
  D-06: [3, 4, 5, 6, 9, 10, 11, 12, 18]
  D-07: [54, 55, 57]
  §9.2#b108: [2, 8]
  §9.2#b113: [54, 56]
  §9.2#b119: [64, 65]
  §9.2#b177: [43, 50]
  §9.2#b179: [45, 47, 76, 78]
  §9.2#b186: [54, 56]
  §9.2#b191: [63, 67]
  §9.4.2#r33: [43, 47, 50, 74, 75]
  §9.4.2#r83: [54, 56]
  §9.4.2#r84: [58, 67]
  §9.4.2#r88: [63, 64, 65]
  §9.4.2#r122: [2, 6, 33]
  §9.4.4#r31: 45
  §9.6#r30: [58, 67]
  §9.9#r22: [56, 66]
  EB-FB-1@delete-override: [32, 36, 43]
  EB-FB-2@delete-override: [20, 58]
  EB-ERR-1@delete-override: [43, 44, 50, 51, 71]
  EB-ERR-2@delete-override: [25, 26, 29, 39, 40, 81]
  EB-BLK-3: [56, 66]
  "§4.4#r19": 8
  "§9.6#r3": [43, 47]
anchor: []
coverage:
  web: automated
---

# Dialog Delete override dan Dialog Blok

## Prerequisites
- Aktor: Manage asset & TAG (Read + Update) pada Group `Proyek Karawang`.
- Layar awal: Settings > Transaction Settings, bagian `Overrides` pada Category `Vehicle > Pool car`. Dialog Delete override dibuka dari menu baris `Delete` atau dari menu `[Bulk Action]` `Delete`, menurut kondisi.
- Komponen: Dialog Delete override
- Data:
  - DU-080-1: override Borrow Scope `Group`, Target `Proyek Karawang`, Overridden `Max duration (30 days)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-15 14:05`, dalam cakupan Group aktor.
  - DU-080-2: override Borrow Scope `Group`, Target `Workshop`, Overridden `Max extensions (1)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-14 10:20`, turunan Group aktor.
  - DU-080-3: override Borrow Scope `Group`, Target `Proyek Bekasi`, Overridden `Auto-approve (OFF)`, Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-06-03 10:00`, di luar cakupan Group aktor.
  - DU-080-4: override Assign Scope `Group`, Target `Proyek Karawang`, Overridden `Allowed assignee: Employee (ON)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-10 09:00`, dalam cakupan Group aktor.
  - DU-080-5: override Assign Scope `Group`, Target `Workshop`, Overridden `Allowed assignee: Division (ON)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-09 09:30`, turunan Group aktor.
  - DU-080-6: override Assign Scope `Group`, Target `Proyek Bekasi`, Overridden `Allowed assignee: Employee (OFF)`, Category `Vehicle > Pool car`, Created By `Siti Nurbaya`, Created At `2026-06-08 08:15`, di luar cakupan Group aktor.
  - DU-080-7: override Assign yang tersisa Scope `Asset`, Target `EXC-0001 · Excavator PC200 - 1` (aset di Group `Proyek Karawang`, dalam cakupan Group aktor), Overridden `Allowed assignee: Division (OFF)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-07 11:00`.
  - DU-080-8: override Assign yang tersisa Scope `Asset`, Target `VEH-0001 · Toyota Avanza - 1` (aset di Group `Workshop`, turunan Group aktor), Overridden `Allowed assignee: Employee (OFF)`, Category `Vehicle > Pool car`, Created By `Budi Santoso`, Created At `2026-06-06 14:10`.
- Kondisi:
  - K1: dialog dibuka dari menu baris `Delete` pada DU-080-1; server menerima permintaan Delete.
  - K2: sama dengan K1; permintaan Delete pertama gagal karena error server, dan permintaan berikutnya diterima.
  - K3: sama dengan K1; permintaan Delete tidak mendapat respons (timeout).
  - K4: dialog dibuka dari menu baris `Delete` pada DU-080-4; DU-080-7 masih tersisa pada Target di bawahnya dan Allow Assign efektif aset itu bukan Deny; server menolak permintaan Delete karena guard Allowed assignee: nilai warisan `Allowed assignee: Employee` bernilai OFF, sehingga penghapusan DU-080-4 membuat kombinasi efektif `Allowed assignee: Employee` dan `Allowed assignee: Division` pada DU-080-7 keduanya OFF.
  - K5: dialog dibuka dari menu `[Bulk Action]` `Delete` dengan seleksi DU-080-4, DU-080-5, dan DU-080-6; DU-080-7 dan DU-080-8 masih tersisa dan Allow Assign efektif aset keduanya bukan Deny; server menolak penghapusan DU-080-4 dan DU-080-5 karena guard Allowed assignee (penghapusan DU-080-4 membuat kombinasi efektif `Allowed assignee: Employee` dan `Allowed assignee: Division` pada DU-080-7 keduanya OFF, dan penghapusan DU-080-5 membuat kombinasi efektif keduanya pada DU-080-8 OFF, dengan nilai warisan OFF), sehingga tidak ada override yang terhapus.
  - K6: dialog dibuka dari menu `[Bulk Action]` `Delete` dengan seleksi DU-080-1 dan DU-080-2; server menerima permintaan Delete.
  - K7: dialog dibuka dari menu `[Bulk Action]` `Delete` dengan seleksi DU-080-1, DU-080-2, dan DU-080-3.
  - K8: sama dengan K1; server belum merespons permintaan Delete sampai pengujian selesai.

## Test Steps

### Dialog konfirmasi satu override
1. Tampilkan Dialog Delete override dengan kondisi K1
2. Verifikasi dialog konfirmasi tampil sesudah `Delete` dipilih
3. Verifikasi judul dialog `Delete Override`
4. Verifikasi satu bullet `Proyek Karawang - Vehicle > Pool car - Max duration`
5. Verifikasi penutup `Are you sure you want to delete it? This action cannot be undone.`
6. Verifikasi tombol `[Cancel]` dan `[Delete]`

### Dialog konfirmasi bulk homogen
7. Tampilkan Dialog Delete override dengan kondisi K6
8. Verifikasi dialog konfirmasi tampil sesudah `Delete` pada menu bulk dipilih
9. Verifikasi judul dialog `Delete Overrides`
10. Verifikasi dua bullet `Proyek Karawang - Vehicle > Pool car - Max duration` dan `Workshop - Vehicle > Pool car - Max extensions`
11. Verifikasi penutup `Are you sure you want to delete them? This action cannot be undone.`
12. Verifikasi tombol `[Cancel]` dan `[Delete]`

### Dialog konfirmasi seleksi campuran
13. Tampilkan Dialog Delete override dengan kondisi K7
14. Verifikasi bullet `Proyek Karawang - Vehicle > Pool car - Max duration` dan `Workshop - Vehicle > Pool car - Max extensions` tampil lebih dahulu untuk override yang akan dihapus
15. Verifikasi satu paragraf `Some overrides are outside your scope and will be skipped:` tampil sesudah bullet override yang akan dihapus, disertai bullet `Proyek Bekasi - Vehicle > Pool car - Auto-approve`
16. Verifikasi penutup `Are you sure you want to continue?` tampil sesudah daftar yang dilewati, dengan tombol `[Cancel]` dan `[Continue]`[^drift-2]

### Cancel, Esc, dan backdrop tidak menghapus
17. Tampilkan Dialog Delete override dengan kondisi K1
18. Verifikasi dialog konfirmasi `Delete Override` tampil dengan tombol `[Cancel]`
19. Klik `[Cancel]`
20. Verifikasi dialog tertutup tanpa toast
21. Tampilkan Dialog Delete override dengan kondisi K1
22. Klik backdrop di luar dialog
23. Verifikasi dialog tetap terbuka
24. Tekan `Esc`
25. Verifikasi dialog tertutup tanpa toast dan override `Proyek Karawang` tetap tampil di tabel
26. Verifikasi fokus kembali ke tombol `⋯` baris `Proyek Karawang` yang membuka dialog

### Fokus terkunci di dalam dialog
27. Tampilkan Dialog Delete override dengan kondisi K1
28. Tekan `Tab` berulang kali sampai melewati kontrol terakhir dialog
29. Verifikasi fokus tetap berada di dalam dialog

### Delete berhasil
30. Tampilkan Dialog Delete override dengan kondisi K1
31. Klik `[Delete]`
32. Verifikasi toast sukses `Success, override has been deleted.` tampil
33. Verifikasi dialog tertutup
34. Tampilkan Dialog Delete override dengan kondisi K6
35. Klik `[Delete]`
36. Verifikasi toast sukses `Success, override has been deleted.` tampil satu kali

### Klik ganda Delete
37. Tampilkan Dialog Delete override dengan kondisi K8
38. Klik ganda `[Delete]`
39. Verifikasi tombol `[Delete]` masuk keadaan saving dan disabled
40. Verifikasi hanya satu permintaan Delete yang terkirim

### Delete gagal karena error server
41. Tampilkan Dialog Delete override dengan kondisi K2
42. Klik `[Delete]`
43. Verifikasi toast error `Error, failed to delete override.` tampil
44. Verifikasi dialog `Delete Override` tetap terbuka dan tombol `[Delete]` aktif lagi
45. Verifikasi toast `Success, override has been deleted.` tidak tampil
46. Klik `[Cancel]`
47. Verifikasi override `Proyek Karawang` tetap tampil di tabel Overrides

### Delete tanpa respons
48. Tampilkan Dialog Delete override dengan kondisi K3
49. Klik `[Delete]`
50. Verifikasi toast error `Connection problem. Please try again.` tampil[^drift-1]
51. Verifikasi dialog `Delete Override` tetap terbuka dan tombol `[Delete]` aktif lagi

### Dialog Blok penolakan guard pada satu override
52. Tampilkan Dialog Delete override dengan kondisi K4
53. Klik `[Delete]`
54. Verifikasi dialog konfirmasi tertutup dan Dialog Blok tampil dengan judul `Cannot Delete Override`
55. Verifikasi Dialog Blok memuat bullet `Proyek Karawang - Vehicle > Pool car - Allowed assignee: Employee`
56. Verifikasi Dialog Blok memuat pesan `At least one assignee type must be enabled` sebagai isi dialog, bukan error inline
57. Verifikasi Dialog Blok hanya memuat satu tombol `[OK]`
58. Verifikasi tidak ada toast yang tampil
59. Klik `[OK]`
60. Verifikasi Dialog Blok tertutup

### Dialog Blok pada bulk tanpa satu pun override terhapus
61. Tampilkan Dialog Delete override dengan kondisi K5
62. Klik `[Delete]`
63. Verifikasi hanya Dialog Blok yang tampil dengan judul `Cannot Delete Overrides`
64. Verifikasi Dialog Blok memuat bullet `Proyek Karawang - Vehicle > Pool car - Allowed assignee: Employee` dan `Workshop - Vehicle > Pool car - Allowed assignee: Division`
65. Verifikasi Dialog Blok tidak memuat bullet `Proyek Bekasi - Vehicle > Pool car - Allowed assignee: Employee`
66. Verifikasi Dialog Blok memuat pesan `At least one assignee type must be enabled` dan satu tombol `[OK]`
67. Verifikasi tidak ada toast yang tampil

### Percobaan ulang Delete di dialog yang sama sesudah error server
68. Tampilkan Dialog Delete override dengan kondisi K2
69. Klik `[Delete]`
70. Klik `[Delete]` sekali lagi pada dialog yang sama
71. Verifikasi toast sukses `Success, override has been deleted.` tampil satu kali

### Delete tanpa respons tidak menghapus override
72. Tampilkan Dialog Delete override dengan kondisi K3
73. Klik `[Delete]`
74. Verifikasi toast error `Connection problem. Please try again.` tampil[^drift-1]
75. Verifikasi tombol `[Delete]` aktif lagi
76. Verifikasi dialog `Delete Override` tetap terbuka
77. Klik `[Cancel]`
78. Verifikasi override `Proyek Karawang` tetap tampil di tabel Overrides

### Klik ganda Delete diterima server
79. Tampilkan Dialog Delete override dengan kondisi K1
80. Klik ganda `[Delete]`
81. Verifikasi toast sukses `Success, override has been deleted.` tampil tepat satu kali

### Dialog Blok: backdrop dan Esc
82. Tampilkan Dialog Delete override dengan kondisi K4
83. Klik `[Delete]`
84. Verifikasi Dialog Blok tampil dengan judul `Cannot Delete Override`
85. Klik backdrop di luar dialog
86. Verifikasi Dialog Blok tetap terbuka
87. Tekan `Esc`
88. Verifikasi Dialog Blok tertutup

[^drift-1]: Drift PRD vs foundation. PRD §7 T-06 dan §9.2 F-FATR-06.k11a: Delete gagal karena error server atau timeout menampilkan toast T-06. Foundation `error-handling-convention.md` §2: timeout menampilkan toast `Connection problem. Please try again.`. Diasersi: foundation (SB-4).

[^drift-2]: Drift PRD vs foundation. PRD §4.1 `DO-12`: penutup dialog seleksi campuran `Are you sure you want to delete them? This action cannot be undone.` dengan tombol `[Cancel]` dan `[Delete]`. Foundation `functions/toast-copy.md` (Aturan Terkunci #10 dan Dialog Konfirmasi poin 5): bulk dengan outcome campuran, dua kelompok bullet, ditutup `Are you sure you want to continue?` dengan tombol `[Continue]`. Diasersi: foundation, karena dialog konfirmasi bulk adalah pola bersama (SB-4).
