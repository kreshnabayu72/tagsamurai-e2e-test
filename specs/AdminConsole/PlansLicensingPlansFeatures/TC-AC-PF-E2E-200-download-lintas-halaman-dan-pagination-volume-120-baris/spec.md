---
id: TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris
title: Pagination modal Changelog Default dan Download lintas halaman dengan volume 120 baris
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-485
  - TC-AC-PF-689
  - TC-AC-PF-690
  - TC-AC-PF-691
coverage:
  web: automated
---

# Pagination modal Changelog Default dan Download lintas halaman dengan volume 120 baris

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup (volume 100 baris atau lebih, kelas e): Dataset Log Big (Changelog Default Principal 120 entri); Dataset Plan B (120 custom plan Principal `Paket 001` sampai `Paket 120`); Dataset Plan Q (custom plan `Paket Banyak Client` dengan 120 client Active `PT Massal 001` sampai `PT Massal 120`). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Default Principal tepat sama dengan Dataset Log Big dan menyediakan Dataset Plan B di hook `before`, menyediakan Dataset Plan Q sebagai langkah penghubung sebelum blok TC-AC-PF-690 (supaya daftar Custom Active berisi tepat 120 plan pada blok TC-AC-PF-689), dan memulihkan semuanya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog dan penyedia dataset volume; pembaca berkas CSV yang terunduh (baris header, jumlah dan isi baris); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini; ukuran halaman Page Size diubah di blok pertama dan dikembalikan ke `10` di blok berikutnya.

## Test Steps

### Pagination modal Changelog Default (TC-AC-PF-485)

1. Klik ikon Changelog pada toolbar tab Default
2. Verifikasi footer `Showing 1–10 of 120 entries`
3. Klik Next
4. Verifikasi footer `Showing 11–20 of 120 entries`
5. Buka Overlay Page Size
6. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100`
7. Pilih `25` pada Overlay Page Size
8. Verifikasi tampilan kembali ke halaman 1 dengan `Showing 1–25 of 120 entries`

### Download modal Changelog Default lintas halaman (TC-AC-PF-691)

9. Buka Overlay Page Size, pilih `10`
10. Verifikasi footer halaman 1 `Showing 1–10 of 120 entries`
11. Klik ikon Download
12. Pilih `Download as CSV`
13. Buka berkas CSV
14. Verifikasi berkas CSV memuat satu baris header dan 120 baris data, bukan 10

### Download tab Custom Active lintas halaman (TC-AC-PF-689)

15. Tutup modal dengan icon (X)
16. Klik tab Custom
17. Verifikasi footer `Showing 1–10 of 120 entries`
18. Klik ikon Download
19. Pilih `Download as CSV`
20. Buka berkas CSV
21. Verifikasi berkas CSV memuat satu baris header dan 120 baris data, bukan 10
22. Verifikasi baris data berisi `Paket 001` sampai `Paket 120`

### Download Tab Assigned Clients lintas halaman (TC-AC-PF-690)

23. Sediakan Dataset Plan Q lewat fixture BE, lalu tekan F5
24. Klik tab Custom
25. Ketik Search `Paket Banyak Client`, tekan Enter
26. Buka Plan Detail `Paket Banyak Client`
27. Klik Tab Assigned Clients
28. Verifikasi footer `Showing 1–10 of 120 entries`
29. Klik ikon Download
30. Pilih `Download as CSV`
31. Buka berkas CSV
32. Verifikasi berkas CSV memuat satu baris header dan 120 baris data, bukan 10
33. Verifikasi baris data berisi `PT Massal 001` sampai `PT Massal 120`

## Notes

- Langkah penghubung (S-03): langkah 9 mengembalikan Page Size ke `10` sebagai prasyarat footer TC-AC-PF-691; langkah 15 menutup modal; langkah 23 menyediakan Dataset Plan Q dan memuat ulang halaman; langkah 24 dan 25 membuka tab Custom dan mencari baris target `Paket Banyak Client` sebelum membuka Plan Detail (R-16).
- Urutan blok: TC-AC-PF-691 diletakkan sesudah TC-AC-PF-485 karena keduanya memakai Dataset Log Big pada modal yang sama (S-10).
- Kelas e (volume data) satu jenis harness: ketiga surface Download memakai dataset 120 baris dengan topik yang sama (Download memuat seluruh baris lintas halaman).
- Temuan untuk QA:
  - TC menetapkan 120 entri sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - TC-AC-PF-689 mengasersi `Showing 1–10 of 120 entries` dan 120 baris data pada tab Custom Active; angka itu hanya benar bila tidak ada custom plan Principal lain (Pre-setup lain atau Dataset Plan Q) di sub-tab yang sama, sehingga spec bergantung pada fixture BE yang menyetel daftar itu (S-13).
  - TC-AC-PF-690 tidak menyebut cara menemukan baris `Paket Banyak Client` pada daftar custom plan; spec memakai Search sebagai langkah penghubung.
