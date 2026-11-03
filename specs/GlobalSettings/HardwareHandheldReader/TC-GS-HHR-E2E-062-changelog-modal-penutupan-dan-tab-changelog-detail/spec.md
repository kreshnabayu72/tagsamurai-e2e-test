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
- Data Pre-setup: Client A plan Growth, format tanggal `dd/MM/yy` 24-hour Asia/Jakarta. Seed Reader A (`Fixture.hardwareHandheldReader.seedReaderA`, fixture baru) dengan reader yang dipakai spec: DD-03 (`Zebra Mobile Reader - 1`, Serial Number `SN-HHR-00103`; tiga baris seed Changelog CL-06, CL-07, CL-08, `Date` `16/06/26` sampai `18/06/26`), DD-08 (`Unitech EA520 - 1`, `SN-HHR-00109`; tanpa entri Changelog untuk TC-GS-HHR-341: reset tingkat reader yang mengembalikan Tab Changelog DD-08 ke kosong di hook `before` dan `after` disediakan tim FE/BE, lihat `suite.md` butir Reset tingkat reader dan Temuan untuk QA), dan DD-01 (`Zebra RFID Reader - 1`, `SN-HHR-00101`; Tab Usage dengan event UE-01 `21/06/26` oleh `Budi S`). Nama reader bernilai literal tanpa suffix karena asersi bergantung pada nilainya.
- Seed Changelog Client A (CL-01 s.d. CL-09; `Fixture.hardwareHandheldReader.seedChangelogClientA`) dan Seed Event Log Client A (EL-01 s.d. EL-05; `Fixture.hardwareHandheldReader.seedEventLogClientA`) ditulis fixture backend sebagai baris seed bertanggal Juni 2026 di hook `before` (kemampuan disediakan tim FE/BE); fixture tidak memulihkan audit trail. Entri yang dipakai asersi:
  - Tab Changelog DD-03: `18/06/26` Edit `Reader Power` `30 dBm` ke `25 dBm` (Modified By `Budi S`); `17/06/26` Edit `Status` `Available` ke `Damaged` (`Sari D`); `16/06/26` Edit `Status` `Damaged` ke `Available` (`Budi S`).
  - Modal Changelog: baris `20/06/26 11:10` Modified By `Sari D` (nama lengkap `Sari Dewi`).
  - Tab Usage DD-01: baris `21/06/26` PIC `Budi S` (nama lengkap `Budi Santoso`).
  - Popup Event Log Activate: baris `21/06/26 08:00` PIC `Budi S` (nama lengkap `Budi Santoso`).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan tooltip hover; pemilih rentang tanggal pada Filter Panel (Filter `Date` diproses server-side dan inklusif kedua ujung, tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE; nilai `Date` pada langkah ditulis dalam format tampil `dd/MM/yy`; input date picker memakai format `MM/dd/yyyy`, mis. `06/16/2026`, dan dipilih lewat date picker; perilaku date picker belum diverifikasi di UI); pemulihan seed lewat fixture backend; reset tingkat reader DD-08 (`suite.md`).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-HHR-340 dan TC-GS-HHR-470: Tab Changelog Popup Detail DD-03, kolom dan Filter Panel

1. Klik `Device Name` baris DD-03 (Serial Number `SN-HHR-00103`)
2. Klik tab `Changelog`
3. Verifikasi kolom tab berurutan: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi kolom `Device Name` tidak tampil
5. Klik ikon Filter di tab
6. Verifikasi field `Date` dengan placeholder `Select date`
7. Verifikasi field `Action` dengan placeholder `All actions`
8. Verifikasi field `Field` dengan placeholder `All fields`
9. Verifikasi field `Modified By` dengan placeholder `All users`
10. Verifikasi tidak ada field `Device Name` pada Filter Panel
11. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
12. Isi `Date` rentang `16/06/26` sampai `18/06/26`, klik `[Apply]`
13. Verifikasi tab menampilkan 3 baris seed (CL-06 sampai CL-08, `Date` `16/06/26` sampai `18/06/26`), dibaca pada tab yang dibatasi Filter `Date` seed (langkah 12) sehingga ketiga baris seed berada pada satu halaman; entri DD-03 lain di luar rentang itu tidak diasersi jumlahnya
14. Verifikasi baris `18/06/26`: Action `Edit`, Field `Reader Power`, Old Value `30 dBm`, New Value `25 dBm`, Modified By `Budi S`
15. Verifikasi baris `17/06/26`: Action `Edit`, Field `Status`, Old Value `Available`, New Value `Damaged`, Modified By `Sari D`
16. Verifikasi baris `16/06/26`: Action `Edit`, Field `Status`, Old Value `Damaged`, New Value `Available`, Modified By `Budi S`
17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Tutup Filter Panel

