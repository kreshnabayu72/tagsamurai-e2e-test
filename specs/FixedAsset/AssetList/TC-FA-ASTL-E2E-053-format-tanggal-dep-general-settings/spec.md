---
id: TC-FA-ASTL-E2E-053-format-tanggal-dep-general-settings
title: "Format tanggal tercermin di tabel"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-XM-1"]
smoke: []
dependsOn: ["General Settings: format tanggal"]
trace:
  "EB-XM-1": [3, 7, 8, 13, 14]
anchor: [2]
coverage:
  web: automated
---

# Format tanggal tercermin di tabel

## Prerequisites
- Aktor: Admin Format `{runId}`, Total Control dengan cakupan seluruh entitas khusus ini.
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-053-1: entitas khusus `Entitas Format Tanggal {runId}` yang tidak dipakai spec lain, dengan Date Format `dd/MM/yy` dan Time Format `24h`.
  - DU-053-2: aset `Printer Laser {runId}` yang tampil sebagai `Printer Laser {runId} - 1`, Group `GA`, Register Date hari ini, ada di entitas khusus ini.
  - DU-053-3: Date Format hasil ubah `dd MMM yy`, dari `dd/MM/yy`.
  - DU-053-4: Time Format hasil ubah `12h`, dari `24h`, dan Time Zone hasil ubah ke zona dengan selisih jam bulat dari Time Zone semula.

## Test Steps

### Format tanggal tabel mengikuti General Settings
1. Ketik Search `Printer Laser {runId}`, tekan Enter
2. Verifikasi baris `Printer Laser {runId} - 1` tampil pada tabel
3. Verifikasi kolom `Register Date` dan `Last Updated` baris `Printer Laser {runId} - 1` menampilkan tanggal dalam Date Format `dd/MM/yy`, dengan `Last Updated` diikuti Time Format `24h`
4. Pada Global Settings > General Settings, ubah Date Format menjadi `dd MMM yy`
5. Muat ulang halaman Fixed Asset > Assets
6. Ketik Search `Printer Laser {runId}`, tekan Enter
7. Verifikasi kolom `Register Date` baris `Printer Laser {runId} - 1` menampilkan tanggal dalam Date Format `dd MMM yy`
8. Verifikasi kolom `Last Updated` baris `Printer Laser {runId} - 1` menampilkan tanggal dalam Date Format `dd MMM yy` diikuti Time Format `24h`

### Time Format 12h dan Time Zone
9. Catat jam `Last Updated` baris `Printer Laser {runId} - 1` dalam Time Format `24h`
10. Pada Global Settings > General Settings, ubah Time Format menjadi `12h` dan Time Zone ke zona lain
11. Muat ulang halaman Fixed Asset > Assets
12. Ketik Search `Printer Laser {runId}`, tekan Enter
13. Verifikasi kolom `Last Updated` baris `Printer Laser {runId} - 1` menampilkan waktu dalam Time Format `12h` (dengan penanda AM atau PM)
14. Verifikasi waktu pada kolom `Last Updated` bergeser sebesar selisih jam antara Time Zone semula dan Time Zone baru dibanding jam yang dicatat
