---
id: TC-FA-FAFM-E2E-025-permanently-delete-single
title: "Permanently Delete satu file dari Recycle Bin"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-05d, ACT-05e, D-03, F-FAFM-03d, INV-05g, INV-06c, S-22, T-06, "§4.4#b10", "EB-FB-1@permanently-delete-file"]
smoke: ["EB-FB-1@permanently-delete-file"]
dependsOn: []
trace:
  ACT-05d: [13, 18]
  ACT-05e: 12
  D-03: 6
  F-FAFM-03d: [13, 18]
  INV-05g: 13
  INV-06c: 18
  S-22: 12
  T-06: 12
  "§4.4#b10": 13
  "EB-FB-1@permanently-delete-file": 12
anchor: [3, 8, 17]
coverage:
  web: automated
  android: automated
---

# Permanently Delete satu file dari Recycle Bin

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-025-1: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-025-2: File di Recycle Bin `laptop-old-{runId}.png`, Source `Asset Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-025-3: Aset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-025-4: File di Recycle Bin `repair-02-{runId}.jpg`, Source `Repair Photo`, Size `120.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`.
  - Toast yang diharapkan `Success, laptop-old-{runId}.png has been permanently deleted.`, dari Name file DU-025-2.

## Test Steps

### Permanently Delete dibatalkan lalu dikonfirmasi
1. Buka Recycle Bin
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi file `laptop-old-{runId}.png` dan `repair-02-{runId}.jpg` tampil di Recycle Bin
4. Buka aksi baris `laptop-old-{runId}.png`
5. Klik `Permanently Delete`
6. Verifikasi dialog `Permanently Delete File` memuat bullet nama file `laptop-old-{runId}.png`
7. Tutup dialog konfirmasi dengan Cancel
8. Verifikasi file `laptop-old-{runId}.png` masih tampil di Recycle Bin
9. Buka aksi baris `laptop-old-{runId}.png`
10. Klik `Permanently Delete`
11. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
12. Verifikasi toast `Success, laptop-old-{runId}.png has been permanently deleted.` tampil
13. Verifikasi file `laptop-old-{runId}.png` tidak tampil lagi di Recycle Bin

### Penghapusan permanen bertahan sesudah muat ulang
14. Muat ulang halaman
15. Buka Recycle Bin
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi file `repair-02-{runId}.jpg` tampil di Recycle Bin
18. Verifikasi file `laptop-old-{runId}.png` tidak tampil lagi di Recycle Bin
19. Tutup modal `Recycle Bin`
