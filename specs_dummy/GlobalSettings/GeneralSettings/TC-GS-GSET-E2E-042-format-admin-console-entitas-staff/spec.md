---
id: TC-GS-GSET-E2E-042-format-admin-console-entitas-staff
title: Format Admin Console mengikuti entitas staff login
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-139
coverage:
  web: automated
---

# Format Admin Console mengikuti entitas staff login

## Prerequisites

- Dua admin (admin A dan admin B) dengan entitas staff/tenant berbeda disiapkan via
  `Fixture.globalSettingsGeneralSettings.actors.adminA` dan `adminB`.
- `Fixture.admin.fmt` menampung `dateFormat`/`timeFormat` dari tiap entitas.
- Environment mode single-tenant digunakan; snapshoot per tenant di sisi negatif tidak diuji untuk
  spec ini (lihat spec 008).

## Test Steps

1. Login sebagai admin A
2. Buka `Global Settings > General Settings`
3. Verifikasi field `Date Format` saat ini menampilkan format yang sesuai entitas A jika ada
   (mengikuti `adminA`), bukan format default yang hard-coded
4. Verifikasi field `Time Format` mengikuti entitas A
5. Logout, login sebagai admin B
6. Buka halaman yang sama
7. Verifikasi `Date Format` dan `Time Format` menampilkan format entitas B (jika berbeda dengan A;
   verifikasi berubah sesuai entitas yang sedang login)
8. Verifikasi pada kedua entitas nilai form dapat diedit & disimpan sesuai format entitasnya

## Notes

- Deviasi multi-tenant diuji terpisah (spec 051 pada suite User). PMC `ADMIN-FORMAT-CONTRACT`
  terpenuhi: pilihan format yang ditampilkan mengikuti entitas staff yang login, bukan nilai statis
  global.