---
id: TC-FA-FASVC-BE-073-be-konkurensi-dan-versi
title: "Server: Konflik Versi pada Edit, Inactivate, Activate, Delete; Create Nama Sama Serentak; Delete Bersamaan dengan Rujukan Baru"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-11a", "FASVC-LOGIC-11b", "FASVC-LOGIC-11d", "FASVC-LOGIC-11f", "EC-FASVC-02", "EC-FASVC-03a", "EC-FASVC-03c", "F-FASVC-02.k3", "§9.6#p6", "§9.6#p5", "§9.2#p13", "EB-CON-2", "EB-CON-3", "EB-ERR-3", "EC-FASVC-09", "F-FASVC-04.k3"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-11a": [5, 20, 26, 32, 38]
  "FASVC-LOGIC-11b": [5, 7, 9, 13, 16, 28, 34, 40]
  "FASVC-LOGIC-11d": [44]
  "FASVC-LOGIC-11f": [65]
  "EC-FASVC-02": [65, 67]
  "EC-FASVC-03a": [5]
  "EC-FASVC-03c": [7]
  "F-FASVC-02.k3": [67, 69]
  "§9.6#p6": [13, 15]
  "§9.6#p5": [61, 63, 73, 75]
  "§9.2#p13": [53, 55]
  "EB-CON-2": [65]
  "EB-CON-3": [20, 22, 26, 38, 48]
  "EB-ERR-3": [44, 48, 53]
  "EC-FASVC-09": [53, 55]
  "F-FASVC-04.k3": [53, 55, 57]
anchor: []
---

