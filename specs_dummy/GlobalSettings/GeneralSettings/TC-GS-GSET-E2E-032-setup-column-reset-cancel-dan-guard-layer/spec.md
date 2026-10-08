---
id: TC-GS-GSET-E2E-032-setup-column-reset-cancel-dan-guard-layer
title: "Setup Column: reset, cancel, dan guard layer"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-101
  - TC-GS-GSET-102
  - TC-GS-GSET-157
  - TC-GS-GSET-158
coverage:
  web: automated
---

# Setup Column: reset to default, cancel, dan guard-lever top layer

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Modal Changelog memiliki data; kolom default enam.

## Test Steps

1. Buka Modal Changelog; buka popup Setup Column

### Reset to Default

2. Lakukan perubahan urutan/hide di popup (misal hide `Action`, pindah `Date Modified` ke kiri)
3. Klik `[Reset to Default]`
4. Verifikasi seluruh kolom kembali ke tampilan default enam, urutan default, tanpa hidden
5. Verifikasi popup menampilkan kondisi reset di semua baris (semua toggle/unhide & urutan default)
6. Tutup popup; verifikasi tabel mencerminkan kondisi default
7. Muat ulang halaman; verifikasi state default persist

### Cancel (batal tanpa simpan)

8. Lakukan perubahan lagi (hidden `New Value`, pindah `Field`)
9. Klik ikon `[✕]` / tekan `Esc` pada popup
10. Verifikasi popup tertutup dan perubahan batalkan
11. Verifikasi tabel tetap menampilkan kondisi sebelum dibuka popup (state sebelumnya)
12. Buka popup lagi; verifikasi state terakhir tetap (bukan hasil perubahan yang dibatalkan)

### Guard-lever: tombol ⋯ pada header tabel tetap terlihat & Esc tutup lapisan

13. Sembunyikan beberapa kolom sehingga header tabel bergeser ke kanan
14. Verifikasi ikon Column Visibility `(⋯)` tetap tampil dan dapat dibuka (perilaku terlepas dari
    jumlah kolom visible)
15. Saat setup column & popup/kriteria lain terbuka bertumpuk, tekan `Esc`
16. Verifikasi hanya layer top paling atas yang tertutup (guard layer top)

## Notes

- Guard-lever dibuktikan dengan memastikan `Esc` tidak menutup layer yang lebih dalam sebelum layer
  teratas ditutup.