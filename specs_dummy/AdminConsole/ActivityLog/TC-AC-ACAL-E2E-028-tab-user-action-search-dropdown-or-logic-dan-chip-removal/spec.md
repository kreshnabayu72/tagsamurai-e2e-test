---
id: TC-AC-ACAL-E2E-028-tab-user-action-search-dropdown-or-logic-dan-chip-removal
title: "Tab User Action — Search dalam dropdown filter, logika OR multi-select, dan manajemen chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-146
  - TC-AC-ACAL-147
  - TC-AC-ACAL-148
  - TC-AC-ACAL-149
  - TC-AC-ACAL-150
  - TC-AC-ACAL-151
  - TC-AC-ACAL-152
  - TC-AC-ACAL-153
  - TC-AC-ACAL-154
  - TC-AC-ACAL-155
  - TC-AC-ACAL-156
  - TC-AC-ACAL-157
  - TC-AC-ACAL-158
  - TC-AC-ACAL-159
  - TC-AC-ACAL-273
  - TC-AC-ACAL-274
  - TC-AC-ACAL-275
coverage:
  web: automated
---

# Tab User Action — Search dalam dropdown filter, logika OR multi-select, dan manajemen chip

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data dengan variasi Action (Create, Edit, Delete, Reassign), Object (Distributor, Partner, Client), dan Modified By

## Test Steps

### Search dalam Dropdown Multi-Select

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"` > klik `[Filter]`
2. Buka dropdown `Action` dan cari opsi melalui input search internal dropdown
3. Verifikasi opsi menyaring sesuai kata kunci
4. Ulangi untuk dropdown `Object` dan `Modified By`

### Logika OR Multi-Select & Chip Display

5. Pada dropdown `Action`, centang opsi `"Create"` dan `"Delete"`
6. Verifikasi dua chip berlabel Create dan Delete muncul di field
7. Klik tombol `[Apply]`
8. Verifikasi tabel menampilkan baris dengan Action Create ATAU Delete

### Penghapusan Chip via (X) dan Uncheck

9. Buka kembali Filter Panel
10. Klik tombol `(X)` pada chip Create
11. Verifikasi chip Create terhapus dan checkbox Create di dropdown otomatis uncheck (chip Delete tetap ada)
12. Centang 2 opsi pada field `Object`
13. Buka dropdown Object dan uncheck salah satu opsi
14. Verifikasi chip terkait otomatis hilang dari input box
15. Lakukan uji coba chip add/remove pada field `Modified By`

### Overflow Chip

16. Centang banyak opsi pada field Action hingga melebihi ruang input
17. Verifikasi penanganan overflow berjalan rapi (`+N more` atau scrollable chip container)

## Notes

- Memverifikasi interaksi filter multi-select chip pada Tab User Action.
