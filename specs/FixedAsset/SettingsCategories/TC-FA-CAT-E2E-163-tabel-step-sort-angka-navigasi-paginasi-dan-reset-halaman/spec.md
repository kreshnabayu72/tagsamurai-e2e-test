---
id: TC-FA-CAT-E2E-163-tabel-step-sort-angka-navigasi-paginasi-dan-reset-halaman
title: "Tabel Step Category Consolidation: Sort Tiga State Kolom Angka (Depth, Total Asset) serta Navigasi Paginasi, Input Nomor Halaman, Page Size, dan Reset ke Halaman 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-447
  - TC-FA-CAT-599
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Sort Tiga State Kolom Angka (Depth, Total Asset) serta Navigasi Paginasi, Input Nomor Halaman, Page Size, dan Reset ke Halaman 1

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy` untuk langkah 1 sampai 7; varian 12 kategori dengan tambahan `Extra 01` sampai `Extra 04` untuk langkah 8 sampai 27 (TC-FA-CAT-599). Pergantian varian dan pemulihan ke 8 kategori lewat fixture backend yang disediakan tim FE/BE, dijalankan di langkah 8 dan hook `after`. Kebutuhan data uji sort: sedikitnya dua nilai distinct pada kolom Depth dan Total Asset; Pre-setup #33 hanya berisi kategori root (lihat Temuan untuk QA).
- Kolom yang diuji pada langkah 2 sampai 7 (langkah diulang untuk setiap baris tabel): `Depth`, `Total Asset`; urutan Ascending (↑) numerik natural.
- Nomor halaman yang diketik pada langkah 15 dan 16 (langkah diulang untuk setiap baris tabel): `0`, `99`, `abc`.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-447: Sort 3-state tabel Step kolom Depth dan Total Asset (untuk setiap kolom pada tabel Kolom yang diuji, langkah 2 sampai 7)

2. Klik header kolom satu kali
3. Verifikasi Ascending (↑) numerik natural
4. Klik header kolom kedua kali
5. Verifikasi Descending (↓) kebalikan penuh dari Ascending
6. Klik header kolom ketiga kali
7. Verifikasi Netral kembali ke default Category Name A-Z

### TC-FA-CAT-599: Navigasi paginasi tabel Step, halaman berikutnya dan sebelumnya, input nomor halaman, page size, sort, dan reset ke halaman 1 (nomor halaman pada langkah 15 dan 16 diulang untuk setiap baris butir Nomor halaman)

8. Klik `[Cancel]` pada wizard, alihkan Pre-setup #33 ke varian 12 kategori lewat fixture backend, lalu klik `[Choose Categories]` pada Alert Category Consolidation
9. Klik kontrol halaman berikutnya
10. Verifikasi halaman 2 memuat 2 kategori sisa, `Theta Heavy` dan `Zeta Vehicle` (default sort Category Name A-Z)
11. Klik kontrol halaman sebelumnya
12. Verifikasi halaman 1 tampil dengan 10 kategori
13. Ketik halaman `2` pada input nomor halaman, tekan `Enter`
14. Verifikasi halaman 2 terbuka
15. Ketik nomor pada input nomor halaman, tekan `Enter`
16. Verifikasi nomor itu diabaikan dan tabel tetap di halaman 2
17. Pada halaman 2, klik header kolom Code untuk mengganti sort
18. Verifikasi tabel tetap di halaman 2
19. Ganti jumlah baris per halaman menjadi 25
20. Verifikasi tabel kembali ke halaman 1 dan menampilkan 12 kategori pada satu halaman
21. Kembalikan jumlah baris per halaman ke 10
22. Pindah ke halaman 2, lalu ketik Search `a`, tekan `Enter`
23. Verifikasi tabel direset ke halaman 1
24. Klik icon panah (←) di kiri toolbar untuk mengosongkan Search
25. Pindah ke halaman 2
26. Klik icon Filter, pilih Depth `L1`, lalu klik `[Apply]`
27. Verifikasi tabel direset ke halaman 1

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (27 langkah nominal, langkah 2 sampai 7 diulang dua kali dan langkah 15 sampai 16 tiga kali: sekitar 37). Alasan: seluruh blok satu kelas fungsional pada tabel Step yang sama, berdiri sendiri, dan pengulangan per kolom atau per nomor identik dengan parameter di butir Prerequisites (bagian 8b butir 7).
- Langkah penghubung (S-03, S-09): langkah 1 (membuka wizard), langkah 8 (menutup wizard, mengalihkan varian, membuka wizard lagi), langkah 21 (mengembalikan page size), langkah 24 (mengosongkan Search sebelum Filter).
- Urutan: TC-FA-CAT-447 pada varian 8 kategori mendahului TC-FA-CAT-599 yang memerlukan varian 12 kategori (S-10).
- Langkah 14 menjadi anchor posisi untuk langkah 15 sampai 16 (halaman 2 terbuka sebelum nomor diabaikan; S-14).
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-447 Expected a menyebut sort Depth numerik natural, tetapi Pre-setup #33 hanya berisi kategori root (Depth `L1`), sehingga hasil sort Depth tidak memiliki dua nilai distinct dan urutannya tidak dapat dibedakan; spec tetap memverifikasi sesuai Expected.
  - TC-FA-CAT-599 Precondition menyebut "varian 12 kategori" tanpa langkah pergantian varian; spec memakai fixture backend (disediakan tim FE/BE).
  - TC-FA-CAT-599 Expected e mengasumsikan Search `a` dan Filter Depth `L1` menyisakan lebih dari satu halaman setelah dipindah ke halaman 2; spec mengikuti urutan langkah TC tanpa asersi jumlah hasil.
