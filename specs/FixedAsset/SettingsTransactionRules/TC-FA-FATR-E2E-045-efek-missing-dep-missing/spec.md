---
id: TC-FA-FATR-E2E-045-efek-missing-dep-missing
title: "Long missing after berlaku di Missing"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-XM-2@missing", "§4.1#r158", "§11#r17"]
smoke: ["§4.1#r158", "§11#r17"]
dependsOn:
  - "Missing: penanda Long missing dan Mark as Found"
trace:
  "EB-XM-2@missing": 11
  "§4.1#r158": [4, 11]
  "§11#r17": [11, 12]
anchor: [3]
coverage:
  web: automated
---

# Long missing after berlaku di Missing

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update), di entitas khusus yang tidak dipakai spec lain.
- Layar awal: Fixed Asset > Missing
- Data:
  - DU-045-1: Entitas Name `Entitas Missing {runId}`, Long missing after `30`; entitas khusus spec ini dengan Long missing after bernilai 30.
  - DU-045-2: Asset Name `Projector Epson EB-X5 {runId}`, Condition `Missing`, Missing since `T0 − 20 hari`; aset Missing sejak 20 hari lalu.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Missing {runId}` yang tidak dipakai spec lain, karena yang diubah adalah setting tingkat entitas.
  - Long missing after bernilai `30` di entitas khusus ini.

## Test Steps

### Long missing after diperkecil memunculkan penanda Long missing
1. Masuk sebagai Default User
2. Buka daftar aset Missing
3. Verifikasi aset `Projector Epson EB-X5 {runId}` tampil di daftar Missing
4. Verifikasi penanda Long missing tidak tampil pada aset `Projector Epson EB-X5 {runId}`
5. Buka tab yang memuat field Long missing after pada node All categories di Fixed Asset > Settings > Transaction Settings
6. Isi Long missing after dengan `10`
7. Klik `[Save]`
8. Klik `[Save]` pada dialog Save Changes
9. Job harian Long missing berjalan
10. Buka daftar aset Missing
11. Verifikasi penanda Long missing tampil pada aset `Projector Epson EB-X5 {runId}` sesuai nilai baru Long missing after `10`
12. Verifikasi saran Report disposal tampil pada aset `Projector Epson EB-X5 {runId}`
