---
id: TC-FA-FASVC-BE-069-be-validasi-cakupan-dan-referensi
title: "Server: Service Type, Available to, Specialization, Brands, dan Referensi Master Tidak Valid"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["V-FASVC-04", "V-FASVC-05", "V-FASVC-13", "V-FASVC-14", "V-FASVC-22", "V-FASVC-26", "V-FASVC-31", "V-FASVC-32", "FLD-FASVC-02", "FLD-FASVC-03", "FLD-FASVC-04", "FLD-FASVC-05", "FASVC-LOGIC-02c", "FASVC-LOGIC-02f", "FASVC-LOGIC-02i", "FASVC-LOGIC-02l", "FASVC-LOGIC-05h", "FASVC-LOGIC-07h", "EC-FASVC-11", "EC-FASVC-37", "EC-FASVC-58c", "F-FASVC-03.k5"]
smoke: []
dependsOn: []
trace:
  "V-FASVC-04": [3, 7]
  "V-FASVC-05": [5, 7]
  "V-FASVC-13": [10, 12, 14, 16]
  "V-FASVC-14": [18, 54]
  "V-FASVC-22": [26]
  "V-FASVC-26": [33, 41]
  "V-FASVC-31": [35, 37]
  "V-FASVC-32": [39]
  "FLD-FASVC-02": [3, 18, 47, 54]
  "FLD-FASVC-03": [39, 49, 51]
  "FLD-FASVC-04": [33, 50, 52]
  "FLD-FASVC-05": [5, 10, 12, 35, 48]
  "FASVC-LOGIC-02c": [3, 47]
  "FASVC-LOGIC-02f": [5, 48]
  "FASVC-LOGIC-02i": [49]
  "FASVC-LOGIC-02l": [50]
  "FASVC-LOGIC-05h": [26, 28]
  "FASVC-LOGIC-07h": [18, 20, 23, 54, 56, 59]
  "EC-FASVC-11": [18, 20, 54]
  "EC-FASVC-37": [26, 28]
  "EC-FASVC-58c": [35, 39, 41, 43]
  "F-FASVC-03.k5": [26, 30]
anchor: []
---

# Server: Service Type, Available to, Specialization, Brands, dan Referensi Master Tidak Valid

