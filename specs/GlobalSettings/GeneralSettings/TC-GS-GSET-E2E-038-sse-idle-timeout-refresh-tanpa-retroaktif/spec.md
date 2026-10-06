---
id: TC-GS-GSET-E2E-038-sse-idle-timeout-non-retroaktif
title: SSE idle timeout refresh tampilan, tidak retroaktif
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-134
coverage:
  web: automated
---

# SSE idle timeout: refresh tampilan, bukan menimpa nilai baru

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data `Session Idle Timeout` yang tersimpan berbeda dengan nilai seed.
- Konsep idle timeout yang dimaksud adalah waktu tunggu koneksi SSE (bukan sesi login).

## Test Steps

1. Buka `Global Settings > General Settings`
2. Verifikasi koneksi SSE timeout saat tidak ada event dalam jangka waktu yang ditetapkan
3. Verifikasi pada timeout, aplikasi melakukan fetch ulang snapshot (GET) dan menampilkan nilai
   terbaru
4. Kunjungi tab lain tanpa mutasi; biarkan timeout terjadi
5. Kembali ke tab General Settings
6. Verifikasi halaman menampilkan nilai terbaru dari server (refresh tampilan)
7. Verifikasi timeout TIDAK berlaku surut/retroaktif: nilai yang tercatat di changelog sebelum timeout
   tidak berubah; snapshot yang lama tetap tampil di Modal Changelog
8. Verifikasi tidak ada dampak pada sesi login auth (idle timeout sesi berbeda — lihat spec 040-041)

## Notes

- Perbedaan idle timeout SSE vs idle timeout sesi dibahas pada spec 040-041; spec ini fokus pada
  refresh display saat timeout stream tanpa menimpa riwayat/snapshot yang sudah ada.