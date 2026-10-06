---
id: TC-GS-GSET-E2E-034-download-changelog-gagal-server
title: Download bergagal saat server bermasalah
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-104
coverage:
  web: automated
mock: true
---

# Download changelog: gagal saat server error

## Prerequisites

- Spec ini dijalankan dengan `Mode: mock`. Endpoint download `(CSV/XLSX)` memberi respons error 500.
- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).

## Test Steps

1. Buka halaman `Global Settings > General Settings` (bukan hanya modal changelog) dengan mock download
   diatur untuk mengembalikan error
2. Buka Modal Changelog
3. Klik tombol `Download` (format `CSV` atau `XLSX`)
4. Verifikasi toast error tampil `Error, failed to download Changelog-General-Settings.`
5. Verifikasi modal changelog tetap terbuka (tidak tertutup akibat error)
6. Verifikasi tidak ada file yang terunduh sebagian/rusak di direktori download
7. Klik `Download` sekali lagi; verifikasi pengguna dapat mencoba lagi (tombol tidak terkunci)

## Notes

- Simulasi error file harus memastikan tidak ada side-effect file parsial yang tertinggal di browser.