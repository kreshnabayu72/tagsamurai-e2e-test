---
id: TC-AC-SU-E2E-005-user-list-search-toolbar-per-kolom-dan-guard
title: "Pencarian toolbar User List per kolom teks dan guard kolom non-searchable"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-13
  - TC-AC-SU-14
  - TC-AC-SU-234
  - TC-AC-SU-235
  - TC-AC-SU-236
  - TC-AC-SU-237
  - TC-AC-SU-238
coverage:
  web: automated
---

# Pencarian toolbar User List per kolom teks dan guard kolom non-searchable

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat dataset pengguna dengan variasi Name, Email, Position, Division, Role, dan Modified By

## Test Steps

### Pencarian Berdasarkan Kolom Teks

1. Ketik sebagian nama pengguna (contoh: `"Alexander"`) di kotak Search toolbar lalu tekan Enter, verifikasi tabel hanya menampilkan pengguna dengan Name yang cocok
2. Ketik sebagian alamat email (contoh: `"@example.com"`) di kotak Search lalu tekan Enter, verifikasi tabel menyaring pengguna berdasarkan kolom Email
3. Ketik nama jabatan (contoh: `"Manager"`) di kotak Search lalu tekan Enter, verifikasi tabel menyaring pengguna berdasarkan kolom Position
4. Ketik nama divisi (contoh: `"Finance"`) di kotak Search lalu tekan Enter, verifikasi tabel menyaring pengguna berdasarkan kolom Division
5. Ketik nama role atau badge (contoh: `"Total Control"`) di kotak Search lalu tekan Enter, verifikasi tabel menyaring pengguna berdasarkan kolom Role
6. Ketik nama admin pengubah (contoh: `"Super Admin"`) di kotak Search lalu tekan Enter, verifikasi tabel menyaring pengguna berdasarkan kolom Modified By

### Guard Kolom Non-Searchable

1. Ketik kata kunci representasi switch status seperti `"true"`, `"false"`, atau string foto di kotak Search
2. Verifikasi pencarian TIDAK menghasilkan pencocokan berdasarkan status switch Active atau file foto avatar (memenuhi aturan Global Table Rules)

## Notes

- Pencarian toolbar mencakup seluruh atribut teks utama dan mengabaikan atribut non-teks.
