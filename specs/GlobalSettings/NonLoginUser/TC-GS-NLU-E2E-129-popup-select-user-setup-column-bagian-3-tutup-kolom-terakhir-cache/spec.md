---
id: TC-GS-NLU-E2E-129-popup-select-user-setup-column-bagian-3-tutup-kolom-terakhir-cache
title: "Popup Select User: Setup Column bagian 3 (tutup tanpa Save, kolom terakhir, cache)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-128
  - TC-GS-NLU-129
  - TC-GS-NLU-130
coverage:
  web: automated
---

# Popup Select User: Setup Column bagian 3 (tutup tanpa Save, kolom terakhir, cache)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (semua Active). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- State global: konfigurasi kolom Setup Column Popup Select User dan tabel List Non-Login User disimpan di browser (TC-GS-NLU-130). Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE. Spec ini memakai Setup Column sehingga nomornya perlu terdaftar pada daftar pemulihan Setup Column di `suite.md`.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-128: Menutup Setup Column Popup Select User tanpa Save membuang perubahan

3. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
4. Hapus centang kolom Email
5. Klik `✕`
6. Verifikasi modal Setup Column tertutup
7. Verifikasi kolom Email kembali tampil di tabel (perubahan dibuang)
8. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
9. Hapus centang kolom Email
10. Tekan `Esc`
11. Verifikasi modal Setup Column tertutup (cara `Esc`)
12. Verifikasi kolom Email kembali tampil di tabel (cara `Esc`)

### TC-GS-NLU-129: Kolom visible terakhir pada Setup Column Popup Select User tidak bisa dihapus centang

13. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
14. Hapus centang semua kolom kecuali Name
15. Hover checkbox Name
16. Verifikasi checkbox Name disabled
17. Verifikasi tooltip `At least one column must remain visible.`
18. Klik `✕` pada modal Setup Column untuk membuang perubahan

### TC-GS-NLU-130: Cache Setup Column Popup Select User independen dari tabel List Non-Login User

19. Klik ikon `⋯` pada header kolom Actions > `Setup Column...` lalu hapus centang kolom Email
20. Klik `[Save]`
21. Klik `[Cancel]`
22. Klik `✕` pada Popup Create Non-Login User
23. Klik ikon `⋯` pada header kolom tabel List Non-Login User > `Setup Column...`
24. Verifikasi kolom Email tetap tercentang pada Setup Column tabel List Non-Login User
25. Hapus centang kolom Position lalu klik `[Save]`
26. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
27. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka
28. Verifikasi kolom Position tetap tampil di Popup Select User
29. Klik `[Cancel]`
30. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-GS-NLU-121 sampai TC-GS-NLU-127 (Setup Column lainnya) ada di spec 039 dan 040.
- Langkah penghubung tanpa `Verifikasi`: langkah 18 (menutup dialog Setup Column yang berubah tanpa Save), langkah 21 sampai 22 (menutup popup sebagai langkah 2 TC-GS-NLU-130; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes), dan langkah 29 sampai 30.
- Temuan untuk QA:
  - TC-GS-NLU-130 langkah 1 tidak menyebut pembukaan Popup Create dan Popup Select User dan tidak menyebut cara membuka Setup Column tabel List Non-Login User (langkah 2). Spec membuka popup dari awal dan memakai ikon `⋯` pada header kolom tabel List dengan pola yang sama.
  - TC-GS-NLU-130 Expected butir a ("Perubahan di Popup Select User tidak memengaruhi kolom List") diasersi lewat Setup Column List yang masih mencentang Email, dan butir b lewat kolom Position yang tetap tampil di popup.
  - TC-GS-NLU-128 menyebut "ulangi dengan Esc" tanpa menyebut ulang langkah buka; spec mengulang pembukaan Setup Column dan penghapusan centang Email sebelum `Esc`.
