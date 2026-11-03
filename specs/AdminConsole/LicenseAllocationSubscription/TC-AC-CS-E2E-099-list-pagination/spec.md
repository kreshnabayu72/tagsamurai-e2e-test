---
id: TC-AC-CS-E2E-099-list-pagination
title: "List Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-377
  - TC-AC-CS-378
  - TC-AC-CS-379
  - TC-AC-CS-380
  - TC-AC-CS-381
  - TC-AC-CS-382
coverage:
  web: automated
---

# List Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History; Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kelas volume data (e): 120 baris Current dan 60 baris History dari Pre-setup #82 dipakai baca-saja. Jumlah halaman yang diasersi diturunkan dari seeding: 120 baris pada 10 per halaman menghasilkan 12 halaman, 25 per halaman 5 halaman, 50 per halaman 3 halaman, 100 per halaman 2 halaman; 60 baris History menghasilkan 6 halaman.
- Nilai input nomor halaman tidak valid: `0`, `999`, `abc` (input uji yang tidak mengubah state).

## Test Steps

### TC-AC-CS-377: Pagination default 10 baris dan pilihan 10, 25, 50, 100

1. Verifikasi tab `Current` menampilkan 10 baris per halaman dan 12 halaman
2. Buka Overlay page size dan pilih `25`
3. Verifikasi tabel menghasilkan 5 halaman dan halaman terakhir berisi 20 baris
4. Pilih `50` pada Overlay page size
5. Verifikasi tabel menghasilkan 3 halaman
6. Pilih `100` pada Overlay page size
7. Verifikasi tabel menghasilkan 2 halaman dan halaman terakhir berisi 20 baris
8. Pilih `10` pada Overlay page size

### TC-AC-CS-378: Navigasi pagination: berikutnya, sebelumnya, nomor halaman

9. Klik tombol berikutnya
10. Verifikasi halaman 2 tampil dengan baris yang sesuai
11. Klik nomor halaman `5`
12. Verifikasi halaman 5 tampil dengan baris yang sesuai
13. Klik tombol sebelumnya
14. Verifikasi halaman 4 tampil dengan baris yang sesuai
15. Klik nomor halaman `1`
16. Verifikasi tombol sebelumnya Disabled di halaman 1
17. Klik nomor halaman terakhir (`12`)
18. Verifikasi tombol berikutnya Disabled di halaman terakhir

### TC-AC-CS-379: Mengganti page size kembali ke halaman 1

19. Buka halaman `3` lalu ganti page size menjadi `25`
20. Verifikasi tabel kembali ke halaman 1
21. Verifikasi Search, filter, dan sort tidak direset

### TC-AC-CS-380: Mengganti sort mempertahankan nomor halaman

22. Pilih page size `10`, buka halaman `3`, lalu klik header `Product` sekali
23. Verifikasi tabel tetap di halaman 3 dengan urutan dataset yang berubah
24. Verifikasi nomor halaman tidak berubah
25. Klik header `Product` dua kali lagi untuk mengembalikan sort ke bawaan

### TC-AC-CS-381: Nomor halaman tidak valid diabaikan

26. Ketik `0` pada input nomor halaman lalu tekan Enter
27. Verifikasi input diabaikan dan tabel tetap di halaman sekarang
28. Ketik `999` pada input nomor halaman lalu tekan Enter
29. Verifikasi input diabaikan dan tabel tetap di halaman sekarang
30. Ketik `abc` pada input nomor halaman lalu tekan Enter
31. Verifikasi input diabaikan dan tabel tetap di halaman sekarang

### TC-AC-CS-382: Paginasi tab History terpisah dari tab Current

32. Pindah ke halaman `4` di tab `Current` lalu klik tab `History`
33. Verifikasi tab `History` mulai dari halaman 1 dengan 6 halaman pada 10 baris per halaman
34. Pindah ke halaman `2` di tab `History`
35. Klik tab `Current`
36. Verifikasi paginasi tab `Current` tetap di halaman 4

## Notes

- Spec ini melewati sekitar 35 langkah. Alasannya: seluruh blok satu topik (Pagination List) pada dataset Pre-setup #82 yang sama (kelas volume data, harness yang sama), baca-saja, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah `Pilih 10` pada Overlay page size, langkah mengembalikan sort ke bawaan (klik header `Product` dua kali lagi), langkah klik nomor halaman `1` dan halaman terakhir, serta klik tab `Current` di akhir blok TC-AC-CS-382.
- Urutan blok mengikuti bagian 3: blok TC-AC-CS-382 (pindah tab) di akhir.
- Temuan untuk QA:
  - TC-AC-CS-379 Expected b (Search, filter, dan sort tidak direset) tidak punya Search, filter, atau sort aktif pada Langkah Uji; keadaan awalnya bawaan sehingga asersi hanya meneguhkan keadaan bawaan.
  - TC-AC-CS-382 Expected b (paginasi tab `Current` tidak berubah) tidak punya langkah kembali ke tab `Current`; spec menambah langkah klik tab `Current` (S-03).
  - TC-AC-CS-380 Expected a ("urutan dataset yang berubah") tidak menyebut nilai baris yang diharapkan.
