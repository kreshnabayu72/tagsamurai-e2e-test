---
id: TC-GS-USER-E2E-114-changelog-modal-setup-column-hide
title: 'Setup Column modal Changelog: overlay, popup, dan sembunyikan kolom'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-248
  - TC-GS-USER-308
  - TC-GS-USER-309
  - TC-GS-USER-310
  - TC-GS-USER-311
  - TC-GS-USER-312
  - TC-GS-USER-313
  - TC-GS-USER-314
  - TC-GS-USER-315
coverage:
  web: automated
---

# Setup Column modal Changelog: overlay, popup, dan sembunyikan kolom

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data Changelog mock dengan lebih dari 10 baris dan nilai panjang supaya tabel bisa di-scroll ke samping
- Konfigurasi kolom modal Changelog disimpan di browser terpisah dari User List dan Tab Changelog, dan dikembalikan ke default di langkah akhir

## Test Steps

1. Buka modal Changelog User List dan klik header kolom `(⋯)`
2. Verifikasi overlay berisi 7 kolom Hideable (Date, Action, Name, Field, Old Value, New Value, Modified By), tercentang dan aktif dengan handle drag
3. Buka popup modal Setup Column
4. Verifikasi header "Setup Column" dengan teks info dan `✕`, 7 baris kolom beserta Live Preview, dan footer `[Reset to Default]`, `[Cancel]`, `[Save]`
5. Hapus centang enam kolom selain `Action`
6. Verifikasi Live Preview dan tabel menyisakan `Action` dan checkbox `Action` Disabled dengan tooltip "At least one column must remain visible."
7. Centang kembali `Date`
8. Verifikasi checkbox `Action` kembali aktif
9. Klik `[Save]` lalu refresh
10. Verifikasi hanya `Date` dan `Action` yang tampil dan konfigurasi bertahan setelah refresh
11. Buka Setup Column di User List dan Tab Changelog
12. Verifikasi konfigurasi kedua tempat itu tidak berubah (cache terpisah)
13. Kembalikan modal Changelog ke default lewat `[Reset to Default]` dan `[Save]`

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.3. Satu spec memverifikasi ketujuh kolom karena perilaku ceklis identik.
