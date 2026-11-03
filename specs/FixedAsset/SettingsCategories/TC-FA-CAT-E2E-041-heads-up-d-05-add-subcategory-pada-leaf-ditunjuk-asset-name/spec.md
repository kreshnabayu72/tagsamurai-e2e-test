---
id: TC-FA-CAT-E2E-041-heads-up-d-05-add-subcategory-pada-leaf-ditunjuk-asset-name
title: "Heads-up D-05 pada Add Subcategory untuk Leaf yang Ditunjuk Asset Name: Isi Dialog, Cancel, Backdrop dan Esc, Daftar Panjang, dan Hasil Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-130
  - TC-FA-CAT-131
  - TC-FA-CAT-132
  - TC-FA-CAT-647
  - TC-FA-CAT-648
  - TC-FA-CAT-134
  - TC-FA-CAT-133
coverage:
  web: automated
---

# Heads-up D-05 pada Add Subcategory untuk Leaf yang Ditunjuk Asset Name: Isi Dialog, Cancel, Backdrop dan Esc, Daftar Panjang, dan Hasil Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup yang hanya dibaca (aksi dibatalkan atau ditutup tanpa Submit, tidak diubah, Last Updated tidak berubah, S-06): `Laptop` ditunjuk Asset Name `Laptop Dell` dan `Laptop HP`, `Furniture` ditunjuk `Office Chair` (Pre-setup #21), `Vehicle` (leaf tidak ditunjuk), `Peripheral` (Internal), dan `Many Names` (Code `MN`, ditunjuk `Many Name 01` sampai `Many Name 30`, Pre-setup #49).
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): kategori L1 leaf `Furniture Own {runId}-041` dengan 5 aset terhitung dan Asset Name `Office Chair {runId}-041` yang menunjuknya. Data Dinamis dibuat spec: `Chairs {runId}-041` (Code `CHR`) di bawah `Furniture Own {runId}-041`. Hook `after` menghapus `Chairs {runId}-041` dan `Furniture Own {runId}-041` beserta Asset Name-nya.
- Kemampuan teknis: membaca jumlah baris Modal Changelog sebelum dan sesudah aksi (baseline, S-12).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-130: Heads-up bentuk jamak

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `+ Add Subcategory`
3. Verifikasi dialog `Add Subcategory` tampil sebelum popup form dibuka
4. Verifikasi dialog memuat bullet `Laptop` dan kalimat `Adding a subcategory will turn this category into a grouping-only category.`
5. Verifikasi dialog memuat kalimat `The following Asset Names use it and will be locked from new asset registration until updated to a different category:` dengan bullet `Laptop Dell` dan `Laptop HP`
6. Verifikasi dialog memuat `Are you sure you want to add a subcategory?`
7. Verifikasi tombol `[Cancel]` dan `[Add Subcategory]` (primary) tampil
8. Klik `[Cancel]`

### TC-FA-CAT-131: Heads-up bentuk tunggal

9. Klik node `All Categories` di Sidebar Category Tree
10. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
11. Verifikasi dialog D-05 memuat bullet `Furniture`, kalimat `The following Asset Name uses it and will be locked from new asset registration until updated to a different category:` (bentuk tunggal), bullet `Office Chair`, dan pertanyaan `Are you sure you want to add a subcategory?`
12. Klik `[Cancel]`

### TC-FA-CAT-132: Cancel membatalkan tanpa efek

13. Buka Modal Changelog, catat jumlah baris (baseline), lalu tutup Modal Changelog
14. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
15. Klik `[Cancel]` pada dialog
16. Verifikasi dialog tertutup
17. Verifikasi popup New Subcategory tidak terbuka
18. Verifikasi `Furniture` tetap leaf
19. Buka Modal Changelog
20. Verifikasi jumlah baris Changelog sama dengan baseline (tidak ada log)
21. Tutup Modal Changelog

### TC-FA-CAT-647: Backdrop diabaikan, Esc setara Cancel

22. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
23. Klik area backdrop di luar dialog
24. Verifikasi dialog `Add Subcategory` tetap terbuka
25. Tekan `Esc`
26. Verifikasi dialog tertutup
27. Verifikasi popup New Subcategory tidak terbuka
28. Verifikasi `Furniture` tetap leaf
29. Buka Modal Changelog
30. Verifikasi jumlah baris Changelog sama dengan baseline (tidak ada baris log)
31. Tutup Modal Changelog

### TC-FA-CAT-648: Daftar 30 Asset Name

32. Klik elipsis (⋯) pada baris `Many Names` > `+ Add Subcategory`
33. Verifikasi dialog `Add Subcategory` memakai bentuk jamak `The following Asset Names use it and will be locked from new asset registration until updated to a different category:`
34. Gulir daftar bullet sampai bullet terakhir
35. Verifikasi seluruh 30 bullet `Many Name 01` sampai `Many Name 30` dapat dicapai lewat gulir di dalam container daftar, tanpa ringkasan `...and N more`
36. Verifikasi judul, kalimat `Are you sure you want to add a subcategory?`, `[Cancel]`, dan `[Add Subcategory]` tetap terlihat tanpa dialog meluap dari layar
37. Klik `[Cancel]`

### TC-FA-CAT-134: Tanpa heads-up untuk leaf tidak ditunjuk dan parent Internal

38. Klik elipsis (⋯) pada baris `Vehicle` > `+ Add Subcategory`
39. Verifikasi popup New Subcategory langsung terbuka untuk `Vehicle` tanpa dialog D-05
40. Klik `✕` pada popup
41. Klik elipsis (⋯) pada baris `Peripheral` > `+ Add Subcategory`
42. Verifikasi popup New Subcategory langsung terbuka untuk `Peripheral` tanpa dialog D-05
43. Klik `✕` pada popup

### TC-FA-CAT-133: Add Subcategory pada heads-up dan hasil Submit

44. Klik elipsis (⋯) pada baris `Furniture Own {runId}-041` > `+ Add Subcategory`
45. Klik `[Add Subcategory]` pada dialog
46. Verifikasi dialog tertutup
47. Verifikasi popup New Subcategory terbuka dengan banner `Adding subcategory under parent: Furniture Own {runId}-041`
48. Isi Category Name `Chairs {runId}-041` dan Code `CHR`
49. Klik `[Submit]`
50. Verifikasi toast `Success, category has been created.` tampil
51. Verifikasi `Furniture Own {runId}-041` menjadi Internal
52. Buka Popup Detail `Furniture Own {runId}-041`
53. Verifikasi Total Asset aset existing tetap `5`
54. Verifikasi aset existing tidak terkunci
55. Tutup Popup Detail

## Notes

- Alasan di atas sekitar 35 langkah: tujuh TC satu topik (heads-up D-05) dan satu client; tiap blok dimulai dari halaman tanpa dialog dan berdiri sendiri, aksi sukses (TC-133) ada di akhir sehingga hanya kategori milik spec yang berubah (S-10).
- Langkah penghubung (S-03): langkah 1, 9 (memilih node agar baris target tampil), 8, 12, 37 (menutup dialog), 13, 21, 31 (baseline dan penutupan Modal Changelog), 40, 43 (menutup popup tanpa input), 55 (menutup Popup Detail).
- Asersi "tidak ada log" TC-132 dan TC-647 ditulis sebagai asersi jumlah terhadap baseline langkah 13 (prinsip 13 bagian 3), dengan Modal Changelog yang tampil sebagai anchor; spec absence tidak memuat TC ini.
- Langkah 4 sampai 7 memecah Expected TC-130 a dan b per klausa (S-01).
- Temuan untuk QA:
  - TC-133 memakai `Furniture` Pre-setup yang berubah permanen; spec memakai kategori milik spec setara (5 aset, ditunjuk satu Asset Name) dan menjadikan `Furniture` Pre-setup hanya target aksi dibatalkan.
  - Post Condition TC-133 (Asset Name `Office Chair` berstatus Category Locked; Asset Name tidak menulis log) tanpa langkah observasi di TC sehingga tidak diasersi; TC dedicated ada di tc-settings-asset-name.md.
  - TC-132 dan TC-647 menyebut "tetap leaf" tanpa cara mengamati; spec mengamati baris `Furniture` tidak memiliki kontrol expand.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
