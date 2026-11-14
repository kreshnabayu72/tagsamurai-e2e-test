---
id: TC-FA-DAMAGED-E2E-048-report-dari-halaman-borrow-dep-borrow
title: "Aktor Borrow melapor rusak dari halaman transaksi Borrow: record langsung Damaged Source Borrowed asset, Last Holder terisi, baris Borrow tidak berubah, dan Damage Log terbuka dari penanda"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b1", "§2.1#b2", "§2#b6", "§4.8#r3", "§2.1#r2", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r37", "§Aturan Logika Modul#r26", "§9.4.2#r3", "§9.4.4#r3", "§3#p2", "§4.2.3#p1", "§4.2.3#p2", "§9.4.2#r19", "§9.11#r1", "T-DMG-01"]
smoke: []
dependsOn:
  - "Borrow: Detail BRW (tombol Report Damaged, penanda Damage reported)"
trace:
  "§2.1#b1": [4, 20]
  "§2.1#b2": [10, 11, 13, 14, 20, 27, 28]
  "§2#b6": [20, 24]
  "§4.8#r3": [4]
  "§2.1#r2": [10, 20]
  "§Aturan Logika Modul#r42": [20]
  "§Aturan Logika Modul#r37": [16, 17]
  "§Aturan Logika Modul#r26": [17, 22, 23]
  "§9.4.2#r3": [16, 17]
  "§9.4.4#r3": [14, 16, 17]
  "§3#p2": [10, 14, 20]
  "§4.2.3#p1": [4]
  "§4.2.3#p2": [4, 5, 6]
  "§9.4.2#r19": [13, 14]
  "§9.11#r1": [13, 14]
  "T-DMG-01": [20, 21, 22, 26, 27, 28]
anchor: []
coverage:
  web: automated
---

# Aktor Borrow melapor rusak dari halaman transaksi Borrow: record langsung Damaged Source Borrowed asset, Last Holder terisi, baris Borrow tidak berubah, dan Damage Log terbuka dari penanda

## Prerequisites
- Aktor: Aktor Borrow Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only.
- Layar awal: halaman Borrow.
- Data:
  - DU-048-1: aset Name `Projector Epson EB-X06 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage, sedang dipinjam `Sari Dewanti {runId}` lewat baris Borrow berstatus `Borrowed`.

## Test Steps

### Report Damaged dari Detail BRW membuat record langsung Damaged
1. Ketik Search `{runId}`, tekan Enter
2. Buka Detail BRW aset `Projector Epson EB-X06 {runId}`
3. Klik `Report Damaged` pada Detail BRW
4. Verifikasi dialog `Report Damaged` tampil
5. Verifikasi kotak dampak memuat `The asset will be marked Damaged.`
6. Verifikasi kotak dampak memuat `[Holder] keeps the asset until it's returned.` dengan `[Holder]` diisi `Sari Dewanti {runId}`
7. Isi What happened `Lensa proyektor berembun dan gambar buram`
8. Pilih Damaged Photo `proyektor-lensa-buram.jpg`
9. Klik `[Report Damaged]`
10. Verifikasi toast `Success, asset has been reported damaged.` tampil

### Damage Log terbuka dari penanda di halaman transaksi
11. Verifikasi penanda `Damage reported` tampil di Detail BRW
12. Klik penanda `Damage reported`
13. Verifikasi dialog `Damage Log` tampil
14. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Lensa proyektor berembun dan gambar buram`
15. Tutup dialog Damage Log

### Baris Borrow tidak berubah oleh laporan
16. Verifikasi baris Borrow aset `Projector Epson EB-X06 {runId}` tetap berstatus `Borrowed`
17. Verifikasi pemegang pada baris itu tetap `Sari Dewanti {runId}`

### Record langsung Damaged di tab Damaged dan tanpa aksi tulis bagi Aktor Borrow
18. Buka halaman Assets, tab `Damaged`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
21. Verifikasi kolom Source pada baris itu `Borrowed asset`
22. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang, dalam bentuk nama depan dan inisial nama belakang
23. Verifikasi kolom Group pada baris itu `Head Office`
24. Verifikasi kolom Reported By pada baris itu memuat nama Aktor Borrow yang melapor, dalam bentuk nama depan dan inisial nama belakang
25. Klik `⋯` pada baris aset `Projector Epson EB-X06 {runId}`
26. Verifikasi aksi `Damage Log` tampil pada menu baris
27. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
28. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
