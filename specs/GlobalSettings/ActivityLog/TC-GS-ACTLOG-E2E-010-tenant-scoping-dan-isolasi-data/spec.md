---
id: TC-GS-ACTLOG-E2E-010-tenant-scoping-dan-isolasi-data
title: "Isolasi data log per tenant tanpa kebocoran data atau opsi agregasi lintas entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-30
coverage:
  web: automated
---

# Isolasi data log per tenant tanpa kebocoran data atau opsi agregasi lintas entitas

## Prerequisites

- Akun Total Control Client A
- Terdapat riwayat log milik Client A dan riwayat log milik Client B di database

## Test Steps

1. Login sebagai Total Control Client A
2. Buka Tab Session di menu Activity Log
3. Verifikasi seluruh baris log yang tampil hanya berasal dari pengguna terdaftar di Client A
4. Verifikasi tidak ada entri log milik Client B yang muncul di tabel
5. Klik tab "User Action"
6. Verifikasi seluruh baris changelog yang tampil hanya berasal dari aksi mutasi di Client A
7. Verifikasi tidak ada opsi dropdown atau tombol untuk memilih atau menggabungkan data lintas entitas

## Notes

- Prinsip isolasi tenant menjamin data audit trail suatu perusahaan tidak pernah terekspos ke entitas lain.
