---
id: TC-FA-FAREG-BE-149-storage-penuh-photo-ditolak
title: "Storage penuh: upload Photo baru ditolak seluruhnya tanpa mutasi"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-22b", "V-REG-23", "FAREG-LOGIC-01q", "FAREG-LOGIC-22a"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-22b": [2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 18, 19, 21, 22, 24, 25, 27, 30, 31]
  "V-REG-23": [2, 10, 13, 16, 21]
  "FAREG-LOGIC-01q": 7
  "FAREG-LOGIC-22a": [27, 28]
anchor: [17]
owner: BE
---

# Storage penuh: upload Photo baru ditolak seluruhnya tanpa mutasi

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Foto Penuh {runId}`); Toni P (Total Control, seluruh entitas `Klien Storage Penuh {runId}`); Hana K (Manage asset & TAG, Group terkelola `Gudang Foto Bebas {runId}`).
- Data:
  - DU-149-1: Client `Klien Storage Penuh {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-149-2: Client `Klien Tanpa Kuota Storage {runId}` tanpa Storage Quota.
  - DU-149-3: Group `Gudang Foto Penuh {runId}` di entitas `Klien Storage Penuh {runId}` dan Group `Gudang Foto Bebas {runId}` di entitas `Klien Tanpa Kuota Storage {runId}`, keduanya Assignable.
  - DU-149-4: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, ada di kedua entitas.
  - DU-149-5: batch Draft A milik Rina W, Group `Gudang Foto Penuh {runId}`, satu Item `Laptop {runId}` Quantity `2`, Condition `Normal`, Tingkat 2 lengkap; aset 1 ber-Photo `foto-lama.jpg` dengan Alias Name `Laptop Lama {runId}`; aset 2 tanpa Photo dengan Alias Name `Laptop Dua {runId}`.
  - DU-149-6: batch Draft B milik Rina W, Group `Gudang Foto Penuh {runId}`, satu Item `Laptop {runId}` Quantity `2`, Condition `Normal`, Tingkat 2 lengkap; kedua aset tanpa Photo.
  - DU-149-7: batch Draft C milik Rina W, Group `Gudang Foto Penuh {runId}`, satu Item `Laptop {runId}` Quantity `1`, Condition `Normal`, Tingkat 2 lengkap; aset ber-Photo `foto-kosong-lama.jpg`.
  - DU-149-8: Tag RFID `E280-1490-0001 {runId}` yang belum dipakai aset mana pun di entitas `Klien Storage Penuh {runId}`.
  - DU-149-9: aset Active `Laptop Aktif {runId}` di Group `Gudang Foto Penuh {runId}` ber-Photo `foto-aktif.jpg`.
  - DU-149-10: batch Draft D milik Hana K, Group `Gudang Foto Bebas {runId}`, satu Item `Laptop {runId}` Quantity `1`, Condition `Normal`, Tingkat 2 lengkap, tanpa Photo.
  - Berkas uji: `foto-baru.jpg` (JPG, 800 KB) dan `dokumen-aset.pdf`.
- Kondisi:
  - Approval Workflow tidak aktif untuk kedua Group.
  - Kuota tenant dan kuota Group mencukupi untuk seluruh aset yang diaktifkan spec ini.

## Test Steps
### Save draft dengan Photo baru ditolak seluruhnya
1. Rina W mengirim Save draft atas batch DU-149-5 dengan Photo `foto-baru.jpg` pada aset 2 dan Alias Name aset 1 diganti menjadi `Laptop Baru {runId}`
2. Verifikasi Save draft ditolak karena Storage penuh dengan pesan yang memuat pemakaian `50.0 GB` dan kuota `50.0 GB`
3. Verifikasi aset 2 batch DU-149-5 tetap tanpa Photo
4. Verifikasi Alias Name aset 1 batch DU-149-5 tetap `Laptop Lama {runId}` karena operasi ditolak seluruhnya
5. Verifikasi Photo aset 1 batch DU-149-5 tetap `foto-lama.jpg`

### Autosave dengan Photo baru ditolak tanpa mutasi
6. Rina W mengirim Autosave atas batch DU-149-5 dengan Photo `foto-baru.jpg` pada aset 2
7. Verifikasi Autosave ditolak karena Storage penuh
8. Verifikasi aset 2 batch DU-149-5 tetap tanpa Photo

### Apply to all Photo ditolak seluruhnya
9. Rina W mengirim Apply to all atas Photo aset 1 batch DU-149-5
10. Verifikasi Apply to all ditolak karena Storage penuh
11. Verifikasi aset 2 batch DU-149-5 tetap tanpa Photo

### Activate dengan Photo baru ditolak, seluruh aset tetap Draft
12. Rina W mengirim Activate atas batch DU-149-6 dengan Photo `foto-baru.jpg` pada aset 1
13. Verifikasi Activate ditolak karena Storage penuh
14. Verifikasi kedua aset batch DU-149-6 tetap berstatus Draft

### Send mobile dengan Photo baru ditolak, Draft tidak terbentuk dan Tag tidak Reserved
15. Rina W mengirim Send mobile atas Tag `E280-1490-0001 {runId}` dengan Photo `foto-baru.jpg`
16. Verifikasi Send mobile ditolak karena Storage penuh
17. Verifikasi daftar Draft Rina W tetap memuat batch DU-149-5, batch DU-149-6, dan batch DU-149-7
18. Verifikasi tidak ada batch Draft yang memuat aset ber-Tag `E280-1490-0001 {runId}`
19. Verifikasi Tag `E280-1490-0001 {runId}` tidak berstatus `Reserved`

### Edit Active dengan Photo baru ditolak
20. Toni P mengirim Edit Active atas aset `Laptop Aktif {runId}` dengan Photo `foto-baru.jpg`
21. Verifikasi Edit Active ditolak karena Storage penuh
22. Verifikasi Photo aset `Laptop Aktif {runId}` tetap `foto-aktif.jpg`

### Penolakan format didahulukan atas Storage penuh
23. Rina W mengirim Save draft atas batch DU-149-5 dengan berkas `dokumen-aset.pdf` pada aset 2
24. Verifikasi Save draft ditolak dengan pesan `Unsupported format. Please upload JPG, PNG, or JPEG.`
25. Verifikasi pesan penolakan tidak menyebut Storage penuh

### Photo dikosongkan tanpa pengganti tidak dicek Storage
26. Rina W mengirim Save draft atas batch DU-149-7 dengan Photo aset dikosongkan tanpa pengganti
27. Verifikasi Save draft berhasil
28. Verifikasi aset batch DU-149-7 tidak lagi memiliki Photo

### Client tanpa kuota Storage tidak diblokir
29. Hana K mengirim Save draft atas batch DU-149-10 dengan Photo `foto-baru.jpg` pada aset 1
30. Verifikasi Save draft berhasil
31. Verifikasi aset 1 batch DU-149-10 memiliki Photo `foto-baru.jpg`
