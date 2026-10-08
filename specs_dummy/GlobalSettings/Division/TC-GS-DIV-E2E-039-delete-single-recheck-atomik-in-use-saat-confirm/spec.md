---
id: TC-GS-DIV-E2E-039-delete-single-recheck-atomik-in-use-saat-confirm
title: "Re-Cek Atomik Saat Confirm Delete Single: Divisi Berubah Status Menjadi In-Use Sebelum Confirm Memunculkan Dialog Blokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-121
coverage:
  web: automated
---

# Re-Cek Atomik Saat Confirm Delete Single: Divisi Berubah Status Menjadi In-Use Sebelum Confirm Memunculkan Dialog Blokir

## Prerequisites

- Login sebagai Role: Total Control
- Divisi bebas relasi dibuka dialog hapusnya oleh Admin A, lalu Admin B mengaitkan user ke divisi tersebut sebelum Confirm
- User berada di Global Settings > User > Division
- Division `Security` (Code `SEC`) bebas relasi (TC-GS-DIV-30)

## Test Steps

1. Admin A membuka row action baris `Security` lalu klik `Delete` hingga dialog konfirmasi tampil
2. Admin B menugaskan Division `Security` ke sebuah user
3. Admin A klik `[Delete]`
4. Verifikasi Dialog `Cannot Delete Data` tampil dengan bullet `Security — still in use` dan `[OK]`
5. Verifikasi Division `Security` tidak terhapus
6. Verifikasi Tidak ada toast sukses

## Notes

- Memvalidasi DIV-LOGIC-02c: re-cek server-side saat tombol Confirm diklik menggagalkan penghapusan dan beralih ke Dialog 2 (PRD §4.2d, §9.2 [F-DIV-04], §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-121.
