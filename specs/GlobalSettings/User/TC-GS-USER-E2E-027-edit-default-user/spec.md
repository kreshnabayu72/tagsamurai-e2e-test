---
id: TC-GS-USER-E2E-027-edit-default-user
title: Edit info dasar Default User oleh Total Control
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-29
coverage:
  web: automated
---

# Edit info dasar Default User oleh Total Control

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), bukan Default User
- Default User (`totalControlGlobalSettings_automated_qaTeam1`) ada, dengan Position dan Division awal yang diketahui dan dicatat
- Position "Manager" dan Division "Operations" ada di master data, berbeda dari nilai awal Default User

## Test Steps

1. Klik row action `Edit` pada baris Default User
2. Verifikasi modal Edit terbuka normal, tidak Disabled dan tidak Hidden
3. Ubah Position dan Division menjadi "Manager" dan "Operations"
4. Klik `[Save]`
5. Verifikasi toast "Success, user has been updated." muncul dan baris Default User menampilkan Position "Manager" dan Division "Operations"
6. Klik `Edit` pada baris Default User lagi, kembalikan Position dan Division ke nilai awal, lalu klik `[Save]`
7. Verifikasi toast "Success, user has been updated." muncul dan baris Default User kembali ke Position dan Division awal

## Notes

- Ruang lingkup spec ini sengaja dibatasi ke info dasar sampai `GAP-274` diputuskan. `TC-GS-USER-29` langkah 3 dan 4 (tambah dan hapus produk di Access Default User) tidak ditulis di sini karena perilaku Access Default User berbeda antara PRD/API (menambah boleh, menghapus ditolak `403`) dan konfirmasi UIUX (Access otomatis semua modul dan tidak bisa diedit).
- Setelah `GAP-274` diputuskan, langkah Access ditambahkan. Bila keputusannya checkbox Access disabled, langkahnya berupa `Verifikasi checkbox Access disabled`.
- `access_level` Default User (Total Control) tidak diedit dari sini dan terkunci permanen di modul Role & Permission (`USER-LOGIC-02`).
- Langkah 6 mengembalikan data awal, jadi spec tidak meninggalkan perubahan.
