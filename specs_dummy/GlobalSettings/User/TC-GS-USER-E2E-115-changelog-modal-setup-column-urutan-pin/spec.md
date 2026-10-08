---
id: TC-GS-USER-E2E-115-changelog-modal-setup-column-urutan-pin
title: 'Setup Column modal Changelog: urutan kolom dan pin'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-316
  - TC-GS-USER-317
  - TC-GS-USER-318
  - TC-GS-USER-319
  - TC-GS-USER-320
  - TC-GS-USER-321
  - TC-GS-USER-322
  - TC-GS-USER-323
  - TC-GS-USER-324
  - TC-GS-USER-325
  - TC-GS-USER-326
  - TC-GS-USER-327
  - TC-GS-USER-328
  - TC-GS-USER-329
coverage:
  web: automated
---

# Setup Column modal Changelog: urutan kolom dan pin

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data Changelog mock dengan lebih dari 10 baris dan nilai panjang supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom modal Changelog disimpan di browser terpisah dari User List dan Tab Changelog, dan dikembalikan ke default di langkah akhir

## Test Steps

1. Buka popup modal Setup Column di modal Changelog User List
2. Drag baris `Modified By` ke posisi paling atas dan `Date` ke posisi paling bawah
3. Verifikasi urutan di Live Preview dan tabel asli berubah sesuai drag
4. Klik ikon Pin pada `Modified By` dan `Action`
5. Klik `[Save]` lalu scroll tabel ke samping
6. Verifikasi `Modified By` dan `Action` membeku saat scroll
7. Refresh halaman
8. Verifikasi urutan dan pin bertahan
9. Buka popup modal lagi, lepas pin `Action`, lalu `[Save]`
10. Verifikasi `Action` ikut bergeser saat scroll sedangkan `Modified By` tetap membeku
11. Kembalikan ke default lewat `[Reset to Default]` dan `[Save]`

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3. Dua kolom mewakili semua kolom untuk drag dan pin.
