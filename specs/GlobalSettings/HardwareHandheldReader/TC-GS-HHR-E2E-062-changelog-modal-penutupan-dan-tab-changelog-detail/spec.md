---
id: TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail
title: "Tab Changelog Popup Detail dan Modal Changelog: Kolom, Filter Panel, Search Tanpa Hasil, Empty State, Hover Nama Pengguna, dan Penutupan Modal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-337
  - TC-GS-HHR-340
  - TC-GS-HHR-341
  - TC-GS-HHR-342
  - TC-GS-HHR-469
  - TC-GS-HHR-470
coverage:
  web: automated
---

# Tab Changelog Popup Detail dan Modal Changelog: Kolom, Filter Panel, Search Tanpa Hasil, Empty State, Hover Nama Pengguna, dan Penutupan Modal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Changelog; tidak ada data yang dibuat atau dihapus. Audit trail permanen tidak dipulihkan: entri Changelog DD-03 lain bertanggal waktu aksi dapat ada di luar rentang `Date` seed; baris seed dikenali lewat `Date`, jumlah baris tab tidak diasersi sebagai angka absolut, dan kembali ke tabel penuh diasersi terhadap baseline N0 yang dicatat sebelum Search atau Filter.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client A plan Growth, format tanggal `dd/MM/yy` 24-hour Asia/Jakarta. Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dengan reader yang dipakai spec: DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`; tiga baris seed Changelog CL-06, CL-07, CL-08, `Date` `16/06/26` sampai `18/06/26`), DD-08 (`Unitech EA520 - 1`, `SN-HHR-00109`; tanpa entri Changelog untuk TC-GS-HHR-341: reset reader-level yang mengembalikan Tab Changelog DD-08 ke kosong disediakan tim FE/BE, lihat Temuan untuk QA), dan DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`; Tab Usage dengan event UE-01 `21/06/26` oleh `Budi S`). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dan Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) ditulis fixture backend sebagai baris seed bertanggal Juni 2026 di hook `before` (kemampuan disediakan tim FE/BE); fixture tidak memulihkan audit trail. Entri yang dipakai asersi:
  - Tab Changelog DD-03: `18/06/26` Edit `Reader Power` `30 dBm` ke `25 dBm` (Modified By `Budi S`); `17/06/26` Edit `Status` `Available` ke `Damaged` (`Sari D`); `16/06/26` Edit `Status` `Damaged` ke `Available` (`Budi S`).
  - Modal Changelog: baris `20/06/26 11:10` Modified By `Sari D` (nama lengkap `Sari Dewi`).
  - Tab Usage DD-01: baris `21/06/26` PIC `Budi S` (nama lengkap `Budi Santoso`).
  - Popup Event Log Activate: baris `21/06/26 08:00` PIC `Budi S` (nama lengkap `Budi Santoso`).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan tooltip hover; pemulihan seed lewat fixture backend.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-340 dan TC-GS-HHR-470: Tab Changelog Popup Detail DD-03, kolom dan Filter Panel

1. Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`)
2. Klik tab `Changelog`
3. Verifikasi kolom tab berurutan: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi kolom `Device Name` tidak tampil
5. Verifikasi tab menampilkan 3 baris seed (CL-06 sampai CL-08, `Date` `16/06/26` sampai `18/06/26`), dibaca pada kolom `Date` seluruh halaman tab; entri DD-03 lain di luar rentang itu tidak diasersi jumlahnya
6. Verifikasi baris `18/06/26`: Action `Edit`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Budi S`
7. Verifikasi baris `17/06/26`: Action `Edit`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
8. Verifikasi baris `16/06/26`: Action `Edit`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Budi S`
9. Klik ikon Filter di tab
10. Verifikasi field `Date` dengan placeholder `Select date`
11. Verifikasi field `Action` dengan placeholder `All actions`
12. Verifikasi field `Field` dengan placeholder `All fields`
13. Verifikasi field `Modified By` dengan placeholder `All users`
14. Verifikasi tidak ada field `Device Name` pada Filter Panel
15. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
16. Tutup Filter Panel

### TC-GS-HHR-342: Search tanpa hasil pada Tab Changelog

17. Catat jumlah baris tab `Changelog` sebagai baseline N0
18. Klik ikon Filter di tab
19. Pilih `Edit` pada `Action`
20. Klik `[Apply]`
21. Ketik Search `zzzz`, tekan Enter
22. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
23. Klik `[Reset Filters]`
24. Verifikasi kotak Search kosong
25. Verifikasi ikon Filter tanpa titik indikator
26. Verifikasi tabel kembali ke halaman 1
27. Verifikasi jumlah baris tabel sama dengan N0 (langkah 17), yaitu seluruh baris Changelog DD-03

### TC-GS-HHR-341: Empty state Tab Changelog untuk reader tanpa catatan

28. Tutup Popup `Handheld Reader Detail` dengan `✕`
29. Klik `Device Name` baris DD-08 (Serial Number `SN-HHR-00109`)
30. Klik tab `Changelog`
31. Verifikasi ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
32. Tutup Popup `Handheld Reader Detail` dengan `✕`

### TC-GS-HHR-469: Hover nama pengguna (Modal Changelog, Tab Usage, Popup Event Log Activate)

33. Klik ikon Changelog
34. Arahkan kursor ke `Sari D` pada kolom `Modified By` baris `20/06/26 11:10`
35. Verifikasi tooltip `Sari Dewi` tampil pada `Modified By`
36. Tutup Modal Changelog dengan `✕`
37. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
38. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26` di Tab Usage
39. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Tab Usage
40. Tutup Popup `Handheld Reader Detail` dengan `✕`
41. Klik ikon Event Log
42. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26 08:00`
43. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Popup Event Log Activate
44. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-337: Modal Changelog ditutup lewat X dan Esc, bukan klik backdrop

45. Klik ikon Changelog
46. Klik area backdrop
47. Verifikasi Modal Changelog tetap terbuka
48. Klik `[✕]`
49. Verifikasi Modal Changelog tertutup
50. Klik ikon Changelog
51. Tekan `Esc`
52. Verifikasi Modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 4b). Spec hanya membaca.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: blok Tab Changelog Popup Detail (340, 470, 342, 341) dahulu, lalu hover nama pengguna (469), dan TC-GS-HHR-337 (menutup modal) paling akhir mengikuti prinsip kasus menutup di akhir. Modal Changelog dibuka 2 kali untuk 337 dan sekali untuk 469; jumlah buka tidak melebihi jumlah kejadian menutup.
- Langkah penghubung (aksi tanpa `Verifikasi`): mencatat baseline N0 (langkah 17), menutup Filter Panel (cara menutup tidak dinyatakan di TC), menutup popup dan modal dengan `✕`, dan membuka popup dan modal berikutnya. Filter `Action` = `Edit`, Search `zzzz` (TC-GS-HHR-342) dan `[Reset Filters]` langsung dari TC.
- Spec memuat 52 langkah (di atas sekitar 35 langkah). Alasan: seluruhnya fungsional baca satu akun, tanpa data yang dibuat atau diubah; 24 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok membuka popup atau modal sendiri dari layar yang sama.
- Pembagian TC lintas spec: TC-GS-HHR-338 (Download Modal Changelog) dan TC-GS-HHR-454 (Download Tab Changelog Popup Detail) ada di spec 058 (kelas isi berkas: klausa fungsional dan klausa isi berkas berada dalam satu TC); TC-GS-HHR-469 (hover nama pengguna) ada di spec ini; kegagalan unduh Modal Changelog dan Popup Event Log (TC-GS-HHR-339) di spec 028; Setup Column Tab Changelog dan Modal Changelog (TC-GS-HHR-292 sampai 305) di spec 056; screening Modal Changelog, Search, Filter, dan Sort (TC-GS-HHR-326 sampai 336) di spec 061; download Popup Event Log (TC-GS-HHR-363) di spec 066.
- Temuan untuk QA:
  - TC-GS-HHR-469 langkah 2 dan 3 menyebut "klik `Device Name` baris DD-01 ... kolom `PIC` baris `21/06/26`" (Tab Usage) dan "ikon Event Log ... baris `21/06/26 08:00`"; spec memakai baris yang dinyatakan TC dan menganggap Tab Usage terbuka pertama saat Popup Detail dibuka.
  - Cara menutup Filter Panel tidak dinyatakan di TC; spec menulis langkah penghubung generik "Tutup Filter Panel".
  - TC-GS-HHR-341 mengasersi empty state Tab Changelog DD-08 sebagai kondisi absolut (tanpa entri), padahal audit trail permanen dan spec lain dapat menulis entri DD-08. Spec mengikuti TC dan mengandalkan reset reader-level yang mengembalikan Tab Changelog DD-08 ke kosong (disediakan tim FE/BE, tidak didefinisikan di TC, PRD, atau LLD).
  - TC-GS-HHR-340 membaca tiga baris seed DD-03 pada tab tanpa Filter `Date`; bila entri DD-03 non-seed (bertanggal waktu aksi) memenuhi halaman pertama pada urutan `Date` terbaru di atas (10 per halaman), baris seed berada di halaman berikutnya. Spec membaca seluruh halaman tab.
