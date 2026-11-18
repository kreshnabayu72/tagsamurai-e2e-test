---
id: TC-FA-MYASSET-E2E-015-cancel-extension-request-dep-borrow
title: "Cancel Extension Request: pengajuan ditarik dan Due date tetap"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§3#p11", "§4.1b#r56", "§4.1b#r57", "§4.1b#r58", "§4.1b#r59", "§Dialog aksi baris (tab Borrowed dan Assigned)#p6", "§4.4#r5", "§7.3#r3", "§9.2#b8", "§9.4.2#r44", "§9.4.2#r45", "§9.6#r4", "§9.7#r5", "EB-FB-1@cancel-extension-request"]
smoke: ["EB-FB-1@cancel-extension-request"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§3#p11": [12, 13]
  "§4.1b#r56": 6
  "§4.1b#r57": [3, 14]
  "§4.1b#r58": 8
  "§4.1b#r59": 11
  "§Dialog aksi baris (tab Borrowed dan Assigned)#p6": [8, 9]
  "§4.4#r5": [8, 11]
  "§7.3#r3": 11
  "§9.2#b8": [12, 18]
  "§9.4.2#r44": 26
  "§9.4.2#r45": 30
  "§9.6#r4": [11, 12]
  "§9.7#r5": [26, 27]
  "EB-FB-1@cancel-extension-request": 11
anchor: [19, 29]
coverage:
  web: automated
---

# Cancel Extension Request: pengajuan ditarik dan Due date tetap

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman. Aktor Borrow pada Group `Head Office` meninjau pengajuan Extension sebagai pemicu.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-015-1: Pinjaman milik Borrower berstatus `Borrowed` dengan pengajuan Extend yang menunggu review Aktor Borrow, sehingga Status tampil `Extension Request`; satu aset: Name `Proyektor BenQ MW535 {runId}`, Asset ID `PRJ-B535-{runId}`, Brand `BenQ`, Model/Type `MW535`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-015-2: Pinjaman milik Borrower berstatus `Borrowed` dengan pengajuan Extend yang menunggu review Aktor Borrow, sehingga Status tampil `Extension Request`; satu aset: Name `Speaker JBL PartyBox 310 {runId}`, Asset ID `SPK-310-{runId}`, Brand `JBL`, Model/Type `PartyBox 310`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-015-3: Pinjaman milik Borrower berstatus `Borrowed` dengan pengajuan Extension yang menunggu approval, sehingga Status tampil `Extension Approval`; satu aset: Name `Kamera Canon EOS R6 {runId}`, Asset ID `CAM-R6-{runId}`, Brand `Canon`, Model/Type `EOS R6`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.

## Test Steps

### Cancel Extension Request yang menunggu review: pengajuan ditarik dan Due date tetap
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Proyektor BenQ MW535 {runId}` berstatus `Extension Request`
4. Catat Due Date baris `Proyektor BenQ MW535 {runId}`
5. Klik `⋯` pada baris `Proyektor BenQ MW535 {runId}`
6. Verifikasi opsi `Cancel Extension Request` tersedia pada menu baris
7. Klik `Cancel Extension Request`
8. Verifikasi dialog `Cancel Extension` tampil dengan aset `Proyektor BenQ MW535 {runId}`
9. Verifikasi dialog memuat `The approval request will be withdrawn and the current due date stays [Date]. Are you sure you want to cancel it?` dengan `[Date]` berisi Due Date yang dicatat
10. Klik `[Cancel Extension]`
11. Verifikasi toast `Success, extension request has been canceled.` tampil
12. Verifikasi baris `Proyektor BenQ MW535 {runId}` berstatus `Borrowed`
13. Verifikasi Due Date baris `Proyektor BenQ MW535 {runId}` sama dengan Due Date yang dicatat

### Cancel Extension Request yang menunggu approval
14. Verifikasi baris `Kamera Canon EOS R6 {runId}` berstatus `Extension Approval`
15. Klik `⋯` pada baris `Kamera Canon EOS R6 {runId}`
16. Klik `Cancel Extension Request`
17. Klik `[Cancel Extension]`
18. Verifikasi baris `Kamera Canon EOS R6 {runId}` berstatus `Borrowed`

### Pengajuan sudah ditinjau Aktor Borrow saat dialog Cancel Extension terbuka
19. Verifikasi baris `Speaker JBL PartyBox 310 {runId}` berstatus `Extension Request`
20. Catat Due Date baris `Speaker JBL PartyBox 310 {runId}`
21. Klik `⋯` pada baris `Speaker JBL PartyBox 310 {runId}`
22. Klik `Cancel Extension Request`
23. Aktor Borrow meninjau pengajuan Extension pinjaman DU-015-2 dan menerapkannya saat dialog `Cancel Extension` masih terbuka
24. Klik `[Cancel Extension]`
25. Muat ulang halaman
26. Verifikasi baris `Speaker JBL PartyBox 310 {runId}` berstatus `Borrowed`
27. Verifikasi Due Date baris `Speaker JBL PartyBox 310 {runId}` berbeda dari Due Date yang dicatat
28. Klik `⋯` pada baris `Speaker JBL PartyBox 310 {runId}`
29. Verifikasi opsi `Borrow Log` tersedia pada menu baris
30. Verifikasi opsi `Cancel Extension Request` tidak tersedia pada menu baris
