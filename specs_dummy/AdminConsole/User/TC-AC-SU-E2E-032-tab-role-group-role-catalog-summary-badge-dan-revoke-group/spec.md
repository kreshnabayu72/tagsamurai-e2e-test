---
id: TC-AC-SU-E2E-032-tab-role-group-role-catalog-summary-badge-dan-revoke-group
title: "Tab Role Sub-tab Group Role: Katalog Role, Group Summary Badge, dan Revoke Akses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-74
  - TC-AC-SU-75
  - TC-AC-SU-76
  - TC-AC-SU-77
  - TC-AC-SU-80
  - TC-AC-SU-81
  - TC-AC-SU-82
  - TC-AC-SU-85
coverage:
  web: automated
---

# Tab Role Sub-tab Group Role: Katalog Role, Group Summary Badge, dan Revoke Akses

## Prerequisites

- Login sebagai Total Control
- Target user memiliki beberapa penugasan Group Role aktif

## Test Steps

### Screening Sub-tab Group Role dan Group Summary Badge
1. Buka `Admin Console > Settings > User > [Detail User]`
2. Buka tab `Role` lalu klik sub-tab `Group Role`
3. Verifikasi daftar katalog peran grup yang tersedia
4. Verifikasi badge `Group Summary` pada tiap baris peran menampilkan jumlah grup yang ter-assign (misal `"3 Groups"`)
5. Verifikasi toggle switch peran berada pada posisi ON jika memiliki >= 1 grup ter-assign

### Alur Revokasi Peran Grup via Toggle OFF
6. Klik toggle switch peran ke posisi OFF
7. Verifikasi dialog konfirmasi bahaya muncul: `"Are you sure to remove all group assignments for this role?"`
8. Klik `[Cancel]`; verifikasi toggle tetap ON dan penugasan grup tetap utuh
9. Klik toggle ke OFF kembali dan klik `[Remove]` pada dialog konfirmasi
10. Verifikasi seluruh penugasan grup untuk peran tersebut dicabut seketika
11. Verifikasi toggle berpindah ke posisi OFF, badge summary menampilkan `"0 Groups"`, dan toast sukses `"Group role assignments removed successfully."` muncul

## Notes

Memvalidasi pengelolaan katalog dan pemutusan akses peran grup di tingkat pengguna.
