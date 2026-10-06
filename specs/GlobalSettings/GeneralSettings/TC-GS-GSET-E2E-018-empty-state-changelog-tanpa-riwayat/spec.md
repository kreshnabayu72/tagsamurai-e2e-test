---
id: TC-GS-GSET-E2E-018-empty-state-changelog-tanpa-riwayat
title: Empty state Modal Changelog tanpa riwayat
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-42
  - TC-GS-GSET-59
coverage:
  web: automated
---

# Empty state Modal Changelog dan dropdown sumber kosong

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Hook menyiapkan tenant yang changelog-nya kosong (tanpa satu pun baris riwayat).

## Test Steps

### Changelog kosong

1. Buka halaman `Global Settings > General Settings`
2. Buka Modal Changelog
3. Verifikasi tabel menampilkan kolom tetap ada (Action, Field, Old Value, New Value, Modified By,
   Date Modified) tetapi tidak ada satupun baris data
4. Verifikasi area kosong menampilkan pesan `No changelog yet` dan penjelasan tambahan
5. Verifikasi kontrol pagination menampilkan indikasi tanpa data (misal `0 of 0`) dan tidak ada kontrol
   halaman yang aktif
6. Verifikasi tombol download tetap tampil (dan mengunduh file kosong/header saja bila diklik)

### Dropdown sumber Modified By kosong

7. Buka Filter dan buka dropdown `Modified By`
8. Verifikasi dropdown menampilkan popup/placeholder dengan pesan kosong (misal "No options found")
9. Verifikasi dropdown tidak menampilkan entri dummy/stub

## Notes

- Kondisi ini muncul setelah tenant besar dibersihkan atau contoh setup belum pernah dimutasi oleh siapa
  pun; spec menggunakan hook untuk menjamin determinisme.