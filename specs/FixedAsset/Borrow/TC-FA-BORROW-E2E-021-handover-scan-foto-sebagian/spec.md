---
id: TC-FA-BORROW-E2E-021-handover-scan-foto-sebagian
title: "Halaman Handover memverifikasi aset lewat scan TAG atau I Can't Scan the TAG, foto, dan handover sebagian"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-55", "FI-BRW-56", "FI-BRW-57", "FI-BRW-58", "FI-BRW-59", "FI-BRW-60", "FI-BRW-61", "FI-BRW-62", "FI-BRW-63", "FI-BRW-64", "FI-BRW-65", "FI-BRW-66", "FI-BRW-67", "FI-BRW-68", "FI-BRW-69", "FI-BRW-70", "FLD-BRW-07", "FLD-BRW-20", "FLD-BRW-21", "V-BRW-28", "V-BRW-29", "V-BRW-30", "V-BRW-31", "§4.2.5#p1", "§4.2.5#p2", "§4.4#r10", "§4.4#r11"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-55": 48
  "FI-BRW-56": 61
  "FI-BRW-57": 58
  "FI-BRW-58": 59
  "FI-BRW-59": [27, 29, 31, 32]
  "FI-BRW-60": 34
  "FI-BRW-61": 34
  "FI-BRW-62": 36
  "FI-BRW-63": 38
  "FI-BRW-64": 41
  "FI-BRW-65": 42
  "FI-BRW-66": 63
  "FI-BRW-67": 43
  "FI-BRW-68": 48
  "FI-BRW-69": 42
  "FI-BRW-70": 67
  "FLD-BRW-07": 51
  "FLD-BRW-20": 45
  "FLD-BRW-21": [51, 53, 55]
  "V-BRW-28": [27, 29, 31]
  "V-BRW-29": 34
  "V-BRW-30": 45
  "V-BRW-31": [51, 55]
  "§4.2.5#p1": [7, 8]
  "§4.2.5#p2": [6, 9, 10, 11, 13, 15, 16, 21, 22, 49]
  "§4.4#r10": 27
  "§4.4#r11": 29
anchor: []
coverage:
  web: automated
---

# Halaman Handover memverifikasi aset lewat scan TAG atau I Can't Scan the TAG, foto, dan handover sebagian

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-021-1: BRW `Waiting for Handover` Group `Head Office`, Borrower `Hendra Kusuma {runId}`, Requested By `Agus Pratama {runId}`, Note `Peminjaman untuk acara kantor`, Photo at start ON pada semua barisnya. Barisnya adalah aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 berstatus `Waiting for Handover`, dan aset DU-021-6 berstatus `Borrowed`.
  - DU-021-2: aset `Laptop Asus Zenbook {runId}`, Brand `Asus`, Model/Type `Zenbook 14`, TAG `RFID`, Category `Laptop`, Duration `3 / 7 days`, Purpose `Presentasi klien`.
  - DU-021-3: aset `Proyektor BenQ {runId}`, Brand `BenQ`, Model/Type `MW535`, TAG `QR`, Category `Proyektor`, Duration `2 / 7 days`, Purpose `Rapat divisi`.
  - DU-021-4: aset `Kamera Canon EOS {runId}`, Brand `Canon`, Model/Type `EOS 90D`, TAG `NFC`, Category `Kamera`, Duration `4 / 7 days`, Purpose `Dokumentasi acara`.
  - DU-021-5: aset `Speaker JBL {runId}`, Brand `JBL`, Model/Type `PartyBox 310`, TAG `RFID` yang tidak terbaca saat dipindai, Category `Audio`, Duration `1 / 3 days`, Purpose `Acara gathering`; Note laporan TAG yang dicoba `TAG tidak terbaca di lokasi serah terima`.
  - DU-021-6: aset `Headset Logitech {runId}` pada BRW yang sama dengan status `Borrowed`.
  - DU-021-7: aset `Genset Honda {runId}` pada BRW lain berstatus `Waiting for Approval` dengan approver `Rina W`.
  - DU-021-8: aset `Router Cisco {runId}` milik Group `Branch Surabaya`, di luar Group Aktor.
  - DU-021-9: aset `Printer HP {runId}` berstatus tersedia dan tidak berada di BRW DU-021-1; Asset ID-nya milik entri ini.
  - Asset ID aset DU-021-2 sampai DU-021-9 dibentuk sistem dan menjadi milik entri aset masing-masing.

## Test Steps

