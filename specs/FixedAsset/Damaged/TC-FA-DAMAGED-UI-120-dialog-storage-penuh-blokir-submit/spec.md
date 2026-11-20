---
id: TC-FA-DAMAGED-UI-120-dialog-storage-penuh-blokir-submit
title: "Dialog Report Damaged dan Mark as Repaired saat Storage penuh: Submit ditolak dengan toast Error persisten, dialog tetap terbuka dengan isian utuh, tombol tidak Disabled, dan Submit berhasil setelah Storage dibebaskan"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [DAMAGED-LOGIC-10c, DAMAGED-LOGIC-10d, DAMAGED-LOGIC-10e, V-DMG-20, TS-DMG-11, TS-DMG-12, F-DMG-01.k10, F-DMG-05.k7]
smoke: []
dependsOn: []
trace:
  DAMAGED-LOGIC-10c: [7, 24, 32, 40, 50, 61, 74]
  DAMAGED-LOGIC-10d: [7, 24, 32, 50, 66, 67, 74]
  DAMAGED-LOGIC-10e: [8, 9, 10, 11, 25, 26, 33, 34, 51, 52, 53, 62]
  V-DMG-20: [5, 7, 8, 14, 24, 25, 32, 33, 40, 48, 50, 51, 61, 62, 74]
  TS-DMG-11: [7, 13, 24, 32, 40]
  TS-DMG-12: [50, 55, 61, 74]
  F-DMG-01.k10: [7, 24, 32, 40]
  F-DMG-05.k7: [50, 61, 74]
anchor: [42, 66, 76]
coverage:
  web: automated
---

# Dialog Report Damaged dan Mark as Repaired saat Storage penuh: Submit ditolak dengan toast Error persisten, dialog tetap terbuka dengan isian utuh, tombol tidak Disabled, dan Submit berhasil setelah Storage dibebaskan

