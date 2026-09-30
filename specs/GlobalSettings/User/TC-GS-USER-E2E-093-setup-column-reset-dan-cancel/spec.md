---
id: TC-GS-USER-E2E-093-setup-column-reset-dan-cancel
title: 'Setup Column User List: Reset to Default dan Cancel membuang perubahan'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-306
  - TC-GS-USER-307
coverage:
  web: automated
---

# Setup Column User List: Reset to Default dan Cancel membuang perubahan

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data User List mock dengan sedikitnya 15 baris supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom disimpan di browser per user, jadi setiap spec Setup Column dimulai dari konfigurasi default

## Test Steps

### Cancel

1. Buka popup modal Setup Column dan hapus centang `Email` tanpa menyimpan
2. Klik `[Cancel]`
3. Verifikasi modal tertutup dan kolom `Email` tetap tampil di tabel
4. Buka popup modal lagi, hapus centang `Email`, lalu klik `✕`
5. Verifikasi modal tertutup dan kolom `Email` tetap tampil di tabel

### Reset to Default

6. Buka popup modal, hapus centang `Email`, centang `TAG`, lalu klik `[Save]`
7. Buka popup modal lagi dan klik `[Reset to Default]`
8. Verifikasi Live Preview kembali ke konfigurasi default (`Email` tampil, kolom Curated tersembunyi)
9. Klik `[Save]` lalu refresh halaman
10. Verifikasi tabel memakai konfigurasi default

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3.
