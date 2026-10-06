---
id: TC-AC-ACAL-E2E-017-tab-session-setup-column-overlay-screening
title: "Tab Session — Screening Dropdown Overlay Quick Panel dan struktur Popup Modal Setup Column 3 Zona"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-83
  - TC-AC-ACAL-84
coverage:
  web: automated
---

# Tab Session — Screening Dropdown Overlay Quick Panel dan struktur Popup Modal Setup Column 3 Zona

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab Session)

## Test Steps

### Screening Quick Overlay Panel

1. Klik header kolom `⋯` pada tabel Tab Session
2. Verifikasi overlay dropdown `"Column Visibility"` terbuka menampilkan 10 kolom dengan urutan default
3. Verifikasi seluruh 10 kolom dalam kondisi tercentang (checked) dan aktif (enabled)
4. Verifikasi setiap baris pada dropdown memiliki drag handle untuk mengatur urutan secara cepat

### Screening Popup Modal Setup Column 3 Zona

5. Klik menu `"Setup Column"` pada bagian bawah overlay
6. Verifikasi Popup Modal Setup Column terbuka dan memiliki 3 Zona:
   - **Zona 1 (Header):** Judul `"Setup Column"`, deskripsi `"Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."`, dan tombol close `(X)`
   - **Zona 2 (Body):** 10 baris daftar kolom (seluruhnya dapat di-hide) beserta panel Live Preview di sisi kanan
   - **Zona 3 (Footer):** Tombol `[Reset to Default]` di sisi kiri, serta tombol `[Cancel]` dan `[Save]` di sisi kanan
7. Klik tombol `(X)` untuk menutup modal

## Notes

- Memverifikasi kepatuhan desain UI Setup Column TAG Samurai rumus 2-level (Quick Overlay & Modal 3 Zona).