### TC-GS-HHR-342: Search tanpa hasil pada Tab Changelog

20. Catat jumlah baris tab `Changelog` sebagai baseline N0
21. Klik ikon Filter di tab
22. Pilih `Edit` pada `Action`
23. Klik `[Apply]`
24. Ketik Search `zzzz`, tekan Enter
25. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
26. Klik `[Reset Filters]`
27. Verifikasi kotak Search kosong
28. Verifikasi ikon Filter tanpa titik indikator
29. Verifikasi tabel kembali ke halaman 1
30. Verifikasi jumlah baris tabel sama dengan N0 (langkah 20), yaitu seluruh baris Changelog DD-03

### TC-GS-HHR-341: Empty state Tab Changelog untuk reader tanpa catatan

31. Tutup Popup `Handheld Reader Detail` dengan `✕`
32. Klik `Device Name` baris DD-08 (Serial Number `SN-HHR-00109`)
33. Klik tab `Changelog`
34. Verifikasi ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
35. Tutup Popup `Handheld Reader Detail` dengan `✕`

### TC-GS-HHR-469: Hover nama pengguna (Modal Changelog, Tab Usage, Popup Event Log Activate)

36. Klik ikon Changelog
37. Klik ikon Filter di modal, isi `Date` rentang `20/06/26` sampai `20/06/26`, klik `[Apply]` (pembatas seed CL-04)
38. Arahkan kursor ke `Sari D` pada kolom `Modified By` baris `20/06/26 11:10`
39. Verifikasi tooltip `Sari Dewi` tampil pada `Modified By`
40. Klik ikon Filter di modal, klik `[Clear Field]`, klik `[Apply]`, lalu klik ikon Filter untuk menutup Filter Panel
41. Tutup Modal Changelog dengan `✕`
42. Klik `Device Name` baris DD-01 (Serial Number `SN-HHR-00101`)
43. Klik ikon Filter di tab, isi `Date` rentang `21/06/26` sampai `21/06/26`, klik `[Apply]` (pembatas seed UE-01)
44. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26` di Tab Usage
45. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Tab Usage
46. Klik `[Clear Field]`, klik `[Apply]`, lalu klik ikon Filter di tab untuk menutup Filter Panel
47. Tutup Popup `Handheld Reader Detail` dengan `✕`
48. Klik ikon Event Log
49. Klik ikon Filter di popup, isi `Date` rentang `21/06/26` sampai `21/06/26`, klik `[Apply]` (pembatas seed EL-01)
50. Arahkan kursor ke `Budi S` pada kolom `PIC` baris `21/06/26 08:00`
51. Verifikasi tooltip `Budi Santoso` tampil pada `PIC` Popup Event Log Activate
52. Klik `[Clear Field]`, klik `[Apply]`, lalu klik ikon Filter di popup untuk menutup Filter Panel
53. Tutup Popup Event Log Activate dengan `✕`

### TC-GS-HHR-337: Modal Changelog ditutup lewat X dan Esc, bukan klik backdrop

54. Klik ikon Changelog
55. Klik area backdrop
56. Verifikasi Modal Changelog tetap terbuka
57. Klik `[✕]`
58. Verifikasi Modal Changelog tertutup
59. Klik ikon Changelog
60. Tekan `Esc`
61. Verifikasi Modal Changelog tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (section 4b). Spec hanya membaca.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: blok Tab Changelog Popup Detail (340, 470, 342, 341) dahulu, lalu hover nama pengguna (469), dan TC-GS-HHR-337 (menutup modal) paling akhir mengikuti prinsip kasus menutup di akhir. Modal Changelog dibuka 2 kali untuk 337 dan sekali untuk 469; jumlah buka tidak melebihi jumlah kejadian menutup.
- Langkah penghubung (aksi tanpa `Verifikasi`): mencatat baseline N0 (langkah 20), Filter `Date` satu hari sebagai pembatas baca blok TC-GS-HHR-469 beserta pelepasannya (langkah 37 dan 40, 43 dan 46, 49 dan 52), mengisi Filter `Date` seed sebagai pembatas baca (langkah 12), `[Clear Field]` dan `[Apply]` untuk melepas pembatas itu (langkah 17 dan 18), menutup Filter Panel (langkah 19; cara menutup tidak dinyatakan di TC), menutup popup dan modal dengan `✕`, dan membuka popup dan modal berikutnya. Filter `Action` = `Edit`, Search `zzzz` (TC-GS-HHR-342) dan `[Reset Filters]` langsung dari TC.
- Spec memuat 61 langkah (di atas sekitar 35 langkah). Alasan: seluruhnya fungsional baca satu akun, tanpa data yang dibuat atau diubah; 24 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok membuka popup atau modal sendiri dari layar yang sama.
- Pembagian TC lintas spec: TC-GS-HHR-338 (Download Modal Changelog) dan TC-GS-HHR-454 (Download Tab Changelog Popup Detail) ada di spec 058 (kelas isi berkas: klausa fungsional dan klausa isi berkas berada dalam satu TC); TC-GS-HHR-469 (hover nama pengguna) ada di spec ini; kegagalan unduh Modal Changelog dan Popup Event Log (TC-GS-HHR-339) di spec 028; Setup Column Tab Changelog dan Modal Changelog (TC-GS-HHR-292 sampai 305) di spec 056; screening Modal Changelog, Search, Filter, dan Sort (TC-GS-HHR-326 sampai 336) di spec 061; download Popup Event Log (TC-GS-HHR-363) di spec 066.
- Temuan untuk QA:
  - TC-GS-HHR-469 langkah 2 dan 3 menyebut "klik `Device Name` baris DD-01 ... kolom `PIC` baris `21/06/26`" (Tab Usage) dan "ikon Event Log ... baris `21/06/26 08:00`"; spec memakai baris yang dinyatakan TC dan menganggap Tab Usage terbuka pertama saat Popup Detail dibuka.
  - Cara menutup Filter Panel tidak dinyatakan di TC; spec menulis langkah penghubung generik "Tutup Filter Panel".
  - Pengecualian A-6 (empty state entitas bersih): TC-GS-HHR-341 mengasersi empty state Tab Changelog DD-08 sebagai nol absolut tanpa baseline; sah menurut A-6 `docs/e2e-conventions.md` karena DD-08 bukan target aksi tulis spec lain, suite berjalan serial, dan reset tingkat reader dinyatakan di `suite.md` dan `## Prerequisites`. Hitungan sesudah aksi tetap selisih terhadap baseline.
  - TC-GS-HHR-341 mengasersi empty state Tab Changelog DD-08 sebagai kondisi absolut (tanpa entri), padahal audit trail permanen dan spec lain dapat menulis entri DD-08. Spec mengikuti TC dan mengandalkan reset reader-level yang mengembalikan Tab Changelog DD-08 ke kosong (disediakan tim FE/BE, tidak didefinisikan di TC, PRD, atau LLD).
  - TC-GS-HHR-340 membaca tiga baris seed DD-03 pada tab Changelog yang tumbuh; baris seed bisa berada di halaman berikutnya bila entri DD-03 non-seed (bertanggal waktu aksi) memenuhi halaman pertama pada urutan `Date` terbaru di atas (10 per halaman). Spec membatasi tab dengan Filter `Date` `16/06/26` sampai `18/06/26` (langkah 12) sebelum membaca baris seed, sehingga seed berada pada satu halaman tanpa langkah pindah halaman (S-14), lalu melepas filter (langkah 17 dan 18) sebelum baseline N0 TC-GS-HHR-342. Filter itu tidak disebut di TC-GS-HHR-340; urutan Filter Panel (TC-GS-HHR-470) dimajukan sebelum pembacaan baris supaya placeholder field `Date` diasersi saat masih kosong.
  - Pembatas Filter `Date` satu hari pada blok TC-GS-HHR-469 (langkah 37 `20/06/26` untuk CL-04 di Modal Changelog, langkah 43 `21/06/26` untuk UE-01 di Tab Usage DD-01, langkah 49 `21/06/26` untuk EL-01 di Popup Event Log Activate; pelepasan di langkah 40, 46, dan 52) ditambahkan spec di luar langkah TC-GS-HHR-469 agar baris seed teramati meski Changelog dan Event Log Client A berisi entri Okt di atasnya (S-14) dan Tab Usage DD-01 dapat bertambah entri; Expected TC tetap terpenuhi karena filter tidak mengubah isi baris seed. Tolong konfirmasi bahwa penambahan itu tidak mengubah maksud TC. Panel Filter tetap terbuka sesudah `[Apply]`, jadi ditutup dengan ikon Filter (cara menutup tidak dinyatakan di TC).
