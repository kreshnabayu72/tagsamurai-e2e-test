---
id: TC-FA-DAMAGED-E2E-007-tabel-history
title: "Sub-tab History menampilkan record selesai dengan Resolved By, Resolved Date, Duration, opsi filter snapshot, tanpa Bulk dan tanpa Search by Scan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-02, "§4.1#r2", "§5#r5", "§9.5#r3", "§9.5#r6", "§9.5#r7", "§9.2#b12", S-DMG-13, S-DMG-14, "§Aturan Logika Modul#r18", EB-SRC-5@tabel-history, EB-TBL-1@tabel-history, "§5#r1"]
smoke: []
dependsOn: []
trace:
  T-DMG-02: [7, 13, 14, 15, 16, 17, 18, 19, 20, 23, 26, 27, 42, 44, 45, 46, 50, 51, 53, 55, 57, 61, 62, 66, 67, 71, 72, 76]
  "§4.1#r2": [3]
  "§5#r5": [10]
  "§9.5#r3": [12]
  "§9.5#r6": [11]
  "§9.5#r7": [23, 24]
  "§9.2#b12": [7, 8]
  S-DMG-13: [79]
  S-DMG-14: [30, 31]
  "§Aturan Logika Modul#r18": [13, 42]
  EB-SRC-5@tabel-history: [33, 37, 40]
  EB-TBL-1@tabel-history: [30]
  "§5#r1": [3, 5, 9]
anchor: [78]
coverage:
  web: automated
---

# Sub-tab History menampilkan record selesai dengan Resolved By, Resolved Date, Duration, opsi filter snapshot, tanpa Bulk dan tanpa Search by Scan

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-007-1: record `Repaired`, Name `Riwayat Aset {runId} - 1`, Asset ID `RWY-0001-{runId}`, Group `Head Office {runId}`, Source `Borrow return`, Last Holder `Sari D`, Reported By `Rina W`, Reported Date `T0 − 20 hari, pukul 09:00`, Resolved By `Rina W`, Resolved Date `T0 − 14 hari, pukul 14:10`, Duration `6 days`, Category `Elektronik {runId}`.
  - DU-007-2: record `Disposed`, Name `Riwayat Aset {runId} - 2`, Asset ID `RWY-0002-{runId}`, Group `Head Office {runId}`, Source `Audit`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 30 hari, pukul 08:00`, Resolved By `System`, Resolved Date `T0 − 10 hari, pukul 00:30`, Duration `20 days`, Category `Elektronik {runId}`.
  - DU-007-3: record `Rejected`, Name `Riwayat Aset {runId} - 3`, Asset ID `RWY-0003-{runId}`, Group `Cabang Lama {runId}`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `Budi S`, Reported Date `T0 − 8 hari, pukul 08:30`, Resolved By `Rina W`, Resolved Date `T0 − 7 hari, pukul 09:15`, Duration `1 day`, Category `Peralatan Lama {runId}`.
  - DU-007-4: record `Canceled`, Name `Riwayat Aset {runId} - 4`, Asset ID `RWY-0004-{runId}`, Group `Gudang Lama {runId}`, Source `Reported by holder`, Last Holder `Dewi A`, Reported By `Dewi A`, Reported Date `T0 − 5 hari, pukul 10:00`, Resolved By `Dewi A`, Resolved Date `T0 − 4 hari, pukul 08:00`, Duration `1 day`, Category `Mebel Lama {runId}`.
  - DU-007-5: record berjalan `Damaged`, Name `Riwayat Aset {runId} - 5`, Asset ID `RWY-0005-{runId}`, Group `Head Office {runId}`, Source `Manual`, Reported By `Agus P`.
  - DU-007-6: Group `Cabang Lama {runId}` sudah dihapus, dan Group `Gudang Lama {runId}` sudah diganti nama menjadi `Gudang Baru {runId}`, sebelum spec dimulai; record DU-007-3 dan DU-007-4 menyimpan nama Group lama sebagai snapshot.
  - DU-007-7: kata kunci Search `Tidak Ada Hasil {runId}` yang tidak cocok dengan record mana pun.
  - DU-007-8: record `Repaired`, Name `Riwayat Aset {runId} - 6`, Asset ID `RWY-0006-{runId}`, Group `Head Office {runId}`, Category `Elektronik {runId}`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 41 hari, pukul 08:00`, Resolved By `Rina W`, Resolved Date `T0 − 38 hari, pukul 16:20`, Duration `3 days`.
  - DU-007-9: record `Canceled` untuk aset yang sama dengan DU-007-8, Name `Riwayat Aset {runId} - 6`, Asset ID `RWY-0006-{runId}`, Group `Head Office {runId}`, Category `Elektronik {runId}`, Source `Reported by holder`, Last Holder `Dewi A`, Reported By `Dewi A`, Reported Date `T0 − 36 hari, pukul 09:00`, Resolved By `Dewi A`, Resolved Date `T0 − 35 hari, pukul 11:30`, Duration `1 day`.
  - DU-007-10: Category `Peralatan Lama {runId}` sudah dihapus, dan Category `Mebel Lama {runId}` sudah diganti nama menjadi `Mebel Baru {runId}`, sebelum spec dimulai; record DU-007-3 dan DU-007-4 menyimpan nama Category lama sebagai snapshot.
  - DU-007-11: rentang Resolved Date `T0 − 14 hari` sampai `T0 − 10 hari`; rentang Duration Min `2`; rentang Duration Max `1`.
  - Keenam record selesai itu dan satu record berjalan itu adalah seluruh record milik spec ini; user `Rina W`, `Agus P`, `Sari D`, `Budi S`, dan `Dewi A` adalah user ber-runId.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Sub-tab History hanya memuat record selesai
