---
id: TC-FA-ASTL-E2E-001-tabel-all-assets-tampilan
title: "Tabel All Assets menampilkan data aset dengan status dan kolom"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-02a, ASTL-LOGIC-02c, ASTL-LOGIC-12a, EC-01, FLD-01, FLD-02, FLD-03, FLD-04, FLD-05, FLD-06, FLD-07, FLD-08, FLD-09, FLD-10, FLD-11, FLD-12, FLD-13, FLD-14, FLD-15, FLD-16, FLD-17, FLD-18, FLD-19, FLD-20, FLD-21, FLD-22, FLD-23, FLD-24, FLD-25, FLD-26, "§9.4.3#p2", "§4.1#p1", "§4.2.1#p1", "§4.8#p1"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-02a: [26, 28]
  ASTL-LOGIC-02c: [30, 31, 34]
  ASTL-LOGIC-12a: 44
  EC-01: 28
  FLD-01: [9, 10]
  FLD-02: [9, 11]
  FLD-03: [40, 46]
  FLD-04: [9, 12]
  FLD-05: [9, 13, 14]
  FLD-06: [9, 15]
  FLD-07: [9, 16, 17]
  FLD-08: 40
  FLD-09: [9, 18]
  FLD-10: [9, 19]
  FLD-11: [9, 20, 21]
  FLD-12: [9, 22, 23]
  FLD-13: [9, 26, 27]
  FLD-14: [9, 24]
  FLD-15: 40
  FLD-16: 40
  FLD-17: [40, 49]
  FLD-18: 40
  FLD-19: 40
  FLD-20: [40, 60]
  FLD-21: [40, 61]
  FLD-22: 40
  FLD-23: 41
  FLD-24: [9, 25, 50]
  FLD-25: [9, 24, 51]
  FLD-26: 35
  "§9.4.3#p2": [29, 30, 37, 38]
  "§4.1#p1": [3, 4]
  "§4.2.1#p1": [5, 6, 7, 52, 53, 56]
  "§4.8#p1": 3
anchor: []
coverage:
  web: automated
---

# Tabel All Assets menampilkan data aset dengan status dan kolom

