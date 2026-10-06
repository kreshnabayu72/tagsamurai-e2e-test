---
id: TC-GS-GSET-E2E-003-state-form-seed-default-dan-populated
title: State awal form seed default vs nilai tersimpan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-03
  - TC-GS-GSET-04
coverage:
  web: automated
---

# State awal form: seed default vs nilai tersimpan

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Skenario A menggunakan environment dengan footer status menampilkan `N/A` dan tidak ada mutasi riil.
  form belum pernah disimpan.
- Skenario B menggunakan `Fixture.globalSettingsGeneralSettings.data.existing` sebagai data tersimpan:
  `currency: IDR (Rp - Indonesian Rupiah)`, `timeZone: (UTC+07:00) Bangkok, Hanoi, Jakarta`,
  `sessionIdleTimeout: "30 minutes"`, `dateFormat: "dd/MM/yy"`, `timeFormat: "HH:mm"`.

## Test Steps

### Skenario A: form pernah disimpan, tampil last saved values

1. Sebelum melihat halaman, set state via hook agar record General Settings bernilai seperti `existing`
2. Buka halaman `Global Settings > General Settings`
3. Verifikasi `Currency` menampilkan `Rp - Indonesian Rupiah`
4. Verifikasi `Time Zone` menampilkan `(UTC+07:00) Bangkok, Hanoi, Jakarta`
5. Verifikasi `Session Idle Timeout` menampilkan `30 minutes`
6. Verifikasi `Date Format` menampilkan `dd/MM/yy`
7. Verifikasi `Time Format` menampilkan `HH:mm`
8. Verifikasi footer status menampilkan waktu penyimpanan record terakhir
9. Verifikasi tombol `[Save]` tidak dapat diklik (tidak ada perubahan)

### Skenario B: form belum pernah diubah, tampil seed default

10. Set state via hook agar record General Settings bernilai seed awal: `Currency` kosong,
    `Session Idle Timeout` = `15 minutes`, `Time Zone` = `(UTC+07:00) Bangkok, Hanoi, Jakarta`,
    `Date Format` = `dd/MM/yy`, `Time Format` = `HH:mm`
11. Buka (ulang) halaman `Global Settings > General Settings`
12. Verifikasi field `Currency` menampilkan keterangan bahwa belum ada currency dipilih
13. Verifikasi `Session Idle Timeout` menampilkan `15 minutes`
14. Verifikasi `Time Zone` menampilkan `(UTC+07:00) Bangkok, Hanoi, Jakarta`
15. Verifikasi `Date Format` menampilkan `dd/MM/yy` dan `Time Format` menampilkan `HH:mm`
16. Verifikasi state tabel-baru: seluruh nilai yang berbeda dari seed dianggap sebagai perubahan yang
    butuh simpan

## Notes

- PRD §4.1 menyatakan record single dibuat otomatis (`auto-created`) saat halaman diakses; spec ini
  membuktikan state default dan state populated sebagai dua representasi dari record yang sama.
- Perilaku "save dibutuhkan saat beda dari seed" dijembatani ke spec 010 (state tombol Save).