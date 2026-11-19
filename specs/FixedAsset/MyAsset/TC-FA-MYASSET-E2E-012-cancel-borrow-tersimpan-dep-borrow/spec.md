---
id: TC-FA-MYASSET-E2E-012-cancel-borrow-tersimpan-dep-borrow
title: "Cancel Borrow pada baris Waiting for Approval: baris Canceled pindah ke tab History"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r31", "§1.2#r33", "§2.1#r4", "§3#p13", "§4.1#p4", "§4.1b#r75", "§4.1b#r77", "§4.1b#r78", "§4.1b#r80", "§Dialog aksi baris (tab Borrowed dan Assigned)#p3", "§4.4#r6", "§4.8#r6", "§7.3#r2", "§9.2#r4", "§9.2#r5", "§9.2#r6", "§9.2#r8", "§9.4.2#r69", "§9.4.2#r70", "§9.4.2#r72", "§9.6#r2", "§9.7#r3", "EB-FB-1@cancel-borrow"]
smoke: ["EB-FB-1@cancel-borrow"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r31": [3, 5]
  "§1.2#r33": [13, 14]
  "§2.1#r4": 18
  "§3#p13": [12, 17]
  "§4.1#p4": [14, 17]
  "§4.1b#r75": 5
  "§4.1b#r77": [7, 10]
  "§4.1b#r78": [17, 18]
  "§4.1b#r80": 12
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p3": [7, 8, 9]
  "§4.4#r6": [7, 12, 17]
  "§4.8#r6": 5
  "§7.3#r2": 12
  "§9.2#r4": 5
  "§9.2#r5": 13
  "§9.2#r6": 18
  "§9.2#r8": [14, 17]
  "§9.4.2#r69": 7
  "§9.4.2#r70": [17, 18]
  "§9.4.2#r72": 12
  "§9.6#r2": [12, 17]
  "§9.7#r3": [14, 17, 21, 24, 25, 29, 32, 33, 38]
  "EB-FB-1@cancel-borrow": 12
anchor: [28]
coverage:
  web: automated
---

# Cancel Borrow pada baris Waiting for Approval: baris Canceled pindah ke tab History

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman. Aktor Borrow menyetujui, menolak, dan mengajukan pinjaman.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-012-1: Pinjaman milik Borrower berstatus `Waiting for Approval`, aset pertama dari BRW dua aset: Name `Printer HP LaserJet M404 - 1 {runId}`, Asset ID `PRN-1-{runId}`, Brand `HP`, Model/Type `LaserJet M404`, Group `Head Office`, Duration `3 days`.
  - DU-012-2: Aset kedua dari BRW yang sama dengan DU-012-1, berstatus `Waiting for Approval`: Name `Printer HP LaserJet M404 - 2 {runId}`, Asset ID `PRN-2-{runId}`, Brand `HP`, Model/Type `LaserJet M404`, Group `Head Office`, Duration `3 days`.
  - DU-012-3: Pinjaman milik Borrower berstatus `Waiting for Approval`, yang disetujui Aktor Borrow: Name `Kamera Canon EOS R6 {runId}`, Asset ID `CAM-1-{runId}`, Brand `Canon`, Model/Type `EOS R6`, Group `Head Office`, Duration `3 days`.
  - DU-012-4: Pinjaman milik Borrower berstatus `Waiting for Approval`, yang ditolak Aktor Borrow: Name `Tripod Manfrotto 055 {runId}`, Asset ID `TRP-1-{runId}`, Brand `Manfrotto`, Model/Type `055`, Group `Head Office`, Duration `3 days`.

## Test Steps

### Cancel Borrow satu baris Waiting for Approval: dialog, toast, dan baris pindah ke tab History
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Printer HP LaserJet M404 - 1 {runId}` dan `Printer HP LaserJet M404 - 2 {runId}` berstatus `Waiting for Approval`
4. Klik `⋯` pada baris `Printer HP LaserJet M404 - 1 {runId}`
5. Verifikasi opsi `Cancel Borrow` tersedia pada menu baris
6. Klik `Cancel Borrow`
7. Verifikasi dialog `Cancel Borrow` tampil dengan aset `Printer HP LaserJet M404 - 1 {runId}`
8. Verifikasi dialog memuat `The asset becomes available again and the Asset Admin is notified.`
9. Verifikasi dialog memuat `Are you sure you want to cancel it?`
10. Verifikasi dialog tidak memuat opsi `Save as Draft to edit`
11. Klik `[Cancel Borrow]`
12. Verifikasi toast `Success, borrow has been canceled.` tampil
13. Verifikasi baris `Printer HP LaserJet M404 - 2 {runId}` tetap berstatus `Waiting for Approval`
14. Verifikasi baris `Printer HP LaserJet M404 - 1 {runId}` berpindah dari tab Borrowed[^drift-1]
15. Klik tab `History`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Printer HP LaserJet M404 - 1 {runId}` berpindah ke tab History[^drift-1]
18. Verifikasi baris `Printer HP LaserJet M404 - 1 {runId}` berstatus `Canceled` dengan Type `Borrow`

### Approval keputusan mengubah status baris di tab Borrowed
19. Klik tab `Borrowed`
20. Ganti isi kotak search dengan `{runId}`, tekan Enter
21. Verifikasi baris `Kamera Canon EOS R6 {runId}` berstatus `Waiting for Approval`
22. Aktor Borrow menyetujui pinjaman `Kamera Canon EOS R6 {runId}`
23. Muat ulang halaman
24. Verifikasi baris `Kamera Canon EOS R6 {runId}` berstatus `Waiting for Handover`

### Reject membuat baris pindah ke tab History dengan status Rejected
25. Verifikasi baris `Tripod Manfrotto 055 {runId}` berstatus `Waiting for Approval`
26. Aktor Borrow menolak pinjaman `Tripod Manfrotto 055 {runId}`
27. Muat ulang halaman
28. Verifikasi baris `Kamera Canon EOS R6 {runId}` berstatus `Waiting for Handover`
29. Verifikasi baris `Tripod Manfrotto 055 {runId}` tidak tampil pada tab Borrowed[^drift-1]
30. Klik tab `History`
31. Ganti isi kotak search dengan `{runId}`, tekan Enter
32. Verifikasi baris `Tripod Manfrotto 055 {runId}` berpindah ke tab History[^drift-1]
33. Verifikasi baris `Tripod Manfrotto 055 {runId}` berstatus `Rejected` dengan Type `Borrow`

### Submit pinjaman baru muncul di tab Borrowed
34. Klik tab `Borrowed`
35. Ganti isi kotak search dengan `{runId}`, tekan Enter
36. Aktor Borrow mengajukan pinjaman untuk Borrower dengan aset `Monitor LG UltraWide 34 {runId}`, Asset ID `MON-1-{runId}`, dan Duration `3 days`
37. Muat ulang halaman
38. Verifikasi baris `Monitor LG UltraWide 34 {runId}` tampil pada tab Borrowed

[^drift-1]: Drift PRD vs foundation. PRD §4.1 «Deviasi»: baris berpindah dari tab Borrowed atau Assigned ke tab History saat status akhir tercapai (`MYASSET-LOGIC-01`). foundation `prd-conventions.md` §14.1: baris tetap di posisinya saat status berubah dan tidak berpindah ke tab atau halaman lain. Diasersi: PRD, karena perpindahan antar-tab adalah perilaku khusus modul yang PRD nyatakan sebagai deviasi (SB-4).
