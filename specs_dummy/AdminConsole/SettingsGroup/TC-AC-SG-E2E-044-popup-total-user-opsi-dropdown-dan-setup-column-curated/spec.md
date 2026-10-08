---
id: TC-AC-SG-E2E-044-popup-total-user-opsi-dropdown-dan-setup-column-curated
title: "Screening opsi dropdown filter, 5 kolom curated Setup Column, dan screening Column Visibility popup Total User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-161
  - TC-AC-SG-191
  - TC-AC-SG-192
  - TC-AC-SG-221
coverage:
  web: automated
---

# Screening opsi dropdown filter, 5 kolom curated Setup Column, dan screening Column Visibility popup Total User

## Prerequisites

- Login sebagai Role: Total Control
- Popup drill-down Total User terbuka

## Test Steps

### Screening Opsi Dropdown Filter
1. Buka Filter Panel pada popup Total User
2. Buka dropdown Position dan Division, verifikasi opsi terisi dinamis dari data user yang terdaftar di scope node ini
3. Buka dropdown Group Role, verifikasi memuat opsi baku (`Total Control`, `Read Only`, `Group Manager`) ditambah nama role literal yang aktif
4. Verifikasi Filter Panel memuat 4 filter curated: `Activation Status`, `Temporary User`, `Temporary Until`, dan `[Custom Field aktif]`
### Setup Column & Column Visibility Dropdown
5. Tutup Filter Panel lalu klik header menu elipsis `[⋯]` pada tabel popup
6. Verifikasi dropdown `"Column Visibility"` terbuka (berupa dropdown quick panel karena popup read-only)
7. Verifikasi 5 kolom bawaan berstatus Checked (Hideable): Name, Email, Position, Division, Group Role
8. Verifikasi 5 opsi kolom curated tersedia dengan status default Unchecked: `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `[Custom Field aktif]`
9. Verifikasi kolom `User Type` TIDAK MUNCUL sebagai kolom curated (populasi heterogen union)

## Notes

- Filter curated pada popup tetap berfungsi independen dari status visibilitas kolom di Setup Column.
