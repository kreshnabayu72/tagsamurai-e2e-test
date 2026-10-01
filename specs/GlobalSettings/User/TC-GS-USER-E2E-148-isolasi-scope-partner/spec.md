---
id: TC-GS-USER-E2E-148-isolasi-scope-partner
title: User List Partner hanya menampilkan staff Partner sendiri
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-607
coverage:
  web: automated
---

# User List Partner hanya menampilkan staff Partner sendiri

## Prerequisites

- Login sebagai Total Control pada entity Partner
- Partner punya staff sendiri "Staff Partner Sendiri"
- Distributor induk punya staff "Staff Distributor Induk", dan Partner lain sejaringan punya staff "Staff Partner Lain"
- Nama akun dan entity disiapkan tim FE
- Spec ini hanya membaca data, jadi tidak butuh cleanup

## Test Steps

1. Buka User List
2. Verifikasi User List menampilkan "Staff Partner Sendiri"
3. Cari "Staff Distributor Induk" lewat kotak Search dan verifikasi hasil kosong
4. Cari "Staff Partner Lain" lewat kotak Search dan verifikasi hasil kosong

## Notes

- Pasangan `TC-GS-USER-E2E-051` bagian Distributor. Murni per entity tanpa agregasi (`user.md` §2.1).
- Entity-scope Principal terhadap Distributor downstream tidak dicakup karena PRD belum menyebutnya (`GAP-300`).
