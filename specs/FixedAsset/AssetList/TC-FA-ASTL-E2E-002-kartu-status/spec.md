---
id: TC-FA-ASTL-E2E-002-kartu-status
title: "Kartu status menghitung dan menyaring aset"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-13a, ASTL-LOGIC-13b, ASTL-LOGIC-13c, ASTL-LOGIC-13e, ASTL-LOGIC-13f, ASTL-LOGIC-13g, EC-12, F-ASTL-02, KartuAll, KartuAvailable, KartuDisposed, KartuInTransaction, KartuIssues, "§4.1a#p2", "§4.1a#r1", "§4.1a#r3", "§4.1a#r4", "§4.1a#r2", "§4.1a#r5", "§4.1a#b1", "§4.1a#b4", "§4.4#b7", "§9.2#p2"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-13a: [3, 24, 25, 45, 46]
  ASTL-LOGIC-13b: 2
  ASTL-LOGIC-13c: 12
  ASTL-LOGIC-13e: [31, 32]
  ASTL-LOGIC-13f: [33, 34]
  ASTL-LOGIC-13g: 26
  EC-12: 36
  F-ASTL-02: 3
  KartuAll: 3
  KartuAvailable: [17, 49, 48]
  KartuDisposed: [6, 22]
  KartuInTransaction: [4, 9, 51, 52]
  KartuIssues: [5, 14, 54, 55, 56, 57, 58]
  "§4.1a#p2": 2
  "§4.1a#r1": [3, 24, 25]
  "§4.1a#r3": [4, 9, 51, 52]
  "§4.1a#r4": [5, 14, 54, 55, 56, 57, 58]
  "§4.1a#r2": [17, 18, 19, 49]
  "§4.1a#r5": [6, 22]
  "§4.1a#b1": 15
  "§4.1a#b4": [7, 41, 42]
  "§4.4#b7": [10, 11, 63, 64, 61]
  "§9.2#p2": 20
anchor: []
coverage:
  web: automated
---

# Kartu status menghitung dan menyaring aset

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-002-1: Aset `Kursi Kantor - 1 {runId}`, Lifecycle `Active`, tanpa status lain, berstatus `Available`.
  - DU-002-2: Aset `Laptop Pinjaman - 1 {runId}`, Lifecycle `Active`, Custody `Borrowed`.
  - DU-002-3: Aset `Monitor Dell - 1 {runId}`, Lifecycle `Active`, Custody `Assigned`.
  - DU-002-4: Aset `Printer Tua - 1 {runId}`, Lifecycle `Active`, Condition `In Disposal Process`.
  - DU-002-5: Aset `Kamera CCTV - 1 {runId}`, Lifecycle `Active`, Condition `Damaged`.
  - DU-002-6: Aset `Scanner Gudang - 1 {runId}`, Lifecycle `Active`, Tagging `Not Paired Yet`.
  - DU-002-7: Aset `Tablet Survei - 1 {runId}`, Lifecycle `Active`, Custody `Borrowed`, Condition `Damaged`.
  - DU-002-8: Aset `Router Kantor - 1 {runId}`, Lifecycle `Active`, berpenanda lisensi `Unmanaged`.
  - DU-002-9: Aset `Meja Lama - 1 {runId}`, Lifecycle `Disposed`.
  - DU-002-10: Aset `Genset Cadangan - 1 {runId}`, Lifecycle `Active`, Activity Lock `In Audit`.
  - DU-002-11: Aset `Pompa Air - 1 {runId}`, Lifecycle `Active`, Condition `Reported Disposal`.
  - DU-002-12: Aset `Dispenser - 1 {runId}`, Lifecycle `Active`, berpenanda lisensi `Pending Activation`.
  - DU-002-13: Aset `Meja Rapat - 1 {runId}`, Lifecycle `Draft`.
  - DU-002-14: Aset `Lemari Arsip - 1 {runId}`, Lifecycle `Waiting for Approval`.
  - DU-002-15: Aset `Kursi Lipat - 1 {runId}`, Lifecycle `Deleted`.
  - DU-002-16: Aset `Proyektor Kelas - 1 {runId}`, Lifecycle `Active`, Custody `In Borrow Process`.
  - DU-002-17: Aset `Laptop Magang - 1 {runId}`, Lifecycle `Active`, Custody `In Assignment Process`.
  - DU-002-18: Aset `Genset Servis - 1 {runId}`, Lifecycle `Active`, Condition `In Repair`.
  - DU-002-19: Aset `Drone Survei - 1 {runId}`, Lifecycle `Active`, Condition `In Tracking`.
  - DU-002-20: Aset `Mesin Fotokopi Rusak - 1 {runId}`, Lifecycle `Active`, Condition `Permanently Damaged`.
  - DU-002-21: Aset `Ponsel Hilang - 1 {runId}`, Lifecycle `Active`, Condition `Permanently Missing`.
  - Dengan Search `{runId}`, jumlah kartu yang diharapkan dihitung dari data di atas: `All` `17` (DU-002-1 sampai DU-002-8, DU-002-10 bersama DU-002-11, DU-002-12, dan DU-002-16 sampai DU-002-21; DU-002-9 `Disposed` serta DU-002-13 sampai DU-002-15 tidak dihitung), `In Transaction` `6` (DU-002-2, DU-002-3, DU-002-4, DU-002-7, DU-002-16, DU-002-17), `Issues` `8` (DU-002-5, DU-002-6, DU-002-7, DU-002-11, DU-002-18 sampai DU-002-21), dan `Disposed` `1` (DU-002-9).

