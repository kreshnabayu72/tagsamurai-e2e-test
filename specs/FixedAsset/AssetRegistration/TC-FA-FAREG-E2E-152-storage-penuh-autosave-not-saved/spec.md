---
id: TC-FA-FAREG-E2E-152-storage-penuh-autosave-not-saved
title: "Storage penuh: Autosave dengan Photo baru ditolak tanpa toast dan indikator Not saved"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["S-REG-25", "FAREG-LOGIC-01q", "FAREG-LOGIC-22b"]
smoke: []
dependsOn: []
trace:
  "S-REG-25": [8, 12]
  "FAREG-LOGIC-01q": [8, 10, 14]
  "FAREG-LOGIC-22b": [8, 9, 20]
anchor: []
coverage:
  web: automated
---

# Storage penuh: Autosave dengan Photo baru ditolak tanpa toast dan indikator Not saved

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Foto Penuh Autosave {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - Spec ini memakai entitas khusus `Klien Penuh Autosave {runId}` yang tidak dipakai spec lain.
  - DU-152-1: Client `Klien Penuh Autosave {runId}` dengan Storage Quota `50.0 GB` dan Storage Usage `50.0 GB`.
  - DU-152-2: Draft tersimpan milik `Rina W` untuk Group `Gudang Foto Penuh Autosave {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`; aset 1 tanpa Photo.
  - Berkas uji: `foto-baru.jpg` (JPG, 800 KB).

## Test Steps
### Autosave yang ditolak menampilkan Not saved tanpa toast dan mempertahankan data form
1. Ketik Search `Gudang Foto Penuh Autosave {runId}`, tekan Enter
2. Klik Group `Gudang Foto Penuh Autosave {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 1
5. Pilih berkas `foto-baru.jpg` pada area `Add photo`
6. Klik `Apply` pada dialog `Adjust photo`
7. Waktu berlalu sampai 20 detik sejak perubahan
8. Verifikasi subjudul form menampilkan `Not saved`
9. Verifikasi tidak ada toast yang tampil
10. Verifikasi kolom Photo aset 1 menampilkan `1` pada form karena data yang diisi dipertahankan
11. Klik tab `General Information`
12. Verifikasi subjudul form pada tab `General Information` juga menampilkan `Not saved`

### Autosave dicoba lagi pada siklus berikutnya dan draft tidak berubah
13. Waktu berlalu sampai 20 detik berikutnya
14. Verifikasi subjudul form masih menampilkan `Not saved` setelah siklus Autosave berikutnya
15. Klik breadcrumb `Draft`
16. Klik `[Leave]` pada dialog `Unsaved Changes`
17. Ketik Search `Gudang Foto Penuh Autosave {runId}`, tekan Enter
18. Klik Group `Gudang Foto Penuh Autosave {runId}` pada baris untuk membuka form Edit
19. Klik tab `Asset`
20. Verifikasi kolom Photo aset 1 menampilkan `—` karena Autosave yang ditolak tidak mengubah draft
