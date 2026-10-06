---
id: TC-GS-DIV-E2E-016-create-division-oleh-actor-capability-create-only
title: "Pembuatan Divisi Baru Sukses oleh Pengguna Ber-capability Create-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-30
coverage:
  web: automated
---

# Pembuatan Divisi Baru Sukses oleh Pengguna Ber-capability Create-Only

## Prerequisites

- Login sebagai pengguna dengan peran Manage User Role berizin Create-Only (tanpa izin Update atau Delete)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi tombol '[+ Division]' tampil dan dapat diklik
3. Klik tombol '[+ Division]'
4. Isi formulir dengan nama divisi unik 'Quality Assurance'
5. Klik tombol '[Submit]'
6. Verifikasi toast notifikasi 'Success, division has been created.' muncul
7. Verifikasi baris 'Quality Assurance' berhasil tersimpan dan tampil pada daftar tabel

## Notes

- Menguji hak akses eksekusi write khusus capability C (Create) sesuai division.md §2.
