---
id: TC-GS-USER-E2E-111-changelog-modal-sort
title: 'Modal Changelog User List: sort tiga keadaan per kolom'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-242
  - TC-GS-USER-243
  - TC-GS-USER-244
  - TC-GS-USER-245
  - TC-GS-USER-246
coverage:
  web: automated
---

# Modal Changelog User List: sort tiga keadaan per kolom

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Riwayat Changelog banyak dengan Action, nama, dan aktor beragam, termasuk baris Create dan Delete dengan Field kosong
- Spec ini tidak mengubah data

## Test Steps

1. Buka modal Changelog User List dan verifikasi urutan default Date terbaru dulu
2. Klik header `Date` satu, dua, dan tiga kali
3. Verifikasi klik pertama naik (terlama dulu), kedua turun, dan ketiga kembali ke default terbaru dulu
4. Ulangi klik tiga kali pada header `Action`, `Name`, `Field`, dan `Modified By`
5. Verifikasi `Action` dan `Name` urut alfabetis naik lalu turun lalu default
6. Verifikasi pada `Field` naik, baris dengan Field kosong selalu berada di akhir
7. Verifikasi `Modified By` mengikuti nama lengkap aktor

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.7.