## Prerequisites
- Aktor: Total Control `Citra Lestari {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-001-1: User `Citra Lestari {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan.
  - DU-001-2: Aset `Printer Laser - 1 {runId}`: Brand `Epson`, Model / Type `L3250`, Category `Elektronik`, Group `Kantor Pusat {runId}`, Division `Finance {runId}`, TAG `QR` dan `NFC`, Labels `Aset Kantor {runId}`, berstatus `Available`.
  - DU-001-3: Aset `Mouse Wireless - 1 {runId}`: Brand `Logitech`, Model / Type `No Model`, wajib TAG tetapi belum dipasangi TAG, tanpa Division, tanpa Labels, berstatus `Not Paired Yet`.
  - DU-001-4: Aset `Laptop Dinas - 1 {runId}`: berstatus `Borrowed`, Condition `Damaged`, Tagging `TAG Reported`, dan Activity Lock `In Audit`.
  - DU-001-5: Aset `Router Cabang - 1 {runId}`: berstatus `Available` dan berpenanda lisensi `Unmanaged`.
  - DU-001-6: Aset `Switch Cabang - 1 {runId}`: berpenanda lisensi `Pending Activation` sesudah aksi Manage diajukan.
  - DU-001-7: Aset `Kamera Lobi - 1 {runId}`: Condition `Damaged`, tanpa status lain.
  - DU-001-8: Aset `Proyektor Meeting - 1 {runId}` ber-Lifecycle `Draft`.
  - DU-001-9: Aset `Scanner Meeting - 1 {runId}` ber-Lifecycle `Waiting for Approval`.
  - DU-001-10: Custom field aktif `Lokasi Rak {runId}` bertipe teks pada grup General.
  - Dengan Search memakai runId spec ini, tabel memuat aset DU-001-2 sampai DU-001-7 dan tidak memuat DU-001-8 dan DU-001-9.
- Kondisi:
  - Akun `Citra Lestari {runId}` aktif dan kredensialnya tersedia.
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Struktur halaman Assets
1. Masuk sebagai `Citra Lestari {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Verifikasi halaman memuat tab `Assets`, `Registration`, `Damaged`, dan `Missing`
4. Verifikasi tab `Assets` aktif sebagai tampilan awal
5. Verifikasi halaman memuat baris kartu status, toolbar tepat di atas tabel, tabel, Paginator di bawah tabel, dan sidebar Group di sisi kanan
6. Verifikasi Filter Panel terlipat sampai ikon Filter diklik
7. Verifikasi tabel memuat checkbox pemilihan baris di sisi kiri dan kolom `Actions` di sisi kanan

### Kolom bawaan menampilkan data aset
8. Ketik Search `{runId}`, tekan Enter
9. Verifikasi header kolom `Photo`, `Name`, `Asset ID`, `TAG`, `Brand`, `Model / Type`, `Category`, `Group`, `Division`, `Labels`, `Status`, `Register Date`, `Modified By`, dan `Last Updated` tampil
10. Verifikasi sel `Photo` pada baris `Printer Laser - 1 {runId}` menampilkan gambar placeholder generik
11. Verifikasi sel `Name` pada baris `Printer Laser - 1 {runId}` berupa tautan bernama `Printer Laser - 1 {runId}`
12. Verifikasi sel `Asset ID` pada baris `Printer Laser - 1 {runId}` berisi Asset ID milik DU-001-2
13. Verifikasi sel `TAG` pada baris `Printer Laser - 1 {runId}` menampilkan ikon `QR` dan ikon `NFC`
14. Verifikasi sel `TAG` pada baris `Mouse Wireless - 1 {runId}` menampilkan `—`
15. Verifikasi sel `Brand` pada baris `Printer Laser - 1 {runId}` menampilkan `Epson`
16. Verifikasi sel `Model / Type` pada baris `Printer Laser - 1 {runId}` menampilkan `L3250`
17. Verifikasi sel `Model / Type` pada baris `Mouse Wireless - 1 {runId}` menampilkan `No Model` sebagai nilai data biasa
18. Verifikasi sel `Category` pada baris `Printer Laser - 1 {runId}` menampilkan `Elektronik`
19. Verifikasi sel `Group` pada baris `Printer Laser - 1 {runId}` menampilkan `Kantor Pusat {runId}`
20. Verifikasi sel `Division` pada baris `Printer Laser - 1 {runId}` menampilkan `Finance {runId}`
21. Verifikasi sel `Division` pada baris `Mouse Wireless - 1 {runId}` menampilkan `—`
22. Verifikasi sel `Labels` pada baris `Printer Laser - 1 {runId}` menampilkan `Aset Kantor {runId}`
23. Verifikasi sel `Labels` pada baris `Mouse Wireless - 1 {runId}` menampilkan `—`
24. Verifikasi sel `Register Date` dan `Last Updated` pada baris `Printer Laser - 1 {runId}` berisi tanggal menurut Date Format `dd/MM/yy`
25. Verifikasi sel `Modified By` pada baris `Printer Laser - 1 {runId}` berisi nama user dan tidak kosong

### Kolom Status menampilkan badge utama dengan overlay
26. Verifikasi sel `Status` pada baris `Printer Laser - 1 {runId}` menampilkan badge `Available` yang berdiri sendiri
27. Verifikasi sel `Status` pada baris `Mouse Wireless - 1 {runId}` menampilkan badge `Not Paired Yet`
28. Verifikasi sel `Status` pada baris `Laptop Dinas - 1 {runId}` menampilkan badge utama `Borrowed` dengan overlay `Damaged`, `TAG Reported`, dan `In Audit`
29. Verifikasi sel `Status` pada baris `Kamera Lobi - 1 {runId}` menampilkan `Damaged` dan tidak menampilkan `Available` berdampingan
30. Verifikasi sel `Status` pada baris `Router Cabang - 1 {runId}` menampilkan badge `Available` berdampingan dengan badge overlay `Unmanaged`
31. Verifikasi sel `Status` pada baris `Switch Cabang - 1 {runId}` menampilkan badge overlay `Pending Activation`
32. Klik ikon Filter
33. Klik field Status pada Filter Panel
34. Verifikasi opsi Status memuat `Unmanaged` dan `Pending Activation`
35. Verifikasi Filter Panel memuat field `Purchase Status` dengan placeholder `All purchase statuses`
36. Klik ikon Filter

### Aset Draft dan Waiting for Approval tidak tampil
37. Verifikasi tabel tidak memuat `Proyektor Meeting - 1 {runId}` yang ber-Lifecycle `Draft`
38. Verifikasi tabel tidak memuat `Scanner Meeting - 1 {runId}` yang ber-Lifecycle `Waiting for Approval`

### Kolom tambahan tersedia di Setup Column dan Asset Value berurutan
39. Klik header kolom `Actions`
40. Verifikasi panel Column Visibility memuat kolom `Alias Name`, `Measurement`, `Last Scanned`, `Asset Class`, `Tax Depreciation Class`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Purchase Date`, `Purchase Cost`, dan `Warranty Expiry` dalam keadaan tidak tercentang
41. Verifikasi panel Column Visibility memuat kolom custom field `Lokasi Rak {runId}` dalam keadaan tidak tercentang
42. Centang kolom `Asset Value (Commercial)` pada panel Column Visibility
43. Centang kolom `Asset Value (Fiscal)` pada panel Column Visibility
44. Verifikasi header kolom `Asset Value (Commercial)` berada tepat sebelum header kolom `Asset Value (Fiscal)`

### Urutan kolom tambahan dan kolom data terakhir
45. Centang kolom `Alias Name` pada panel Column Visibility
46. Verifikasi header kolom `Alias Name` berada tepat sesudah header kolom `Name`
47. Centang kolom `Asset Class` pada panel Column Visibility
48. Centang kolom `Tax Depreciation Class` pada panel Column Visibility
49. Verifikasi header kolom `Tax Depreciation Class` berada tepat sesudah header kolom `Asset Class`
50. Verifikasi header kolom `Modified By` adalah kolom data kedua dari akhir
51. Verifikasi header kolom `Last Updated` adalah kolom data terakhir sebelum kolom `Actions`

### Judul halaman dan header tabel
52. Verifikasi breadcrumb `Assets > All Assets` tampil
53. Verifikasi halaman tidak memuat heading judul halaman terpisah
54. Klik `(←)` pada kotak Search
55. Gulir tabel ke bawah
56. Verifikasi baris header kolom tetap terlihat di bagian atas tabel

### Purchase Date dan Purchase Cost tampil sebelum Warranty Expiry
57. Centang kolom `Purchase Date` pada panel Column Visibility
58. Centang kolom `Purchase Cost` pada panel Column Visibility
59. Centang kolom `Warranty Expiry` pada panel Column Visibility
60. Verifikasi header kolom `Purchase Date` berada sebelum header kolom `Warranty Expiry`
61. Verifikasi header kolom `Purchase Cost` berada sebelum header kolom `Warranty Expiry`