1. Buka tab `Damaged` pada halaman Assets
2. Klik sub-tab `History`
3. Verifikasi ikon `Search`, `Filter`, dan `Download` tampil pada toolbar sub-tab History
4. Klik ikon `Search`
5. Verifikasi placeholder kotak Search adalah `Search asset name or ID...`
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi tabel memuat `6` baris, yaitu `Riwayat Aset {runId} - 1`, `Riwayat Aset {runId} - 2`, `Riwayat Aset {runId} - 3`, `Riwayat Aset {runId} - 4`, dan dua baris `Riwayat Aset {runId} - 6`
8. Verifikasi record `Riwayat Aset {runId} - 5` yang berstatus `Damaged` tidak tampil di sub-tab History
9. Verifikasi tombol `Search by Scan` tidak tampil di kotak Search sub-tab History
10. Verifikasi tabel tidak memiliki kolom Checkbox dan tidak menampilkan `Bulk Action`
11. Verifikasi ikon `Filter` di sub-tab History tidak menampilkan badge titik saringan aktif

### Urutan default History dari penyelesaian terbaru
12. Verifikasi baris berurutan dari atas: `Riwayat Aset {runId} - 4`, `Riwayat Aset {runId} - 3`, `Riwayat Aset {runId} - 2`, `Riwayat Aset {runId} - 1`, lalu dua baris `Riwayat Aset {runId} - 6` dengan record `Canceled` di atas record `Repaired`

