---
id: TC-GS-ROLE-E2E-016-assign-dan-remove-read-only-server-failure-resilience
title: "Ketahanan Alur Assign dan Remove Read Only Terhadap Kegagalan Server 5xx Serta Notifikasi In-App"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-114
coverage:
  web: automated
---

# Ketahanan Alur Assign dan Remove Read Only Terhadap Kegagalan Server 5xx Serta Notifikasi In-App

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Intersept endpoint access-level POST dan DELETE disiapkan untuk mengembalikan status 500
- Target user login di sesi browser terpisah

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Read Only
2. Klik tombol [+ Assign], pilih target user pada picker, lalu klik [Assign]
3. Simulasikan backend mengembalikan respon HTTP 500 saat submit penugasan Read Only
4. Verifikasi toast error muncul: "Error, failed to assign Read Only."
5. Verifikasi target user tidak ditambahkan ke tabel Tab Read Only
6. Tutup popup picker
7. Klik row action [⋯] pada salah satu user Read Only lalu pilih 'Remove'
8. Pada dialog konfirmasi, klik tombol [Remove]
9. Simulasikan backend mengembalikan respon HTTP 500 saat konfirmasi pencabutan Read Only
10. Verifikasi toast error muncul: "Error, failed to remove Read Only."
11. Verifikasi user target tetap berada di tabel Tab Read Only tanpa perubahan
12. Simulasikan pencabutan Read Only berhasil dan periksa sesi browser target user
13. Verifikasi target user menerima notifikasi in-app pencabutan hak akses Read Only

## Notes

- Resilience kegagalan server memastikan rollback mutasi data dan notifikasi dikirimkan hanya saat aksi sukses (role.md §8.8, §9.6).
