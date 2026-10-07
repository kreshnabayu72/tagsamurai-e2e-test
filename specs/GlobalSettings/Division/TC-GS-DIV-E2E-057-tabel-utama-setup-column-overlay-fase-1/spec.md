---
id: TC-GS-DIV-E2E-057-tabel-utama-setup-column-overlay-fase-1
title: "Setup Column Tabel Utama Fase 1: Overlay Column Visibility pada Header Kolom Actions, Toggle Cepat Visibilitas, dan Guard Minimal 1 Kolom Tersisa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-167
  - TC-GS-DIV-168
  - TC-GS-DIV-169
coverage:
  web: automated
---

# Setup Column Tabel Utama Fase 1: Overlay Column Visibility pada Header Kolom Actions, Toggle Cepat Visibilitas, dan Guard Minimal 1 Kolom Tersisa

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tabel Division tampil
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Ubah page size ke 25, 50, dan 100 (TC-GS-DIV-167)

1. Pilih page size 25
2. Pilih page size 50
3. Pilih page size 100
4. Verifikasi 25: halaman 1 berisi 25 baris dan total 2 halaman
5. Verifikasi 50: seluruh 32 baris pada 1 halaman
6. Verifikasi 100: seluruh 32 baris pada 1 halaman

### Navigasi Next, Previous, dan input nomor halaman lewat Enter (TC-GS-DIV-168)

7. Klik Next ke halaman 2
8. Klik Previous
9. Ketik `4` pada input nomor halaman lalu Enter
10. Verifikasi Next menampilkan halaman 2, Previous kembali ke halaman 1
11. Verifikasi Input `4` lalu Enter langsung membuka halaman 4 yang berisi 2 baris

### Apply Filter dari halaman lebih dari 1 mereset ke halaman 1 (TC-GS-DIV-169)

12. Pindah ke halaman 3
13. Buka Filter, pilih rentang tanggal pre-setup, klik `[Apply]`
14. Verifikasi Tabel kembali ke halaman 1 dengan hasil filter

## Notes

- Memvalidasi Fase 1 Setup Column: klik header Actions (⋯) membuka panel overlay Column Visibility, toggle cepat kolom data (Name, Code, Last Updated), dan pencegahan uncheck seluruh kolom (minimal 1 kolom visible tersisa) (PRD §4.1.1, §4.2e, prd-conventions.md §9.3).
- Sumber pemetaan test case granular: TC-GS-DIV-167, TC-GS-DIV-168, TC-GS-DIV-169.
