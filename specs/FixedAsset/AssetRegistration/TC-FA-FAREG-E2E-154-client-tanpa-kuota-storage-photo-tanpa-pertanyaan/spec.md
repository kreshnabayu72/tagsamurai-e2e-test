---
id: TC-FA-FAREG-E2E-154-client-tanpa-kuota-storage-photo-tanpa-pertanyaan
title: "Client tanpa kuota Storage: Photo baru tidak diblokir dan penggantian Photo tidak menanyakan File Manager"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FAREG-LOGIC-22b", "FAREG-LOGIC-22a"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-22b": [8, 9, 12]
  "FAREG-LOGIC-22a": [13, 14]
anchor: []
coverage:
  web: automated
---

# Client tanpa kuota Storage: Photo baru tidak diblokir dan penggantian Photo tidak menanyakan File Manager

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Foto Tanpa Kuota {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - Spec ini memakai entitas khusus `Klien Tanpa Kuota Foto {runId}` yang tidak dipakai spec lain.
  - DU-154-1: Client `Klien Tanpa Kuota Foto {runId}` tanpa Storage Quota.
  - DU-154-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Foto Tanpa Kuota {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`. Aset 1: Photo `2`. Aset 2: Photo `1`.
  - Berkas uji: `foto-baru.jpg` (JPG, 800 KB).

## Test Steps
### Photo baru pada Save draft tidak diblokir
1. Ketik Search `Gudang Foto Tanpa Kuota {runId}`, tekan Enter
2. Klik Group `Gudang Foto Tanpa Kuota {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 2
5. Pilih berkas `foto-baru.jpg` pada area `Add photo`
6. Klik `Apply` pada dialog `Adjust photo`
7. Klik `[Save draft]`
8. Verifikasi toast `Success, draft has been saved.` tampil
9. Verifikasi kolom Photo aset 2 menampilkan `2`

### Apply to all Photo mengganti foto aset tujuan tanpa pertanyaan tentang File Manager
10. Klik row option `Detail` pada aset 1
11. Klik `Apply to all` pada bagian Photo di panel samping aset
12. Verifikasi toast `Success, the value has been applied to all assets in the item.` tampil
13. Verifikasi tidak ada dialog yang menanyakan nasib file di File Manager
14. Verifikasi kolom Photo aset 2 menampilkan `2`
