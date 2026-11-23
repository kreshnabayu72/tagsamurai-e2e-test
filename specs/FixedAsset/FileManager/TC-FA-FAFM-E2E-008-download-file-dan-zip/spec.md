---
id: TC-FA-FAFM-E2E-008-download-file-dan-zip
title: "Download satu file dan Download (ZIP) beberapa file"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-01a", "ACT-01b", "ACT-01c", "ACT-03d", "ACT-03e", "ARS-06a", "ARS-06b", "ARS-06d", "EC-01", "F-FAFM-02c", "S-18", "TBL-05a", "V-01", "§4.4#b3", "§9.4.3#b1", "EB-FB-2@download-file"]
smoke: []
dependsOn: []
trace:
  "ACT-01a": 4
  "ACT-01b": [6, 10]
  "ACT-01c": 6
  "ACT-03d": [16, 18, 19]
  "ACT-03e": [16, 17]
  "ARS-06a": 10
  "ARS-06b": 6
  "ARS-06d": 11
  "EC-01": [6, 7]
  "F-FAFM-02c": 6
  "S-18": [6, 7, 16, 17]
  "TBL-05a": 14
  "V-01": 28
  "§4.4#b3": 6
  "§9.4.3#b1": [7, 17]
  "EB-FB-2@download-file": [7, 17]
anchor: [6, 16, 18, 23]
coverage:
  web: automated
  android: automated
---

# Download satu file dan Download (ZIP) beberapa file

## Prerequisites
- Aktor: Total Control, user `Dewi Lestari {runId}` (tampil `Dewi L`), akun aktif dengan kredensial disediakan fase 2. Aktor kedua yang memicu perubahan: Total Control lain di entitas yang sama.
- Layar awal: Settings > File Manager.
- Data:
  - DU-008-1: File File Name `proposal-vendor-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Genset Cummins C220 {runId}`, Group `Pabrik Karawang {runId}`, Size `300.0 KB`, Uploaded By `Dewi L`, ada di tab `Asset Documents`.
  - DU-008-2: File File Name `spesifikasi-teknis-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Genset Cummins C220 {runId}`, Group `Pabrik Karawang {runId}`, Size `450.0 KB`, Uploaded By `Dewi L`, ada di tab `Asset Documents`.
  - DU-008-3: File File Name `foto-instalasi-{runId}.png`, File Format `PNG`, Source `Attachment`, Reference `General`, Asset `Genset Cummins C220 {runId}`, Group `Pabrik Karawang {runId}`, Size `200.0 KB`, Uploaded By `Dewi L`, ada di tab `Asset Documents`.
  - DU-008-4: File File Name `berita-acara-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Genset Cummins C220 {runId}`, Group `Pabrik Karawang {runId}`, Size `150.0 KB`, Uploaded By `Dewi L`, ada di tab `Asset Documents`.
- Kondisi:
  - Pada kelompok langkah terakhir, daftar tab `Asset Documents` milik aktor pertama sudah termuat dan tidak dimuat ulang oleh aktor pertama sampai ia mengklik `Download` pada baris `berita-acara-{runId}.pdf`.

## Test Steps

### Download satu file langsung terunduh tanpa toast sukses
1. Klik tab `Asset Documents`
2. Ketik Search `{runId}`, tekan Enter
3. Buka aksi baris `proposal-vendor-{runId}.pdf`
4. Verifikasi aksi `Download` ada pada aksi baris `proposal-vendor-{runId}.pdf`
5. Klik `Download`
6. Verifikasi berkas `proposal-vendor-{runId}.pdf` terunduh
7. Verifikasi tidak ada toast sukses setelah file `proposal-vendor-{runId}.pdf` terunduh

### Download ulang file yang sama tidak mengubah data
8. Buka aksi baris `proposal-vendor-{runId}.pdf`
9. Klik `Download`
10. Verifikasi berkas `proposal-vendor-{runId}.pdf` terunduh kembali dengan isi yang sama
11. Verifikasi file `proposal-vendor-{runId}.pdf` masih tampil di tab `Asset Documents`

### Download (ZIP) memuat file terpilih saja
12. Pilih `proposal-vendor-{runId}.pdf` untuk aksi bulk
13. Pilih `spesifikasi-teknis-{runId}.pdf` untuk aksi bulk
14. Verifikasi bar aksi bulk memuat aksi `Download (ZIP)`
15. Klik `Download (ZIP)` pada bar aksi bulk
16. Verifikasi berkas `File-Manager-Files.zip` terunduh langsung tanpa dialog atau langkah tambahan
17. Verifikasi tidak ada toast sukses setelah unduhan ZIP selesai
18. Verifikasi berkas ZIP memuat `proposal-vendor-{runId}.pdf` dan `spesifikasi-teknis-{runId}.pdf`
19. Verifikasi berkas ZIP tidak memuat `foto-instalasi-{runId}.png`

### Download file yang sudah dihapus permanen oleh aktor lain
20. Muat ulang halaman
21. Klik tab `Asset Documents`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi file `berita-acara-{runId}.pdf` dan `foto-instalasi-{runId}.png` tampil di tab `Asset Documents`
24. Aktor kedua menghapus file `berita-acara-{runId}.pdf`
25. Aktor kedua menghapus permanen file `berita-acara-{runId}.pdf` dari Recycle Bin
26. Buka aksi baris `berita-acara-{runId}.pdf`
27. Klik `Download`
28. Verifikasi tidak ada berkas `berita-acara-{runId}.pdf` yang terunduh
