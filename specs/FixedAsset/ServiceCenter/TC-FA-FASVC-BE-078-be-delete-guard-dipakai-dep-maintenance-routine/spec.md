---
id: TC-FA-FASVC-BE-078-be-delete-guard-dipakai-dep-maintenance-routine
title: "Server: Delete Ditolak Bila Dipakai; Rujukan Tidak Cocok Ditolak"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-06a", "FASVC-LOGIC-06e", "FASVC-LOGIC-04m", "V-FASVC-15", "V-FASVC-17", "EC-FASVC-47", "F-FASVC-05.k6", "§Aturan Logika Modul#p3"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  "FASVC-LOGIC-06a": [2, 4, 6, 8, 10, 12, 15, 18, 21, 49, 51, 53, 55, 57, 59]
  "FASVC-LOGIC-06e": [4, 10]
  "FASVC-LOGIC-04m": [24, 26, 28, 30, 32, 37, 76, 78]
  "V-FASVC-15": [4, 10]
  "V-FASVC-17": [24, 26, 28, 30, 32, 34, 40, 47, 76, 78]
  "EC-FASVC-47": [24, 26, 28, 30, 32]
  "F-FASVC-05.k6": [24, 34, 64, 66, 68, 70]
  "§Aturan Logika Modul#p3": [40, 42, 45, 47, 72, 74, 76, 78]
anchor: []
---

