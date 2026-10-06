---
id: TC-AC-SU-E2E-042-cross-action-race-conditions-resilience
title: "Resiliensi race condition 2 aktor: Deactivate vs Assign Group Role dan Deactivate vs Edit Role Auto-Revert"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-215
  - TC-AC-SU-216
coverage:
  web: automated
---

# Resiliensi race condition 2 aktor: Deactivate vs Assign Group Role dan Deactivate vs Edit Role Auto-Revert

## Prerequisites

- 2 Sesi Login Admin Total Control (Aktor A dan Aktor B) yang beroperasi bersamaan
- Target user X dalam status Active dan Total Control

## Test Steps

### Race Condition: Deactivate vs Assign Group Role

1. Pada Sesi Admin B, buka popup Assign Group Role untuk target user X dan siapkan penugasan group baru
2. Pada Sesi Admin A, lakukan Deactivate pada target user X yang sama dan klik konfirmasi lebih dulu
3. Seketika setelah Admin A commit, klik `[Save]` pada popup di Sesi Admin B
4. Verifikasi kedua request berhasil diproses secara independen tanpa error korupsi data:
5.   - Status user menjadi `is_active = false` (sesi login user X diputus)
6.   - Penugasan group baru dari Admin B tetap tersimpan di DB
7.   - Terbentuk 2 entri changelog terpisah (`Deactivate` dan `Assign Group Role`)

### Race Condition: Deactivate vs Edit Role (Auto-Revert)

1. Admin A melakukan Deactivate pada target user Total Control
2. Nyaris bersamaan, Admin B mengubah 1 checkbox Global Role pada target user yang sama hingga memicu Auto-Revert
3. Verifikasi kedua aksi saling komutatif dan menghasilkan state akhir yang konsisten: `is_active = false` DAN `access_level = —`

## Notes

- Domain status aktif dan domain penugasan role bersifat independen dalam transaksi database.
