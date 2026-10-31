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
- Suite serial (`parallel: false`); lihat `suite.md`. Spec ini hanya membaca Changelog; tidak ada data yang dibuat atau dihapus.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka.
- Akun aktor: Total Control (Sari Dewi) Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client A plan Growth, format tanggal `dd/MM/yy` 24-hour Asia/Jakarta. Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dengan reader yang dipakai spec: DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`; tiga entri Changelog CL-06, CL-07, CL-08), DD-08 (`Unitech EA520 - 1`, `SN-HHR-00109`; tanpa entri Changelog), dan DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`; Tab Usage dengan event UE-01 `21/06/26` oleh `Budi S`). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dan Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) dipulihkan lewat fixture backend di hook `before` dan `after` (kemampuan disediakan tim FE/BE). Entri yang dipakai asersi:
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
5. Verifikasi tab menampilkan tepat 3 baris
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

17. Klik ikon Filter di tab
18. Pilih `Edit` pada `Action`
19. Klik `[Apply]`
20. Ketik Search `zzzz`, tekan Enter
21. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
22. Klik `[Reset Filters]`
23. Verifikasi kotak Search kosong
24. Verifikasi ikon Filter tanpa titik indikator
25. Verifikasi tabel kembali ke halaman 1
26. Verifikasi tabel menampilkan seluruh baris Changelog DD-03 (3 baris)

### TC-GS-HHR-341: Empty state Tab Changelog untuk reader tanpa catatan

27. Tutup Popup `Handheld Reader Detail` dengan `✕`
28. Klik `Device Name` baris DD-08 (Serial Number `SN-HHR-00109`)
29. Klik tab `Changelog`
30. Verifikasi ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
31. Tutup Popup `Handheld Reader Detail` dengan `✕`

### TC-GS-HHR-469: Hover nama pengguna (Modal Changelog, Tab Usage, Popup Event Log Activate)

32. Klik ikon Changelog
33. Arahkan kursor ke `Sari D` pada kolom `Modified By` baris `20/06/26 11:10`
34. Verifikasi tooltip `Sari Dewi` tampil pada `Modified By`
35. Tutup Modal Changelog dengan `✕`
36. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
37. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26` di Tab Usage
38. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Tab Usage
39. Tutup Popup `Handheld Reader Detail` dengan `✕`
40. Klik ikon Event Log
41. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26 08:00`
42. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Popup Event Log Activate
43. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-337: Modal Changelog ditutup lewat X dan Esc, bukan klik backdrop

44. Klik ikon Changelog
45. Klik area backdrop
46. Verifikasi Modal Changelog tetap terbuka
47. Klik `[✕]`
48. Verifikasi Modal Changelog tertutup
49. Klik ikon Changelog
50. Tekan `Esc`
51. Verifikasi Modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 4b). Spec hanya membaca.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: blok Tab Changelog Popup Detail (340, 470, 342, 341) dahulu, lalu hover nama pengguna (469), dan TC-GS-HHR-337 (menutup modal) paling akhir mengikuti prinsip kasus menutup di akhir. Modal Changelog dibuka 2 kali untuk 337 dan sekali untuk 469; jumlah buka tidak melebihi jumlah kejadian menutup.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup Filter Panel (cara menutup tidak dinyatakan di TC), menutup popup dan modal dengan `✕`, dan membuka popup dan modal berikutnya. Filter `Action` = `Edit`, Search `zzzz` (TC-GS-HHR-342) dan `[Reset Filters]` langsung dari TC.
- Spec memuat 51 langkah (di atas sekitar 35 langkah). Alasan: seluruhnya fungsional baca satu akun, tanpa data yang dibuat atau diubah; 24 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok membuka popup atau modal sendiri dari layar yang sama.
- Pembagian TC lintas spec: TC-GS-HHR-338 (Download Modal Changelog) dan TC-GS-HHR-454 (Download Tab Changelog Popup Detail) ada di spec 058 (kelas isi berkas: klausa fungsional dan klausa isi berkas berada dalam satu TC); TC-GS-HHR-469 (hover nama pengguna) ada di spec ini; kegagalan unduh Modal Changelog dan Popup Event Log (TC-GS-HHR-339) di spec 028; Setup Column Tab Changelog dan Modal Changelog (TC-GS-HHR-292 sampai 305) di spec 056; screening Modal Changelog, Search, Filter, dan Sort (TC-GS-HHR-326 sampai 336) di spec 061; download Popup Event Log (TC-GS-HHR-363) di spec 066.
- Temuan untuk QA:
  - TC-GS-HHR-469 langkah 2 dan 3 menyebut "klik `Device Name` baris DD-01 ... kolom `PIC` baris `21/06/26`" (Tab Usage) dan "ikon Event Log ... baris `21/06/26 08:00`"; spec memakai baris yang dinyatakan TC dan menganggap Tab Usage terbuka pertama saat Popup Detail dibuka.
  - Cara menutup Filter Panel tidak dinyatakan di TC; spec menulis langkah penghubung generik "Tutup Filter Panel".
