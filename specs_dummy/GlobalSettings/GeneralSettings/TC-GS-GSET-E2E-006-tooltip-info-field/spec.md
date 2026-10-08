---
id: TC-GS-GSET-E2E-006-tooltip-info-field
title: Tooltip info pada tiga field
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-14
coverage:
  web: automated
---

# Tooltip info field

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Form dalam keadaan isi sehingga seluruh ikon info tampil.

## Test Steps

1. Buka halaman `Global Settings > General Settings`
2. Verifikasi ikon/marker info tampil di samping label `Currency`
3. Arahkan kursor ke ikon info `Currency`
4. Verifikasi tooltip menampilkan penjelasan bahwa `Currency` menentukan satuan rupiah dari transaksi
   (kemungkinan offset waktu/negara juga sesuai data)
5. Verifikasi tooltip menghilang saat kursor menjauh
6. Verifikasi ikon info tampil di samping label `Time Zone`
7. Verifikasi tooltip `Time Zone` menjelaskan bahwa `Time Zone` menentukan zona waktu jam kerja
   (kemungkinan offset waktu/negara juga sesuai data)
8. Verifikasi ikon info tampil di samping label `Session Idle Timeout`
9. Verifikasi tooltip `Session Idle Timeout` menjelaskan bahwa nilai ini menentukan durasi sebelum sesi
   dianggap idle (default `15 minutes`) dan tidak berlaku surut ke sesi yang sudah berjalan

## Notes

- Verifikasi hanya keberadaan dan isi tooltip info, bukan perilaku sinkron yang dibahas spec 040-041.
- Apabila tooltip beserta perilaku buka/tutup dimiliki bersama dengan Guided Tooltip pada PRD §4.7.
  keperilakuan walkthrough dijembatani ke spec 007.