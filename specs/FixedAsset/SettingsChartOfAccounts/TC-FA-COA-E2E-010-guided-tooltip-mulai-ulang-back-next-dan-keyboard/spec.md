---
id: TC-FA-COA-E2E-010-guided-tooltip-mulai-ulang-back-next-dan-keyboard
title: "Guided Tooltip: Mulai Ulang, Back Next, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-338
  - TC-FA-COA-339
  - TC-FA-COA-342
coverage:
  web: automated
---

# Guided Tooltip: Mulai Ulang, Back Next, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control desktop `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Chart of Accounts bernilai true (user sudah pernah menyelesaikan tur) oleh hook suite `before`, sehingga tur hanya berjalan lewat `[?]` (butir "Flag Guided Tooltip" di `suite.md`).
- Kemampuan teknis: viewport desktop; keyboard (Enter, panah kiri, panah kanan, Esc). Flag tidak dibaca langsung; persistensi diamati lewat muat ulang halaman.
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-338: Tombol `[?]` memulai ulang tur tanpa mereset flag kunjungan

1. Klik `[?]` di kanan Breadcrumb
2. Verifikasi tur mulai dari step 1
3. Klik `[Next]` sampai tur berada di step 6
4. Klik `[Done]`
5. Muat ulang halaman
6. Verifikasi Breadcrumb `Settings > Accounting > Chart of Accounts` tampil
7. Verifikasi tur tidak mulai otomatis

### TC-FA-COA-339: Tombol Back tersembunyi di step pertama dan tombol Next berubah menjadi Done di step terakhir

8. Klik `[?]` di kanan Breadcrumb
9. Verifikasi tombol `[Next]` tampil pada step 1
10. Verifikasi tombol `[Back]` tidak tampil pada step 1
11. Klik `[Next]` sampai tur berada di step 6
12. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada step 6
13. Klik `[Done]`

### TC-FA-COA-342: Navigasi keyboard tur: Esc, Enter, panah kanan, dan panah kiri

14. Klik `[?]` di kanan Breadcrumb
15. Tekan Enter
16. Verifikasi tur pindah ke step 2
17. Tekan panah kiri
18. Verifikasi tur kembali ke step 1
19. Tekan panah kanan
20. Verifikasi tur pindah ke step 2
21. Tekan Esc
22. Verifikasi tur tertutup

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 4 dan 13 (menutup tur dengan `[Done]`); langkah 3 dan 11 ditulis sebagai satu langkah "Klik `[Next]` sampai step 6" (langkah berulang sebagai teks biasa).
- Asersi tambahan di luar Expected TC (S-03): langkah 6 menjadi anchor positif untuk absence tur (langkah 7) dan langkah 9 menjadi anchor positif untuk absence `[Back]` (langkah 10) (bagian 8b butir 2).
- Muat ulang halaman (langkah 5) adalah langkah observasi flag; flag tidak dibaca langsung (S-13).
- Temuan untuk QA:
  - TC-FA-COA-338 dan 339 langkah 2 menyebut "Selesaikan tur" tanpa menyebut tombol; spec menyelesaikan dengan `[Next]` sampai step 6 lalu `[Done]`.
  - TC-FA-COA-342 butir a menyebut "Enter atau panah kanan"; spec menguji keduanya berurutan (langkah 15 sampai 20).
