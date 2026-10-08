---
id: TC-GS-USER-E2E-144-create-user-distributor-entity-access-options
title: Buat user di entity Distributor membatasi opsi Access ke Admin Console
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-603
coverage:
  web: automated
---

# Buat user di entity Distributor membatasi opsi Access ke Admin Console

## Prerequisites

- Login sebagai Role: Total Control, entity Distributor
- Akun dengan Role Total Control ada di entity Distributor
- Sebuah Division ada di master data entity Distributor
- Email user baru unik per run

## Test Steps

1. Klik `[+ User]` untuk membuka modal Create
2. Verifikasi opsi Access hanya memuat "Admin Console" dan "Global Settings"
3. Verifikasi produk Client "FAMS", "SAMS", dan "SIEM" tidak ada dalam daftar
4. Isi First Name "Dimas", Last Name "Kurniawan", Email unik, dan Division yang sudah ada
5. Pilih Access "Admin Console" saja
6. Klik `[Submit]`
7. Verifikasi toast sukses "User created successfully." muncul
8. Verifikasi baris user baru muncul di User List
9. Verifikasi kolom Access menampilkan tepat 1 badge dark dengan teks "Admin Console"
10. Verifikasi role user baru adalah User Basic

## Notes

- Pasangan `TC-GS-USER-E2E-003` (Principal). Aturan sama untuk Principal, Distributor, dan Partner (`user.md` §9.2).
- User dihapus saat pembersihan.
