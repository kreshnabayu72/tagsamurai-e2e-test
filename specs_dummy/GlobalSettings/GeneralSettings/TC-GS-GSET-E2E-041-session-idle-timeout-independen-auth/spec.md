---
id: TC-GS-GSET-E2E-041-session-idle-timeout-independen-auth
title: Idle timeout independen dari Auth Session Management
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-138
coverage:
  web: automated
---

# Session Idle Timeout independen dari Auth Session Management

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Auth module (Auth Session Management) memiliki mekanisme logout otomatis sendiri yang TIDAK terhubung
  ke field ini.

## Test Steps

1. Buka `Global Settings > General Settings`
2. Verifikasi eksistensi field `Session Idle Timeout` di form General Settings
3. Ubah field tersebut menjadi nilai yang jauh berbeda dari default (misal `2 hours`)
4. Verifikasi tidak ada perubahan pada perilaku Auth (sesi tetap aktif, tidak logout paksa)
5. Verifikasi tidak ada pesan/peringatan dari Auth terkait nilai baru tersebut
6. Buka modul Auth Session Management; verifikasi nilainya tidak mengganggu/terhubung ke mekanisme
    logout otomatis di auth
7. Verifikasi sesi tetap aman: melakukan minimal satu interaksi sehat (klik navigasi) dan Auth tidak
    menutup sesi secara paksa

## Notes

- PMC `AUTH-INDEPENDENCE-CONTRACT` terpenuhi: perubahan nilai di General Settings tidak memengaruhi
  mekanisme logout otomatis Auth Session Management; keduanya independen.