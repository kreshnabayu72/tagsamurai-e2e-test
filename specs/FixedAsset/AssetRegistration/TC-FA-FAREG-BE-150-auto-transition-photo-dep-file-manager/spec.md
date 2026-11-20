---
id: TC-FA-FAREG-BE-150-auto-transition-photo-dep-file-manager
title: "Photo diganti atau dikosongkan: file lama soft-delete ke Recycle Bin File Manager, penolakan Storage penuh tidak soft-delete"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FAREG-LOGIC-22a", "FAREG-LOGIC-22b"]
smoke: []
dependsOn: ["File Manager: Recycle Bin"]
trace:
  "FAREG-LOGIC-22a": [2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16]
  "FAREG-LOGIC-22b": [19, 20, 21]
owner: BE
---

# Photo diganti atau dikosongkan: file lama soft-delete ke Recycle Bin File Manager, penolakan Storage penuh tidak soft-delete

## Prerequisites
- Aktor: Rina T (Manage asset & TAG, Group terkelola `Gudang Transisi {runId}`); Toni F (Total Control, seluruh entitas `Klien Foto Transisi {runId}`); Gita P (Manage asset & TAG, Group terkelola `Gudang Transisi Penuh {runId}`).
- Data:
  - DU-150-1: Client `Klien Foto Transisi {runId}` dengan Storage tersedia di bawah kuota.
  - DU-150-2: Client `Klien Foto Transisi Penuh {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-150-3: Group `Gudang Transisi {runId}` di entitas `Klien Foto Transisi {runId}` dan Group `Gudang Transisi Penuh {runId}` di entitas `Klien Foto Transisi Penuh {runId}`, keduanya Assignable.
  - DU-150-4: Asset Name `Laptop {runId}`, Category `IT Equipment`, Brand `Dell`, Model `Latitude 5440`, TAG Type `Non-TAG`, ada di kedua entitas.
  - DU-150-5: batch Draft P milik Rina T, Group `Gudang Transisi {runId}`, satu Item `Laptop {runId}` Quantity `2`; aset 1 ber-Photo `foto-ganti-lama.jpg`; aset 2 ber-Photo `foto-apply-lama.jpg`.
  - DU-150-6: batch Draft Q milik Rina T, Group `Gudang Transisi {runId}`, satu Item `Laptop {runId}` Quantity `1`, aset ber-Photo `foto-kosong-lama.jpg`.
  - DU-150-7: batch Draft R milik Rina T, Group `Gudang Transisi {runId}`, satu Item `Laptop {runId}` Quantity `1`, aset ber-Photo `foto-autosave-lama.jpg`.
  - DU-150-8: aset Active `Laptop Aktif Transisi {runId}` di Group `Gudang Transisi {runId}` ber-Photo `foto-aktif-lama.jpg`.
  - DU-150-9: batch Draft S milik Gita P, Group `Gudang Transisi Penuh {runId}`, satu Item `Laptop {runId}` Quantity `1`, aset ber-Photo `foto-penuh-lama.jpg`.
  - Berkas uji: `foto-ganti-baru.jpg`, `foto-autosave-baru.jpg`, `foto-aktif-baru.jpg`, dan `foto-penuh-baru.jpg`, semuanya JPG di bawah 1 MB.
- Kondisi:
  - Approval Workflow tidak aktif untuk kedua Group.

## Test Steps
### Ganti Photo lewat Save draft: file lama soft-delete oleh System
1. Rina T mengirim Save draft atas batch DU-150-5 dengan Photo aset 1 diganti dari `foto-ganti-lama.jpg` menjadi `foto-ganti-baru.jpg`
2. Verifikasi Save draft berhasil
3. Verifikasi Photo aset 1 batch DU-150-5 adalah `foto-ganti-baru.jpg`
4. Verifikasi Recycle Bin File Manager entitas `Klien Foto Transisi {runId}` memuat `foto-ganti-lama.jpg` dengan Source `Asset Photo` dan Deleted By `System`

### Apply to all Photo: foto lama aset tujuan soft-delete oleh System
5. Rina T mengirim Apply to all atas Photo aset 1 batch DU-150-5
6. Verifikasi Apply to all berhasil
7. Verifikasi Recycle Bin File Manager entitas `Klien Foto Transisi {runId}` memuat `foto-apply-lama.jpg` dengan Source `Asset Photo` dan Deleted By `System`

### Photo dikosongkan: file lama soft-delete atas nama pengguna pelaku
8. Rina T mengirim Save draft atas batch DU-150-6 dengan Photo aset dikosongkan tanpa pengganti
9. Verifikasi Save draft berhasil
10. Verifikasi Recycle Bin File Manager entitas `Klien Foto Transisi {runId}` memuat `foto-kosong-lama.jpg` dengan Source `Asset Photo` dan Deleted By `Rina T`

### Autosave yang mengganti Photo: file lama soft-delete
11. Rina T mengirim Autosave atas batch DU-150-7 dengan Photo aset diganti dari `foto-autosave-lama.jpg` menjadi `foto-autosave-baru.jpg`
12. Verifikasi Autosave berhasil
13. Verifikasi Recycle Bin File Manager entitas `Klien Foto Transisi {runId}` memuat `foto-autosave-lama.jpg` dengan Source `Asset Photo` dan Deleted By `System`

### Edit Active yang mengganti Photo: file lama soft-delete
14. Toni F mengirim Edit Active atas aset `Laptop Aktif Transisi {runId}` dengan Photo diganti dari `foto-aktif-lama.jpg` menjadi `foto-aktif-baru.jpg`
15. Verifikasi Edit Active berhasil
16. Verifikasi Recycle Bin File Manager entitas `Klien Foto Transisi {runId}` memuat `foto-aktif-lama.jpg` dengan Source `Asset Photo` dan Deleted By `System`

### Penggantian ditolak Storage penuh: file lama tidak soft-delete
17. Gita P mencatat jumlah entri Recycle Bin File Manager entitas `Klien Foto Transisi Penuh {runId}`
18. Gita P mengirim Save draft atas batch DU-150-9 dengan Photo aset diganti dari `foto-penuh-lama.jpg` menjadi `foto-penuh-baru.jpg`
19. Verifikasi Save draft ditolak karena Storage penuh
20. Verifikasi Photo aset batch DU-150-9 tetap `foto-penuh-lama.jpg`
21. Verifikasi jumlah entri Recycle Bin File Manager entitas `Klien Foto Transisi Penuh {runId}` sama dengan jumlah yang dicatat
