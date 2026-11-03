---
id: TC-GS-NLU-E2E-039-popup-select-user-column-visibility-dan-setup-column-bagian
title: "Popup Select User: Column Visibility dan Setup Column bagian 1"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-121
  - TC-GS-NLU-122
  - TC-GS-NLU-124
  - TC-GS-NLU-125
coverage:
  web: automated
---

# Popup Select User: Column Visibility dan Setup Column bagian 1

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 dengan Ahmad Fauzi (tanpa TAG dan Blood Type) dan Rudi Setiawan (Temporary aktif, TAG `04A1B2C3`, Blood Type `O`), keduanya berada di halaman pertama (urutan Name A-Z); Custom Field dasar Blood Type (No. 13, Active). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Format tanggal kolom Temporary Until mengikuti General Settings (Date Format `dd/MM/yy`, Pre-setup No. 16); tanggal Rudi Setiawan dibaca dari selnya.
- State global: konfigurasi kolom Setup Column Popup Select User disimpan di browser. Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE dan dinyatakan di `suite.md`.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-121: Screening overlay Column Visibility Popup Select User

3. Klik ikon `⋯` pada header kolom Actions
4. Verifikasi overlay menampilkan daftar kolom berurutan Name, Email, Position, Division, Status dengan checkbox ☑ checked dan enabled
5. Verifikasi overlay menampilkan kolom curated Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif dengan checkbox ☐ unchecked dan enabled
6. Verifikasi setiap kolom punya drag handle
7. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-GS-NLU-122: Screening Popup Setup Column pada Popup Select User

8. Klik item `Setup Column...`
9. Verifikasi header menampilkan Title `Setup Column`
10. Verifikasi header menampilkan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi header menampilkan tombol `✕`
12. Verifikasi body menampilkan daftar kolom dengan checkbox status default
13. Verifikasi body menampilkan drag handle pada setiap kolom
14. Verifikasi body menampilkan ikon Pin pada setiap kolom
15. Verifikasi body menampilkan Live Preview urutan header dan data sel
16. Verifikasi footer menampilkan `[Reset to Default]` dan `[Save]`
17. Verifikasi footer tidak memiliki `[Cancel]`

### TC-GS-NLU-124: Ceklis kolom curated Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif

18. Centang Activation Status, Temporary User, Temporary Until, TAG, dan Blood Type
19. Klik `[Save]`
20. Verifikasi kolom Activation Status menampilkan badge `Activated`
21. Verifikasi kolom Temporary User menampilkan `Yes` atau `No`
22. Verifikasi kolom Temporary Until menampilkan tanggal Rudi Setiawan sesuai General Settings dan `—` untuk Ahmad Fauzi
23. Verifikasi kolom TAG menampilkan `04A1B2C3` untuk Rudi Setiawan dan `—` untuk Ahmad Fauzi
24. Verifikasi kolom Blood Type menampilkan `O` untuk Rudi Setiawan dan `—` untuk Ahmad Fauzi
25. Muat ulang halaman, buka Popup Create Non-Login User lalu Popup Select User
26. Verifikasi pengaturan kolom curated tetap setelah muat ulang

### TC-GS-NLU-125: Drag reorder kolom pada Setup Column Popup Select User

27. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
28. Drag Status ke posisi sebelum Name
29. Verifikasi Live Preview mengikuti urutan baru dengan Status paling kiri
30. Klik `[Save]`
31. Verifikasi tabel mengikuti urutan baru dengan Status paling kiri
32. Muat ulang halaman, buka Popup Create Non-Login User lalu Popup Select User
33. Verifikasi Status tetap paling kiri setelah muat ulang
34. Klik `[Cancel]`
35. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-GS-NLU-123 dan TC-GS-NLU-126 sampai TC-GS-NLU-130 (Setup Column lainnya) ada di spec 040 dan 129.
- Urutan: TC-GS-NLU-124 dan TC-GS-NLU-125 dilanjutkan dari dialog Setup Column yang sama; TC-GS-NLU-125 memakai kolom Status dan Name yang tetap tampil pada hasil TC-GS-NLU-124.
- Langkah penghubung tanpa `Verifikasi`: langkah 25 dan 32 (muat ulang halaman dan membuka kembali popup untuk asersi persisten) dan langkah 34 sampai 35 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- Muat ulang dilakukan saat Popup Create tidak dirty sehingga tidak memicu dialog `beforeunload`.
- Temuan untuk QA:
  - TC-GS-NLU-121 menyebut "header kolom Actions" untuk ikon `⋯`, sedangkan TC-GS-NLU-102 menamai kolom itu "Column Visibility (⋯)". Spec memakai ikon `⋯` pada header kolom terakhir tabel.
  - TC-GS-NLU-124 Expected butir a tidak menyebut baris pembanding selain Rudi Setiawan dan Ahmad Fauzi untuk kolom Activation Status dan Temporary User ("`Yes`/`No`" tanpa baris); spec mengasersi sedikitnya satu nilai `Yes` atau `No` per kolom tanpa memetakan ke baris tertentu.
