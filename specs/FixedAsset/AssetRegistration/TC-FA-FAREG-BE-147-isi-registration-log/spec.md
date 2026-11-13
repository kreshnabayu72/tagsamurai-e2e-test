---
id: TC-FA-FAREG-BE-147-isi-registration-log
title: "Registration Log: penggabungan entri dan isi per event"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-07f, FAREG-LOGIC-21a, "§8#b2", "§8.3#r2"]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-07f: [20, 37]
  FAREG-LOGIC-21a: [19, 36]
  "§8#b2": [7, 8]
  "§8.3#r2": [5, 7, 11, 15, 20, 27, 32, 37]
---

# Registration Log: penggabungan entri dan isi per event

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Batam {runId}`) sebagai pengaju.
  - Agus P (Group Manager Group `Gudang Batam {runId}`) sebagai approver.
- Data:
  - DU-147-1: Group `Gudang Batam {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-147-2: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-147` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-147-3: batch Draft milik Rina W di Group `Gudang Batam {runId}`, Item `Meja Kerja {runId}` Quantity `2`, belum pernah diedit sesudah dibuat.
  - DU-147-4: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Batam {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-147`.
  - DU-147-8: batch Draft milik Rina W di Group `Gudang Batam {runId}`, Item `Meja Kerja {runId}` Brand `Olympic` Model `OL-147` Quantity `1`, belum pernah diedit sesudah dibuat.
  - DU-147-9: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-147-10: batch Draft milik Rina W di Group `Gudang Batam {runId}`, Item `Laptop {runId}` Quantity `1`, belum pernah diedit sesudah dibuat.
  - DU-147-12: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Batam {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-147`.
- Kondisi:
  - kuota Group `Gudang Batam {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.
  - Tag `E280-1470-0001 {runId}` terdaftar di registri Global dengan status `Available`.

## Test Steps

### Entri Draft edited digabung per sesi edit dan ditulis saat kunci dilepas
1. Rina W membuka form batch DU-147-3 sehingga memegang kunci sesi edit
2. Rina W menyimpan batch DU-147-3 dengan Quantity `3`
3. Rina W mengirim autosave atas batch DU-147-3 dengan Alias Name aset pertama `Meja Rapat {runId}`
4. Rina W menyimpan batch DU-147-3 dengan Quantity `4`
5. Verifikasi Registration Log batch belum memuat node `Draft edited by Rina W` untuk sesi ini karena kunci sesi belum dilepas
6. Rina W keluar dari form batch DU-147-3 sehingga kunci sesi edit dilepas
7. Verifikasi Registration Log batch memuat tepat satu node `Draft edited by Rina W` untuk seluruh sesi edit, bukan satu node per Save atau autosave
8. Verifikasi node itu tanpa isi entri sehingga tidak memuat field dan nilai

### Sesi tanpa perubahan tidak menambah entri dan sesi berikutnya menambah satu entri
9. Rina W membuka form batch DU-147-3
10. Rina W keluar dari form batch DU-147-3 tanpa mengubah apa pun
11. Verifikasi Registration Log batch tetap memuat satu node `Draft edited by Rina W`
12. Rina W membuka form batch DU-147-3
13. Rina W menyimpan batch DU-147-3 dengan Quantity `5`
14. Rina W keluar dari form batch DU-147-3
15. Verifikasi Registration Log batch memuat dua node `Draft edited by Rina W`, satu per sesi edit yang mengubah data

### Keputusan approval mencatat node keputusan dan satu node Draft edited untuk aset yang disetujui
16. Agus P menyimpan koreksi Brand aset pertama pengajuan DU-147-4 menjadi `Chitose` dengan Model `Orion`
17. Agus P menyimpan koreksi Brand aset kedua pengajuan DU-147-4 menjadi `Chitose` dengan Model `Orion`
18. Agus P mengirim satu keputusan atas pengajuan DU-147-4: aset pertama `Approve`, aset kedua `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
19. Verifikasi Registration Log pengajuan memuat node `Partially approved by Agus P` dengan Jumlah Approved `1`, Returned `0`, dan Rejected `1`
20. Verifikasi Registration Log pengajuan memuat tepat satu node `Draft edited by Agus P` untuk koreksi yang diterapkan hanya pada aset yang disetujui

### Sesi yang mengubah Item menghasilkan satu entri Draft edited
21. Rina W membuka form batch DU-147-8 sehingga memegang kunci sesi edit
22. Rina W menambah Item `Meja Kerja {runId}` Brand `Chitose` Model `Orion` Quantity `1` lewat `[+ Asset Name]`
23. Rina W menyimpan batch DU-147-8
24. Rina W menghapus Item pertama batch DU-147-8 lewat Remove Item
25. Rina W menyimpan batch DU-147-8
26. Rina W keluar dari form batch DU-147-8 sehingga kunci sesi edit dilepas
27. Verifikasi Registration Log batch DU-147-8 memuat tepat satu node `Draft edited by Rina W` untuk sesi yang menambah dan menghapus Item

### Sesi yang hanya memindai Tag menghasilkan satu entri Draft edited
28. Rina W membuka form batch DU-147-10 sehingga memegang kunci sesi edit
29. Rina W memindai Tag `E280-1470-0001 {runId}` pada aset pertama
30. Rina W menyimpan batch DU-147-10
31. Rina W keluar dari form batch DU-147-10 sehingga kunci sesi edit dilepas
32. Verifikasi Registration Log batch DU-147-10 memuat tepat satu node `Draft edited by Rina W` untuk sesi yang hanya memindai Tag

### Koreksi hanya pada aset yang ditolak tidak menghasilkan node Draft edited
33. Agus P menyimpan koreksi Brand aset pertama pengajuan DU-147-12 menjadi `Chitose` dengan Model `Orion`
34. Agus P menyimpan koreksi Brand aset kedua pengajuan DU-147-12 menjadi `Chitose` dengan Model `Orion`
35. Agus P mengirim satu keputusan atas pengajuan DU-147-12: kedua aset `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
36. Verifikasi Registration Log pengajuan DU-147-12 memuat node `Rejected by Agus P`
37. Verifikasi Registration Log pengajuan DU-147-12 tidak memuat node `Draft edited by Agus P` karena tidak ada aset yang disetujui