## Prerequisites
- Aktor: Aktor Damaged pada Group aset; pada K3 pelapor umum.
- Layar awal: Dialog Report Damaged dan Dialog Mark as Repaired belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Report Damaged (D-DMG-01), Dialog Mark as Repaired (D-DMG-02)
- Data:
  - DU-120-1: Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`.
  - DU-120-2: Asset `Projector Epson EB-X06 - 2`, Asset ID `PRJ-2026-0002`, Group `Head Office`.
  - DU-120-3: record `Damaged` untuk aset `Toyota Avanza - 2`, Asset ID `VEH-2026-0002`, Group `Head Office`, tanpa TAG.
  - DU-120-4: laporan valid lengkap untuk satu aset: What happened `Layar retak dan perangkat tidak menyala` dan foto `kerusakan-layar.jpeg`.
  - DU-120-5: laporan valid lengkap untuk dua aset: What happened `Bodi perangkat retak dan tidak dapat dipakai`, foto `kerusakan-laptop.jpeg` untuk `Laptop Dell Latitude 5420 - 4`, foto `kerusakan-proyektor.jpeg` untuk `Projector Epson EB-X06 - 2`.
  - DU-120-6: Repair note `Layar diganti baru dan sudah diuji fungsi` dan After photo `foto-sesudah.jpeg`.
  - DU-120-7: Storage penuh: usage ledger Storage client sama dengan kuota, `50.0 GB` dari `50.0 GB`.
  - DU-120-8: Storage melebihi kuota: usage ledger `51.2 GB`, kuota `50.0 GB`.
- Kondisi:
  - K1: satu aset terpilih (DU-120-1); Storage penuh DU-120-7; respons simpan ditolak karena Storage penuh.
  - K2: dua aset terpilih (DU-120-1 dan DU-120-2); Storage melebihi kuota DU-120-8; respons simpan ditolak karena Storage penuh.
  - K3: satu aset terpilih (DU-120-1), pelapor umum; Storage penuh DU-120-7; respons simpan ditolak karena Storage penuh.
  - K4: satu aset terpilih (DU-120-1); respons simpan pertama ditolak karena Storage penuh DU-120-7, respons berikutnya sukses (Storage dibebaskan).
  - K5: record DU-120-3; setting After photo required bernilai `ON`; Storage penuh DU-120-7; respons simpan ditolak karena Storage penuh.
  - K6: record DU-120-3; setting After photo required bernilai `OFF`; Storage penuh DU-120-7; respons simpan ditolak karena Storage penuh.
  - K7: record DU-120-3; setting After photo required bernilai `OFF`; Storage penuh DU-120-7; tanpa After photo; respons simpan sukses.
  - K8: record DU-120-3; setting After photo required bernilai `ON`; respons simpan pertama ditolak karena Storage penuh DU-120-7, respons berikutnya sukses (Storage dibebaskan).

## Test Steps

### Report Damaged satu aset ditolak saat Storage penuh
1. Tampilkan Dialog Report Damaged dengan kondisi K1
2. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
3. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
4. Klik `Apply` pada dialog `Adjust photo`
5. Verifikasi tombol `[Report Damaged]` tidak Disabled sebelum diklik
6. Klik `[Report Damaged]`
7. Verifikasi toast Error `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` tampil
8. Verifikasi dialog Report Damaged tetap terbuka
9. Verifikasi isian `What happened*` masih berisi `Layar retak dan perangkat tidak menyala`
10. Verifikasi foto `kerusakan-layar.jpeg` masih tampil pada pemilih foto `Damaged Photo*`
11. Verifikasi tidak ada toast sukses yang tampil
12. Waktu berlalu sampai 5 detik sejak toast tampil
13. Verifikasi toast Error `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` masih tampil karena bersifat persisten
14. Verifikasi tombol `[Report Damaged]` tidak Disabled dan dapat diklik lagi
15. Klik `[Cancel]`
16. Klik `[Leave]` pada dialog `Unsaved Changes`

### Report Damaged dua aset ditolak seluruhnya dengan nilai terpakai melebihi kuota
17. Tampilkan Dialog Report Damaged dengan kondisi K2
18. Isi `What happened*` dengan `Bodi perangkat retak dan tidak dapat dipakai`
19. Pilih berkas foto `kerusakan-laptop.jpeg` pada pemilih foto aset `Laptop Dell Latitude 5420 - 4`
20. Klik `Apply` pada dialog `Adjust photo`
21. Pilih berkas foto `kerusakan-proyektor.jpeg` pada pemilih foto aset `Projector Epson EB-X06 - 2`
22. Klik `Apply` pada dialog `Adjust photo`
23. Klik `[Report Damaged]`
24. Verifikasi toast Error `Error, failed to report damage. Storage is full (51.2 GB of 50.0 GB used).` tampil
25. Verifikasi dialog Report Damaged tetap terbuka dengan blok aset `Laptop Dell Latitude 5420 - 4` dan `Projector Epson EB-X06 - 2` dan isian `What happened*` tidak direset
26. Verifikasi tidak ada toast sukses dan tidak ada keterangan `Already reported damaged` yang tampil untuk salah satu aset

### Report Damaged oleh pelapor umum ditolak saat Storage penuh
27. Tampilkan Dialog Report Damaged dengan kondisi K3
28. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
29. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
30. Klik `Apply` pada dialog `Adjust photo`
31. Klik `[Report Damaged]`
32. Verifikasi toast Error `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` tampil
33. Verifikasi dialog Report Damaged tetap terbuka
34. Verifikasi tidak ada toast `Success, your report has been sent to the asset admins.` yang tampil

### Report Damaged berhasil setelah Storage dibebaskan
35. Tampilkan Dialog Report Damaged dengan kondisi K4
36. Isi `What happened*` dengan `Layar retak dan perangkat tidak menyala`
37. Pilih berkas foto `kerusakan-layar.jpeg` pada pemilih foto `Damaged Photo*`
38. Klik `Apply` pada dialog `Adjust photo`
39. Klik `[Report Damaged]`
40. Verifikasi toast Error `Error, failed to report damage. Storage is full (50.0 GB of 50.0 GB used).` tampil
41. Klik `[Report Damaged]` sekali lagi tanpa mengubah isian
42. Verifikasi toast `Success, asset has been reported damaged.` tampil
43. Verifikasi dialog Report Damaged tertutup

### Mark as Repaired dengan After photo wajib ditolak saat Storage penuh
44. Tampilkan Dialog Mark as Repaired dengan kondisi K5
45. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
46. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo*`
47. Klik `Apply` pada dialog `Adjust photo`
48. Verifikasi tombol `[Mark as Repaired]` tidak Disabled sebelum diklik
49. Klik `[Mark as Repaired]`
50. Verifikasi toast Error `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` tampil
51. Verifikasi dialog Mark as Repaired tetap terbuka
52. Verifikasi isian `Repair note*` masih berisi `Layar diganti baru dan sudah diuji fungsi`
53. Verifikasi tidak ada toast sukses yang tampil
54. Waktu berlalu sampai 5 detik sejak toast tampil
55. Verifikasi toast Error `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` masih tampil karena bersifat persisten