### Halaman Handover hanya memuat baris Waiting for Handover
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Hendra Kusuma {runId}`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-021-1
5. Klik `Hand Over`
6. Verifikasi header transaksi memuat Transaction ID milik DU-021-1, Requested By `Agus Pratama {runId}`, Borrower `Hendra Kusuma {runId}`, Group `Head Office`, Note `Peminjaman untuk acara kantor`, dan Last Updated
7. Verifikasi tabel Handover memuat aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5
8. Verifikasi tabel Handover tidak memuat aset DU-021-6 yang berstatus `Borrowed`
9. Verifikasi toolbar Handover memuat Search, Filter, dan tombol `[Verify Asset]`
10. Verifikasi kolom Verification baris DU-021-2 `Unverified`
11. Verifikasi teks bantu `Scanned assets are ready. Ask [Borrower] to confirm.` tidak tampil sebelum ada aset yang discan
12. Urutkan kolom `Duration` dengan `Shortest First`
13. Verifikasi urutan dari atas ke bawah adalah DU-021-5, DU-021-3, DU-021-2, DU-021-4
14. Ketik Search `Kamera Canon EOS {runId}`, tekan Enter
15. Verifikasi baris DU-021-4 tampil
16. Verifikasi baris DU-021-2, DU-021-3, dan DU-021-5 tidak tampil
17. Klik `(←)` pada kotak Search
18. Klik ikon Filter
19. Pada field `Brand` pilih `Canon`
20. Klik `[Apply]`
21. Verifikasi baris DU-021-4 tampil
22. Verifikasi baris DU-021-2, DU-021-3, dan DU-021-5 tidak tampil
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Klik ikon Filter

### Scan ditolak untuk TAG yang bukan baris BRW ini
26. Scan TAG aset DU-021-9 lewat `[Verify Asset]`
27. Verifikasi toast `Error, this TAG belongs to [Asset Code], not in this borrow.` tampil dengan [Asset Code] berisi Asset ID milik DU-021-9
28. Scan TAG aset DU-021-7 lewat `[Verify Asset]`
29. Verifikasi toast `Error, this asset is still waiting for approval from [Names].` tampil dengan [Names] berisi `Rina W`
30. Scan TAG aset DU-021-8 lewat `[Verify Asset]`
31. Verifikasi toast `Error, this asset belongs to [Group].` tampil dengan [Group] berisi `Branch Surabaya`
32. Verifikasi kolom Verification baris DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 tidak berubah dan tidak ada yang `Verified`

### Aset ber-tag yang tagnya tidak terbaca dilaporkan lewat I Can't Scan the TAG
33. Scan TAG aset DU-021-5 lewat `[Verify Asset]`
34. Verifikasi toast `Error, this TAG can't be read. Report the TAG and use another asset.` tampil dan handover aset DU-021-5 tidak dapat dimulai tanpa identifikasi manual
35. Klik menu ⋯ pada baris DU-021-5
36. Verifikasi menu ⋯ baris DU-021-5 memuat `I Can't Scan the TAG`
37. Klik `I Can't Scan the TAG`
38. Verifikasi dialog Report TAG biasa tampil dengan Report Type `Unreadable`, bukan varian identifikasi manual
39. Isi Note laporan dengan `TAG tidak terbaca di lokasi serah terima`
40. Klik tombol kirim laporan pada dialog Report TAG
41. Verifikasi kolom Verification baris DU-021-5 menampilkan teks `TAG reported. Replace the TAG to hand over.`
42. Verifikasi baris DU-021-5 nonaktif untuk Verify, foto, dan Request Confirmation, tanpa pilihan identifikasi manual, sehingga tidak dapat diserahkan oleh siapa pun
43. Verifikasi baris DU-021-5 tetap tampil di daftar Handover sebagai `Waiting for Handover`

### Request Confirmation memerlukan minimal satu aset terverifikasi dan foto per aset
44. Klik `[Request Confirmation]`
45. Verifikasi pesan `Verify at least one asset with Verify Asset.` tampil di atas tombol `[Request Confirmation]`
46. Scan TAG aset DU-021-2 lewat `[Verify Asset]`
47. Scan TAG aset DU-021-3 lewat `[Verify Asset]`
48. Verifikasi kolom Verification baris DU-021-2 dan DU-021-3 `Verified` dan baris DU-021-4 tetap `Unverified`, sehingga aset lain tetap dapat diserahkan
49. Verifikasi teks bantu `Scanned assets are ready. Ask [Borrower] to confirm.` tampil
50. Klik `[Request Confirmation]`
51. Verifikasi pesan `2 assets need a handover photo.` tampil di atas tombol `[Request Confirmation]`
52. Ambil foto pada kolom Handover Photo baris DU-021-2
53. Verifikasi kolom Handover Photo baris DU-021-2 menampilkan thumbnail foto
54. Klik `[Request Confirmation]`
55. Verifikasi pesan `1 asset needs a handover photo.` tampil di atas tombol `[Request Confirmation]`
56. Ambil foto pada kolom Handover Photo baris DU-021-3

### Handover sebagian: aset yang belum discan tetap Waiting for Handover
57. Klik `[Request Confirmation]`
58. Verifikasi popup `Waiting for Confirmation` tampil dengan pesan `1 asset will stay Waiting for Handover.`
59. Verifikasi daftar aset sesi konfirmasi memuat aset DU-021-2 dan DU-021-3 saja, tanpa aset DU-021-4
60. Klik `[Cancel Request]`
61. Verifikasi aset DU-021-2, DU-021-3, DU-021-4, dan DU-021-5 tetap `Waiting for Handover` sesudah permintaan dibatalkan

### Replace TAG selesai mengembalikan baris ke Unverified
62. Replace TAG aset DU-021-5 selesai dan laporan TAG terbuka ditutup `Replaced`
63. Verifikasi kolom Verification baris DU-021-5 kembali `Unverified` tanpa memuat ulang halaman
64. Buka Borrow Detail BRW milik DU-021-1 dari tabel Transactions
65. Klik menu ⋯ pada baris aset DU-021-5
66. Klik `Borrow Log`
67. Verifikasi Borrow Log aset DU-021-5 memuat node `TAG reported by [Reporter]` dengan daftar TAG yang dilaporkan
