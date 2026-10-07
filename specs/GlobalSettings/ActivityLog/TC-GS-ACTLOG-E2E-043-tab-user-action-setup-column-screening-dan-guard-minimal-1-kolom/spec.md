---
id: TC-GS-ACTLOG-E2E-043-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom
title: "Tab User Action Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-180
  - TC-GS-ACTLOG-181
  - TC-GS-ACTLOG-182
  - TC-GS-ACTLOG-189
  - TC-GS-ACTLOG-190
coverage:
  web: automated
---

# Tab User Action Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab User Action

## Test Steps

### Screening Overlay Column Visibility
1. Klik header kolom Actions (⋯) pada tabel Tab User Action.
2. Verifikasi overlay memuat 8 checkbox kolom berurutan: Date, Action, Object, Name, Field, Old Value, New Value, Modified By.
3. Verifikasi item 'Setup Column...' tampil di bagian bawah overlay.
### Toggle Cepat Tanpa Save
4. Pada overlay tersebut, hilangkan centang kolom 'Object'.
5. Verifikasi kolom Object langsung hilang dari tabel seketika tanpa perlu menekan tombol simpan.
6. Refresh browser (F5), verifikasi kolom Object tetap tersembunyi.
### Screening Modal Popup & Pembatalan
7. Buka overlay (⋯), klik item 'Setup Column...'.
8. Verifikasi modal dialog terbuka dengan judul 'Setup Column', 8 baris kolom, live preview, tombol [Cancel], [Reset to Default], [Save].
9. Hilangkan centang kolom Action, lalu klik tombol [Cancel].
10. Verifikasi popup tertutup dan kolom Action tetap tampil di tabel.
11. Buka kembali popup, ubah centang lalu klik tombol tutup (X), verifikasi perubahan dibatalkan.
### Guard Minimal 1 Kolom Visible
12. Buka modal Setup Column, sembunyikan kolom lain hingga hanya tersisa 1 kolom aktif (misal Action).
13. Arahkan kursor ke checkbox kolom terakhir tersebut, verifikasi checkbox berstatus disabled.
14. Verifikasi muncul tooltip 'At least one column must remain visible.'.
15. Centang kolom Date kembali, verifikasi checkbox kolom Action aktif kembali.

## Notes

- Setup Column Tab User Action mengelola 8 kolom dengan guard minimal satu kolom visible.
