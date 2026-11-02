---
id: TC-FA-CAT-E2E-105-pagination-ukuran-halaman-nomor-halaman-dan-perpindahan-halaman
title: "Pagination Tabel Utama: Ukuran Halaman Default, Input Nomor Halaman, dan Perpindahan Halaman saat Ganti Sort atau Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-363
  - TC-FA-CAT-364
  - TC-FA-CAT-365
coverage:
  web: automated
---

# Pagination Tabel Utama: Ukuran Halaman Default, Input Nomor Halaman, dan Perpindahan Halaman saat Ganti Sort atau Page Size

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #24 (CatMany), hanya dibaca dan tidak diubah: 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` (tiga halaman pada 10 baris per halaman). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-363: Pagination default dan pilihan jumlah baris

1. Verifikasi tabel Categories List menampilkan 10 baris per halaman secara default
2. Buka pilihan jumlah baris per halaman
3. Verifikasi pilihan tepat 10, 25, 50, 100 tanpa opsi All
4. Pilih 25
5. Verifikasi halaman satu menampilkan 25 baris
6. Buka pilihan jumlah baris per halaman lalu pilih 50
7. Verifikasi halaman satu menampilkan 30 baris

### TC-FA-CAT-364: Input nomor halaman langsung dan kasus tepi

8. Buka pilihan jumlah baris per halaman lalu pilih 10
9. Ketik halaman `3` pada input nomor halaman, tekan `Enter`
10. Verifikasi halaman 3 tampil
11. Ketik halaman `0` pada input nomor halaman, tekan `Enter`
12. Verifikasi input `0` diabaikan dan tabel tetap di halaman 3
13. Ketik halaman `99` pada input nomor halaman, tekan `Enter`
14. Verifikasi input `99` (melebihi halaman terakhir) diabaikan dan tabel tetap di halaman 3
15. Ketik halaman `abc` pada input nomor halaman, tekan `Enter`
16. Verifikasi input `abc` (bukan angka) diabaikan dan tabel tetap di halaman 3

### TC-FA-CAT-365: Ganti page size kembali ke halaman 1, ganti sort tetap di halaman sekarang

17. Pindah ke halaman 2
18. Klik header Code satu kali
19. Verifikasi tabel tetap di halaman 2 setelah ganti sort
20. Ubah jumlah baris per halaman menjadi 25
21. Verifikasi tabel kembali ke halaman 1 setelah ganti page size

## Notes

- Langkah penghubung (S-03): langkah 8 (mengembalikan ukuran halaman ke 10 sebelum TC-364, S-09).
- Temuan untuk QA:
  - TC-364 tidak menyebut perilaku input nomor halaman bila `Enter` ditekan pada input tidak valid (apakah input dikosongkan atau mempertahankan teks); spec hanya mengasersi bahwa halaman tidak berpindah.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
