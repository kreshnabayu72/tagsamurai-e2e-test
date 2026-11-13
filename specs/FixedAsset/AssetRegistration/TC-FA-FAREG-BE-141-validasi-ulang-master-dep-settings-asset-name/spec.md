---
id: TC-FA-FAREG-BE-141-validasi-ulang-master-dep-settings-asset-name
title: "Validasi ulang referensi master di server"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-08b, FAREG-LOGIC-18a, FAREG-LOGIC-18e]
smoke: []
dependsOn:
  - "Settings Asset Name: arsip, hapus, dan lepas Brand atau Model"
owner: BE
trace:
  FAREG-LOGIC-08b: [3, 5, 8, 11]
  FAREG-LOGIC-18a: [14, 16, 19, 21, 24, 26]
  FAREG-LOGIC-18e: [28, 30]
---

# Validasi ulang referensi master di server

## Prerequisites
- Aktor:
  - Hana T (Total Control, termasuk akses mengubah master di Settings Asset Name).
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Depok {runId}`) sebagai pengaju.
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Depok {runId}`) sebagai approver.
- Data:
  - DU-141-1: Group `Gudang Depok {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-141-2: Asset Name `Kursi Arsip {runId}`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-3: Asset Name `Meja Hapus {runId}`, Brand `Olympic {runId}`, Model `OL-141`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-4: Asset Name `Lemari Lepas {runId}`, Brand `Chitose`, Model `Orion C`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-5: Asset Name `Rak Gudang {runId}`, Brand `Krisbow {runId}`, Model `KR-141`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-6: Asset Name `Rak Besi {runId}`, Brand `Lion {runId}`, Model `LN-141`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-7: Asset Name `Rak Plastik {runId}`, Brand `Napolly {runId}`, Model `NP-141`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-8: Asset Name `Rak Kayu {runId}`, Brand `Napolly Kayu {runId}`, Model `NK-141`, TAG Type `Non-TAG`, Status `Active`.
  - DU-141-9: batch Draft milik Rina W di Group `Gudang Depok {runId}`, Item `Kursi Arsip {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-141-10: batch Draft milik Rina W di Group `Gudang Depok {runId}`, Item `Meja Hapus {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-141-11: batch Draft milik Rina W di Group `Gudang Depok {runId}`, Item `Lemari Lepas {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-141-12: pengajuan `Waiting for Approval` milik Rina W berisi `1` aset `Rak Gudang {runId}`.
  - DU-141-13: pengajuan `Waiting for Approval` milik Rina W berisi `1` aset `Rak Besi {runId}`.
  - DU-141-14: pengajuan `Waiting for Approval` milik Rina W berisi `1` aset `Rak Plastik {runId}`.
  - DU-141-15: pengajuan `Waiting for Approval` milik Rina W berisi `1` aset `Rak Kayu {runId}`.
- Kondisi:
  - kuota Group `Gudang Depok {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.

## Test Steps

### Save draft memvalidasi ulang Asset Name yang diarsipkan
1. Hana T mengarsipkan Asset Name `Kursi Arsip {runId}` di Settings Asset Name
2. Rina W menyimpan batch DU-141-9 dengan Quantity `2`
3. Verifikasi batch DU-141-9 tersimpan dengan Asset Name, Brand, dan Model dikosongkan serta Quantity `2` dipertahankan, dan respons memuat peringatan
4. Rina W mengirim Activate atas batch DU-141-9
5. Verifikasi Activate ditolak server dan batch DU-141-9 tetap Draft tanpa pengajuan baru

### Save draft memvalidasi ulang Brand yang dihapus
6. Hana T menghapus Brand `Olympic {runId}` dari Asset Name `Meja Hapus {runId}` di Settings Asset Name
7. Rina W menyimpan batch DU-141-10 dengan Quantity `2`
8. Verifikasi batch DU-141-10 tersimpan dengan Brand dan Model dikosongkan, Asset Name `Meja Hapus {runId}` tetap terisi, dan Quantity `2` dipertahankan

### Activate memvalidasi ulang Model yang dilepas dari Brand
9. Hana T melepas Model `Orion C` dari Brand `Chitose` pada Asset Name `Lemari Lepas {runId}` di Settings Asset Name
10. Rina W mengirim Activate atas batch DU-141-11
11. Verifikasi Activate ditolak server dan batch DU-141-11 tetap Draft tanpa pengajuan baru

### Keputusan memvalidasi ulang Brand yang diarsipkan
12. Hana T mengarsipkan Brand `Krisbow {runId}` pada Asset Name `Rak Gudang {runId}` di Settings Asset Name
13. Budi membuka halaman Approval pengajuan DU-141-12
14. Verifikasi aset pengajuan DU-141-12 ditandai `Unavailable` karena Brand diarsipkan
15. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-141-12
16. Verifikasi keputusan ditolak server dan pengajuan DU-141-12 tetap `Waiting for Approval`

### Keputusan memvalidasi ulang Model yang dilepas
17. Hana T melepas Model `LN-141` dari Brand `Lion {runId}` pada Asset Name `Rak Besi {runId}` di Settings Asset Name
18. Budi membuka halaman Approval pengajuan DU-141-13
19. Verifikasi aset pengajuan DU-141-13 ditandai `Unavailable` karena Model dilepas dari Brand
20. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-141-13
21. Verifikasi keputusan ditolak server dan pengajuan DU-141-13 tetap `Waiting for Approval`

### Keputusan memvalidasi ulang Asset Name yang dihapus
22. Hana T menghapus Asset Name `Rak Plastik {runId}` di Settings Asset Name
23. Budi membuka halaman Approval pengajuan DU-141-14
24. Verifikasi aset pengajuan DU-141-14 ditandai `Unavailable` karena Asset Name dihapus
25. Budi mengirim keputusan `Approve` untuk aset pengajuan DU-141-14
26. Verifikasi keputusan ditolak server dan pengajuan DU-141-14 tetap `Waiting for Approval`

### Koreksi ke nilai master yang tidak valid ditolak
27. Budi menyimpan koreksi Brand aset pertama pengajuan DU-141-15 menjadi `Krisbow {runId}` yang sudah diarsipkan
28. Verifikasi koreksi ditolak server dan aset pertama tidak memiliki koreksi staged
29. Budi menyimpan koreksi Model aset pertama pengajuan DU-141-15 menjadi `LN-141` yang sudah dilepas dari Brand `Lion {runId}`
30. Verifikasi koreksi ditolak server dan aset pertama tidak memiliki koreksi staged
