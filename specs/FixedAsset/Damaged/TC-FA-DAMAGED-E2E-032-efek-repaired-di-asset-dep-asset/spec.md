---
id: TC-FA-DAMAGED-E2E-032-efek-repaired-di-asset-dep-asset
title: "Setelah Mark as Repaired, Asset Detail menampilkan status global Normal tanpa banner Damaged dan Transaction log memuat Repaired"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§Aturan Logika Modul#r33, §Aturan Logika Modul#r61, §Aturan Logika Modul#r43, §9.7#r9, §8.2#b1, §4.1#r10, §8.2#p8, §8.2#p9]
smoke: []
dependsOn:
  - "Asset: Asset Detail (status global aset, banner Damaged, Transaction log)"
trace:
  §Aturan Logika Modul#r33: [13, 14]
  §Aturan Logika Modul#r61: 13
  §Aturan Logika Modul#r43: 14
  §9.7#r9: [13, 21]
  §8.2#b1: 16
  §4.1#r10: 14
  §8.2#p8: [16, 17]
  §8.2#p9: [26, 27]
anchor: [3, 4]
coverage:
  web: automated
---

# Setelah Mark as Repaired, Asset Detail menampilkan status global Normal tanpa banner Damaged dan Transaction log memuat Repaired

## Prerequisites
- Aktor: Total Control.
- Layar awal: halaman Assets, tab Assets (Asset List).
- Data:
  - DU-032-1: aset `Genset Honda EU22i {runId}`, Group `Head Office`, tanpa TAG, tidak sedang dipinjam maupun di-assign ke siapa pun, status global `Damaged`, sudah punya record Damage berjalan berstatus `Damaged` yang dilaporkan Pelapor admin.
  - DU-032-2: Repair note `Mesin diservis dan busi diganti` untuk Mark as Repaired atas `Genset Honda EU22i {runId}`.
  - DU-032-5: aset `Mesin Pemotong Kertas Krisbow {runId}`, Group `Head Office`, status `Disposed`, sudah punya record Damage berstatus `Disposed` yang dilaporkan pemegang, di-Confirm, lalu melewati Report Disposal.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Efek Mark as Repaired di Asset Detail dan Transaction log
1. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
2. Klik nama aset `Genset Honda EU22i {runId}` untuk membuka Asset Detail
3. Verifikasi status global aset `Damaged` sebelum perbaikan pada Asset Detail aset ini
4. Verifikasi banner `Damaged since [Date].` tampil pada Asset Detail
5. Buka tab `Damaged` pada halaman Assets
6. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
7. Klik aksi `Mark as Repaired` pada baris `Genset Honda EU22i {runId}`
8. Isi `Repair note` dengan `Mesin diservis dan busi diganti`
9. Klik `[Mark as Repaired]` pada footer dialog
10. Buka tab `Assets` pada halaman Assets
11. Ganti isi kotak search dengan `Genset Honda EU22i {runId}`, tekan Enter
12. Klik nama aset `Genset Honda EU22i {runId}` untuk membuka Asset Detail
13. Verifikasi status global aset `Normal` (bukan `Borrowed` atau `Assigned`, karena aset tidak dipegang) tampil pada Asset Detail
14. Verifikasi banner `Damaged since [Date].` tidak tampil pada Asset Detail
15. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
16. Verifikasi entri `Marked as repaired by [Admin Name]` tampil
17. Verifikasi kolom `Status` entri itu `Repaired`

### Record Repaired pindah ke History
18. Buka tab `Damaged` pada halaman Assets
19. Buka sub-tab `History`
20. Ketik Search `Genset Honda EU22i {runId}`, tekan Enter
21. Verifikasi baris `Genset Honda EU22i {runId}` tampil dengan Status `Repaired`

### Peristiwa Disposed di Transaction log
22. Buka tab `Assets` pada halaman Assets
23. Ganti isi kotak search dengan `Mesin Pemotong Kertas Krisbow {runId}`, tekan Enter
24. Klik nama aset `Mesin Pemotong Kertas Krisbow {runId}` untuk membuka Asset Detail
25. Buka Transaction log pada Asset Detail, sub-tab `Damaged`
26. Verifikasi entri `Disposed` tampil
27. Verifikasi kolom `Status` entri `Disposed` itu `Disposed`
