---
id: TC-FA-FATR-E2E-055-efek-general-settings-dep-general-settings
title: "Tanggal mengikuti Date Format dan Time Format General Settings"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-XM-1"]
smoke: []
dependsOn:
  - "General Settings: Date Format dan Time Format"
trace:
  "EB-XM-1": [9, 11, 14, 16, 24, 26]
anchor: [3, 5]
coverage:
  web: automated
---

# Tanggal mengikuti Date Format dan Time Format General Settings

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan dapat mengubah General Settings, di entitas khusus yang tidak dipakai spec lain.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-055-1: Entitas Name `Entitas Format Tanggal {runId}`, Date Format `dd/MM/yy`, Time Format `24h`, Time Zone `UTC+07:00`; entitas khusus spec ini dengan Date Format dd/MM/yy, Time Format 24h, dan Time Zone UTC+07:00.
  - DU-055-2: Category Name `Lighting Fixtures {runId}`; Category leaf tempat override dibuat.
  - DU-055-3: Group Name `Lighting Team {runId}`; Group target override.
  - DU-055-4: Override Target `Lighting Team {runId}`, Scope `Group`, Category `Lighting Fixtures {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Group yang barisnya menampilkan Created At.
  - DU-055-5: Changelog Category `Lighting Fixtures {runId}`, Field `Borrow (Max duration)`, Old `14 Days`, New `12 Days`; entri Changelog dengan kolom Date.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Format Tanggal {runId}` yang tidak dipakai spec lain, karena yang diubah adalah setting tingkat entitas.
  - Date Format bernilai `dd/MM/yy`, Time Format bernilai `24h`, dan Time Zone bernilai `UTC+07:00` di entitas khusus ini.

## Test Steps
### Perubahan Date Format di General Settings sampai ke kolom tanggal halaman ini
1. Masuk sebagai Default User
2. Buka tab `Borrow` pada node Category `Lighting Fixtures {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi kolom Created At baris override untuk `Lighting Team {runId}` tampil menurut Date Format `dd/MM/yy` ditambah Time Format `24h`
4. Buka dialog Changelog dari header halaman Transaction Settings
5. Verifikasi kolom Date entri Changelog untuk Category `Lighting Fixtures {runId}` tampil menurut Date Format `dd/MM/yy` ditambah Time Format `24h`
6. Tutup dialog Changelog
7. Ubah Date Format di General Settings menjadi `dd MMM yy`
8. Buka tab `Borrow` pada node Category `Lighting Fixtures {runId}` di Fixed Asset > Settings > Transaction Settings
9. Verifikasi kolom Created At baris override untuk `Lighting Team {runId}` tampil menurut Date Format `dd MMM yy` ditambah Time Format `24h`
10. Buka dialog Changelog dari header halaman Transaction Settings
11. Verifikasi kolom Date entri Changelog untuk Category `Lighting Fixtures {runId}` tampil menurut Date Format `dd MMM yy` ditambah Time Format `24h`

### Perubahan Time Format di General Settings sampai ke kolom tanggal halaman ini
12. Ubah Time Format di General Settings menjadi `12h`
13. Buka tab `Borrow` pada node Category `Lighting Fixtures {runId}` di Fixed Asset > Settings > Transaction Settings
14. Verifikasi kolom Created At baris override untuk `Lighting Team {runId}` tampil menurut Date Format `dd MMM yy` ditambah Time Format `12h`
15. Buka dialog Changelog dari header halaman Transaction Settings
16. Verifikasi kolom Date entri Changelog untuk Category `Lighting Fixtures {runId}` tampil menurut Date Format `dd MMM yy` ditambah Time Format `12h`
17. Tutup dialog Changelog

### Perubahan Time Zone di General Settings sampai ke kolom tanggal halaman ini
18. Catat waktu pada kolom Created At baris override untuk `Lighting Team {runId}`
19. Buka dialog Changelog dari header halaman Transaction Settings
20. Catat waktu pada kolom Date entri Changelog untuk Category `Lighting Fixtures {runId}`
21. Tutup dialog Changelog
22. Ubah Time Zone di General Settings menjadi `UTC+06:00`, 1 jam lebih awal dari `UTC+07:00`
23. Buka tab `Borrow` pada node Category `Lighting Fixtures {runId}` di Fixed Asset > Settings > Transaction Settings
24. Verifikasi waktu pada kolom Created At baris override untuk `Lighting Team {runId}` tampil 1 jam lebih awal dari waktu yang dicatat, menurut Time Zone baru entitas
25. Buka dialog Changelog dari header halaman Transaction Settings
26. Verifikasi waktu pada kolom Date entri Changelog untuk Category `Lighting Fixtures {runId}` tampil 1 jam lebih awal dari waktu yang dicatat, menurut Time Zone baru entitas
