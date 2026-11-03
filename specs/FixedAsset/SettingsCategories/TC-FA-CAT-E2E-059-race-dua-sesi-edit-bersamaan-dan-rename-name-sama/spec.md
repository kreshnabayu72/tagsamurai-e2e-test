---
id: TC-FA-CAT-E2E-059-race-dua-sesi-edit-bersamaan-dan-rename-name-sama
title: "Race Dua Sesi UI: Edit Bersamaan pada Record Sama dan Rename ke Name yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-205
  - TC-FA-CAT-578
coverage:
  web: automated
---

# Race Dua Sesi UI: Edit Bersamaan pada Record Sama dan Rename ke Name yang Sama

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor: Total Control (Pre-setup #1, dua sesi UI) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Sesi A: login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite. Sesi B: konteks browser kedua dengan akun yang sama, dibuka dan login lewat langkah 1 sampai 3, ditutup di hook `after`. Hook `after` juga mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: CatMain (#20) hanya dibaca; baris seed tidak diubah.
- Data milik spec (seed API di hook `before` lewat jalur Create resmi, dihapus di hook `after`; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Race Root {runId}-059` | `E059ROOT` | L1; dipilih di sidebar kedua sesi |
  | Target TC-205 | `Furniture {runId}-059` | `E059FURN` | anak `Race Root`, leaf, Description kosong; menggantikan `Furniture` |
  | Bersaudara TC-578 | `Race Name A {runId}-059` | `E059NA` | anak `Race Root`; menggantikan `Furniture` |
  | Bersaudara TC-578 | `Race Name B {runId}-059` | `E059NB` | anak `Race Root`, saudara `Race Name A`; menggantikan `Tools` |

- Kemampuan teknis: dua konteks browser berjalan bersamaan dengan urutan klik terkendali; pemantauan respons jaringan untuk status 422 (disediakan tim FE); Modal Changelog dapat dibaca dan dicari.
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### Pembukaan Sesi B

1. Sesi B: buka konteks browser kedua dan login sebagai Total Control client CatMain
2. Sesi B: buka Fixed Asset > Settings > Categories
3. Sesi B: klik node `Race Root {runId}-059` di sidebar
4. Sesi A: klik node `Race Root {runId}-059` di sidebar

### TC-FA-CAT-205: Dua sesi mengedit record sama: Save terakhir menang tanpa dialog konflik versi

5. Sesi A: klik elipsis (⋯) pada baris `Furniture {runId}-059` > `Edit`
6. Tunggu aksi selesai (popup Edit Sesi A terbuka dengan data terisi)
7. Sesi B: klik elipsis (⋯) pada baris `Furniture {runId}-059` > `Edit`
8. Sesi A: ubah Description menjadi `Dari A`
9. Sesi A: klik `[Save]`
10. Sesi A: verifikasi toast `Success, category has been updated.`
11. Sesi A: verifikasi tidak ada dialog konflik versi
12. Sesi B: ubah Description menjadi `Dari B`
13. Sesi B: klik `[Save]`
14. Sesi B: verifikasi toast `Success, category has been updated.`
15. Sesi B: verifikasi tidak ada dialog konflik versi
16. Sesi B: klik elipsis (⋯) pada baris `Furniture {runId}-059` > `Edit`
17. Sesi B: verifikasi Description tampil `Dari B`
18. Sesi B: klik `✕` pada header popup
19. Sesi A: buka Modal Changelog
20. Sesi A: ketik Search `Furniture {runId}-059`, tekan Enter
21. Sesi A: verifikasi baris Edit Field `Description` Old Value `—` New Value `Dari A` tampil
22. Sesi A: verifikasi baris Edit Field `Description` Old Value `Dari A` New Value `Dari B` tampil sebagai baris terpisah
23. Sesi A: tutup Modal Changelog

### TC-FA-CAT-578: Dua aktor me-rename kategori berbeda ke Name yang sama bersamaan: Save kedua ditolak 422

24. Sesi A: klik elipsis (⋯) pada baris `Race Name A {runId}-059` > `Edit`
25. Sesi A: ubah Category Name menjadi `Shared Name {runId}-059`
26. Tunggu aksi selesai (popup Edit Sesi A terisi)
27. Sesi B: klik elipsis (⋯) pada baris `Race Name B {runId}-059` > `Edit`
28. Sesi B: ubah Category Name menjadi `Shared Name {runId}-059`
29. Sesi A: klik `[Save]`
30. Sesi A: verifikasi toast `Success, category has been updated.`
31. Sesi A: verifikasi baris `Race Name A {runId}-059` menjadi `Shared Name {runId}-059`
32. Sesi B: klik `[Save]`
33. Sesi B: verifikasi Save ditolak server (422) dengan pesan unik Name `Category name already exists`
34. Sesi B: verifikasi popup Edit tetap terbuka
35. Sesi B: verifikasi input Category Name `Shared Name {runId}-059` dipertahankan
36. Sesi B: klik `✕` pada header popup
37. Sesi B: klik `[Leave]`
38. Sesi B: muat ulang halaman
39. Sesi B: klik node `Race Root {runId}-059` di sidebar
40. Sesi B: verifikasi baris `Race Name B {runId}-059` tidak berubah
41. Sesi B: verifikasi hanya satu baris bernama `Shared Name {runId}-059` di tabel
42. Sesi A: buka Modal Changelog
43. Sesi A: ketik Search `Shared Name {runId}-059`, tekan Enter
44. Sesi A: verifikasi hanya satu baris Edit Field `Category Name` Old Value `Race Name A {runId}-059` New Value `Shared Name {runId}-059` tampil
45. Sesi A: verifikasi tidak ada baris dari Sesi B (tidak ada baris dengan Old Value `Race Name B {runId}-059`)
46. Sesi A: tutup Modal Changelog

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-205 dan TC-578 ada di spec ini; TC-631, TC-512, dan TC-513 ada di spec 185.
- Kelas c (multi-konteks): kedua sesi UI menjadi objek asersi. Spec ini melewati sekitar 35 langkah karena dua sesi diasersi bergantian dan Expected ditulis per klausa (S-01); kedua blok memakai satu jenis harness (dua sesi UI), data milik sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Penyesuaian data (S-06, S-12): TC memakai kategori L1 Pre-setup #20 (`Furniture`, `Tools`); spec memakai node milik spec bersuffix `{runId}-059` sebagai anak `Race Root`. Aturan keunikan Name berlaku per parent (V-04), sehingga dua saudara di bawah `Race Root` setara dengan dua L1 bersaudara; Expected "hanya satu kategori L1 bernama `Shared Name`" ditulis sebagai satu baris `Shared Name {runId}-059` di tabel anak `Race Root`.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): membuka Sesi B dan memilih node `Race Root` di sidebar kedua sesi; menunggu aksi selesai sebelum Sesi B bertindak; menutup popup dirty Sesi B lewat `✕` dan `[Leave]` (S-08); memuat ulang Sesi B dan memilih node `Race Root` agar tabel Sesi B menampilkan keadaan terkini; membuka, Search, dan menutup Modal Changelog. Search memakai nama bersuffix sehingga baseline nol (S-12).
- Temuan untuk QA:
  - Pre-setup #1 menyebut akun Total Control "dua sesi untuk skenario paralel" tanpa akun kedua; spec memakai akun yang sama pada konteks browser kedua. Kemampuan dua sesi web pada akun yang sama (batas sesi web) perlu dikonfirmasi tim FE/BE.
  - TC-205 dan TC-578 berlabel "Manual Only (d) dua sesi paralel"; spec menuliskannya sebagai spec otomasi dengan dua konteks browser.
  - TC-205 Expected b ("Nilai akhir Description `Dari B`") tidak memberi langkah observasi; spec membuka ulang Edit di Sesi B untuk membaca nilai tersimpan.
  - TC-578 Expected b menyebut `Tools` tidak berubah; spec membaca baris saudara (`Race Name B`) sesudah memuat ulang Sesi B karena tabel Sesi B tidak di-refresh otomatis.