### Isi baris record selesai
13. Verifikasi baris `Riwayat Aset {runId} - 1` menampilkan badge status `Repaired` dan Source `Borrow return`
14. Verifikasi baris `Riwayat Aset {runId} - 1` memuat Last Holder `Sari D`, Reported By `Rina W`, Resolved By `Rina W`, Reported Date pukul `09:00`, Resolved Date pukul `14:10`, dan Duration `6 days`
15. Verifikasi baris `Riwayat Aset {runId} - 2` menampilkan badge status `Disposed` dan Source `Audit`
16. Verifikasi baris `Riwayat Aset {runId} - 2` memuat Last Holder `—`, Reported By `Agus P`, Resolved By `System`, Resolved Date pukul `00:30`, dan Duration `20 days`
17. Verifikasi baris `Riwayat Aset {runId} - 3` menampilkan badge status `Rejected` dan Source `Reported by holder`
18. Verifikasi baris `Riwayat Aset {runId} - 3` memuat Group `Cabang Lama {runId}`, Last Holder `Budi S`, Reported By `Budi S`, Resolved By `Rina W`, Resolved Date pukul `09:15`, dan Duration `1 day`
19. Verifikasi baris `Riwayat Aset {runId} - 4` menampilkan badge status `Canceled` dan Source `Reported by holder`
20. Verifikasi baris `Riwayat Aset {runId} - 4` memuat Group `Gudang Lama {runId}`, Last Holder `Dewi A`, Reported By `Dewi A`, Resolved By `Dewi A`, Resolved Date pukul `08:00`, dan Duration `1 day`

### Opsi filter History mengikuti data tabel sebagai snapshot
21. Klik ikon `Filter`
22. Buka dropdown field `Status`
23. Verifikasi opsi `Repaired`, `Disposed`, `Rejected`, dan `Canceled` tampil
24. Verifikasi opsi `Damaged`, `Waiting for Confirmation`, `Reported Disposal`, dan `In Disposal Process` tidak tampil
25. Buka dropdown field `Group`
26. Verifikasi opsi `Cabang Lama {runId}` dan `Gudang Lama {runId}` tampil sebagai nama Group saat record selesai
27. Verifikasi opsi `Gudang Baru {runId}` tidak tampil karena belum ada record selesai atas nama Group itu
28. Klik ikon `Filter` untuk menutup Filter Panel

### Search tanpa hasil dan kolom yang disembunyikan
29. Ganti isi kotak search dengan `Tidak Ada Hasil {runId}`, tekan Enter
30. Verifikasi sub-tab History menampilkan `No results found`
31. Verifikasi tabel menampilkan `Try adjusting your search or filter.`
32. Ganti isi kotak search dengan `Gudang Lama {runId}`, tekan Enter
33. Verifikasi baris `Riwayat Aset {runId} - 4` tampil karena Group cocok
34. Klik header kolom Actions `⋯`
35. Hapus centang `Group`
36. Ganti isi kotak search dengan `Gudang Lama {runId}`, tekan Enter
37. Verifikasi baris `Riwayat Aset {runId} - 4` tidak tampil karena kolom Group disembunyikan
38. Centang `Group`
39. Ganti isi kotak search dengan `Gudang Lama {runId}`, tekan Enter
40. Verifikasi baris `Riwayat Aset {runId} - 4` tampil kembali karena kolom Group ditampilkan lagi

### Record selesai hanya menyediakan aksi Damage Log
41. Buka menu `⋯` pada baris `Riwayat Aset {runId} - 1`
42. Verifikasi menu baris hanya memuat aksi `Damage Log`

### Satu aset muncul lebih dari sekali dengan record berbeda
43. Ganti isi kotak search dengan `Riwayat Aset {runId} - 6`, tekan Enter
44. Verifikasi tabel memuat dua baris `Riwayat Aset {runId} - 6` dengan Asset ID `RWY-0006-{runId}` yang sama
45. Verifikasi satu baris `Riwayat Aset {runId} - 6` berstatus `Repaired` dengan Reported Date pukul `08:00`, Resolved Date pukul `16:20`, dan Duration `3 days`
46. Verifikasi baris `Riwayat Aset {runId} - 6` lainnya berstatus `Canceled` dengan Reported Date pukul `09:00`, Resolved Date pukul `11:30`, dan Duration `1 day`
47. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Opsi filter Category sebagai snapshot
48. Klik ikon `Filter`
49. Buka dropdown field `Category`
50. Verifikasi opsi `Elektronik {runId}`, `Peralatan Lama {runId}`, dan `Mebel Lama {runId}` tampil sebagai nama Category saat record selesai
51. Verifikasi opsi `Mebel Baru {runId}` tidak tampil karena belum ada record selesai atas nama Category itu

