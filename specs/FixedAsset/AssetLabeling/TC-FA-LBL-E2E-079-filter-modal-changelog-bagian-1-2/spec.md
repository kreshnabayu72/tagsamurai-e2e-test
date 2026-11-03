---
id: TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2
title: "Filter Modal Changelog (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-296
  - TC-FA-LBL-297
  - TC-FA-LBL-298
  - TC-FA-LBL-299
  - TC-FA-LBL-300
coverage:
  web: automated
---

# Filter Modal Changelog (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K). Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum mengamati baris seed, dan asersi dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12, S-14).
- State global yang diubah: tidak ada. Tidak ada data dinamis; spec tidak membuat atau mengubah data backend. Filter Panel dibersihkan di akhir spec.

## Test Steps

### Membuka Modal Changelog

1. Klik icon Changelog di Table Tools

### TC-FA-LBL-296: Screening Filter Panel Modal Changelog

2. Klik icon Filter di toolbar modal
3. Verifikasi panel muncul di bawah toolbar modal
4. Verifikasi Filter Panel memuat field `Date` (date range, placeholder `Select date`), `Action` (multi-select, `All actions`), `Label Name` (multi-select, `All labels`), `Field` (multi-select, `All fields`), dan `Modified By` (multi-select, `All users`)
5. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan) tampil
6. Verifikasi belum ada filter ter-Apply: semua field menampilkan placeholder `Select date`, `All actions`, `All labels`, `All fields`, dan `All users`

### TC-FA-LBL-297: Isi opsi dropdown filter Changelog bersumber dari baris log, termasuk label yang sudah dihapus

7. Buka dropdown `Action`
8. Verifikasi opsi `Action`: `Create`, `Edit`, `Delete`
9. Buka dropdown `Label Name`
10. Verifikasi opsi `Label Name` memuat `Audit Ready`, `Executive Asset`, `Finance Department`, `High Priority`, `Old Tag` (label yang sudah dihapus tetap muncul karena ada di log); opsi dari entri TC lain boleh ada
11. Buka dropdown `Field`
12. Verifikasi opsi `Field`: `Label Name`, `Color`
13. Buka dropdown `Modified By`
14. Verifikasi opsi `Modified By` memuat `David K`, `Michael W`, `Sarah J`
15. Verifikasi tidak ada opsi untuk label atau pengguna tanpa entri log

### TC-FA-LBL-298: Filter Date Changelog: rentang inklusif

16. Pilih rentang `14 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
17. Verifikasi tabel memuat tepat empat baris: dua `High Priority` dan dua `Finance Department`
18. Verifikasi baris 12 Sep, 10 Sep, dan 08 Sep tidak tampil

### TC-FA-LBL-299: Filter multi-select Changelog kelas Action, Label Name, Field, Modified By

19. Klik `[Clear Field]`
20. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Action` = `Create` lalu klik `[Apply]`
21. Verifikasi pada hasil Filter Date, tabel memuat empat baris seed Create
22. Klik `[Clear Field]`
23. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Label Name` = `Audit Ready` dan `Executive Asset` lalu klik `[Apply]`
24. Verifikasi tabel memuat tepat dua baris (OR): `Create Audit Ready` dan `Create Executive Asset`
25. Klik `[Clear Field]`
26. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Field` = `Color` lalu klik `[Apply]`
27. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Edit High Priority`
28. Klik `[Clear Field]`
29. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` dan `Modified By` = `Michael W` lalu klik `[Apply]`
30. Verifikasi pada hasil Filter Date, tabel memuat hanya satu baris: `Create Executive Asset`

### TC-FA-LBL-300: Kombinasi Action dan Modified By berlogika AND di Changelog

31. Klik `[Clear Field]`
32. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026`, `Action` = `Create` dan `Modified By` = `Sarah J` lalu klik `[Apply]`
33. Verifikasi pada hasil Filter Date, tabel memuat dua baris seed: `Create High Priority` dan `Create Audit Ready`
34. Klik `[Clear Field]`
35. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal dan Filter Panel dibuka sekali di awal; tiap TC multi-select dimulai dengan `[Clear Field]` supaya filter TC sebelumnya tidak terbawa. Pada TC-FA-LBL-299 dan TC-FA-LBL-300 rentang Filter Date seed (langkah TC) dipilih ulang bersama filter lain sesudah `[Clear Field]`, sehingga asersi dinilai atas hasil Filter Date (tujuh baris seed).
- Langkah penghubung (tanpa awalan `Verifikasi`): `[Clear Field]` antar blok Filter dan menutup Modal Changelog di akhir spec.
- Pasangan TC filter bagian 2 (TC-FA-LBL-301 sampai TC-FA-LBL-304) ada di spec 080.
- Temuan untuk QA:
  - TC-FA-LBL-299 mengasumsikan Filter Panel tetap terbuka sesudah `[Apply]` ("Bersihkan, pilih ...") sedangkan TC-FA-LBL-301 dan TC-FA-LBL-302 membuka panel dengan klik icon Filter. TC tidak menyatakan apakah panel menutup sesudah `[Apply]`; spec ini mengikuti TC-FA-LBL-299 untuk blok multi-select.
  - Kata `Bersihkan` pada TC-FA-LBL-299 dan TC-FA-LBL-300 diartikan `[Clear Field]` (tombol kiri panel); TC tidak menyebut tombol itu secara eksplisit.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
