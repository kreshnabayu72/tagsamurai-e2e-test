---
id: TC-AUTH-MFA-E2E-054-security-no-optimistic-success
title: Frontend tidak mengasumsikan status login sukses tanpa konfirmasi server resmi
priority: High
caseType: Security
status: draft
sourceTc:
  - TC-AUTH-MFA-98
coverage:
  web: automated
---

# Frontend tidak mengasumsikan status login sukses tanpa konfirmasi server resmi

## Prerequisites

- Mode: mock
- Mode: mock (tahan response server verifikasi MFA dalam keadaan pending/ambigu)

## Test Steps

1. Masukkan kode verifikasi pada halaman faktor kedua dan submit
2. Tahan respons server (status pending)
3. Amati antarmuka pengguna
4. Verifikasi antarmuka tetap menampilkan state loading dan TIDAK melakukan pengalihan atau menganggap sukses secara optimistik sebelum respons definitif diterima

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-54`
- Merepresentasikan `TC-AUTH-MFA-98` (FE Ref: `TC-AUTH-MFA-FE-54`).
