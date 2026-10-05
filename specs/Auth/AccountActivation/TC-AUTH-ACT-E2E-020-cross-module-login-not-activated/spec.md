---
id: TC-AUTH-ACT-E2E-020-cross-module-login-not-activated
title: Cross-module - login gagal oleh user belum aktivasi dicatat oleh modul Login
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-71
coverage:
  web: automated
---

# Cross-module - login gagal oleh user belum aktivasi dicatat oleh modul Login

## Prerequisites

- User dengan status `Pending Activation` (belum melakukan aktivasi) tersedia.
- Akses untuk memverifikasi surface log modul Login (Activity Log > Session dan User Log, sesuai scope modul Login).
- Akses ke halaman Login with Password.

## Test Steps

1. Siapkan user dengan status `Pending Activation`.
2. Catat baseline jumlah entri log pada surface yang relevan untuk modul Login.
3. Coba login dengan kredensial user `Pending Activation` melalui halaman Login with Password.
4. Verifikasi login ditolak.
5. Catat ulang jumlah entri log pada surface modul Login.
6. Verifikasi terdapat entri log baru dari modul Login dengan Note `"Account is not activated"`.
7. Verifikasi entri log tersebut merupakan tanggung jawab modul Login (bukan fitur Activation).

## Notes

- TC-AUTH-ACT-71 adalah cross-module verification (modul Login, bukan Activation).
