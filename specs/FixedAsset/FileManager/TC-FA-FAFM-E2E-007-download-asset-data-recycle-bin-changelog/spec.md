---
id: TC-FA-FAFM-E2E-007-download-asset-data-recycle-bin-changelog
title: "Download dari tab Asset Data, Recycle Bin, dan Changelog"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TBL-06d", "TBL-07b"]
smoke: []
dependsOn: []
trace:
  "TBL-06d": [4, 13]
  "TBL-07b": 18
anchor: []
coverage:
  web: automated
---

# Download dari tab Asset Data, Recycle Bin, dan Changelog

## Prerequisites
- Aktor: Total Control, user `Wulan Puspita {runId}` (tampil `Wulan P`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Spec ini memakai entitas khusus (seluruh-daftar): Download tanpa Search dan Filter memuat seluruh baris tabel, jadi entitas hanya berisi aset dan file di bawah; Recycle Bin dan Changelog kosong sebelum spec mulai.
  - DU-007-1: File File Name `kontrak-sewa-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Printer Canon iR2206 {runId}`, Group `Kantor Pusat {runId}`, Size `250.0 KB`, Uploaded By `Wulan P`, ada di tab `Asset Documents`.
  - DU-007-2: Aset Name `Printer Canon iR2206 {runId}`, Group `Kantor Pusat {runId}`, Status `Disposed`, ada di tab `Disposed & Unmanaged Assets`.
  - DU-007-3: Aset Name `Scanner Fujitsu fi-7160 {runId}`, Group `Kantor Pusat {runId}`, Status `Unmanaged`, ada di tab `Disposed & Unmanaged Assets`.

## Test Steps

### Download tab Asset Data memakai nama berkas default
1. Klik tab `Disposed & Unmanaged Assets`
2. Klik ikon Download
3. Klik `Download as CSV`
4. Verifikasi berkas `File-Manager-Asset-Data` format CSV terunduh

### Download Recycle Bin memakai nama berkas default setelah Delete file
5. Klik tab `Asset Documents`
6. Ketik Search `{runId}`, tekan Enter
7. Buka aksi baris `kontrak-sewa-{runId}.pdf`
8. Klik `Delete`
9. Klik `[Delete]` pada dialog `Delete File`
10. Klik `Recycle Bin` pada header kartu `Storage Usage`
11. Klik ikon Download pada modal `Recycle Bin`
12. Klik `Download as XLSX`
13. Verifikasi berkas `File-Manager-Recycle-Bin` format XLSX terunduh
14. Tutup modal `Recycle Bin`

### Download Changelog memakai nama berkas default
15. Klik `Changelog` pada header kartu `Storage Usage`
16. Klik ikon Download pada modal `Changelog`
17. Klik `Download as CSV`
18. Verifikasi berkas `Changelog-File-Manager` format CSV terunduh
19. Tutup modal `Changelog`
