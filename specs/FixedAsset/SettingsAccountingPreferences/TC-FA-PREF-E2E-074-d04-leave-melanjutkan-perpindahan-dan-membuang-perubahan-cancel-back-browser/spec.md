---
id: TC-FA-PREF-E2E-074-d04-leave-melanjutkan-perpindahan-dan-membuang-perubahan-cancel-back-browser
title: "D-04: [Leave] Melanjutkan Perpindahan (Tab, Sidebar, Back Browser) dan Membuang Perubahan; [Cancel] pada Back Browser"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-261
  - TC-FA-PREF-262
  - TC-FA-PREF-613
  - TC-FA-PREF-614
coverage:
  web: automated
---

# D-04: [Leave] Melanjutkan Perpindahan (Tab, Sidebar, Back Browser) dan Membuang Perubahan; [Cancel] pada Back Browser

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-261 dan 262 memakai PB-1 dan PB-2 (akun Chart of Accounts tersedia); TC-613 dan 614 memakai PC-1. Nilai awal PB-1 dan PC-1 setara (In-service Date Source "Activation date").
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan; seri fixture dialihkan dari PB-1 ke PC-1 pada langkah 16.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-261: Klik [Leave] pada D-04 melanjutkan perpindahan ke tab Chart of Accounts dan membuang perubahan

1. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
2. Klik tab Chart of Accounts pada Settings > Accounting
3. Klik [Leave] pada dialog D-04
4. Verifikasi dialog D-04 tertutup dan tab Chart of Accounts aktif
5. Klik tab Preferences
6. Verifikasi Select In-service Date Source menampilkan "Activation date"
7. Verifikasi [Save changes] dan [Cancel] berstatus Disabled karena form pristine
8. Verifikasi tidak ada toast

### TC-FA-PREF-262: Klik [Leave] pada D-04 melanjutkan perpindahan lewat sidebar dan membuang perubahan

9. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
10. Klik salah satu entri menu sidebar selain Accounting
11. Klik [Leave] pada dialog D-04
12. Verifikasi dialog D-04 tertutup dan halaman entri sidebar yang diklik tampil
13. Buka kembali Settings > Accounting > Preferences
14. Verifikasi Select In-service Date Source menampilkan "Activation date"
15. Verifikasi tidak ada toast
16. Seed ulang Preferences ke PC-1 lewat API (nilai awal setara PB-1) dan buka kembali Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-613: Klik [Leave] pada D-04 yang muncul dari tombol Back browser meninggalkan halaman dan membuang perubahan

17. Klik tab Chart of Accounts pada Settings > Accounting
18. Klik tab Preferences pada Settings > Accounting
19. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
20. Tekan tombol Back browser
21. Klik [Leave] pada dialog D-04
22. Verifikasi dialog D-04 tertutup dan halaman sebelumnya pada riwayat browser (Settings > Accounting > Chart of Accounts) tampil
23. Buka kembali Settings > Accounting > Preferences
24. Verifikasi Select In-service Date Source menampilkan "Activation date"
25. Verifikasi tidak ada toast

### TC-FA-PREF-614: Klik [Cancel] pada D-04 yang muncul dari tombol Back browser tetap pada tab Preferences dengan form dirty

26. Klik tab Chart of Accounts pada Settings > Accounting
27. Klik tab Preferences pada Settings > Accounting
28. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
29. Tekan tombol Back browser
30. Klik [Cancel] pada dialog D-04
31. Verifikasi dialog D-04 tertutup
32. Verifikasi tab Preferences tetap tampil dan Select In-service Date Source masih menampilkan "Manual by Accounting"
33. Verifikasi [Save changes] dan [Cancel] form berstatus Enabled
34. Ubah Select In-service Date Source menjadi "Activation date"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 16 (seri fixture berganti dari PB-1 ke PC-1), langkah 17 dan 18 serta 26 dan 27 (membentuk riwayat browser dari Chart of Accounts ke Preferences sesuai Precondition d TC-613 dan 614), langkah 34 (mengembalikan Select ke nilai tersimpan, S-09).
- Post Condition ("Preferences company belum berubah, In-service Date Source tetap Activation date") diasersi pada langkah 6, 14, 24 setelah perubahan dibuang; pada TC-614 tidak ada Save sehingga nilai tersimpan tidak berubah.
- Temuan untuk QA:
  - TC-FA-PREF-261, 262, 613 menyebut `[Leave]` tanpa sebutan Expected "dialog D-04 tampil" sebelum klik; dialog D-04 sendiri diasersi pada spec lain (D-04 tampil) dan di sini diasumsikan tampil sebagai prasyarat klik [Leave].
  - Entri sidebar pada TC-262 tidak disebut namanya; spec memilih entri apa pun selain Accounting.
