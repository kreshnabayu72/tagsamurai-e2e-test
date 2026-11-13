---
id: TC-FA-FAREG-E2E-119-format-tanggal-dep-general-settings
title: "Format tanggal mengikuti General Settings"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [EB-XM-1]
smoke: []
dependsOn: ["General Settings: Date Format dan Time Format"]
trace:
  EB-XM-1: [2, 5, 8]
anchor: []
coverage:
  web: automated
---

# Format tanggal mengikuti General Settings

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Format {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang mengubah Date Format di General Settings.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-119-1: Group `Gudang Format {runId}`, ada di entitas aktor.
  - DU-119-2: batch Draft `Gudang Format {runId}` berisi 1 Item Asset Name `Rak Format {runId}` dengan TAG Type `Non-TAG`, Brand `Olympic`, Model `No Model`, Quantity `1`, dengan Last Updated `T0`.
  - DU-119-3: Date Format General Settings `dd/MM/yy` dengan Time Format 24 jam, diubah menjadi `dd MMM yy` lalu dikembalikan.
- Kondisi:
  - Date Format General Settings `dd/MM/yy` dan Time Format 24 jam saat spec dimulai.
  - Date Format diubah menjadi `dd MMM yy` oleh langkah 3 dan dikembalikan menjadi `dd/MM/yy` oleh langkah 6.

## Test Steps

### Last Updated memakai format General Settings saat ini
1. Ketik Search `Gudang Format {runId}`, tekan Enter
2. Verifikasi Last Updated baris batch `Gudang Format {runId}` memakai Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Perubahan Date Format sampai ke tabel Draft
3. Admin mengubah Date Format di General Settings menjadi `dd MMM yy`
4. Muat ulang halaman
5. Verifikasi Last Updated baris batch `Gudang Format {runId}` memakai Date Format `dd MMM yy` diikuti Time Format 24 jam

### Date Format dikembalikan
6. Admin mengembalikan Date Format di General Settings menjadi `dd/MM/yy`
7. Muat ulang halaman
8. Verifikasi Last Updated baris batch `Gudang Format {runId}` memakai Date Format `dd/MM/yy` diikuti Time Format 24 jam
