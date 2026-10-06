---
id: TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user
title: "Sinkronisasi Dua Arah: Perubahan Katalog Division Terfleksi Instan pada Dropdown Form User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-38
  - TC-GS-DIV-178
  - TC-GS-DIV-179
  - TC-GS-DIV-180
coverage:
  web: automated
---

# Sinkronisasi Dua Arah: Perubahan Katalog Division Terfleksi Instan pada Dropdown Form User

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buka tab Division lalu buat divisi baru 'Sync Division'
2. Pindah ke tab 'User List' lalu klik tombol '[+ User]'
3. Buka dropdown 'Division' pada form User
4. Verifikasi opsi 'Sync Division' langsung tersedia sebagai pilihan baru tanpa perlu refresh aplikasi
5. Tutup modal User lalu kembali ke tab Division
6. Edit divisi 'Sync Division' menjadi 'Sync Division Updated'
7. Buka kembali form Create User pada tab User List
8. Verifikasi nama opsi pada dropdown Division telah terbarukan menjadi 'Sync Division Updated'
9. Kembali ke tab Division lalu hapus divisi 'Sync Division Updated'
10. Buka kembali form Create User dan verifikasi opsi tersebut sudah hilang dari daftar pilihan

## Notes

- Memvalidasi dependensi kritis DIV-LOGIC-01 dan DIV-LOGIC-03 terhadap modul User (division.md §11).
