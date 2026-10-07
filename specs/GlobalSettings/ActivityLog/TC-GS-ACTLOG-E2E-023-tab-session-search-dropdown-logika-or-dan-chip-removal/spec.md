---
id: TC-GS-ACTLOG-E2E-023-tab-session-search-dropdown-logika-or-dan-chip-removal
title: "Tab Session: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-81
  - TC-GS-ACTLOG-82
  - TC-GS-ACTLOG-83
  - TC-GS-ACTLOG-84
  - TC-GS-ACTLOG-85
coverage:
  web: automated
---

# Tab Session: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat variasi opsi pada field multi-select Tab Session

## Test Steps

### Search di Dalam Dropdown
1. Buka Filter Panel Tab Session, buka field multi-select User.
2. Ketik kata kunci 'jo' di input search internal dropdown, verifikasi opsi 'John Doe' dan 'John Dalton' tampil, sedangkan opsi lain terfilter.
3. Ketik kata kunci non-existent 'zzz', verifikasi daftar opsi kosong tanpa error.
### Siklus Chip Seleksi 2-Arah
4. Centang opsi 'John Doe', verifikasi chip berlabel 'John Doe' muncul di dalam field.
5. Centang opsi kedua 'Budi Anwar', verifikasi chip kedua muncul di samping chip pertama.
6. Klik icon (✕) pada chip 'John Doe' tanpa membuka dropdown, verifikasi chip hilang dan centang di daftar opsi otomatis terlepas.
7. Buka dropdown list, hilangkan centang pada opsi 'Budi Anwar', verifikasi chip 'Budi Anwar' di dalam field langsung terhapus.
### Overflow Chip Multi-Seleksi
8. Pilih 6 opsi pada salah satu field multi-select.
9. Verifikasi sebagian chip ditampilkan dan sisanya diringkas menjadi chip counter '+N more'.
10. Verifikasi field tidak melebar keluar dari batas Filter Panel.

## Notes

- Komponen multi-select mendukung pencarian internal, seleksi chip dua arah, dan ringkasan overflow.
