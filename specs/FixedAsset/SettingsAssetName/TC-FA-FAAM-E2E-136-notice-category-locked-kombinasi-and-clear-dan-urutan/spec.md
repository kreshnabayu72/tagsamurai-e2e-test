---
id: TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan
title: "Notice Category Locked: Quick Filter AND dengan Search-Filter, Clear Terpisah, Seleksi, dan Urutan Elemen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-695
  - TC-FA-FAAM-696
  - TC-FA-FAAM-702
  - TC-FA-FAAM-724
coverage:
  web: automated
---

# Notice Category Locked: Quick Filter AND dengan Search-Filter, Clear Terpisah, Seleksi, dan Urutan Elemen

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoLocked` (Pre-setup #12c); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_LOCKED_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (client `AutoLocked`, Pre-setup #12c; tidak diubah spec ini; `Fixture.faSettingsAssetName.autoLocked`, fixture baru belum ada): 30 `Seed Item 01` sampai `Seed Item 30` (Category `IT Equipment`, Total Asset 0) dan 3 Asset Name Category Locked `Lock Alpha`, `Lock Beta`, `Lock Gamma` (Category internal `Electronics`, Total Asset 0); hitungan Needs Update 3.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-695: Quick filter berkombinasi AND dengan Search dan Filter Panel dan hasil 0 menampilkan empty state
1. Klik `Show only these`
2. Ketik Search `Beta`, tekan Enter
3. Verifikasi baris `Lock Beta` tampil di tabel
4. Verifikasi hanya `Lock Beta` yang tampil
5. Verifikasi notice tetap `Showing 3 asset names that need a category update.` (hitungan katalog, bukan jumlah baris)
6. Ganti isi kotak search dengan `Seed`, tekan Enter
7. Verifikasi tabel kosong dengan Title `No results found` dan Description `Try adjusting your search or filter.`
8. Verifikasi notice tetap tampil
9. Verifikasi chip `Needs Update` tetap tampil
10. Klik `(←)` pada kotak Search
11. Klik icon Filter, buka dropdown Category
12. Verifikasi dropdown Category memuat `IT Equipment` dan `Electronics` walau quick filter aktif (opsi berasal dari seluruh katalog client)
13. Pilih Category `IT Equipment`, lalu klik `[Apply]`
14. Verifikasi tabel kosong dengan Title `No results found` dan Description `Try adjusting your search or filter.`
15. Verifikasi notice tetap tampil
16. Verifikasi chip `Needs Update` tetap tampil
17. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
18. Klik `Clear filter`
### TC-FA-FAAM-696: Clear Search dan [Clear Field] Filter Panel tidak melepas quick filter
19. Klik `Show only these`
20. Ketik Search `Lock`, tekan Enter
21. Klik icon Filter, pilih Category `Electronics`, lalu klik `[Apply]`
22. Klik `(✕)` pada Search, lalu tekan Enter pada input kosong
23. Verifikasi Search kosong
24. Verifikasi chip `Needs Update` tetap tampil
25. Verifikasi notice `Showing 3 asset names that need a category update.` tetap tampil
26. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
27. Verifikasi Filter Panel kosong
28. Verifikasi chip `Needs Update` tetap tampil
29. Verifikasi notice `Showing 3 asset names that need a category update.` tetap tampil
30. Verifikasi tabel memuat tiga Asset Name `Needs Update`
31. Klik `Clear filter`
### TC-FA-FAAM-702: Seleksi checkbox tidak direset oleh pemasangan dan pelepasan quick filter
32. Centang baris `Lock Alpha` dan `Seed Item 01`
33. Klik `Show only these`
34. Verifikasi Bulk Action Bar tetap tampil dengan `2 asset names selected`
35. Verifikasi `Lock Alpha` tetap tercentang
36. Klik `Clear filter`
37. Verifikasi `Lock Alpha` dan `Seed Item 01` masih tercentang
38. Verifikasi Bulk Action Bar tetap `2 asset names selected`
39. Klik `Unselect All` pada Bulk Action Bar
### TC-FA-FAAM-724: Quick filter Category Locked tidak menyalakan badge titik ikon Filter dan bukan field Filter Panel; urutan notice, chip, dan Bulk Action Bar
40. Klik `Show only these`
41. Verifikasi chip `Needs Update` tampil
42. Verifikasi ikon Filter tidak menampilkan badge titik
43. Klik icon Filter
44. Verifikasi Filter Panel menampilkan field `Category`
45. Verifikasi Filter Panel tidak memuat field quick filter (tidak ada field `Needs Update` atau Category Locked)
46. Klik icon Filter untuk menutup Filter Panel
47. Centang baris `Lock Alpha`
48. Verifikasi urutan dari atas ke bawah: Table Tools, Alert `Showing 3 asset names that need a category update.`, chip `Needs Update`, Bulk Action Bar `1 asset name selected`, lalu tabel
49. Klik `Unselect All` pada Bulk Action Bar
50. Klik `Clear filter`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan konfigurasi kolom dan pembersihan Search, Filter, dan seleksi di antara blok (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): `Clear filter` di akhir blok dan `Unselect All` supaya blok berikutnya mulai tanpa quick filter dan tanpa seleksi (S-09); dropdown Category dibuka sesuai langkah 4 TC-FA-FAAM-695.
- Asersi "hanya `Lock Beta` yang tampil" pada TC-FA-FAAM-695 didahului Verifikasi `Lock Beta` tampil (bagian 8b butir 2); absence badge titik dan field quick filter pada TC-FA-FAAM-724 beranchor Verifikasi chip `Needs Update` dan field `Category` tampil.
- Pada TC-FA-FAAM-702 baris `Lock Alpha` dan `Seed Item 01` berada di halaman 1 menurut urutan default Asset Name A-Z.
- Di atas smell 35 langkah. Spec berjumlah 50 langkah (melewati sekitar 35). Semua blok adalah kombinasi quick filter Category Locked pada client `AutoLocked` yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: Pre-setup #12c berupa client tanpa baris akun Total Control (email tidak tertulis).
