---
id: TC-FA-FAFM-BE-074-request-langsung-tanpa-capability
title: "Request langsung aksi tulis tanpa capability ditolak server"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["EB-AKS-3@delete-file", "EB-AKS-3@permanently-delete-file"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-3@delete-file": [2, 3, 5, 6]
  "EB-AKS-3@permanently-delete-file": [8, 9, 11, 12]
---

# Request langsung aksi tulis tanpa capability ditolak server

## Prerequisites
- Aktor: Read Only `Sari Wulandari {runId}` dan Custom `Wulan Anggraini {runId}`.
- Data:
  - DU-074-1: User `Sari Wulandari {runId}`, role Read Only, cakupan seluruh group, tanpa capability Delete.
  - DU-074-2: User `Wulan Anggraini {runId}`, role Custom dengan "Manage files": Read pada group `Head Office` saja, tanpa capability Delete.
  - DU-074-3: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`.
  - DU-074-4: File `delete-langsung-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-074-3, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-074-5: File `delete-bulk-satu-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-074-3, group `Head Office`, Size `310.0 KB`, aktif.
  - DU-074-6: File `delete-bulk-dua-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-074-3, group `Head Office`, Size `450.2 KB`, aktif.
  - DU-074-7: File `permanen-langsung-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-074-3, group `Head Office`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-074-8: File `permanen-bulk-satu-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-074-3, group `Head Office`, Size `640.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-074-9: File `permanen-bulk-dua-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-074-3, group `Head Office`, Size `750.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.

## Test Steps

### Delete langsung tanpa capability Delete
1. `Sari Wulandari {runId}` mengirim permintaan Delete atas file `delete-langsung-{runId}.jpg` langsung ke server, tanpa melalui UI
2. Verifikasi permintaan ditolak
3. Verifikasi file `delete-langsung-{runId}.jpg` tetap aktif, tanpa perubahan dan tanpa entri Changelog baru untuk File Name `delete-langsung-{runId}.jpg`
4. `Wulan Anggraini {runId}` mengirim permintaan Delete bulk atas file `delete-bulk-satu-{runId}.pdf` dan `delete-bulk-dua-{runId}.pdf` langsung ke server, tanpa melalui UI
5. Verifikasi permintaan ditolak untuk kedua file
6. Verifikasi file `delete-bulk-satu-{runId}.pdf` dan `delete-bulk-dua-{runId}.pdf` tetap aktif, tanpa perubahan dan tanpa entri Changelog baru

### Permanently Delete langsung tanpa capability Delete
7. `Sari Wulandari {runId}` mengirim permintaan Permanently Delete atas file `permanen-langsung-{runId}.png` langsung ke server, tanpa melalui UI
8. Verifikasi permintaan ditolak
9. Verifikasi file `permanen-langsung-{runId}.png` tetap berada di Recycle Bin, tanpa perubahan dan tanpa entri Changelog baru untuk File Name `permanen-langsung-{runId}.png`
10. `Wulan Anggraini {runId}` mengirim permintaan Permanently Delete bulk atas file `permanen-bulk-satu-{runId}.png` dan `permanen-bulk-dua-{runId}.png` langsung ke server, tanpa melalui UI
11. Verifikasi permintaan ditolak untuk kedua file
12. Verifikasi file `permanen-bulk-satu-{runId}.png` dan `permanen-bulk-dua-{runId}.png` tetap berada di Recycle Bin, tanpa perubahan dan tanpa entri Changelog baru