### Mark as Repaired dengan After photo opsional yang diisi ditolak saat Storage penuh
56. Tampilkan Dialog Mark as Repaired dengan kondisi K6
57. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
58. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo`
59. Klik `Apply` pada dialog `Adjust photo`
60. Klik `[Mark as Repaired]`
61. Verifikasi toast Error `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` tampil
62. Verifikasi dialog Mark as Repaired tetap terbuka

### Mark as Repaired tanpa After photo tidak dicek Storage
63. Tampilkan Dialog Mark as Repaired dengan kondisi K7
64. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
65. Klik `[Mark as Repaired]`
66. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil
67. Verifikasi toast Error Storage penuh tidak tampil
68. Verifikasi dialog Mark as Repaired tertutup

### Mark as Repaired berhasil setelah Storage dibebaskan
69. Tampilkan Dialog Mark as Repaired dengan kondisi K8
70. Isi `Repair note*` dengan `Layar diganti baru dan sudah diuji fungsi`
71. Pilih berkas foto `foto-sesudah.jpeg` pada pemilih foto `After photo*`
72. Klik `Apply` pada dialog `Adjust photo`
73. Klik `[Mark as Repaired]`
74. Verifikasi toast Error `Error, failed to mark asset as repaired. Storage is full (50.0 GB of 50.0 GB used).` tampil
75. Klik `[Mark as Repaired]` sekali lagi tanpa mengubah isian
76. Verifikasi toast `Success, Toyota Avanza - 2 has been marked as repaired.` tampil
77. Verifikasi dialog Mark as Repaired tertutup

## Notes
- Spec ini bersumber dari PRD `damaged.md` (DAMAGED-LOGIC-10c sampai 10e, V-DMG-20, TS-DMG-11, TS-DMG-12); belum ada TestCase untuk aturan Storage penuh, sehingga keterlacakan memakai ID aturan PRD.
- Nilai `50.0 GB of 50.0 GB` dan `51.2 GB of 50.0 GB` adalah contoh nilai Data (DU-120-7, DU-120-8); format Size mengikuti T-FAFM-01 (`file-manager.md` §4.2a), seperti contoh PRD di §7.3.
- Jeda 5 detik pada asersi toast persisten adalah pilihan spec (lebih lama dari auto-hide toast sukses 4 detik).
- Form modul asal (Return, Unassign, Receive, Stock Opname, Mark as Found) menampilkan toast Storage penuh miliknya sendiri; asersinya dimiliki spec modul asal, bukan spec ini.
- Di atas 35 langkah (77) karena delapan kondisi respons dengan siklus isi dialog yang sama, dikelompokkan dalam satu spec per kemiripan prasyarat.
