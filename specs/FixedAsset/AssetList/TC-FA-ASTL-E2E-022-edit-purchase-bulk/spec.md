---
id: TC-FA-ASTL-E2E-022-edit-purchase-bulk
title: "Bulk Edit Purchase tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-07d", "ASTL-LOGIC-07e"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-07d": [12, 14]
  "ASTL-LOGIC-07e": [21, 23]
anchor: []
coverage:
  web: automated
---
# Bulk Edit Purchase tersimpan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-022-1: aset Active Purchase `Complete`, Asset Name `Monitor Samsung {runId}`, tampil `Monitor Samsung {runId} - 1`, Brand `Samsung`, Model/Type `S24R350`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, Purchase Date `T0 − 90 hari`, Purchase Cost `5000000`, tampil `Rp 5.000.000,00`.
  - DU-022-2: aset Active Purchase `Complete`, Asset Name `Monitor LG {runId}`, tampil `Monitor LG {runId} - 1`, Brand `LG`, Model/Type `24MK600`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, Purchase Date `T0 − 90 hari`, Purchase Cost `5000000`.
  - DU-022-3: aset Active Purchase `Complete`, Asset Name `Monitor Dell {runId}`, tampil `Monitor Dell {runId} - 1`, Brand `Dell`, Model/Type `P2422H`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, Purchase Date `T0 − 90 hari`, Purchase Cost `7000000`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.

## Test Steps

### Bulk yang tidak mengubah nilai pada aset mana pun
1. Ketik Search `{runId}`, tekan Enter
2. Buka Setup Column lewat menu `⋯` pada header tabel
3. Centang kolom `Purchase Cost`
4. Centang baris `Monitor Samsung {runId} - 1` dan baris `Monitor LG {runId} - 1`
5. Klik ikon `Changelog` pada toolbar
6. Catat entri Changelog teratas
7. Tutup modal Changelog
8. Klik `Bulk Action`
9. Pilih `Edit Purchase`
10. Isi `Purchase Cost (per asset)` dengan `5000000`
11. Klik `[Save]`
12. Verifikasi toast `No changes to save.` tampil karena kedua aset sudah bernilai Purchase Cost `5000000`
13. Klik ikon `Changelog` pada toolbar
14. Verifikasi Changelog tidak memuat entri baru untuk `Monitor Samsung {runId} - 1` maupun `Monitor LG {runId} - 1`
15. Tutup modal Changelog

### Bulk yang hanya mengubah sebagian aset
16. Centang baris `Monitor Samsung {runId} - 1` dan baris `Monitor Dell {runId} - 1`
17. Klik `Bulk Action`
18. Pilih `Edit Purchase`
19. Isi `Purchase Cost (per asset)` dengan `5000000`
20. Klik `[Save]`
21. Verifikasi toast `Success, purchase data has been saved.` tampil dan Purchase Cost `Rp 5.000.000,00` tampil pada baris `Monitor Dell {runId} - 1`
22. Klik ikon `Changelog` pada toolbar
23. Verifikasi Changelog memuat tepat satu entri baru field `Purchase Cost` untuk `Monitor Dell {runId} - 1` dan tanpa entri baru untuk `Monitor Samsung {runId} - 1`
24. Tutup modal Changelog
