---
id: TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download
title: "Pengujian Modal Changelog Detail Role: Filter Dinamis Field Sesuai Hak Akses, Sorting 7 Kolom, dan Download"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-81
  - TC-GS-ROLE-221
  - TC-GS-ROLE-222
  - TC-GS-ROLE-223
  - TC-GS-ROLE-224
  - TC-GS-ROLE-225
  - TC-GS-ROLE-228
  - TC-GS-ROLE-244
  - TC-GS-ROLE-245
  - TC-GS-ROLE-246
  - TC-GS-ROLE-247
  - TC-GS-ROLE-248
  - TC-GS-ROLE-249
  - TC-GS-ROLE-344
  - TC-GS-ROLE-352
coverage:
  web: automated
---

# Pengujian Modal Changelog Detail Role: Filter Dinamis Field Sesuai Hak Akses, Sorting 7 Kolom, dan Download

## Prerequisites

- Login sebagai Role: Total Control
- Buka halaman Detail role 'Manage TAG'

## Test Steps

1. Buka Tab System > Detail role 'Manage TAG'
2. Klik icon Changelog (⏱) pada toolbar halaman Detail
3. Verifikasi modal Changelog terbuka dengan judul dinamis: "Changelog: Role & Permission > Manage TAG"
4. Buka Filter Panel modal Changelog
5. Verifikasi filter 'Field' secara dinamis hanya menampilkan opsi kolom CRUD yang berlaku pada role ini (Read, Update)
6. Terapkan filter Field 'Update' dan verifikasi hasil log yang difilter
7. Uji sorting 3-state untuk 7 kolom: Date, Action, Role — User, Field, Old Value, New Value, Modified By
8. Klik tombol Download pada toolbar modal Changelog
9. Verifikasi file bernama Changelog-Role-Permission-Manage-TAG.csv berhasil diunduh

## Notes

- Modal Changelog halaman Detail menampilkan riwayat mutasi spesifik role tersebut dengan opsi filter Field yang dinamis (role.md §8.4).
