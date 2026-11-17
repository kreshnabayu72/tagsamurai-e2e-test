---
id: TC-FA-PREF-E2E-165-d04-tombol-esc-setara-cancel-dan-klik-di-luar-dialog-tidak-menutup
title: "D-04: Tombol Esc Setara [Cancel] dan Klik Area di Luar Dialog Tidak Menutup Dialog"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-264
  - TC-FA-PREF-265
sourceRules: ["§4.5#b1", "F-FAPREF-02.k1c", "D-04"]
smoke: []
dependsOn: []
trace:
  "§4.5#b1": 4
  "F-FAPREF-02.k1c": 5
  "D-04": 10
coverage:
  web: automated
---

# D-04: Tombol Esc Setara [Cancel] dan Klik Area di Luar Dialog Tidak Menutup Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PB-1 (Preferences nilai awal; In-service Date Source "Activation date"), PB-2 (akun Chart of Accounts tersedia).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-264: Tombol Esc pada D-04 setara [Cancel]

1. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
2. Klik tab Chart of Accounts pada Settings > Accounting
3. Tekan tombol Esc pada keyboard
4. Verifikasi dialog D-04 tertutup
5. Verifikasi tab Preferences tetap aktif dan Select In-service Date Source masih menampilkan "Manual by Accounting"
6. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-265: Klik area di luar dialog D-04 tidak menutup dialog

7. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
8. Klik tab Chart of Accounts pada Settings > Accounting
9. Klik area backdrop gelap di luar dialog D-04
10. Verifikasi dialog D-04 tetap terbuka tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
11. Klik [Cancel] pada dialog D-04
12. Ubah Select In-service Date Source menjadi "Activation date"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6 dan 12 (mengembalikan Select ke nilai tersimpan agar form pristine, S-09), langkah 11 (menutup dialog D-04 yang tetap terbuka).
- Post Condition ("Preferences company belum berubah") tidak ada Save pada TC ini; nilai tersimpan tidak berubah.
- Temuan untuk QA:
  - TC-FA-PREF-264 tidak memuat langkah verifikasi dialog tampil sebelum Esc; spec mengikuti TC (dialog D-04 sudah diasersi pada spec lain untuk pemicu yang sama).
