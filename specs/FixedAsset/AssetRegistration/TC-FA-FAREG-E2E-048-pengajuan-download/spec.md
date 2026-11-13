---
id: TC-FA-FAREG-E2E-048-pengajuan-download
title: "Sub tab Waiting for Approval dan History: Download"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#b8", "§5#r6"]
smoke: []
dependsOn: []
trace:
  "§4.1#b8": [5, 6, 9, 15, 16, 19]
  "§5#r6": [5, 9, 15, 19]
anchor: [2, 12]
coverage:
  web: automated
---

# Sub tab Waiting for Approval dan History: Download

## Prerequisites
- Aktor: Total Control `Dian P`, seluruh client.
- Layar awal: Assets > Registration > Waiting for Approval.
- Data:
  - DU-048-1: Pengajuan Waiting for Approval dengan Registration ID `REG-20261109-04801`, Group `Gudang Unduh Menunggu {runId}`, Total Asset `6`, Requested By `Maya L`, Last Updated `T0 − 1 hari`.
  - DU-048-2: Pengajuan History dengan Registration ID `REG-20261108-04802`, Group `Gudang Unduh Riwayat {runId}`, Total Asset `7`, Status `Approved`, Requested By `Hadi K`, Approver `Maya L`, Last Updated `T0 − 2 hari`.
  - Maya L dan Hadi K adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing; Maya L dan Hadi K bukan Total Control.

## Test Steps

### Download dari sub tab Waiting for Approval
1. Ganti isi kotak search dengan `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Unduh Menunggu {runId}`
3. Klik `[Download]`
4. Pilih `Download as CSV`
5. Verifikasi berkas `Registration-Requests` dengan ekstensi `.csv` terunduh dan memuat baris dengan Registration ID `REG-20261109-04801`
6. Verifikasi berkas `Registration-Requests` dengan ekstensi `.csv` tidak memuat baris dengan Registration ID `REG-20261108-04802`
7. Klik `[Download]`
8. Pilih `Download as XLSX`
9. Verifikasi berkas `Registration-Requests` dengan ekstensi `.xlsx` terunduh dan memuat baris dengan Registration ID `REG-20261109-04801`

### Download dari sub tab History
10. Klik sub tab `History`
11. Ganti isi kotak search dengan `{runId}`, tekan Enter
12. Verifikasi tabel sub tab History memuat baris `Gudang Unduh Riwayat {runId}`
13. Klik `[Download]`
14. Pilih `Download as CSV`
15. Verifikasi berkas `Registration-Requests` dengan ekstensi `.csv` terunduh dan memuat baris dengan Registration ID `REG-20261108-04802`
16. Verifikasi berkas `Registration-Requests` dengan ekstensi `.csv` tidak memuat baris dengan Registration ID `REG-20261109-04801`
17. Klik `[Download]`
18. Pilih `Download as XLSX`
19. Verifikasi berkas `Registration-Requests` dengan ekstensi `.xlsx` terunduh dan memuat baris dengan Registration ID `REG-20261108-04802`
