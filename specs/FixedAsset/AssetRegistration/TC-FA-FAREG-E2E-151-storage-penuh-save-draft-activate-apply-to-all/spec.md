---
id: TC-FA-FAREG-E2E-151-storage-penuh-save-draft-activate-apply-to-all
title: "Storage penuh: Save draft, Submit, dan Apply to all dengan Photo baru ditolak dengan toast Error persisten"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["T-REG-19", "FAREG-LOGIC-22b", "V-REG-23"]
smoke: []
dependsOn: []
trace:
  "T-REG-19": [9, 11, 16, 26]
  "FAREG-LOGIC-22b": [9, 12, 16, 20, 23, 26, 27]
  "V-REG-23": 13
anchor: [7]
coverage:
  web: automated
---

# Storage penuh: Save draft, Submit, dan Apply to all dengan Photo baru ditolak dengan toast Error persisten

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Foto Penuh Simpan {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - Spec ini memakai entitas khusus `Klien Penuh Simpan {runId}` yang tidak dipakai spec lain.
  - DU-151-1: Client `Klien Penuh Simpan {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-151-2: Group `Gudang Foto Penuh Simpan {runId}` ber-toggle `Require Approval for Registration` OFF.
  - DU-151-3: Draft tersimpan milik `Rina W` untuk Group `Gudang Foto Penuh Simpan {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `2`, Condition `Normal`, TAG Type `Non-TAG`, seluruh aset memenuhi Tingkat 2. Aset 1: Photo `2`. Aset 2: Photo `1`.
  - Berkas uji: `foto-baru.jpg` (JPG, 800 KB).

## Test Steps
### Save draft dengan Photo baru ditolak dan data form dipertahankan
1. Ketik Search `Gudang Foto Penuh Simpan {runId}`, tekan Enter
2. Klik Group `Gudang Foto Penuh Simpan {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 2
5. Pilih berkas `foto-baru.jpg` pada area `Add photo`
6. Klik `Apply` pada dialog `Adjust photo`
7. Verifikasi kolom Photo aset 2 menampilkan `2` pada form
8. Klik `[Save draft]`
9. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
10. Waktu berlalu 10 detik tanpa menutup toast
11. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` masih tampil karena Error persisten
12. Verifikasi kolom Photo aset 2 tetap menampilkan `2` pada form karena data yang diisi dipertahankan
13. Verifikasi bagian Photo pada panel samping tidak menampilkan pesan error inline

### Submit dengan Photo baru ditolak dan seluruh aset tetap Draft
14. Klik `[Submit]`
15. Klik `[Activate]` pada dialog konfirmasi
16. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
17. Klik breadcrumb `Draft`
18. Klik `[Leave]` pada dialog `Unsaved Changes`
19. Ketik Search `Gudang Foto Penuh Simpan {runId}`, tekan Enter
20. Verifikasi baris Group `Gudang Foto Penuh Simpan {runId}` tampil di sub tab `Draft` dengan Total Asset `2`
21. Klik Group `Gudang Foto Penuh Simpan {runId}` pada baris untuk membuka form Edit
22. Klik tab `Asset`
23. Verifikasi kolom Photo aset 2 menampilkan `1` karena Save draft dan Submit yang ditolak tidak mengubah draft

### Apply to all Photo ditolak dan Photo aset tujuan tidak berubah
24. Klik row option `Detail` pada aset 1
25. Klik `Apply to all` pada bagian Photo di panel samping aset
26. Verifikasi toast `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
27. Verifikasi kolom Photo aset 2 tetap menampilkan `1`
