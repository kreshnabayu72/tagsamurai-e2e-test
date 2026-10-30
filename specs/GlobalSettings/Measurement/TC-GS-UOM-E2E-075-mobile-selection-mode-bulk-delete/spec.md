---
id: TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete
title: "Mobile Android: Selection Mode Bulk Delete (Long-Press, Cancel, Commit, Tanpa Capability Delete)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-363
  - TC-GS-UOM-364
  - TC-GS-UOM-365
coverage:
  mobile: automated
---

# Mobile Android: Selection Mode Bulk Delete (Long-Press, Cancel, Commit, Tanpa Capability Delete)

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji dipakai bersama sehingga spec ini `parallel: false` (S-09).
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | System Role: Update dan Read (Agus Wijaya) | `updateOnly_automated_qaTeam1@qwertysystem.net` | `GS_UPDATE_PASSWORD` |

  Login akun 1 di hook `before` spec ini pada aplikasi Android (akun default suite); hook `after` mengembalikan sesi ke akun 1. Halaman awal: Global Settings > Master Reference > Tab Measurement.
- Environment variable: `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`, bagian Hook suite).
- Data Pre-setup Client A (hanya dibaca, tidak diubah, tanpa suffix `{runId}`): `Liter` (long-press oleh aktor tanpa capability Delete, TC-GS-UOM-365).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), bebas relasi, di-seed lewat API di hook `before`: `Meter {runId}-075` / `m` dan `Milliliter {runId}-075` / `mL` (dialog Delete dibatalkan pada TC-GS-UOM-363; pengganti Meter dan Milliliter literal); `Cup {runId}-075` / `cup` dan `Plate {runId}-075` / `plt` (D-21; terhapus Bulk Delete pada TC-GS-UOM-364).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Meter`, `Milliliter`, `Cup`, dan `Plate` bersuffix `{runId}-075` bila masih ada.
- Kemampuan teknis: gesture long-press dan tap pada card, serta pembukaan bottom sheet di perangkat atau emulator Android; ganti akun di aplikasi (logout lalu login).
- Tidak ada state global yang diubah.
- TC-GS-UOM-363, 364: login sebagai Total Control pada aplikasi Android. TC-GS-UOM-365: login sebagai System Role: Update dan Read.

## Test Steps

### TC-GS-UOM-363: Long-press card masuk selection mode Bulk Delete

1. Tap `[🔍]`, ketik `{runId}-075`, tekan Enter
2. Long-press card `Meter {runId}-075`
3. Verifikasi checkbox muncul di kiri tiap card
4. Verifikasi card `Meter {runId}-075` tercentang
5. Verifikasi header berubah menjadi `1 selected` dengan `[Cancel]`
6. Verifikasi bulk action bar muncul di bawah
7. Tap card `Milliliter {runId}-075`
8. Verifikasi header `2 selected`
9. Verifikasi Unit Detail tidak terbuka
10. Tap `Delete` pada bulk action bar
11. Verifikasi dialog `Delete Units` tampil sebagai bottom sheet dengan bullet `Meter {runId}-075` dan `Milliliter {runId}-075`
12. Klik [Cancel] pada dialog
13. Verifikasi `Meter {runId}-075` dan `Milliliter {runId}-075` tetap ada
14. Verifikasi selection mode tetap aktif
15. Tap `[Cancel]` di header untuk keluar dari selection mode

### TC-GS-UOM-364: Keluar selection mode lewat Cancel dan setelah Bulk Delete ter-commit

16. Ganti isi Search dengan `Cup {runId}-075`, tekan Enter, long-press card `Cup {runId}-075`, lalu tap `[Cancel]` di header
17. Verifikasi checkbox hilang dan header kembali normal
18. Verifikasi tidak ada unit terpilih
19. Ganti isi Search dengan `{runId}-075`, tekan Enter, long-press card `Cup {runId}-075`
20. Tap card `Plate {runId}-075`, lalu tap `Delete` pada bulk action bar
21. Klik [Delete] pada dialog
22. Verifikasi toast sukses: "Success, unit has been deleted."
23. Verifikasi card `Cup {runId}-075` dan `Plate {runId}-075` hilang dari daftar
24. Verifikasi selection mode berakhir otomatis

### TC-GS-UOM-365: Aktor tanpa capability Delete tidak dapat masuk selection mode

25. Ganti akun: logout, lalu login sebagai System Role: Update dan Read (`updateOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_UPDATE_PASSWORD`, lalu buka Global Settings > Master Reference > Tab Measurement
26. Ketik Search `Liter`, tekan Enter, long-press card `Liter`
27. Verifikasi selection mode tidak aktif; checkbox dan bulk action bar tidak muncul
28. Verifikasi tidak ada aksi Delete tersedia

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Spec mobile Android (`coverage.mobile: automated`), preseden `TC-GS-BRAND-E2E-074-mobile-card-list-dan-selection-mode`.
- Urutan TC di spec berbeda dari urutan sumber: 363 (dialog dibatalkan), 364 (commit Delete, aksi yang menghabisi data paling akhir di blok Total Control), lalu satu kali ganti akun (langkah 25) ke aktor tanpa capability Delete untuk 365.
- Langkah penghubung: langkah 1, 16, 19, dan 26 (mencari card target lewat Search inline), langkah 15 (keluar dari selection mode sebelum TC berikutnya, mengikuti Expected d TC-GS-UOM-363 "selection mode tetap aktif"), langkah 25 (ganti akun eksplisit, S-07).
- Langkah 16 sampai 18 memakai satu long-press dan `[Cancel]` (Langkah Uji 1 TC-GS-UOM-364); langkah 19 sampai 24 memakai long-press baru (Langkah Uji 2), karena selection mode berakhir setelah Cancel.
- Langkah 3 sampai 6 dipecah per klausa dari Expected a TC-GS-UOM-363 (checkbox, Meter tercentang, header `1 selected` dengan `[Cancel]`, bulk action bar).
- Sumber memakai `Meter`, `Milliliter`, `Cup`, dan `Plate` literal; spec memakai unit milik spec bersuffix `{runId}-075` (S-06, S-12). `Liter` Pre-setup hanya di-long-press oleh aktor tanpa capability Delete dan tidak diubah.
- Pembagian TC lintas spec: card list mobile dan menu card ada di spec 074; Bulk Delete web ada di spec 033 dan 034.
- Temuan untuk QA:
  - TC-GS-UOM-364 langkah 1 menyebut `Long-press card Cup, tap [Cancel]` tanpa menyebut card yang tampil setelah Search; spec memakai Search nama unit.
  - TC-GS-UOM-363, 364, dan 365 tidak punya Post Condition di luar Expected.