# Server: Konflik Versi pada Edit, Inactivate, Activate, Delete; Create Nama Sama Serentak; Delete Bersamaan dengan Rujukan Baru

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` dan Total Control `Budi Santoso {runId}` pada client suite.
- Data:
  - DU-073-1: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-073-2: User `Budi Santoso {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-073-3: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-4: Service Center `CV Genset Prima {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@konkurensi073.co.id`, Status `Active`, Notes `Vendor genset resmi`, ada di client suite.
  - DU-073-5: Service Center `Bengkel Maju Motor {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-6: Service Center `Lab Kalibrasi Pratama {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Johor Bahru`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-7: Service Center `UD Cahaya Servis {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Malang`, Company email `kontak@konkurensi073.co.id`, Status `Inactive`, ada di client suite.
  - DU-073-8: Service Center `Servis Elektrik Surabaya {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-9: Service Center `Servis Pendingin Malang {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Malang`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-10: Service Center `Servis Panel Bekasi {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bekasi`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-11: Service Center `Servis Genset Bogor {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Bogor`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-12: Service Center `Mitra Kompresor Medan {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Medan`, Company email `kontak@konkurensi073.co.id`, Status `Active`, ada di client suite.
  - DU-073-27: Asset `Genset Cadangan Bogor {runId}`, Status `Active`, ada di client suite.
  - DU-073-28: Schedule Maintenance Routine `Servis Panel Bulanan {runId}`, Status `Active`, Asset `Genset Cadangan Bogor {runId}`, Service type `Routine`, tanpa pelaksana default, ada di client suite.
  - DU-073-29: User `Yoga Saputra {runId}` dengan Role `Read Only`, dan cakupan Group seluruh pohon Group.
  - Group `Cabang Surabaya {runId}` adalah anak langsung root pohon Group di client suite.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.
  - `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` bekerja bersamaan pada client suite; setiap blok langkah menyebut data yang dibaca keduanya sebelum salah satu mengubahnya.

## Test Steps
### Edit serentak pada field yang sama dengan nilai berbeda: simpan kedua ditolak dan tidak menimpa
1. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `PT Sejuk Abadi Teknik {runId}` dan memegang versi data yang sama
2. `Dewi Anggraini {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Pusat`
3. Baca Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}` dan catat jumlah entrinya sebagai L0
4. `Budi Santoso {runId}` mengirim Edit atas `PT Sejuk Abadi Teknik {runId}` dengan City diganti `Jakarta Barat` dan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
5. Verifikasi permintaan ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`
6. Baca `PT Sejuk Abadi Teknik {runId}` dari daftar dengan pencarian `PT Sejuk Abadi Teknik {runId}`
7. Verifikasi City tersimpan tetap `Jakarta Pusat`, sehingga simpan kedua tidak menimpa
8. Baca ulang Changelog Service Center dengan Service Center Name `PT Sejuk Abadi Teknik {runId}`
9. Verifikasi jumlah entri tetap L0, sehingga permintaan yang ditolak tidak mengubah apa pun

### Edit serentak pada field berbeda tetap konflik dan tidak membatalkan cakupan yang baru diputuskan
10. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `CV Genset Prima {runId}` dan memegang versi data yang sama
11. `Dewi Anggraini {runId}` mengirim Edit atas `CV Genset Prima {runId}` dengan Available to dipersempit menjadi `Cabang Surabaya {runId}`
12. `Budi Santoso {runId}` mengirim Edit atas `CV Genset Prima {runId}` dengan Notes diganti `Vendor genset dan kompresor` dan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
13. Verifikasi permintaan ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`, walau field yang diubah berbeda
14. Baca `CV Genset Prima {runId}` dari daftar dengan pencarian `CV Genset Prima {runId}`
15. Verifikasi Available to tersimpan tetap `Cabang Surabaya {runId}`, sehingga cakupan yang baru diputuskan tidak dibatalkan
16. Verifikasi Notes tersimpan tetap `Vendor genset resmi`

### Inactivate oleh satu admin lalu Edit oleh admin lain ditolak
17. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Bengkel Maju Motor {runId}` dan memegang versi data yang sama
18. `Dewi Anggraini {runId}` mengirim Inactivate atas `Bengkel Maju Motor {runId}`
19. `Budi Santoso {runId}` mengirim Edit atas `Bengkel Maju Motor {runId}` dengan Notes diganti `Bengkel resmi kendaraan` dan versi data yang dibaca sebelum Inactivate `Dewi Anggraini {runId}`
20. Verifikasi permintaan Edit ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`
21. Baca `Bengkel Maju Motor {runId}` dari daftar dengan pencarian `Bengkel Maju Motor {runId}`
22. Verifikasi Status tersimpan `Inactive` dan Notes tidak berisi `Bengkel resmi kendaraan`

### Inactivate dan Activate dengan versi usang ditolak
23. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Lab Kalibrasi Pratama {runId}` dan memegang versi data yang sama
24. `Dewi Anggraini {runId}` mengirim Edit atas `Lab Kalibrasi Pratama {runId}` dengan City diganti `Kuala Lumpur`
25. `Budi Santoso {runId}` mengirim Inactivate atas `Lab Kalibrasi Pratama {runId}` dengan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
26. Verifikasi permintaan Inactivate ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`
27. Baca `Lab Kalibrasi Pratama {runId}` dari daftar dengan pencarian `Lab Kalibrasi Pratama {runId}`
28. Verifikasi Status `Active` tidak berubah, sehingga Inactivate dengan versi usang tidak mengubah apa pun
29. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `UD Cahaya Servis {runId}` dan memegang versi data yang sama
30. `Dewi Anggraini {runId}` mengirim Edit atas `UD Cahaya Servis {runId}` dengan City diganti `Batu`
31. `Budi Santoso {runId}` mengirim Activate atas `UD Cahaya Servis {runId}` dengan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
32. Verifikasi permintaan Activate ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`
33. Baca `UD Cahaya Servis {runId}` dari daftar dengan pencarian `UD Cahaya Servis {runId}`
34. Verifikasi Status `Inactive` tidak berubah, sehingga Activate dengan versi usang tidak mengubah apa pun

### Edit oleh satu admin lalu Delete dengan versi usang oleh admin lain ditolak
35. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Servis Elektrik Surabaya {runId}` dan memegang versi data yang sama
36. `Dewi Anggraini {runId}` mengirim Edit atas `Servis Elektrik Surabaya {runId}` dengan Notes diganti `Vendor elektrik Surabaya`
37. `Budi Santoso {runId}` mengirim Delete atas `Servis Elektrik Surabaya {runId}` dengan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
38. Verifikasi permintaan Delete ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`
39. Baca `Servis Elektrik Surabaya {runId}` dari daftar dengan pencarian `Servis Elektrik Surabaya {runId}`
40. Verifikasi Service Center itu masih ada dengan Notes `Vendor elektrik Surabaya`

### Service Center yang sudah dihapus pengguna lain ditolak sebagai tidak ditemukan
41. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Servis Pendingin Malang {runId}` dan memegang versi data yang sama
42. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Pendingin Malang {runId}`
43. `Budi Santoso {runId}` mengirim Edit atas `Servis Pendingin Malang {runId}` dengan Notes diganti `Vendor pendingin Malang` dan versi data yang dibaca sebelum Delete `Dewi Anggraini {runId}`
44. Verifikasi permintaan Edit ditolak karena data tidak ditemukan, dengan pesan `This service center is no longer available.`
45. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Servis Panel Bekasi {runId}` dan memegang versi data yang sama
46. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Panel Bekasi {runId}`
47. `Budi Santoso {runId}` mengirim Delete atas `Servis Panel Bekasi {runId}` yang sudah dihapus `Dewi Anggraini {runId}`
48. Verifikasi permintaan Delete kedua ditolak karena data tidak ditemukan, dengan pesan `This service center is no longer available.`, tanpa efek tambahan

### Delete dibatalkan bila rujukan baru muncul bersamaan
49. Baca Changelog Service Center dengan Service Center Name `Servis Genset Bogor {runId}` dan catat jumlah entrinya sebagai L1
50. `Dewi Anggraini {runId}` membaca `Servis Genset Bogor {runId}` dengan Usage `0` sebagai dasar Delete
51. `Budi Santoso {runId}` menjadikan `Servis Genset Bogor {runId}` pelaksana default Schedule `Servis Panel Bulanan {runId}`, sehingga Usage-nya menjadi `1`
52. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Genset Bogor {runId}` berdasarkan bacaan saat Usage-nya `0`
53. Verifikasi Delete ditolak server sebagai konflik karena Service Center sudah dipakai
54. Baca `Servis Genset Bogor {runId}` dari daftar dengan pencarian `Servis Genset Bogor {runId}`
55. Verifikasi Service Center itu masih ada dengan Usage `1`, sehingga tidak terhapus
56. Baca ulang Changelog Service Center dengan Service Center Name `Servis Genset Bogor {runId}`
57. Verifikasi jumlah entri tetap L1, sehingga penolakan Delete tidak menulis log

### Urutan evaluasi: No-Op sebelum versi, versi sebelum validasi
58. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` masing-masing membaca `Mitra Kompresor Medan {runId}` dan memegang versi data yang sama
59. `Dewi Anggraini {runId}` mengirim Edit atas `Mitra Kompresor Medan {runId}` dengan City diganti `Binjai`
60. `Budi Santoso {runId}` mengirim Edit atas `Mitra Kompresor Medan {runId}` dengan semua nilai sama dengan nilai tersimpan sekarang, termasuk City `Binjai`, dan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
61. Verifikasi permintaan tidak ditolak sebagai konflik versi, karena Edit tanpa perubahan nilai dinilai No-Op sebelum versi diperiksa
62. `Budi Santoso {runId}` mengirim Edit atas `Mitra Kompresor Medan {runId}` dengan Country diganti `Atlantis` dan versi data yang sama yang usang
63. Verifikasi permintaan ditolak sebagai konflik versi dengan pesan `This service center was changed by someone else. Please review.`, bukan sebagai kesalahan validasi Country

### Create dengan Name sama serentak: satu berhasil dan satu ditolak
64. `Dewi Anggraini {runId}` dan `Budi Santoso {runId}` mengirim Create dengan Name `Sentral Mekanik Nusantara {runId}` bersamaan
65. Verifikasi tepat satu dari kedua permintaan berhasil dan satu lagi ditolak dengan pesan `Name already exists`
66. Baca daftar Service Center client suite dengan pencarian `Sentral Mekanik Nusantara {runId}`
67. Verifikasi hasil memuat tepat satu Service Center bernama `Sentral Mekanik Nusantara {runId}`
68. Baca Changelog Service Center dengan Service Center Name `Sentral Mekanik Nusantara {runId}` dan Action `Created`
69. Verifikasi seluruh entri Changelog Action `Created` memiliki Modified By yang sama, yaitu admin yang permintaannya berhasil

### Urutan evaluasi: hak sebelum versi
70. `Yoga Saputra {runId}` membaca `Mitra Kompresor Medan {runId}` dan memegang versi data itu
71. `Dewi Anggraini {runId}` mengirim Edit atas `Mitra Kompresor Medan {runId}` dengan City diganti `Tebing Tinggi`
72. `Yoga Saputra {runId}` mengirim Edit atas `Mitra Kompresor Medan {runId}` dengan City diganti `Pematang Siantar` dan versi data yang dibaca sebelum Edit `Dewi Anggraini {runId}`
73. Verifikasi permintaan ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`, bukan sebagai konflik versi
74. Baca `Mitra Kompresor Medan {runId}` dari daftar dengan pencarian `Mitra Kompresor Medan {runId}`
75. Verifikasi City tersimpan `Tebing Tinggi`, sehingga Edit yang ditolak tidak mengubah apa pun
