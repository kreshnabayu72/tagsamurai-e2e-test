---
id: TC-GS-USER-E2E-065-custom-field-inline-edit-guard-aktor
title: 'Inline-edit Custom Field tidak tersedia untuk aktor Read Only dan capability holder pada target Total Control'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-500
  - TC-GS-USER-501
coverage:
  web: automated
---

# Inline-edit Custom Field tidak tersedia untuk aktor Read Only dan capability holder pada target Total Control

## Prerequisites

- Sesi aktor Read Only (login sebagai Role: Read Only)
- Sesi aktor capability holder: role "Manage user and role" Full CRUD, bukan Total Control
- User "Budi Santoso" dengan Custom Field `Blood Type` aktif dan value existing
- User "Siti Rahmawati" berstatus Total Control, dengan Custom Field `Blood Type` aktif dan value existing
- Spec ini tidak mengubah data

## Test Steps

### Aktor Read Only

1. Di sesi Read Only, buka User Detail "Budi Santoso" lalu expand Section Custom Fields
2. Hover baris `Blood Type` lalu klik area value
3. Verifikasi value tetap tampil (Display), ikon `Edit2Line` tidak muncul saat hover, dan tidak ada jalur ke widget input

### Aktor capability holder

4. Di sesi capability holder, buka User Detail "Siti Rahmawati" lalu expand Section Custom Fields
5. Hover baris `Blood Type`
6. Verifikasi ikon `Edit2Line` Disabled dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
7. Klik area value
8. Verifikasi value tetap Display dan tidak bisa masuk state Active

## Notes

- Sisi positif (aktor Total Control) dicakup `TC-GS-USER-E2E-064-custom-field-inline-edit`. Spec ini sisi negatif matriks role.
- Sumber `user.md` bagian 9.3, 2.5, dan 4.3. Endpoint tulis Custom Field digate role yang sama seperti aksi lain, sehingga percobaan API langsung dicakup lapisan BE.
