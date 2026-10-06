---
id: TC-GS-GSET-E2E-001-screening-form-general-settings
title: Screening 3 Zona halaman dan ketiadaan row/bulk action
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-01
  - TC-GS-GSET-148
coverage:
  web: automated
---

# Screening 3 Zona halaman dan ketiadaan row/bulk action

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- `Fixture.globalSettingsGeneralSettings.data.existing` berisi record General Settings lengkap ter-seed
  dengan seluruh lima field terisi nilai valid.
- Modul General Settings adalah halaman form single-record dan bukan menu dengan tabel utama, sehingga
  tidak ada Tab Bar; dokumen hanya terdiri dari 3 zona vertikal.

## Test Steps

1. Buka halaman `Global Settings > General Settings`
2. Verifikasi zona Header menampilkan breadcrumb/judul halaman `General Settings` (statis)
3. Verifikasi zona Header menampilkan Icon Button `Changelog` di kanan atas
4. Verifikasi zona Body menampilkan form grid 2 kolom dengan field flat berderet tanpa
   section/divider: `Currency Code`, Preview text Currency, `Time Zone`, `Session Idle Timeout`,
   `Date Format`, `Time Format`, dan Preview text Date & Time menampilkan default `17/04/23 14:30`
   (kombinasi default `dd/MM/yy` + `HH:mm`)
5. Verifikasi tidak ada satu pun label field yang bertanda `*` (kelimanya Required di API namun tidak
   ada state kosong yang bisa dicapai lewat UI; dropdown ter-prefill, record auto-created)
6. Verifikasi zona Footer menampilkan tombol `[Save]` (severity Success) dan **tidak ada tombol Cancel**
7. Verifikasi halaman menampilkan record yang sudah tersimpan (record auto-created), yaitu form dalam
   keadaan terisi dan bukan keadaan kosong
8. Verifikasi tidak ada tombol Create (misalnya `[+ Add]`) di halaman ini
9. Verifikasi tidak ada baris data/baris tabel yang bisa dipilih, tidak ada kolom Checkbox di header
   maupun body, tidak ada ikon Elipsis `(⋯)` per baris, dan tidak ada Bulk Action Bar
10. Verifikasi tidak ada toolbar tabel (Search, Filter, Download) pada tingkat halaman form; satu-satunya
    entry point ke data riwayat adalah Icon Button `Changelog`

## Notes

- Halaman ini adalah form single-record; sebaris data atau aksi tabel hanya muncul di dalam Modal
  Changelog yang dibuka dari Icon Button `Changelog`, dan diperiksa pada spec 017.
- TC-GS-GSET-148 (pemeriksaan "tidak ada kontrol Create/Delete/Bulk") dibuktikan di langkah 8-10 ini.