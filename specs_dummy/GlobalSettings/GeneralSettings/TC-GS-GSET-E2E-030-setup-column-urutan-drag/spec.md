---
id: TC-GS-GSET-E2E-030-setup-column-urutan-drag
title: "Setup Column: drag urutan keenam kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-89
  - TC-GS-GSET-90
  - TC-GS-GSET-91
  - TC-GS-GSET-92
  - TC-GS-GSET-93
  - TC-GS-GSET-94
coverage:
  web: automated
---

# Setup Column: drag ulang urutan kolom dan persist

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Modal Changelog memiliki data; kolom default berurutan Action → Field → Old Value → New Value →
  Modified By → Date Modified.

## Test Steps

1. Buka Modal Changelog; buka popup Setup Column

### Drag per kolom ke posisi baru

2. Drag kolom `Field` satu posisi ke bawah
3. Verifikasi tabel langsung memperbarui urutan kolom (live preview): `Action, Old Value, Field, ...`
4. Drag kolom `Date Modified` ke posisi pertama
5. Verifikasi tabel menampilkan `Date Modified` di kolom pertama
6. Drag kolom `Action` ke posisi terakhir dan `Old Value` ke urutan kedua
7. Verifikasi susunan kolom pada tabel mengikuti posisi terakhir drag

### Persist setelah muat ulang

8. Tutup popup; muat ulang halaman
9. Verifikasi urutan kolom yang telah di-drag bertahan

### Urutan default tidak berubah untuk tabel lain

10. `after` spec: pindahkan kembali susunan ke urutan awal dan render ulang
11. Verifikasi urutan default kembali: `Action, Field, Old Value, New Value, Modified By, Date Modified`

## Notes

- Drag diuji hanya pada kolom yang bisa di-reorder (seluruh enam). Guard drag saat hanya 1 kolom
  tersisa dibuktikan bersamaan pada spec 029 (guard minimum).