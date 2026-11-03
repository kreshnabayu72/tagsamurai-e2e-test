---
id: TC-FA-FAAM-E2E-055-generator-code-pada-edit
title: "Generator Code pada Edit: Code Dikosongkan, Nama Akhir, dan Cek Keunikan Mengecualikan Diri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-338
  - TC-FA-FAAM-339
  - TC-FA-FAAM-340
  - TC-FA-FAAM-341
coverage:
  web: automated
---

# Generator Code pada Edit: Code Dikosongkan, Nama Akhir, dan Cek Keunikan Mengecualikan Diri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup #13e: Asset Name `Edit Code Item` ber-Code `ECI` (Total Asset 0) dipakai TC-FA-FAAM-339 (Save ditolak, tidak mengubah data) dan TC-FA-FAAM-340 (Save tanpa perubahan nilai Code; Last Updated baris ini dapat berubah, efeknya dicatat dan tidak dipulihkan).
- Data Dinamis (suffix `{runId}-055` pada nama, seed API di hook `before`): `Edit Code Item 338 {runId}-055` (Code `ECI338`) dan `Edit Code Item 341 {runId}-055` (Code `ECI341`), salinan Pre-setup #13e yang disimpan-ubah spec ini. Nama hasil rename `Another Name 341 {runId}-055` memakai suffix. Hanya `Renamed Gadget Pro` literal tanpa suffix karena Code hasil generator (`RGP`) diturunkan dari nama baru itu; record bernama `Renamed Gadget Pro` sisa run sebelumnya dihapus lewat API di hook `before`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog sebelum aksi sebagai baseline dengan filter Search `Renamed Gadget Pro`, sama dengan filter pembandingan sesudah Save (langkah 36), agar jumlah dibandingkan pada cakupan yang sama; asersi memakai selisih terhadap baseline (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Renamed Gadget Pro` (hasil ubah `Edit Code Item 338 {runId}-055`) dan `Another Name 341 {runId}-055` (hasil ubah `Edit Code Item 341 {runId}-055`); Pre-setup #13e `Edit Code Item` tidak dihapus.

## Test Steps

### TC-FA-FAAM-339: Edit dengan Code kosong dan nama baru gagal validasi menolak seluruh submit

1. Ketik Search `Edit Code Item`, tekan Enter
2. Buka Edit `Edit Code Item` (klik `⋯` pada baris bernama persis `Edit Code Item`, lalu `Edit`)
3. Ubah Asset Name menjadi nama yang sudah dipakai `Dell Latitude` dan kosongkan Code
4. Klik `[Save]`
5. Verifikasi Seluruh submit ditolak dengan error inline `Asset name already exists`
6. Klik `[✕]`
7. Verifikasi dialog `Unsaved Changes` tampil
8. Klik `[Leave]`
9. Buka Popup Detail `Edit Code Item` dari tabel
10. Verifikasi Code tetap `ECI`
11. Tutup Popup Detail

### TC-FA-FAAM-340: Cek keunikan kandidat pada Edit mengecualikan record yang sedang diedit

12. Buka Edit `Edit Code Item`
13. Kosongkan Code tanpa mengubah nama
14. Klik `[Save]`
15. Verifikasi Kandidat `ECI` tidak dianggap bentrok dengan dirinya: toast `Success, asset name has been updated.` tampil tanpa error `Code already exists`
16. Buka Popup Detail `Edit Code Item` dari tabel
17. Verifikasi Save tidak menambah suffix: Code tetap `ECI`
18. Tutup Popup Detail

### TC-FA-FAAM-341: Code yang sudah ada tidak berubah saat rename tanpa mengosongkan Code

19. Ganti isi kotak search dengan `Edit Code Item 341 {runId}-055`, tekan Enter
20. Buka Edit `Edit Code Item 341 {runId}-055`, lalu ubah hanya Asset Name menjadi `Another Name 341 {runId}-055`
21. Klik `[Save]`
22. Ganti isi kotak search dengan `Another Name 341 {runId}-055`, tekan Enter
23. Buka Popup Detail `Another Name 341 {runId}-055` dari tabel
24. Verifikasi Code tetap `ECI341`
25. Tutup Popup Detail

