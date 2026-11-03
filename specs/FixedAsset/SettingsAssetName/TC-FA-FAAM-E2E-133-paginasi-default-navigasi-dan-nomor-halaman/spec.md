---
id: TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman
title: "Paginasi: Default 10, Page Size, Next-Prev, Nomor Halaman, dan Reset oleh Search-Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-432
  - TC-FA-FAAM-433
  - TC-FA-FAAM-434
  - TC-FA-FAAM-435
  - TC-FA-FAAM-436
coverage:
  web: automated
---

# Paginasi: Default 10, Page Size, Next-Prev, Nomor Halaman, dan Reset oleh Search-Filter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Total baris katalog (36) diturunkan dari seeding (6 Asset Name contoh + 30 `Seed Item`), sehingga halaman 3 ada pada page size 10.
- Nomor halaman tidak valid untuk TC-FA-FAAM-435 (diulang pada langkah 19 sampai 20):

  | Input |
  |---|
  | 0 |
  | -1 |
  | 999 |
  | abc |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-432: Paginasi default 10 data dan pilihan page size
1. Perhatikan footer Asset Name List
2. Verifikasi default 10 baris per halaman
3. Pindah ke halaman 2
4. Buka page size menu
5. Verifikasi pilihan page size 10, 25, 50, dan 100 tanpa opsi All
6. Pilih page size 25
7. Verifikasi tabel kembali ke halaman 1
8. Pilih page size 50
9. Pilih page size 100
10. Pilih page size 10
### TC-FA-FAAM-433: Navigasi halaman Next dan Prev
11. Klik Next
12. Verifikasi halaman berpindah ke halaman 2
13. Verifikasi tabel menampilkan baris halaman 2 (baris `Dell Latitude` halaman 1 tidak tampil)
14. Klik Prev
15. Verifikasi halaman kembali ke halaman 1
16. Verifikasi tabel menampilkan baris halaman 1 (baris `Dell Latitude` tampil)
### TC-FA-FAAM-434: Input nomor halaman langsung dengan Enter
17. Ketik `3` di input halaman, lalu tekan Enter
18. Verifikasi tabel berpindah ke halaman 3
### TC-FA-FAAM-435: Nomor halaman tidak valid diabaikan
19. Untuk setiap baris tabel "Input", ketik nilai tersebut di input halaman, lalu tekan Enter
20. Verifikasi input diabaikan dan tabel tetap di halaman 3
### TC-FA-FAAM-436: Search dan Filter mengembalikan ke halaman 1
21. Ketik Search `Seed`, tekan Enter
22. Verifikasi tabel kembali ke halaman 1
23. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan konfigurasi kolom dan pembersihan Search, Filter, dan seleksi di antara blok (S-09).
- Langkah yang diulang per input pada TC-FA-FAAM-435: langkah 19 sampai 20; parameter tiap iterasi ada di tabel "Input" pada Prerequisites. Ekspansi: 4 input x 2 langkah = 8 langkah.
- Pindah ke halaman 2 sebelum membuka page size menu pada TC-FA-FAAM-432 adalah langkah penghubung supaya "kembali ke halaman 1" teramati (S-14). Halaman 3 pada TC-FA-FAAM-434 dipertahankan untuk TC-FA-FAAM-435 dan TC-FA-FAAM-436 (S-14).
- Expected b TC-FA-FAAM-436 ("Search dan Filter mengembalikan ke halaman 1") hanya menyebut langkah Search; Filter diuji pada TC-FA-FAAM-379.
