---
id: TC-FA-FAFM-E2E-036-gating-manage-files-delete-permanently
title: "Manage files Delete: Permanently Delete pada group yang di-assign"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-AKS-5@permanently-delete-file"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-5@permanently-delete-file": [3, 4, 6, 9, 11]
anchor: [10]
coverage:
  web: automated
---

# Manage files Delete: Permanently Delete pada group yang di-assign

## Prerequisites
- Aktor: Eka Penghapus Permanen `{runId}` (pemegang capability Group Role Manage files dengan Delete saja, di-assign pada group `Fleet`).
- Layar awal: Settings > File Manager, tab Kategori `Asset Photo` aktif.
- Data:
  - DU-036-1: User `Eka Penghapus Permanen {runId}`, role `Pengelola File Fleet Hapus {runId}`, capability `Manage files: Delete`, group yang di-assign `Fleet`.
  - DU-036-2: File `foto-bin-derek-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Derek Armada {runId}` (Increment dibentuk server), Group `Fleet`, Size `640.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 2 hari, pukul 14:00`, ada di Recycle Bin; dihapus permanen oleh spec ini.
  - DU-036-3: File `foto-bin-tangki-{runId}.jpg`, File Format `JPG`, Category `Asset Photo`, Source `Asset Photo`, Asset `Tangki BBM {runId}` (Increment dibentuk server), Group `Fleet`, Size `520.0 KB`, Deleted By `Rina A`, Deleted Date `T0 − 3 hari, pukul 16:20`, ada di Recycle Bin.

## Test Steps

### Permanently Delete atas file di group yang di-assign
1. Klik `Recycle Bin` pada header kartu Storage Usage
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `foto-bin-derek-{runId}.jpg` tampil pada Recycle Bin
4. Verifikasi baris `foto-bin-tangki-{runId}.jpg` tampil pada Recycle Bin
5. Klik `⋯` pada baris `foto-bin-derek-{runId}.jpg`
6. Verifikasi menu baris memuat `Permanently Delete`
7. Klik `Permanently Delete`
8. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
9. Verifikasi toast `Success, [File Name] has been permanently deleted.` tampil dengan File Name `foto-bin-derek-{runId}.jpg`
10. Verifikasi baris `foto-bin-tangki-{runId}.jpg` tetap tampil pada Recycle Bin
11. Verifikasi baris `foto-bin-derek-{runId}.jpg` tidak ada pada Recycle Bin
