---
id: TC-GS-ACTLOG-E2E-041-tab-user-action-search-dropdown-logika-or-dan-chip-removal
title: "Tab User Action: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-170
  - TC-GS-ACTLOG-171
  - TC-GS-ACTLOG-172
  - TC-GS-ACTLOG-173
  - TC-GS-ACTLOG-174
coverage:
  web: automated
---

# Tab User Action: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat variasi opsi pada field multi-select Tab User Action

## Test Steps

### Search di Dalam Dropdown
1. Buka Filter Panel Tab User Action, buka field Object.
2. Ketik kata kunci 'role' di input search internal dropdown, verifikasi opsi 'Role & Permission' tampil.
3. Ketik kata kunci non-existent 'zzz', verifikasi daftar opsi kosong tanpa pesan error.
### Siklus Chip Seleksi 2-Arah
4. Centang opsi 'Create', verifikasi chip 'Create' muncul di dalam field Action.
5. Centang opsi kedua 'Edit', verifikasi chip kedua muncul berdampingan.
6. Klik icon (✕) pada chip 'Create' tanpa membuka dropdown, verifikasi chip hilang dan centang di daftar opsi otomatis terlepas.
7. Buka dropdown list, hilangkan centang opsi 'Edit', verifikasi chip otomatis hilang dari field.
### Overflow Chip Multi-Seleksi
8. Pilih 6 opsi pada salah satu field multi-select.
9. Verifikasi sebagian chip tampil dan sisanya diringkas dalam counter '+N more'.
10. Verifikasi field tidak melebar keluar dari batas Filter Panel.

## Notes

- Interaksi chip seleksi pada Tab User Action seragam dengan konvensi multi-select platform.
