---
id: TC-FA-CAT-E2E-100-sort-3-state-tabel-utama
title: "Sort 3-State Tabel Utama: Kolom Category, Code, Modified By, Total Asset, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-346
  - TC-FA-CAT-347
  - TC-FA-CAT-348
  - TC-FA-CAT-349
coverage:
  web: automated
---

# Sort 3-State Tabel Utama: Kolom Category, Code, Modified By, Total Asset, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (Code `SC01` sampai `SC30`, Total Asset 0 sampai 29, Modified By bergantian `Jane Smith`, `Alex Brown`, `John Doe`, `System`, Last Updated berbeda-beda). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Tampilan Modified By di tabel berformat singkat (`Alex B`, `Jane S`, `John D`, `System`); urutan sort mengikuti nama lengkap underlying (`Alex Brown`, `Jane Smith`, `John Doe`, `System`).
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-346: Sort 3-state kolom Category dan Code

1. Ubah jumlah baris per halaman menjadi 50 supaya ke-30 baris tampil pada satu halaman
2. Klik header Category satu kali
3. Verifikasi Category berstatus Ascending (↑) dengan urutan `Seed Cat 01` sampai `Seed Cat 30`
4. Klik header Category kedua kali
5. Verifikasi Category berstatus Descending (↓) dengan urutan kebalikan penuh (`Seed Cat 30` sampai `Seed Cat 01`)
6. Klik header Category ketiga kali
7. Verifikasi Category berstatus Netral dan urutan kembali ke default Category A-Z
8. Klik header Code satu kali
9. Verifikasi Code berstatus Ascending (↑) dengan urutan `SC01` sampai `SC30`
10. Klik header Code kedua kali
11. Verifikasi Code berstatus Descending (↓) dengan urutan kebalikan penuh (`SC30` sampai `SC01`)
12. Klik header Code ketiga kali
13. Verifikasi Code berstatus Netral dan urutan kembali ke default Category A-Z

### TC-FA-CAT-347: Sort 3-state kolom Modified By

14. Klik header Modified By satu kali
15. Verifikasi Modified By berstatus Ascending (↑) dengan urutan nama lengkap underlying `Alex Brown`, `Jane Smith`, `John Doe`, `System` (tampil `Alex B`, `Jane S`, `John D`, `System`), bukan urutan format singkatnya
16. Klik header Modified By kedua kali
17. Verifikasi Modified By berstatus Descending (↓) dengan urutan kebalikan penuh
18. Klik header Modified By ketiga kali
19. Verifikasi indikator sort pada header Modified By hilang dan urutan kembali ke default Category A-Z

### TC-FA-CAT-348: Sort 3-state kolom Total Asset

20. Klik header Total Asset satu kali
21. Verifikasi Total Asset berstatus Ascending (↑) dengan urutan numerik natural (`0, 1, 2, 3, 10, 11` dan seterusnya, bukan `0, 1, 10, 11, 2, 3`)
22. Klik header Total Asset kedua kali
23. Verifikasi Total Asset berstatus Descending (↓) dengan urutan kebalikan penuh
24. Klik header Total Asset ketiga kali
25. Verifikasi indikator sort pada header Total Asset hilang dan urutan kembali ke default Category A-Z

### TC-FA-CAT-349: Sort 3-state kolom Last Updated

26. Klik header Last Updated satu kali
27. Verifikasi Last Updated berstatus Ascending (↑) dengan Oldest First (tanggal terlama di atas)
28. Klik header Last Updated kedua kali
29. Verifikasi Last Updated berstatus Descending (↓) dengan Newest First (kebalikan penuh)
30. Klik header Last Updated ketiga kali
31. Verifikasi indikator sort pada header Last Updated hilang dan urutan kembali ke default Category A-Z

## Notes

- Langkah penghubung (S-03): langkah 1 (ukuran halaman 50 agar urutan `Seed Cat 01` sampai `Seed Cat 30` dapat diasersi pada satu halaman). Tiap TC berakhir pada keadaan Netral sehingga TC berikutnya tidak membutuhkan langkah pembersih (S-09).
- Temuan untuk QA:
  - TC-346 menyebut urutan `Seed Cat 01` sampai `Seed Cat 30` tetapi pagination default 10 baris; TC tidak menyebut ukuran halaman yang dipakai (langkah 1 adalah usulan).
  - TC-349 tidak menyebut nilai Last Updated yang dipakai untuk memeriksa urutan; spec membandingkan urutan tanggal antarbaris yang tampil.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