## Test Steps

### Isi dan angka kartu mengikuti himpunan aset
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris kartu status tampil di antara tab dan toolbar, dengan setiap kartu memuat judul dan jumlah aset
3. Verifikasi kartu `All` berjumlah `17`
4. Verifikasi kartu `In Transaction` berjumlah `6`
5. Verifikasi kartu `Issues` berjumlah `8`
6. Verifikasi kartu `Disposed` berjumlah `1`
7. Verifikasi kartu `In Audit` dan kartu `Under Maintenance` tidak ada

### Kartu menyaring tabel dan dapat dihitung lintas kartu
8. Klik kartu `In Transaction`
9. Verifikasi tabel memuat `Laptop Pinjaman - 1 {runId}`, `Monitor Dell - 1 {runId}`, `Printer Tua - 1 {runId}`, dan `Tablet Survei - 1 {runId}`
10. Verifikasi tombol halaman `1` aktif
11. Verifikasi kartu `In Transaction` menjadi kartu aktif
12. Verifikasi tab `Assets` tetap aktif dan kolom `Status` tetap menampilkan badge status pada baris yang tampil
13. Klik kartu `Issues`
14. Verifikasi tabel memuat `Kamera CCTV - 1 {runId}`, `Scanner Gudang - 1 {runId}`, dan `Tablet Survei - 1 {runId}`
15. Verifikasi `Tablet Survei - 1 {runId}` dihitung di kartu `In Transaction` dan kartu `Issues` sekaligus
16. Klik kartu `Available`
17. Verifikasi tabel memuat `Kursi Kantor - 1 {runId}`
18. Verifikasi tabel tidak memuat `Router Kantor - 1 {runId}` yang berpenanda `Unmanaged`
19. Verifikasi tabel tidak memuat `Laptop Pinjaman - 1 {runId}` yang berstatus `Borrowed`
20. Verifikasi angka pada kartu `Available` sama dengan total pada laporan halaman tabel
21. Klik kartu `Disposed`
22. Verifikasi tabel memuat `Meja Lama - 1 {runId}`
23. Klik kartu `All`
24. Verifikasi tabel memuat `Printer Tua - 1 {runId}` yang berstatus `In Disposal Process` dan `Router Kantor - 1 {runId}` yang berpenanda `Unmanaged`
25. Verifikasi tabel tidak memuat `Meja Lama - 1 {runId}` yang berstatus `Disposed`
26. Verifikasi isi tiap kartu hanya ditetapkan oleh definisi kartu status dan tidak ada kartu selain `All`, `Available`, `In Transaction`, `Issues`, dan `Disposed`

