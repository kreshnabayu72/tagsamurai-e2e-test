---
id: TC-GS-ACTLOG-E2E-026-tab-session-setup-column-screening-dan-guard-minimal-1-kolom
title: "Tab Session Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-93
  - TC-GS-ACTLOG-94
  - TC-GS-ACTLOG-95
  - TC-GS-ACTLOG-102
  - TC-GS-ACTLOG-103
coverage:
  web: automated
---

# Tab Session Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab Session

## Test Steps

### Screening Overlay Column Visibility
1. Klik header kolom Actions (⋯) pada tabel Tab Session.
2. Verifikasi overlay memuat 10 checkbox kolom berurutan: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device / Browser.
3. Verifikasi item 'Setup Column...' tampil di bagian bawah overlay.
### Toggle Cepat Tanpa Save
4. Pada overlay tersebut, hilangkan centang kolom 'Employee ID'.
5. Verifikasi kolom Employee ID langsung hilang dari tabel seketika tanpa perlu menekan tombol simpan.
6. Refresh halaman (F5), verifikasi kolom Employee ID tetap tersembunyi (tersimpan di cache).
### Screening Modal Popup & Pembatalan
7. Buka overlay (⋯), klik item 'Setup Column...'.
8. Verifikasi modal dialog terbuka dengan judul 'Setup Column', 10 baris kolom, live preview, tombol [Cancel], [Reset to Default], [Save].
9. Hilangkan centang kolom User, lalu klik tombol [Cancel].
10. Verifikasi popup tertutup dan kolom User tetap tampil di tabel.
11. Buka kembali popup, ubah centang lalu klik tombol tutup (X), verifikasi perubahan dibatalkan.
### Guard Minimal 1 Kolom Visible
12. Buka modal Setup Column, sembunyikan kolom lain hingga hanya tersisa 1 kolom aktif (misal User).
13. Arahkan kursor ke checkbox kolom terakhir tersebut, verifikasi checkbox berstatus disabled.
14. Verifikasi muncul tooltip 'At least one column must remain visible.'.
15. Centang kolom Date kembali, verifikasi checkbox kolom User aktif kembali.

## Notes

- Fitur Setup Column mencegah pengguna menyembunyikan seluruh kolom tabel secara tidak sengaja.
