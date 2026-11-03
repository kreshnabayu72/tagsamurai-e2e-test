---
id: TC-AC-DS-E2E-134-usage-sort-company-entity-type-dan-total-stock
title: "Sort Usage: Company Default A-Z Tiga Tahap, Entity Type Badge, dan Total Stock Numerik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-451
  - TC-AC-DS-452
  - TC-AC-DS-453
coverage:
  web: automated
---

# Sort Usage: Company Default A-Z Tiga Tahap, Entity Type Badge, dan Total Stock Numerik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dan jaringan entitas (#32, #24): `PT Arunika Prima` (Principal) 55, `PT Cakra Distribusi` (Distributor) 25, `PT Delta Retail` (Client) 5, `PT Mitra Lintas Nusa` (Distributor dan Client) 20, `PT Surya Logistik` (Client) 15. Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE). Kolom Entity Type, Company, dan Total Stock masing-masing memuat sedikitnya dua nilai berbeda.
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil

### TC-AC-DS-451: Sort Usage Company default A-Z dan siklus tiga tahap

3. Verifikasi urutan awal Company A-Z: `PT Arunika Prima`, `PT Cakra Distribusi`, `PT Delta Retail`, `PT Mitra Lintas Nusa`, `PT Surya Logistik`
4. Klik header kolom Company sekali
5. Verifikasi klik pertama tetap Ascending (urutan A-Z)
6. Klik header kolom Company sekali lagi
7. Verifikasi klik kedua Descending dengan `PT Surya Logistik` pertama
8. Klik header kolom Company sekali lagi
9. Verifikasi klik ketiga kembali ke default (urutan A-Z)

### TC-AC-DS-452: Sort Usage Entity Type berdasarkan badge

10. Klik header kolom Entity Type sekali
11. Verifikasi Ascending: `PT Delta Retail` dan `PT Surya Logistik` (Client), lalu `PT Cakra Distribusi` dan `PT Mitra Lintas Nusa` (Distributor), lalu `PT Arunika Prima` (Principal)
12. Klik header kolom Entity Type sekali lagi
13. Verifikasi Descending: `PT Arunika Prima`, lalu `PT Cakra Distribusi` dan `PT Mitra Lintas Nusa`, lalu `PT Delta Retail` dan `PT Surya Logistik`
14. Verifikasi baris dengan nilai sort sama berurutan menurut default sort Company A-Z

### Pemulihan state antar TC

15. Klik header kolom Entity Type sekali lagi (kembali ke default)

### TC-AC-DS-453: Sort Usage Total Stock secara numerik

16. Klik header kolom Total Stock sekali
17. Verifikasi Ascending: 5, 15, 20, 25, 55 (`PT Delta Retail`, `PT Surya Logistik`, `PT Mitra Lintas Nusa`, `PT Cakra Distribusi`, `PT Arunika Prima`)
18. Klik header kolom Total Stock sekali lagi
19. Verifikasi Descending: 55, 25, 20, 15, 5

### Pemulihan state akhir

20. Klik header kolom Total Stock sekali lagi (kembali ke default); tutup popup dengan ikon close `[✕]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 15 dan 20 (menuntaskan siklus sort ke default, S-03, S-09).
- Expected 451 butir b dipecah menjadi langkah 5, 7, 9; Expected 452 butir a, b, c menjadi langkah 11, 13, 14; Expected 453 butir a dan b langkah 17 dan 19.
- Temuan untuk QA:
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - S-15: TC 451 butir b menyebut klik pertama "tetap Ascending" karena urutan awal sudah A-Z; hasil klik pertama tidak dapat dibedakan dari urutan awal, spec mengikuti TC.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
