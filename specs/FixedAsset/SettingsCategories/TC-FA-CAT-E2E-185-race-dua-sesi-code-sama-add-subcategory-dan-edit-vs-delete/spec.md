---
id: TC-FA-CAT-E2E-185-race-dua-sesi-code-sama-add-subcategory-dan-edit-vs-delete
title: "Race Dua Sesi UI: Edit dengan Code Sama, Add Subcategory vs Delete, dan Edit vs Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-631
  - TC-FA-CAT-512
  - TC-FA-CAT-513
coverage:
  web: automated
---

# Race Dua Sesi UI: Edit dengan Code Sama, Add Subcategory vs Delete, dan Edit vs Delete

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1, dua sesi UI pada TC-631) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Sesi A: login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Sesi B: konteks browser kedua dengan akun yang sama, dibuka dan login lewat langkah 1 sampai 3, ditutup di hook `after`. Hook `after` juga mengembalikan sesi ke akun default suite.
- Pelaku kedua TC-512 dan TC-513 (menghapus node): Total Control (Pre-setup #1) lewat sesi API aktor (butir hook `suite.md`; kemampuan disediakan tim BE/FE), karena hasil di sesi itu tidak diasersi.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed tidak diubah.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Race Root {runId}-185` | `E185ROOT` | L1; dipilih di sidebar |
  | Target TC-631 | `Race Code A {runId}-185` | `E185CA` | anak `Race Root`; menggantikan `Furniture` |
  | Target TC-631 | `Race Code B {runId}-185` | `E185CB` | anak `Race Root`; menggantikan `Tools` |
  | Parent TC-512 | `Vehicle {runId}-185` | `E185VEH` | anak `Race Root`, leaf; dihapus pelaku kedua |
  | Target TC-513 | `Race Del {runId}-185` | `E185DEL` | anak `Race Root`, leaf; dihapus pelaku kedua |

- Code `RCODE3` (literal TC-631) harus bebas: hook `before` menghapus sisa kategori ber-Code `RCODE3` dari run yang gagal.
- Kemampuan teknis: dua konteks browser berjalan bersamaan dengan urutan klik terkendali; pemantauan respons jaringan untuk status 422 (disediakan tim FE); Modal Changelog dapat dibaca dan dicari; TreeSearchInput sidebar.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### Pembukaan Sesi B

1. Sesi B: buka konteks browser kedua dan login sebagai Total Control client CatMain
2. Sesi B: buka Fixed Asset > Settings > Categories
3. Sesi B: klik node `Race Root {runId}-185` di sidebar
4. Sesi A: klik node `Race Root {runId}-185` di sidebar

### TC-FA-CAT-631: Dua Edit dengan Code manual sama bersamaan: yang kedua ditolak dengan error unik

5. Sesi A: klik elipsis (⋯) pada baris `Race Code A {runId}-185` > `Edit`
6. Sesi A: isi Code `RCODE3`
7. Tunggu aksi selesai (popup Edit Sesi A terisi)
8. Sesi B: klik elipsis (⋯) pada baris `Race Code B {runId}-185` > `Edit`
9. Sesi B: isi Code `RCODE3`
10. Sesi A: klik `[Save]`
11. Sesi B: klik `[Save]` segera setelah Sesi A
12. Sesi A: verifikasi toast `Success, category has been updated.`
13. Sesi B: verifikasi Save ditolak server (422) dengan error inline `Code already exists`
14. Sesi B: verifikasi popup Edit tetap terbuka
15. Sesi B: verifikasi input Code `RCODE3` dipertahankan
16. Sesi B: klik `✕` pada header popup
17. Sesi B: klik `[Leave]`
18. Sesi B: muat ulang halaman
19. Sesi B: klik node `Race Root {runId}-185` di sidebar
20. Sesi B: verifikasi Code baris `Race Code B {runId}-185` tidak berubah (`E185CB`)

### TC-FA-CAT-512: Add Subcategory dan Delete parent bersamaan pada kategori sama

21. Sesi A: klik node `Vehicle {runId}-185` di sidebar
22. Sesi A: buka popup New Subcategory di bawah `Vehicle {runId}-185`
23. Sesi A: isi Category Name `Race Child {runId}-185`
24. Tunggu aksi selesai (popup New Subcategory Sesi A terisi)
25. Pelaku kedua (sesi API) menghapus `Vehicle {runId}-185` hingga penghapusan tersimpan
26. Sesi A: klik `[Submit]`
27. Sesi A: verifikasi Submit ditolak server (404) dengan toast netral `This category is no longer available.`
28. Sesi A: verifikasi popup New Subcategory tertutup
29. Sesi A: verifikasi tabel di-refresh dan menampilkan baris `Race Root {runId}-185`
30. Sesi A: verifikasi sidebar di-refresh tanpa node `Vehicle {runId}-185`
31. Sesi A: verifikasi seleksi sidebar kembali ke `All Categories`
32. Sesi A: verifikasi Category Context Header kembali menampilkan `All Categories`
33. Sesi A: ketik TreeSearchInput `Race Child {runId}-185`, tekan Enter
34. Sesi A: verifikasi sidebar menampilkan empty state `No results found` (tidak ada kategori baru)
35. Sesi A: kosongkan isi TreeSearchInput, tekan Enter
36. Sesi A: buka Modal Changelog
37. Sesi A: ketik Search `Race Child {runId}-185`, tekan Enter
38. Sesi A: verifikasi empty state `No results found` (tidak ada baris log untuk `Race Child {runId}-185`)
39. Sesi A: tutup Modal Changelog

### TC-FA-CAT-513: Edit dan Delete bersamaan pada kategori sama (pasangan Edit-vs-Delete)

40. Sesi A: klik node `Race Root {runId}-185` di sidebar
41. Sesi A: klik elipsis (⋯) pada baris `Race Del {runId}-185` > `Edit`
42. Tunggu aksi selesai (popup Edit Sesi A terbuka dengan data terisi)
43. Pelaku kedua (sesi API) menghapus `Race Del {runId}-185` hingga penghapusan tersimpan
44. Sesi A: klik `[Save]`
45. Sesi A: verifikasi toast netral `This category is no longer available.`
46. Sesi A: buka Modal Changelog
47. Sesi A: ketik Search `Race Del {runId}-185`, tekan Enter
48. Sesi A: verifikasi baris Action `Delete` untuk `Race Del {runId}-185` (dari pelaku kedua) tampil
49. Sesi A: verifikasi tidak ada baris Action `Edit` untuk `Race Del {runId}-185`
50. Sesi A: tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-631, TC-512, dan TC-513 ada di spec ini; TC-205 dan TC-578 ada di spec 059.
- Kelas c (multi-konteks). Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01) dan Modal Changelog dipakai untuk asersi log. Ketiga blok berkelas sama (race dua sesi), memakai data milik sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Penyesuaian data (S-06, S-12): TC memakai kategori Pre-setup #20 (`Furniture`, `Tools`, `Vehicle`); spec memakai node milik spec bersuffix `{runId}-185` sebagai anak `Race Root`. Kode `RCODE3` dipertahankan dari TC-631.
- Hanya TC-631 memakai Sesi B sebagai objek asersi (konteks UI kedua). Pada TC-512 dan TC-513 pelaku kedua hanya memicu penghapusan, sehingga memakai sesi API (langkah pemicu ditulis "... hingga ... tersimpan", R-20).
- P-1: asersi "tidak ada kategori baru dan tidak ada log" TC-512 serta "tidak ada log tambahan" TC-513 ditulis di spec ini dan bukan di spec absence, karena kondisi "parent atau node dihapus pihak lain saat popup terbuka" dibangun berurutan oleh langkah sebelumnya dan tidak dapat dibangun ulang tanpa biaya besar di spec lain. Anchor positif: baris `Delete` dari pelaku kedua pada TC-513 (langkah 48) dan toast netral serta empty state `No results found` hasil Search pada TC-512; nama bersuffix memberi baseline nol (S-12).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): membuka Sesi B dan memilih node `Race Root`; menunggu aksi selesai sebelum pihak kedua bertindak; menutup popup dirty Sesi B lewat `✕` dan `[Leave]` (S-08); memuat ulang Sesi B dan memilih node `Race Root`; mengosongkan TreeSearchInput; membuka, Search, dan menutup Modal Changelog.
- Temuan untuk QA:
  - TC-631, TC-512, dan TC-513 berlabel "Manual Only (d) dua sesi paralel"; spec menuliskannya sebagai spec otomasi (TC-631 dengan dua konteks browser, dua lainnya dengan pelaku kedua lewat sesi API).
  - TC-512 langkah 2 tidak menyebut cara membuka popup New Subcategory untuk node yang dipilih di sidebar; spec mengikuti redaksi TC.
  - TC-513 menekan `[Save]` tanpa mengubah nilai; hasil yang diharapkan (toast netral 404) bergantung pada server memeriksa keberadaan node sebelum Zero-Delta. TC tidak menyatakan precondition ini.
  - TC-631 Expected b menyebut Code `Tools` tidak berubah; spec membaca baris saudara (`Race Code B`) sesudah memuat ulang Sesi B.
  - Pre-setup #1 menyebut dua sesi tanpa akun kedua; kemampuan dua sesi web pada akun yang sama perlu dikonfirmasi tim FE/BE.
