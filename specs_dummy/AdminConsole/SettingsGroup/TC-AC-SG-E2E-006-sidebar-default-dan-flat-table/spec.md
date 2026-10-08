---
id: TC-AC-SG-E2E-006-sidebar-default-dan-flat-table
title: "Sidebar default state dan render tabel flat lintas semua level saat All Groups aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-8
  - TC-AC-SG-167
coverage:
  web: automated
---

# Sidebar default state dan render tabel flat lintas semua level saat All Groups aktif

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia pohon hierarki 3 level: `"Region A"` (level 1) > `"Branch 1"` (level 2) > `"Sub Branch 1"` (level 3)

## Test Steps

### Default State Sidebar & Header
1. Buka halaman `Settings > Group`
2. Verifikasi pada Sidebar Group Tree, node root `"All Groups"` berstatus aktif / terpilih secara default
3. Verifikasi seluruh percabangan pohon di sidebar berada dalam status ter-expand (seluruh level terlihat)
4. Verifikasi Group Context Header di atas tabel menampilkan teks `"All Groups"` beserta angka Total User dan Total Member agregat
### Render Tabel Flat Lintas Level
5. Amati baris-baris pada tabel utama
6. Verifikasi tabel merender seluruh node sebagai deretan baris flat lintas semua kedalaman
7. Verifikasi `"Region A"` (level 1), `"Branch 1"` (level 2), dan `"Sub Branch 1"` (level 3) semuanya tampil bersamaan sebagai baris di tabel utama

## Notes

- State "All Groups" tidak menyaring tabel; seluruh pohon disajikan secara flat (ACSG-LOGIC-09).
