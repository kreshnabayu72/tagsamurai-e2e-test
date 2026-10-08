---
id: TC-AC-SU-E2E-030-tab-role-global-role-permission-guards-dan-modal-changelog
title: "Guard Hak Akses Global Role (Default User, Self-Edit, Tier Lock) dan Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-69
  - TC-AC-SU-71
  - TC-AC-SU-72
  - TC-AC-SU-73
  - TC-AC-SU-161
coverage:
  web: automated
---

# Guard Hak Akses Global Role (Default User, Self-Edit, Tier Lock) dan Modal Changelog

## Prerequisites

- Login sebagai Total Control
- Terdapat akun Default User, akun Self, dan akun dengan tier Total Control / Read Only

## Test Steps

### Guard Default User dan Self-Edit pada Global Role
1. Buka Detail User untuk `Default User` > tab `Role` > sub-tab `Global Role`
2. Verifikasi seluruh toggle switch dan checkbox CRUD berstatus disabled permanen dengan tooltip: `"Default user permissions cannot be modified"`
3. Buka Detail User untuk akun profil sendiri (`Self`)
4. Verifikasi seluruh toggle switch dan checkbox CRUD berstatus disabled dengan tooltip: `"You cannot modify your own permissions"`

### Guard Akun Tier dan Modal Changelog
5. Buka Detail User untuk akun berstatus tier `Total Control` atau `Read Only`
6. Verifikasi kontrol mutasi role terkunci dengan banner tier aktif
7. Klik tombol `[Changelog]` pada toolbar sub-tab Global Role
8. Verifikasi modal `Changelog Global Role` terbuka, menampilkan riwayat perubahan role, aktor pengubah, tanggal mutasi, dan rincian sebelum/sesudah mutasi

## Notes

Menjaga integritas hak akses akun-akun terproteksi dari modifikasi ilegal.
