---
id: TC-FA-FAFM-BE-062-state-entitas-dan-plan
title: "Entitas Suspended, Expired, Grace menolak aksi tulis, job tetap berjalan, tanpa gating plan"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: ["DIM-02a", "EC-09", "EC-12", "V-08", "§9.4.1#r1", "§9.10#p1", "EB-AKS-7"]
smoke: []
dependsOn: []
trace:
  "DIM-02a": [50]
  "EC-09": [3, 5, 7, 9, 13, 15, 17, 19, 23, 25, 27, 29]
  "EC-12": [35, 36, 41, 42, 47, 48]
  "V-08": [3, 5, 7, 9, 13, 15, 17, 19, 23, 25, 27, 29]
  "§9.4.1#r1": [3, 13, 23, 35, 41, 47]
  "§9.10#p1": [50, 54, 56, 58]
  "EB-AKS-7": [3, 5, 7, 9, 10, 13, 15, 17, 19, 20, 23, 25, 27, 29, 30]
---

# Entitas Suspended, Expired, Grace menolak aksi tulis, job tetap berjalan, tanpa gating plan

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-062-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-062-2: File `foto-laptop-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-062-3: File `foto-scanner-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Size `640.0 KB`, aktif.
  - DU-062-4: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `1.0 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-062-5: File `scanner-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-062-6: File `tanpa-gating-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `500.0 KB`, aktif.
  - DU-062-8: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Disposed`.
  - DU-062-9: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Disposed`.
  - DU-062-10: Aset `Projector Epson EB-X06 {runId}`, group `Branch Bandung`, Status `Disposed`.
  - DU-062-11: File `dsp-printer-{runId}.pdf`, Source `Disposal Document`, File Format PDF, aset DU-062-8, group `Head Office`, Size `3.2 MB`, aktif.
  - DU-062-12: File `dsp-monitor-{runId}.pdf`, Source `Disposal Document`, File Format PDF, aset DU-062-9, group `Head Office`, Size `1.5 MB`, aktif.
  - DU-062-13: File `dsp-projector-{runId}.pdf`, Source `Disposal Document`, File Format PDF, aset DU-062-10, group `Branch Bandung`, Size `2.0 MB`, aktif.
  - DU-062-14: File `purge-suspended-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `700.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-062-15: File `purge-expired-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `710.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-062-16: File `purge-grace-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `720.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-062-17: File `ledger-hapus-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `530.0 KB`, aktif.
  - DU-062-18: File `ledger-permanen-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `540.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Entitas Suspended menolak aksi tulis user
1. Keadaan: entitas aktor berstatus `Suspended`
2. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` langsung ke server
3. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
4. `Bagas Pratama {runId}` mengirim permintaan Delete bulk atas file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` langsung ke server
5. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
6. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
7. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
8. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` langsung ke server
9. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
10. Verifikasi file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` tetap aktif, file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` tetap berada di Recycle Bin, dan tidak ada entri Changelog untuk keempat file itu

### Entitas Expired menolak aksi tulis user
11. Keadaan: entitas aktor berstatus `Expired`
12. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` langsung ke server
13. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
14. `Bagas Pratama {runId}` mengirim permintaan Delete bulk atas file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` langsung ke server
15. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
16. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
17. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
18. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` langsung ke server
19. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
20. Verifikasi file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` tetap aktif, file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` tetap berada di Recycle Bin, dan tidak ada entri Changelog untuk keempat file itu

### Entitas dalam masa Grace menolak aksi tulis user
21. Keadaan: entitas aktor berada dalam masa Grace setelah `Expired`
22. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` langsung ke server
23. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
24. `Bagas Pratama {runId}` mengirim permintaan Delete bulk atas file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` langsung ke server
25. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
26. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
27. Verifikasi permintaan ditolak server walau `Bagas Pratama {runId}` punya capability Delete atas group file
28. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` langsung ke server
29. Verifikasi seluruh permintaan bulk ditolak server tanpa ada item yang diproses
30. Verifikasi file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` tetap aktif, file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` tetap berada di Recycle Bin, dan tidak ada entri Changelog untuk keempat file itu

### Job tetap berjalan pada entitas Suspended
31. `Bagas Pratama {runId}` menghapus Asset Data aset `Printer HP M404 {runId}` dan penghapusan berhasil, saat entitas aktor masih berstatus Active
32. Keadaan: entitas aktor berstatus `Suspended`
33. Waktu berlalu sampai batas purge file `purge-suspended-{runId}.png` terlewati
34. Job auto-purge harian dan job cascade purge berjalan
35. Verifikasi file `purge-suspended-{runId}.png` terhapus permanen dari Recycle Bin, dengan aktor `System`
36. Verifikasi file `dsp-printer-{runId}.pdf`, file aset `Printer HP M404 {runId}`, terhapus permanen

### Job tetap berjalan pada entitas Expired
37. `Bagas Pratama {runId}` menghapus Asset Data aset `Monitor LG 24 {runId}` dan penghapusan berhasil, saat entitas aktor masih berstatus Active
38. Keadaan: entitas aktor berstatus `Expired`
39. Waktu berlalu sampai batas purge file `purge-expired-{runId}.png` terlewati
40. Job auto-purge harian dan job cascade purge berjalan
41. Verifikasi file `purge-expired-{runId}.png` terhapus permanen dari Recycle Bin, dengan aktor `System`
42. Verifikasi file `dsp-monitor-{runId}.pdf`, file aset `Monitor LG 24 {runId}`, terhapus permanen

### Job tetap berjalan pada entitas dalam masa Grace
43. `Bagas Pratama {runId}` menghapus Asset Data aset `Projector Epson EB-X06 {runId}` dan penghapusan berhasil, saat entitas aktor masih berstatus Active
44. Keadaan: entitas aktor berada dalam masa Grace setelah `Expired`
45. Waktu berlalu sampai batas purge file `purge-grace-{runId}.png` terlewati
46. Job auto-purge harian dan job cascade purge berjalan
47. Verifikasi file `purge-grace-{runId}.png` terhapus permanen dari Recycle Bin, dengan aktor `System`
48. Verifikasi file `dsp-projector-{runId}.pdf`, file aset `Projector Epson EB-X06 {runId}`, terhapus permanen

### File Manager tersedia di semua plan tanpa gating plan
49. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `tanpa-gating-{runId}.jpg` langsung ke server
50. Verifikasi permintaan diterima dan file `tanpa-gating-{runId}.jpg` berada di Recycle Bin, tanpa penolakan karena fitur tidak tersedia di plan entitas aktor

### Delete dan Permanently Delete tidak mengubah ledger Storage per-Client
51. Keadaan: entitas aktor berstatus Active
52. `Bagas Pratama {runId}` membaca nilai Total Used dan Storage Quota client pada ledger Storage per-Client
53. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `ledger-hapus-{runId}.jpg` langsung ke server
54. Verifikasi permintaan diterima dan file `ledger-hapus-{runId}.jpg` berada di Recycle Bin, tanpa penolakan karena batas Storage
55. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `ledger-permanen-{runId}.png` langsung ke server
56. Verifikasi permintaan diterima dan file `ledger-permanen-{runId}.png` terhapus permanen dari Recycle Bin, tanpa penolakan karena batas Storage
57. `Bagas Pratama {runId}` membaca ulang nilai Total Used dan Storage Quota client pada ledger Storage per-Client
58. Verifikasi Total Used dan Storage Quota sama dengan nilai yang dibaca sebelum Delete dan Permanently Delete, sehingga File Manager tidak mengubah ledger Storage per-Client
