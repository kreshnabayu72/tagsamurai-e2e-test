---
id: TC-FA-FAREG-E2E-153-storage-penuh-format-tidak-didukung-didahulukan
title: "Storage penuh: format Photo yang tidak didukung ditolak dengan pesan format, bukan toast Storage penuh"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-22b", "V-REG-23"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-22b": [6, 8]
  "V-REG-23": 8
anchor: [7]
coverage:
  web: automated
---

# Storage penuh: format Photo yang tidak didukung ditolak dengan pesan format, bukan toast Storage penuh

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Foto Penuh Format {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - Spec ini memakai entitas khusus `Klien Penuh Format {runId}` yang tidak dipakai spec lain.
  - DU-153-1: Client `Klien Penuh Format {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-153-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Foto Penuh Format {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`; aset 1 ber-Photo `1`.
  - Berkas uji: `dokumen-aset.pdf`.

## Test Steps
### Format tidak didukung didahulukan atas penolakan Storage penuh
1. Ketik Search `Gudang Foto Penuh Format {runId}`, tekan Enter
2. Klik Group `Gudang Foto Penuh Format {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 1
5. Pilih berkas `dokumen-aset.pdf` pada area `Add photo`
6. Verifikasi pesan `Unsupported format. Please upload JPG, PNG, or JPEG.` tampil pada bagian Photo
7. Verifikasi kolom Photo aset 1 tetap menampilkan `1`
8. Verifikasi tidak ada toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).`
