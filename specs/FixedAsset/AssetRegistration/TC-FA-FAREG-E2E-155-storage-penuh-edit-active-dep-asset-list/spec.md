---
id: TC-FA-FAREG-E2E-155-storage-penuh-edit-active-dep-asset-list
title: "Storage penuh: Edit Active dengan Photo baru ditolak dan Photo aktif tidak berubah"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["T-REG-19", "FAREG-LOGIC-22b", "V-REG-23"]
smoke: []
dependsOn: ["Asset List: Row Action Edit aset Active"]
trace:
  "T-REG-19": 5
  "FAREG-LOGIC-22b": [5, 8]
  "V-REG-23": 5
anchor: []
coverage:
  web: automated
---

# Storage penuh: Edit Active dengan Photo baru ditolak dan Photo aktif tidak berubah

## Prerequisites
- Aktor: Toni E (Total Control, seluruh entitas `Klien Penuh Edit {runId}`).
- Layar awal: Fixed Asset > Assets > Assets.
- Data:
  - Spec ini memakai entitas khusus `Klien Penuh Edit {runId}` yang tidak dipakai spec lain.
  - DU-155-1: Client `Klien Penuh Edit {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-155-2: aset Active `Laptop Foto Penuh {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `Non-TAG`, Condition `Normal`, ber-Photo `foto-aktif.jpg`.
  - Berkas uji: `foto-baru.jpg` (JPG, 800 KB).

## Test Steps
### Edit Active dengan Photo baru ditolak
1. Toni E mengetik Search `Laptop Foto Penuh {runId}`, tekan Enter
2. Toni E klik row action `Edit` pada baris aset `Laptop Foto Penuh {runId}`
3. Toni E mengunggah Photo `foto-baru.jpg`
4. Toni E menyimpan perubahan aset
5. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
6. Toni E menutup form Edit aset tanpa menyimpan
7. Toni E klik row action `Detail` pada baris aset `Laptop Foto Penuh {runId}`
8. Verifikasi Photo `foto-aktif.jpg` tampil pada aset
