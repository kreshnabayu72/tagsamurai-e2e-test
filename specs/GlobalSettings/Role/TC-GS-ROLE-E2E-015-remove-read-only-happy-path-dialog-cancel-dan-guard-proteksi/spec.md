---
id: TC-GS-ROLE-E2E-015-remove-read-only-happy-path-dialog-cancel-dan-guard-proteksi
title: "Pencabutan Read Only Sukses, Screening Dialog Konfirmasi, Pembatalan Cancel, dan Guard Self-Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-31
  - TC-GS-ROLE-330
coverage:
  web: automated
---

# Pencabutan Read Only Sukses, Screening Dialog Konfirmasi, Pembatalan Cancel, dan Guard Self-Edit

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia target Budi Hartono ter-assign pada Tab Read Only

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Read Only
2. Klik row action [⋯] pada baris Budi Hartono lalu pilih 'Remove'
3. Verifikasi dialog konfirmasi muncul dengan bullet nama: "• Budi Hartono"
4. Verifikasi deskripsi dialog memuat informasi pencabutan Read Only dan tombol [Cancel] serta [Remove]
5. Klik tombol [Cancel] pada dialog konfirmasi
6. Verifikasi dialog tertutup dan Budi Hartono tetap berada di Tab Read Only
7. Klik kembali row action [⋯] pada Budi Hartono lalu pilih 'Remove'
8. Klik tombol [Remove] pada dialog konfirmasi
9. Verifikasi toast sukses muncul: "Success, Read Only has been removed."
10. Verifikasi Budi Hartono langsung hilang dari tabel Tab Read Only
11. Buka Tab System dan verifikasi seluruh 6 baris role milik Budi Hartono telah terhapus bersih

## Notes

- Pencabutan Read Only menghapus seluruh role sistem dan mengembalikan status user ke tanpa akses GS (role.md §9.2 [F-ROLE-05]).