### Kartu aktif dan filter lain berlaku bersamaan, dan angka kartu mengikuti saringan
27. Klik kartu `In Transaction`
28. Klik ikon Filter
29. Pilih Status `Damaged` pada Filter Panel
30. Klik `[Apply]`
31. Verifikasi tabel memuat `Tablet Survei - 1 {runId}`
32. Verifikasi tabel tidak memuat `Laptop Pinjaman - 1 {runId}` dan `Kamera CCTV - 1 {runId}`
33. Verifikasi kartu `All` berjumlah `2`, kartu `In Transaction` berjumlah `1`, dan kartu `Issues` berjumlah `2`
34. Verifikasi kartu `Disposed` berjumlah `0`
35. Klik kartu `Disposed`
36. Verifikasi tabel menampilkan empty state `No results found` dan kartu status tetap tampil

### Opsi Status memuat Activity Lock yang tidak punya kartu
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Klik kartu `All`
40. Klik field Status pada Filter Panel
41. Verifikasi opsi Status memuat `In Audit`

### Opsi Status memuat Under Maintenance
42. Verifikasi opsi Status memuat `Under Maintenance`
43. Klik ikon Filter

### Himpunan kartu All dan Available mengecualikan aset di luar himpunan Active
44. Klik kartu `All`
45. Verifikasi tabel memuat `Pompa Air - 1 {runId}` yang ber-Condition `Reported Disposal` dan `Dispenser - 1 {runId}` yang berpenanda `Pending Activation`
46. Verifikasi tabel tidak memuat `Meja Rapat - 1 {runId}` yang ber-Lifecycle `Draft`, `Lemari Arsip - 1 {runId}` yang ber-Lifecycle `Waiting for Approval`, dan `Kursi Lipat - 1 {runId}` yang ber-Lifecycle `Deleted`
47. Klik kartu `Available`
48. Verifikasi tabel memuat `Kursi Kantor - 1 {runId}`
49. Verifikasi tabel tidak memuat `Dispenser - 1 {runId}` yang berpenanda `Pending Activation`

### Kartu In Transaction dan Issues memuat setiap nilai Custody dan Condition
50. Klik kartu `In Transaction`
51. Verifikasi tabel memuat `Proyektor Kelas - 1 {runId}` yang ber-Custody `In Borrow Process`
52. Verifikasi tabel memuat `Laptop Magang - 1 {runId}` yang ber-Custody `In Assignment Process`
53. Klik kartu `Issues`
54. Verifikasi tabel memuat `Genset Servis - 1 {runId}` yang ber-Condition `In Repair`
55. Verifikasi tabel memuat `Drone Survei - 1 {runId}` yang ber-Condition `In Tracking`
56. Verifikasi tabel memuat `Mesin Fotokopi Rusak - 1 {runId}` yang ber-Condition `Permanently Damaged`
57. Verifikasi tabel memuat `Ponsel Hilang - 1 {runId}` yang ber-Condition `Permanently Missing`
58. Verifikasi tabel memuat `Pompa Air - 1 {runId}` yang ber-Condition `Reported Disposal`

### Klik kartu memuat ulang tabel dari halaman 1
59. Klik kartu `All`
60. Klik tombol halaman `2`
61. Verifikasi laporan halaman menampilkan `Showing 11 to 17 of 17`
62. Klik kartu `Issues`
63. Verifikasi tombol halaman `1` aktif
64. Verifikasi laporan halaman menampilkan `Showing 1 to 8 of 8`
