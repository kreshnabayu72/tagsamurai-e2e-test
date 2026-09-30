---
id: TC-GS-USER-E2E-038-reset-authenticator-belum-enrolled
title: Reset Authenticator tidak tersedia untuk user yang belum enrolled
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-70
coverage:
  web: automated
---

# Reset Authenticator tidak tersedia untuk user yang belum enrolled

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Tari Baru" belum pernah menyiapkan Authenticator (tidak ada MFA yang terdaftar)
- Spec ini tidak mengubah data, jadi tidak butuh cleanup

## Test Steps

1. Buka User Detail "Tari Baru"
2. Verifikasi section Authenticator menampilkan teks muted "Not enrolled yet"
3. Verifikasi tombol `Reset Authenticator` tidak dirender sama sekali (Hidden, bukan Disabled)

## Notes

- Spec ini dipisah dari `TC-GS-USER-E2E-037-reset-authenticator` karena butuh user tanpa MFA, sedangkan alur reset butuh user yang sudah enrolled (prinsip 12 di `docs/e2e-conventions.md` bagian 3).
- Perilaku "Not enrolled yet" tanpa tombol mengikuti PRD `user.md` bagian 4.2 (Authenticator).
