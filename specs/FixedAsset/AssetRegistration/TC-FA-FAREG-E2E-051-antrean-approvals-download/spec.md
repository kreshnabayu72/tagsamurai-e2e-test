---
id: TC-FA-FAREG-E2E-051-antrean-approvals-download
title: "Antrean Approvals: Download"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.5#b3", "§5#r6"]
smoke: []
dependsOn: []
trace:
  "§4.2.5#b3": [5, 6, 9, 13, 16, 24, 25, 28]
  "§5#r6": [5, 9, 24, 28]
anchor: [2, 21]
coverage:
  web: automated
---

# Antrean Approvals: Download

## Prerequisites
- Aktor: Total Control `Dian P`, seluruh client, bukan pengaju satu pun pengajuan data uji.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-051-1: Pengajuan Waiting for Approval dengan Registration ID `REG-20261109-05101`, Group `Gudang Unduh Aktif {runId}`, Total Asset `6`, Requested By `Hadi K.`, Last Updated `T0 − 1 hari`.
  - DU-051-2: Pengajuan Waiting for Approval dengan Registration ID `REG-20261108-05102`, Group `Gudang Unduh Aktif Dua {runId}`, Total Asset `9`, Requested By `Siti N`, Last Updated `T0 − 2 hari`.
  - DU-051-3: Pengajuan History dengan Registration ID `REG-20261107-05103`, Group `Gudang Unduh Riwayat {runId}`, Total Asset `7`, Status `Approved`, Requested By `Rina W`, Approver `Maya L`, Last Updated `T0 − 3 hari`.
  - Hadi K, Siti N, Rina W, dan Maya L adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing.

## Test Steps

### Download dari tab Active mengikuti Search
1. Ganti isi kotak search dengan `{runId}`, tekan Enter
2. Verifikasi tabel tab Active memuat baris `Gudang Unduh Aktif {runId}` dan `Gudang Unduh Aktif Dua {runId}`
3. Klik `[Download]`
4. Pilih `Download as CSV`
5. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.csv` terunduh dan memuat baris dengan Registration ID `REG-20261109-05101` dan `REG-20261108-05102`
6. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.csv` tidak memuat baris dengan Registration ID `REG-20261107-05103`
7. Klik `[Download]`
8. Pilih `Download as XLSX`
9. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.xlsx` terunduh dan memuat baris dengan Registration ID `REG-20261109-05101` dan `REG-20261108-05102`

### Download dari tab Active mengikuti Filter
10. Klik ikon Filter
11. Pilih opsi `Hadi K.` pada field `Requested By`[^drift-1]
12. Klik `[Apply]`
13. Verifikasi tabel tab Active memuat baris `Gudang Unduh Aktif {runId}` dan tidak memuat baris `Gudang Unduh Aktif Dua {runId}`
14. Klik `[Download]`
15. Pilih `Download as CSV`
16. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.csv` memuat baris dengan Registration ID `REG-20261109-05101` dan tidak memuat baris dengan Registration ID `REG-20261108-05102`
17. Klik `[Clear Field]`
18. Klik `[Apply]`

### Download dari tab History
19. Klik tab `History`
20. Ganti isi kotak search dengan `{runId}`, tekan Enter
21. Verifikasi tabel tab History memuat baris `Gudang Unduh Riwayat {runId}`
22. Klik `[Download]`
23. Pilih `Download as CSV`
24. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.csv` terunduh dan memuat baris dengan Registration ID `REG-20261107-05103`
25. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.csv` tidak memuat baris dengan Registration ID `REG-20261109-05101`
26. Klik `[Download]`
27. Pilih `Download as XLSX`
28. Verifikasi berkas `Approvals-Registration` dengan ekstensi `.xlsx` terunduh dan memuat baris dengan Registration ID `REG-20261107-05103`

[^drift-1]: Drift PRD vs foundation vs override. PRD §4.1 kolom Requested By: `Nama singkat`. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).
