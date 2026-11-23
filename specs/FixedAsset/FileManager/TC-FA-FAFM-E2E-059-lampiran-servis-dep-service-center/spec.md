---
id: TC-FA-FAFM-E2E-059-lampiran-servis-dep-service-center
title: "Lampiran Service Center tidak tampil di File Manager"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2d#p6", "§11#r8"]
smoke: []
dependsOn: ["Service Center: lampiran servis"]
trace:
  "§4.2d#p6": [4, 8, 17, 22]
  "§11#r8": [4, 8, 17, 22]
anchor: [3, 7, 16]
coverage:
  web: automated
---

# Lampiran Service Center tidak tampil di File Manager

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Settings > File Manager.
- Data:
  - DU-059-1: Aset `Printer HP M404 {runId}`, Group `Head Office`, ada di entitas aktor, memiliki foto aktif DU-059-2 dan dokumen aktif DU-059-3.
  - DU-059-2: File `servis-foto-{runId}.jpg`, Category `Asset Photo`, aktif, foto aset DU-059-1.
  - DU-059-3: File `servis-dokumen-{runId}.pdf`, Source `Attachment`, aktif, dokumen aset DU-059-1.
  - DU-059-4: Lampiran servis `servis-lampiran-{runId}.pdf` yang diunggah pada servis aset DU-059-1 di Service Center, dihapus dari servis itu di dalam spec.
  - DU-059-5: Lampiran servis `servis-hitung-{runId}.pdf`, Size `3.0 MB`, diunggah pada servis aset DU-059-1 di dalam spec.

## Test Steps

### Lampiran servis tidak terdaftar di tab Asset Photo dan Asset Documents
1. Klik tab `Asset Photo`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris file `servis-foto-{runId}.jpg` tampil dengan Asset `Printer HP M404 {runId}`
4. Verifikasi tidak ada baris file `servis-lampiran-{runId}.pdf` di tab `Asset Photo`
5. Klik tab `Asset Documents`
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi baris file `servis-dokumen-{runId}.pdf` tampil dengan Source `Attachment`
8. Verifikasi tidak ada baris file `servis-lampiran-{runId}.pdf` di tab `Asset Documents`

### Lampiran servis tidak terdaftar di Recycle Bin
9. Klik tab `Asset Photo`
10. Ketik Search `servis-foto-{runId}.jpg`, tekan Enter
11. Klik aksi Delete pada baris file `servis-foto-{runId}.jpg`
12. Klik `[Delete]` pada dialog Delete File
13. Hapus lampiran `servis-lampiran-{runId}.pdf` dari servis aset `Printer HP M404 {runId}` di Service Center
14. Klik tombol Recycle Bin pada header kartu Storage Usage
15. Ketik Search `{runId}`, tekan Enter
16. Verifikasi baris file `servis-foto-{runId}.jpg` tampil di Recycle Bin
17. Verifikasi tidak ada baris file `servis-lampiran-{runId}.pdf` di Recycle Bin
18. Tutup modal Recycle Bin

### Ukuran lampiran servis hanya masuk angka Fixed Asset di kartu Storage Usage
19. Catat nilai `Fixed Asset` pada kartu Storage Usage
20. Unggah lampiran `servis-hitung-{runId}.pdf` pada servis aset `Printer HP M404 {runId}` di Service Center
21. Buka Settings > File Manager
22. Verifikasi nilai `Fixed Asset` pada kartu Storage Usage lebih besar dari nilai yang dicatat pada langkah 19
