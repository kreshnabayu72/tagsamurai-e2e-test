---
id: TC-FA-TDC-E2E-203-fiscal-year-start-terkunci-oleh-versi-bertanggal
title: "Preferences: Fiscal Year Start Terkunci oleh Versi Bertanggal dan Tidak Terkunci oleh Versi Pertama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-749
  - TC-FA-TDC-750
  - TC-FA-TDC-751
  - TC-FA-TDC-752
coverage:
  web: automated
---

# Preferences: Fiscal Year Start Terkunci oleh Versi Bertanggal dan Tidak Terkunci oleh Versi Pertama

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) diperlukan TC-752 (pilihan Effective From `Jan 2027`); jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Data Pre-setup (disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, kunci `exampleData`, fixture belum ada): sembilan class Example Data PRD dengan tabel dalam satu halaman (9 baris, 10 baris per halaman) sehingga baris target tidak dicari lewat Search. Kondisi tiap blok, dibentuk lewat seeding di langkah penghubung (langkah 1, 15, 24):
  - TC-750 dan TC-751: seluruh class hanya memiliki versi pertama tanpa Effective From (NB-2 Useful Life 8, Straight Line Rate 12.5%, Declining Balance Rate 25%); Fiscal Year Start `January`, semua periode akuntansi Open, belum ada penyusutan diposting.
  - TC-749: NB-2 memiliki versi kedua dengan Effective From Jan 2027 (Scheduled); Fiscal Year Start `January`, semua periode akuntansi Open.
  - TC-752: NB-4 hanya memiliki versi pertama tanpa Effective From; tidak ada versi bertanggal di class lain; Fiscal Year Start `January`.
  - Class Code dibatasi 15 karakter sehingga kode memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Data uji: TC-750 dan TC-751 mengubah Fiscal Year Start ke `July`; TC-749 dan TC-752 mencoba mengubahnya ke `April`; TC-752 mengubah Useful Life NB-4 menjadi 10 dengan Effective From `Jan 2027`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class, versi, periode akuntansi Open, dan Fiscal Year Start lewat API; pemulihan data lewat API.
- State global yang diubah: Fiscal Year Start (July pada blok TC-750, dikembalikan ke January lewat seeding langkah 15 dan 24), versi NB-2 dan NB-4, serta jam server dan browser. Dipulihkan di hook `after` lewat seeding ulang Fiscal Year Start `January` dan class Example Data, serta pemulihan jam.

## Test Steps

### TC-FA-TDC-750 dan TC-FA-TDC-751: versi pertama tanpa Effective From tidak menghalangi perubahan Fiscal Year Start

1. Seed seluruh class hanya dengan versi pertama tanpa Effective From dan Fiscal Year Start `January` lewat seeding API
2. Buka Settings > Accounting > Preferences
3. Ubah Fiscal Year Start dari `January` menjadi `July`
4. Klik `[Save changes]`
5. Klik `[Save]` pada dialog konfirmasi Save Changes hingga perubahan berhasil tersimpan
6. Verifikasi Fiscal Year Start tersimpan `July`
7. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tidak tampil
8. Buka Settings > Accounting > Tax Depreciation Class
9. Verifikasi baris tabel NB-2 tetap: Useful Life (years) "8", Straight Line Rate "12.5%", Declining Balance Rate "25%", Effective From "—"
10. Klik link Class Code NB-2
11. Klik tautan View versions
12. Verifikasi modal Versions NB-2 tetap memuat satu versi berstatus "Current" tanpa Effective From dengan Useful Life 8
13. Tutup modal Versions lewat `[×]` pada header modal
14. Klik `[×]` pada header Drawer Edit

### TC-FA-TDC-749: Fiscal Year Start tidak dapat diubah selama ada versi Scheduled

15. Seed NB-2 dengan versi kedua Scheduled Effective From Jan 2027 dan Fiscal Year Start `January` lewat seeding API
16. Buka Settings > Accounting > Preferences
17. Ubah Fiscal Year Start dari `January` menjadi `April`
18. Klik `[Save changes]`
19. Klik `[Save]` pada dialog konfirmasi Save Changes
20. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
21. Kembalikan field Fiscal Year Start ke `January`
22. Muat ulang halaman
23. Verifikasi Fiscal Year Start tetap `January`

