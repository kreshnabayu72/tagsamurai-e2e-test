---
id: TC-FA-ASTL-E2E-040-status-assignment-dep-assignment
title: "Status Assignment dan pintasan Assign"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#r1"]
smoke: []
dependsOn: ["Assignment: transaksi Assignment"]
trace:
  "§9.7#r1": [4, 5, 7]
anchor: [2]
coverage:
  web: automated
---

# Status Assignment dan pintasan Assign

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-040-1: aset `Printer Laser {runId} - 1`, Group `IT`, managed, Custody `Available`.

## Test Steps

### Status Assignment tercermin di daftar
1. Ketik Search `Printer Laser {runId}`, tekan Enter
2. Verifikasi baris `Printer Laser {runId} - 1` menampilkan `Available`
3. Pada modul Assignment, Hendra Saputra menyelesaikan Assignment aset `Printer Laser {runId} - 1` kepada seorang assignee, tanpa memuat ulang halaman Fixed Asset > Assets
4. Verifikasi badge Status baris `Printer Laser {runId} - 1` berubah menjadi `Assigned` dan `Available` tidak lagi tampil
5. Verifikasi angka kartu `In Transaction` menjadi `1` karena Search hanya memuat aset ini
6. Pada modul Assignment, Hendra Saputra menjalankan Unassign atas aset `Printer Laser {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
7. Verifikasi badge Status baris `Printer Laser {runId} - 1` kembali menjadi `Available`
