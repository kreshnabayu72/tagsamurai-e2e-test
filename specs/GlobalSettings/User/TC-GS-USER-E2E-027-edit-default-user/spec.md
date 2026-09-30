---
id: TC-GS-USER-E2E-027-edit-default-user
title: Edit info dasar Default User oleh Total Control dengan Access terkunci
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-29
coverage:
  web: automated
---

# Edit info dasar Default User oleh Total Control dengan Access terkunci

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), bukan Default User
- Default User (`totalControlGlobalSettings_automated_qaTeam1`) ada, dengan Position dan Division awal yang diketahui dan dicatat
- Position "Manager" dan Division "Operations" ada di master data, berbeda dari nilai awal Default User

## Test Steps

1. Klik row action `Edit` pada baris Default User
2. Verifikasi modal Edit terbuka normal, tidak Disabled dan tidak Hidden
3. Ubah Position dan Division menjadi "Manager" dan "Operations"
4. Verifikasi checkbox Access Disabled dengan semua produk entitas tercentang
5. Hover checkbox Access yang Disabled dan verifikasi tooltip "Default User cannot be modified."
6. Klik `[Save]`
7. Verifikasi toast "Success, user has been updated." muncul dan baris Default User menampilkan Position "Manager" dan Division "Operations"
8. Klik `Edit` pada baris Default User lagi, kembalikan Position dan Division ke nilai awal, lalu klik `[Save]`
9. Verifikasi toast "Success, user has been updated." muncul dan baris Default User kembali ke Position dan Division awal

## Notes

- Access Default User bersifat derived: otomatis mencakup seluruh produk entitas termasuk yang ditambahkan kemudian, dan tidak bisa diedit (`GAP-274` sudah ditutup, PRD `USER-LOGIC-02` dan bagian 4.8).
- Percobaan mengubah `access[]` Default User lewat API langsung ditolak `403`, dan itu dicakup lapisan BE, bukan spec ini.
- `access_level` Default User (Total Control) tidak diedit dari sini dan terkunci permanen di modul Role & Permission (`USER-LOGIC-02`).
- Langkah 8 mengembalikan data awal, jadi spec tidak meninggalkan perubahan.
