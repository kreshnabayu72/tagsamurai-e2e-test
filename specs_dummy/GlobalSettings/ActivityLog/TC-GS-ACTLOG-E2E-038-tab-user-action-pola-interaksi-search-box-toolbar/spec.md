---
id: TC-GS-ACTLOG-E2E-038-tab-user-action-pola-interaksi-search-box-toolbar
title: "Tab User Action: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-158
coverage:
  web: automated
---

# Tab User Action: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse)

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab User Action

## Test Steps

### Siklus Buka & Submit
1. Buka Tab User Action, klik icon Search pada toolbar.
2. Verifikasi kotak input Search melebar dengan placeholder 'Search user action log...'.
3. Ketik karakter 'e', verifikasi icon (✕) muncul di sisi kanan dan tabel belum tersaring.
4. Tekan tombol Enter pada keyboard, verifikasi tabel tersaring sesuai kata kunci 'e'.
### Siklus Clear Tanpa Reset
5. Klik icon (✕) di dalam kotak input.
6. Verifikasi teks terhapus, input tetap fokus, dan tabel MASIH mempertahankan hasil pencarian sebelumnya.
7. Tekan Enter saat input kosong, verifikasi tabel kembali menampilkan seluruh data normal.
### Siklus Collapse
8. Ketik kata kunci 'edit' lalu tekan Enter.
9. Klik icon panah kembali (←) di sebelah kiri kotak input.
10. Verifikasi kotak Search menutup kembali menjadi icon Search, kata kunci dibersihkan, dan tabel langsung kembali normal.

## Notes

- Pola interaksi search toolbar di Tab User Action seragam dengan Tab Session.
