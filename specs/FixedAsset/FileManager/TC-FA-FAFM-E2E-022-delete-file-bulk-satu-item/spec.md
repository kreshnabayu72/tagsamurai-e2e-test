---
id: TC-FA-FAFM-E2E-022-delete-file-bulk-satu-item
title: "Bulk Delete dengan satu file terpilih memakai bentuk tunggal"
layer: ui-e2e
priority: Medium
caseType: Edge
status: ready-for-automation
sourceRules: ["§7#p3", EB-EDG-2]
smoke: []
dependsOn: []
trace:
  "§7#p3": [7, 9, 19, 21]
  EB-EDG-2: [7, 10, 11, 19, 22, 23]
anchor: [2, 14]
coverage:
  web: automated
  android: automated
---

# Bulk Delete dengan satu file terpilih memakai bentuk tunggal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-022-1: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-022-2: File aktif `laptop-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `300.0 KB`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-022-3: File aktif `laptop-back-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `280.0 KB`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-022-4: File di Recycle Bin `laptop-old-satu-{runId}.png`, Source `Asset Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - DU-022-5: File di Recycle Bin `laptop-old-dua-{runId}.png`, Source `Asset Photo`, Size `160.0 KB`, Deleted By `System`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`.
  - Toast yang diharapkan `Success, laptop-front-{runId}.jpg has been deleted.`, dari Name file DU-022-2.
  - Toast yang diharapkan `Success, laptop-old-satu-{runId}.png has been permanently deleted.`, dari Name file DU-022-4.

## Test Steps

### Bulk Delete dengan satu file tersisa memakai bentuk tunggal
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi file `laptop-front-{runId}.jpg` dan `laptop-back-{runId}.jpg` tampil di tab `Asset Photo`
3. Pilih `laptop-front-{runId}.jpg` untuk aksi bulk
4. Pilih `laptop-back-{runId}.jpg` untuk aksi bulk
5. Batalkan pilihan `laptop-back-{runId}.jpg`
6. Klik `Delete` pada bar aksi bulk
7. Verifikasi dialog yang tampil untuk satu file terpilih berjudul `Delete File` dan memuat bullet nama file `laptop-front-{runId}.jpg`
8. Klik `[Delete]` pada dialog `Delete File`
9. Verifikasi toast `Success, laptop-front-{runId}.jpg has been deleted.` tampil
10. Verifikasi file `laptop-front-{runId}.jpg` tidak tampil lagi di tab `Asset Photo`
11. Verifikasi file `laptop-back-{runId}.jpg` masih tampil di tab `Asset Photo`

### Bulk Permanently Delete dengan satu file tersisa memakai bentuk tunggal
12. Klik `Recycle Bin` pada header kartu `Storage Usage`
13. Ketik Search `{runId}`, tekan Enter
14. Verifikasi file `laptop-old-satu-{runId}.png` dan `laptop-old-dua-{runId}.png` tampil di Recycle Bin
15. Pilih `laptop-old-satu-{runId}.png` untuk aksi bulk
16. Pilih `laptop-old-dua-{runId}.png` untuk aksi bulk
17. Batalkan pilihan `laptop-old-dua-{runId}.png`
18. Klik `Permanently Delete` pada bar aksi bulk
19. Verifikasi dialog yang tampil untuk satu file terpilih berjudul `Permanently Delete File` dan memuat bullet nama file `laptop-old-satu-{runId}.png`
20. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
21. Verifikasi toast `Success, laptop-old-satu-{runId}.png has been permanently deleted.` tampil
22. Verifikasi file `laptop-old-satu-{runId}.png` tidak tampil lagi di Recycle Bin
23. Verifikasi file `laptop-old-dua-{runId}.png` masih tampil di Recycle Bin
24. Tutup modal `Recycle Bin`
