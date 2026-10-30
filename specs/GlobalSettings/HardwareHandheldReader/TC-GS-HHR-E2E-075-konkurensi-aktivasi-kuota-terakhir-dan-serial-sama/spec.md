---
id: TC-GS-HHR-E2E-075-konkurensi-aktivasi-kuota-terakhir-dan-serial-sama
title: "Konkurensi Aktivasi: Kuota Habis Sebelum Submit, Dua Admin pada Slot Kuota Terakhir, dan Serial Number yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-81
  - TC-GS-HHR-434
  - TC-GS-HHR-435
coverage:
  web: automated
---

# Konkurensi Aktivasi: Kuota Habis Sebelum Submit, Dua Admin pada Slot Kuota Terakhir, dan Serial Number yang Sama

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, dua sesi admin Client A) bersama harness eksternal (kelas d, simulator reader USB) sesuai pengecualian `P-7` (lihat Notes). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini dan akun Admin B (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Peran | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| B (UI) | Admin B, Total Control (Client A) | Nadia Pratama | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC2_PASSWORD` |
| B (API) | Admin B yang sama, hanya memicu aktivasi | Nadia Pratama | Sesi API akun yang sama | Sesi API |

- Login Sesi A dilakukan di hook `before`; Sesi B (UI) dibuka dengan langkah ganti akun eksplisit (langkah 1) karena hasil di sesi B diasersi (TC-GS-HHR-434 dan TC-GS-HHR-435). Untuk TC-GS-HHR-81 Admin B memakai sesi API karena hanya memicu aktivasi slot Long Range terakhir. Hook `after` menutup Sesi B dan mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE, `Long Range` terpakai 5 dari 6 sehingga tersisa 1; Event Log awal memuat 2 baris `Failed`: EL-03 dan EL-05): stok Principal HS-01 `SN-HHR-00201` (SKU-HHR-01 Zebra RFID Reader, Long Range, Current Power 22 dBm, Device Name bawaan `Zebra RFID Reader - 2`) dan HS-05 `SN-HHR-00206` (SKU-HHR-01, Long Range, Current Power tidak tersedia). Aktivasi Admin B pada TC-GS-HHR-81 memakai satu reader Long Range yang disediakan tim FE (TC tidak menyebut serialnya; lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE):
  - Simulator reader USB/driver lokal pada dua komputer (Sesi A dan Sesi B) untuk Sync `SN-HHR-00201` dan `SN-HHR-00206`; mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
  - Sinkronisasi klik `[Submit]` hampir bersamaan pada dua sesi.
  - Sesi API Admin B untuk mengaktifkan satu reader Long Range hingga `0 remaining` (TC-GS-HHR-81); endpoint tidak ditulis di spec ini.
  - Pemulihan Seed Reader A dan stok Principal antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
- Baseline: jumlah baris `Failed` di Event Log dicatat sebelum aksi pemicu TC-GS-HHR-81 (aksi Admin B menambah baris `Activated`, bukan `Failed`; S-12).
- State global yang diubah: Seed Reader A, kuota `Long Range`, stok Principal HS-01 dan HS-05. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi B) dan login sebagai Admin B (Nadia Pratama) Total Control Client A

### Kuota habis antara pemilihan Range Type dan Submit: TC-GS-HHR-81

2. Pulihkan Seed Reader A dan stok Principal
3. Sesi A: muat ulang Handheld Reader, klik ikon Event Log, catat jumlah baris `Failed` sebagai baseline, tutup Popup Event Log
4. Sesi A: klik `[+ Activate Reader]`
5. Sesi A: klik `Long Range` pada Overlay `Select Range Type`
6. Sesi A: klik `[Sync]` (reader USB `SN-HHR-00201` tersambung)
7. Admin B: aktifkan satu reader Long Range lewat sesi API hingga kuota Long Range `0 remaining` dan tersimpan
8. Tunggu aksi selesai
9. Sesi A: klik `[Submit]`
10. Verifikasi pesan inline di Popup Activate: `License quota reached for selected range type.`
11. Verifikasi Popup Activate tetap terbuka
12. Verifikasi input (Range Type `Long Range` dan Serial Number `SN-HHR-00201`) dipertahankan
13. Sesi A: klik `✕`
14. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
15. Sesi A: klik `[Cancel Activation]`
16. Muat ulang Handheld Reader, ketik Search `SN-HHR-00201`, tekan Enter
17. Verifikasi tidak ada baris baru dari sesi pertama di daftar reader (empty state `No results found`)
18. Klik `(←)` pada kotak Search, klik ikon Event Log
19. Verifikasi jumlah baris `Failed` di Event Log bertambah satu dari baseline
20. Verifikasi baris `Failed` baru memuat `Range Type` `Long Range`
21. Verifikasi baris `Failed` baru memuat `Device Name` `Zebra RFID Reader (SKU-HHR-01)`
22. Verifikasi baris `Failed` baru memuat `PIC` `Sari D`
23. Tutup Popup Event Log

### Dua admin pada slot kuota terakhir: TC-GS-HHR-434

24. Pulihkan Seed Reader A dan stok Principal
25. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00201` tersambung)
26. Sesi B: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00206` tersambung)
27. Sesi A dan Sesi B: klik `[Submit]` hampir bersamaan
28. Verifikasi tepat satu dari Sesi A atau Sesi B berhasil: Popup Activate tertutup pada tepat satu sesi
29. Verifikasi kartu `Long Range` pada sesi yang popup-nya tertutup menampilkan `6 of 6` dan `0 remaining`
30. Verifikasi sesi yang popup-nya masih terbuka menampilkan pesan inline `License quota reached for selected range type.`
31. Verifikasi Popup Activate sesi tersebut tetap terbuka
32. Verifikasi input sesi tersebut dipertahankan
33. Pada sesi yang popup-nya masih terbuka: klik `✕`
34. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
35. Pada sesi yang popup-nya masih terbuka: klik `[Cancel Activation]`

### Dua admin mengaktifkan serial yang sama: TC-GS-HHR-435

36. Pulihkan Seed Reader A dan stok Principal
37. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00201` tersambung)
38. Sesi B: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00201` tersambung)
39. Sesi A dan Sesi B: klik `[Submit]` hampir bersamaan
40. Verifikasi tepat satu dari Sesi A atau Sesi B berhasil dengan baris `Zebra RFID Reader - 2`
41. Verifikasi sesi yang popup-nya masih terbuka menampilkan pesan inline `Serial number already exists`
42. Pada sesi yang popup-nya masih terbuka: klik `✕`
43. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
44. Pada sesi yang popup-nya masih terbuka: klik `[Cancel Activation]`
45. Sesi yang berhasil: ketik Search `Zebra RFID Reader - 2`, tekan Enter
46. Verifikasi hanya satu reader `Zebra RFID Reader - 2` tercipta (tepat satu baris)
47. Sesi yang berhasil: klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 3a-4 untuk TC-GS-HHR-81, Section 9 untuk TC-GS-HHR-434 dan TC-GS-HHR-435). Ketiga TC berlabel Manual Only: (b) reader USB fisik dan (d) dua sesi paralel; kebutuhannya ditulis di Prerequisites.
- Urutan: kasus Admin B lewat sesi API (TC-GS-HHR-81) lebih dulu, kedua race dua sesi UI sesudahnya. Seed Reader A dan stok dipulihkan di awal tiap blok (langkah 2, 24, 36) supaya kuota `Long Range` tersisa 1 pada tiap blok dan kegagalan satu blok tidak menutupi hasil blok lain.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan, muat ulang, membuka dan menutup Popup Event Log, membuka Popup Activate, Search dan bersih Search, menutup Popup Activate. Langkah "Tunggu aksi selesai" dipakai karena aksi Admin B lewat sesi API diikuti pengamatan di Sesi A.
- Hasil race tidak menentukan sesi mana yang berhasil: langkah 28 dan 40 menegaskan tepat satu dari Sesi A atau Sesi B berhasil, dan langkah sesudahnya mengacu pada "sesi yang popup-nya masih terbuka" dan "sesi yang berhasil" tanpa cabang bersyarat; kedua sesi dibersihkan (popup sesi lain ditutup lewat dialog `Cancel Activation`, Search sesi yang berhasil dikosongkan).
- `P-7` (simulator USB bersama konteks lain, pengecualian atas pemisahan kelas d). Alasan per TC:
  - TC-GS-HHR-81: membutuhkan simulator USB untuk Sync `SN-HHR-00201` dan sesi kedua Admin B (sesi API) yang mengaktifkan slot Long Range terakhir sebelum `[Submit]` (kelas c).
  - TC-GS-HHR-434: membutuhkan dua simulator USB (`SN-HHR-00201` dan `SN-HHR-00206`) pada dua komputer dan race `[Submit]` antara Sesi A dan Sesi B (kelas c).
  - TC-GS-HHR-435: membutuhkan simulator USB `SN-HHR-00201` pada dua komputer dan race `[Submit]` serial yang sama antara Sesi A dan Sesi B (kelas c).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu topik (race aktivasi dua sesi) dan berdiri sendiri; tiap blok memulihkan data dan tidak bergantung pada hasil blok lain.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00201` dan `SN-HHR-00206` pada dua komputer) tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - TC-GS-HHR-81 langkah 4 ("aktifkan satu reader Long Range") tidak menyebut serial atau Device Name reader yang diaktifkan Admin B; spec menyerahkannya ke tim FE.
  - TC-GS-HHR-81 butir b ("Tidak ada baris baru dari sesi pertama di daftar reader") tidak menyebut cara mengenali baris sesi pertama padahal Admin B menambah baris sendiri; spec mencari serial `SN-HHR-00201`.
  - TC-GS-HHR-434 dan TC-GS-HHR-435 tidak menyebut cara menutup popup sesi yang ditolak; spec memakai `✕`, `Verifikasi` dialog `Cancel Activation` (teks dari TC-GS-HHR-89), lalu `[Cancel Activation]` seperti TC-GS-HHR-81 langkah 6 (S-08).
  - TC-GS-HHR-434 butir b dan TC-GS-HHR-435 butir b menyatakan hasil "sesi lain" tanpa menyebut sesi mana yang menang; hasil bergantung pada urutan di server.
  - TC-GS-HHR-435 butir a menyebut baris `Zebra RFID Reader - 2` (HS-01); bila Seed Reader A sudah memuat `Zebra RFID Reader - 1` (DD-01), nomor `N` mengikuti Device Name bawaan stok.
