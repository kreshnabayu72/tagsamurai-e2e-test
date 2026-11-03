---
id: TC-AC-DN-E2E-180-konkurensi-category-berubah-dan-sku-baru
title: "Konkurensi: Category Dihapus atau Mendapat Subcategory (Create) dan SKU Baru dari Sesi Lain saat Edit Category"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-105
  - TC-AC-DN-106
  - TC-AC-DN-582
coverage:
  web: automated
---

# Konkurensi: Category Dihapus atau Mendapat Subcategory (Create) dan SKU Baru dari Sesi Lain saat Edit Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement `Unit`, Brand `Brand C`, Model/Type `Model X`, node pohon Category. Nama dinamis dibentuk `<nama dasar> {runId}-180` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja kecuali dinyatakan): #13 Measurement `Unit`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `GPS`).
- Data Dinamis (milik spec; dibuat fixture BE di hook `before`, dihapus di hook `after`; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Data | Detail | Dipakai oleh |
  |---|---|---|---|
  | C1 | Node Category `Kategori Sementara {runId}-180` | leaf di bawah `TAG` > `GPS`, tanpa Device Name; dihapus Maya lewat sesi API | TC-AC-DN-105 |
  | D1 | Nama `Stale Cat Gateway {runId}-180` | diketik sesi Budi; Submit ditolak | TC-AC-DN-105 |
  | D2 | Nama `Nonleaf Gateway {runId}-180` | Measurement `Unit`, Category `Antenna`; Maya menambah Subcategory `Antenna Outdoor {runId}-180` di bawah `Antenna` lewat sesi API | TC-AC-DN-106 |
  | R1 | Device Name `Antenna Edit {runId}-180` | Measurement `Unit`, Category `Antenna`, tanpa SKU; Maya membuat SKU `DA-CX-6-{runId}-180` (Brand C/Model X) | TC-AC-DN-582 |

- Kemampuan teknis (disediakan tim FE/BE): sesi API Maya Putri untuk menghapus node Category, menambah Subcategory, dan membuat SKU (tanpa endpoint karangan, S-13); membaca jumlah entri Changelog Device Name (baseline N0, S-12).
- State global (S-06, pengecualian 2026-10-30): pohon Category Pre-setup #14 menerima C1 dan Subcategory `Antenna Outdoor {runId}-180` (membuat `Antenna` sementara bukan leaf); fixture backend menghapus keduanya setelah blok (langkah 27) dan di hook `before` dan `after`. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

### TC-AC-DN-105: Category dihapus admin lain

1. Klik `+ Device Name`
2. Ketik "Stale Cat Gateway {runId}-180" pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field Category, expand `TAG` lalu `GPS`, pilih leaf `Kategori Sementara {runId}-180`
5. Maya Putri (sesi API) menghapus Category `Kategori Sementara {runId}-180` hingga terhapus
6. Klik `[Submit]`
7. Verifikasi error inline di bawah field Category: "This category no longer exists. Please select another."
8. Verifikasi field Category dikosongkan
9. Klik field Category, expand `TAG` lalu `GPS`
10. Verifikasi pohon Category memuat node `GPS`
11. Verifikasi pohon Category tidak memuat `Kategori Sementara {runId}-180`
12. Verifikasi field Device Name berisi "Stale Cat Gateway {runId}-180" dan field Measurement berisi `Unit`
13. Verifikasi popup form tetap terbuka
14. Klik icon `(✕)` pada form
15. Verifikasi dialog `Unsaved Changes` tampil
16. Klik `[Leave]`

### TC-AC-DN-106: Category mendapat Subcategory setelah dipilih

17. Klik `+ Device Name`
18. Ketik "Nonleaf Gateway {runId}-180" pada field Device Name
19. Klik field Measurement lalu pilih `Unit`
20. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
21. Maya Putri (sesi API) menambahkan Subcategory `Antenna Outdoor {runId}-180` di bawah `Antenna` hingga tersimpan
22. Klik `[Submit]`
23. Verifikasi toast sukses "Success, device name has been created."
24. Verifikasi popup form tertutup
25. Ketik Search `Nonleaf Gateway {runId}-180`, tekan Enter
26. Verifikasi List memuat baris `Nonleaf Gateway {runId}-180` dengan Category badge `Antenna`
27. Hapus Subcategory `Antenna Outdoor {runId}-180` lewat fixture BE hingga terhapus

### TC-AC-DN-582: SKU baru dari sesi lain saat Edit Category

28. Catat jumlah entri Changelog Device Name sebagai N0 lewat kemampuan baca Changelog
29. Ketik Search `Antenna Edit {runId}-180`, tekan Enter
30. Buka menu aksi pada baris `Antenna Edit {runId}-180`, klik `Edit`
31. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
32. Maya Putri (sesi API) membuat SKU `DA-CX-6-{runId}-180` (Brand C/Model X) untuk Device Name `Antenna Edit {runId}-180` hingga tersimpan
33. Klik `[Save]`
34. Verifikasi error inline "This device name already has SKUs. Category cannot be changed." di bawah field Category pada form Edit
35. Verifikasi form Edit tetap terbuka
36. Verifikasi tidak ada toast tampil
37. Klik icon `(✕)` pada form
38. Verifikasi dialog `Unsaved Changes` tampil
39. Klik `[Leave]`
40. Verifikasi baris `Antenna Edit {runId}-180` menampilkan badge Category `Antenna`
41. Verifikasi baris `Antenna Edit {runId}-180` menampilkan Brand `Brand C`
42. Klik ikon Changelog
43. Verifikasi modal "Changelog: Device Name" memuat jumlah entri sama dengan N0

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah pemicu ditulis "... hingga ... tersimpan/terhapus" (R-20). Pembuatan dan penghapusan node Category, Subcategory, dan SKU lewat sesi API adalah kemampuan yang disediakan tim FE/BE; TC menyebut jalur UI untuk langkah tersebut.
- Langkah penghubung (S-03, R-16): langkah 9 sampai 11 membuka pohon Category agar "pohon dimuat ulang" teramati (S-14), dengan langkah 10 sebagai anchor langkah 11 (8b butir 2); langkah 14 sampai 16 dan 37 sampai 39 menutup form dirty (S-08, S-09); langkah 25, 29 (Search) menemukan baris record milik spec; langkah 27 memulihkan pohon Category (S-06); langkah 28 mencatat baseline.
- Record milik spec (S-06, S-12): C1, D2, dan R1 menggantikan `Kategori Sementara`, `Antenna`, dan `Door Antenna` Pre-setup #16 TC sumber; baris Device Name Pre-setup tidak diubah.
- Urutan: mengikuti sourceTc; tidak ada aksi menghapus data Device Name oleh spec.
- Ukuran spec (43 langkah, di atas smell 35 langkah, kode R3): satu topik (perubahan Category oleh admin lain), satu kelas harness, tiap blok memakai data sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-105 (tidak ada record baru), TC-AC-DN-106 (pemulihan baseline), TC-AC-DN-582 (Category tetap `Antenna`; SKU tersimpan).
  - TC-AC-DN-582 Expected d: "tidak ada entri baru untuk Door Antenna" diasersi dengan jumlah entri sama dengan N0 karena hasil Search kosong tidak membuktikan ketiadaan entri lintas halaman dan baseline N0 lebih deterministik; TC menyebut "11 entri" dan spec tidak memakai angka absolut (S-12).
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-180` (S-12).
