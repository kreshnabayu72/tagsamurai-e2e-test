---
id: TC-FA-DAMAGED-E2E-049-return-accept-with-damage-dep-borrow
title: "Return Accept with damage membuat record Source Borrow return dari catatan dan foto Return; saat record Waiting for Confirmation sudah ada, Aktor Borrow memutuskan lewat Assess Damage tanpa record baru"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r46", "§Aturan Logika Modul#r51", "§Aturan Logika Modul#r52", "§Aturan Logika Modul#r55", "§Aturan Logika Modul#r34", "§Aturan Logika Modul#r41", "§9.2#b7", "§8.3#r2", "§8.1#r7", "§8.1#r8", "§9.4.2#r6", "§9.4.4#r4", "§9.7#r3", "§2.1#b3", "T-DMG-01"]
smoke: []
dependsOn:
  - "Borrow: Return (Accept with damage, Assess Damage)"
trace:
  "§Aturan Logika Modul#r46": [21, 22]
  "§Aturan Logika Modul#r51": [39, 56]
  "§Aturan Logika Modul#r52": [36, 54]
  "§Aturan Logika Modul#r55": [39, 56]
  "§Aturan Logika Modul#r34": [32, 36]
  "§Aturan Logika Modul#r41": [13, 32]
  "§9.2#b7": [21, 22]
  "§8.3#r2": [20]
  "§8.1#r7": [20, 21, 22]
  "§8.1#r8": [39, 56]
  "§9.4.2#r6": [35, 39, 40, 41]
  "§9.4.4#r4": [40]
  "§9.7#r3": [16, 18]
  "§2.1#b3": [5, 39, 56]
  "T-DMG-01": [2, 5, 16, 17, 18, 36, 37]
anchor: [4]
coverage:
  web: automated
---

# Return Accept with damage membuat record Source Borrow return dari catatan dan foto Return; saat record Waiting for Confirmation sudah ada, Aktor Borrow memutuskan lewat Assess Damage tanpa record baru

## Prerequisites
- Aktor: Aktor Borrow Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-049-1: aset Name `Printer Brother HL-L2375 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Hana Pratiwi {runId}` lewat baris Borrow berstatus `Borrowed`, belum punya record Damage.
  - DU-049-2: aset Name `Scanner Fujitsu fi-7160 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Rudi Hartono {runId}` lewat baris Borrow berstatus `Borrowed`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Roller pemindai macet dan kertas sering tersangkut`.
  - DU-049-3: aset Name `Barcode Scanner Zebra DS2208 {runId}`, Group `Head Office`, tanpa TAG, sedang dipinjam `Agus Santoso {runId}` lewat baris Borrow berstatus `Borrowed`, dengan record `Waiting for Confirmation` Source `Reported by holder` dari laporan pemegang dengan What happened `Tombol trigger barcode scanner tidak responsif`.

## Test Steps

### Laporan pemegang yang menunggu keputusan tidak bisa di-Review dari tabel oleh Aktor Borrow
1. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
2. Verifikasi baris aset `Scanner Fujitsu fi-7160 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
3. Klik `⋯` pada baris aset `Scanner Fujitsu fi-7160 {runId}`
4. Verifikasi aksi `Damage Log` tampil pada menu baris
5. Verifikasi aksi `Review` tidak tampil pada menu baris

### Return Accept with damage atas aset tanpa record membuat record Damaged Source Borrow return
6. Buka halaman Borrow
7. Ketik Search `Printer Brother HL-L2375 {runId}`, tekan Enter
8. Klik `Return` pada baris Borrow aset `Printer Brother HL-L2375 {runId}`
9. Pilih `Accept with damage`
10. Isi Description `Casing printer retak setelah terjatuh saat dikembalikan`
11. Pilih foto Return `printer-casing-retak.jpg`
12. Submit form Return
13. Verifikasi baris Borrow aset `Printer Brother HL-L2375 {runId}` tidak lagi berstatus `Borrowed`
14. Buka halaman Assets, tab `Damaged`
15. Ketik Search `Printer Brother HL-L2375 {runId}`, tekan Enter
16. Verifikasi baris aset `Printer Brother HL-L2375 {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
17. Verifikasi kolom Source pada baris itu `Borrow return`
18. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang saat Return, dalam bentuk nama depan dan inisial nama belakang
19. Klik nama aset pada baris aset `Printer Brother HL-L2375 {runId}`
20. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama Aktor Borrow yang melakukan Return
21. Verifikasi baris detail What happened pada node itu `Casing printer retak setelah terjatuh saat dikembalikan`
22. Verifikasi baris detail Damaged Photo pada node itu memuat foto Return `printer-casing-retak.jpg`
23. Tutup dialog Damage Log

### Return atas aset dengan laporan pemegang: Aktor Borrow Confirm lewat Assess Damage tanpa record baru
24. Buka halaman Borrow
25. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
26. Klik `Return` pada baris Borrow aset `Scanner Fujitsu fi-7160 {runId}`
27. Pilih `Accept with damage`
28. Isi Description `Roller pemindai macet seperti yang dilaporkan pemegang`
29. Pilih foto Return `scanner-roller-macet.jpg`
30. Pilih `Confirm` pada Assess Damage atas laporan pemegang
31. Submit form Return
32. Verifikasi baris Borrow aset `Scanner Fujitsu fi-7160 {runId}` tidak lagi berstatus `Borrowed`
33. Buka halaman Assets, tab `Damaged`
34. Ketik Search `Scanner Fujitsu fi-7160 {runId}`, tekan Enter
35. Verifikasi tepat satu baris aset `Scanner Fujitsu fi-7160 {runId}` tampil di sub-tab `Active`
36. Verifikasi Status baris itu `Damaged`
37. Verifikasi kolom Source pada baris itu `Reported by holder`
38. Klik nama aset pada baris aset `Scanner Fujitsu fi-7160 {runId}`
39. Verifikasi node `Report confirmed by [Admin Name]` tampil atas nama Aktor Borrow yang memutuskan
40. Verifikasi dialog Damage Log memuat tepat satu node `Reported damaged by [Reporter Name]`
41. Verifikasi baris detail What happened pada node itu tetap `Roller pemindai macet dan kertas sering tersangkut`
42. Tutup dialog Damage Log

### Return atas aset dengan laporan pemegang: Aktor Borrow Reject lewat Assess Damage
43. Buka halaman Borrow
44. Ketik Search `Barcode Scanner Zebra DS2208 {runId}`, tekan Enter
45. Klik `Return` pada baris Borrow aset `Barcode Scanner Zebra DS2208 {runId}`
46. Pilih `Accept with damage`
47. Isi Description `Layar barcode scanner menampilkan garis horizontal`
48. Pilih foto Return `barcode-scanner-layar.jpg`
49. Pilih `Reject` pada Assess Damage atas laporan pemegang
50. Submit form Return
51. Buka halaman Assets, tab `Damaged`
52. Klik sub-tab `History`
53. Ketik Search `Barcode Scanner Zebra DS2208 {runId}`, tekan Enter
54. Verifikasi baris aset `Barcode Scanner Zebra DS2208 {runId}` tampil di sub-tab `History` dengan Status `Rejected`
55. Klik nama aset pada baris aset `Barcode Scanner Zebra DS2208 {runId}`
56. Verifikasi node `Report rejected by [Admin Name]` tampil atas nama Aktor Borrow yang memutuskan
57. Tutup dialog Damage Log
