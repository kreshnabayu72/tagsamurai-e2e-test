---
id: TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar
title: "List State Preservation: Detail, F5, dan Sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-394
  - TC-AC-CS-395
  - TC-AC-CS-396
  - TC-AC-CS-397
coverage:
  web: automated
---

# List State Preservation: Detail, F5, dan Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History; Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kelas volume data (e): dataset Pre-setup #82 dipakai agar halaman 2 pada Search `a` tersedia. Kemampuan membaca penyimpanan sesi browser (`sessionStorage`) untuk TC-AC-CS-396 disediakan tim FE (disebut di Expected TC).

## Test Steps

### TC-AC-CS-394: Kembali dari Detail lewat crumb mempertahankan Search, Filter, Sort, dan halaman

1. Ketik Search `a`, tekan Enter
2. Klik header `Client` sekali dan pindah ke halaman 2
3. Catat isi baris tabel halaman 2
4. Klik satu baris untuk membuka Detail lalu klik crumb `Client Subscription`
5. Verifikasi List kembali dengan keyword `a`
6. Verifikasi sort Client ascending dipertahankan
7. Verifikasi tabel berada di halaman 2
8. Verifikasi isi tabel identik dengan isi yang dicatat sebelum meninggalkan halaman

### TC-AC-CS-395: Refresh F5 mempertahankan Search, Filter, Sort, dan halaman pada tab yang sama

9. Klik menu `Client Subscription` di sidebar untuk mereset List
10. Ketik Search `a`, tekan Enter
11. Klik ikon Filter di toolbar, pilih Product `FAMS`, lalu klik `[Apply]`
12. Klik header `Client` sekali, pindah ke halaman 2, catat jumlah baris per halaman, lalu tekan F5
13. Verifikasi keyword `a` dipertahankan setelah F5
14. Verifikasi filter Product `FAMS` dipertahankan setelah F5
15. Verifikasi sort Client ascending dipertahankan setelah F5
16. Verifikasi tabel berada di halaman 2 setelah F5
17. Verifikasi jumlah baris per halaman sama dengan yang dicatat sebelum F5

### TC-AC-CS-396: Klik ulang menu sidebar mereset List ke default

18. Ganti isi kotak search dengan `a`, tekan Enter
19. Klik tab `History` lalu klik menu `Client Subscription` di sidebar
20. Verifikasi List terbuka di tab `Current`
21. Verifikasi keyword Search kosong
22. Verifikasi filter kosong
23. Verifikasi sort default
24. Verifikasi tabel berada di halaman 1
25. Verifikasi state `sessionStorage` sebelumnya dibersihkan

### TC-AC-CS-397: Tab aktif dipertahankan setelah F5 dan setelah kembali dari Detail

26. Klik tab `History`
27. Buka satu Detail dengan mengklik satu baris lalu klik crumb `Client Subscription`
28. Verifikasi List kembali terbuka di tab `History` beserta state tab itu
29. Tekan F5
30. Verifikasi tab `History` tetap aktif setelah F5

## Notes

- Langkah penghubung (S-03): langkah mencatat isi baris tabel halaman 2 dan jumlah baris per halaman sebelum aksi (baseline untuk asersi "identik" dan "tetap"), serta klik menu `Client Subscription` di sidebar di awal blok TC-AC-CS-395 yang mereset Search, Filter, Sort, dan halaman dari blok sebelumnya (bagian 4).
- Temuan untuk QA:
  - TC-AC-CS-394 butir Langkah Uji ke-1 sampai 4 tidak menyebut baris yang diklik untuk membuka Detail; spec mengklik baris pertama di halaman 2.
  - TC-AC-CS-395 Expected b ("Jumlah baris per halaman tetap") tidak menyebut nilai awal; spec mencatat nilai bawaan sebelum F5.
  - TC-AC-CS-396 Expected b (state `sessionStorage` dibersihkan) tidak menyebut cara membacanya; spec memakai kemampuan baca penyimpanan sesi yang disediakan tim FE.
  - TC-AC-CS-397 Expected a ("beserta state tab itu") tidak menyebut state tab `History` yang diharapkan; spec mengasersinya sebagai keadaan bawaan tab `History`.
