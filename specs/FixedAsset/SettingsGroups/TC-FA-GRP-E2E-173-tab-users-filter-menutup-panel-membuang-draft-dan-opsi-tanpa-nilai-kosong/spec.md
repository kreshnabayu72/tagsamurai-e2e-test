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

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A

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

10. Telusuri semua halaman tabel dari halaman 1 sampai menemukan user ber-Position `—`, lalu catat nama satu user itu
11. Kembali ke halaman 1 pagination tabel
12. Klik icon Filter, buka dropdown Position
13. Verifikasi dropdown Position memuat sedikitnya satu opsi Position
14. Verifikasi dropdown Position tidak memuat opsi `—` atau nilai kosong
15. Pilih satu opsi, klik [Apply]
16. Verifikasi sedikitnya satu baris tampil pada tabel
17. Ketik Search nama user ber-Position kosong yang dicatat pada langkah 10, tekan Enter
18. Verifikasi user ber-Position kosong yang dicatat pada langkah 10 tidak tampil
19. Klik `(←)` pada kotak Search
20. Verifikasi badge titik tampil
21. Buka Filter, klik [Clear Field], klik [Apply]
22. Ketik Search nama user ber-Position kosong yang dicatat pada langkah 10, tekan Enter
23. Verifikasi user ber-Position kosong yang dicatat pada langkah 10 tampil kembali
24. Klik `(←)` pada kotak Search
25. Verifikasi badge titik hilang

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup Filter Panel di tengah spec, menelusuri halaman untuk menemukan user ber-Position kosong, serta `Ketik Search` nama user itu dan `(←)` agar absence dan kemunculan kembali user diamati tanpa bergantung pada halaman 1 (S-14).
- Asersi tambahan (S-03, 8b.2): langkah `Catat nama baris halaman 1 tabel` dan `Catat nama satu user ber-Position kosong` (hasil penelusuran semua halaman) menjadi baseline asersi "tabel tidak berubah" dan absence user ber-Position kosong; `Verifikasi sedikitnya satu baris tampil pada tabel` menjadi anchor positif sebelum absence user ber-Position kosong, dan `Verifikasi dropdown Position memuat sedikitnya satu opsi Position` menjadi anchor positif sebelum absence opsi `—`. Bukan klausa Expected TC.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - TC-1135 dan TC-1136 tidak menyebut baris sampel pembanding; asersi "tabel tidak berubah" dan "user ber-Position kosong tidak tampil" memakai data Warehouse A pada Prerequisites. TC-1136 tidak menyebut cara memastikan bahwa user ber-Position kosong benar ada sebelum filter; spec memakai Prerequisites.
