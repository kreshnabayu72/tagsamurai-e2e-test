---
id: TC-FA-CAT-E2E-069-delete-diblok-in-use-d-07-asset-name-menunjuk-saat-dialog
title: "Delete Diblok In-Use (D-07): Bentuk Jamak dan Tunggal, Descendant, Node Excess, dan Asset Name Menunjuk Saat Dialog"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-220
  - TC-FA-CAT-221
  - TC-FA-CAT-222
  - TC-FA-CAT-226
  - TC-FA-CAT-233
  - TC-FA-CAT-228
coverage:
  web: automated
---

# Delete Diblok In-Use (D-07): Bentuk Jamak dan Tunggal, Descendant, Node Excess, dan Asset Name Menunjuk Saat Dialog

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang di-mock.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Categories dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-228): Total Control (Pre-setup #1) client CatExcess (Pre-setup #31) dengan `{namaCompany}` client CatExcess, password `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua TC-233 (membuat Asset Name yang menunjuk `Vehicle`): Total Control (Pre-setup #1) lewat sesi API aktor (butir hook `suite.md`; kemampuan membuat Asset Name lewat API disediakan tim FE/BE, tanpa endpoint karangan).
- Env var `FA_TC_PASSWORD` (nama usulan mengikuti `<APP>_<ROLE>_PASSWORD`) didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup yang dibaca dan tidak diubah (aksi Delete pada baris ini selalu diblokir guard In-Use sehingga data dan Last Updated tidak berubah, S-06): CatMain (#20) kategori `Electronics` (internal), `Laptop` (leaf, ditunjuk Asset Name `Laptop Dell` dan `Laptop HP`, Pre-setup #21), dan `Furniture` (ditunjuk Asset Name `Office Chair`); CatExcess (#31) kategori Excess `Furniture` (ditunjuk Asset Name `Office Chair`).
- Data milik spec di CatMain (seed API di hook `before` lewat jalur Create resmi sehingga Changelog memuat entri Create; dihapus di hook `after` bersama Asset Name yang dibuat TC-233; disediakan tim FE). Nilai data merujuk `Fixture.settings-categories` (belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Peran | Category Name | Code | Keterangan |
  |---|---|---|---|
  | Induk uji | `Del Root {runId}-069` | `E069ROOT` | L1; dipilih di sidebar |
  | Target TC-233 | `Vehicle {runId}-069` | `E069VEH` | anak `Del Root`, leaf, belum ditunjuk Asset Name; menggantikan `Vehicle` |

- Kemampuan teknis: Modal Changelog dapat dibaca dan dicari; pemantauan respons jaringan untuk status 409 (disediakan tim FE).
- Seed, pemulihan, flag Guided Tooltip, dan sesi API aktor mengikuti butir hook `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-220: Delete diblok D-07 bentuk jamak saat node ditunjuk dua Asset Name

1. Klik node `Electronics` di sidebar
2. Klik elipsis (⋯) pada baris `Laptop` > `Delete`
3. Verifikasi dialog tampil dengan Title `Cannot Delete Category`, bullet `Laptop`, body `This category (or one of its subcategories) is still used by 2 Asset Name templates in Asset Master. Update Asset Master before deleting.`, dan tombol `[OK]`
4. Verifikasi tidak ada toast
5. Verifikasi tidak ada kategori yang terhapus: baris `Laptop` tetap tampil di tabel
6. Klik `[OK]`

### TC-FA-CAT-221: Delete diblok D-07 bentuk tunggal saat node ditunjuk satu Asset Name

7. Klik node `All Categories` di sidebar
8. Klik elipsis (⋯) pada baris `Furniture` > `Delete`
9. Verifikasi dialog `Cannot Delete Category` dengan bullet `Furniture`, body `This category (or one of its subcategories) is still used by 1 Asset Name template in Asset Master. Update Asset Master before deleting.`, dan tombol `[OK]`
10. Klik `[OK]`

### TC-FA-CAT-222: Delete diblok saat descendant (bukan node itu sendiri) ditunjuk Asset Name

11. Klik elipsis (⋯) pada baris `Electronics` > `Delete`
12. Verifikasi dialog D-07 (bukan D-08) `Cannot Delete Category` dengan bullet `Electronics` dan body `This category (or one of its subcategories) is still used by 2 Asset Name templates in Asset Master. Update Asset Master before deleting.` (N=2 distinct Asset Name templates dari seluruh descendant)
13. Verifikasi tidak ada node yang terhapus: baris `Electronics` tetap tampil di tabel
14. Klik `[OK]`

### TC-FA-CAT-226: Dialog blok Delete hanya ditutup lewat [OK]

15. Klik elipsis (⋯) pada baris `Furniture` > `Delete`
16. Klik backdrop di luar dialog
17. Verifikasi dialog tidak tertutup
18. Klik `[OK]`
19. Verifikasi dialog tertutup
20. Verifikasi tidak ada toast
21. Verifikasi tanpa mutasi dan seleksi: baris `Furniture` tetap tampil di tabel dan tidak ada baris tercentang

### TC-FA-CAT-233: Asset Name menunjuk node setelah dialog D-09 tampil: Confirm ditolak 409 dan dialog berubah menjadi D-07

22. Klik node `Del Root {runId}-069` di sidebar
23. Sesi A: klik elipsis (⋯) pada baris `Vehicle {runId}-069` > `Delete` sampai dialog D-09 tampil
24. Tunggu aksi selesai (dialog D-09 tampil)
25. Sesi B (sesi API) membuat Asset Name yang menunjuk `Vehicle {runId}-069` hingga Asset Name tersimpan
26. Sesi A: klik `[Delete]` pada dialog
27. Verifikasi server me-re-check guard dalam transaksi dan menolak permintaan Delete dengan status 409
28. Verifikasi dialog berubah menjadi D-07 `Cannot Delete Category` dengan bullet `Vehicle {runId}-069` dan body `This category (or one of its subcategories) is still used by 1 Asset Name template in Asset Master. Update Asset Master before deleting.`
29. Verifikasi tidak ada toast generik
30. Verifikasi `Vehicle {runId}-069` tidak terhapus: baris tetap tampil di tabel
31. Klik `[OK]`
32. Buka Modal Changelog
33. Ketik Search `Vehicle {runId}-069`, tekan Enter
34. Verifikasi baris Action `Create` untuk `Vehicle {runId}-069` tampil
35. Verifikasi tidak ada baris Action `Delete` untuk `Vehicle {runId}-069`
36. Tutup Modal Changelog

### TC-FA-CAT-228: Node Excess yang ditunjuk Asset Name tetap diblok D-07

37. Logout
38. Login sebagai Total Control client CatExcess (Pre-setup #31)
39. Buka Fixed Asset > Settings > Categories
40. Klik elipsis (⋯) pada baris `Furniture` > `Delete`
41. Verifikasi dialog D-07 `Cannot Delete Category` dengan `1 Asset Name template` tampil
42. Verifikasi node `Furniture` tetap ada di tabel
43. Klik `[OK]`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-220, TC-221, TC-222, TC-226, TC-233, dan TC-228 ada di spec ini.
- Spec ini melewati sekitar 35 langkah karena Expected ditulis per klausa (S-01), ada ganti akun ke client CatExcess, dan asersi log memakai Modal Changelog. Keenam blok berkelas fungsional yang sama (guard In-Use), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-228 di akhir karena memakai client lain (ganti akun, S-07, S-10); TC-233 sebelum TC-228 karena membuat dan membersihkan data milik spec.
- Penyesuaian data (S-06, S-12): TC-220, TC-221, TC-222, TC-226, dan TC-228 memakai baris Pre-setup yang selalu diblokir guard (tidak diubah); TC-233 memakai `Vehicle` milik spec bersuffix `{runId}-069` karena Asset Name baru menunjuk node itu.
- P-1: asersi "tidak ada log" TC-233 ditulis di spec ini dan bukan di spec absence, karena kondisi (dialog D-09 yang berubah menjadi D-07 akibat Asset Name baru) dibangun berurutan oleh langkah sebelumnya dan tidak dapat dibangun ulang tanpa biaya besar di spec lain. Anchor positif: baris `Create` pada Changelog; nama bersuffix memberi baseline nol untuk baris `Delete`.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): memilih node di sidebar; klik backdrop sebagai pemicu asersi; menunggu aksi selesai sebelum sesi API bertindak; membuka, Search, dan menutup Modal Changelog; ganti akun ke client CatExcess (Logout, Login, buka halaman).
- Temuan untuk QA:
  - TC-233 tidak menyebut bagaimana Asset Name dibuat oleh Sesi B; spec menulisnya sebagai kemampuan sesi API yang disediakan tim FE/BE tanpa endpoint.
  - TC-233 Expected a ("Server me-re-check guard dalam transaksi dan menolak (409)") tidak teramati langsung di UI; spec mengasersi status 409 lewat pemantauan respons jaringan.
  - TC-233 Expected b ("tidak ada log") tidak menyebut surface; spec memakai Modal Changelog dan mengasumsikan seeding Create menulis entri Create (anchor).
  - TC-226 menyebut "tanpa mutasi, seleksi, atau toast"; "seleksi" ditafsirkan sebagai tidak ada baris tercentang di tabel.
  - TC-222 menyebut N=2 distinct Asset Name templates dari seluruh descendant; Pre-setup #21 hanya menyebut `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`.
  - TC-228 Post Condition tidak ada; Expected hanya menyebut "1 Asset Name template" tanpa teks lengkap dialog D-07, sehingga spec mengasersi dialog dengan penyebutan itu.
