---
id: TC-GS-GSET-E2E-036-snapshot-immutability-entri-lama
title: Snapshot immutability entri log lama
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-106
coverage:
  web: automated
---

# Snapshot immutability: entri changelog lama tidak berubah

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Hook menyiapkan entri changelog lama (misal catatan `Time Zone` lama dengan `Old Value`,`New Value`,
  `Modified By`, dan `Date Modified` statis).

## Test Steps

1. Buka Modal Changelog
2. Verifikasi entri changelog lama tampil dengan nilai snapshot persis (tanggal & pembuat tercatat
    saat itu — bukan dirender ulang dari state saat ini)
3. Lakukan perubahan field lain (misal `Session Idle Timeout`) dan simpan
4. Verifikasi entri lama tidak berubah/cara render tetap menampilkan snapshot asli
5. Verifikasi entri lama juga tidak berubah saat field yang sama diubah lagi (snapshot tetap dari
    kejadian pertama)
6. Muat ulang halaman; verifikasi entri lama tetap identik (immutable lintas sesi)

## Notes

- PMC `SNAPSHOT-CONTRACT` dipenuhi: entri changelog adalah snapshot waktu kejadian, bukan relasi
  langsung ke nilai saat ini.