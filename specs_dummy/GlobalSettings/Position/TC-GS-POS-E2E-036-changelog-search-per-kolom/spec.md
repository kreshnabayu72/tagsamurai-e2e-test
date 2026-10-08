---
id: TC-GS-POS-E2E-036-changelog-search-per-kolom
title: Popup Changelog — Search per Kolom (Action, Name, Field, Old/New Value, Modified By) & Guard Kolom Date
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-218
  - TC-GS-POS-201
  - TC-GS-POS-202
  - TC-GS-POS-203
  - TC-GS-POS-204
  - TC-GS-POS-205
  - TC-GS-POS-206
  - TC-GS-POS-207
coverage:
  web: automated
---

# Popup Changelog — Search per Kolom (Action, Name, Field, Old/New Value, Modified By) & Guard Kolom Date

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia entri Changelog: Create/Edit/Delete, termasuk mutasi Edit dengan Old Value/New Value spesifik (mis. TC-GS-POS-123) dan Modified By ber-nama panjang untuk uji tooltip.
- Toolbar search popup Changelog: submit-on-Enter, bukan live-as-you-type, icon (✕) menghapus teks tanpa auto-submit, collapse via (←).

## Test Steps

### A. Siklus search toolbar

1. Buka Popup Changelog → klik icon Search → bar reveal, auto-focus, placeholder sesuai.
2. Ketik `"Delete"`, icon (✕) muncul, tabel belum tersaring.
3. Tekan `Enter` → tabel tersaring.
4. Klik (✕) → teks kosong, bar tetap terbuka & fokus, tabel tetap hasil terakhir.
5. Tekan `Enter` → reset ke seluruh entri.
6. Ketik keyword, Enter, klik (←) → collapse & kembali default.

### B. Search by kolom

7. Ketik `"edit"` (case-insensitive) → Enter → hanya entri Action `"Edit"`.
8. Clear via (✕)+Enter.
9. Ketik `"it manager"` → Enter → hanya entri dengan Name `"IT Manager"`.
10. Clear.
11. Ketik `"name"` → Enter → hanya entri yang mencatat field `"Name"`.
12. Clear.
13. Ketik `"client relations"` → Enter → entri dengan Old Value mengandung frasa tsb.
14. Clear.
15. Ketik `"client success"` → Enter → entri dengan New Value mengandung frasa tsb.
16. Clear.
17. Ketik nama user (mis. `"Admin"`) → Enter → hanya entri dimodifikasi user tsb.

### C. Guard kolom Date

18. Ketik teks format tanggal (mis. `"14 Jul 2026"`) → Enter.
19. Verifikasi tidak cocok ke kolom Date; tampil `"No results found"`.
20. Verifikasi pencarian tanggal wajib lewat Filter Panel Date.

### D. Tooltip Modified By & sel terpotong (konfirmasi)

21. Hover sel Modified By format singkat → tooltip nama lengkap utuh.
22. Hover sel Old Value/New Value terpotong → tooltip isi lengkap.

## Notes

- C menegaskan Date non-searchable di toolbar search box popup Changelog (berlaku hanya di popup ini).
