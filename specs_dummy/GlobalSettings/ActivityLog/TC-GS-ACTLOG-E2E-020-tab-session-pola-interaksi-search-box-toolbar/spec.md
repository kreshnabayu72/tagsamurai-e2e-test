---
id: TC-GS-ACTLOG-E2E-020-tab-session-pola-interaksi-search-box-toolbar
title: "Tab Session: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-65
coverage:
  web: automated
---

# Tab Session: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse)

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab Session dengan data log tersedia

## Test Steps

### Siklus Buka & Submit Search
1. Klik icon Search pada toolbar sisi kanan Tab Session.
2. Verifikasi kotak input Search melebar, kursor otomatis fokus, placeholder menampilkan 'Search session log...'.
3. Ketik karakter 'j', verifikasi icon (✕) muncul di sisi kanan input dan tabel belum tersaring.
4. Tekan tombol Enter pada keyboard, verifikasi tabel tersaring sesuai kata kunci 'j'.
### Siklus Clear Tanpa Reset
5. Klik icon (✕) di dalam kotak input.
6. Verifikasi teks di dalam input terhapus dan kotak input tetap dalam kondisi terbuka dan fokus.
7. Verifikasi tabel MASIH mempertahankan hasil saringan 'j' sebelumnya (tidak langsung mereset data).
8. Tekan Enter saat kotak input kosong, verifikasi tabel kembali menampilkan seluruh data tanpa saringan.
### Siklus Collapse
9. Ketik kata kunci 'john' lalu tekan Enter.
10. Klik icon panah kembali (←) di sebelah kiri kotak input.
11. Verifikasi kotak Search menutup kembali menjadi icon Search, kata kunci dihapus, dan tabel langsung kembali menampilkan seluruh data.

## Notes

- Pola interaksi search toolbar mematuhi prd-conventions.md §9.1b.
