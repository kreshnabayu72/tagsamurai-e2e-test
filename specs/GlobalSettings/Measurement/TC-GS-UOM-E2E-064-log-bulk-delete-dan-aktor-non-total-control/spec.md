---
id: TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control
title: "Pencatatan Log Bulk Delete dan Modified By Aktor Non-Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-220
  - TC-GS-UOM-224
  - TC-GS-UOM-267
coverage:
  web: automated
---

# Pencatatan Log Bulk Delete dan Modified By Aktor Non-Total Control

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai tiga akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | System Role: Create dan Read (Rina Marlina, `Rina M`) | `createOnly_automated_qaTeam1@qwertysystem.net` | `GS_CREATE_PASSWORD` |
  | 3 | System Role: Delete dan Read (Dewi Lestari, `Dewi L`) | `deleteOnly_automated_qaTeam1@qwertysystem.net` | `GS_DELETE_PASSWORD` |

  Login akun 1 di hook `before` spec ini (akun default suite); hook `after` mengembalikan sesi ke akun 1.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_DELETE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`, bagian Hook suite).
- Data Pre-setup Client A (dilewati oleh guard in-use pada Bulk Delete campuran, tidak diubah dan Last Updated tidak berubah; pengecualian S-06; tanpa suffix `{runId}`): `Box` (in-use, FAMS Storage Box A, B, C, D).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Liter {runId}-064` / `L` dan `Pack {runId}-064` / `pk`: dua unit bebas relasi, di-seed lewat API di hook `before`; terhapus oleh Bulk Delete campuran (setara dependensi TC-GS-UOM-118; pengganti Liter dan Pack Pre-setup).
  - `Kilometer {runId}-064` / `km`: dibuat spec lewat UI oleh akun 2 dan dihapus lewat UI oleh akun 3 (setara dependensi TC-GS-UOM-34).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Liter`, `Pack`, dan `Kilometer` bersuffix `{runId}-064` bila masih ada; pulihkan page size tabel Measurement ke 10.
- Kemampuan teknis: akses Total Control ke Detail User Sari Dewi > Tab System Log dan Global Settings > Activity Log; akun 3 membuka Changelog Measurement (capability Read tercakup pada System Role: Delete dan Read).
- Tidak ada state global yang diubah.
- TC-GS-UOM-220 dan 267: login sebagai Total Control. TC-GS-UOM-224: Create sebagai System Role: Create dan Read, Delete sebagai System Role: Delete dan Read. Semua berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-220 dan TC-GS-UOM-267: Bulk Delete campuran mencatat unit terhapus di tiga surface

1. Ubah page size tabel menjadi 50, lalu centang baris `Liter {runId}-064`, `Pack {runId}-064`, dan `Box`
2. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
3. Klik [Continue] pada dialog Bulk Delete campuran
4. Verifikasi toast: "Success, unit has been deleted. Some items were skipped."
5. Buka Changelog, ketik Search `{runId}-064`, tekan Enter
6. Verifikasi Changelog: baris Action `Delete`, Unit Name `Liter {runId}-064`, Field `Unit Name`, Old Value `Liter {runId}-064`, New Value `—`, Modified By `Sari D`
7. Verifikasi Changelog: baris Action `Delete`, Unit Name `Pack {runId}-064`, Field `Unit Name`, Old Value `Pack {runId}-064`, New Value `—`, Modified By `Sari D`
8. Verifikasi Changelog: tepat dua baris Delete untuk unit milik spec (Liter dan Pack)
9. Tutup Changelog
10. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `{runId}-064`, tekan Enter
11. Verifikasi System Log: tepat satu baris Delete dengan Object `Measurement` dan Name `Liter {runId}-064`
12. Verifikasi System Log: tepat satu baris Delete dengan Object `Measurement` dan Name `Pack {runId}-064`
13. Buka Global Settings > Activity Log, pilih tab `User Action`, ketik Search `{runId}-064`, tekan Enter
14. Verifikasi Activity Log: tepat satu baris Delete dengan Object `Measurement` dan Name `Liter {runId}-064`
15. Verifikasi Activity Log: tepat satu baris Delete dengan Object `Measurement` dan Name `Pack {runId}-064`

### TC-GS-UOM-224: Modified By mencatat aktor pelaksana tiap aksi

16. Ganti akun: logout, lalu login sebagai System Role: Create dan Read (`createOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_CREATE_PASSWORD`, lalu buka Global Settings > Master Reference > Measurement
17. Klik [+ Unit], isi Unit Name `Kilometer {runId}-064` dan Symbol `km`, klik [Submit]
18. Tunggu aksi selesai (form tertutup)
19. Ganti akun: logout, lalu login sebagai System Role: Delete dan Read (`deleteOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_DELETE_PASSWORD`, lalu buka Global Settings > Master Reference > Measurement
20. Ketik Search `Kilometer {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog
21. Tunggu aksi selesai (toast sukses tampil)
22. Buka Changelog, ketik Search `Kilometer {runId}-064`, tekan Enter
23. Verifikasi Changelog: baris Action `Create` untuk `Kilometer {runId}-064` berisi Modified By `Rina M`
24. Verifikasi Changelog: baris Action `Delete` untuk `Kilometer {runId}-064` berisi Modified By `Dewi L`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: pencatatan log.
- Urutan TC di spec berbeda dari urutan sumber: blok Total Control (220, 267) dahulu, lalu satu kali ganti akun ke akun Create (langkah 16) dan satu kali ke akun Delete (langkah 19) untuk 224. Bulk Delete (aksi menghapus) berada di awal karena data tiap blok independen dan blok sesudahnya tidak membutuhkan baris yang terhapus.
- Pembagian TC lintas spec: TC-GS-UOM-220 b dan TC-GS-UOM-267 b ("tidak ada baris/entri untuk Box") adalah asersi absence (kelas g) dan dikerjakan di spec `TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen` dengan aksi Bulk Delete campuran dan baseline sendiri (S-05). Spec ini hanya memuat presence (TC-GS-UOM-220 a dan TC-GS-UOM-267 a); id kedua TC tercatat di `sourceTc` kedua spec.
- Modified By memakai format `[First Name] [Last Initial]` (`Rina M`, `Dewi L`, `Sari D`), bukan nama lengkap.
- Entri log dikenali lewat nama bersuffix `{runId}-064`; entri milik spec atau run lain diabaikan. Hitungan "tepat satu baris" memakai Search `{runId}-064` pada surface yang sedang terbuka (S-12).
- Langkah penghubung: langkah 1 (ubah page size menjadi 50 agar `Liter`, `Pack`, dan `Box` tampil bersama untuk dicentang; dipulihkan ke 10 di hook `after`), langkah 5, 10, 13, dan 22 (membuka surface log dan Search; langkah 13 juga memilih tab `User Action` pada Activity Log), langkah 9 (menutup Changelog), langkah 16 dan 19 (ganti akun eksplisit, S-07), langkah 18 dan 21 (menunggu aksi selesai sebelum ganti akun atau membuka Changelog).
- `Box` tidak terhapus karena dilewati (in-use); Box Pre-setup hanya dicentang sebagai bagian aksi campuran dan tidak diubah (S-06). Sumber memakai `Liter`, `Pack`, dan `Box` literal; spec mengganti Liter dan Pack dengan unit milik spec bersuffix.
- Temuan untuk QA:
  - TC-GS-UOM-224 tidak menyebut surface dan akun pembaca untuk membandingkan Modified By; spec memakai Changelog (kolom Modified By, PRD §4.1.4/§8.1) dan membacanya sebagai aktor Delete.
  - TC-GS-UOM-224 menyebut aktor Create dan Delete tanpa menyebut akunnya; spec memakai System Role: Create dan Read (Rina Marlina) dan System Role: Delete dan Read (Dewi Lestari) dari Pre-setup TC.
  - TC-GS-UOM-220 dan 267 tidak punya Post Condition di luar Expected.
  - TC-GS-UOM-267 menulis "Buka Activity Log Global Settings" tanpa menyebut tab; log mutasi Measurement ada di tab `User Action` (`global-settings/activity-log/PRD/activity-log.md` §4.1.2), sehingga langkah 13 memilih tab `User Action` sebelum Search. Isi `Verifikasi` langkah 14 dan 15 tidak berubah.
