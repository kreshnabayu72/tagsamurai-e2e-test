---
id: TC-FA-COA-E2E-085-role-matrix-visibilitas-elemen-update-delete-dan-default-user
title: "Role Matrix: Visibilitas Elemen Update + Delete dan Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-363
  - TC-FA-COA-364
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Update + Delete dan Default User

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Manage accounting – Update + Delete (akun pertama, login di hook `before`) | `manageAccountingUpdateDelete_automated_{namaCompany}@qwertysystem.net` (gabungan huruf; asumsi pre-setup, bukan data PRD) | `Spectra.env.FA_MACC_UPDDEL_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; perlu didaftarkan tim FE) | TC-FA-COA-363 |
| Default User (Total Control permanen) | `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` (asumsi pre-setup, bukan data PRD) | `Spectra.env.FA_DU_PASSWORD` (sudah terdaftar dengan keterangan "Default User (#57)"; kesamaan akun dengan `defaultUserFixedAsset_automated_{namaCompany}` perlu dikonfirmasi tim FE) | TC-FA-COA-364 |

- Login akun pertama (Manage accounting – Update + Delete) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` spec mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001` (Active). Form Add Account pada TC-FA-COA-364 hanya dibuka dan ditutup tanpa diisi.
- Kemampuan teknis: klien HTTP untuk permintaan langsung Create Account (TC-FA-COA-363) dengan sesi API akun Manage accounting – Update + Delete (butir "Sesi API aktor" di `suite.md`). Endpoint Create Account tidak tertulis di TC; disediakan tim FE/BE (S-13). Spec hanya mengasersi status respons (bagian 8b butir 1).
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk kedua akun di tabel (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-363: Visibilitas elemen dan batas akses untuk Manage accounting – Update + Delete (gabungan huruf)

1. Ketik Search `5-6001`, tekan Enter
2. Verifikasi `+ Account` Hidden
3. Verifikasi Switch Status baris P1 Show dan Enabled
4. Centang baris P1
5. Verifikasi Checkbox dan Bulk Action Bar Show
6. Verifikasi Bulk Action memuat `Deactivate` dan `Delete` untuk seleksi P1 (Active)
7. Klik `Unselect All`
8. Verifikasi ⋯ per baris P1 Show
9. Klik ⋯ pada baris P1
10. Verifikasi row action `Edit` dan `Delete` Show
11. Tekan Esc
12. Kirim permintaan langsung Create Account lewat klien HTTP dengan sesi API akun ini
13. Verifikasi permintaan langsung Create Account ditolak server dengan 403
14. Klik `(←)` pada kotak Search

### TC-FA-COA-364: Default User memiliki akses setara Total Control: seluruh elemen Show dan Enabled tanpa batasan

15. Logout dari akun Manage accounting – Update + Delete
16. Login sebagai Default User
17. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
18. Verifikasi menu `Accounting` pada sidebar Show dan Enabled
19. Verifikasi Search, Filter, Download, Changelog, dan `+ Account` di toolbar Show dan Enabled
20. Ketik Search `5-6001`, tekan Enter
21. Verifikasi Switch Status baris P1 Show dan Enabled
22. Verifikasi Checkbox baris P1 Show dan Enabled
23. Verifikasi ⋯ per baris P1 Show dan Enabled
24. Klik ⋯ pada baris P1
25. Verifikasi row action `Edit` dan `Delete` Show dan Enabled
26. Tekan Esc
27. Klik `+ Account`
28. Verifikasi modal Add Account terbuka
29. Klik `✕` di header modal Add Account
30. Centang baris P1
31. Verifikasi Bulk Action memuat `Deactivate` dan `Delete` untuk seleksi P1 (Active)
32. Klik `Unselect All`
33. Verifikasi tidak ada elemen Hidden atau Disabled pada menu, toolbar, Switch Status, Checkbox, Bulk Action, dan ⋯ per baris
34. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix visibilitas (bagian 3a): matriks elemen per role boleh memuat polaritas Show dan Hidden/Disabled dalam satu spec. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`) dan langkah per role berbeda (TC-FA-COA-363 memuat permintaan langsung; TC-FA-COA-364 membuka modal Add Account). Satu spec memuat dua role karena daftar elemen yang diperiksa sama.
- Langkah penghubung (S-03): langkah 1 dan 20 (Search untuk menampilkan baris P1; R-16, bagian 8b butir 12); langkah 4, 7, 30, dan 32 (menyiapkan seleksi lalu `Unselect All`, S-09); langkah 9, 11, 24, dan 26 (membuka dan menutup menu ⋯); langkah 14 dan 34 (menutup Search dan mereset tabel, S-09); langkah 15 sampai 17 (ganti akun eksplisit, S-07); langkah 29 (menutup modal Add Account yang tidak diisi, form tidak dirty sehingga dialog `Unsaved Changes` tidak diharapkan).
- Asersi tambahan di luar Expected TC (S-03): absence Hidden pada langkah 2 memakai langkah 3 (Switch Status Show) sebagai anchor permukaan (bagian 8b butir 2); langkah 33 meringkas Expected d TC-FA-COA-364 ("Tidak ada elemen Hidden atau Disabled") atas elemen yang diasersi langkah 18 sampai 31.
- Permintaan langsung (langkah 12 dan 13) hanya mengasersi status respons; tampilan FE untuk respons yang sama tidak diasersi (bagian 8b butir 1). Langkah 12 menyebut sesi API akun (butir "Sesi API aktor" di `suite.md`).
- Pembagian TC lintas spec: TC-FA-COA-10 dan TC-FA-COA-11 ada di spec 005.
- Temuan untuk QA:
  - TC-FA-COA-363 Post Condition "Tidak ada akun baru dan tidak ada log" tidak punya langkah observasi; hanya status 403 yang diasersi (langkah 13).
  - Akun Manage accounting – Update + Delete dan Default User adalah asumsi pre-setup (tabel Data Uji Pre-setup TC), bukan data PRD; password Default User memakai `FA_DU_PASSWORD` yang sudah terdaftar dengan keterangan modul lain.
  - TC-FA-COA-363 tidak menyebut endpoint atau payload Create Account untuk permintaan langsung; disediakan tim FE/BE.
