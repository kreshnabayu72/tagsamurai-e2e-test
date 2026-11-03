---
id: TC-AC-LA-E2E-097-search-list-teks-dan-kolom-status-quantity
title: "Search List: Siklus Interaksi, Allocated By, dan Status"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-280
  - TC-AC-LA-282
  - TC-AC-LA-283
coverage:
  web: automated
---

# Search List: Siklus Interaksi, Allocated By, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; Client `PT Sejahtera` dan `Klinik Medika Jaya`; Allocated By `Dewi A` untuk dua pengguna `Dewi Anggraini` dan `Dewi Angkasa`; status `Pending` dan `Active`) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-280: Siklus interaksi Search toolbar

1. Hover ikon Search
2. Verifikasi tooltip `Search` tampil
3. Klik ikon Search
4. Verifikasi search bar melebar
5. Verifikasi kursor otomatis fokus di input
6. Catat isi halaman pertama tabel sebagai baseline
7. Ketik `Sejahtera` di input Search tanpa menekan Enter
8. Verifikasi ikon `(✕)` muncul di input
9. Verifikasi tabel belum tersaring (isi halaman pertama sama dengan baseline langkah 6)
10. Tekan Enter
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi tabel hanya memuat baris yang cocok `Sejahtera`
13. Klik ikon `(✕)` di dalam input
14. Verifikasi input Search kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi tabel tetap menampilkan hasil `Sejahtera`
17. Tekan Enter pada input kosong
18. Verifikasi tabel mereset ke semua data (isi halaman pertama sama dengan baseline langkah 6)
19. Ketik `Medika` di input Search, tekan Enter
20. Klik ikon panah `(←)`
21. Verifikasi search bar tertutup
22. Verifikasi kata kunci dikosongkan
23. Verifikasi tabel langsung reset ke semua data (isi halaman pertama sama dengan baseline langkah 6)

### TC-AC-LA-282: Search kolom Allocated By

24. Ketik Search `dewi`, tekan Enter
25. Verifikasi baris dengan Allocated By `Dewi A` (Dewi Anggraini dan Dewi Angkasa) tampil
26. Verifikasi baris dengan Allocated By lain tidak tampil

### TC-AC-LA-283: Search kolom Status

27. Ganti isi kotak search dengan `pending`, tekan Enter
28. Verifikasi baris berbadge `Pending` tampil
29. Ganti isi kotak search dengan `active`, tekan Enter
30. Verifikasi baris berbadge `Active` tampil
31. Verifikasi seluruh baris hasil berbadge `Active` saja
32. Klik ikon panah `(←)`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-281 dan TC-AC-LA-284 ada di spec 119.
- Langkah penghubung (S-03): langkah 6 (baseline), langkah 20 dan 32 (menutup search bar). Urutan TC dalam spec: TC-AC-LA-280, TC-AC-LA-282, TC-AC-LA-283; Search terakhir ditutup sebelum spec selesai (S-09).
- Spec ini sekitar 32 langkah.
- Temuan untuk QA:
  - TC-AC-LA-280 butir b ("tabel belum tersaring") tidak menyebut cara mengamatinya; spec membandingkan isi halaman pertama dengan baseline yang dicatat sebelum mengetik.
  - TC-AC-LA-283 butir b menyebut "tidak ada status `Inactive` pada modul ini" sebagai penjelasan; spec mengasersi seluruh baris hasil berbadge `Active`.
