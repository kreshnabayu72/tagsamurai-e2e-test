---
id: TC-FA-FAREG-BE-138-konkurensi-registrasi
title: "Konkurensi: Submit ganda, Tag direbut, dan keputusan bersamaan"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-19g, "§9.4.2#r17", "§9.4.2#r50", "§9.4.2#r51", EB-CON-3, EB-EDG-1]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-19g: [3, 5, 7]
  "§9.4.2#r17": [20, 22, 23]
  "§9.4.2#r50": [10, 11, 12]
  "§9.4.2#r51": [15, 16, 17]
  EB-CON-3: [3, 20, 22, 26, 30, 31]
  EB-EDG-1: [7, 26]
---

# Konkurensi: Submit ganda, Tag direbut, dan keputusan bersamaan

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Tangerang {runId}`) dengan dua sesi, disebut sesi pertama dan sesi kedua.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Tangerang {runId}`).
  - Budi dan Citra (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Tangerang {runId}`) sebagai approver.
- Data:
  - DU-138-1: Group `Gudang Tangerang {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-138-2: Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-138`, TAG Type `Non-TAG`, Status `Active`.
  - DU-138-3: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-138-4: batch Draft milik Rina W di Group `Gudang Tangerang {runId}`, Item `Meja Kerja {runId}` Quantity `3`, memenuhi Tingkat 2.
  - DU-138-5: batch Draft milik Rina W di Group `Gudang Tangerang {runId}`, Item `Laptop {runId}` Quantity `1` dengan Tag `E280-1380-0001 {runId}` pada aset pertama.
  - DU-138-6: batch Draft milik Lina di Group `Gudang Tangerang {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-138-7: batch Draft milik Rina W di Group `Gudang Tangerang {runId}`, Item `Laptop {runId}` Quantity `2` dengan Tag `E280-1380-0002 {runId}` pada aset pertama dan Tag `E280-1380-0003 {runId}` pada aset kedua, memenuhi Tingkat 2.
  - DU-138-8: batch Draft milik Lina di Group `Gudang Tangerang {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-138-9: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Meja Kerja {runId}`.
  - DU-138-10: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Meja Kerja {runId}`.
  - DU-138-11: batch Draft milik Rina W di Group `Gudang Tangerang {runId}`, Item `Meja Kerja {runId}` Quantity `1`.
  - DU-138-16: aset `Active` `Meja Kerja {runId}` di Group `Gudang Tangerang {runId}`, Brand `Olympic`, Model `OL-138`.
  - Asset Name `Meja Kerja {runId}` (DU-138-2) memuat pasangan Brand dan Model `Olympic` / `OL-138` dan `Lion` / `LN-138`.
- Kondisi:
  - kuota Group `Gudang Tangerang {runId}` dan kuota tenant cukup untuk seluruh pengajuan yang terbentuk.

## Test Steps

### Batch sudah di-Submit oleh sesi lain
1. Rina W di sesi kedua mengirim Submit for Approval atas batch DU-138-4
2. Rina W di sesi pertama menyimpan batch DU-138-4 dengan Quantity `4`
3. Verifikasi Save draft dari sesi pertama ditolak server tanpa mutasi dan Quantity pengajuan hasil Submit tetap `3`
4. Rina W di sesi pertama mengirim autosave atas batch DU-138-4 dengan Quantity `4`
5. Verifikasi autosave dari sesi pertama ditolak server tanpa mutasi
6. Rina W di sesi pertama mengirim Submit for Approval atas batch DU-138-4
7. Verifikasi Submit dari sesi pertama ditolak server dan tidak ada pengajuan kedua yang memuat aset batch itu

### Tag direbut aset lain sebelum Save draft
8. Lina menyimpan batch DU-138-6 dengan memasang Tag `E280-1380-0001 {runId}` pada aset pertama
9. Rina W menyimpan batch DU-138-5 yang masih memuat Tag `E280-1380-0001 {runId}` pada aset pertama
10. Verifikasi batch DU-138-5 tersimpan tanpa Tag `E280-1380-0001 {runId}` dan slot Tag aset pertama kembali `Unverified`
11. Verifikasi respons Save memuat peringatan `E280-1380-0001 {runId} is no longer available. Scan another TAG.`
12. Verifikasi Tag `E280-1380-0001 {runId}` tetap terpasang pada aset pertama batch DU-138-6

### Tag direbut aset lain sebelum Submit
13. Lina menyimpan batch DU-138-8 dengan memasang Tag `E280-1380-0002 {runId}` pada aset pertama
14. Rina W mengirim Submit for Approval atas batch DU-138-7 yang memuat Tag `E280-1380-0002 {runId}` pada aset pertama dan Tag `E280-1380-0003 {runId}` pada aset kedua
15. Verifikasi seluruh Submit ditolak server dan tidak ada pengajuan yang terbentuk dari batch itu
16. Verifikasi slot Tag aset pertama kembali `Unverified` dengan peringatan `E280-1380-0002 {runId} is no longer available. Scan another TAG.`
17. Verifikasi kedua aset batch DU-138-7 tetap Draft dan Tag `E280-1380-0003 {runId}` tetap terpasang pada aset kedua

### Pengajuan dibatalkan atau diputuskan bersamaan dengan keputusan
18. Rina W membatalkan pengajuan DU-138-9
19. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-138-9 yang ia buka sebelum pembatalan
20. Verifikasi keputusan ditolak server tanpa mutasi dan pengajuan DU-138-9 tetap `Canceled`
21. Budi dan Citra mengirim keputusan atas pengajuan DU-138-10 pada saat yang sama: Budi `Approve` untuk kedua aset, Citra `Reject` untuk kedua aset
22. Verifikasi tepat satu dari kedua keputusan atas pengajuan DU-138-10 diterima server dan keputusan yang lain ditolak tanpa mutasi
23. Verifikasi status akhir pengajuan DU-138-10 serta slot Reserved dan Used Group mengikuti hanya keputusan yang diterima server, tanpa pelepasan Reserved ganda

### Delete draft yang sudah dihapus
24. Rina W menghapus batch DU-138-11
25. Rina W menghapus batch DU-138-11 sekali lagi
26. Verifikasi penghapusan kedua ditolak dengan pesan `This draft is no longer available.` tanpa efek ganda

### Edit Active oleh dua user pada aset yang sama tetap menegakkan guard
27. Rina W dan Lina sama-sama membaca aset DU-138-16 dengan Brand `Olympic` dan Model `OL-138`
28. Rina W menyimpan Edit Active atas aset DU-138-16 dengan Brand `Lion` dan Model `LN-138`
29. Lina menyimpan Edit Active atas aset DU-138-16 dari keadaan yang ia baca sebelum Save Rina W, dengan Brand `Merek Tak Terdaftar {runId}`
30. Verifikasi Save Rina W diterima dan Brand aset DU-138-16 bernilai `Lion` dengan Model `LN-138`
31. Verifikasi Save Lina ditolak server karena referensi Brand tidak valid dan aset DU-138-16 tidak berubah oleh Save itu
