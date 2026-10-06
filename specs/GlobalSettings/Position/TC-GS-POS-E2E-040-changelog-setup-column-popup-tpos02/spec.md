---
id: TC-GS-POS-E2E-040-changelog-setup-column-popup-tpos02
title: Popup Changelog — Setup Column Popup T-POS-02 (Drag, Check/Uncheck, Pin, Reset to Default, Cancel/X, Persist)
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-138
  - TC-GS-POS-139
  - TC-GS-POS-143
  - TC-GS-POS-144
  - TC-GS-POS-145
  - TC-GS-POS-148
  - TC-GS-POS-149
  - TC-GS-POS-150
  - TC-GS-POS-153
  - TC-GS-POS-154
  - TC-GS-POS-155
  - TC-GS-POS-158
  - TC-GS-POS-159
  - TC-GS-POS-160
  - TC-GS-POS-163
  - TC-GS-POS-164
  - TC-GS-POS-165
  - TC-GS-POS-168
  - TC-GS-POS-169
  - TC-GS-POS-170
  - TC-GS-POS-173
  - TC-GS-POS-174
  - TC-GS-POS-175
  - TC-GS-POS-177
coverage:
  web: automated
---

# Popup Changelog — Setup Column Popup T-POS-02

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Popup Changelog terbuka (T-POS-02). Kolom: Date, Action, Name, Field, Old Value, New Value, Modified By, Actions.
- Setup Column tersedia via `[Setup Column]` di overlay column visibility header Changelog.

## Test Steps

### A. Screening Setup Column Changelog

1. Buka Popup Changelog → Actions ⋯ header → `[Setup Column]`.
2. Verifikasi title `"Setup Column"`, info guidance, tombol `(X)`.
3. Verifikasi daftar kolom Changelog, live preview, footer `[Cancel] [Save] [Reset to Default]`.
4. Tutup via `(X)`.

### B. Show/hide per kolom

5. Buka Setup Column Changelog → uncheck kolom (mis. Field/Old Value/New Value) → amati preview → Save.
6. Verifikasi kolom hilang dari tabel Changelog, persist setelah refresh dalam popup.
7. Centang kembali → Save → muncul kembali.

### C. Reorder drag & drop

8. Drag kolom untuk mengubah urutan → preview & tabel mengikuti.
9. Coba drag kolom teratas ke bawah/kolom bawah ke atas sesuai batasan → perilaku sesuai (drag handle aktif).
10. Save → persist setelah refresh.

### D. Pin/Unpin

11. Pin kolom (mis. Date/Name/Modified By) → indikator aktif → Save.
12. Scroll horizontal tabel Changelog (viewport sempit) → kolom ter-pin membeku (sticky).
13. Refresh → status pin persist.
14. Unpin kembali.

### E. Reset to Default

15. Ubah konfigurasi (hide/reorder/pin) → buka Setup Column → `[Reset to Default]`.
16. Verifikasi preview kembali ke default → Save → tabel kembali default & persist.

### F. Cancel & X (discard)

17. Ubah konfigurasi → klik `[Cancel]` atau `(X)`.
18. Verifikasi popup tertutup, perubahan di-discard, tabel tetap seperti semula, tidak tersimpan.

### G. Guard minimal 1 kolom visible

19. Sembunyikan kolom hingga tersisa 1 kolom visible.
20. Verifikasi checkbox kolom terakhir disabled, tidak bisa di-uncheck + tooltip guard.

## Notes

- T-POS-02 terpisah dari T-POS-01 (tabel utama). Konfigurasi tidak bercampur.
