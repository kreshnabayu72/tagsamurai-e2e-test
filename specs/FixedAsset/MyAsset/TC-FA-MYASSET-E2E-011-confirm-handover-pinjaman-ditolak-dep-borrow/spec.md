---
id: TC-FA-MYASSET-E2E-011-confirm-handover-pinjaman-ditolak-dep-borrow
title: "Confirm Handover pinjaman ditolak: Cancel Request oleh admin dan sudah dikonfirmasi lewat cara lain"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["V-03", "§1.2#r12", "§3#p5", "§4.2.5#p11", "§4.2.5#p12", "§4.2.5#r5", "§4.4#r40", "§4.4#r41", "§9.2#b3", "§9.2#r2", "§9.2#r3", "§9.4.2#r37", "§9.4.2#r38", "§9.4.2#r39", "§9.4.2#r41", "§9.4.2#r42"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "V-03": [8, 9, 24, 25]
  "§1.2#r12": 12
  "§3#p5": [12, 28]
  "§4.2.5#p11": [9, 25]
  "§4.2.5#p12": [11, 12, 27, 28]
  "§4.2.5#r5": [8, 24]
  "§4.4#r40": [8, 24]
  "§4.4#r41": [11, 27]
  "§9.2#b3": [12, 15]
  "§9.2#r2": 31
  "§9.2#r3": 25
  "§9.4.2#r37": [8, 24]
  "§9.4.2#r38": [9, 25]
  "§9.4.2#r39": [12, 28]
  "§9.4.2#r41": 28
  "§9.4.2#r42": 25
anchor: [3, 19]
coverage:
  web: automated
---

# Confirm Handover pinjaman ditolak: Cancel Request oleh admin dan sudah dikonfirmasi lewat cara lain

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login pemilik pinjaman. Aktor Borrow pada Group `Head Office` memicu Handover, Cancel Request, dan konfirmasi lewat perangkat admin.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-011-1: Pinjaman milik Borrower berstatus `Waiting for Handover` dengan satu aset: Name `Mesin Fotokopi Canon IR2625 {runId}`, Asset ID `CPY-1-{runId}`, Brand `Canon`, Model/Type `IR2625`, Group `Head Office`, Duration `3 days`.
  - DU-011-2: Pinjaman milik Borrower berstatus `Waiting for Handover` dengan satu aset: Name `Kamera Sony A7 III {runId}`, Asset ID `CAM-1-{runId}`, Brand `Sony`, Model/Type `A7 III`, Group `Head Office`, Duration `3 days`.

## Test Steps

### Cancel Request oleh admin saat dialog Confirm Handover terbuka
1. Aktor Borrow memulai Handover untuk pinjaman DU-011-1
2. Ketik Search Transaction ID pinjaman DU-011-1, tekan Enter
3. Verifikasi baris Task dengan Task `Confirm Handover` tampil
4. Klik `⋯` pada baris Task pinjaman DU-011-1
5. Klik `Confirm Handover`
6. Aktor Borrow menekan `Cancel Request` pada Handover pinjaman DU-011-1 saat dialog `Confirm Handover` masih terbuka
7. Klik `[Confirm]`
8. Verifikasi dialog `Handover No Longer Available` tampil
9. Verifikasi isi dialog `[Admin] canceled this handover request. Ask them to start again if you still need the assets.` dengan `[Admin]` berisi nama Aktor Borrow yang menekan `Cancel Request`
10. Klik `[OK]`
11. Verifikasi dialog `Handover No Longer Available` sudah tertutup
12. Verifikasi empty state `No results found` tampil karena baris Task pinjaman DU-011-1 sudah hilang
13. Klik tab `Borrowed`
14. Ketik Search `{runId}`, tekan Enter
15. Verifikasi baris `Mesin Fotokopi Canon IR2625 {runId}` berstatus `Waiting for Handover`

### Sudah dikonfirmasi lewat perangkat admin saat dialog Confirm Handover terbuka
16. Klik tab `Task`
17. Aktor Borrow memulai Handover untuk pinjaman DU-011-2
18. Ganti isi kotak search dengan Transaction ID pinjaman DU-011-2, tekan Enter
19. Verifikasi baris Task dengan Task `Confirm Handover` tampil
20. Klik `⋯` pada baris Task pinjaman DU-011-2
21. Klik `Confirm Handover`
22. Aktor Borrow mengonfirmasi Handover pinjaman DU-011-2 lewat `Confirm on This Device` di perangkat admin saat dialog `Confirm Handover` masih terbuka
23. Klik `[Confirm]`
24. Verifikasi dialog `Handover No Longer Available` tampil
25. Verifikasi isi dialog `This handover has already been confirmed.`
26. Klik `[OK]`
27. Verifikasi dialog `Handover No Longer Available` sudah tertutup
28. Verifikasi empty state `No results found` tampil karena baris Task pinjaman DU-011-2 sudah hilang
29. Klik tab `Borrowed`
30. Ganti isi kotak search dengan `{runId}`, tekan Enter
31. Verifikasi baris `Kamera Sony A7 III {runId}` berstatus `Borrowed`
