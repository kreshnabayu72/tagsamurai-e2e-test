---
id: TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use
title: "Bulk Delete Blokir In-Use (Satu Item dan Seluruhnya), Campuran (Warning lalu Continue), dan Daftar Nama Tidak Diringkas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-138
  - TC-GS-POS-142
  - TC-GS-POS-143
  - TC-GS-POS-144
  - TC-GS-POS-145
  - TC-GS-POS-302
  - TC-GS-POS-303
coverage:
  web: automated
---

# Bulk Delete Blokir In-Use (Satu Item dan Seluruhnya), Campuran (Warning lalu Continue), dan Daftar Nama Tidak Diringkas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec bergantung pada Selection Limit bawaan (tidak kurang dari 24), sedangkan spec 024 menurunkan Selection Limit sementara dan memulihkannya di hook `after`; spec ini tidak berjalan bersamaan dengan spec 024. Spec ini juga menghapus Position, sehingga dijalankan sesudah spec lain.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Data Pre-setup (tetap di environment, hanya dibaca, tidak diubah atau dihapus spec ini, tanpa suffix): Position 12 `Warehouse Supervisor` (dipakai user Login aktif `Rina Wulandari`) dan Position 13 `Customer Success Manager` (dipakai user Non-Login `Agus Pratama`), keduanya merujuk Pre-setup 17. Kedua Position in-use ini dirancang TC untuk blokir: hanya dibaca dan diblokir atau dilewati guard in-use (pengecualian S-06), sehingga tidak berubah dan Last Updated-nya tidak berubah. Aksi `[Continue]` pada TC-GS-POS-144 melewati `Warehouse Supervisor` sehingga Position itu tidak terhapus.
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.bulkDeleteMixedSeed026`): `Customer Support Agent {runId}-026` (bebas relasi, dihapus oleh TC-GS-POS-144); 12 Position `Scroll In-Use 01 {runId}-026` sampai `Scroll In-Use 12 {runId}-026`, masing-masing dipakai satu user aktif bersuffix `{runId}-026` yang di-seed lewat API; 12 Position `Scroll Free 01 {runId}-026` sampai `Scroll Free 12 {runId}-026` (bebas relasi). Mekanisme seeding user disediakan tim FE/BE (TC tidak menyebut tipe user).
- Total Position di environment tidak lebih dari 100 sehingga semua baris tampil dalam satu halaman pada ukuran halaman 100; Selection Limit tidak kurang dari 24 (nilai bawaan tidak diubah spec ini).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user bersuffix `{runId}-026` yang masih ada terlebih dahulu, lalu semua Position bersuffix `{runId}-026` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pengamatan severity dialog, gaya tombol, dan container scrollable; pembacaan ada atau tidaknya toast.
- State global: ukuran halaman tabel diubah ke 100 (langkah 1) dan dikembalikan ke 10 (langkah terakhir, langkah 69); selain itu dan flag Guided Tooltip (diatur hook suite) tidak ada state global yang diubah.

## Test Steps

### TC-GS-POS-138: Bulk Delete 1 jabatan in-use memakai dialog blokir single

1. Ubah ukuran halaman tabel ke 100
2. Centang baris `Warehouse Supervisor`
3. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
4. Verifikasi dialog "Cannot Delete Data" tampil
5. Verifikasi dialog memuat `• Warehouse Supervisor`
6. Verifikasi body dialog "This position is still in use. Remove the references before deleting."
7. Verifikasi dialog memuat tombol `[OK]`
8. Klik `[OK]`
9. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-145: Bulk Delete, seluruh terpilih in-use diblokir

10. Centang baris `Warehouse Supervisor` dan `Customer Success Manager`
11. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
12. Verifikasi dialog "Cannot Delete Data" tampil
13. Verifikasi severity dialog warning
14. Verifikasi Dialog Delete Position campuran tidak tampil
15. Verifikasi dialog memuat `• Warehouse Supervisor`
16. Verifikasi dialog memuat `• Customer Success Manager`
17. Verifikasi dialog memuat "These positions are still in use. Remove the references before deleting."
18. Verifikasi footer dialog hanya memuat tombol `[OK]`
19. Klik `[OK]`
20. Verifikasi tidak ada toast yang tampil
21. Verifikasi dialog tertutup
22. Verifikasi baris `Warehouse Supervisor` tetap tercentang
23. Verifikasi baris `Customer Success Manager` tetap tercentang
24. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-302: Daftar nama di Dialog Cannot Delete Data (bulk) tidak diringkas

25. Centang 12 baris `Scroll In-Use 01 {runId}-026` sampai `Scroll In-Use 12 {runId}-026`
26. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
27. Verifikasi dialog "Cannot Delete Data" menampilkan ke-12 bullet `• Scroll In-Use 01 {runId}-026` sampai `• Scroll In-Use 12 {runId}-026`
28. Verifikasi ke-12 bullet berada di container scrollable
29. Verifikasi dialog tidak memuat ringkasan "[N] items are selected."
30. Verifikasi dialog tidak memuat "...and N more"
31. Klik `[OK]`
32. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-142: Screening Dialog Delete Position campuran (sebagian in-use)

33. Centang baris `Customer Support Agent {runId}-026` dan `Warehouse Supervisor`
34. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
35. Verifikasi Title dialog "Delete Position"
36. Verifikasi severity dialog warning
37. Verifikasi body dialog memuat "The following will be deleted:"
38. Verifikasi kelompok tersebut memuat `• Customer Support Agent {runId}-026`
39. Verifikasi body dialog memuat "The following are still in use and will be skipped:"
40. Verifikasi kelompok tersebut memuat `• Warehouse Supervisor`
41. Verifikasi body dialog memuat "Are you sure you want to continue? This action cannot be undone."
42. Verifikasi tombol `[Cancel]` di footer berupa text button dengan warna contrast
43. Verifikasi tombol `[Continue]` di footer berupa filled button dengan severity danger

### TC-GS-POS-143: Bulk Delete campuran, Cancel mempertahankan seleksi

44. Klik `[Cancel]` pada dialog yang sama (langkah 1 dan 2 TC sumber identik dengan langkah 33 dan 34)
45. Verifikasi dialog tertutup
46. Verifikasi baris `Customer Support Agent {runId}-026` tetap ada
47. Verifikasi baris `Customer Support Agent {runId}-026` tetap tercentang
48. Verifikasi baris `Warehouse Supervisor` tetap ada
49. Verifikasi baris `Warehouse Supervisor` tetap tercentang
50. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-303: Daftar nama di Dialog Delete Position campuran tidak diringkas

51. Centang 24 baris `Scroll Free 01 {runId}-026` sampai `Scroll Free 12 {runId}-026` dan `Scroll In-Use 01 {runId}-026` sampai `Scroll In-Use 12 {runId}-026`
52. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
53. Verifikasi kelompok "The following will be deleted:" menampilkan ke-12 bullet `• Scroll Free 01 {runId}-026` sampai `• Scroll Free 12 {runId}-026`
54. Verifikasi ke-12 bullet `Scroll Free NN` berada di container scrollable
55. Verifikasi kelompok "The following are still in use and will be skipped:" menampilkan ke-12 bullet `• Scroll In-Use 01 {runId}-026` sampai `• Scroll In-Use 12 {runId}-026`
56. Verifikasi ke-12 bullet `Scroll In-Use NN` berada di container scrollable
57. Verifikasi dialog tidak memuat ringkasan "[N] items are selected."
58. Verifikasi dialog tidak memuat "...and N more"
59. Klik `[Cancel]`
60. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-144: Bulk Delete campuran, Continue

61. Centang baris `Customer Support Agent {runId}-026` dan `Warehouse Supervisor`
62. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
63. Klik `[Continue]`
64. Verifikasi toast sukses "Success, position has been deleted. Some items were skipped."
65. Verifikasi baris `Customer Support Agent {runId}-026` hilang dari tabel
66. Verifikasi baris `Warehouse Supervisor` tetap ada di tabel
67. Verifikasi Bulk Action Bar hilang
68. Verifikasi tidak ada baris yang tercentang (seleksi 0), termasuk `Warehouse Supervisor` yang dilewati
69. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 138, 145, 302, 142, 143, 303, 144. Dialog blokir (138, 145, 302) dijalankan lebih dulu, lalu dialog campuran yang tidak menghapus data (142, 143, 303); TC-GS-POS-144 menghapus `Customer Support Agent {runId}-026` sehingga ditaruh paling akhir (bagian 3 prinsip 5). Urutan ini menyimpang dari urutan TC sumber.
- TC-GS-POS-142 dan 143 memakai satu pembukaan dialog: langkah 1 dan 2 TC-GS-POS-143 identik dengan langkah 33 dan 34 sehingga langkah 44 melanjutkan dialog yang sama (bagian 3 prinsip 8). TC-GS-POS-144 membuka dialog baru (langkah 61 sampai 63).
- Pada TC-GS-POS-145, asersi tidak ada toast (langkah 20) diletakkan segera sesudah klik `[OK]` (langkah 19) dan sebelum asersi dialog tertutup dan baris tetap tercentang, karena toast adalah state sementara; urutan ini menyimpang dari urutan Expected TC-GS-POS-145 d (bagian 8b butir 5 dan 11).
- Langkah 46 sampai 49 memecah Expected b TC-GS-POS-143 ("kedua baris tetap ada dan tercentang") per baris dan per klausa.
- Langkah 64 (toast sukses TC-GS-POS-144) diasersi segera sesudah `[Continue]` karena toast sukses hilang otomatis (bagian 8b butir 5); urutan ini menyimpang dari urutan Expected TC (a, b, lalu c).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar semua baris tampil tanpa Search), langkah 8 (`[OK]` menutup dialog "Cannot Delete Data"; TC-GS-POS-138 tidak memuat langkah menutup dialog), langkah 9, 24, 32, 50, dan 60 (`[✕]` pada Bulk Action Bar membatalkan seleksi sebelum TC berikutnya), langkah 31 (`[OK]` menutup dialog "Cannot Delete Data"), langkah 59 (`[Cancel]` menutup dialog), dan langkah 69 (mengembalikan ukuran halaman ke 10).
- Pembagian TC lintas spec: Bulk Delete homogen dan dialog single untuk 1 item bebas relasi (TC-GS-POS-137, 139, 140, 141, 146, 150) di spec 025; seleksi per halaman dan Select All di spec 022 dan 023; Selection Limit di spec 024; Bulk Delete mobile di spec 027.
- Spec melewati sekitar 35 langkah (69 langkah). Seluruhnya satu kelas harness (Bulk Delete dengan evaluasi in-use lewat Bulk Action Bar), satu akun, satu dataset; tiap blok TC memilih ulang barisnya dan tetap bermakna bila blok lain gagal. Aksi yang menghapus data (TC-GS-POS-144) berada di akhir.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-144 ("Changelog: Position mencatat 1 entri Delete untuk `Customer Support Agent`; tidak ada entri untuk `Warehouse Supervisor`") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); bagian "tidak ada entri" adalah asersi absence.
  - Post Condition "Tidak ada record terhapus" (TC-GS-POS-145 dan 302) tidak punya langkah observasi tersendiri; Expected TC-GS-POS-145 d hanya menyebut kedua baris tetap tercentang dan tidak ada toast, yang diasersi pada langkah 20 sampai 23. TC-GS-POS-302 tidak punya Expected tentang `[OK]`; spec menutup dialog sebagai langkah penghubung.
  - TC-GS-POS-138 tidak memuat langkah menutup dialog dan tidak menyebut counter Bulk Action Bar untuk satu item; spec mengklik `[OK]` (tombol dari Expected b) sebagai langkah penghubung dan tidak mengasersi counter.
  - TC-GS-POS-302 dan 303 mensyaratkan 12 Position dipakai "≥1 user" tanpa menyebut tipe atau status user dan cara menyiapkannya; spec memakai satu user aktif bersuffix per Position dengan mekanisme seeding yang disediakan tim FE/BE.
  - Nama `Scroll In-Use NN` dan `Scroll Free NN` di TC literal tanpa suffix; spec memberi suffix `{runId}-026` agar tidak bentrok antarrun.
