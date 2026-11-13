---
id: TC-FA-FAREG-E2E-097-mobile-card-draft
title: "Sub tab Draft mobile: card dan aksi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-20p", "§4.6#b2", "§4.6#b3", "§4.6#b4", "§4.6#b5", "§4.6#b6"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-20p": 2
  "§4.6#b2": [3, 11, 18]
  "§4.6#b3": [8, 9, 11, 14]
  "§4.6#b4": [20, 22, 23, 26]
  "§4.6#b5": [4, 5, 6, 7]
  "§4.6#b6": 16
anchor: [1, 25]
coverage:
  android: automated
---

# Sub tab Draft mobile: card dan aksi

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}` dan `Gudang 2 {runId}`).
- Layar awal: Registration mobile, sub tab `Draft`.
- Data:
  - DU-097-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`.
  - DU-097-2: Batch Draft dengan Group `Gudang 2 {runId}`, Origin `—`, Total Asset `5`, Progress `60%`, Requested By `Rina W`, Last Updated `T0 − 2 hari`.
  - DU-097-3: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}` dan `Gudang 2 {runId}`).

## Test Steps

### Sub tab Draft tampil sebagai card dan hanya sub tab Draft tersedia
1. Verifikasi sub tab `Draft` tampil pada Registration mobile
2. Verifikasi sub tab `Waiting for Approval` dan `History` tidak tersedia pada Registration mobile
3. Verifikasi daftar Draft tampil sebagai card `Gudang 1 {runId}` dan card `Gudang 2 {runId}`, bukan tabel
4. Verifikasi card `Gudang 1 {runId}` memuat Group `Gudang 1 {runId}`
5. Verifikasi card `Gudang 1 {runId}` memuat Progress `0%`
6. Verifikasi card `Gudang 1 {runId}` memuat Requested By `Rina W`
7. Verifikasi card `Gudang 1 {runId}` memuat tombol `[⋯]`

### Toolbar menjadi tombol dan ikon pencarian inline
8. Verifikasi tombol `[⋯]` toolbar tampil di atas daftar card
9. Verifikasi ikon `[🔍]` tampil di atas daftar card
10. Klik tombol `[⋯]` toolbar
11. Verifikasi bottom sheet toolbar terbuka
12. Tutup bottom sheet toolbar
13. Klik ikon `[🔍]`
14. Verifikasi kotak pencarian inline tampil

### Aksi pada card Draft
15. Klik `[⋯]` pada card `Gudang 1 {runId}`
16. Verifikasi menu aksi card `Gudang 1 {runId}` memuat `Edit`, `Delete`, dan `Registration Log`
17. Klik `Registration Log`
18. Verifikasi dialog Registration Log tampil sebagai bottom sheet
19. Tutup bottom sheet Registration Log

### Multi-select hanya lewat long-press
20. Verifikasi card `Gudang 1 {runId}` dan card `Gudang 2 {runId}` tidak menampilkan checkbox
21. Tekan lama card `Gudang 1 {runId}`
22. Verifikasi card `Gudang 1 {runId}` terpilih dan bilah aksi massal menampilkan `1 Selected`
23. Verifikasi checkbox kosong tampil pada card `Gudang 2 {runId}`
24. Klik `✕` pada bilah aksi massal
25. Verifikasi card `Gudang 2 {runId}` tetap tampil sesudah bilah aksi massal ditutup
26. Verifikasi checkbox tidak tampil lagi pada card `Gudang 2 {runId}`
