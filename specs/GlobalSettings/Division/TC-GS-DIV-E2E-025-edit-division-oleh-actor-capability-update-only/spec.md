---
id: TC-GS-DIV-E2E-025-edit-division-oleh-actor-capability-update-only
title: "Penyuntingan Divisi Sukses oleh Pengguna Ber-capability Update-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-40
coverage:
  web: automated
---

# Penyuntingan Divisi Sukses oleh Pengguna Ber-capability Update-Only

## Prerequisites

- Login sebagai pengguna dengan peran Manage User Role berizin Update-Only (tanpa Create atau Delete)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi tombol '[+ Division]' tersembunyi
3. Klik menu row action (⋯) pada salah satu divisi dan verifikasi hanya opsi 'Edit' yang tersedia
4. Klik 'Edit' lalu ubah nama divisi
5. Klik tombol '[Save]'
6. Verifikasi toast 'Success, division has been updated.' muncul
7. Verifikasi perubahan nama divisi berhasil tersimpan di tabel

## Notes

- Menguji hak eksekusi write capability U (Update) sesuai division.md §2.
