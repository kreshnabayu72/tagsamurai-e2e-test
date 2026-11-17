---
id: TC-FA-MISS-E2E-035-efek-transaksi-dep-transactions-transfer
title: "Efek Missing pada Transfer: baris In transit ditutup dan pintu masuk Report Missing"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r43", "§11#r6", "§9.7#r1", "§4.2.3#b5"]
smoke: []
dependsOn: ["Transfer: halaman Transfer > aksi Report Missing"]
trace:
  "§1.2#r43": [10]
  "§11#r6": [3, 10]
  "§9.7#r1": [9, 10]
  "§4.2.3#b5": [5, 6]
anchor: []
coverage:
  web: automated
---

# Efek Missing pada Transfer: baris In transit ditutup dan pintu masuk Report Missing

## Prerequisites
- Aktor: Aktor Transfer tanpa Manage asset & TAG (Update) `Rudi Hartono {runId}`.
- Layar awal: Transfer.
- Data:
  - DU-035-1: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, tanpa pemegang, dengan baris Transfer berstatus `In transit`, tanpa record Missing.
  - DU-035-2: Pengguna `Rudi Hartono {runId}`, Aktor Transfer tanpa Manage asset & TAG (Update).
  - DU-035-3: What happened `Kendaraan tidak sampai di cabang tujuan setelah pengiriman`.
- Kondisi:
  - Akun `Rudi Hartono {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Report Missing atas baris In transit menutup baris
1. Ketik Search `Toyota Innova {runId}`, tekan Enter
2. Buka menu `⋯` pada baris `Toyota Innova {runId}`
3. Verifikasi aksi `Report Missing` tampil pada menu
4. Klik `Report Missing`
5. Verifikasi kotak dampak memuat baris `The asset admins will be notified.`
6. Verifikasi baris pratinjau penutupan baris Transfer `In transit` tidak tampil pada kotak dampak
7. Isi What happened `Kendaraan tidak sampai di cabang tujuan setelah pengiriman`
8. Klik `[Report Missing]` pada dialog
9. Verifikasi toast `Success, asset has been reported missing.` tampil
10. Verifikasi baris Transfer `Toyota Innova {runId}` tidak lagi berstatus `In transit`
