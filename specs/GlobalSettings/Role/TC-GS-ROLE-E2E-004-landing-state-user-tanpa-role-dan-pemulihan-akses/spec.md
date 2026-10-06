---
id: TC-GS-ROLE-E2E-004-landing-state-user-tanpa-role-dan-pemulihan-akses
title: "Landing State Kosong User Tanpa Role dan Pemulihan Otomatis Saat Akses Di-assign"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-08
  - TC-GS-ROLE-09
coverage:
  web: automated
---

# Landing State Kosong User Tanpa Role dan Pemulihan Otomatis Saat Akses Di-assign

## Prerequisites

- Tersedia akun user noRoleUser dengan akses global_settings=true tetapi belum di-assign role apa pun (access_level null dan 0 role)
- Tersedia sesi admin Total Control

## Test Steps

1. Login sebagai akun noRoleUser dan navigasi ke modul Global Settings
2. Verifikasi sidebar tidak menampilkan menu modul Global Settings apa pun (0 menu)
3. Verifikasi area konten utama menampilkan ilustrasi kosong dengan Title: "You don't have access to any menu yet." dan Description: "Contact your administrator to get access."
4. Verifikasi bahwa halaman ini bukan halaman error "Unable to load this data." dan sistem tidak me-redirect ke Portal
5. Pada sesi admin Total Control, buka Global Settings > Role & Permission > Tab System
6. Buka Detail role 'Manage TAG', klik [+ Assign], dan assign noRoleUser ke role tersebut dengan hak akses Read
7. Kembali ke sesi browser noRoleUser dan lakukan refresh halaman (F5)
8. Verifikasi landing state kosong hilang dan menu 'Manage TAG' muncul di sidebar Global Settings dengan hak akses Read-only

## Notes

- Landing state kosong adalah perilaku resmi bagi user yang memiliki lisensi modul tetapi belum di-assign capability (role.md §10.1).
