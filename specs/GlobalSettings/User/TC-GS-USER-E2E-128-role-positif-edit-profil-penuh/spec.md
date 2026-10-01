---
id: TC-GS-USER-E2E-128-role-positif-edit-profil-penuh
title: Role berhak Update berhasil mengedit profil user secara penuh
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-587
coverage:
  web: automated
---

# Role berhak Update berhasil mengedit profil user secara penuh

## Prerequisites

Spec ini memakai satu role. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

| Role | Akun |
|---|---|
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` |

- Entity Client
- Target "Rama Prakoso" adalah User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login), Login User, bukan Temporary, dengan First Name, Last Name, Employee ID, Position, dan Division terisi
- Position "Supervisor" dan Division "Finance" ada di master data dan berbeda dari nilai target
- Minimal satu custom field aktif non-Required ada

## Test Steps

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Buka Modal Edit pada "Rama Prakoso"
3. Ubah First Name menjadi "Rama2" dan Last Name menjadi "Prakoso2"
4. Ubah Employee ID menjadi nilai baru yang belum dipakai, Position menjadi "Supervisor", dan Division menjadi "Finance"
5. Centang `Set as Temporary User` dan isi `Temporary Until` dengan tanggal di masa depan
6. Ubah nilai satu custom field
7. Klik `[Save]`
8. Verifikasi tidak ada dialog tambahan dan toast "Success, user has been updated." muncul
9. Verifikasi baris target menampilkan Name, Employee ID, Position, dan Division baru, kolom `Temporary User` bernilai Yes, dan `Temporary Until` terisi
10. Buka Modal Edit lagi dan verifikasi nilai custom field tersimpan

## Notes

- Ini spec positif Edit profil penuh dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Melengkapi `TC-GS-USER-E2E-011` yang hanya mengubah Position, dan `TC-GS-USER-E2E-024` yang dijalankan Total Control.
- Edit digerbang izin Update (`user.md` §4.8). Ubah Email memiliki alur sendiri di `TC-GS-USER-E2E-129`.
- Target harus dikembalikan ke profil awal atau di-seed ulang setelah run.
