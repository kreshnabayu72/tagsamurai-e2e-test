---
id: TC-FA-PREF-E2E-076-muat-ulang-f5-dan-tutup-tab-konfirmasi-bawaan-browser-dan-d04
title: "Muat Ulang F5 dan Tutup Tab: Konfirmasi Bawaan Browser Hanya untuk Form Dirty dan Tidak Memunculkan D-04"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-270
  - TC-FA-PREF-271
  - TC-FA-PREF-272
  - TC-FA-PREF-273
  - TC-FA-PREF-575
sourceRules: ["§4.2b#b5", "T-01", "F-FAPREF-01.k13", "D-04", "F-FAPREF-02.k1b"]
smoke: []
dependsOn: []
trace:
  "§4.2b#b5": 7
  "T-01": 16
  "F-FAPREF-01.k13": 19
  "D-04": 23
  "F-FAPREF-02.k1b": [25, 27]
anchor: [2, 5, 11, 18]
coverage:
  web: automated
---

# Muat Ulang F5 dan Tutup Tab: Konfirmasi Bawaan Browser Hanya untuk Form Dirty dan Tidak Memunculkan D-04

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-270 sampai 273 memakai PB-1 dan PB-2 (akun Chart of Accounts tersedia); TC-575 memakai PC-1. Nilai awal PB-1 dan PC-1 setara (In-service Date Source "Activation date", Default Capitalization Threshold 5.000.000).
- Dialog `beforeunload` browser ditangani deterministik oleh harness: dialog dikenali dan ditolak (halaman tetap) agar form dirty tidak hilang tak terkendali (S-08); kemampuan itu disediakan tim FE.
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini menyimpan In-service Date Source "Manual by Accounting" pada TC-273; pemulihan ke nilai awal dilakukan pada langkah 24 dan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-272: Muat ulang halaman dengan F5 saat form pristine tidak memunculkan konfirmasi

1. Tekan F5 untuk memuat ulang halaman
2. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser

### TC-FA-PREF-270: Muat ulang halaman dengan F5 saat form dirty memunculkan konfirmasi bawaan browser

3. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
4. Tekan F5 untuk memuat ulang halaman
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
6. Tolak konfirmasi bawaan browser agar halaman tetap
7. Verifikasi dialog D-04 tidak tampil
8. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-271: Menutup tab browser saat form dirty memunculkan konfirmasi bawaan browser

9. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
10. Tutup tab browser
11. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum tab ditutup
12. Tolak konfirmasi bawaan browser agar tab tetap terbuka
13. Ubah Select In-service Date Source menjadi "Activation date"

### TC-FA-PREF-273: Muat ulang halaman dengan F5 sesudah Save berhasil tidak memunculkan konfirmasi

14. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
15. Klik [Save changes]
16. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
17. Tekan F5 untuk memuat ulang halaman
18. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
19. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
20. Seed ulang Preferences ke PC-1 lewat API (In-service Date Source "Activation date") dan buka kembali Fixed Asset > Settings > Accounting > Preferences

### TC-FA-PREF-575: Meninggalkan halaman dengan form dirty menampilkan dialog Unsaved Changes

21. Ubah Default Capitalization Threshold menjadi "10000000"
22. Klik entri sidebar menu lain
23. Verifikasi dialog D-04 tampil tanpa Title dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
24. Klik [Leave]
25. Verifikasi halaman menu lain terbuka dan perubahan dibuang
26. Buka kembali Settings > Accounting > Preferences
27. Verifikasi Default Capitalization Threshold tampil Rp 5.000.000,00

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-272 ditaruh paling awal (form pristine), TC-273 dan TC-575 berurutan setelah TC dirty.
- Langkah penghubung (S-03): langkah 6 dan 12 (menolak konfirmasi bawaan browser agar halaman tetap, S-08), langkah 8 dan 13 (mengembalikan Select ke nilai tersimpan, S-09), langkah 20 (seed ulang ke PC-1 sebelum TC-575; memulihkan state TC-273), langkah 26 (membuka kembali halaman, aksi TC).
- Post Condition TC-273 ("tersimpan Manual by Accounting") diasersi pada langkah 19 (nilai tampil setelah muat ulang). Post Condition TC-575 ("threshold tersimpan tetap 5.000.000") diasersi pada langkah 27.
- Temuan untuk QA:
  - TC-FA-PREF-271 (tutup tab) tidak menyebut cara menolak konfirmasi; spec menolaknya agar sesi tidak terputus. Perilaku setelah konfirmasi ditolak tidak diasersi oleh TC.
