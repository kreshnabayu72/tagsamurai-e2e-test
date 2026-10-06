---
id: TC-GS-ROLE-E2E-013-assign-dan-remove-total-control-server-failure-resilience
title: "Ketahanan Alur Assign dan Remove Total Control Terhadap Kegagalan Server 5xx"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-27
coverage:
  web: automated
---

# Ketahanan Alur Assign dan Remove Total Control Terhadap Kegagalan Server 5xx

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Intersept endpoint access-level POST dan DELETE disiapkan untuk mengembalikan status 500

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik tombol [+ Assign], pilih target user pada picker, lalu klik [Assign]
3. Simulasikan backend mengembalikan respon HTTP 500 saat submit penugasan
4. Verifikasi toast error muncul: "Error, failed to assign Total Control."
5. Verifikasi target user tidak ditambahkan ke tabel Tab Total Control
6. Tutup popup picker
7. Klik row action [⋯] pada salah satu user Total Control lalu pilih 'Remove'
8. Pada dialog konfirmasi, klik tombol [Remove]
9. Simulasikan backend mengembalikan respon HTTP 500 saat konfirmasi pencabutan
10. Verifikasi toast error muncul: "Error, failed to remove Total Control."
11. Verifikasi user target tetap berada di tabel Tab Total Control tanpa perubahan

## Notes

- Resilience kegagalan server memastikan data UI tidak berubah jika transaksi backend gagal (role.md §9.6).
