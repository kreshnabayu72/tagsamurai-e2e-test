---
id: TC-AC-DS-E2E-177-state-tenant-baca-dan-download-suspended-expired
title: "State Tenant: Suspended dan Expired Tetap Dapat Membaca List dan Download"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-35
  - TC-AC-DS-577
  - TC-AC-DS-578
coverage:
  web: automated
---

# State Tenant: Suspended dan Expired Tetap Dapat Membaca List dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Bahari Teknik, Suspended (Hendra Saputra, Modified By `Hendra S`): `totalControlDistSusp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTSUSP_PASSWORD` (Pre-setup #18). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (di akhir iterasi sebelumnya): Total Control Distributor PT Kencana Daya, Expired (Maya Anggraini, Modified By `Maya A`): `totalControlDistExp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTEXP_PASSWORD` (Pre-setup #19).
- State global: status entitas (Suspended, Expired) adalah state Pre-setup dan tidak diubah spec. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Pre-setup (hanya dibaca): SKU inti dan seed (#29, #30), SKU lokal Distributor Suspended `BAH-LOC-01` dan Expired `KEN-LOC-01` (#18, #19), General Settings (#35).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan `Device-SKU.csv` (header dan jumlah baris data).

## Test Steps

### TC-AC-DS-35: Entitas Suspended tetap dapat membaca List

1. Klik ikon Changelog
2. Verifikasi List Device SKU tampil dengan baris SKU yang berhak dilihat Distributor
3. Verifikasi modal Changelog terbuka normal
4. Tutup modal, ketik Search `BAH-LOC-01`, tekan Enter, lalu klik SKU `BAH-LOC-01`
5. Verifikasi Popup Device SKU Detail terbuka normal
6. Tutup popup lalu klik ⋯ pada baris `BAH-LOC-01`
7. Verifikasi tombol `[+ SKU]` tampil
8. Verifikasi tombol ⋯ pada baris `BAH-LOC-01` memuat `Detail`, `Edit`, dan `Delete`
9. Tutup menu ⋯ lalu klik `(←)` pada kotak Search

### TC-AC-DS-577: Download List oleh Distributor Suspended tetap berjalan tanpa toast

10. Klik ikon Download
11. Klik `Download as CSV`
12. Verifikasi tidak ada toast, termasuk toast "Changes can't be saved while this workspace is suspended or expired."
13. Buka file `Device-SKU.csv` dan periksa baris data serta kode SKU `BAH-LOC-01`
14. Verifikasi file `Device-SKU.csv` terunduh berisi header dan 130 baris data: 129 SKU Principal (read-only) dan `BAH-LOC-01` milik Distributor

### TC-AC-DS-578: Download List oleh Distributor Expired tetap berjalan tanpa toast

15. Logout lalu login sebagai Total Control Distributor PT Kencana Daya (Expired) (`totalControlDistExp_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DISTEXP_PASSWORD`) dan buka halaman `Settings > Device > Device SKU`
16. Klik ikon Download
17. Klik `Download as CSV`
18. Verifikasi tidak ada toast, termasuk toast "Changes can't be saved while this workspace is suspended or expired."
19. Buka file `Device-SKU.csv` dan periksa baris data serta kode SKU `KEN-LOC-01`
20. Verifikasi file `Device-SKU.csv` terunduh berisi header dan 130 baris data: 129 SKU Principal (read-only) dan `KEN-LOC-01` milik Distributor

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search `BAH-LOC-01` pada langkah 4 (menemukan baris target, R-16), penutupan modal, popup, dan menu, serta langkah 15 (ganti akun eksplisit; sesi dikembalikan ke akun default suite di hook `after`).
- Absence toast (langkah 12 dan 18) diasersi tepat sesudah klik `Download as CSV` dan sebelum asersi berkas (8b butir 11): pemicu (klik pilihan format) menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 14 dan 20).
- Temuan untuk QA:
  - TC 35 berjudul "Entitas Suspended atau Expired" tetapi langkah dan Precondition hanya memuat Distributor Suspended (#18); spec menjalankan Suspended saja untuk TC 35 dan Expired hanya untuk Download (TC 578).
  - Entitas Pre-setup #18, #19, #20 (nama tampil, Model/Type `B-01`/`K-01`, SKU `EXP-PRI-01`) adalah data rancangan yang belum terverifikasi ada di environment.
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
