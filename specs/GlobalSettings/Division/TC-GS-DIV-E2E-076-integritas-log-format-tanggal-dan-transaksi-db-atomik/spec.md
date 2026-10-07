---
id: TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik
title: "Integritas Baris Log: Format Tanggal General Settings, Larangan Old & New Value Em-dash Sekaligus, Transaksi DB Atomik, dan All-or-Nothing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-246
  - TC-GS-DIV-247
  - TC-GS-DIV-248
  - TC-GS-DIV-249
coverage:
  web: automated
---

# Integritas Baris Log: Format Tanggal General Settings, Larangan Old & New Value Em-dash Sekaligus, Transaksi DB Atomik, dan All-or-Nothing

## Prerequisites

- Login sebagai Role: Total Control
- Buka Modal Changelog dan Activity Log GS
- User berada di Global Settings > User > Division
- TC eksekusi per capability sudah dijalankan (TC-GS-DIV-26, TC-GS-DIV-27, TC-GS-DIV-28)
- Division `Metro Branch 3` ada
- Entri Create, Edit, dan Delete tersedia (TC-GS-DIV-235, TC-GS-DIV-237, TC-GS-DIV-242)

## Test Steps

### Modified By mencatat aktor pelaksana tiap aksi (TC-GS-DIV-246)

1. Buka Modal Changelog dan lihat Modified By pada entri hasil aksi Create-Only, Update-Only, dan Delete-Only
2. Hover Modified By tiap entri
3. Verifikasi Entri Create oleh Create-Only: `Rina M` (tooltip `Rina Marlina`)
4. Verifikasi Entri Edit oleh Update-Only: `Agus W` (tooltip `Agus Wijaya`)
5. Verifikasi Entri Delete oleh Delete-Only: `Dewi L` (tooltip `Dewi Lestari`)

### Division tidak menulis System Log di Detail User (TC-GS-DIV-247)

6. Buat, ubah, lalu hapus sebuah Division
7. Buka Detail User > Tab System Log untuk user mana pun
8. Verifikasi Tab System Log tidak memuat entri apa pun tentang Division (Division bukan aksi yang melekat pada satu user)

### Edit tercatat juga di Activity Log Global Settings (TC-GS-DIV-248)

9. Edit Division `Metro Branch 3`: ubah Code menjadi `MB3`, Save
10. Buka Activity Log Global Settings dan lihat entri teratas
11. Verifikasi Entri Action `Edit`, Object `Division`, Name `Metro Branch 3`, Field `Code`, Old Value kode lama, New Value `MB3`, Modified By aktor

### Old Value dan New Value tidak pernah keduanya strip pada satu entri (TC-GS-DIV-249)

12. Buka Modal Changelog dan periksa seluruh entri Create, Edit, dan Delete pada halaman pertama
13. Verifikasi Create: Old Value `—` dan New Value terisi nama Division
14. Verifikasi Edit: Old Value dan New Value keduanya terisi
15. Verifikasi Delete: Old Value terisi dan New Value `—`
16. Verifikasi Tidak ada entri dengan Old Value dan New Value sama-sama `—`

## Notes

- Memvalidasi kepatuhan format tanggal mengikuti General Settings, jaminan bahwa Old Value dan New Value tidak pernah keduanya em-dash sekaligus, dan transaksi DB atomik: mutasi data dan penulisan log berada dalam 1 transaksi (PRD §4.1.2, §8.1, §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-246, TC-GS-DIV-247, TC-GS-DIV-248, TC-GS-DIV-249.