## Prerequisites
- Aktor: Total Control pada client suite; `Rina Wulandari {runId}` (DU-069-5) hanya pada langkah yang menyebut namanya.
- Data:
  - DU-069-1: Group `Cabang Surabaya {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-069-2: Group `Cabang Malang {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-069-3: Category `AC {runId}`, ada di client suite.
  - DU-069-4: Brand `Daikin {runId}`, ada di client suite.
  - DU-069-5: User `Rina Wulandari {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-069-6: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `admin@sejukabadi.co.id`, Status `Active`.
  - DU-069-7: Schedule Maintenance Routine `Servis AC Triwulan {runId}` berstatus `Active` dengan pelaksana default `PT Sejuk Abadi Teknik {runId}`.
  - DU-069-8: Service Center `UD Cahaya Servis {runId}`, Service type `Repair`, Available to kosong, Country `Indonesia`, City `Malang`, Company email `cahaya@udservis.co.id`, Status `Inactive`.
  - DU-069-9: Service Center `Servis Elektrik Surabaya {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `elektrik@servissby.co.id`, Status `Active`.
  - DU-069-23: Service Center `CV Mitra Pendingin Servis {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `servis@mitrapendingin.co.id`, Status `Active`.
  - DU-069-24: Schedule Maintenance Routine `Servis Chiller Bulanan {runId}` berstatus `Paused` dengan pelaksana default `CV Mitra Pendingin Servis {runId}`.
  - DU-069-25: Task Maintenance Routine `Inspeksi Chiller Gedung B {runId}` berstatus `In Progress` dari Schedule `Servis Chiller Bulanan {runId}`, dengan pelaksana `CV Mitra Pendingin Servis {runId}`.
  - DU-069-26: Service Center `Teknik Dingin Sentosa {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Country `Indonesia`, City `Semarang`, Company email `layanan@teknikdingin.co.id`, Status `Active`.
  - DU-069-27: Schedule Maintenance Routine `Servis Kompresor Bulanan {runId}` berstatus `Paused` dengan pelaksana default `Teknik Dingin Sentosa {runId}`.
  - DU-069-28: Task Maintenance Routine `Servis Kompresor Maret {runId}` berstatus `Completed` dari Schedule `Servis Kompresor Bulanan {runId}`, dengan pelaksana `Teknik Dingin Sentosa {runId}`.
  - Setiap Create yang dikirim memuat field wajib lain bernilai Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `layanan@mitrapendingin.co.id`, kecuali yang disebut di langkah; Name dikirim sesuai langkah.
  - Setiap Edit dan Activate yang dikirim memuat versi data terkini dan nilai tersimpan untuk semua field selain yang disebut di langkah.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.
  - `Cabang Bekasi {runId}` sudah dihapus dari master Group, `Generator {runId}` sudah dihapus dari master Category, dan `LG {runId}` sudah dihapus dari master Brand, sehingga ketiganya tidak ada di master.
  - `Cabang Cirebon {runId}` ada di master Group dengan status `Inactive`.

## Test Steps
### Service type dan Available to kosong ditolak
1. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
2. Kirim Create dengan Name `Mitra Teknik Barokah {runId}` tanpa satu pun Service type
3. Verifikasi permintaan ditolak dengan pesan `Select at least one service type`
4. Kirim Create dengan Name `Karya Servis Lestari {runId}` dan Available to dikosongkan
5. Verifikasi permintaan ditolak dengan pesan `Select at least one group`
6. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
7. Verifikasi jumlah baris tetap N0, sehingga permintaan tanpa Service type dan tanpa Available to tidak membuat Service Center

### Available to di luar cakupan pembuat ditolak
8. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N1
9. `Rina Wulandari {runId}` mengirim Create dengan Name `Servis Elektrik Malang {runId}` dan Available to `Cabang Malang {runId}`
10. Verifikasi permintaan ditolak dengan pesan `You don't have access to some groups.`
11. `Rina Wulandari {runId}` mengirim Edit atas `Servis Elektrik Surabaya {runId}` dengan Available to menjadi `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`
12. Verifikasi permintaan ditolak dengan pesan `You don't have access to some groups.`
13. Baca `Servis Elektrik Surabaya {runId}` sebagai Total Control dari daftar dengan pencarian `Servis Elektrik Surabaya {runId}`
14. Verifikasi Available to tersimpan tetap hanya `Cabang Surabaya {runId}`
15. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
16. Verifikasi jumlah baris tetap N1, sehingga Create di luar cakupan tidak membuat Service Center

### Service type yang dipakai Schedule aktif tidak bisa dilepas
17. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Service type hanya `Repair`, sehingga `Routine` yang dipakai Schedule `Servis AC Triwulan {runId}` dilepas
18. Verifikasi permintaan ditolak dengan pesan `Routine is used by active schedules or open tasks.`
19. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
20. Verifikasi Service type tersimpan tetap `Routine` dan `Repair`
21. Kirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan Service type hanya `Routine`, sehingga `Repair` yang tidak dipakai dilepas
22. Baca ulang `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
23. Verifikasi Service type tersimpan `Routine`, karena hanya type yang dipakai yang tidak bisa dilepas

### Activate tanpa Available to ditolak
24. Baca Changelog Service Center dengan Service Center Name `UD Cahaya Servis {runId}` dan catat jumlah entrinya sebagai L0
25. Kirim Activate atas `UD Cahaya Servis {runId}` yang berstatus `Inactive` dan Available to-nya kosong
26. Verifikasi permintaan ditolak dengan pesan `Add at least one group before activating.`
27. Baca `UD Cahaya Servis {runId}` dari daftar dengan pencarian `UD Cahaya Servis {runId}`
28. Verifikasi Status tersimpan tetap `Inactive`
29. Baca ulang Changelog Service Center dengan Service Center Name `UD Cahaya Servis {runId}`
30. Verifikasi jumlah entri Changelog `UD Cahaya Servis {runId}` tetap L0, sehingga Activate yang ditolak tidak menulis log

### Referensi Group, Category, dan Brand yang tidak valid ditolak
31. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N2
32. Kirim Create dengan Name `Tiga Mitra Pendingin {runId}` dan Brands `Daikin {runId}` dipilih dua kali
33. Verifikasi permintaan ditolak dengan pesan `Select a valid brand`
34. Kirim Create dengan Name `Kencana Teknik Bekasi {runId}` dan Available to `Cabang Bekasi {runId}`
35. Verifikasi permintaan ditolak dengan pesan `Select a valid group`
36. Kirim Create dengan Name `Pantai Utara Teknik {runId}` dan Available to `Cabang Cirebon {runId}`
37. Verifikasi permintaan ditolak dengan pesan `Select a valid group`, karena node yang Inactive di master tidak dapat dipilih baru
38. Kirim Create dengan Name `Mulia Genset Servis {runId}` dan Specialization `Generator {runId}`
39. Verifikasi permintaan ditolak dengan pesan `Select a valid category`
40. Kirim Create dengan Name `Sentosa Elektronik Servis {runId}` dan Brands `LG {runId}`
41. Verifikasi permintaan ditolak dengan pesan `Select a valid brand`
42. Baca ulang daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
43. Verifikasi jumlah baris tetap N2, sehingga kelima permintaan tidak membuat Service Center

### Satu Service type, Specialization dan Brands kosong, serta referensi valid diterima
44. Kirim Create dengan Name `Bengkel Maju Motor {runId}`, Service type hanya `Repair`, Available to `Cabang Surabaya {runId}`, tanpa Specialization, dan tanpa Brands
45. Kirim Create dengan Name `Lab Kalibrasi Pratama {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization `AC {runId}`, dan Brands `Daikin {runId}`
46. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
47. Verifikasi `Bengkel Maju Motor {runId}` tersimpan dengan Service type hanya `Repair`
48. Verifikasi `Bengkel Maju Motor {runId}` tersimpan dengan Available to `Cabang Surabaya {runId}`
49. Verifikasi `Bengkel Maju Motor {runId}` tersimpan dengan Specialization kosong
50. Verifikasi `Bengkel Maju Motor {runId}` tersimpan dengan Brands kosong
51. Verifikasi `Lab Kalibrasi Pratama {runId}` tersimpan dengan Specialization `AC {runId}`
52. Verifikasi `Lab Kalibrasi Pratama {runId}` tersimpan dengan Brands `Daikin {runId}`

### Service type yang hanya dipakai Task terbuka tidak bisa dilepas
53. Kirim Edit atas `CV Mitra Pendingin Servis {runId}` dengan Service type hanya `Repair`, sehingga `Routine` yang hanya dipakai Task terbuka `Inspeksi Chiller Gedung B {runId}` dilepas
54. Verifikasi permintaan ditolak dengan pesan `Routine is used by active schedules or open tasks.`
55. Baca `CV Mitra Pendingin Servis {runId}` dari daftar dengan pencarian `CV Mitra Pendingin Servis {runId}`
56. Verifikasi Service type tersimpan tetap `Routine` dan `Repair`

### Service type yang hanya dipakai Schedule Paused dan Task Completed bisa dilepas
57. Kirim Edit atas `Teknik Dingin Sentosa {runId}` dengan Service type hanya `Repair`, sehingga `Routine` yang hanya dipakai Schedule `Paused` dan Task `Completed` dilepas
58. Baca `Teknik Dingin Sentosa {runId}` dari daftar dengan pencarian `Teknik Dingin Sentosa {runId}`
59. Verifikasi Service type tersimpan hanya `Repair`, karena Schedule `Paused` dan Task `Completed` bukan Schedule aktif atau Task terbuka
