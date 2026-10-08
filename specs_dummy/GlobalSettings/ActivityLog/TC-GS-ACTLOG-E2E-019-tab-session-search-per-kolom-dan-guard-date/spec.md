---
id: TC-GS-ACTLOG-E2E-019-tab-session-search-per-kolom-dan-guard-date
title: "Tab Session: Search Substring, Case-Insensitive, Status Nilai Tampil, dan Guard Kolom Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-56
  - TC-GS-ACTLOG-57
  - TC-GS-ACTLOG-58
  - TC-GS-ACTLOG-59
  - TC-GS-ACTLOG-60
  - TC-GS-ACTLOG-61
  - TC-GS-ACTLOG-62
  - TC-GS-ACTLOG-63
  - TC-GS-ACTLOG-64
coverage:
  web: automated
---

# Tab Session: Search Substring, Case-Insensitive, Status Nilai Tampil, dan Guard Kolom Date

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat variasi data log Session di entitas aktif

## Test Steps

### Pencarian Substring & Case-Insensitive
1. Buka Tab Session, uji pencarian substring per kolom teks (Employee ID, Position, Division, Activity, Status, Note, IP, Device).
2. Verifikasi pencarian tidak membedakan huruf besar dan kecil (case-insensitive, misal 'emp002' menemukan 'EMP002', 'finance' menemukan 'Finance').
### Pencarian Nama Pengguna
3. Masukkan nama depan 'john' di kotak Search, verifikasi menemukan baris 'John D'.
4. Masukkan nama belakang 'doe' di kotak Search, verifikasi menemukan baris 'John D' (mencocokkan full underlying name).
### Pencarian Kolom Status Nilai Tampil
5. Masukkan keyword 'Failed' di kotak Search.
6. Verifikasi baris Login Failed dan Reset Password Failed tampil.
7. Verifikasi baris Logout dan Session (yang Status-nya tampil '—') TIDAK tampil.
8. Masukkan keyword 'Success', verifikasi baris Logout dan Session tidak ikut tampil.
### Guard Kolom Date & Kolom Tersembunyi
9. Masukkan keyword format tanggal (misal '14 Jul 2026') di kotak Search, tekan Enter.
10. Verifikasi tidak ada baris yang cocok ('No results found') karena kolom Date tidak searchable via search box toolbar.
11. Sembunyikan kolom Employee ID via Column Visibility, cari keyword 'EMP002', verifikasi tidak ditemukan.
12. Tampilkan kembali kolom Employee ID, cari 'EMP002', verifikasi baris kembali ditemukan.
### Spasi & Pencarian Multi-Kolom
13. Masukkan keyword dengan spasi di awal dan akhir '  EMP002  ', verifikasi spasi dipangkas dan hasil pencarian valid.
14. Masukkan keyword 'password', verifikasi baris yang cocok di kolom Activity (Change Password, Reset Password) maupun Note (Login with password, Incorrect password) tampil bersamaan.

## Notes

- Search box toolbar menyaring seluruh kolom teks yang visible dan mengecualikan kolom Date.