### TC-FA-FAAM-338: Edit dengan Code dikosongkan memakai nama akhir pada submit yang sama

26. Ganti isi kotak search dengan `Edit Code Item 338 {runId}-055`, tekan Enter
27. Buka Changelog (icon Changelog), ketik Search `Renamed Gadget Pro`, tekan Enter, catat jumlah entri hasil filter sebagai baseline, lalu tutup Modal Changelog
28. Buka Edit `Edit Code Item 338 {runId}-055`
29. Ubah Asset Name menjadi `Renamed Gadget Pro` dan kosongkan Code
30. Klik `[Save]`
31. Ganti isi kotak search dengan `Renamed Gadget Pro`, tekan Enter
32. Buka Popup Detail `Renamed Gadget Pro` dari tabel
33. Verifikasi Code baru `RGP` (dari nama baru) menggantikan Code lama `ECI338`
34. Tutup Popup Detail, lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
35. Buka Changelog
36. Ketik Search `Renamed Gadget Pro` di Modal Changelog, tekan Enter
37. Verifikasi jumlah entri Changelog `Renamed Gadget Pro` bertambah dibanding baseline pada langkah 27
38. Verifikasi entri Changelog baru memuat baris Edit dengan Field `Code`, Old `ECI338`, dan New `RGP`
39. Tutup Modal Changelog

## Notes

- Urutan TC dalam spec (S-10): validasi ditolak (TC-FA-FAAM-339) lebih dahulu, lalu Edit sukses (TC-FA-FAAM-340, 341, 338); TC-FA-FAAM-338 terakhir karena menulis entri Changelog yang diperiksa di akhir spec.
- TC-FA-FAAM-339 "Code tetap `ECI`" diamati lewat Popup Detail sesudah form ditutup dengan `[Leave]` (S-08: `[✕]`, Verifikasi dialog `Unsaved Changes` pada langkah 7, `[Leave]`).
- Langkah penghubung (tanpa `Verifikasi`): Search nama (R-16), penutupan Popup Detail, Search, pembacaan baseline Changelog beserta penutupannya (langkah 27), dan Modal Changelog. Search pertama pada blok TC-FA-FAAM-341 (langkah 19) menemukan baris `Edit Code Item 341 {runId}-055` di antara baris `Edit Code Item` lain; kotak Search sudah berisi teks sehingga ditulis "ganti isi kotak search" (langkah 19, 22, 26, 31).
- Alasan melewati sekitar 35 langkah (39 langkah): empat blok satu topik (Generator Code pada Edit) yang berbagi data Pre-setup #13e dan halaman yang sama; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-FAAM-339 dan 340 memakai Pre-setup #13e `Edit Code Item` langsung, sedangkan salinan seed hanya disediakan untuk TC-FA-FAAM-338 dan 341. Save pada TC-FA-FAAM-340 dapat mengubah Last Updated baris Pre-setup bersama (S-06).
  - Expected a TC-FA-FAAM-340 ("Kandidat `ECI` tidak dianggap bentrok dengan dirinya") tidak punya padanan UI langsung; spec mengasersi Save berhasil tanpa error bentrok Code.
  - Expected TC-FA-FAAM-338 menyebut Changelog entri teratas; spec mencari entri lewat Search nama karena Changelog adalah audit trail yang tumbuh (S-14), dan mengasersi pertambahan jumlah entri terhadap baseline langkah 27 (langkah 37) sebelum isi entri (langkah 38). Jumlah pertambahan tidak ditetapkan: satu Save yang mengganti nama dan mengosongkan Code dapat menulis lebih dari satu baris (Field `Asset Name` dan `Code`), dan TC-FA-FAAM-338 tidak menyebut jumlah entri.
