---
id: TC-FA-GRP-E2E-173-tab-users-filter-menutup-panel-membuang-draft-dan-opsi-tanpa-nilai-kosong
title: "Tab Users Filter: Menutup Panel Tanpa [Apply] Membuang Draft dan Dropdown Tanpa Opsi Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1135
  - TC-FA-GRP-1136
coverage:
  web: automated
---

# Tab Users Filter: Menutup Panel Tanpa [Apply] Membuang Draft dan Dropdown Tanpa Opsi Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan Position terisi (sedikitnya dua nilai distinct) dan sedikitnya satu user dengan Position kosong (tampil `—`).
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Klik angka Total User Warehouse A

### TC-1135: Menutup panel tanpa [Apply] membuang draft

2. Catat nama baris halaman 1 tabel
3. Klik icon Filter, pilih satu Position tanpa klik [Apply]
4. Klik di luar panel
5. Verifikasi tabel tidak berubah: nama baris halaman 1 sama dengan yang dicatat pada langkah 2
6. Klik icon Filter
7. Verifikasi panel kosong (tidak ada draft)
8. Verifikasi badge titik tidak tampil
9. Tutup Filter Panel

### TC-1136: Dropdown tanpa opsi nilai kosong

10. Catat nama satu user ber-Position `—` pada tabel
11. Klik icon Filter, buka dropdown Position
12. Verifikasi dropdown Position tidak memuat opsi `—` atau nilai kosong
13. Pilih satu opsi, klik [Apply]
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi user ber-Position kosong yang dicatat pada langkah 10 tidak tampil
16. Verifikasi badge titik tampil
17. Buka Filter, klik [Clear Field], klik [Apply]
18. Verifikasi user ber-Position kosong yang dicatat pada langkah 10 tampil kembali
19. Verifikasi badge titik hilang

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup Filter Panel di tengah spec.
- Asersi tambahan (S-03, 8b.2): langkah `Catat nama baris halaman 1 tabel` dan `Catat nama satu user ber-Position kosong pada tabel` menjadi baseline asersi "tabel tidak berubah" dan absence user ber-Position kosong; `Verifikasi sedikitnya satu baris tampil pada tabel` menjadi anchor positif sebelum absence. Bukan klausa Expected TC.
- Temuan untuk QA:
  - TC-1135 dan TC-1136 tidak menyebut baris sampel pembanding; asersi "tabel tidak berubah" dan "user ber-Position kosong tidak tampil" memakai data Warehouse A pada Prerequisites. TC-1136 tidak menyebut cara memastikan bahwa user ber-Position kosong benar ada sebelum filter; spec memakai Prerequisites.
