---
id: TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi
title: "List Filter: Chip Lanjutan dan Pemulihan Opsi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-344
  - TC-AC-CS-345
  - TC-AC-CS-346
  - TC-AC-CS-575
  - TC-AC-CS-576
  - TC-AC-CS-348
coverage:
  web: automated
---

# List Filter: Chip Lanjutan dan Pemulihan Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Data seed milik spec (bersuffix `{runId}-091`; dibuat lewat API seeding di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription+{runId}-091` (binaan langsung PT Maju Bersama, belum punya term; padanan #48) dan Client `Toko Serba Ada+{runId}-091` (punya satu term Active sehingga tampil di dropdown Client; padanan Client Pre-setup #67). Dataset #82 hanya dibaca.
- Jam: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API Group Manager Distributor Dewi Anggraini (Pre-setup #5, `Spectra.env.AC_SUB_GM_PASSWORD`) menambah term SAMS Growth Start Date `19/08/26` untuk Client `Client Tanpa Subscription+{runId}-091` hingga term tersimpan (TC-AC-CS-575, pemicu state); penahanan respons endpoint opsi filter lewat `Spectra.intercept()` parsial di atas backend nyata (TC-AC-CS-576; alamat endpoint disediakan tim FE/BE), dilepas segera setelah pengamatan (S-09); penghapusan Client `Toko Serba Ada+{runId}-091` dari sesi lain lewat fixture backend (TC-AC-CS-348). Term baru dan Client seed dibersihkan fixture backend di hook `after` dan sebagai langkah penghubung; intercept dilepas oleh fixture.
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after`); intercept dilepas setelah blok TC-AC-CS-576.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-344: Uncheck di dalam dropdown menghapus chip yang bersangkutan

1. Klik ikon Filter, pilih Status `Active` dan `Expired`, buka dropdown Status, lalu uncheck `Active` dari dalam dropdown
2. Verifikasi chip `Active` hilang dari field
3. Verifikasi chip `Expired` tetap ada

### TC-AC-CS-345: Menghapus chip lalu Apply memfilter ulang dengan opsi tersisa

4. Tutup dropdown Status, centang `Active` kembali lalu klik `[Apply]`
5. Hapus chip `Active` lewat icon `(✕)`, lalu klik `[Apply]`
6. Verifikasi tabel menampilkan sedikitnya satu baris
7. Verifikasi tabel hanya menampilkan baris Expired

### TC-AC-CS-346: Banyak chip diringkas menjadi chip `+N more`

8. Klik `[Clear Field]`, buka dropdown Client, lalu pilih seluruh opsi Client yang jumlahnya melebihi lebar field
9. Verifikasi chip ditampilkan sebanyak yang muat dan sisanya diringkas satu chip `+N more` dengan N sama dengan jumlah chip tersembunyi
10. Verifikasi field tidak melebar keluar panel dan tidak digulir horizontal

### TC-AC-CS-575: Opsi baru muncul di dropdown filter tanpa muat ulang halaman

11. Klik `[Clear Field]`, buka dropdown Client, lalu catat opsi
12. Verifikasi sedikitnya satu opsi Client lain tampil di dropdown Client
13. Verifikasi `Client Tanpa Subscription+{runId}-091` tidak ada di opsi Client
14. Tambah term SAMS Growth Start Date `19/08/26` untuk Client `Client Tanpa Subscription+{runId}-091` lewat sesi API Group Manager Dewi Anggraini hingga term tersimpan
15. Tutup dan buka kembali dropdown Client tanpa memuat ulang halaman
16. Verifikasi opsi `Client Tanpa Subscription+{runId}-091` muncul di dropdown Client tanpa muat ulang halaman

### TC-AC-CS-576: Dropdown filter menampilkan state loading saat opsi diambil

17. Tutup dropdown Client, tahan respons endpoint opsi filter lewat intercept, lalu buka dropdown Client
18. Verifikasi dropdown menampilkan indikator loading (skeleton atau spinner mini), bukan dropdown kosong
19. Lepas penahanan respons
20. Verifikasi opsi Client menggantikan indikator loading

### TC-AC-CS-348: Kriteria filter yang record sumbernya hilang dibersihkan saat filter diterapkan ulang

21. Pulihkan term baru dan intercept lewat fixture backend, lalu klik `[Clear Field]`, pilih Client `Toko Serba Ada+{runId}-091`, klik `[Apply]`
22. Hapus Client `Toko Serba Ada+{runId}-091` lewat fixture backend (sesi lain), lalu klik `[Apply]` ulang
23. Verifikasi nilai stale dibersihkan dari kriteria tanpa pesan error
24. Verifikasi hasil tabel mengikuti kriteria yang tersisa
25. Bersihkan sisa seed Client `Toko Serba Ada+{runId}-091` lewat fixture backend

## Notes

- Langkah penghubung: penutupan dropdown, `[Clear Field]`, dan pemulihan fixture antar blok.
- Urutan TC: TC-AC-CS-344 sebelum TC-AC-CS-345 karena TC-AC-CS-345 melanjutkan keadaan dua opsi terpilih; TC-AC-CS-348 terakhir karena menghapus Client seed milik spec.
- Intercept pada TC-AC-CS-576 adalah intercept parsial atas backend nyata (kelas b ringan, penahanan respons hanya untuk mengamati state loading); karena itu Mode FE+BE.
- Temuan untuk QA: (1) TC-AC-CS-345 langkah 2 mengulang pemilihan `Active` dan `Expired` yang sama dengan TC-AC-CS-344; spec memulihkan chip lewat centang kembali. (2) TC-AC-CS-346 butir a menyebut N "sama dengan jumlah chip tersembunyi" tanpa angka; spec mengasersi relasi tanpa nilai absolut. (3) TC-AC-CS-575 langkah 2 menyebut sesi kedua dengan login Group Manager; spec memakai sesi API karena sesi itu hanya memicu perubahan state (R-20). (4) TC-AC-CS-348 menyebut "Hapus seluruh baris Client itu dari sesi lain (Client dihapus)" tanpa mekanisme; dilakukan fixture backend yang disediakan tim FE/BE. (5) TC-AC-CS-345 butir "logika OR dalam field berlaku dengan opsi tersisa" dengan satu opsi tersisa tidak punya pengamatan di luar hasil tabel hanya Expired, sehingga tidak diasersi sebagai langkah sendiri.
