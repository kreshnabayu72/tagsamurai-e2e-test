---
id: TC-GS-DIV-E2E-001-screening-tabel-utama-dan-struktur-halaman
title: "Screening 3 Zona Tabel Division List dan Default Sort Name A-Z"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-01
  - TC-GS-DIV-02
coverage:
  web: automated
---

# Screening 3 Zona Tabel Division List dan Default Sort Name A-Z

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia data seed awal Head Office (in-use oleh default user) dan Human Resources (in-use oleh user dinamis Budi Santoso)
- Tersedia minimal 3 data divisi dengan awalan huruf berbeda untuk membuktikan default sort

## Test Steps

1. Buka menu Global Settings > User
2. Klik tab 'Division' pada navigasi sub-tab
3. Verifikasi Header halaman: breadcrumb menampilkan 'User', sub-tab memuat 'User List | Position | Division (aktif) | Custom Field'
4. Verifikasi TableTools di sisi kanan toolbar memuat: Search 🔖 | Filter | Download | Changelog (⏱) | [+ Division]
5. Verifikasi Body tabel memuat kolom terurut: Checkbox (seleksi), Name (sortable), Code (sortable), Last Updated (sortable), dan Actions (⋯) (unsortable)
6. Verifikasi data terurut alfabetis A-Z case-insensitive berdasarkan kolom Name secara default tanpa indikator sort aktif pada header
7. Verifikasi Footer tabel menampilkan kontrol paginasi default 10 per halaman, info jumlah record, dan tombol navigasi halaman

## Notes

- Division adalah sub-tab pada modul Global Settings User, bukan menu sidebar terpisah (division.md §4.1).
- Genuinely empty state (0 data) tidak reachable pada entitas normal karena selalu ada seed Head Office (DIV-LOGIC-01).
