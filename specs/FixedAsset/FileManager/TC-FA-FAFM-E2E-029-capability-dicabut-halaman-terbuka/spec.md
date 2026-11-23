---
id: TC-FA-FAFM-E2E-029-capability-dicabut-halaman-terbuka
title: "Capability Delete dicabut saat halaman terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [EB-AKS-6]
smoke: []
dependsOn: []
trace:
  EB-AKS-6: [2, 4, 8, 9, 12, 15]
anchor: [11, 14]
coverage:
  web: automated
---

# Capability Delete dicabut saat halaman terbuka

## Prerequisites
- Aktor: Sari Pengelola File `{runId}` (pemegang capability Manage files Read dan Delete pada group Head Office), dan Admin Pusat `{runId}` (Total Control) yang hanya memicu pencabutan capability.
- Layar awal: Settings > File Manager, halaman sudah terbuka untuk Sari Pengelola File.
- Data:
  - DU-029-1: User `Sari Pengelola File {runId}`, role `Pengelola File Head Office {runId}`, capability `Manage files: Read, Delete`, group `Head Office` beserta descendant.
  - DU-029-2: User `Admin Pusat {runId}`, role `Total Control`, cakupan seluruh group.
  - DU-029-3: File `laptop-front-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Reference `—`, Asset `Laptop Dell Latitude 5420 {runId}` (Increment dibentuk server), Asset ID milik aset itu, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `T0 − 3 hari, pukul 14:30`, ada di tab `Asset Photo`.

## Test Steps

### Delete ditolak setelah capability dicabut di halaman yang sudah terbuka
1. Ketik Search `laptop-front-{runId}.jpg`, tekan Enter
2. Verifikasi baris `laptop-front-{runId}.jpg` tampil pada tabel
3. Klik `⋯` pada baris `laptop-front-{runId}.jpg`
4. Verifikasi menu baris memuat `Delete`
5. Klik `Delete`
6. Admin Pusat `{runId}` mencabut capability Delete dari role `Pengelola File Head Office {runId}`
7. Klik `[Delete]` pada dialog `Delete File`
8. Verifikasi toast `You don't have permission to do this.` tampil
9. Verifikasi baris `laptop-front-{runId}.jpg` tetap tampil pada tabel

### Aksi Delete tidak lagi tersedia pada layar yang sama
10. Klik `⋯` pada baris `laptop-front-{runId}.jpg`
11. Verifikasi menu baris memuat `Download`
12. Verifikasi menu baris tidak memuat `Delete` (Hidden)
13. Centang baris `laptop-front-{runId}.jpg`
14. Verifikasi aksi bulk `Download (ZIP)` tampil
15. Verifikasi aksi bulk `Delete` tidak tampil (Hidden)
