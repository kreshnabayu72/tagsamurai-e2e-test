---
id: TC-FA-FAREG-E2E-099-aset-active-dep-asset-list
title: "Aset hasil registrasi di Asset List dan Asset Detail"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-21a, §9.2#p10, §9.7#r9, EB-XM-2@asset]
smoke: []
dependsOn: ["Asset List: aset Active dan Asset Detail"]
trace:
  FAREG-LOGIC-21a: 25
  §9.2#p10: [12, 22]
  §9.7#r9: [21, 22]
  EB-XM-2@asset: 20
anchor: [9]
coverage:
  web: automated
---

# Aset hasil registrasi di Asset List dan Asset Detail

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Aktif {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-099-1: Group `Gudang Aktif {runId}`, ada di entitas aktor.
  - DU-099-2: Asset Name `Printer Aktif {runId}` dengan TAG Type `Non-TAG`, Brand `Epson`, Model `L3250`.
- Kondisi:
  - approval registrasi pada Group `Gudang Aktif {runId}` bernilai OFF.
  - sisa kuota Group dan tenant mencukupi untuk 1 aset.

## Test Steps

### Draft belum tampil di daftar aset
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Aktif {runId}`
3. Klik `[+ Asset Name]`
4. Pilih Asset Name `Printer Aktif {runId}`
5. Pilih Brand `Epson`
6. Pilih Model `L3250`
7. Isi Quantity `1`
8. Klik `[Save draft]`
9. Verifikasi subjudul form `Saved`
10. Klik tab `Assets`
11. Ketik Search `Printer Aktif {runId}`, tekan Enter
12. Verifikasi tidak ada baris aset `Printer Aktif {runId}`, empty state `No results found` tampil

### Aktivasi membuat aset Active di daftar aset
13. Buka Fixed Asset > Assets > Registration > Draft
14. Ketik Search `Gudang Aktif {runId}`, tekan Enter
15. Klik row action `Edit` pada baris batch `Gudang Aktif {runId}`
16. Klik `[Submit]`
17. Klik `[Activate]`
18. Klik tab `Assets`
19. Ketik Search `Printer Aktif {runId}`, tekan Enter
20. Verifikasi baris aset `Printer Aktif {runId}` tampil di daftar
21. Verifikasi Lifecycle aset `Active`
22. Verifikasi Purchase aset `Pending`

### Log aset di Asset Detail
23. Klik row action `Detail` pada baris aset `Printer Aktif {runId}`
24. Buka bagian log aset
25. Verifikasi entri log dengan Action `Activate`, Field `Status`, Old Value `Draft`, dan New Value `Active` tampil
