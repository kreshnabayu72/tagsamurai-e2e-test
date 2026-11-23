---
id: TC-FA-PREF-E2E-028-role-matrix-tooltip-st-05-st-08-field-disabled-atau-terkunci
title: "Role Matrix: Visibilitas Tooltip ST-05 dan ST-08 pada Field Disabled atau Terkunci untuk Read Only dan Read + Update"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-51
  - TC-FA-PREF-66
  - TC-FA-PREF-88
  - TC-FA-PREF-245
  - TC-FA-PREF-246
  - TC-FA-PREF-247
sourceRules: ["§4.8#r4", "ST-08", "§4.5#b4", "ST-05", "§4.3#b1", "FAPREF-LOGIC-02e"]
smoke: []
dependsOn: []
trace:
  "§4.8#r4": [1, 9, 26]
  "ST-08": [3, 5, 7, 9, 10, 16, 20]
  "§4.5#b4": 7
  "ST-05": [14, 18, 25]
  "§4.3#b1": [14, 18, 25]
  "FAPREF-LOGIC-02e": [14, 18, 25]
coverage:
  web: automated
---

# Role Matrix: Visibilitas Tooltip ST-05 dan ST-08 pada Field Disabled atau Terkunci untuk Read Only dan Read + Update

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | Role | Email Pre-setup | Env var password | TC |
  |---|---|---|---|
  | Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-PREF-51, TC-FA-PREF-66, TC-FA-PREF-247, TC-FA-PREF-88, TC-FA-PREF-245 |
  | Manage accounting - Read + Update | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MARU_PASSWORD` | TC-FA-PREF-246 |

- Akun aktor pertama: Read Only. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke Manage accounting - Read + Update memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_RO_PASSWORD` dan `FA_MARU_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` dengan Preferences nilai awal PA-2 dan PB-1 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, tidak terkunci, semua setting wajib terisi). Langkah 1 sampai 11 memakai state tanpa kunci.
- Kunci aktif untuk langkah 13 sampai 26: posting penyusutan pertama sudah ada, Depreciation Run periode Mei 2026 berstatus Posted (PA-9; PB-7a). Dibentuk lewat fixture BE pada langkah 12 (disediakan tim FE/BE, tanpa endpoint karangan). Kondisi PA-9 dan PB-7a setara untuk spec ini.
- State yang diubah spec: kunci posting penyusutan pertama. Dipulihkan ke tanpa kunci (PA-2) di hook `after`. Spec tidak menyimpan perubahan Preferences.
- Kemampuan teknis: fixture BE untuk kunci dan pemulihan lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`); aksi keyboard Tab pada langkah 6 memakai aksi keyboard Spectra.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-51: Hover field Disabled bagi Read Only menampilkan tooltip ST-08

1. Verifikasi Select Default Gain on Disposal dan CurrencyInput Default Capitalization Threshold tetap tampil namun Disabled
2. Hover Select Default Gain on Disposal yang Disabled
3. Verifikasi tooltip "You don't have permission to edit." tampil pada Select Default Gain on Disposal
4. Hover CurrencyInput Default Capitalization Threshold yang Disabled
5. Verifikasi tooltip "You don't have permission to edit." tampil pada CurrencyInput Default Capitalization Threshold

### TC-FA-PREF-66: Tooltip field Disabled dapat diakses lewat keyboard focus

6. Pindahkan kursor keluar dari field Preferences, lalu tekan Tab hingga fokus berada pada Select Fiscal Year Start yang Disabled
7. Verifikasi tooltip "You don't have permission to edit." tampil saat Select Fiscal Year Start menerima fokus keyboard

### TC-FA-PREF-247: Read Only tanpa kunci aktif melihat tooltip ST-08 pada Fiscal Year Start

8. Arahkan kursor ke Select Fiscal Year Start
9. Verifikasi Select Fiscal Year Start tetap tampil (visible) namun Disabled tanpa ikon gembok
10. Verifikasi tooltip "You don't have permission to edit." tampil pada Select Fiscal Year Start

### Kunci aktif (posting penyusutan pertama)

11. Pindahkan kursor keluar dari field Preferences
12. Bentuk kunci posting penyusutan pertama (Depreciation Run periode Mei 2026 berstatus Posted) lewat fixture BE hingga tersimpan, lalu muat ulang halaman Preferences

### TC-FA-PREF-88: Read Only melihat tooltip ST-05 pada field terkunci dan ST-08 pada field Disabled lain

13. Hover Select Fiscal Year Start yang terkunci
14. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted. It cannot be changed from this page." tampil pada Select Fiscal Year Start
15. Hover CurrencyInput Default Capitalization Threshold yang Disabled
16. Verifikasi tooltip "You don't have permission to edit." tampil pada CurrencyInput Default Capitalization Threshold

### TC-FA-PREF-245: Read Only melihat tooltip ST-05 pada field terkunci dan ST-08 pada field Disabled lain

17. Arahkan kursor ke Select Fiscal Year Start
18. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted. It cannot be changed from this page." tampil pada Select Fiscal Year Start
19. Arahkan kursor ke Select In-service Date Source
20. Verifikasi tooltip "You don't have permission to edit." tampil pada Select In-service Date Source

### TC-FA-PREF-246: Read + Update melihat tooltip ST-05 pada field terkunci dan field lain tetap Enabled

21. Logout dari akun Read Only
22. Login sebagai Manage accounting - Read + Update (`manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MARU_PASSWORD`)
23. Buka Fixed Asset > Settings > Accounting > Preferences
24. Arahkan kursor ke Select bulan First Accounting Period
25. Verifikasi tooltip "First accounting period is locked because depreciation has been posted. It cannot be changed from this page." tampil pada First Accounting Period
26. Verifikasi Select In-service Date Source berstatus Enabled

## Notes

- Matriks visibilitas per role (bagian 3a): spec Role Matrix sendiri yang memuat tooltip tampil dan field Enabled; title tanpa kata Positif atau Negatif. Ditulis per blok karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`) dan Expected tiap TC berbeda.
- Urutan: TC tanpa kunci (TC-FA-PREF-51, 66, 247) lebih dulu, lalu TC dengan kunci (TC-FA-PREF-88, 245, 246), karena kunci dibentuk sekali lewat fixture BE (langkah 12) dan tidak dicabut di antara blok.
- Langkah penghubung (S-03): langkah 11, 12, 21, 22, 23 dan bagian "pindahkan kursor keluar" pada langkah 6.
- Tooltip diasersi tepat setelah hover atau fokus dan sebelum langkah yang mengubah state-nya (8b.5).
- Seri fixture: TC-FA-PREF-51, 66, 88 memakai PA, TC-FA-PREF-245 sampai 247 memakai PB; nilai awal PA-2 dan PB-1 setara, kunci PA-9 dan PB-7a setara, sehingga satu company dipakai.
- Temuan untuk QA:
  - TC-FA-PREF-247 tidak punya Expected tentang kondisi "tanpa kunci aktif" selain Precondition; spec memakai state tanpa kunci hasil seed sebelum langkah 12.
  - Email akun tidak ditulis utuh di TC (`{namaCompany}`); nama company perlu dikonfirmasi tim FE.
