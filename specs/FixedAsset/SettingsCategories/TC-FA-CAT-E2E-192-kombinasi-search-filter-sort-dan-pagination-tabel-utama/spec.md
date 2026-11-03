---
id: TC-FA-CAT-E2E-192-kombinasi-search-filter-sort-dan-pagination-tabel-utama
title: "Kombinasi Search, Filter, Sort, dan Pagination Tabel Utama: Irisan, Urutan Penerapan, dan Pelepasan Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-383
  - TC-FA-CAT-384
  - TC-FA-CAT-385
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Tabel Utama: Irisan, Urutan Penerapan, dan Pelepasan Kontrol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Total Asset 0 sampai 29, Modified By bergantian `Jane Smith`, `Alex Brown`, `John Doe`, `System`). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-383: Kombinasi penuh Search, Filter, Sort, dan Pagination

1. Ketik Search `Seed`, tekan Enter
2. Terapkan Filter Total Asset Min `5` lalu klik `[Apply]`
3. Klik header Total Asset dua kali (Descending)
4. Ubah jumlah baris per halaman menjadi 25
5. Verifikasi hasil adalah irisan Search `Seed` dan Filter Total Asset Min `5`
6. Verifikasi hasil terurut Total Asset menurun
7. Verifikasi halaman menampilkan 25 baris per halaman
8. Verifikasi Search `Seed`, Filter Total Asset Min `5`, dan Sort Total Asset Descending tetap aktif bersamaan (tidak ada kontrol yang menimpa yang lain)
9. Klik `✕` pada Search, tekan Enter
10. Klik `[Clear Field]` pada Filter lalu `[Apply]`
11. Klik header Total Asset ketiga kali (Netral)
12. Ubah jumlah baris per halaman menjadi 10

### TC-FA-CAT-384: Urutan Search lalu Filter dan Filter lalu Search

13. Ketik Search `Seed Cat 2`, tekan Enter
14. Terapkan Filter Modified By `Jane S` lalu klik `[Apply]`
15. Verifikasi keyword Search `Seed Cat 2` tidak tertimpa saat Filter diterapkan
16. Verifikasi tabel menampilkan sedikitnya satu baris hasil
17. Catat dataset baris hasil (baseline)
18. Klik `✕` pada Search, tekan Enter
19. Klik `[Clear Field]` pada Filter lalu `[Apply]`
20. Terapkan Filter Modified By `Jane S` lalu klik `[Apply]`
21. Ketik Search `Seed Cat 2`, tekan Enter
22. Verifikasi dataset baris sama dengan baseline langkah 17

### TC-FA-CAT-385: Melepas Filter atau Search tidak mereset kontrol lain

23. Klik `✕` pada Search, tekan Enter
24. Klik `[Clear Field]` pada Filter lalu `[Apply]`
25. Ketik Search `Seed`, tekan Enter
26. Terapkan Filter Modified By `John D` lalu klik `[Apply]`
27. Klik header Code dua kali (Descending)
28. Klik `[Clear Field]` pada Filter lalu `[Apply]`
29. Verifikasi Search `Seed` dan Sort Code Descending dipertahankan setelah Clear Filter
30. Terapkan Filter Modified By `John D` lalu klik `[Apply]`
31. Klik `✕` pada Search, tekan Enter
32. Verifikasi Filter Modified By `John D` dan Sort Code Descending dipertahankan setelah Clear Search
33. Ketik Search `zzzz`, tekan Enter
34. Verifikasi Title `No results found` tampil
35. Klik `✕` pada Search, tekan Enter
36. Verifikasi tabel menampilkan sedikitnya satu baris (hasil nol pulih otomatis saat Search dilepas)

## Notes

- Langkah penghubung (S-03): langkah 9 sampai 12 (melepas Search, Filter, Sort, dan mengembalikan ukuran halaman, S-09); langkah 18 sampai 19 dan 23 sampai 24 (mengosongkan kontrol sebelum TC berikutnya); langkah 30 (menerapkan ulang Filter agar asersi "Clear Search mempertahankan Filter" bermakna).
- Ambang sekitar 35 langkah terlampaui tipis (36 langkah). Alasan: seluruh TC satu halaman, satu dataset CatMany, dan satu kelas harness; tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-385 menulis "Clear Filter" sebelum "Kosongkan Search" lalu mengharapkan "Clear Search mempertahankan Filter"; Filter sudah dilepas pada langkah 2 TC sehingga asersi itu tidak dapat diamati. Spec menerapkan ulang Filter pada langkah 30.
  - TC-383 menyebut "25 baris per halaman"; hasil irisan Total Asset Min `5` pada seed #24 tepat 25 baris, sehingga halaman kedua tidak teramati.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
