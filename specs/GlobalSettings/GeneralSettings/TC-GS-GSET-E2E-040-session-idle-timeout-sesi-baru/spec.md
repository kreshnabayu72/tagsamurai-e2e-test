---
id: TC-GS-GSET-E2E-040-session-idle-timeout-sesi-baru
title: Idle timeout berlaku sesi baru saja
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-137
coverage:
  web: automated
---

# Session Idle Timeout hanya berlaku untuk sesi baru

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Sesi aktif saat ini menggunakan nilai default `15 minutes`.

## Test Steps

1. Buka `Global Settings > General Settings`
2. Verifikasi sesi yang sedang berjalan masih menggunakan nilai `15 minutes` (tidak terpengaruh)
3. Ubah `Session Idle Timeout` menjadi `1 hour` dan simpan
4. Verifikasi tampilan form mengonfirmasi penyimpanan (tanpa menutup sesi yang sedang aktif)
5. Logout, lalu login ulang
6. Verifikasi sesi baru menggunakan `1 hour` (nilai baru) — buktikan dengan perilaku/indikator yang
    menampilkan durasi sesi
7. Logout dan login ulang lagi; verifikasi nilai tetap `1 hour` (persist lintas sesi)

## Notes

- PMC `SESSION-IDLE-CONTRACT` terpenuhi: perubahan idle timeout tidak memotong sesi yang sedang
  berjalan; hanya sesi-sesi baru yang membaca nilai baru.