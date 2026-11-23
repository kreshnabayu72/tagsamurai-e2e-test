---
id: TC-FA-MYASSET-E2E-013-cancel-borrow-ditolak-dep-borrow
title: "Cancel Borrow ditolak: sudah dibatalkan Aktor Borrow dan sesi Handover sedang berjalan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-12", "V-02", "§1.2#r35", "§3#p13", "§4.1b#r76", "§4.1b#r81", "§4.2.5#p14", "§4.2.5#p15", "§4.2.5#r7", "§4.4#r6", "§4.4#r42", "§4.4#r43", "§4.4#r44", "§7.3#r14", "§9.4.2#r75", "§9.4.2#r76", "§9.4.2#r77", "§9.4.2#r79", "§9.4.2#r80", "§9.4.2#r81", "§9.4.2#r82", "EB-ERR-4"]
smoke: ["EB-ERR-4"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-12": 24
  "V-02": [8, 24]
  "§1.2#r35": 8
  "§3#p13": [8, 24]
  "§4.1b#r76": 24
  "§4.1b#r81": 8
  "§4.2.5#p14": [9, 10]
  "§4.2.5#p15": [12, 14, 17]
  "§4.2.5#r7": 8
  "§4.4#r6": 8
  "§4.4#r42": 8
  "§4.4#r43": [12, 14]
  "§4.4#r44": 17
  "§7.3#r14": 24
  "§9.4.2#r75": 8
  "§9.4.2#r76": 8
  "§9.4.2#r77": [14, 17]
  "§9.4.2#r79": 24
  "§9.4.2#r80": [29, 33]
  "§9.4.2#r81": [40, 43]
  "§9.4.2#r82": 46
  "EB-ERR-4": 25
anchor: [3, 13, 36, 45]
coverage:
  web: automated
---

# Cancel Borrow ditolak: sudah dibatalkan Aktor Borrow dan sesi Handover sedang berjalan

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman. Aktor Borrow pada Group `Head Office` memicu pembatalan, Handover, dan Cancel Request.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-013-1: Pinjaman milik Borrower berstatus `Waiting for Approval`, satu aset: Name `Scanner Epson DS-530 {runId}`, Asset ID `SCN-1-{runId}`, Brand `Epson`, Model/Type `DS-530`, Group `Head Office`, Duration `3 days`.
  - DU-013-2: Pinjaman milik Borrower berstatus `Waiting for Approval`, satu aset: Name `Tablet Samsung Galaxy Tab S8 {runId}`, Asset ID `TAB-1-{runId}`, Brand `Samsung`, Model/Type `Galaxy Tab S8`, Group `Head Office`, Duration `3 days`.
  - DU-013-3: Pinjaman milik Borrower berstatus `Waiting for Handover`, satu aset: Name `Tripod Manfrotto 055 {runId}`, Asset ID `TRP-1-{runId}`, Brand `Manfrotto`, Model/Type `055`, Group `Head Office`, Duration `3 days`.

## Test Steps

### Baris sudah dibatalkan Aktor Borrow saat dialog Cancel Borrow terbuka
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Scanner Epson DS-530 {runId}` berstatus `Waiting for Approval`
4. Klik `⋯` pada baris `Scanner Epson DS-530 {runId}`
5. Klik `Cancel Borrow`
6. Aktor Borrow membatalkan pinjaman DU-013-1 saat dialog `Cancel Borrow` masih terbuka
7. Klik `[Cancel Borrow]`
8. Verifikasi dialog `Borrow Already Canceled` tampil
9. Verifikasi isi dialog `[Admin] already canceled this borrow.` dengan `[Admin]` berisi nama Aktor Borrow yang membatalkan
10. Verifikasi dialog memuat `Your action was not saved.`
11. Klik `[OK]`
12. Verifikasi dialog `Borrow Already Canceled` sudah tertutup
13. Verifikasi baris `Tablet Samsung Galaxy Tab S8 {runId}` tetap tampil di tab Borrowed dengan status `Waiting for Approval`
14. Verifikasi baris `Scanner Epson DS-530 {runId}` tidak tampil di tab Borrowed
15. Klik tab `History`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris `Scanner Epson DS-530 {runId}` tampil di tab History dengan Status `Canceled`

### Cancel Borrow ditolak saat sesi Handover baris itu berjalan
18. Klik tab `Borrowed`
19. Ganti isi kotak search dengan `{runId}`, tekan Enter
20. Aktor Borrow memulai Handover untuk pinjaman DU-013-3
21. Klik `⋯` pada baris `Tripod Manfrotto 055 {runId}`
22. Klik `Cancel Borrow`
23. Klik `[Cancel Borrow]`
24. Verifikasi toast `Error, handover is in progress for this asset.` tampil
25. Verifikasi baris `Tripod Manfrotto 055 {runId}` tetap berstatus `Waiting for Handover`
26. Aktor Borrow menekan `Cancel Request` pada Handover pinjaman DU-013-3
27. Klik `⋯` pada baris `Tripod Manfrotto 055 {runId}`
28. Klik `Cancel Borrow`
29. Verifikasi dialog `Cancel Borrow` tampil dengan aset `Tripod Manfrotto 055 {runId}`
30. Klik `[Cancel Borrow]`
31. Klik tab `History`
32. Ganti isi kotak search dengan `{runId}`, tekan Enter
33. Verifikasi baris `Tripod Manfrotto 055 {runId}` tampil di tab History dengan Status `Canceled`

### Aktor Borrow membatalkan baris saat tab Borrowed terbuka
34. Klik tab `Borrowed`
35. Ganti isi kotak search dengan `{runId}`, tekan Enter
36. Verifikasi baris `Tablet Samsung Galaxy Tab S8 {runId}` berstatus `Waiting for Approval`
37. Aktor Borrow membatalkan pinjaman DU-013-2 saat tab Borrowed terbuka
38. Muat ulang halaman
39. Ganti isi kotak search dengan `{runId}`, tekan Enter
40. Verifikasi baris `Tablet Samsung Galaxy Tab S8 {runId}` tidak tampil di tab Borrowed
41. Klik tab `History`
42. Ganti isi kotak search dengan `{runId}`, tekan Enter
43. Verifikasi baris `Tablet Samsung Galaxy Tab S8 {runId}` tampil di tab History dengan Status `Canceled`
44. Klik `⋯` pada baris `Tablet Samsung Galaxy Tab S8 {runId}`
45. Verifikasi opsi `Borrow Log` tersedia pada menu baris
46. Verifikasi opsi `Cancel Borrow` tidak tersedia pada menu baris
