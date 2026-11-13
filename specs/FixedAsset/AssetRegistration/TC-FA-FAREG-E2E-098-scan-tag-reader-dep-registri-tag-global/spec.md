---
id: TC-FA-FAREG-E2E-098-scan-tag-reader-dep-registri-tag-global
title: "Scan TAG dengan reader: Verified dan status Tag di registri"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-04h, §9.7#r6, §9.4.2#r30, §9.4.2#r31, S-REG-18]
smoke: [§9.4.2#r30, §9.4.2#r31, S-REG-18]
dependsOn: ["Registri Tag Global: status Tag"]
trace:
  FAREG-LOGIC-04h: [15, 28]
  §9.7#r6: [11, 15, 28]
  §9.4.2#r30: [11, 15]
  §9.4.2#r31: [22, 26, 28]
  S-REG-18: [11, 22]
anchor: []
coverage:
  web: manual
---

# Scan TAG dengan reader: Verified dan status Tag di registri

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Scan {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-098-1: Group `Gudang Scan {runId}`, ada di entitas aktor.
  - DU-098-2: Asset Name `Laptop Scan {runId}` dengan TAG Type `RFID`, Brand `Dell`, Model `Latitude 5440`.
  - DU-098-3: Tag `E280-0098-A1-{runId}` berstatus `Available` di registri Global.
  - DU-098-4: Tag `E280-0098-B2-{runId}` berstatus `Available` di registri Global.
- Kondisi:
  - reader TAG terhubung ke perangkat aktor dan Tag fisik tersedia di dekatnya.
  - approval registrasi pada Group `Gudang Scan {runId}` bernilai OFF.

## Test Steps

### Scan Tag pada aset tanpa Tag
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Scan {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Laptop Scan {runId}`
5. Pilih Brand `Dell`
6. Pilih Model `Latitude 5440`
7. Isi Quantity `1`
8. Klik tab `Asset`
9. Klik `Scan RFID`
10. Pindai Tag `E280-0098-A1-{runId}` dengan reader
11. Verifikasi Badge `Verified` tampil pada kolom TAG aset
12. Klik `[Save draft]`
13. Buka Registri Tag Global
14. Ketik Search `E280-0098-A1-{runId}`, tekan Enter
15. Verifikasi status Tag `E280-0098-A1-{runId}` adalah `Reserved`

### Rescan mengganti Tag dan melepas Tag lama
16. Buka Fixed Asset > Assets > Registration > Draft
17. Ketik Search `Gudang Scan {runId}`, tekan Enter
18. Klik row action `Edit` pada baris batch `Gudang Scan {runId}`
19. Klik tab `Asset`
20. Klik `Scan RFID`
21. Pindai Tag `E280-0098-B2-{runId}` dengan reader
22. Verifikasi Badge `Verified` tampil pada kolom TAG aset
23. Klik `[Save draft]`
24. Buka Registri Tag Global
25. Ketik Search `E280-0098-A1-{runId}`, tekan Enter
26. Verifikasi status Tag `E280-0098-A1-{runId}` kembali `Available`
27. Ganti isi kotak search dengan `E280-0098-B2-{runId}`, tekan Enter
28. Verifikasi status Tag `E280-0098-B2-{runId}` adalah `Reserved`
