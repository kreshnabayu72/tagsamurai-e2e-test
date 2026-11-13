---
id: TC-FA-FAREG-E2E-109-asset-label-default-dan-arsip-dep-settings-asset-labeling
title: "Asset Label default dan Asset Label yang diarsipkan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-08f, FAREG-LOGIC-16d]
smoke: []
dependsOn: ["Settings Asset Labeling: master Asset Label"]
trace:
  FAREG-LOGIC-16d: [10, 11, 13, 15]
  FAREG-LOGIC-08f: [22, 24]
anchor: []
coverage:
  web: automated
---

# Asset Label default dan Asset Label yang diarsipkan

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Label {runId}` dan `Gudang Label Arsip {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu pengarsipan Asset Label.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-109-1: Group `Gudang Label {runId}`, ada di entitas aktor.
  - DU-109-2: Group `Gudang Label Arsip {runId}`, ada di entitas aktor.
  - DU-109-3: Asset Name `Router Label {runId}` dengan TAG Type `Non-TAG`, Brand `Cisco`, Model `ISR 4331`, dan Asset Label default `Label Default {runId}`.
  - DU-109-4: Asset Label `Label Umum {runId}`, bukan default, ada di master Asset Label.
  - DU-109-5: Asset Label `Label Arsip {runId}`, ada di master Asset Label.
  - DU-109-6: batch Draft `Gudang Label Arsip {runId}` berisi 1 Item Asset Name `Switch Label {runId}` dengan TAG Type `Non-TAG`, Brand `Cisco`, Model `Catalyst 9200`, Quantity `1`, dan Asset labels `Label Arsip {runId}` terpilih.

## Test Steps

### Asset Label default ditempel otomatis dan tidak dapat dilepas
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Label {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Router Label {runId}`
5. Pilih Brand `Cisco`
6. Pilih Model `ISR 4331`
7. Isi Quantity `1`
8. Klik tab `Asset`
9. Klik row action `Detail` pada baris aset pertama
10. Verifikasi Asset labels memuat `Label Default {runId}`
11. Verifikasi tombol lepas pada `Label Default {runId}` tidak tampil
12. Pilih Asset labels `Label Umum {runId}`
13. Verifikasi Asset labels memuat `Label Umum {runId}` dan `Label Default {runId}`
14. Lepas Asset label `Label Umum {runId}`
15. Verifikasi Asset labels hanya memuat `Label Default {runId}`

### Asset Label yang diarsipkan dilepas dari draft dengan peringatan
16. Klik `[Cancel]`
17. Klik `[Leave]` pada dialog Unsaved Changes
18. Admin mengarsipkan Asset Label `Label Arsip {runId}`
19. Ketik Search `Gudang Label Arsip {runId}`, tekan Enter
20. Klik row action `Edit` pada baris batch `Gudang Label Arsip {runId}`
21. Klik tab `Asset`
22. Verifikasi `Alert` Warning tampil di atas form
23. Klik row action `Detail` pada baris aset pertama
24. Verifikasi Asset labels tidak lagi memuat `Label Arsip {runId}`
