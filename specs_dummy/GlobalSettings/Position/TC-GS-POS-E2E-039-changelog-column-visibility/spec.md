---
id: TC-GS-POS-E2E-039-changelog-column-visibility
title: Popup Changelog — Column Visibility, Search per Kolom Tersimpan, Persist
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-111
  - TC-GS-POS-140
  - TC-GS-POS-141
  - TC-GS-POS-142
  - TC-GS-POS-146
  - TC-GS-POS-147
  - TC-GS-POS-151
  - TC-GS-POS-152
  - TC-GS-POS-156
  - TC-GS-POS-157
  - TC-GS-POS-161
  - TC-GS-POS-162
  - TC-GS-POS-166
  - TC-GS-POS-167
  - TC-GS-POS-171
  - TC-GS-POS-172
  - TC-GS-POS-251
coverage:
  web: automated
---

# Popup Changelog — Column Visibility, Search per Kolom Tersimpan, Persist

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Popup Changelog T-POS-02 tersedia (tabel Changelog Position). Kolom sesuai wireframe (8 kolom termasuk Actions).

## Test Steps

### A. Column Visibility & reorder (overlay/popup level Changelog)

1. Buka Popup Changelog → buka Overlay Column Visibility (via Actions ⋯ header kolom Changelog).
2. Uji show/hide kolom Changelog (Date, Action, Name, Field, Old Value, New Value, Modified By) — masing-masing Hideable sesuai definisi.
3. Uji reorder drag & drop antar kolom di overlay/popup Setup Column Changelog.
4. Uji guard minimal 1 kolom visible.
5. Terapkan perubahan → Save → verifikasi tabel Changelog mengikuti.
6. Refresh dalam konteks popup/tab → verifikasi persist.

### B. Search per kolom (jika ada kolom-search terpisah) & persist konfigurasi

7. Uji konfigurasi visibility/reorder tersimpan terpisah dari tabel utama (independensi cache antara tabel utama vs Popup Changelog).
8. Logout/login → buka Popup Changelog → konfigurasi kolom tetap utuh.
9. Verifikasi search per kolom yang dikonfigurasi (sesuai TC-111,140–142,146–147,151–152,156–157,161–162,166–167,171–172,251) tetap berfungsi sesuai konfigurasi tersimpan.

## Notes

- Setup kolom untuk Popup Changelog adalah level terpisah (T-POS-02) vs tabel utama T-POS-01 — konfigurasi tidak boleh bercampur.
- Persistensi menggunakan mekanisme cache terpisah (sesuai §9.3 konvensi).
