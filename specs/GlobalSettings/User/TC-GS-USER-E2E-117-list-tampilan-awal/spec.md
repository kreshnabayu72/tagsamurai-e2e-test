---
id: TC-GS-USER-E2E-117-list-tampilan-awal
title: 'Tampilan awal User List: header, kolom, urutan default, dan Default User selalu ada'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1
  - TC-GS-USER-2
coverage:
  web: automated
---

# Tampilan awal User List: header, kolom, urutan default, dan Default User selalu ada

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Sedikitnya tiga user termasuk Default User (`totalControlGlobalSettings_automated_qaTeam1`) dan user "Doni Pratama"
- Spec ini tidak mengubah data

## Test Steps

1. Buka Global Settings > User
2. Verifikasi breadcrumb "User > User List", tab `User List` (aktif), `Position`, `Division`, `Custom Field`, dan sub-tab `Login User` (aktif) serta `Non-Login User`
3. Verifikasi toolbar berisi Search, Filter, Download, Changelog, dan `[+ User]`
4. Verifikasi kolom tabel: Checkbox, Active, Name (avatar dan nama satu sel), Email, Position, Division, Access, Employee ID, Modified By, Last Update, dan header `(⋯)` untuk Column Visibility
5. Verifikasi footer pagination dengan default 10 baris per halaman
6. Verifikasi urutan default Name A-Z dan Default User selalu ada di daftar tanpa ilustrasi empty state

## Notes

- Sumber `user.md` bagian 4.2, 4.2a, dan 7. Default User membuat keadaan genuinely empty tidak pernah tercapai. Baris Default User dan akun sendiri dicakup `TC-GS-USER-E2E-118-list-baris-default-user-dan-self`.
