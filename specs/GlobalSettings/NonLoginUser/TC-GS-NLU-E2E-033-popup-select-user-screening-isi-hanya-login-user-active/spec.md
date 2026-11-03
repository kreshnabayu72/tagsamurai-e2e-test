---
id: TC-GS-NLU-E2E-033-popup-select-user-screening-isi-hanya-login-user-active
title: "Popup Select User: screening, isi hanya Login User Active, pilih baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-102
  - TC-GS-NLU-103
  - TC-GS-NLU-104
coverage:
  web: automated
---

# Popup Select User: screening, isi hanya Login User Active, pilih baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (Active: Ahmad Fauzi, Dewi Anggraini, Dewi Anggreni, Andi Wijaya, dan lainnya; Jane Smith Inactive; Mike Tan Pending Activation) dan Non-Login User Budi Kurniawan (No. 11). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create dibuka tanpa Submit.
- Data uji: kata kunci Search `Jane`, `Mike`, `Budi Kurniawan` (TC-GS-NLU-103); baris Andi Wijaya dan Dewi Anggraini (TC-GS-NLU-104).
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-102: Screening Popup Select User

3. Verifikasi header Popup Select User menampilkan Title `Select User` dan tombol close `✕`
4. Verifikasi toolbar menampilkan Search dengan placeholder `Search...`
5. Verifikasi toolbar menampilkan Filter
6. Verifikasi toolbar tanpa Download dan tanpa Changelog
7. Verifikasi kolom tabel berurutan `Name (sortable) | Email (sortable) | Position (sortable) | Division (sortable) | Status (sortable) | Column Visibility (⋯) (unsortable)`
8. Verifikasi tidak ada kolom Radio atau Checkbox
9. Verifikasi tabel menampilkan sedikitnya satu baris Login User aktif
10. Verifikasi baris terurut Name A-Z
11. Verifikasi pagination default 10 per halaman
12. Verifikasi tombol `[Cancel]` dan `[Select]` tampil
13. Verifikasi tidak ada pesan error saat popup baru dibuka

### TC-GS-NLU-103: Popup Select User hanya memuat Login User berstatus Active

14. Ketik Search `Jane`, tekan Enter
15. Verifikasi tabel menampilkan `No results found` untuk pencarian `Jane`
16. Verifikasi Jane Smith (Inactive) tidak muncul
17. Ganti isi kotak search dengan `Mike`, tekan Enter
18. Verifikasi tabel menampilkan `No results found` untuk pencarian `Mike`
19. Verifikasi Mike Tan (Pending Activation) tidak muncul
20. Ganti isi kotak search dengan `Budi Kurniawan`, tekan Enter
21. Verifikasi tabel menampilkan `No results found` untuk pencarian `Budi Kurniawan`
22. Verifikasi Non-Login User Budi Kurniawan tidak muncul
23. Klik `(←)` pada kotak Search sehingga tabel kembali menampilkan seluruh baris

### TC-GS-NLU-104: Memilih user dengan klik baris menyorot baris dan memindahkan pilihan

24. Klik baris Andi Wijaya
25. Verifikasi baris Andi Wijaya tersorot (terpilih)
26. Klik baris Dewi Anggraini
27. Verifikasi baris Dewi Anggraini tersorot
28. Verifikasi baris Andi Wijaya tidak lagi tersorot
29. Klik lagi baris Dewi Anggraini
30. Verifikasi baris Dewi Anggraini tetap terpilih tanpa deselect dan tidak ada perubahan lain
31. Klik `[Cancel]`
32. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan: screening (TC-GS-NLU-102) di awal, TC-GS-NLU-103 sebelum TC-GS-NLU-104.
- Langkah penghubung tanpa `Verifikasi`: langkah 23 (mereset Search sebelum TC-GS-NLU-104) dan langkah 31 sampai 32 (menutup popup; Popup Create tidak dirty karena Represented By belum dipilih sehingga tidak ada dialog Unsaved Changes).
- Absence pada TC-GS-NLU-103 memakai `No results found` sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA: tidak ada.
