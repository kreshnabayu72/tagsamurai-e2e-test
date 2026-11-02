---
id: TC-FA-GRP-E2E-193-resilience-download-tab-users-dan-tab-assets-gagal-server
title: "Resilience: Download Tab Users Gagal dan Download Tab Assets Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-673
  - TC-FA-GRP-726
coverage:
  web: automated
---

# Resilience: Download Tab Users Gagal dan Download Tab Assets Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user variasi role dan 24 aset aktif variasi status.
- Kemampuan teknis (disediakan tim FE): intercept parsial di atas backend nyata yang mengembalikan respons 5xx untuk request download Tab Users dan request download Tab Assets (endpoint tidak tertulis di TC, PRD, atau LLD sehingga tidak dituliskan di sini, S-13); intercept dipasang sebelum pemicu dan dilepas segera sesudah toast error diasersi (S-09); penangkap unduhan browser untuk memeriksa tidak adanya berkas.

## Test Steps

1. Klik angka Total User Warehouse A

### TC-673: Download Tab Users gagal

2. Pasang intercept 5xx untuk request download Tab Users
3. Catat jumlah baris yang tampil di tabel
4. Klik icon Download
5. Pilih Download as CSV
6. Verifikasi toast error "Error, failed to download Group-Users." tampil
7. Verifikasi tidak ada berkas terunduh
8. Verifikasi tabel tetap seperti semula (jumlah baris sama dengan yang dicatat)
9. Lepas intercept download Tab Users
10. Tutup popup Detail Group

### TC-726: Download Tab Assets gagal

11. Klik angka Total Asset Warehouse A (Tab Assets)
12. Pasang intercept 5xx untuk request download Tab Assets
13. Catat jumlah baris yang tampil di tabel
14. Klik icon Download
15. Pilih Download as CSV
16. Verifikasi toast error "Error, failed to download Group-Assets." tampil
17. Verifikasi tidak ada berkas terunduh
18. Verifikasi tabel tetap seperti semula (jumlah baris sama dengan yang dicatat)
19. Lepas intercept download Tab Assets

## Notes

- P-5 butir b: spec ini memuat dua TC objek-uji ringan kelas b (satu kegagalan 5xx pada tiap permukaan download, tanpa harness eksternal dan tanpa state berat), keduanya pada permukaan yang sama (download tabel detail Group) sehingga satu spec.
- Langkah penghubung (S-03): mencatat jumlah baris sebagai pembanding "tabel tetap seperti semula", melepas intercept, dan menutup popup Detail Group sebelum membuka Tab Assets.
- Temuan untuk QA:
  - TC-673 dan TC-726 tidak menyebut endpoint yang dibuat gagal dan tidak menyebut kode 5xx atau timeout; spec memakai 5xx. "Tabel tetap seperti semula" diasersi lewat jumlah baris yang dicatat sebelum aksi.
  - Mekanisme klik angka Total Asset Warehouse A sebagai pembuka Tab Assets mengikuti TC-726 langkah 2 ("Buka Detail Warehouse A (Tab Assets)").
