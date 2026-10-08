---
id: TC-AUTH-ACT-E2E-019-non-logging-internal-actions
title: Non-logging murni untuk aksi internal fitur Activation (4 surface)
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-67
  - TC-AUTH-ACT-68
  - TC-AUTH-ACT-69
  - TC-AUTH-ACT-70
coverage:
  web: automated
---

# Non-logging murni untuk aksi internal fitur Activation (4 surface)

## Prerequisites

- User dengan berbagai state (Pending Activation, token states) tersedia.
- Akses admin untuk membuka dan memverifikasi keempat surface log: Activity Log > Session, User Log, System Log, dan Changelog.
- Memungkinkan perbandingan jumlah entri log secara akurat (count-based comparison).

## Test Steps

### A. Buka link (valid maupun invalid) tidak dicatat

1. Catat jumlah entri pada keempat surface log sebagai baseline.
2. Buka `/activate?token={validToken}` (link valid) beberapa kali.
3. Buka `/activate?token={invalidToken}` (berbagai kondisi invalid) beberapa kali.
4. Catat ulang jumlah entri pada keempat surface log.
5. Verifikasi tidak ada entri baru pada keempat surface log (jumlah entri tetap sama).

### B. Set Password sukses/gagal tidak dicatat

6. Siapkan token valid baru. Catat baseline jumlah entri keempat surface log.
7. Lakukan submit password valid (sukses).
8. Catat ulang jumlah entri keempat surface log. Verifikasi tidak ada entri baru.
9. Siapkan token valid baru. Catat baseline jumlah entri keempat surface log.
10. Lakukan submit password dengan mismatch/invalid (gagal).
11. Catat ulang jumlah entri keempat surface log. Verifikasi tidak ada entri baru.

### C. Token consumed/superseded tidak dicatat

12. Catat baseline jumlah entri keempat surface log.
13. Picu skenario consume token (aktivasi sukses) dan skenario supersede token (resend).
14. Catat ulang jumlah entri keempat surface log.
15. Verifikasi tidak ada entri baru di keempat surface log terkait event consumed/superseded dari sisi fitur Activation.

### D. Tampil halaman 404 aktivasi tidak dicatat

16. Catat baseline jumlah entri keempat surface log.
17. Buka berbagai link yang menghasilkan halaman 404 aktivasi (expired/consumed/superseded/malformed/user-deleted).
18. Catat ulang jumlah entri keempat surface log.
19. Verifikasi tidak ada entri baru di keempat surface log terkait tampilnya halaman 404 aktivasi.

## Notes

- Verifikasi menggunakan count-based comparison pada keempat surface log.
