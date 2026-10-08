---
id: TC-GS-POS-E2E-044-format-tanggal-general-settings
title: Format Tanggal Mengikuti General Settings
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-76
  - TC-GS-POS-198
coverage:
  web: automated
---

# Format Tanggal Mengikuti General Settings

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia konfigurasi format tanggal di General Settings (sesuai aplikasi).
- Kolom Last Updated di tabel Position dan kolom Date di Changelog menampilkan tanggal.

## Test Steps

### A. Format tanggal tabel utama mengikuti General Settings

1. Catat format tanggal yang berlaku di General Settings (atau set ke format tertentu).
2. Buka halaman `Global Settings > User > Position`.
3. Amati tampilan nilai Last Updated pada beberapa baris.
4. Verifikasi format tanggal sesuai konfigurasi General Settings (bukan hardcoded format terpisah).
5. Ubah format tanggal di General Settings (jika diuji lintas format), simpan, kembali ke tab Position.
6. Verifikasi format Last Updated ter-update mengikuti perubahan General Settings.

### B. Format tanggal Popup Changelog mengikuti General Settings

7. Buka Popup Changelog Position.
8. Amati kolom Date pada beberapa entri log.
9. Verifikasi format tanggal sesuai General Settings yang berlaku.
10. Ulangi perubahan format General Settings dan verifikasi kolom Date ter-update konsisten.

## Notes

- Seluruh tampilan tanggal (tabel utama & popup Changelog) harus mengikuti format global General Settings, bukan format lokal modul.
