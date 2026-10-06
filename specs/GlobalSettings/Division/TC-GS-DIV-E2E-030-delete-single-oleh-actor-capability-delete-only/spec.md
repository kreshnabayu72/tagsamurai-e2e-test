---
id: TC-GS-DIV-E2E-030-delete-single-oleh-actor-capability-delete-only
title: "Penghapusan Divisi Tunggal oleh Pengguna Ber-capability Delete-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-46
coverage:
  web: automated
---

# Penghapusan Divisi Tunggal oleh Pengguna Ber-capability Delete-Only

## Prerequisites

- Login sebagai pengguna dengan peran Manage User Role berizin Delete-Only (tanpa Create atau Update)
- Tersedia divisi aman dinamis yang siap dihapus

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi tombol '[+ Division]' tersembunyi
3. Klik menu row action (⋯) pada divisi aman dan verifikasi hanya opsi 'Delete' yang tersedia
4. Klik 'Delete' lalu konfirmasi pada dialog pemusnahan data
5. Verifikasi toast 'Success, division has been deleted.' muncul
6. Verifikasi baris divisi tersebut berhasil terhapus dari tabel

## Notes

- Menguji hak eksekusi write capability D (Delete) sesuai division.md §2.
