---
id: TC-GS-NLU-E2E-038-popup-select-user-search-tanggal-filter-temporary-pagination-dan-tanpa-download-changelog
title: "Popup Select User: Search tanggal, Filter Temporary, Pagination, dan tanpa Download Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-114
  - TC-GS-NLU-117
  - TC-GS-NLU-119
  - TC-GS-NLU-120
coverage:
  web: automated
---

# Popup Select User: Search tanggal, Filter Temporary, Pagination, dan tanpa Download Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 yang berisi lebih dari 10 baris Active (precondition TC-GS-NLU-119), termasuk Rudi Setiawan (Temporary aktif) dan Rina Putri (Activated, email pending `rinaputri.baru@qwertysystem.net`, tampil Pending Email Confirmation). Tanggal Temporary Until Rudi Setiawan tidak tertulis di Pre-setup; dibaca dari sel kolom Temporary Until sesudah kolom diaktifkan. Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Visibilitas kolom Temporary Until diatur lewat overlay Column Visibility pada sesi popup tanpa menyimpan lewat Setup Column; spec memulihkannya dengan langkah eksplisit.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-120: Popup Select User tidak memiliki tombol Download dan Changelog

3. Verifikasi toolbar hanya memuat Search dan Filter

### TC-GS-NLU-114: Kolom tanggal Temporary Until tidak dapat dicari lewat Search Popup Select User

4. Ketik Search `Rudi Setiawan`, tekan Enter
5. Klik ikon `⋯` pada header kolom tabel
6. Centang kolom Temporary Until pada overlay Column Visibility
7. Baca nilai sel Temporary Until baris Rudi Setiawan
8. Ganti isi kotak search dengan nilai tanggal Temporary Until Rudi Setiawan yang dibaca, tekan Enter
9. Verifikasi tabel menampilkan `No results found`
10. Klik `(←)` pada kotak Search sehingga tabel kembali menampilkan seluruh baris
11. Klik ikon `⋯` pada header kolom tabel dan hapus centang kolom Temporary Until

### TC-GS-NLU-119: Pagination Popup Select User

12. Verifikasi pagination default 10 per halaman
13. Verifikasi opsi page size 10, 25, 50, dan 100
14. Klik halaman berikutnya
15. Verifikasi tabel berpindah ke halaman 2
16. Ganti page size ke 25
17. Verifikasi tabel kembali ke halaman 1

### TC-GS-NLU-117: Filter Temporary User, Activation Status, dan Temporary Until pada Popup Select User

18. Klik icon Filter
19. Verifikasi tabel menampilkan sedikitnya satu baris sebelum Filter diterapkan
20. Pilih Temporary User `Yes`, klik `[Apply]`
21. Verifikasi hanya Rudi Setiawan yang tampil
22. Klik `[Clear Field]`
23. Pilih Activation Status `Activated`, klik `[Apply]`
24. Verifikasi seluruh baris pool tampil kecuali Rina Putri
25. Ganti Activation Status menjadi `Pending Email Confirmation`, klik `[Apply]`
26. Verifikasi hanya Rina Putri yang tampil
27. Klik `[Clear Field]`
28. Pilih rentang Temporary Until yang memuat tanggal Rudi Setiawan, klik `[Apply]`
29. Verifikasi Rudi Setiawan ditemukan
30. Verifikasi kolom Temporary Until tidak ditampilkan di tabel sementara filter Temporary Until tetap tersedia
31. Klik `[Cancel]`
32. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-GS-NLU-120 (screening toolbar) lebih dulu, lalu TC-GS-NLU-114, TC-GS-NLU-119, dan TC-GS-NLU-117 terakhir karena filter Temporary yang tersisa membuat tabel tidak lagi cukup panjang untuk Pagination. TC-GS-NLU-118 (Sort) ada di spec 130.
- Langkah penghubung tanpa `Verifikasi`: langkah 4 (mencari baris Rudi Setiawan untuk membaca tanggalnya, R-16), langkah 10 dan 11 (mereset Search dan memulihkan visibilitas kolom, S-09), langkah 22 dan 27 (mengosongkan filter sebelumnya supaya tiap filter diuji sendiri), serta langkah 31 sampai 32 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- Absence pada TC-GS-NLU-114 memakai empty state `No results found` sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-NLU-114 langkah 3 ("Aktifkan kolom Temporary Until lewat Setup Column") tidak menyebut `[Save]`. Spec memakai centang di overlay Column Visibility tanpa Save; bila yang dimaksud Setup Column dengan `[Save]`, spec ini perlu didaftarkan pada daftar pemulihan Setup Column di `suite.md`.
  - TC-GS-NLU-114 Expected butir a memuat klausa "penyaringan tanggal hanya lewat Filter Panel" yang bukan keadaan teramati pada langkah ini sehingga tidak diasersi. TC tidak menyebut nilai tanggal Rudi Setiawan; spec membaca nilainya dari sel kolom Temporary Until.
  - TC-GS-NLU-117 langkah 4 sampai 7 tidak menyebut pengosongan filter di antara langkah, padahal Expected butir b (seluruh baris pool kecuali Rina Putri) dan butir d (Rudi Setiawan ditemukan) hanya benar bila filter sebelumnya tidak ikut berlaku. Spec menambah `[Clear Field]` sebagai langkah penghubung.
  - TC-GS-NLU-117 tidak menyebut tanggal Temporary Until Rudi Setiawan ("rentang yang memuat tanggal Rudi Setiawan"); tanggal itu tidak ada di Tabel Data Uji Pre-setup.
