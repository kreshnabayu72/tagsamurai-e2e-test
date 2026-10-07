---
id: TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user
title: "Pemblokiran Hapus Divisi In-Use (D-02): Referensi Login User Aktif, Non-Aktif, Non-Login User, dan Dismiss Tombol Tunggal OK"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-117
  - TC-GS-DIV-118
  - TC-GS-DIV-119
  - TC-GS-DIV-120
coverage:
  web: automated
---

# Pemblokiran Hapus Divisi In-Use (D-02): Referensi Login User Aktif, Non-Aktif, Non-Login User, dan Dismiss Tombol Tunggal OK

## Prerequisites

- Login sebagai Role: Total Control
- Human Resources (in-use User aktif), Operations (in-use User non-aktif), Compliance (in-use Non-Login User)
- User berada di Global Settings > User > Division
- Division `Human Resources` dipakai oleh Login User aktif Budi Santoso
- Division `Operations` dipakai oleh Login User non-aktif Siti Rahmawati
- Division `Compliance` dipakai oleh Non-Login User Andi Pratama

## Test Steps

### Delete Division yang dipakai Login User aktif diblokir (TC-GS-DIV-117)

1. Buka row action baris `Human Resources` lalu klik `Delete`
2. Verifikasi Dialog konfirmasi hapus tidak tampil; langsung muncul Dialog `Cannot Delete Data` (severity warning)
3. Verifikasi Body: bullet `Human Resources — still in use`, lalu `This division is still in use. Remove the references before deleting.`
4. Verifikasi Satu tombol `[OK]` (Single Dismiss Rule)
5. Verifikasi Tidak ada toast

### Delete Division yang dipakai Login User non-aktif diblokir (TC-GS-DIV-118)

6. Buka row action baris `Operations` lalu klik `Delete`
7. Verifikasi Dialog konfirmasi hapus tidak tampil; langsung muncul Dialog `Cannot Delete Data` (severity warning)
8. Verifikasi Body: bullet `Operations — still in use`, lalu `This division is still in use. Remove the references before deleting.`
9. Verifikasi Satu tombol `[OK]` (Single Dismiss Rule)
10. Verifikasi Tidak ada toast

### Delete Division yang dipakai Non-Login User diblokir (TC-GS-DIV-119)

11. Buka row action baris `Compliance` lalu klik `Delete`
12. Verifikasi Dialog konfirmasi hapus tidak tampil; langsung muncul Dialog `Cannot Delete Data` (severity warning)
13. Verifikasi Body: bullet `Compliance — still in use`, lalu `This division is still in use. Remove the references before deleting.`
14. Verifikasi Satu tombol `[OK]` (Single Dismiss Rule)
15. Verifikasi Tidak ada toast

### OK pada dialog blokir menutup dialog tanpa menghapus (TC-GS-DIV-120)

16. Buka row action baris `Human Resources` lalu klik `Delete`
17. Klik `[OK]`
18. Verifikasi Dialog `Cannot Delete Data` tertutup
19. Verifikasi Baris `Human Resources` tetap ada

## Notes

- Memvalidasi DIV-LOGIC-02: Dialog 2 (D-02: title "Cannot Delete Data", bullet "[Name] — still in use", Single Dismiss Rule tombol [OK]) memblokir penghapusan seluruh jenis referensi user (PRD §4.2d, §6 V-09, §10).
- Sumber pemetaan test case granular: TC-GS-DIV-117, TC-GS-DIV-118, TC-GS-DIV-119, TC-GS-DIV-120.
