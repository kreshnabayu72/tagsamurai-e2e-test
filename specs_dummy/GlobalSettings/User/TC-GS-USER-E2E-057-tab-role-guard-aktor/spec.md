---
id: TC-GS-USER-E2E-057-tab-role-guard-aktor
title: 'Tab Role tidak bisa diedit oleh aktor Read Only atau capability holder pada target Total Control'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-498
  - TC-GS-USER-499
coverage:
  web: automated
---

# Tab Role tidak bisa diedit oleh aktor Read Only atau capability holder pada target Total Control

## Prerequisites

- Sesi aktor Read Only (login sebagai Role: Read Only)
- Sesi aktor capability holder: role "Manage user and role" Full CRUD, bukan Total Control
- User "Siti Rahmawati" berstatus Total Control di Global Settings
- Spec ini tidak mengubah data

## Test Steps

### Aktor Read Only

1. Di sesi Read Only, buka User Detail "Siti Rahmawati" > Tab Role
2. Verifikasi banner "This user has Total Control access." tetap tampil, tabel 6 role tampil, dan kolom Active serta CRUD Disabled
3. Klik salah satu checkbox
4. Verifikasi tidak ada perubahan tersimpan dan tidak ada toast, sedangkan ikon Changelog di toolbar tetap tampil

### Aktor capability holder

5. Di sesi capability holder, buka User Detail "Siti Rahmawati" > Tab Role
6. Verifikasi kolom Active dan CRUD Disabled, lalu hover salah satu checkbox dan verifikasi tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
7. Klik salah satu checkbox
8. Verifikasi tidak ada perubahan tersimpan dan tidak ada toast

## Notes

- Positif untuk aktor Total Control ada di `TC-GS-USER-E2E-054-tab-role-edit-inline-sinkron` dan `055`. Spec ini adalah sisi negatif matriks role.
- Sumber `user.md` bagian 9.3 dan 2.5. Tooltip sama dengan aksi lain pada target Total Control (`TC-GS-USER-84`).
- Cara menjalankan dua sesi dengan role berbeda ditentukan tim FE di tahap script.
