---
id: TC-GS-NLU-E2E-034-popup-select-user-select-error-tanpa-pilihan-cancel-dan
title: "Popup Select User: Select, error tanpa pilihan, Cancel dan tutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-105
  - TC-GS-NLU-106
  - TC-GS-NLU-107
coverage:
  web: automated
---

# Popup Select User: Select, error tanpa pilihan, Cancel dan tutup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (Andi Wijaya, Dewi Anggraini). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Kemampuan teknis: jumlah total record tabel List Non-Login User dibaca sebagai baseline sebelum aksi pertama (dipakai pada TC-GS-NLU-105 untuk asersi tidak ada record baru); kemampuan baca disediakan tim FE/BE.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah total record tabel List Non-Login User sebagai baseline
2. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
3. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-106: Select tanpa baris terpilih menampilkan error inline dan popup tetap terbuka

4. Verifikasi `[Select]` tetap enabled sebelum diklik
5. Klik `[Select]` tanpa memilih baris
6. Verifikasi teks error `You must pick a user` tampil tanpa titik di akhir
7. Verifikasi teks error tampil rata kanan di atas tombol footer
8. Verifikasi teks error berwarna danger
9. Verifikasi Popup Select User tetap terbuka

### TC-GS-NLU-107: Cancel dan icon close menutup Popup Select User tanpa mengubah Represented By

10. Klik baris Andi Wijaya
11. Klik `[Cancel]`
12. Verifikasi Popup Select User tertutup tanpa dialog Unsaved Changes (cara `[Cancel]`)
13. Verifikasi field Represented By tetap `[+ Select User]` (cara `[Cancel]`)
14. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka
15. Klik baris Andi Wijaya
16. Klik `✕`
17. Verifikasi Popup Select User tertutup tanpa dialog Unsaved Changes (cara `✕`)
18. Verifikasi field Represented By tetap `[+ Select User]` (cara `✕`)
19. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka
20. Tekan `Esc`
21. Verifikasi Popup Select User tertutup tanpa dialog Unsaved Changes (cara `Esc`)
22. Verifikasi field Represented By tetap `[+ Select User]` (cara `Esc`)

### TC-GS-NLU-105: Select dengan satu baris terpilih menutup popup dan menampilkan badge Represented By

23. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka
24. Klik baris Dewi Anggraini
25. Klik `[Select]`
26. Verifikasi Popup Select User tertutup dan Popup Create masih terbuka
27. Verifikasi field Represented By berubah menjadi badge `Dewi Anggraini` dengan ikon edit `✎` di sisi kanan
28. Verifikasi tidak ada toast
29. Verifikasi jumlah total record tabel List Non-Login User sama dengan baseline langkah 1
30. Klik `✕` pada Popup Create Non-Login User
31. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-GS-NLU-106 (error, diblokir), TC-GS-NLU-107 (tutup tanpa memilih), lalu TC-GS-NLU-105 (aksi sukses). TC-GS-NLU-107 mengharapkan Represented By tetap `[+ Select User]`, yang hanya benar sebelum TC-GS-NLU-105 memilih user; TC-GS-NLU-105 dijalankan terakhir.
- Langkah 1: baseline jumlah total record (aksi tanpa `Verifikasi`). Langkah 30 sampai 32: menutup Popup Create yang dirty secara deterministik (S-08); `Verifikasi` dialog Unsaved Changes tidak perlu dicatat lagi.
- Temuan untuk QA:
  - TC-GS-NLU-105 Expected butir c ("tidak ada record baru") tidak menyebut cara membaca record; spec memakai jumlah total record tabel sebelum dan sesudah. Cara membaca jumlah itu tidak disebut TC, PRD, atau LLD sehingga dicatat sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-NLU-106 Expected butir a meminta `[Select]` enabled sebelum diklik tanpa menyebut elemen pembandingnya; spec mengasersi state enabled apa adanya.
