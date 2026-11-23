---
id: TC-FA-FAFM-E2E-009-preview-file-web
title: "File Preview web: tab baru, format, dan file tidak tersedia"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FAFM-02a", "INV-03a", "INV-03c", "INV-03d", "PRV-01", "PRV-02", "PRV-03", "PRV-04", "PRV-05", "PRV-06", "PRV-07", "S-12", "§4.4#b1"]
smoke: []
dependsOn: []
trace:
  "F-FAFM-02a": 4
  "INV-03a": [5, 9]
  "INV-03c": 4
  "INV-03d": [4, 9]
  "PRV-01": [4, 8]
  "PRV-02": [4, 6]
  "PRV-03": [5, 11]
  "PRV-04": [14, 16]
  "PRV-05": 9
  "PRV-06": 8
  "PRV-07": [24, 27]
  "S-12": [24, 27]
  "§4.4#b1": 4
anchor: [20, 26]
coverage:
  web: automated
---

# File Preview web: tab baru, format, dan file tidak tersedia

## Prerequisites
- Aktor: Total Control, user `Hendra Wijaya {runId}` (tampil `Hendra W`), akun aktif dengan kredensial disediakan fase 2. Aktor kedua yang memicu perubahan: Total Control lain di entitas yang sama.
- Layar awal: halaman Settings > File Manager.
- Data:
  - DU-009-1: File File Name `laporan-inspeksi-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Forklift Toyota 8FD25 {runId}`, Group `Gudang Cikarang {runId}`, Size `400.0 KB`, Uploaded By `Hendra W`, ada di tab `Asset Documents`.
  - DU-009-2: File File Name `denah-lokasi-{runId}.png`, File Format `PNG`, Source `Attachment`, Reference `General`, Asset `Forklift Toyota 8FD25 {runId}`, Group `Gudang Cikarang {runId}`, Size `250.0 KB`, Uploaded By `Hendra W`, ada di tab `Asset Documents`.
  - DU-009-3: File File Name `rekap-biaya-{runId}.xlsx`, File Format `XLSX`, Source `Attachment`, Reference `Purchase`, Asset `Forklift Toyota 8FD25 {runId}`, Group `Gudang Cikarang {runId}`, Size `120.0 KB`, Uploaded By `Hendra W`, ada di tab `Asset Documents`.
  - DU-009-4: File File Name `notulen-vendor-{runId}.docx`, File Format `DOCX`, Source `Attachment`, Reference `General`, Asset `Forklift Toyota 8FD25 {runId}`, Group `Gudang Cikarang {runId}`, Size `90.0 KB`, Uploaded By `Hendra W`, ada di tab `Asset Documents`.
  - DU-009-5: File File Name `notulen-rapat-{runId}.pdf`, File Format `PDF`, Source `Attachment`, Reference `General`, Asset `Forklift Toyota 8FD25 {runId}`, Group `Gudang Cikarang {runId}`, Size `180.0 KB`, Uploaded By `Hendra W`, ada di tab `Asset Documents`.
- Kondisi:
  - Pada kelompok langkah terakhir, daftar tab `Asset Documents` milik aktor pertama sudah termuat dan tidak dimuat ulang oleh aktor pertama sampai ia mengklik File Name `notulen-rapat-{runId}.pdf`.

## Test Steps

### File PDF terbuka langsung di tab browser baru tanpa dialog
1. Klik tab `Asset Documents`
2. Ketik Search `{runId}`, tekan Enter
3. Klik File Name `laporan-inspeksi-{runId}.pdf`
4. Verifikasi file `laporan-inspeksi-{runId}.pdf` terbuka langsung di tab browser baru
5. Verifikasi file `laporan-inspeksi-{runId}.pdf` ditampilkan oleh viewer native browser
6. Verifikasi tab browser baru tidak memiliki akses ke window pembuka
7. Tutup tab browser baru
8. Verifikasi tab asal masih menampilkan halaman Settings > File Manager dengan baris `laporan-inspeksi-{runId}.pdf` pada tab `Asset Documents`
9. Verifikasi tidak ada dialog atau modal yang tampil di tab asal

### File gambar ditampilkan oleh viewer native browser
10. Klik File Name `denah-lokasi-{runId}.png`
11. Verifikasi file `denah-lokasi-{runId}.png` ditampilkan oleh viewer native browser di tab browser baru
12. Tutup tab browser baru

### Format yang tidak dapat ditampilkan browser langsung terunduh
13. Klik File Name `rekap-biaya-{runId}.xlsx`
14. Verifikasi file `rekap-biaya-{runId}.xlsx` langsung terunduh oleh browser
15. Klik File Name `notulen-vendor-{runId}.docx`
16. Verifikasi file `notulen-vendor-{runId}.docx` langsung terunduh oleh browser

### Preview file yang sudah dihapus permanen oleh aktor lain
17. Muat ulang halaman
18. Klik tab `Asset Documents`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi file `notulen-rapat-{runId}.pdf` tampil di tab `Asset Documents`
21. Aktor kedua menghapus file `notulen-rapat-{runId}.pdf`
22. Aktor kedua menghapus permanen file `notulen-rapat-{runId}.pdf` dari Recycle Bin
23. Klik File Name `notulen-rapat-{runId}.pdf`
24. Verifikasi tab browser baru menampilkan respons tidak ditemukan
25. Tutup tab browser baru
26. Verifikasi tab asal masih menampilkan halaman Settings > File Manager
27. Verifikasi tidak ada toast yang tampil di tab asal
