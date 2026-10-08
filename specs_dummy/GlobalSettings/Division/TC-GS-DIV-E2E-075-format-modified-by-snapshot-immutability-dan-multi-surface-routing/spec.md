---
id: TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing
title: "Format Modified By, Snapshot Immutability Log Lama Pasca-Rename, Ingestion ke Activity Log GS, dan Absennya System Log User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-242
  - TC-GS-DIV-243
  - TC-GS-DIV-244
  - TC-GS-DIV-245
coverage:
  web: automated
---

# Format Modified By, Snapshot Immutability Log Lama Pasca-Rename, Ingestion ke Activity Log GS, dan Absennya System Log User

## Prerequisites

- Login sebagai Role: Total Control
- Lakukan rename pada divisi yang sudah memiliki riwayat mutasi terdahulu
- User berada di Global Settings > User > Division
- Division `Log Create Renamed` bebas relasi ada
- Division `Business Development` dan `Corporate Communication` bebas relasi (TC-GS-DIV-30)
- Division `Human Resources` in-use; `Information Technology` bebas relasi

## Test Steps

### Delete mencatat satu entri Division Name dengan New Value strip (TC-GS-DIV-242)

1. Hapus Division `Log Create Renamed`
2. Buka Modal Changelog dan Activity Log
3. Verifikasi Changelog: 1 entri Action `Delete`, Division Name `Log Create Renamed`, Field `Division Name`, Old Value `Log Create Renamed`, New Value `—`, Modified By aktor
4. Verifikasi Activity Log: 1 entri Action `Delete`, Object `Division`

### Bulk Delete mencatat satu entri per Division yang berhasil dihapus (TC-GS-DIV-243)

5. Centang `Business Development` dan `Corporate Communication`, Bulk Delete lalu konfirmasi
6. Buka Modal Changelog
7. Verifikasi Tepat 2 entri Delete (satu per Division), masing-masing Old Value nama Division dan New Value `—`
8. Verifikasi Tidak ada entri untuk Division yang di-skip

### Division yang di-skip karena in-use tidak menghasilkan entri log (TC-GS-DIV-244)

9. Centang `Human Resources` dan `Information Technology`, Bulk Delete lalu `[Continue]`
10. Buka Modal Changelog
11. Verifikasi Hanya entri Delete untuk `Information Technology`
12. Verifikasi Tidak ada entri untuk `Human Resources`

### Entri Changelog lama tidak berubah setelah rename berikutnya (TC-GS-DIV-245)

13. Buat Division `Metro Branch` (Code `MTB`)
14. Rename `Metro Branch` menjadi `Metro Branch 2`, lalu rename lagi menjadi `Metro Branch 3`
15. Buka Modal Changelog dan lihat dua entri Edit Name
16. Verifikasi Entri rename pertama tetap Old Value `Metro Branch` dan New Value `Metro Branch 2`
17. Verifikasi Entri rename kedua Old Value `Metro Branch 2` dan New Value `Metro Branch 3`
18. Verifikasi Entri lama tidak ter-overwrite oleh nilai terbaru

## Notes

- Memvalidasi format Modified By "[First Name] [Last Initial]" dengan hover nama lengkap, sifat snapshot immutability log historis tidak berubah pasca-rename, routing log ke Activity Log GS, dan ketiadaan log di System Log User Detail (DIV-LOGIC-03b, PRD §8.1, §8.2, §8.3).
- Sumber pemetaan test case granular: TC-GS-DIV-242, TC-GS-DIV-243, TC-GS-DIV-244, TC-GS-DIV-245.
