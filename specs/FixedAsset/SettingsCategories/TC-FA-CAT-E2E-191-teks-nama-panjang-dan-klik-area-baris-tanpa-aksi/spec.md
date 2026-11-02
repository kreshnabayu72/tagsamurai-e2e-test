---
id: TC-FA-CAT-E2E-191-teks-nama-panjang-dan-klik-area-baris-tanpa-aksi
title: "Teks Nama Panjang Tidak Di-Truncate dan Klik Area Baris di Luar Nama, Total Asset, Checkbox, dan Row Action Tidak Melakukan Aksi"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-387
  - TC-FA-CAT-636
coverage:
  web: automated
---

# Teks Nama Panjang Tidak Di-Truncate dan Klik Area Baris di Luar Nama, Total Asset, Checkbox, dan Row Action Tidak Melakukan Aksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), hanya dibaca dan tidak diubah: baris `Furniture` (Code `FURN`, leaf, Total Asset 5).
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dihapus hook `after`): kategori L1 ber-Category Name 120 karakter yang berakhiran `{runId}-191` (Fixture.settings-categories.longName120; nama diawali `Long ` dan diisi huruf sampai tepat 120 karakter termasuk sufiks).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-387: Teks nama panjang tidak di-truncate

1. Catat tinggi baris `Furniture` (baseline)
2. Ketik Search `{runId}-191`, tekan Enter
3. Verifikasi baris kategori ber-nama 120 karakter tampil
4. Verifikasi kolom Category melebar mengikuti isi (hug content) tanpa potongan `..`
5. Hover nama kategori ber-nama 120 karakter
6. Verifikasi tidak ada tooltip pada nama kategori
7. Verifikasi label header kolom tetap satu baris
8. Verifikasi tinggi baris kategori ber-nama 120 karakter sama dengan baseline langkah 1
9. Klik `✕` pada Search, tekan Enter

### TC-FA-CAT-636: Klik area baris di luar nama, Total Asset, checkbox, dan row action

10. Catat jumlah baris dan isi tabel (baseline)
11. Klik sel Code baris `Furniture`
12. Klik sel Modified By baris `Furniture`
13. Klik sel Last Updated baris `Furniture`
14. Klik ruang kosong pada baris `Furniture` di luar teks sel
15. Verifikasi tidak ada popup, dialog, atau navigasi yang terbuka
16. Verifikasi checkbox baris `Furniture` tidak tercentang
17. Verifikasi Bulk Action Bar tidak muncul
18. Verifikasi seleksi sidebar tetap `All Categories`
19. Verifikasi isi tabel sama dengan baseline langkah 10

## Notes

- Langkah penghubung (S-03): langkah 1 dan 10 (mencatat baseline), 2 dan 9 (Search untuk menemukan baris target dan mengosongkannya, R-16).
- Asersi absence pada langkah 15 sampai 17 memakai baris `Furniture` yang tampil dan diklik pada langkah 11 sampai 14 sebagai anchor.
- Temuan untuk QA:
  - TC-387 menyebut kategori 120 karakter "ditambahkan lewat seed API" tanpa menyebut isi nama; spec memakai nama milik spec berakhiran `{runId}-191` (S-06, S-12).
  - TC-636 menandai hint kelas `g` (absence) padahal tidak menegasi log; diperlakukan fungsional.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
