---
id: TC-AC-DS-E2E-107-pagination-list-ukuran-halaman-dan-input-nomor
title: "Pagination List: Default 10 per Halaman, Opsi Ukuran, Input Nomor Halaman, dan Reset ke Halaman 1"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-362
  - TC-AC-DS-363
  - TC-AC-DS-364
  - TC-AC-DS-365
coverage:
  web: automated
---

# Pagination List: Default 10 per Halaman, Opsi Ukuran, Input Nomor Halaman, dan Reset ke Halaman 1

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Dengan default sort SKU A-Z, baris ke-5 sampai ke-123 adalah `SEED-001` sampai `SEED-119`.
- Tabel "Input tidak valid" untuk langkah 11 sampai 12: `0`, `-3`, `99`, `abc`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; ukuran halaman dikembalikan ke 10 di langkah 21.

## Test Steps

### TC-AC-DS-362: Pagination default dan opsi ukuran

1. Verifikasi pagination default 10 baris per halaman
2. Verifikasi total 13 halaman untuk 129 baris
3. Klik selector jumlah data per halaman
4. Verifikasi Overlay Page Size memuat opsi `10`, `25`, `50`, dan `100`
5. Verifikasi tidak ada opsi "All" pada Overlay Page Size
6. Tekan Esc

### TC-AC-DS-363: Input nomor halaman langsung

7. Ketik `5` pada input nomor halaman, tekan Enter
8. Verifikasi halaman 5 tampil dengan baris ke-41 sampai ke-50 (`SEED-037` sampai `SEED-046`)

### TC-AC-DS-364: Nomor halaman tidak valid

9. Klik nomor halaman 2
10. Untuk setiap baris tabel "Input tidak valid", lakukan langkah 11 sampai 12
11. Ketik {Input tidak valid} pada input nomor halaman, tekan Enter
12. Verifikasi input diabaikan dan tabel tetap pada halaman 2

### TC-AC-DS-365: Mengganti jumlah data per halaman

13. Klik nomor halaman 3
14. Ubah jumlah data per halaman menjadi 25
15. Verifikasi tabel kembali ke halaman 1
16. Verifikasi terdapat 6 halaman dengan 25 per halaman
17. Klik nomor halaman 2
18. Ubah jumlah data per halaman menjadi 100
19. Verifikasi tabel kembali ke halaman 1
20. Verifikasi terdapat 2 halaman dengan 100 per halaman
21. Ubah jumlah data per halaman menjadi 10

## Notes

- Langkah 11 sampai 12 diulang untuk empat baris tabel "Input tidak valid" (ekspansi 8 langkah; total spec 26 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Langkah penghubung (S-03, S-14): langkah 6 menutup overlay; langkah 17 memindahkan ke halaman 2 agar "kembali ke halaman 1" pada langkah 19 teramati (langkah TC hanya memulai dari halaman 3 sekali); langkah 21 memulihkan ukuran halaman; tanpa asersi tambahan.
- Langkah 8 memakai `SEED-037` sampai `SEED-046` sebagai turunan data Pre-setup #30; TC hanya menyebut baris ke-41 sampai ke-50.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 dan total 129 SKU (13 halaman, 6 halaman, 2 halaman). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - TC-AC-DS-365 Expected a menyebut kembali ke halaman 1 setelah perubahan ke 100, tetapi langkah TC memulai dari halaman 1 sesudah perubahan ke 25; spec menambah langkah 17.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
