---
id: TC-AUTH-ACT-E2E-014-zero-logging-set-password
title: Zero-logging aksi Set Password (sukses dan gagal)
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-47
coverage:
  web: automated
---

# Zero-logging aksi Set Password (sukses dan gagal)

## Prerequisites

- Token valid `active` tersedia.
- Akses admin untuk membuka dan memverifikasi keempat surface log: Activity Log > Session, User Log, System Log, dan Changelog.
- Memungkinkan perbandingan jumlah entri log secara akurat (count-based comparison).

## Test Steps

### A. Zero-logging saat submit sukses

1. Catat jumlah entri pada keempat surface log (Activity Log > Session, User Log, System Log, Changelog) sebagai baseline sebelum submit.
2. Lakukan submit password valid (sukses) pada token valid.
3. Tunggu proses selesai dan catat ulang jumlah entri pada keempat surface log.
4. Verifikasi tidak ada entri baru di keempat surface untuk aksi Set Password (jumlah entri tetap sama dengan baseline).

### B. Zero-logging saat submit gagal

5. Siapkan token valid baru. Catat baseline jumlah entri keempat surface log.
6. Lakukan submit password dengan mismatch/invalid (gagal) pada halaman Set Password.
7. Catat ulang jumlah entri keempat surface log.
8. Verifikasi tidak ada entri baru di keempat surface log untuk aksi Set Password gagal.

## Notes

- Zero-logging diverifikasi pada kedua hasil (sukses dan gagal).
