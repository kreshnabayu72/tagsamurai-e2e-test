---
id: TC-FA-FAREG-BE-123-operasi-item-aset
title: "Quantity turun, Remove Item, dan Apply to all"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-01r, FAREG-LOGIC-03u, "§9.6#r13", "§9.6#r14", "§9.6#r15"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-01r: [22, 23, 25, 26, 28, 29]
  FAREG-LOGIC-03u: [9, 11]
  "§9.6#r13": [2, 3, 5, 7]
  "§9.6#r14": [9, 11, 13, 14, 16, 18, 19]
  "§9.6#r15": [25, 28, 31]
owner: BE
---

# Quantity turun, Remove Item, dan Apply to all

## Prerequisites
- Aktor: Rina (Manage asset & TAG, Group terkelola `Gudang Semarang {runId}`); Dewi (Manage asset & TAG, Group terkelola `Gudang Semarang {runId}`).
- Data:
  - DU-123-1: Group `Gudang Semarang {runId}`, Assignable, di entitas aktor.
  - DU-123-2: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`.
  - DU-123-3: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-123`, TAG Type `Non-TAG`.
  - DU-123-4: Asset Name `Kursi Kantor {runId}`, Category `Furnitur`, Brand `Chitose`, Model `Orion`, TAG Type `Non-TAG`.
  - DU-123-5: batch Draft milik Rina, Group `Gudang Semarang {runId}`, satu Item `Laptop {runId}` Quantity `3`; aset pertama ber-Tag RFID `E280-1230-0001 {runId}`, aset kedua tanpa Tag, aset ketiga ber-Tag RFID `E280-1230-0002 {runId}`; kedua Tag Reserved atas aset itu.
  - DU-123-6: batch Draft milik Rina, Group `Gudang Semarang {runId}`, Item 1 `Laptop {runId}` Quantity `2` dengan aset pertama ber-Tag RFID `E280-1230-0003 {runId}` (Reserved) dan aset kedua tanpa Tag; Item 2 `Meja Kerja {runId}` Quantity `1` tanpa data.
  - DU-123-7: batch Draft milik Dewi, Group `Gudang Semarang {runId}`, satu Item `Laptop {runId}` Quantity `2`, kedua aset tanpa Tag.
  - DU-123-8: batch Draft milik Rina, Group `Gudang Semarang {runId}`, Item 1 `Meja Kerja {runId}` Quantity `1` dan Item 2 `Kursi Kantor {runId}` Quantity `1`, Tingkat 2 lengkap.
  - DU-123-9: batch Draft milik Rina, Group `Gudang Semarang {runId}`, satu Item `Meja Kerja {runId}` Quantity `3`; aset pertama berFoto `meja-depan.jpg` dan `meja-samping.jpg` dengan Alias Name `Meja Rapat Direksi {runId}`; aset kedua berFoto `meja-atas.jpg` dengan Alias Name `Meja Lama {runId}`; aset ketiga tanpa Foto dengan Alias Name `Meja Cadangan {runId}`.
- Kondisi:
  - Approval Workflow tidak aktif untuk `Gudang Semarang {runId}`.
  - Kuota tenant dan kuota Group `Gudang Semarang {runId}` mencukupi untuk seluruh aset yang diaktifkan spec ini.

## Test Steps

### Quantity turun menghapus aset terakhir dan melepas Tag dalam transaksi yang sama
1. Rina mengirim Save draft atas batch DU-123-5 dengan Quantity Item `Laptop {runId}` diturunkan dari `3` menjadi `2`
2. Verifikasi batch DU-123-5 berisi dua aset `Laptop {runId}`
3. Verifikasi aset ketiga, yang bernomor increment terbesar, sudah dihapus dari batch
4. Dewi memindai Tag `E280-1230-0002 {runId}` pada aset pertama batch DU-123-7
5. Verifikasi pemindaian Tag `E280-1230-0002 {runId}` diterima dan slot Tag berstatus `Verified`
6. Dewi memindai Tag `E280-1230-0001 {runId}` pada aset kedua batch DU-123-7
7. Verifikasi pemindaian ditolak dengan pesan yang memuat Tag `E280-1230-0001 {runId}` dan status `Reserved` karena aset pertama batch DU-123-5 tetap memegang Tag itu

### Remove Item melepas Tag aset Item dan menjaga minimal satu Item
8. Rina mengirim Remove Item atas Item `Laptop {runId}` pada batch DU-123-6
9. Verifikasi Item `Laptop {runId}` beserta kedua asetnya sudah dihapus dari batch DU-123-6
10. Dewi memindai Tag `E280-1230-0003 {runId}` pada aset kedua batch DU-123-7
11. Verifikasi pemindaian Tag `E280-1230-0003 {runId}` diterima dan slot Tag berstatus `Verified`
12. Rina mengirim Remove Item atas Item `Meja Kerja {runId}` pada batch DU-123-6, satu-satunya Item yang tersisa
13. Verifikasi Remove Item ditolak server karena batch minimal berisi satu Item
14. Verifikasi batch DU-123-6 tetap berisi Item `Meja Kerja {runId}` dengan satu aset

### Remove Item atas batch yang sudah di-Submit ditolak
15. Rina mengirim Submit atas batch DU-123-8
16. Verifikasi kedua aset batch DU-123-8 berstatus Active
17. Rina mengirim Remove Item atas Item `Kursi Kantor {runId}` pada batch DU-123-8
18. Verifikasi Remove Item ditolak server tanpa mutasi karena aset Item tidak lagi Draft
19. Verifikasi aset `Kursi Kantor {runId}` tetap berstatus Active

### Apply to all gagal total atau mengganti nilai tanpa menggabung
20. Rina mencatat Foto dan Alias Name aset kedua dan ketiga batch DU-123-9
21. Rina mengirim Apply to all atas Alias Name aset pertama batch DU-123-9 dengan nilai sumber `Meja rapat utama di lantai tiga gedung timur dengan kaca bening besar untuk rapat direksi bulanan dan tamu cabang Bandung` (121 karakter)
22. Verifikasi Apply to all ditolak server dengan pesan `Max. 120 characters`
23. Verifikasi Foto dan Alias Name aset kedua dan ketiga sama dengan catatan langkah 20
24. Rina mengirim Apply to all atas Foto aset pertama batch DU-123-9
25. Verifikasi aset kedua dan ketiga masing-masing memiliki tepat dua Foto, yaitu `meja-depan.jpg` dan `meja-samping.jpg`
26. Verifikasi Foto `meja-atas.jpg` tidak lagi ada pada aset kedua
27. Rina mengirim Apply to all atas Alias Name aset pertama batch DU-123-9
28. Verifikasi aset kedua dan ketiga masing-masing memiliki Alias Name `Meja Rapat Direksi {runId}`
29. Verifikasi Alias Name `Meja Lama {runId}` dan `Meja Cadangan {runId}` tidak lagi ada pada aset mana pun
30. Rina mengirim ulang Apply to all atas Alias Name aset pertama batch DU-123-9
31. Verifikasi batch DU-123-9 tetap berisi tiga aset dan setiap aset hanya memiliki Alias Name `Meja Rapat Direksi {runId}`
