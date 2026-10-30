---
id: TC-GS-POS-E2E-047-format-tanggal-general-settings
title: "Format Tanggal General Settings pada Tabel Utama, Filter Panel, Popup Changelog, dan Filter Date Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-254
  - TC-GS-POS-255
coverage:
  web: automated
---

# Format Tanggal General Settings pada Tabel Utama, Filter Panel, Popup Changelog, dan Filter Date Position

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (parallel: false): spec ini mengubah General Settings entitas (Date Format, Time Format, Time Zone).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Spec ini tidak menguji navigasi sehingga langkah 1 sampai 3 langsung membuat Position.
- Data Pre-setup yang dipakai: General Settings entitas (Pre-setup 22) sebagai state yang diubah dan dipulihkan.
- Data Dinamis (suffix per run dan nomor spec): `Format Tanggal {runId}-047`, dibuat lewat UI pada langkah 1 sampai 3 sehingga tabel dan Popup Changelog memuat record dan entri Create dengan waktu yang diketahui.
- State global dan pemulihan: hook `before` mencatat nilai awal Date Format, Time Format, dan Time Zone entitas lalu menyetelnya ke kondisi awal TC-GS-POS-254 (Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`) lewat API; hook `after` memulihkan nilai awal itu, sehingga tetap berjalan bila spec gagal di tengah. Mekanisme penyetelan General Settings lewat API disediakan tim FE/BE.
- Kemampuan teknis: membaca `updatedAt` record `Format Tanggal {runId}-047` (waktu UTC) lewat API Position untuk menghitung nilai Last Updated yang diharapkan di Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`; membaca teks input date range pada Filter Panel dan pada filter Popup Changelog.
- Cleanup (hook `after`, tidak berasumsi pembuatan berhasil): hapus lewat API Position `Format Tanggal {runId}-047` bila masih ada; kosongkan Search tabel Position.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.

## Test Steps

### Persiapan: Position dibuat lewat UI

1. Klik `[+ Position]`
2. Isi Position Name dengan `Format Tanggal {runId}-047`
3. Klik `[Submit]`
4. Tunggu aksi selesai (modal tertutup)
5. Baca `updatedAt` record `Format Tanggal {runId}-047` lewat API Position dan catat sebagai `U` (UTC)

### TC-GS-POS-254: Format tanggal pada tabel utama dan Filter Panel

6. Ketik Search `Format Tanggal {runId}-047` pada tabel Position, tekan Enter
7. Verifikasi tanggal pada kolom Last Updated baris tersebut tampil dengan Date Format `dd/MM/yy`
8. Verifikasi jam pada kolom Last Updated baris tersebut tampil dengan Time Format `HH:mm`
9. Verifikasi nilai Last Updated sama dengan `U` ditampilkan dalam Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`
10. Catat teks Last Updated sebagai `L1`
11. Klik ikon Filter
12. Pilih rentang tanggal pada Last Updated dari tanggal hari ini sampai tanggal hari ini
13. Verifikasi input date range menampilkan tanggal dalam format `dd/MM/yy`
14. Tutup Filter Panel dengan klik ikon Filter
15. Buka Global Settings > General Settings
16. Ubah Date Format menjadi `dd MMM yy`
17. Ubah Time Format menjadi `hh:mm a`
18. Ubah Time Zone menjadi `(UTC+00:00) UTC, Reykjavik, Accra`
19. Klik `[Save]`
20. Tunggu aksi selesai
21. Buka Global Settings > User, klik sub-tab Position
22. Ketik Search `Format Tanggal {runId}-047` pada tabel Position, tekan Enter
23. Verifikasi tanggal pada kolom Last Updated mengikuti Date Format `dd MMM yy`
24. Verifikasi jam pada kolom Last Updated mengikuti Time Format `hh:mm a`
25. Verifikasi waktu Last Updated bergeser 7 jam lebih awal dibanding `L1` (UTC+07:00 menjadi UTC+00:00)
26. Klik ikon Filter
27. Pilih rentang tanggal pada Last Updated dari tanggal hari ini sampai tanggal hari ini
28. Verifikasi input date range menampilkan tanggal dalam format `dd MMM yy`
29. Tutup Filter Panel dengan klik ikon Filter

### TC-GS-POS-255: Format tanggal pada Popup Changelog dan Filter Date

30. Buka Global Settings > General Settings
31. Ubah Date Format menjadi `dd/MM/yy`
32. Ubah Time Format menjadi `HH:mm`
33. Klik `[Save]`
34. Tunggu aksi selesai
35. Buka Global Settings > User, klik sub-tab Position
36. Klik ikon Changelog, ketik Search `Format Tanggal {runId}-047`, tekan Enter
37. Verifikasi tanggal pada kolom Date entri Create `Format Tanggal {runId}-047` mengikuti Date Format `dd/MM/yy`
38. Verifikasi jam pada kolom Date entri Create `Format Tanggal {runId}-047` mengikuti Time Format `HH:mm`
39. Klik ikon Filter pada Popup Changelog
40. Pilih rentang pada Date dari tanggal hari ini sampai tanggal hari ini
41. Verifikasi input Date filter mengikuti format `dd/MM/yy`
42. Tutup Filter Panel Popup Changelog dengan klik ikon Filter
43. Tutup Popup Changelog dengan `✕`
44. Buka Global Settings > General Settings
45. Ubah Time Format menjadi `hh:mm a`
46. Klik `[Save]`
47. Tunggu aksi selesai
48. Buka Global Settings > User, klik sub-tab Position
49. Klik ikon Changelog, ketik Search `Format Tanggal {runId}-047`, tekan Enter
50. Verifikasi waktu pada kolom Date entri Create tampil dengan pola `hh:mm a`
51. Tutup Popup Changelog dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec ini kelas state global (serial): General Settings diubah dan dipulihkan di hook `after`.
- Urutan TC di spec: 254 lalu 255. TC-GS-POS-254 mengubah ketiga setting (Date Format `dd MMM yy`, Time Format `hh:mm a`, Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`); langkah 30 sampai 33 mengembalikan Date Format dan Time Format ke kondisi awal TC-GS-POS-255 (Date Format `dd/MM/yy`, Time Format `HH:mm`). Time Zone dibiarkan `(UTC+00:00) UTC, Reykjavik, Accra` pada TC-GS-POS-255 karena TC itu tidak mensyaratkan Time Zone; hook `after` memulihkan nilai awal ketiganya.
- Langkah "Tunggu aksi selesai" (langkah 4, 20, 34, 47) ditulis tanpa `Verifikasi` sesudah `[Submit]` atau `[Save]` yang hasilnya tidak diasersi langsung dan langkah berikutnya pindah surface (membaca `updatedAt` lewat API, kembali ke tab Position; konvensi bagian 8b butir 8). Langkah 4 menjamin `U` dibaca sesudah Create selesai.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (mencatat `U`), langkah 10 (mencatat `L1`), langkah 14, 29, 42 (menutup Filter Panel dengan klik ikon Filter), langkah 15 sampai 21 (termasuk langkah 20), 30 sampai 35 (termasuk langkah 34), dan 44 sampai 48 (termasuk langkah 47; mengubah General Settings dan kembali ke tab Position), langkah 43 dan 51 (menutup Popup Changelog dengan `✕`; popup tidak dirty). Rentang pada langkah 12, 27, dan 40 dipilih hanya untuk mengamati teks input; filter tidak di-Apply. Search pada langkah 6 dan 22 mencari baris `Format Tanggal {runId}-047` di tabel Position agar kolom Last Updated bisa dibaca (tidak ada di TC); Search pada langkah 36 dan 49 mempersempit Popup Changelog ke entri milik spec (tidak ada di TC).
- Spec melewati sekitar 35 langkah (51 langkah). Seluruhnya satu kelas (state global General Settings, serial), satu akun, satu record `Format Tanggal {runId}-047`; setiap blok TC mengatur ulang General Settings sendiri sebelum diamati, sehingga blok TC-GS-POS-255 tetap bermakna bila blok TC-GS-POS-254 gagal.
- Pembagian TC lintas spec: Popup Changelog sebagai objek uji pencatatan log (TC-GS-POS-242 sampai 245) ada di spec TC-GS-POS-E2E-044.
- Temuan untuk QA:
  - TC-GS-POS-255 precondition tidak menyebut Time Zone; setelah TC-GS-POS-254 Time Zone tetap `(UTC+00:00) UTC, Reykjavik, Accra` dan spec tidak mengembalikannya di tengah spec (hook `after` memulihkan).
  - TC-GS-POS-255 Langkah 2 menyebut "Buka Filter" pada Popup Changelog tanpa menyebut Apply atau cara menutup Filter Panel; spec hanya mengamati input lalu menutup Filter Panel dengan klik ikon Filter.
  - TC-GS-POS-254 dan 255 tidak menyebut data record; spec membuat `Format Tanggal {runId}-047` dan membaca `updatedAt`-nya lewat API Position (kemampuan disediakan tim FE/BE; endpoint tidak ditetapkan di TC atau PRD).
