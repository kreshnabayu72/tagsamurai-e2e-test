---
id: TC-AC-SU-E2E-049-multi-tenant-entity-suspended-blanket-lockdown-resilience
title: "Penegakan Status Entitas Suspended: Blanket Read-Only Lockdown Lintas Modul"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-40
  - TC-AC-SU-159
coverage:
  web: automated
---

# Penegakan Status Entitas Suspended: Blanket Read-Only Lockdown Lintas Modul

## Prerequisites

- Entitas organisasi berstatus "Suspended" oleh Superadmin
- Login sebagai Administrator Total Control pada entitas yang di-suspend

## Test Steps

### Verifikasi Kunci Blanket Read-Only di Settings User
1. Buka menu `Admin Console > Settings > User`
2. Verifikasi banner darurat prominent muncul: `"Your entity is currently suspended. Write operations are disabled."`
3. Verifikasi seluruh kontrol write dikunci total:
   - Seluruh switch kolom Active berstatus disabled
   - Tombol menu aksi baris `[...]` dinonaktifkan
   - Checkbox pemilihan massal dan Bulk Action Bar tidak dapat dioperasikan

### Verifikasi Kunci Lintas Modul (Role & Permission dan Group)
4. Buka menu `Settings > Role & Permission`
5. Verifikasi seluruh kontrol penugasan access_level dan tombol Create/Edit role terkunci
6. Buka menu `Settings > Group`
7. Verifikasi tombol Create Group, Edit Group, dan Delete Group semuanya berstatus disabled

### Verifikasi Reaktifitas Real-Time Event Suspensi (GAP-ACSU-E2E-005)
8. Pada sesi browser yang sedang aktif di halaman Settings User, simulasikan event background webhook suspensi entitas
9. Verifikasi UI secara reaktif mengunci seluruh kontrol write dan memunculkan banner suspensi TANPA MEMERLUKAN refresh browser (F5) manual

## Notes

Mengintegrasikan GAP-ACSU-E2E-005 untuk penegakan keamanan real-time saat entitas di-suspend.
