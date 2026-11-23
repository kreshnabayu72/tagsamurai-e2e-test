---
id: TC-FA-FAFM-BE-060-authz-per-role-sisi-server
title: "Server menegakkan permission Delete dan Permanently Delete per role"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["ACT-03b", "DIM-04a", "EC-08", "F-FAFM-02.k1", "F-FAFM-02f", "FAFM-LOGIC-05f", "FAFM-LOGIC-05g", "FAFM-LOGIC-05k", "FAFM-LOGIC-05l", "V-09", "§9.3#p1", "EB-ERR-4"]
smoke: []
dependsOn: []
trace:
  "ACT-03b": [22, 23]
  "DIM-04a": [2, 6, 11, 13, 16, 19, 25]
  "EC-08": [2, 11, 16, 19]
  "F-FAFM-02.k1": [2, 6, 16]
  "F-FAFM-02f": [2, 16]
  "FAFM-LOGIC-05f": [9, 30]
  "FAFM-LOGIC-05g": [11, 13, 19, 30]
  "FAFM-LOGIC-05k": 25
  "FAFM-LOGIC-05l": [2, 6, 11, 13, 16, 19, 23, 25]
  "V-09": [2, 11, 16, 19]
  "§9.3#p1": [2, 28]
  "EB-ERR-4": [3, 4, 7, 14, 17, 20, 26]
---

# Server menegakkan permission Delete dan Permanently Delete per role

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`, Read Only `Sari Wulandari {runId}`, pemegang Manage files `Rahmat Hidayat {runId}` dan `Wulan Anggraini {runId}`.
- Data:
  - DU-060-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-060-2: User `Sari Wulandari {runId}`, role Read Only, cakupan seluruh group.
  - DU-060-3: User `Rahmat Hidayat {runId}`, capability Manage files dengan Read atas group `Branch Bandung` beserta descendant dan Delete atas group `Head Office` beserta descendant, tanpa capability lain.
  - DU-060-4: User `Wulan Anggraini {runId}`, capability Manage files dengan Read atas group `Branch Bandung` beserta descendant, tanpa Delete dan tanpa capability lain.
  - DU-060-5: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status Active, Photo merujuk DU-060-8.
  - DU-060-6: Aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Status Active, Photo merujuk DU-060-9.
  - DU-060-7: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status Active, Photo merujuk DU-060-12.
  - DU-060-8: File `foto-laptop-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-060-5, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-060-9: File `foto-scanner-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-060-6, group `Branch Bandung`, Size `640.0 KB`, aktif.
  - DU-060-10: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-060-5, group `Head Office`, Size `1.0 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-060-11: File `scanner-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-060-6, group `Branch Bandung`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-060-12: File `foto-monitor-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-060-7, group `Head Office`, Size `750.0 KB`, aktif.

## Test Steps

### Read Only ditolak Delete single
1. `Sari Wulandari {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` langsung ke server tanpa melalui UI
2. Verifikasi permintaan ditolak karena `Sari Wulandari {runId}` tidak punya capability Delete atas group `Head Office`, walau file berada dalam scope-nya
3. Verifikasi file `foto-laptop-{runId}.jpg` tetap aktif dan tetap menjadi rujukan Photo aset `Laptop Dell Latitude 5420 {runId}`
4. Verifikasi tidak ada entri Changelog File Manager dengan File Name `foto-laptop-{runId}.jpg`

### Read Only ditolak Delete bulk
5. `Sari Wulandari {runId}` mengirim permintaan Delete bulk atas file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` langsung ke server
6. Verifikasi seluruh permintaan bulk ditolak tanpa ada item yang diproses
7. Verifikasi file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg` tetap aktif

### Read Only ditolak Permanently Delete
8. `Sari Wulandari {runId}` membaca daftar Recycle Bin
9. Verifikasi daftar Recycle Bin yang dibaca `Sari Wulandari {runId}` memuat file `laptop-lama-{runId}.png`, tanpa capability lain selain Read
10. `Sari Wulandari {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
11. Verifikasi permintaan ditolak karena `Sari Wulandari {runId}` tidak punya capability Delete, capability yang sama yang menjadi gate Permanently Delete
12. `Sari Wulandari {runId}` mengirim permintaan Permanently Delete bulk atas file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` langsung ke server
13. Verifikasi seluruh permintaan bulk ditolak karena capability Delete tidak dimiliki
14. Verifikasi file `laptop-lama-{runId}.png` dan `scanner-lama-{runId}.png` tetap berada di Recycle Bin dan tidak ada entri Changelog `Permanently Delete` untuk keduanya

### Pemegang Read di satu group dan Delete di group lain ditolak pada group Read
15. `Rahmat Hidayat {runId}` mengirim permintaan Delete atas file `foto-scanner-{runId}.jpg` langsung ke server
16. Verifikasi permintaan ditolak karena `Rahmat Hidayat {runId}` hanya punya Read atas group `Branch Bandung`, walau punya Delete atas group `Head Office`
17. Verifikasi file `foto-scanner-{runId}.jpg` tetap aktif
18. `Rahmat Hidayat {runId}` mengirim permintaan Permanently Delete atas file `scanner-lama-{runId}.png` langsung ke server
19. Verifikasi permintaan ditolak karena Delete atas group `Branch Bandung` tidak dimiliki `Rahmat Hidayat {runId}`
20. Verifikasi file `scanner-lama-{runId}.png` tetap berada di Recycle Bin

### Gate Read per baris pada Download ZIP
21. `Wulan Anggraini {runId}` meminta Download (ZIP) atas file `foto-laptop-{runId}.jpg` dan `foto-scanner-{runId}.jpg`
22. Verifikasi berkas ZIP yang diterima memuat file `foto-scanner-{runId}.jpg`, yang berada dalam Read `Wulan Anggraini {runId}`
23. Verifikasi berkas ZIP yang diterima tidak memuat file `foto-laptop-{runId}.jpg`, karena Read atas group `Head Office` tidak dimiliki `Wulan Anggraini {runId}`

### Penolakan server tidak bergantung pada UI Hidden
24. `Wulan Anggraini {runId}`, yang aksi Delete-nya Hidden di UI, mengirim permintaan Delete atas file `foto-scanner-{runId}.jpg` langsung ke server
25. Verifikasi server menolak permintaan itu sebagai lapis penegakan sesudah UI Hidden
26. Verifikasi file `foto-scanner-{runId}.jpg` tetap aktif

### Delete oleh aktor berwenang tidak diblokir rujukan record sumber
27. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-monitor-{runId}.jpg`, yang sedang dirujuk Photo aset `Monitor LG 24 {runId}`
28. Verifikasi permintaan diterima dan file `foto-monitor-{runId}.jpg` berada di Recycle Bin, tanpa blokir karena dirujuk record sumber

### Permanently Delete oleh pemegang Delete tanpa capability Recycle Bin terpisah
29. `Rahmat Hidayat {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
30. Verifikasi permintaan diterima dan file `laptop-lama-{runId}.png` terhapus permanen dari Recycle Bin, hanya dengan capability Manage files yang sama
