---
id: TC-AC-SU-E2E-028-detail-user-tab-role-group-role-guards-detail-popup-dan-modal-changelog
title: "Guard Sub-tab Group Role (Default User, Self-edit), popup Detail Group Assignment read-only, dan modal Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-84
  - TC-AC-SU-162
  - TC-AC-SU-221
  - TC-AC-SU-261
coverage:
  web: automated
---

# Guard Sub-tab Group Role (Default User, Self-edit), popup Detail Group Assignment read-only, dan modal Changelog

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target Default User, Self User, dan Group Role dengan penugasan multi-group

## Test Steps

### Verifikasi Guard Group Role pada Default User dan Self

1. Buka Tab Role Sub-tab Group Role untuk Default User: verifikasi seluruh 6 switch ON & Disabled, tombol `Detail` tampil, dan tombol `Assign Group` disembunyikan (hidden)
2. Buka Tab Role Sub-tab Group Role untuk akun sendiri (Self): coba klik switch role, verifikasi Disabled dengan tooltip `"You cannot edit your own roles."` dan tombol `Assign Group` hidden

### Popup Detail Group Assignment (Read-Only)

1. Buka Tab Role Sub-tab Group Role target pengguna yang ter-assign ke ≥2 group dengan matriks CRUD berbeda
2. Klik tombol `[Detail]` pada baris Group Role tersebut
3. Verifikasi popup `"Group Assignment"` terbuka menampilkan seluruh group ter-assign beserta matriks C/R/U/D
4. Verifikasi seluruh checkbox CRUD berstatus Disabled (read-only)
5. Verifikasi popup TIDAK memiliki tombol footer (Save / Cancel), dan satu-satunya cara menutup popup adalah icon `[✕]` di header

### Modal Changelog Group Role

1. Klik icon `[📋 Changelog]` pada toolbar Sub-tab Group Role
2. Verifikasi modal `"Changelog: User > Group Role"` terbuka dengan kolom format `Role Name — Group Name`

## Notes

- Popup detail group assignment memberikan visibilitas penuh terhadap hak akses per group.
