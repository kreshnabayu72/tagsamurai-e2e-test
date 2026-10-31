---
id: TC-GS-IMPORT-E2E-131-role-negatif-import-data-read-only-accept-dismiss-ai-dan-create-missing
title: "Role negatif Import data (Read Only): Accept, Dismiss AI, dan Create Missing (Divisions, Positions, Options) Disabled dengan tooltip izin"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-305
  - TC-GS-IMPORT-347
  - TC-GS-IMPORT-921
coverage:
  web: automated
---

# Role negatif Import data (Read Only): Accept, Dismiss AI, dan Create Missing (Divisions, Positions, Options) Disabled dengan tooltip izin

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (satu akun; tidak ada perulangan role):

| Role | Akun | Env var |
|---|---|---|
| Import data (Read Only) Client C (Hari Wibowo) | `importRead_automated_qaTeam3@qwertysystem.net` | `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD` |

- Akun penyiap draft: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`, hanya lewat sesi API di hook `before` dan di langkah penyiapan draft (bukan sesi UI kedua).
- Login akun Import data (Read Only) Client C sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Client C), Tab Brand; langkah pertama spec ini tidak membuka halaman lagi untuk TC-GS-IMPORT-305.
- Data Dinamis (fixture baru, berkas literal dari TC; dibuat lewat API oleh Total Control Client C):
  - `Fixture.import.aiBrandLong` (ai-brand-long.csv, D-44): draft Brand 1 baris `error` dengan Brand Name nilai sumber Brand pada D-41 (121 karakter) dan badge saran AI; layanan AI mock mode normal (D-40, D-41, D-42).
  - `Fixture.import.userLoginLogistik4` (user-login-logistik-4.csv, D-45): draft User Login 4 baris `error` dengan Division `Logistik` (Siti Rahmawati, Budi Santoso, Andi Pratama, Rina Wijaya).
  - `Fixture.import.userLoginShiftLembur` (user-login-shift-lembur.csv, D-79): draft User Login 3 baris, #1 dan #2 `error`, #3 `pending`.
- Kemampuan teknis yang disediakan tim FE/BE: mock layanan AI mode normal dengan pencatat jumlah permintaan (D-40) dan pengembalian ke normal di hook `after`; penyiapan dan penggantian draft Client C lewat sesi API Total Control Client C; reset draft Client C.
- Cleanup (hook `after`): hapus draft Client C (Tab Brand dan Tab User Login), kembalikan mock AI ke mode normal, pulihkan sesi ke akun default suite. Spec tidak mengubah data master.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- State global: mode mock AI (dipulihkan di `after`); suite berjalan serial.
- Env var yang dipakai: `GS_CLIENTC_IMPORTRO_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-305: Accept dan Dismiss Disabled untuk role tanpa capability Create

1. Siapkan draft Brand `ai-brand-long.csv` di Client C lewat sesi API Total Control Client C, lalu muat ulang halaman Import > Brand
2. Arahkan kursor ke `[Accept]` pada badge saran sel Brand Name baris #1
3. Verifikasi `[Accept]` tampil dalam keadaan Disabled
4. Verifikasi tooltip `[Accept]` "You don't have permission to do this."
5. Arahkan kursor ke `[Dismiss]` pada badge saran sel Brand Name baris #1
6. Verifikasi `[Dismiss]` tampil dalam keadaan Disabled
7. Verifikasi tooltip `[Dismiss]` "You don't have permission to do this."

### TC-GS-IMPORT-347: Create Missing Divisions Disabled pada menu row action dan Callout

8. Hapus draft Brand Client C dan siapkan draft User Login `user-login-logistik-4.csv` lewat sesi API Total Control Client C, lalu buka Import > User Login
9. Klik `⋯` pada baris #1
10. Arahkan kursor ke `[Create Missing Divisions]` pada menu `⋯`
11. Verifikasi `[Create Missing Divisions]` pada menu `⋯` tampil Disabled
12. Verifikasi tooltip `[Create Missing Divisions]` pada menu `⋯` "You don't have permission to do this."
13. Tutup menu `⋯`
14. Arahkan kursor ke `[Create Missing Divisions]` pada Error Summary Callout
15. Verifikasi `[Create Missing Divisions]` pada Error Summary Callout tampil Disabled
16. Verifikasi tooltip `[Create Missing Divisions]` pada Error Summary Callout "You don't have permission to do this."

### TC-GS-IMPORT-921: Create Missing Options Disabled pada menu row action dan Callout

17. Ganti draft User Login Client C dengan `user-login-shift-lembur.csv` lewat sesi API Total Control Client C, lalu muat ulang halaman Import > User Login
18. Klik `⋯` pada baris #1
19. Arahkan kursor ke `[Create Missing Options]` pada menu `⋯`
20. Verifikasi `[Create Missing Options]` pada menu `⋯` tampil Disabled
21. Verifikasi tooltip `[Create Missing Options]` pada menu `⋯` "You don't have permission to do this."
22. Tutup menu `⋯`
23. Arahkan kursor ke `[Create Missing Options]` pada Error Summary Callout
24. Verifikasi `[Create Missing Options]` pada Error Summary Callout tampil Disabled
25. Verifikasi tooltip `[Create Missing Options]` pada Error Summary Callout "You don't have permission to do this."

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-305, 347, 921).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan; tidak ada aksi tulis oleh role yang diuji, sehingga tidak ada langkah destruktif.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 17 (penyiapan atau penggantian draft sebagai precondition TC lewat sesi API Total Control Client C, tidak diasersi); langkah 9, 18 (membuka menu `⋯`) dan langkah 13, 22 (menutup menu).
- TC-GS-IMPORT-305, 347, dan 921 memakai draft yang disiapkan Total Control Client C sebagai precondition; sesi API itu hanya menyiapkan state (P-2) dan hasilnya tidak diasersi di sesi tersebut.
- Pasangan Disabled dan tooltip dipisah menjadi dua `Verifikasi` karena dua klausa yang dapat gagal sendiri (state tombol dan teks tooltip).
- Aksi baris kedua Create Missing yang serupa untuk role yang berhak (Create) ada di spec 132, dan visibilitas tombol pada role Total Control di spec 122.
- Temuan untuk QA:
  - TC-GS-IMPORT-347 menyebut berkas `user-login-logistik-4.csv` (D-45) tetapi tidak menyebut Position pada baris; D-45 hanya menyebut Division dan Position sesuai Data Uji tiap TC. Spec mengikuti Data Uji TC (Division `Logistik`, Position kosong).
  - Draft pada precondition TC-GS-IMPORT-305 (Brand `error` dengan badge saran) membutuhkan layanan AI mock D-40; TC tidak menyebut hook untuk membaca badge saran bila mock AI mati.
  - TC-GS-IMPORT-305, 347, dan 921 bertanda FE Test `Need API` tanpa menyebut endpoint penyiapan draft; spec memakai "sesi API Total Control Client C" sebagai kemampuan yang disediakan tim FE/BE (S-13).
