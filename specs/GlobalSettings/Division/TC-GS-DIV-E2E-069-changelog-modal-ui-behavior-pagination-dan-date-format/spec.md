---
id: TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format
title: "Modal Changelog: Header Column Visibility Tanpa Sort, Kontrol Pagination, Dismiss Modal, dan Kepatuhan Format Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-209
  - TC-GS-DIV-210
  - TC-GS-DIV-211
  - TC-GS-DIV-212
coverage:
  web: automated
---

# Modal Changelog: Header Column Visibility Tanpa Sort, Kontrol Pagination, Dismiss Modal, dan Kepatuhan Format Tanggal

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Changelog terbuka dan memuat >50 entri riwayat
- General Settings Date Format DD/MM/YY dan Time Format 24-jam
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Riwayat memuat lebih dari 50 entri
- General Settings Date Format `DD/MM/YY` (default) dan Time Format 24-jam

## Test Steps

### Kolom Column Visibility Modal Changelog tidak memiliki ikon sort (TC-GS-DIV-209)

1. Klik icon Changelog di Table Tools
2. Perhatikan header kolom Column Visibility (⋯)
3. Verifikasi Header kolom Column Visibility (⋯) tidak memiliki ikon sort

### Pagination Modal Changelog: default 10 dan pilihan 10, 25, 50, 100 (TC-GS-DIV-210)

4. Klik icon Changelog di Table Tools
5. Perhatikan jumlah baris halaman 1
6. Pilih page size 25, 50, dan 100
7. Verifikasi Default 10 baris per halaman
8. Verifikasi Page size 25, 50, 100 menampilkan sampai 25, 50, 100 baris per halaman; tanpa opsi All

### Modal Changelog ditutup lewat icon close dan klik di luar modal (TC-GS-DIV-211)

9. Klik icon Changelog di Table Tools
10. Klik icon `[✕]`
11. Klik icon Changelog di Table Tools lagi lalu klik area gelap di luar modal
12. Verifikasi Modal tertutup lewat icon close
13. Verifikasi Modal tertutup lewat klik di luar modal

### Format tanggal Modal Changelog dan input Date filter mengikuti General Settings (TC-GS-DIV-212)

14. Klik icon Changelog di Table Tools
15. Lihat kolom Date
16. Buka Filter dan pilih rentang tanggal
17. Verifikasi Kolom Date tampil dengan format General Settings (tanggal, jam, timezone entitas)
18. Verifikasi Teks tanggal pada input Date filter mengikuti Date Format General Settings (`DD/MM/YY`)

## Notes

- Memvalidasi perilaku dasar modal Changelog: header kolom Column Visibility (⋯) tidak memiliki icon sort, pagination 10/25/50/100 tanpa opsi All, penutupan modal via icon X dan klik di luar modal (backdrop), serta format tanggal mengikuti konfigurasi General Settings (PRD §4.1.2, §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-209, TC-GS-DIV-210, TC-GS-DIV-211, TC-GS-DIV-212.
