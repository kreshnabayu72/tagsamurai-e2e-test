---
id: TC-FA-DAMAGED-E2E-055-hapus-group-dep-groups
title: "Group yang memiliki record berjalan tidak dapat dihapus, dan Group yang dihapus sesudah record-nya selesai dibersihkan dari kriteria filter sub-tab Active saat re-apply"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-DMG-11", "§9.4.2#r17", "§9.4.4#r13", "§9.4.1#r14", "EB-FLT-7"]
smoke: []
dependsOn:
  - "Groups: hapus Group"
trace:
  "V-DMG-11": [2, 3]
  "§9.4.2#r17": [2, 3, 6]
  "§9.4.4#r13": [2, 8]
  "§9.4.1#r14": [2, 3, 6]
  "EB-FLT-7": [15, 19, 20, 21]
anchor: [14]
coverage:
  web: automated
---

# Group yang memiliki record berjalan tidak dapat dihapus, dan Group yang dihapus sesudah record-nya selesai dibersihkan dari kriteria filter sub-tab Active saat re-apply

## Prerequisites
- Aktor: Total Control. Aktor kedua, Total Control lain, hanya memicu perubahan (Mark as Repaired dan hapus Group) dan layarnya tidak diasersi.
- Layar awal: halaman Groups.
- Data:
  - DU-055-1: Group Name `Gudang Cabang Bekasi {runId}`, berisi aset Name `Genset Honda EU22i {runId}`, tanpa TAG, dengan record `Damaged` Source `Manual` dan What happened `Mesin genset sulit menyala dan mengeluarkan asap hitam`.
  - DU-055-2: aset Name `Kompresor Atlas Copco GX5 {runId}`, Group `Head Office`, tanpa TAG, dengan record `Damaged` Source `Manual` dan What happened `Kompresor tidak mencapai tekanan kerja dan bocor di sambungan selang`.

## Test Steps

### Penghapusan Group yang memiliki record berjalan ditolak
1. Klik `Delete` pada Group `Gudang Cabang Bekasi {runId}`
2. Verifikasi penghapusan Group `Gudang Cabang Bekasi {runId}` ditolak
3. Verifikasi Group `Gudang Cabang Bekasi {runId}` tetap tampil di daftar Group

### Record berjalan tetap ada dan tanpa node baru
4. Buka halaman Assets, tab `Damaged`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi baris aset `Genset Honda EU22i {runId}` tetap tampil di sub-tab `Active` dengan Status `Damaged`
7. Klik nama aset pada baris aset `Genset Honda EU22i {runId}`
8. Verifikasi dialog Damage Log memuat tepat satu node `Reported damaged by [Reporter Name]`, tanpa node baru dari penghapusan Group
9. Tutup dialog Damage Log

### Group yang dihapus sesudah record-nya selesai dibersihkan dari kriteria filter saat re-apply
10. Ganti isi kotak search dengan `{runId}`, tekan Enter
11. Klik ikon `Filter`
12. Pilih Group `Gudang Cabang Bekasi {runId}` pada field `Group`
13. Klik `[Apply]`
14. Verifikasi baris aset `Genset Honda EU22i {runId}` tampil di sub-tab `Active`
15. Verifikasi baris aset `Kompresor Atlas Copco GX5 {runId}` tidak tampil
16. Aktor kedua melakukan Mark as Repaired atas record aset `Genset Honda EU22i {runId}` dengan Repair note `Mesin genset sudah diservis dan menyala normal`
17. Aktor kedua menghapus Group `Gudang Cabang Bekasi {runId}`
18. Klik `[Apply]`
19. Verifikasi tidak ada pesan error yang tampil
20. Verifikasi baris aset `Kompresor Atlas Copco GX5 {runId}` tampil di sub-tab `Active`, karena tabel mengikuti kriteria tersisa Search `{runId}`
21. Verifikasi field `Group` pada Filter Panel tidak lagi memuat `Gudang Cabang Bekasi {runId}`
