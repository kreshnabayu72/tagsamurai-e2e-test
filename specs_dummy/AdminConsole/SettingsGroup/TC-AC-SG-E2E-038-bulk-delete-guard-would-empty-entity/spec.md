---
id: TC-AC-SG-E2E-038-bulk-delete-guard-would-empty-entity
title: "Guard Bulk Delete would-empty-entity: pemblokiran total batch jika seluruh group entitas akan musnah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-72
  - TC-AC-SG-73
coverage:
  web: automated
---

# Guard Bulk Delete would-empty-entity: pemblokiran total batch jika seluruh group entitas akan musnah

## Prerequisites

- Login sebagai Role: Total Control
- Kasus A: Entitas memiliki tepat 2 group kosong
- Kasus B: Entitas memiliki 3 group (2 kosong, 1 memiliki member)

## Test Steps

### Kasus A: Blokir Total (T - E == 0)
1. Buka `Settings > Group` pada entitas dengan 2 group kosong
2. Centang kedua group tersebut via checkbox
3. Klik tombol `[Delete]` pada Bulk Action Bar
4. Verifikasi muncul dialog blokir total `"Cannot Delete Groups"`
5. Verifikasi body dialog menyebutkan nama-nama group yang eligible: `"These groups are all that's left: [Group 1], [Group 2]. At least one group must always exist — deselect at least one of the groups above and try again."` dengan tombol `[OK]`
6. Verifikasi tidak ada group yang terhapus
### Kasus B: Lolos Guard Karena Ada yang Tersisa (Skip)
7. Buka `Settings > Group` pada entitas dengan 3 group (1 ber-member)
8. Centang ketiganya lalu klik `[Delete]` di Bulk Action Bar
9. Verifikasi guard would-empty-entity TIDAK MEMBLOKIR karena 1 group ber-member di-skip dan tetap tersisa (`T - E >= 1`)
10. Verifikasi sistem melanjutkan ke dialog campuran

## Notes

- Guard would-empty-entity (ACSG-LOGIC-03) dievaluasi sebagai Langkah 0 sebelum evaluasi per baris.
