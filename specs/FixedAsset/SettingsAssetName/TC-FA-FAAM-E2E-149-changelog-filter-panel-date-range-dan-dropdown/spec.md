---
id: TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown
title: "Modal Changelog: Filter Panel, Date Range Inklusif, Dropdown DISTINCT, dan Kombinasi dengan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-474
  - TC-FA-FAAM-475
  - TC-FA-FAAM-476
  - TC-FA-FAAM-477
  - TC-FA-FAAM-478
  - TC-FA-FAAM-479
coverage:
  web: automated
---

# Modal Changelog: Filter Panel, Date Range Inklusif, Dropdown DISTINCT, dan Kombinasi dengan Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) pada Asset Name `Dell Latitude` berisi entri Create, Edit, dan Delete oleh Sarah Johnson, David Kurniawan, dan Michael Wijaya, termasuk entri Edit Field `Code` dan entri `Dell Latitude` pada satu hari seed (`changelogSeed.dellLatitudeDate`). Jumlah total entri tidak diasersi sebagai angka absolut (S-12).
- Kemampuan teknis: membaca daftar Field dan daftar user (Modified By) yang tercatat di Changelog, untuk membandingkan opsi dropdown DISTINCT (disediakan tim FE/BE; mekanismenya tidak disebut TC).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-474: Screening Filter Panel Modal Changelog

2. Klik icon Filter
3. Verifikasi field berurutan: `Date` `Select date`, `Action` `All actions`, `Asset Name` `All asset names`, `Field` `All fields`, `Modified By` `All users`
4. Verifikasi tombol `[Clear Field]` dan `[Apply]`

### TC-FA-FAAM-475: Filter Date range Changelog inklusif

5. Pilih rentang tanggal satu hari entri `Dell Latitude` (Start = End = `Fixture.faAssetName.changelogSeed.dellLatitudeDate`)
6. Klik `[Apply]`
7. Verifikasi sedikitnya satu baris tampil pada tabel Changelog
8. Verifikasi semua baris yang tampil bertanggal hari itu (Start = End inklusif)
9. Verifikasi format tanggal pada kolom Date dan pada input Date Filter mengikuti General Settings

### TC-FA-FAAM-476: Filter Action, Asset Name, Field berupa dropdown DISTINCT dari data Changelog

10. Klik icon Filter, lalu klik `[Clear Field]`
11. Buka dropdown Action
12. Verifikasi opsi Action hanya `Create`, `Edit`, `Delete`
13. Pilih `Edit`
14. Buka dropdown Field
15. Verifikasi opsi Field berasal dari Field yang tercatat di Changelog
16. Pilih `Code`
17. Klik `[Apply]`
18. Verifikasi sedikitnya satu baris tampil pada tabel Changelog
19. Verifikasi semua baris yang tampil ber-Action `Edit` dan Field `Code` (AND antar-field)

### TC-FA-FAAM-477: Filter Modified By Changelog

20. Klik icon Filter, lalu klik `[Clear Field]`
21. Buka dropdown Modified By
22. Verifikasi opsi Modified By hanya user yang tercatat di Changelog
23. Pilih `Sarah Johnson`
24. Klik `[Apply]`
25. Verifikasi sedikitnya satu baris tampil pada tabel Changelog
26. Verifikasi semua baris yang tampil ber-Modified By `Sarah J`

### TC-FA-FAAM-478: Alur Search lalu Filter dan Filter lalu Search pada Changelog

27. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
28. Ketik Search `Dell`, tekan Enter
29. Terapkan Filter Action `Edit`: klik icon Filter, pilih Action `Edit`, klik `[Apply]`
30. Catat baris hasil pada halaman pertama (urutan Search lalu Filter)
31. Klik `(←)` pada kotak Search, lalu klik icon Filter, klik `[Clear Field]`, dan klik `[Apply]`
32. Terapkan Filter Action `Edit`: klik icon Filter, pilih Action `Edit`, klik `[Apply]`
33. Ketik Search `Dell`, tekan Enter
34. Verifikasi baris hasil pada halaman pertama sama dengan yang dicatat pada langkah 30 (irisan sama)

### TC-FA-FAAM-479: Clear Filter dan Clear Search Changelog saling independen

35. Klik `(←)` pada kotak Search, lalu klik icon Filter, klik `[Clear Field]`, dan klik `[Apply]`
36. Ketik Search `Dell`, tekan Enter
37. Terapkan Filter Action `Edit`: klik icon Filter, pilih Action `Edit`, klik `[Apply]`
38. Klik header Date satu kali (Oldest First)
39. Clear Filter: klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
40. Verifikasi kotak Search masih berisi `Dell`
41. Verifikasi Sort Date tetap Oldest First
42. Terapkan Filter Action `Edit` lagi: klik icon Filter, pilih Action `Edit`, klik `[Apply]`
43. Klik `✕` pada Search, tekan Enter
44. Verifikasi Filter Action `Edit` masih aktif
45. Verifikasi Sort Date tetap Oldest First

## Notes

- Spec ini melewati sekitar 35 langkah (45). Alasan: seluruh blok satu kelas harness (Filter Modal Changelog), satu akun, dan satu dataset seed; Search, Filter, dan Sort pada satu surface tetap satu spec (bagian 3 prinsip 13), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan modal hanya satu kali (langkah 1).
- Langkah penghubung (aksi tanpa `Verifikasi`): mengosongkan Filter lewat `[Clear Field]` dan `[Apply]` di awal blok berikutnya (langkah 10, 20, 27, 31, 35), mencatat baris hasil sebagai pembanding (langkah 30), serta mengosongkan Search (langkah 31, 35).
- Urutan langkah 29 sampai 34 mengikuti TC (Search lalu Filter, kemudian Filter lalu Search); langkah 30 mencatat baris hasil halaman pertama dan langkah 34 membandingkannya.
- Opsi dropdown pada langkah 12 sampai 15 dan 22 diamati sebelum pilihan dibuat karena dropdown tertutup sesudah pemilihan (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-FAAM-475 Expected b ("Format tanggal mengikuti General Settings") tidak menyebut nilai format konkret, dan Pre-setup TC tidak mencantumkan Date Format dan Time Format baseline client utama; spec mengasersi kesesuaian dengan General Settings client.
  - TC-FA-FAAM-476 Expected b dan TC-FA-FAAM-477 Expected b ("berasal dari Field yang tercatat", "hanya user yang tercatat") tidak menyebut cara membaca daftar Field dan user yang tercatat; spec memakai kemampuan baca yang disediakan tim FE/BE.
  - TC-FA-FAAM-478 dan TC-FA-FAAM-479 tidak menyebut jumlah baris irisan; asersi memakai baris hasil yang dicatat.