### TC-FA-TDC-752: Fiscal Year Start terkunci setelah versi bertanggal pertama terbentuk lewat Apply

24. Seed seluruh class hanya dengan versi pertama tanpa Effective From dan Fiscal Year Start `January` lewat seeding API
25. Buka Settings > Accounting > Tax Depreciation Class
26. Klik link Class Code NB-4
27. Ubah Useful Life menjadi `10`
28. Klik `[Save]`
29. Pilih Effective From `Jan 2027`
30. Klik `[Apply]` hingga versi berhasil tersimpan
31. Klik link Class Code NB-4
32. Klik tautan View versions
33. Verifikasi modal Versions NB-4 memuat versi baru berstatus "Scheduled" dengan Effective From `Jan 2027`
34. Tutup modal Versions lewat `[×]` pada header modal
35. Klik `[×]` pada header Drawer Edit
36. Buka Settings > Accounting > Preferences
37. Ubah Fiscal Year Start dari `January` menjadi `April`
38. Klik `[Save changes]`
39. Klik `[Save]` pada dialog konfirmasi Save Changes
40. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
41. Verifikasi nilai Fiscal Year Start tetap `January`

## Notes

- Urutan TC di spec: 750 dan 751 (digabung), 749, 752. TC-750 dan TC-751 memiliki langkah 1 sampai 3 yang identik (ubah Fiscal Year Start ke July, `[Save changes]`, `[Save]`) dan precondition yang sama, sehingga dijalankan sekali pada langkah 3 sampai 5; langkah 8 sampai 12 adalah langkah 4 TC-751 dan Expected b dan c. Expected b TC-750 dan Expected a TC-751 ("Fiscal Year Start tersimpan July") dicakup langkah 6; Expected a TC-750 (caption tidak tampil) dicakup langkah 7.
- Urutan langkah 6 sebelum langkah 7: kondisi tersimpan `July` menjadi anchor positif sebelum asersi absence caption (8b.2).
- Langkah 22 dan 23 membuktikan "tetap January setelah halaman dimuat ulang" (Expected b TC-749); langkah 21 mengembalikan field ke nilai tersimpan sebelum muat ulang (S-08, S-09).
- Langkah penghubung (S-03): langkah 1, 15, 24 (seeding, tanpa asersi), langkah 2, 8, 16, 25, 36 (berpindah halaman), langkah 13, 14, 34, 35 (menutup modal Versions dan Drawer yang tidak diubah), langkah 21 (pemulihan field Fiscal Year Start yang dirty sebelum muat ulang, S-08 dan S-09), langkah 31 sampai 34 pada TC-752 (membuktikan versi Scheduled terbentuk, Expected a TC-752; TC tidak menyebut cara membuktikannya, lihat Temuan).
- Langkah 41 pada TC-752 memecah Expected b ("caption tampil dan nilai tetap January") menjadi dua `Verifikasi` (S-01).
- Alasan di atas ~35 langkah: semua blok satu topik (penguncian Fiscal Year Start oleh versi bertanggal), tiap blok berdiri sendiri dengan kondisi data di Prerequisites, dan langkah panjangnya adalah seeding ulang serta perpindahan antara Preferences dan Tax Depreciation Class; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-753, 754, 755, 924, dan 925 (Fiscal Year Start terbuka kembali dan pilihan Effective From) ada di spec 204.
- Temuan untuk QA:
  - TC-749 Expected b menyebut "tetap January setelah halaman dimuat ulang"; spec mengembalikan field dirty ke January sebelum memuat ulang (S-08) sehingga nilai yang dibaca berasal dari server.
  - TC-752 Expected a ("versi baru Scheduled terbentuk") tidak menyebut cara mengamatinya; spec membuka modal Versions (langkah 31 sampai 33) dan mengasersi status "Scheduled" dengan Effective From `Jan 2027`.
  - TC-749, 750, 752 tidak menyebut label tab atau menu Preferences selain jalur "Settings > Accounting > Preferences"; spec mengikuti jalur itu.
  - TC-751 Post Condition tidak diasersi di luar Expected.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang data di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - Email akun Total Control tidak tertulis di TC.
