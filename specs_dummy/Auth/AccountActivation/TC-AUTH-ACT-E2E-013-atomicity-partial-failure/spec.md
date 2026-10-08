---
id: TC-AUTH-ACT-E2E-013-atomicity-partial-failure
title: Atomicity - rollback penuh saat partial failure
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-46
coverage:
  web: automated
---

# Atomicity - rollback penuh saat partial failure

## Prerequisites

- Token valid `active` tersedia.
- Dibutuhkan simulasi partial failure di tengah transaksi (fault injection) sesuai kemampuan test environment. Jika tidak dapat disimulasikan sepenuhnya secara otomatis, kebutuhan teknis dan batasan verifikasi dicatat.

## Test Steps

1. Siapkan skenario partial failure sesuai kemampuan test environment.
2. Lakukan submit dengan password valid dalam kondisi partial-failure tersebut.
3. Verifikasi rollback penuh terjadi (bukan kombinasi campuran): password **tidak** tersimpan, token tetap `active`, user tetap `Pending Activation`. Tidak ada kredensial baru tersimpan.

## Notes

- TC-AUTH-ACT-46 bersifat kompleks; bisa manual-only setup. Spec tetap dibuat sesuai konvensi.