# Server: Delete Ditolak Bila Dipakai; Rujukan Tidak Cocok Ditolak

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` pada client suite.
- Data:
  - DU-078-1: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group.
  - DU-078-2: Group `Cabang Surabaya {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-078-3: Group `Cabang Malang {runId}`, anak langsung root pohon Group, ada di client suite.
  - DU-078-4: Category `AC {runId}`, ada di client suite.
  - DU-078-5: Category `Genset {runId}`, ada di client suite.
  - DU-078-6: Brand `Daikin {runId}`, ada di client suite.
  - DU-078-7: Brand `LG {runId}`, ada di client suite.
  - DU-078-8: Asset `Chiller Lantai 2 {runId}`, Group `Cabang Surabaya {runId}`, Category `AC {runId}`, Brand `Daikin {runId}`, ada di client suite.
  - DU-078-9: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Specialization `AC {runId}`, Brands `Daikin {runId}`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-10: Service Center `CV Genset Prima {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `Cabang Malang {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-11: Service Center `Bengkel Maju Motor {runId}`, Service type `Repair`, Specialization kosong, Brands kosong, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-12: Service Center `UD Cahaya Servis {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Inactive`, tanpa rujukan.
  - DU-078-13: Service Center `Lab Kalibrasi Pratama {runId}`, Service type `Routine`, Specialization `Genset {runId}`, Brands kosong, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-14: Service Center `Servis Merek Lain {runId}`, Service type `Routine`, Specialization kosong, Brands `LG {runId}`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-15: Service Center `Servis Terpakai Schedule {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai sebagai pelaksana default Schedule `Servis AC Triwulan {runId}` yang berstatus `Active`.
  - DU-078-16: Service Center `Servis Terpakai Task {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai sebagai pelaksana Task `Task Servis AC Selesai {runId}` yang berstatus `Completed`.
  - DU-078-17: Service Center `Servis Cakra Mandiri {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-18: Service Center `Servis Rujukan Dilepas {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai sebagai pelaksana default Schedule `Servis Panel Bulanan {runId}`.
  - DU-078-19: Service Center `Servis Pengganti {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, tanpa rujukan.
  - DU-078-20: Service Center `Servis Cakupan Berubah {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `Cabang Surabaya {runId} dan Cabang Malang {runId}`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai sebagai pelaksana default Schedule `Servis Pompa Bulanan {runId}` untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-21: Schedule Maintenance Routine `Servis AC Triwulan {runId}`, status `Active`, pelaksana default `Servis Terpakai Schedule {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-22: Task Maintenance Routine `Task Servis AC Selesai {runId}`, status `Completed`, pelaksana `Servis Terpakai Task {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-23: Schedule Maintenance Routine `Servis Panel Bulanan {runId}`, status `Active`, pelaksana default `Servis Rujukan Dilepas {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-24: Schedule Maintenance Routine `Servis Pompa Bulanan {runId}`, status `Active`, pelaksana default `Servis Cakupan Berubah {runId}`, untuk Asset `Chiller Lantai 2 {runId}`, Notes `Servis pompa bulanan`.
  - DU-078-34: Service Center `Servis Terpakai Task Batal {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai hanya sebagai pelaksana Task `Task Servis AC Batal {runId}` yang berstatus `Canceled`.
  - DU-078-35: Task Maintenance Routine `Task Servis AC Batal {runId}`, status `Canceled`, pelaksana `Servis Terpakai Task Batal {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-36: Service Center `Servis Sumber Biaya Task {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai hanya sebagai sumber biaya Task `Task Servis AC Biaya {runId}`.
  - DU-078-45: Service Center `Servis Pelaksana Biaya {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai hanya sebagai pelaksana Task `Task Servis AC Biaya {runId}`.
  - DU-078-37: Task Maintenance Routine `Task Servis AC Biaya {runId}`, status `Completed`, pelaksana `Servis Pelaksana Biaya {runId}`, sumber biaya `Servis Sumber Biaya Task {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-38: Service Center `Servis Terpakai Schedule Jeda {runId}`, Service type `Routine`, Specialization kosong, Brands kosong, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `kontak@pakai078.co.id`, Status `Active`, dipakai hanya sebagai pelaksana default Schedule `Servis Kalibrasi Jeda {runId}` yang berstatus `Paused`.
  - DU-078-39: Schedule Maintenance Routine `Servis Kalibrasi Jeda {runId}`, status `Paused`, pelaksana default `Servis Terpakai Schedule Jeda {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
  - DU-078-41: Task Maintenance Routine `Task Pompa Berjalan {runId}`, status `In Progress`, pelaksana `Servis Cakupan Berubah {runId}`, untuk Asset `Chiller Lantai 2 {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite.
## Test Steps
### Delete ditolak bila Service Center dipakai Schedule atau Task, apa pun statusnya
1. Baca daftar Service Center client suite dengan pencarian `Servis Terpakai Schedule {runId}`
2. Verifikasi kolom Usage Service Center itu `1`
3. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Terpakai Schedule {runId}`
4. Verifikasi permintaan ditolak dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.`
5. Baca ulang daftar Service Center client suite dengan pencarian `Servis Terpakai Schedule {runId}`
6. Verifikasi `Servis Terpakai Schedule {runId}` tetap ada dan Usage-nya tetap `1`
7. Baca daftar Service Center client suite dengan pencarian `Servis Terpakai Task {runId}`
8. Verifikasi kolom Usage Service Center itu `1`, walau Task yang merujuknya sudah `Completed`
9. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Terpakai Task {runId}`
10. Verifikasi permintaan ditolak dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.`, karena Task yang sudah selesai tetap dihitung selama rujukannya masih ada
11. Baca ulang daftar Service Center client suite dengan pencarian `Servis Terpakai Task {runId}`
12. Verifikasi `Servis Terpakai Task {runId}` tetap ada dan Usage-nya tetap `1`

### Delete diterima bila Usage 0, termasuk setelah rujukan dilepas
13. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Cakra Mandiri {runId}` yang Usage-nya `0`
14. Baca daftar Service Center client suite dengan pencarian `Servis Cakra Mandiri {runId}`
15. Verifikasi hasil pencarian kosong, sehingga Service Center tanpa rujukan terhapus
16. `Dewi Anggraini {runId}` mengganti pelaksana default Schedule `Servis Panel Bulanan {runId}` dari `Servis Rujukan Dilepas {runId}` menjadi `Servis Pengganti {runId}`
17. Baca daftar Service Center client suite dengan pencarian `Servis Rujukan Dilepas {runId}`
18. Verifikasi kolom Usage Service Center itu `0`, karena rujukan yang sudah dilepas tidak dihitung
19. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Rujukan Dilepas {runId}`
20. Baca ulang daftar Service Center client suite dengan pencarian `Servis Rujukan Dilepas {runId}`
21. Verifikasi hasil pencarian kosong, sehingga Service Center yang rujukannya sudah dilepas terhapus

### Rujukan ke Service Center yang tidak memenuhi syarat ditolak server
22. Baca daftar Schedule Maintenance Routine dengan pencarian `{runId}` dan catat jumlah barisnya sebagai N0
23. Simpan Schedule `Servis Uji Tolak Group {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `CV Genset Prima {runId}` lewat permintaan langsung
24. Verifikasi permintaan ditolak dengan pesan `CV Genset Prima {runId} doesn't cover this asset.`
25. Simpan Schedule `Servis Uji Tolak Type {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `Bengkel Maju Motor {runId}` lewat permintaan langsung
26. Verifikasi permintaan ditolak dengan pesan `Bengkel Maju Motor {runId} doesn't cover this asset.`
27. Simpan Schedule `Servis Uji Tolak Inactive {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `UD Cahaya Servis {runId}` lewat permintaan langsung
28. Verifikasi permintaan ditolak dengan pesan `UD Cahaya Servis {runId} doesn't cover this asset.`
29. Simpan Schedule `Servis Uji Tolak Kategori {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `Lab Kalibrasi Pratama {runId}` lewat permintaan langsung
30. Verifikasi permintaan ditolak dengan pesan `Lab Kalibrasi Pratama {runId} doesn't cover this asset.`
31. Simpan Schedule `Servis Uji Tolak Merek {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `Servis Merek Lain {runId}` lewat permintaan langsung
32. Verifikasi permintaan ditolak dengan pesan `Servis Merek Lain {runId} doesn't cover this asset.`
33. Baca ulang daftar Schedule Maintenance Routine dengan pencarian `{runId}`
34. Verifikasi jumlah baris tetap N0, sehingga kelima permintaan tidak membuat Schedule dan tidak menulis log
35. Simpan Schedule `Servis Chiller Baru {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `PT Sejuk Abadi Teknik {runId}` lewat permintaan langsung
36. Baca daftar Service Center client suite dengan pencarian `PT Sejuk Abadi Teknik {runId}`
37. Verifikasi kolom Usage Service Center itu `1`, sehingga rujukan ke Service Center yang memenuhi semua syarat diterima

### Menyimpan perubahan lain pada Schedule yang pelaksananya tidak lagi cocok tidak ditolak
38. `Dewi Anggraini {runId}` mengedit Service Center `Servis Cakupan Berubah {runId}` dengan Available to dipersempit menjadi `Cabang Malang {runId}`, sehingga tidak lagi mencakup lokasi Asset `Chiller Lantai 2 {runId}`
39. Simpan Edit Schedule `Servis Pompa Bulanan {runId}` dengan Notes diganti `Servis pompa bulanan dan inspeksi` dan pelaksana default tetap `Servis Cakupan Berubah {runId}` lewat permintaan langsung
40. Verifikasi permintaan tidak ditolak, karena hanya penggantian pelaksana yang diuji syarat pemilih
41. Baca Schedule `Servis Pompa Bulanan {runId}` dari daftar Schedule dengan pencarian `Servis Pompa Bulanan {runId}`
42. Verifikasi Notes tersimpan `Servis pompa bulanan dan inspeksi` dan pelaksana default tersimpan tetap `Servis Cakupan Berubah {runId}`
43. `Dewi Anggraini {runId}` mengirim Inactivate atas `Servis Cakupan Berubah {runId}`
44. Simpan Edit Schedule `Servis Pompa Bulanan {runId}` dengan Notes diganti `Servis pompa bulanan, kontrak diperpanjang` dan pelaksana default tetap `Servis Cakupan Berubah {runId}` lewat permintaan langsung
45. Verifikasi permintaan tidak ditolak, walau pelaksana default kini `Inactive` dan tidak mencakup lokasi aset
46. Simpan Edit Schedule `Servis Pompa Bulanan {runId}` dengan pelaksana default diganti `CV Genset Prima {runId}` lewat permintaan langsung
47. Verifikasi permintaan ditolak dengan pesan `CV Genset Prima {runId} doesn't cover this asset.`, karena nilai pelaksana diganti dengan Service Center yang tidak cocok

### Delete ditolak untuk Service Center yang hanya dirujuk Task Canceled, sumber biaya Task, atau Schedule Paused
48. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Terpakai Task Batal {runId}`
49. Verifikasi permintaan ditolak dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.`, karena rujukan Task `Canceled` tetap dihitung apa pun statusnya
50. Baca daftar Service Center client suite dengan pencarian `Servis Terpakai Task Batal {runId}`
51. Verifikasi `Servis Terpakai Task Batal {runId}` tetap ada dan Usage-nya `1`
52. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Sumber Biaya Task {runId}`
53. Verifikasi permintaan ditolak dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.`, karena rujukan sumber biaya Task tetap dihitung apa pun statusnya
54. Baca daftar Service Center client suite dengan pencarian `Servis Sumber Biaya Task {runId}`
55. Verifikasi `Servis Sumber Biaya Task {runId}` tetap ada dan Usage-nya `1`
56. `Dewi Anggraini {runId}` mengirim Delete atas `Servis Terpakai Schedule Jeda {runId}`
57. Verifikasi permintaan ditolak dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.`, karena rujukan Schedule `Paused` tetap dihitung apa pun statusnya
58. Baca daftar Service Center client suite dengan pencarian `Servis Terpakai Schedule Jeda {runId}`
59. Verifikasi `Servis Terpakai Schedule Jeda {runId}` tetap ada dan Usage-nya `1`

### Rujukan yang ditolak tidak menulis log
60. Baca Changelog Service Center dengan Service Center Name `CV Genset Prima {runId}` dan catat jumlah entrinya sebagai L0
61. Baca Activity Log dengan Object `Service Center` dan Name `CV Genset Prima {runId}` dan catat jumlah entrinya sebagai A0
62. Baca Activity Log dengan Name `Servis Uji Tolak Log {runId}` dan catat jumlah entrinya sebagai A1
63. Simpan Schedule `Servis Uji Tolak Log {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana default `CV Genset Prima {runId}` lewat permintaan langsung
64. Verifikasi permintaan ditolak dengan pesan `CV Genset Prima {runId} doesn't cover this asset.`
65. Baca ulang Changelog Service Center dengan Service Center Name `CV Genset Prima {runId}`
66. Verifikasi jumlah entri Changelog tetap L0, sehingga penolakan tidak menulis Changelog
67. Baca ulang Activity Log dengan Object `Service Center` dan Name `CV Genset Prima {runId}`
68. Verifikasi jumlah entri Activity Log tetap A0, sehingga penolakan tidak menulis Activity Log
69. Baca ulang Activity Log dengan Name `Servis Uji Tolak Log {runId}`
70. Verifikasi jumlah entri Activity Log tetap A1, sehingga penolakan tidak menulis log Schedule

### Cabang Task: rujukan diuji hanya saat dibuat atau diganti, dan perubahan lain tidak ditolak
71. Simpan Edit Task `Task Pompa Berjalan {runId}` dengan Notes diganti `Pompa diperiksa bulanan` dan pelaksana tetap `Servis Cakupan Berubah {runId}` lewat permintaan langsung
72. Verifikasi permintaan tidak ditolak, walau pelaksana kini `Inactive` dan tidak mencakup lokasi aset, karena hanya penggantian pelaksana yang diuji syarat pemilih
73. Baca Task `Task Pompa Berjalan {runId}` dari daftar Task dengan pencarian `Task Pompa Berjalan {runId}`
74. Verifikasi Notes tersimpan `Pompa diperiksa bulanan` dan pelaksana tersimpan tetap `Servis Cakupan Berubah {runId}`
75. Simpan Edit Task `Task Pompa Berjalan {runId}` dengan pelaksana diganti `CV Genset Prima {runId}` lewat permintaan langsung
76. Verifikasi permintaan ditolak dengan pesan `CV Genset Prima {runId} doesn't cover this asset.`, karena nilai pelaksana diganti dengan Service Center yang tidak cocok
77. Simpan Task `Task Uji Tolak Baru {runId}` untuk Asset `Chiller Lantai 2 {runId}` dengan pelaksana `CV Genset Prima {runId}` lewat permintaan langsung
78. Verifikasi permintaan ditolak dengan pesan `CV Genset Prima {runId} doesn't cover this asset.`, karena Task baru dibuat dengan Service Center yang tidak cocok
