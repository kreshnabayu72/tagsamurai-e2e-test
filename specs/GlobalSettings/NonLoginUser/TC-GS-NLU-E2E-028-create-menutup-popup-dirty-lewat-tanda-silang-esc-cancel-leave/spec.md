---
id: TC-GS-NLU-E2E-028-create-menutup-popup-dirty-lewat-tanda-silang-esc-cancel-leave
title: "Create: menutup Popup dirty lewat tanda silang, Esc, Cancel, dan Leave"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-56
  - TC-GS-NLU-57
  - TC-GS-NLU-58
  - TC-GS-NLU-59
  - TC-GS-NLU-60
coverage:
  web: automated
---

# Create: menutup Popup dirty lewat tanda silang, Esc, Cancel, dan Leave

## Prerequisites

- Mode: FE+BE (backend nyata; jumlah total baris tabel dibaca dari backend nyata untuk memastikan tidak ada record dibuat).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 12, hanya dibaca): Non-Login User dasar pada tabel (sumber baseline jumlah baris).
- Data Dinamis: tidak ada; spec ini tidak menyimpan record (nilai First Name `Anton` tidak pernah disubmit). Tidak ada cleanup selain hook `after` suite.
- Kemampuan teknis: membaca jumlah total baris tabel (baseline B0).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

1. Catat jumlah total baris tabel Non-Login User sebagai baseline B0

### TC-GS-NLU-56: Menutup Popup Create dalam keadaan kosong

2. Klik `[+ Non-Login User]`
3. Klik `✕`
4. Verifikasi popup langsung tertutup tanpa dialog Unsaved Changes
5. Klik `[+ Non-Login User]`
6. Tekan `Esc`
7. Verifikasi popup langsung tertutup tanpa dialog Unsaved Changes

### TC-GS-NLU-57: Menutup Popup yang sudah terisi via tanda silang

8. Klik `[+ Non-Login User]`
9. Isi First Name `Anton`
10. Klik `✕`
11. Verifikasi dialog Unsaved Changes tampil: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
12. Verifikasi Popup Create masih terbuka di belakang dialog

### TC-GS-NLU-59: Klik Cancel mempertahankan isian

13. Klik `[Cancel]` pada dialog
14. Verifikasi dialog tertutup dan Popup Create tetap terbuka
15. Verifikasi First Name tetap `Anton`

### TC-GS-NLU-58: Menutup Popup yang sudah terisi via Esc

16. Tekan `Esc`
17. Verifikasi dialog Unsaved Changes tampil: `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`

### TC-GS-NLU-60: Klik Leave membuang isian dan menutup popup

18. Klik `[Cancel]` pada dialog
19. Klik `✕`
20. Klik `[Leave]` pada dialog
21. Verifikasi dialog dan popup tertutup
22. Verifikasi jumlah total baris tabel sama dengan baseline B0 (tidak ada record baru)
23. Klik `[+ Non-Login User]`
24. Verifikasi Popup Create yang dibuka ulang kosong
25. Klik `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC-GS-NLU-56, 57, 59, 58, 60 mengikuti state popup (TC-GS-NLU-59 dan TC-GS-NLU-60 bergantung pada dialog dari TC-GS-NLU-57; kasus menutup form berurutan satu pembukaan; bagian 3 dan S-10). Popup dari TC-GS-NLU-57 dilanjutkan untuk TC-GS-NLU-58 (Esc pada popup terisi `Anton` yang sama) dan TC-GS-NLU-60 sehingga tiap TC tidak mengulang pembukaan dan pengisian.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline B0 untuk klausa "tidak ada record baru"), langkah 18 (menutup dialog hasil `Esc` sebelum TC-GS-NLU-60 mengklik `✕` sendiri; S-09), langkah 25 (menutup popup kosong).
- Temuan untuk QA:
  - TC-GS-NLU-58 dan TC-GS-NLU-60 menyatakan precondition popup baru terisi `Anton`; spec memakai popup yang sama sejak TC-GS-NLU-57 karena isian dan dialog identik.
  - TC-GS-NLU-56 Expected a/b tidak menyebut cara membuktikan "tanpa dialog" selain ketiadaan dialog; spec mengasersi popup tertutup langsung dan ketiadaan dialog dalam satu Verifikasi.
