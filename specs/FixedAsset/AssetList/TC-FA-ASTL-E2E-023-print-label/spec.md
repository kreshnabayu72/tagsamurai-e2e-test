---
id: TC-FA-ASTL-E2E-023-print-label
title: "Print Label dari toolbar dan Row Action"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["DO-01", "F-ASTL-15.k1", "§4.1h#p1", "§4.1h#b13", "§4.1h#b14", "§9.2#p9", "§9.6#r5", "EB-FB-1@print-label"]
smoke: ["EB-FB-1@print-label"]
dependsOn: []
trace:
  "DO-01": [10, 19]
  "F-ASTL-15.k1": 8
  "§4.1h#p1": [10, 23, 29]
  "§4.1h#b13": [7, 23, 29]
  "§4.1h#b14": 14
  "§9.2#p9": 8
  "§9.6#r5": [12, 14, 25, 31]
  "EB-FB-1@print-label": 12
anchor: []
coverage:
  web: automated
---
# Print Label dari toolbar dan Row Action

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-023-1: aset Active managed, Asset Name `Laptop Pro 16 {runId}`, tampil `Laptop Pro 16 {runId} - 1`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-023-2: aset Active managed, Asset Name `Proyektor X2 {runId}`, tampil `Proyektor X2 {runId} - 1`, Brand `Epson`, Model/Type `EB-X06`, Category `Peralatan Presentasi`, Group `Kantor Pusat {runId}`, Status `Available`.
  - DU-023-3: aset Disposed, Asset Name `Genset 20kVA {runId}`, tampil `Genset 20kVA {runId} - 1`, Brand `Perkins`, Model/Type `403A-15G2`, Category `Peralatan Listrik`, Group `Kantor Pusat {runId}`, Status `Disposed`.
  - DU-023-4: aset Active Unmanaged, Asset Name `Kamera Mirrorless {runId}`, tampil `Kamera Mirrorless {runId} - 1`, Brand `Sony`, Model/Type `A6400`, Category `Peralatan Foto`, Group `Kantor Pusat {runId}`, Status `Available, Unmanaged`.
  - DU-023-5: Group `Kantor Pusat {runId}`.

## Test Steps

### Pintu toolbar lewat dialog Select Asset
1. Ketik Search `{runId}`, tekan Enter
2. Klik ikon `Changelog` pada toolbar
3. Catat entri Changelog teratas
4. Tutup modal Changelog
5. Centang baris `Laptop Pro 16 {runId} - 1`
6. Klik tombol `Print Label` pada toolbar
7. Verifikasi dialog `Select Asset` memuat `Laptop Pro 16 {runId} - 1` dan `Proyektor X2 {runId} - 1`
8. Verifikasi dialog `Select Asset` tidak memuat `Kamera Mirrorless {runId} - 1` (Unmanaged) maupun `Genset 20kVA {runId} - 1` (Disposed)
9. Klik `[Select]`
10. Verifikasi dialog `Print Label` tampil dan memuat `Selected asset: 1 asset`
11. Klik `[Start Print]`
12. Verifikasi toast `Success, label has been sent to print.` tampil
13. Klik ikon `Changelog` pada toolbar
14. Verifikasi Changelog tidak memuat entri baru untuk `Laptop Pro 16 {runId} - 1` karena mencetak label tidak mengubah data aset
15. Tutup modal Changelog

### Select tanpa aset terpilih
16. Klik `×` pada Bar Bulk untuk melepas seluruh seleksi tabel
17. Klik tombol `Print Label` pada toolbar
18. Klik `[Select]`
19. Verifikasi teks `You must pick an asset` tampil dan dialog `Select Asset` tidak tertutup
20. Klik `[Cancel]`

### Pintu Row Action melewati Select Asset
21. Klik menu `⋯` pada baris `Proyektor X2 {runId} - 1`
22. Pilih `Print Label`
23. Verifikasi dialog `Print Label` langsung tampil dan memuat `Selected asset: 1 asset`, tanpa dialog `Select Asset`
24. Klik `[Start Print]`
25. Verifikasi toast `Success, label has been sent to print.` tampil

### Pintu Bulk Action melewati Select Asset
26. Centang baris `Laptop Pro 16 {runId} - 1` dan baris `Proyektor X2 {runId} - 1`
27. Klik `Bulk Action`
28. Pilih `Print Label`
29. Verifikasi dialog `Print Label` langsung tampil dan memuat `Selected asset: 2 assets`, tanpa dialog `Select Asset`
30. Klik `[Start Print]`
31. Verifikasi toast `Success, labels have been sent to print.` tampil
