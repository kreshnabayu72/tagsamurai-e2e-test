---
id: TC-FA-FAAM-E2E-143-download-lebih-dari-5000-baris
title: "Download List: Lebih dari 5.000 Baris Memakai Loading Screen"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-461
coverage:
  web: automated
---

# Download List: Lebih dari 5.000 Baris Memakai Loading Screen

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Dinamis: katalog Asset Name di atas 5.000 baris (Pre-setup #15f) disiapkan lewat seed API di hook `before` dan dihapus di hook `after` (disediakan tim FE/BE); jumlah baris seed dicatat oleh seeding dan dipakai langkah. Ceiling Master Data Count Limit dan Selection Limit dibaca dari System Limits (tidak di-hardcode) dan harus mengizinkan jumlah seed; pemulihan di hook `after`.
- Kemampuan teknis: mengunduh berkas dari browser dan membaca isi berkas XLSX atau CSV (sel, encoding, nama sheet) lewat pembaca berkas; disediakan tim FE/BE.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: katalog di atas 5.000 baris di-seed oleh spec ini dan dibersihkan di hook `after`; System Limits (Master Data Count Limit) hanya dibaca dan dipulihkan di hook `after` bila diubah seeding. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-461: Download di atas 5.000 baris memakai loading screen tanpa job background
1. Klik icon Download lalu `Download as CSV`
2. Verifikasi loading screen tampil
3. Verifikasi tidak ada toast, notifikasi in-app, atau job background
4. Verifikasi berkas langsung terunduh setelah loading screen selesai
5. Verifikasi berkas memuat seluruh baris (sama dengan jumlah baris seed)

## Notes

- Asersi absence toast, notifikasi, dan job latar diletakkan segera sesudah pemicu unduh dan sebelum asersi berkas (bagian 8b butir 11); loading screen yang tampil adalah anchor positif bahwa unduh berjalan.
- Temuan untuk QA: Pre-setup #15f hanya menulis "Katalog di atas 5.000 baris disiapkan lewat seed API" tanpa nama client dan tanpa akun aktornya; spec memakai akun Total Control client utama dengan katalog seed milik spec. Jumlah baris yang tepat tidak ditulis TC (disediakan seeding).
