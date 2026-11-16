---
id: TC-FA-PREF-E2E-035-bulan-berjalan-mengikuti-time-zone-entitas-pada-pergantian-bulan
title: "Bulan Berjalan First Accounting Period Mengikuti Time Zone Entitas (Jakarta dan Honolulu) pada Pergantian Bulan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-150
  - TC-FA-PREF-151
  - TC-FA-PREF-599
  - TC-FA-PREF-600
sourceRules: ["FAPREF-LOGIC-02m", "FI-06", "FAPREF-LOGIC-02i"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-02m": [4, 11, 18, 23]
  "FI-06": [6, 12, 17]
  "FAPREF-LOGIC-02i": 24
coverage:
  web: automated
---

# Bulan Berjalan First Accounting Period Mengikuti Time Zone Entitas (Jakarta dan Honolulu) pada Pergantian Bulan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth) dengan Preferences nilai awal PA-2 dan PC-1 (setara: First Accounting Period Mar 2026, tidak terkunci; belum ada posting penyusutan; semua periode Open).
- Jam sistem dan Time Zone entitas (clock; jam server dan jam browser diatur bersama; bagian 6): TC-FA-PREF-150: 31 Oktober 2026 pukul 23:30 UTC, Asia/Jakarta (waktu entitas 1 November 2026 pukul 06:30; PA-18). TC-FA-PREF-151: 31 Oktober 2026 pukul 23:30 UTC, Pacific/Honolulu (waktu entitas 31 Oktober 2026 pukul 13:30; PA-19). TC-FA-PREF-599: 31 Oktober 2026 pukul 16:59 UTC, Asia/Jakarta (23:59 waktu entitas; PC-15). TC-FA-PREF-600: 31 Oktober 2026 pukul 17:00 UTC, Asia/Jakarta (1 November 2026 pukul 00:00 waktu entitas; PC-15). Perubahan Time Zone entitas dan jam disediakan tim FE/BE (butir "Kendali jam sistem" di `suite.md`). Hook `after` memulihkan jam sistem dan Time Zone entitas ke Asia/Jakarta. Suite serial.
- State yang diubah spec: jam sistem dan Time Zone entitas. Tidak ada Save; form dikembalikan ke nilai tersimpan pada langkah 7, 13, 19, dan 25.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-150: Bulan berjalan mengikuti Time Zone entitas Asia/Jakarta, 31 Oktober 23:30 UTC sudah November

1. Atur Time Zone entitas Asia/Jakarta dan jam server serta jam browser ke 31 Oktober 2026 pukul 23:30 UTC, lalu muat ulang halaman Preferences
2. Pilih tahun "2026" pada Select tahun First Accounting Period
3. Buka daftar opsi Select bulan dan pilih "November"
4. Verifikasi opsi "November" dapat dipilih dan Select bulan menampilkan "November"
5. Buka daftar opsi Select bulan
6. Verifikasi opsi "December" tidak dapat dipilih
7. Pilih bulan "March" pada Select bulan First Accounting Period

### TC-FA-PREF-151: Bulan berjalan mengikuti Time Zone entitas Pacific/Honolulu, 31 Oktober 23:30 UTC masih Oktober

8. Atur Time Zone entitas Pacific/Honolulu dan jam server serta jam browser ke 31 Oktober 2026 pukul 23:30 UTC, lalu muat ulang halaman Preferences
9. Pilih tahun "2026" pada Select tahun First Accounting Period
10. Buka daftar opsi Select bulan dan klik opsi "November"
11. Verifikasi opsi "October" dapat dipilih
12. Verifikasi opsi "November" tidak dapat dipilih
13. Pilih bulan "March" pada Select bulan First Accounting Period

### TC-FA-PREF-599: Bulan berjalan mengikuti Time Zone entitas sebelum pergantian bulan

14. Atur Time Zone entitas Asia/Jakarta dan jam server serta jam browser ke 31 Oktober 2026 pukul 16:59 UTC, lalu muat ulang halaman Preferences
15. Pilih tahun "2026" pada Select tahun First Accounting Period
16. Buka daftar opsi Select bulan dan amati opsi Oktober dan November
17. Verifikasi opsi November tidak dapat dipilih
18. Verifikasi opsi Oktober dapat dipilih
19. Pilih bulan "March" pada Select bulan First Accounting Period

### TC-FA-PREF-600: Bulan berjalan mengikuti Time Zone entitas tepat saat pergantian bulan

20. Atur Time Zone entitas Asia/Jakarta dan jam server serta jam browser ke 31 Oktober 2026 pukul 17:00 UTC, lalu muat ulang halaman Preferences
21. Pilih tahun "2026" pada Select tahun First Accounting Period
22. Buka daftar opsi Select bulan dan amati opsi Oktober dan November
23. Verifikasi opsi November dapat dipilih
24. Verifikasi opsi Oktober dapat dipilih
25. Pilih bulan "March" pada Select bulan First Accounting Period

## Notes

- Pengaturan jam dan Time Zone per TC (langkah 1, 8, 14, 20) dilakukan bersama jam server dan jam browser lalu halaman dimuat ulang saat form pristine, karena opsi bulan dihitung saat render.
- Langkah penghubung (S-03): langkah 1, 5, 7, 8, 13, 14, 19, 20, 25 (pengaturan jam, membuka ulang daftar opsi, dan mengembalikan First Accounting Period ke Mar 2026 agar form tidak berakhir dirty; S-09). Langkah 16 dan 22 ("amati") digabung dengan pembukaan daftar.
- Pada TC-FA-PREF-150, opsi "December" diasersi pada daftar yang dibuka ulang (langkah 5) karena pemilihan "November" pada langkah 3 menutup daftar.
- Temuan untuk QA:
  - TC-FA-PREF-150 dan 151 memuat langkah "pilih November" yang pada TC-FA-PREF-151 bersifat percobaan klik pada opsi yang tidak dapat dipilih; spec mengasersi opsi "October" lalu "November" seperti urutan Expected.
  - Mekanisme mengubah Time Zone entitas (PA-18, PA-19) tidak tertulis di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
  - Post Condition tidak ada pada keempat TC.
