---
id: TC-AC-SU-E2E-024-bulk-resend-activation-mail-partial-skip-dan-batch-delivery
title: "Bulk Resend Activation Email: Partial Skip Non-Pending dan Partial Skip Cooldown"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-46
  - TC-AC-SU-258
  - TC-AC-SU-289
coverage:
  web: automated
---

# Bulk Resend Activation Email: Partial Skip Non-Pending dan Partial Skip Cooldown

## Prerequisites

- Login sebagai Total Control
- Terdapat variasi user: User A (Not Activated, ready), User B (Not Activated, cooldown aktif), User C (Active)

## Test Steps

### Seleksi Baris Campuran
1. Buka `Admin Console > Settings > User`
2. Centang checkbox pada baris User A, User B, dan User C
3. Verifikasi Bulk Action Bar menampilkan tombol `[Resend Activation Email]`

### Verifikasi Dialog Ringkasan dan Eksekusi
4. Klik tombol `[Resend Activation Email]` pada Bulk Action Bar
5. Verifikasi dialog ringkasan menampilkan informasi:
   - 1 user siap dikirim (User A)
   - 1 user dilewati karena masih dalam masa cooldown (User B)
   - 1 user dilewati karena sudah aktif (User C)
6. Klik tombol konfirmasi `[Send]`
7. Verifikasi toast sukses muncul: `"Activation email sent to 1 user. 2 users were skipped."`
8. Verifikasi cooldown timer kini aktif pada User A

## Notes

Memastikan efisiensi pemrosesan batch email aktivasi tanpa melanggar status cooldown.
