---
id: TC-AC-DS-E2E-110-download-list-nama-file-nol-baris-dan-distributor
title: "Download List: Nama File dan Ekstensi, Nol Baris, Tanpa Toast Sukses, dan Download oleh Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-373
  - TC-AC-DS-375
  - TC-AC-DS-377
  - TC-AC-DS-579
coverage:
  web: automated
---

# Download List: Nama File dan Ekstensi, Nol Baris, Tanpa Toast Sukses, dan Download oleh Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (langkah 24): Total Control Distributor PT Cakra Distribusi, Local Registration aktif, `totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT Arunika Prima).
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti; `SFR-VEL-4P` Brand `Veltrix`), #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dan #31 (SKU lokal Distributor PT Cakra Distribusi `LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`; SKU Distributor PT Nusantara Mitra `NUS-LOC-01`; SKU Distributor PT Mandala Niaga `MAN-LOC-01`). Dipasang idempoten oleh seeding di hook `before`.
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Kemampuan teknis: pembaca berkas unduhan CSV dan XLSX (nama berkas, pemisah, encoding dan BOM, nama sheet, header kolom, serta jumlah dan kode SKU baris data) disediakan tim FE.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-373: Nama file dan ekstensi

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi file pertama bernama `Device-SKU.csv`
4. Verifikasi file pertama memakai pemisah koma
5. Verifikasi file pertama memakai encoding UTF-8 dengan BOM
6. Klik ikon Download
7. Klik `Download as XLSX`
8. Verifikasi file kedua bernama `Device-SKU.xlsx`
9. Verifikasi file kedua memiliki satu sheet bernama `Sheet1`

### TC-AC-DS-377: Download berhasil tanpa toast sukses

10. Klik ikon Download
11. Klik `Download as CSV`
12. Verifikasi tidak ada toast sukses apa pun
13. Verifikasi file terunduh langsung

### TC-AC-DS-375: Download dengan nol baris

14. Ketik Search `BLE`, tekan Enter
15. Klik ikon Filter
16. Pada field Brand pilih `Veltrix`
17. Klik `[Apply]`
18. Verifikasi tombol Download tetap aktif
19. Klik ikon Download
20. Klik `Download as CSV`
21. Verifikasi tidak ada toast
22. Verifikasi file terunduh berisi hanya baris header kolom yang tampil
23. Klik `[Clear Field]`, lalu `[Apply]`, lalu klik `(←)` pada kotak Search

### TC-AC-DS-579: Download List oleh Distributor

24. Ganti akun: Logout dari Total Control Principal PT Arunika Prima, lalu login sebagai Total Control Distributor PT Cakra Distribusi (`totalControlDist_automated_{namaCompany}@qwertysystem.net`)
25. Buka halaman `Settings > Device > Device SKU`
26. Klik ikon Download
27. Klik `Download as CSV`
28. Verifikasi tidak ada toast
29. Verifikasi file `Device-SKU.csv` terunduh berisi header dan 132 baris data: 129 SKU Principal (read-only) dan `LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03` milik Distributor
30. Verifikasi file tidak memuat `NUS-LOC-01` (PT Nusantara Mitra) dan `MAN-LOC-01` (PT Mandala Niaga)

## Notes

- Urutan blok: TC-AC-DS-377 dan TC-AC-DS-375 dikerjakan sebelum TC-AC-DS-579 karena TC-AC-DS-579 memakai akun lain; sumber memuat 373, 375, 377, 579.
- Langkah penghubung (S-03, S-07): langkah 23 melepas Filter dan Search; langkah 24 sampai 25 adalah ganti akun eksplisit dan membuka halaman karena hook `beforeEach` hanya membuka halaman untuk akun pertama; tanpa asersi tambahan.
- Asersi absence toast pada langkah 12, 21, dan 28 diletakkan segera setelah pemicu dan sebelum asersi berkas (8b butir 11); berkas terunduh menjadi anchor positifnya. Langkah 30 didahului langkah 29 yang membuktikan baris SKU lain tampil di berkas.
- TC-AC-DS-373 memuat asersi isi berkas (pemisah, encoding dan BOM, nama sheet) yang termasuk kelas binary buffer; TC itu ada di spec ini bersama nama berkas (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-AC-DS-373 mengasersi pemisah, encoding UTF-8 BOM, dan nama sheet (isi berkas, kelas binary buffer konvensi bagian 3 prinsip 13 butir f); perlu keputusan apakah dipindah ke spec binary buffer.
  - Fixture rancangan belum diverifikasi ada di environment: SKU Distributor lain (`NUS-LOC-01` Model/Type `NM-01`, `MAN-LOC-01` Model/Type `MN-01`) dan SKU lokal Distributor (#31).
  - S-12: asersi bergantung pada nama literal Pre-setup #29, #30, dan #31 serta total 129 dan 132 baris. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan `AC_DS_DIST_PASSWORD` serta berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