### Sort kolom Resolved Date dan Duration
52. Klik ikon sort pada header kolom `Resolved Date`
53. Verifikasi baris berurutan dari Resolved Date terlama: `Riwayat Aset {runId} - 6` berstatus `Repaired`, `Riwayat Aset {runId} - 6` berstatus `Canceled`, `Riwayat Aset {runId} - 1`, `Riwayat Aset {runId} - 2`, `Riwayat Aset {runId} - 3`, lalu `Riwayat Aset {runId} - 4`
54. Klik ikon sort pada header kolom `Duration`
55. Verifikasi tiga baris terakhir berurutan menurut Duration terkecil dulu: `Riwayat Aset {runId} - 6` berstatus `Repaired` (`3 days`), `Riwayat Aset {runId} - 1` (`6 days`), lalu `Riwayat Aset {runId} - 2` (`20 days`)
56. Klik ikon sort pada header kolom `Duration`
57. Verifikasi tiga baris pertama berurutan menurut Duration terbesar dulu: `Riwayat Aset {runId} - 2` (`20 days`), `Riwayat Aset {runId} - 1` (`6 days`), lalu `Riwayat Aset {runId} - 6` berstatus `Repaired` (`3 days`)
58. Klik ikon sort pada header kolom `Duration`

### Filter Resolved Date dan Duration
59. Pilih rentang tanggal Resolved Date dari `T0 − 14 hari` sampai `T0 − 10 hari`
60. Klik `[Apply]`
61. Verifikasi baris `Riwayat Aset {runId} - 1` dan `Riwayat Aset {runId} - 2` tampil, termasuk baris pada tanggal awal dan tanggal akhir rentang
62. Verifikasi baris `Riwayat Aset {runId} - 3`, `Riwayat Aset {runId} - 4`, dan `Riwayat Aset {runId} - 6` tidak tampil
63. Klik `[Clear Field]`
64. Isi `Min` pada field `Duration` dengan `2`
65. Klik `[Apply]`
66. Verifikasi baris `Riwayat Aset {runId} - 1`, `Riwayat Aset {runId} - 2`, dan `Riwayat Aset {runId} - 6` berstatus `Repaired` tampil
67. Verifikasi baris `Riwayat Aset {runId} - 3`, `Riwayat Aset {runId} - 4`, dan `Riwayat Aset {runId} - 6` berstatus `Canceled` tidak tampil
68. Klik `[Clear Field]`
69. Isi `Max` pada field `Duration` dengan `1`
70. Klik `[Apply]`
71. Verifikasi baris `Riwayat Aset {runId} - 3`, `Riwayat Aset {runId} - 4`, dan `Riwayat Aset {runId} - 6` berstatus `Canceled` tampil
72. Verifikasi baris `Riwayat Aset {runId} - 1`, `Riwayat Aset {runId} - 2`, dan `Riwayat Aset {runId} - 6` berstatus `Repaired` tidak tampil
73. Klik `[Clear Field]`
74. Klik `[Apply]`
75. Klik ikon `Filter` untuk menutup Filter Panel

### Sub-tab History tanpa kartu ringkasan
76. Verifikasi sub-tab History tidak menampilkan kartu ringkasan

### Kosong akibat Search tidak memakai teks kosong alami
77. Ganti isi kotak search dengan `Tidak Ada Hasil {runId}`, tekan Enter
78. Verifikasi sub-tab History menampilkan `No results found`
79. Verifikasi teks `No resolved records yet` tidak tampil karena sub-tab History memuat record selesai dan tabel kosong hanya akibat Search
