---
id: TC-AC-DS-E2E-022-scope-baris-principal-tidak-melihat-sku-distributor
title: "Scope Baris Principal: Tidak Melihat SKU Distributor dan Tanpa Tombol Aksi untuk SKU Distributor"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-77
  - TC-AC-DS-86
coverage:
  web: automated
---

# Scope Baris Principal: Tidak Melihat SKU Distributor dan Tanpa Tombol Aksi untuk SKU Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100`) dan seed #30 (total 129 SKU Principal, dari seeding), SKU Distributor PT Cakra Distribusi #31 (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`, tidak boleh terlihat oleh Principal), riwayat Changelog Principal #33 (entri Edit `UHF Handheld Reader (HHR-ARC-100)` Model/Type `H10` > `H100`, oleh `Jane S`). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-77: Principal tidak melihat SKU milik Distributor

1. Ketik Search `LOC-NOR`, tekan Enter
2. Verifikasi tabel menampilkan "No results found"
3. Verifikasi baris `LOC-NOR-01`, `LOC-NOR-02`, dan `LOC-NOR-03` tidak tampil pada List
4. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
5. Verifikasi baris `HHR-ARC-100` tampil
6. Klik `(←)` pada kotak Search
7. Klik ikon Changelog
8. Ketik Search `HHR-ARC-100` pada modal Changelog, tekan Enter
9. Verifikasi modal Changelog Principal memuat entri Edit `UHF Handheld Reader (HHR-ARC-100)` Model/Type `H10` > `H100`
10. Ganti isi kotak search modal Changelog dengan `LOC-NOR`, tekan Enter
11. Verifikasi modal Changelog tidak memuat entri SKU milik Distributor
12. Tutup modal Changelog

### TC-AC-DS-86: Principal melihat SKU globalnya tanpa tombol aksi untuk SKU Distributor

13. Ketik Search `HHR-ARC-100`, tekan Enter
14. Klik ⋯ baris `HHR-ARC-100`
15. Verifikasi menu memuat `Detail`, `Edit`, dan `Delete` untuk SKU Principal
16. Tutup menu aksi
17. Klik `(←)` pada kotak Search
18. Verifikasi List memuat tepat 129 SKU Principal tanpa SKU Distributor

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-77, TC-86.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 4, 13 (Search untuk menemukan baris atau memeriksa absence, R-16), 6 dan 17 (mengosongkan Search, S-09), 7 (membuka modal Changelog), 8 dan 10 (Search pada modal Changelog agar entri target dan absence teramati tanpa bergantung pada posisi halaman, S-14), 12, 14, 16 (menutup modal dan menu).
- Asersi absence langkah 3 didahului langkah 2 ("No results found" hasil Search sebagai anchor) dan langkah 5 (pencarian berfungsi, baris Principal tampil); langkah 11 didahului langkah 9 (entri Principal tampil pada modal yang sama).
- Langkah 18 membaca total baris List dari Pagination; angka 129 berasal dari seeding Pre-setup #30 (8b butir 10).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30/#31/#33 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30/#31 dan #33 (Changelog Principal) di environment belum diverifikasi.
  - TC-77 Expected c meminta modal Changelog "tidak memuat entri SKU milik Distributor" tanpa merinci cara memeriksa seluruh halaman; spec memakai Search modal `LOC-NOR` sebagai cara pemeriksaan (perilaku Search modal atas kode SKU belum diverifikasi).
  - Changelog adalah audit trail permanen yang tumbuh; entri `HHR-ARC-100` dicari lewat Search modal (S-14) alih-alih posisi halaman.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
