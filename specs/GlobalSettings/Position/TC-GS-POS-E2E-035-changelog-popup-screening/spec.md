---
id: TC-GS-POS-E2E-035-changelog-popup-screening
title: Popup Changelog — Screening Struktur, Toolbar, Empty States, Hover Tooltip
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-75
  - TC-GS-POS-112
coverage:
  web: automated
---

# Popup Changelog — Screening Struktur, Toolbar, Empty States, Hover Tooltip

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia entri mutasi Changelog (Create/Edit/Delete) agar testing hover/isi relevan. Jika belum ada, buat minimal satu entri terlebih dahulu.
- Konvensi: Popup Changelog 3 zona (Header/Body/Footer), kolom Actions header = Setup Column (read-only, tidak ada row action).

## Test Steps

### A. Screening struktur Popup Changelog

1. Buka halaman `Global Settings > User > Position`.
2. Klik icon Changelog di toolbar kanan atas tabel utama → Popup Changelog terbuka.
3. Verifikasi Header: title `"Changelog: Position"`, tombol Close `(X)`.
4. Verifikasi Table Tools Header: `Search "Search action, field, or value..." | Filter | Download`.
5. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯)` (unsortable header klik = Setup Column, kolom kosong per baris, read-only).
6. Verifikasi format sel: dash `—` pada Create/Delete, default sort Date descending (Newest First).
7. Verifikasi Footer: pagination modal (default 10).
8. Tutup popup.

### B. Empty states

9. Buka Popup Changelog (dalam kondisi tanpa entri jika bisa diuji, atau amati). Jika sudah ada entri, lanjut ke C.
10. Verifikasi genuinely kosong menampilkan `"No changelog yet."`.
11. Ketik keyword acak tidak match → verifikasi search kosong menampilkan `"No results found"` (dengan titik sesuai string popup Changelog).

### C. Search box behavior (reveal, focus, clear, collapse, tooltip) & hover tooltip

12. Buka Popup Changelog (dengan entri mutasi tersedia).
13. Hover icon Search di toolbar Popup Changelog → muncul tooltip `🔖 Search`.
14. Klik icon Search → search bar melebar (reveal), kursor auto-focus, placeholder `"Search action, field, or value..."`.
15. Ketik `"Delete"` (tanpa Enter dulu) → icon `(✕)` muncul; tabel **belum** tersaring (bukan live).
16. Tekan `Enter` → tabel menyaring entri Delete.
17. Klik `(✕)` → teks terhapus, search bar tetap terbuka, kursor tetap fokus, **tabel tidak langsung reset** (masih menampilkan hasil terakhir).
18. Tekan `Enter` lagi pada input kosong → tabel reset ke seluruh entri log.
19. Ketik ulang keyword, Enter, lalu klik icon `(←)` → search bar collapse kembali ke icon Search, tabel langsung kembali ke kondisi default.

### D. Hover tooltip Modified By & sel terpotong

20. Pada kolom `Modified By`, hover sel nama user dalam format singkat → tooltip menampilkan **nama lengkap user secara utuh**.
21. Hover sel `Old Value` atau `New Value` yang terpotong (elipsis) → tooltip menampilkan isi lengkap.

## Notes

- Screening ini fokus struktur & perilaku toolbar search popup Changelog (beda dari tabel utama).
- Empty state spesifik popup Changelog memakai `"No results found"` dengan titik.
