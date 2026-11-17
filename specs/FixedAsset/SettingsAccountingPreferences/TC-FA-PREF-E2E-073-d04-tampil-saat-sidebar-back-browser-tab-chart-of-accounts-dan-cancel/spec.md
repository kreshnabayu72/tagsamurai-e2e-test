---
id: TC-FA-PREF-E2E-073-d04-tampil-saat-sidebar-back-browser-tab-chart-of-accounts-dan-cancel
title: "D-04: Dialog Unsaved Changes Tampil Saat Sidebar, Back Browser, dan Tab Chart of Accounts dengan Form Dirty; [Cancel] Tetap pada Tab Preferences"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-258
  - TC-FA-PREF-259
  - TC-FA-PREF-260
  - TC-FA-PREF-263
sourceRules: ["D-04", "§4.2b#r13", "F-FAPREF-02.k1c", "§4.2b#b6", "ST-01"]
smoke: []
dependsOn: []
trace:
  "D-04": [3, 11, 17]
  "§4.2b#r13": 3
  "F-FAPREF-02.k1c": [4, 12, 18, 24, 25]
  "§4.2b#b6": [4, 11, 12, 17, 18]
  "ST-01": 26
coverage:
  web: automated
---

# D-04: Dialog Unsaved Changes Tampil Saat Sidebar, Back Browser, dan Tab Chart of Accounts dengan Form Dirty; [Cancel] Tetap pada Tab Preferences

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PB-1 (Preferences nilai awal; In-service Date Source "Activation date"), PB-2 (akun Chart of Accounts tersedia).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan; tiap TC mengembalikan Select ke nilai tersimpan lewat langkah eksplisit.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-258: D-04 tampil saat entri sidebar lain diklik dengan form dirty

1. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
2. Klik salah satu entri menu sidebar selain Accounting
3. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
4. Verifikasi perpindahan halaman ditahan: tab Preferences masih tampil dengan nilai "Manual by Accounting"
5. Klik [Cancel] pada dialog D-04
6. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-259: D-04 tampil saat tombol Back browser ditekan dengan form dirty

7. Klik tab Chart of Accounts pada Settings > Accounting
8. Klik tab Preferences pada Settings > Accounting
9. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
10. Tekan tombol Back browser
11. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
12. Verifikasi perpindahan halaman ditahan: tab Preferences masih tampil dengan nilai "Manual by Accounting"
13. Klik [Cancel] pada dialog D-04
14. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-260: D-04 tampil saat berpindah ke tab Chart of Accounts dengan form Preferences dirty

15. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
16. Klik tab Chart of Accounts pada Settings > Accounting
17. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
18. Verifikasi tab Preferences tetap aktif dengan nilai "Manual by Accounting" selama dialog tampil
19. Klik [Cancel] pada dialog D-04
20. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-263: Klik [Cancel] pada D-04 tetap pada tab Preferences dengan form dirty

21. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
22. Klik tab Chart of Accounts pada Settings > Accounting
23. Klik [Cancel] pada dialog D-04
24. Verifikasi dialog D-04 tertutup
25. Verifikasi tab Preferences tetap aktif dan Select In-service Date Source masih menampilkan "Manual by Accounting"
26. Verifikasi [Save changes] dan [Cancel] form berstatus Enabled
27. Ubah Select In-service Date Source menjadi "Activation date"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 13, 19 (menutup dialog D-04 lewat [Cancel], bagian dari kondisi uji), langkah 6, 14, 20, 27 (mengembalikan Select ke nilai tersimpan agar form pristine sebelum TC berikutnya, S-09), langkah 7 dan 8 (membentuk riwayat browser Chart of Accounts lalu Preferences sesuai Precondition d TC-259).
- D-04 tanpa Title; teks body dan tombol diverifikasi persis seperti TC (S-02).
- Post Condition ("Preferences company belum berubah, In-service Date Source tetap Activation date") tidak ada Save pada TC ini; nilai tersimpan tidak berubah dan dikembalikan pada langkah 6, 14, 20, 27.
- Temuan untuk QA:
  - TC-FA-PREF-258 dan 267 menyebut "salah satu entri menu sidebar selain Accounting" tanpa menamai entrinya; spec memilih entri apa pun yang tersedia untuk Total Control.
  - TC-FA-PREF-259 tidak menyebut entri riwayat yang dituju Back browser; spec hanya memverifikasi dialog dan penahanan di tab Preferences.
