---
id: TC-GS-POS-E2E-041-changelog-detail-filter-action-keterbatasan
title: Popup Changelog — Detail Filter Action, Keterbatasan Filter (Single-Value Guard), Download Error, Multi-select OR, Chip Removal 2 Arah
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-185
  - TC-GS-POS-192
  - TC-GS-POS-193
  - TC-GS-POS-194
  - TC-GS-POS-195
  - TC-GS-POS-221
  - TC-GS-POS-222
  - TC-GS-POS-223
  - TC-GS-POS-224
  - TC-GS-POS-225
  - TC-GS-POS-227
  - TC-GS-POS-228
  - TC-GS-POS-235
coverage:
  web: automated
---

# Popup Changelog — Detail Filter Action & Keterbatasan

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Popup Changelog berisi entri Create/Edit/Delete dengan variasi user/Position cukup.
- Filter Panel: Action multi-select, Name/Modified By populate dari data Changelog, Date range.

## Test Steps

### A. Clear Field saat Search aktif

1. Search + Filter aktif di Popup Changelog.
2. Buka Filter Panel → `Clear Field` → `Apply`.
3. Verifikasi filter dilepas, keyword Search tetap aktif, tabel menampilkan hasil Search saja.

### B. Filter Action detail (OR dalam field, chip 2 arah)

4. Buka dropdown Action → centang Create dan Edit → closed-state tampil chip terpisah (bukan "2 selected").
5. `Apply` → hasil = Create OR Edit.
6. Tanpa buka dropdown, klik `(X)` pada chip Create → chip hilang, checkbox sinkron.
7. Kembalikan 2 chip, buka dropdown → uncheck Create → chip langsung hilang (checkbox→chip sinkron).
8. Banyak opsi (≥6) di Modified By → overflow chip (`+N more`) terjaga. Banyak opsi (≥6) di Modified By → overflow chip (`+N more`) terjaga.

### C. Keterbatasan filter & Single-Value Guard

9. Verifikasi Field filter tidak ditampilkan (Position hanya 1 atribut mutable = Name) — Single-Value Guard §9.10.
10. Verifikasi populate scope: Name/Modified By hanya opsi yang punya entri Changelog; Position tanpa entri Changelog tidak muncul.
11. Buat entri baru → dropdown Name update real-time.
12. Loading state dropdown → tampil indikator loading (bukan kosong).
13. Stale reference: filter Name aktif, hapus Position master → tabel tetap tampil entri historis; saat panel dibuka ulang, opsi hilang.

### D. Search internal dropdown & download error

14. Dropdown internal search: substring + case-insensitive; tidak match → empty state dalam dropdown.
15. Download Popup Changelog → file Changelog-Position, tidak ada toast sukses.
16. Simulasi backend down → toast error `"Error, failed to download Changelog-Position."`.

### E. Kombinasi lanjut

17. Kombinasi Action multi-select + Name multi-select + Modified By + Date → logika AND antar field, OR dalam field.
18. Search ∩ Filter tetap konsisten (irisan).

## Notes

- Action hardcode 3 opsi; Create polos (tanpa qualifier Import).
- Historis Changelog dipertahankan meski master data dihapus (snapshot) — dropdown populate ikut update saat dibuka ulang.
