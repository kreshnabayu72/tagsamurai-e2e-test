---
id: TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single
title: "Bulk Delete Homogen: Dialog Single untuk 1 Item Bebas Relasi, Screening Dialog, Cancel, Delete, Daftar Nama Tidak Diringkas, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-137
  - TC-GS-POS-139
  - TC-GS-POS-140
  - TC-GS-POS-141
  - TC-GS-POS-146
  - TC-GS-POS-150
coverage:
  web: automated
---

# Bulk Delete Homogen: Dialog Single untuk 1 Item Bebas Relasi, Screening Dialog, Cancel, Delete, Daftar Nama Tidak Diringkas, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec bergantung pada Selection Limit bawaan (tidak kurang dari 12), sedangkan spec 024 menurunkan Selection Limit sementara dan memulihkannya di hook `after`; spec ini tidak berjalan bersamaan dengan spec 024. Spec ini juga menghapus Position, sehingga dijalankan sesudah spec lain.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Data Pre-setup: tidak ada yang dibaca atau diubah spec ini. Position Pre-setup 10-16 tetap berada di tabel dan tidak diasersi.
- Data Dinamis (di-seed lewat API di hook `before`; bebas relasi dan tidak dipakai user; nama bersuffix per run; fixture baru `Fixture.position.bulkDeleteSeed025`): `Account Executive {runId}-025`, `Business Analyst {runId}-025`, `Content Writer {runId}-025`, `UX Researcher {runId}-025`, dan 12 Position `Bulk Name 01 {runId}-025` sampai `Bulk Name 12 {runId}-025` (untuk TC-GS-POS-146). Data ini menggantikan Data Dinamis No. 20-34 pada TC sumber.
- Total Position di environment tidak lebih dari 100 sehingga semua baris tampil dalam satu halaman pada ukuran halaman 100; Selection Limit tidak kurang dari 12 (nilai bawaan tidak diubah spec ini).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-025` yang masih ada (termasuk 12 `Bulk Name NN` yang tidak dihapus oleh langkah spec).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: dua klik beruntun cepat pada `[Delete]` (TC-GS-POS-150); pembacaan jumlah toast yang tampil bersamaan; pengamatan severity dialog, gaya tombol, dan container scrollable.
- State global: ukuran halaman tabel diubah ke 100 (langkah 1) dan dikembalikan ke 10 (langkah terakhir, langkah 53); selain itu dan flag Guided Tooltip (diatur hook suite) tidak ada state global yang diubah.

## Test Steps

1. Ubah ukuran halaman tabel ke 100

### TC-GS-POS-137: Bulk Delete 1 jabatan bebas relasi memakai dialog single

2. Centang baris `Account Executive {runId}-025`
3. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
4. Verifikasi Title dialog "Delete Position" (singular)
5. Verifikasi severity dialog danger
6. Verifikasi body dialog memuat `• Account Executive {runId}-025`
7. Verifikasi body dialog hanya memuat satu bullet (format single, bukan daftar bulk)
8. Verifikasi body dialog memuat "Are you sure you want to delete it? This action cannot be undone."
9. Verifikasi footer dialog memuat tombol `[Cancel]`
10. Verifikasi footer dialog memuat tombol `[Delete]`
11. Klik `[Cancel]`
12. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-139: Screening Dialog Delete Position, seluruh terpilih bebas relasi

13. Centang baris `Business Analyst {runId}-025` dan `Content Writer {runId}-025`
14. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
15. Verifikasi Title dialog "Delete Position"
16. Verifikasi severity dialog danger
17. Verifikasi body dialog memuat `• Business Analyst {runId}-025`
18. Verifikasi body dialog memuat `• Content Writer {runId}-025`
19. Verifikasi body dialog memuat "Are you sure you want to delete them? This action cannot be undone."
20. Verifikasi tombol `[Cancel]` di footer berupa text button dengan warna contrast
21. Verifikasi tombol `[Delete]` di footer berupa filled button dengan severity danger

### TC-GS-POS-140: Bulk Delete homogen, Cancel mempertahankan seleksi

22. Klik `[Cancel]` pada dialog yang sama (langkah 1 dan 2 TC sumber identik dengan langkah 13 dan 14)
23. Verifikasi dialog tertutup
24. Verifikasi baris `Business Analyst {runId}-025` tetap ada
25. Verifikasi baris `Business Analyst {runId}-025` tetap tercentang
26. Verifikasi baris `Content Writer {runId}-025` tetap ada
27. Verifikasi baris `Content Writer {runId}-025` tetap tercentang
28. Verifikasi counter Bulk Action Bar "2 Positions selected"
29. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-146: Daftar nama di Dialog Delete Position tidak diringkas

30. Centang 12 baris `Bulk Name 01 {runId}-025` sampai `Bulk Name 12 {runId}-025`
31. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
32. Verifikasi ke-12 nama `• Bulk Name 01 {runId}-025` sampai `• Bulk Name 12 {runId}-025` tampil sebagai bullet pada dialog
33. Verifikasi ke-12 bullet berada di container scrollable
34. Verifikasi dialog tidak memuat ringkasan "[N] items are selected."
35. Verifikasi dialog tidak memuat "...and N more"
36. Klik `[Cancel]`
37. Klik `[✕]` pada Bulk Action Bar untuk membatalkan seleksi

### TC-GS-POS-141: Bulk Delete homogen, Delete

38. Centang baris `Business Analyst {runId}-025` dan `Content Writer {runId}-025`
39. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
40. Klik `[Delete]`
41. Verifikasi toast sukses "Success, position has been deleted."
42. Verifikasi baris `Business Analyst {runId}-025` hilang dari tabel
43. Verifikasi baris `Content Writer {runId}-025` hilang dari tabel
44. Verifikasi Bulk Action Bar hilang
45. Verifikasi tidak ada baris yang tercentang (seleksi 0)

### TC-GS-POS-150: Bulk Delete, klik ganda Delete hanya diproses sekali

46. Tunggu toast dari langkah 41 hilang otomatis
47. Centang baris `Account Executive {runId}-025` dan `UX Researcher {runId}-025`
48. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
49. Klik `[Delete]` 2× cepat
50. Verifikasi hanya 1 toast sukses "Success, position has been deleted." yang tampil
51. Verifikasi baris `Account Executive {runId}-025` hilang dari tabel
52. Verifikasi baris `UX Researcher {runId}-025` hilang dari tabel
53. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 137, 139, 140, 146, 141, 150. Dialog yang tidak menghapus data (137, 139, 140, 146) dijalankan lebih dulu; TC-GS-POS-141 dan 150 menghapus data sehingga ditaruh paling akhir (bagian 3 prinsip 5). Urutan ini menyimpang dari urutan TC sumber (146 sebelum 141).
- TC-GS-POS-139 dan 140 memakai satu pembukaan dialog: langkah 1 dan 2 TC-GS-POS-140 identik dengan langkah 13 dan 14 sehingga langkah 22 melanjutkan dialog yang sama (bagian 3 prinsip 8). Aksi `[Delete]` TC-GS-POS-141 membuka dialog baru (langkah 38 sampai 40).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar semua baris tampil tanpa Search), langkah 12, 29, dan 37 (`[✕]` pada Bulk Action Bar membatalkan seleksi sebelum TC berikutnya), langkah 11 dan 36 (`[Cancel]` menutup dialog; TC-GS-POS-137 dan 146 tidak memuat langkah menutup dialog), langkah 46 (menunggu toast sukses dari langkah 41 hilang otomatis supaya hitungan toast pada langkah 50 hanya memuat toast hasil klik ganda), serta langkah 53 (mengembalikan ukuran halaman ke 10).
- Langkah 24 sampai 27 memecah Expected b TC-GS-POS-140 ("kedua baris tetap ada dan tetap tercentang") per baris dan per klausa.
- Pembagian TC lintas spec: Bulk Action Bar dan seleksi per halaman ada di spec 022 dan 023; Selection Limit di spec 024; Bulk Delete 1 item in-use (TC-GS-POS-138), campuran, dan seluruhnya in-use di spec 026 (blokir karena kondisi data, bagian 3 prinsip 12); Bulk Delete mobile (TC-GS-POS-151) di spec 027.
- Spec melewati sekitar 35 langkah (53 langkah). Seluruhnya satu kelas harness (Bulk Delete homogen lewat Bulk Action Bar), satu akun, satu dataset; tiap blok TC memilih ulang barisnya dan tetap bermakna bila blok lain gagal. Aksi yang menghapus data (TC-GS-POS-141 dan 150) berada di akhir.
- Temuan untuk QA:
  - Data Dinamis No. 20-34 pada TC sumber ("15 nama bulk `Account Executive` ... `UX Researcher`") tidak dirinci seluruhnya. Langkah TC-GS-POS-146 ("`Facility Manager` s.d. `UX Researcher` kecuali `Graphic Designer`, `Network Engineer`, `Product Designer`", 12 nama) tidak konsisten dengan daftar 15 nama yang juga memuat `Account Executive`, `Business Analyst`, `Content Writer`, `Customer Support Agent`. Spec memakai 12 Position `Bulk Name NN {runId}-025` untuk TC-GS-POS-146; nama pasti 12 Position dari TC tidak dapat ditentukan.
  - Post Condition "Changelog: Position mencatat 2 entri Delete (1 per jabatan)" (TC-GS-POS-141) dan "Changelog mencatat tepat 2 entri Delete" (TC-GS-POS-150) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-GS-POS-137 tidak menyebut counter Bulk Action Bar untuk satu item; tidak diasersi.
  - Selection Limit bawaan tidak disebut di TC; spec mengasumsikan tidak kurang dari 12 (dicatat di Prerequisites).
