---
id: TC-AC-SU-E2E-008-user-list-sorting-3-state-dan-guard-kolom-non-sortable
title: "Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-19
  - TC-AC-SU-274
  - TC-AC-SU-275
  - TC-AC-SU-276
coverage:
  web: automated
---

# Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat dataset pengguna dengan data variatif pada seluruh kolom

## Test Steps

### Verifikasi Default Sort dan Transisi Sort saat Filter Aktif

1. Buka halaman User List
2. Verifikasi urutan default tabel adalah kolom Name A-Z (Ascending)
3. Terapkan pencarian dan filter tertentu
4. Klik header kolom `Position`
5. Verifikasi pengurutan tabel beralih ke kolom Position tanpa mereset kata kunci pencarian atau kriteria filter aktif

### Siklus Sorting 3-State pada Seluruh Kolom Sortable

1. Lakukan siklus klik 3-state pada masing-masing dari 12 kolom sortable (`Active`, `Name`, `Email`, `Role`, `Position`, `Division`, `Employee ID`, `Modified By`, `Last Updated`, `Activation Status`, `Temporary User`, `Temporary Until`):
2. Klik 1: Verifikasi indikator Ascending (↑) aktif dan data terurut naik
3. Klik 2: Verifikasi indikator Descending (↓) aktif dan data terurut turun
4. Klik 3: Verifikasi indikator netral kembali ke default sort (Name A-Z)

### Guard Kolom Non-Sortable

1. Klik header kolom `TAG` dan header kolom `Custom Field`
2. Verifikasi tidak ada indikator sort yang muncul dan klik tidak memicu pengurutan apa pun pada tabel

## Notes

- Aturan sorting 3-state berlaku seragam di seluruh tabel platform TAG Samurai.
