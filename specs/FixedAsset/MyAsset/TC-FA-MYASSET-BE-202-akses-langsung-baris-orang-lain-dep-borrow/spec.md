---
id: TC-FA-MYASSET-BE-202-akses-langsung-baris-orang-lain-dep-borrow
title: "Server menolak akses dan aksi atas baris milik orang lain"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r23", "§1.2#r28", "§9.3#b1", "§9.3#b2", "§9.4.2#r19", "§9.4.3#b4", "EB-AKS-3@confirm-handover", "EB-AKS-3@confirm-handover-assignment", "EB-AKS-3@cancel-borrow", "EB-AKS-3@cancel-extension-request", "EB-AKS-3@report-damaged", "EB-AKS-3@report-missing", "EB-AKS-3@cancel-damage-report", "EB-AKS-3@cancel-missing-report"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
trace:
  "§1.2#r23": [4, 5, 7, 13, 14, 18, 19]
  "§1.2#r28": [2, 11, 16, 21, 25, 29, 35, 39, 43, 47, 51]
  "§9.3#b1": [9, 31]
  "§9.3#b2": [4, 13, 18]
  "§9.4.2#r19": [18, 19]
  "§9.4.3#b4": [29, 33]
  "EB-AKS-3@confirm-handover": [21, 23]
  "EB-AKS-3@confirm-handover-assignment": [25, 27]
  "EB-AKS-3@cancel-borrow": [29, 33]
  "EB-AKS-3@cancel-extension-request": [35, 37]
  "EB-AKS-3@report-damaged": [39, 41]
  "EB-AKS-3@report-missing": [43, 45]
  "EB-AKS-3@cancel-damage-report": [47, 49]
  "EB-AKS-3@cancel-missing-report": [51, 53]
owner: BE
---

# Server menolak akses dan aksi atas baris milik orang lain

## Prerequisites
- Aktor: Dedi, user tanpa capability apa pun di My Asset dan bukan Borrower maupun Assignee baris yang dituju; Rahmat, user ber-capability penuh yang juga bukan pemilik baris; Maya (Borrower), Tono (Assignee Employee), dan Rudi (Borrower di entitas lain) sebagai pemilik baris. Aktor Borrow dan Aktor Assignment hanya menyiapkan transaksinya.
- Data:
  - DU-202-1: User `Dedi Kurniawan {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-202-2: User `Rahmat Hidayat {runId}`, role Total Control, cakupan seluruh Group entitas aktor.
  - DU-202-3: User `Maya Anggraini {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Borrower pada DU-202-5 sampai DU-202-11.
  - DU-202-4: User `Tono Wibowo {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Assignee pada DU-202-12.
  - DU-202-5: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Projector Epson EB-X06 - 11 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-202-6: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 12 {runId}`, Group `Head Office`, status `Waiting for Approval`.
  - DU-202-7: Pinjaman Maya dengan pengajuan Extend yang menunggu review, aset `Laptop Dell Latitude 5420 - 13 {runId}`, Group `Head Office`, status `Extension Request`.
  - DU-202-8: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 14 {runId}`, Group `Head Office`, status `Borrowed`, tanpa Damage Report dan tanpa laporan Missing.
  - DU-202-9: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 15 {runId}`, Group `Head Office`, status `Borrowed`, tanpa Damage Report dan tanpa laporan Missing.
  - DU-202-10: Pinjaman Maya dengan Damage Report `Waiting for Confirmation` yang dilaporkan Maya, aset `Laptop Dell Latitude 5420 - 16 {runId}`, Group `Head Office`, status `Borrowed`, badge `Reported Damaged`.
  - DU-202-11: Pinjaman Maya dengan laporan Missing `Waiting for Confirmation` yang dilaporkan Maya, aset `Laptop Dell Latitude 5420 - 17 {runId}`, Group `Head Office`, status `Borrowed`, badge `Reported Missing`.
  - DU-202-12: Penugasan Tono dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Monitor Dell P2422H - 18 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-202-13: Pinjaman Rudi, Borrower di entitas lain (role Asset Admin, cakupan seluruh Group entitas itu), user `Rudi Hermawan {runId}`, aset `Camera Sony A7 III - 19 {runId}`, status `Borrowed`.
  - DU-202-14: Transaction ID yang tidak ada di entitas mana pun, `BRW-2099-9999`.

## Test Steps

### Akses langsung ke pinjaman orang lain ditolak tanpa membuka data atau keberadaannya
1. Maya meminta data tab Borrowed dengan highlight Transaction ID milik DU-202-6
2. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 12 {runId}`
3. Dedi meminta data tab Borrowed dengan highlight Transaction ID milik DU-202-6
4. Verifikasi permintaan ditolak server
5. Verifikasi penolakan tidak membuka data baris pinjaman aset `Laptop Dell Latitude 5420 - 12 {runId}` maupun keberadaannya
6. Dedi meminta data tab Borrowed dengan highlight Transaction ID `BRW-2099-9999`
7. Verifikasi penolakan untuk Transaction ID `BRW-2099-9999` sama dengan penolakan untuk Transaction ID milik DU-202-6
8. Rahmat meminta data tab Borrowed dengan highlight Transaction ID milik DU-202-6
9. Verifikasi permintaan ditolak server walaupun Rahmat berperan Total Control
10. Rudi meminta data tab Borrowed dengan highlight Transaction ID milik DU-202-13
11. Verifikasi data memuat baris pinjaman aset `Camera Sony A7 III - 19 {runId}`
12. Dedi meminta data tab Borrowed dengan highlight Transaction ID milik DU-202-13
13. Verifikasi permintaan ditolak server
14. Verifikasi penolakan tidak membuka data baris pinjaman aset `Camera Sony A7 III - 19 {runId}` maupun keberadaannya

### Akses langsung ke penugasan orang lain ditolak tanpa membuka data atau keberadaannya
15. Tono meminta data tab Assigned dengan highlight Transaction ID milik DU-202-12
16. Verifikasi data memuat baris penugasan aset `Monitor Dell P2422H - 18 {runId}`
17. Dedi meminta data tab Assigned dengan highlight Transaction ID milik DU-202-12
18. Verifikasi permintaan ditolak server
19. Verifikasi penolakan tidak membuka data baris penugasan aset `Monitor Dell P2422H - 18 {runId}` maupun keberadaannya

### Confirm Handover pinjaman milik orang lain ditolak
20. Dedi mengirim Confirm Handover dengan aset `Projector Epson EB-X06 - 11 {runId}` tercentang untuk sesi Handover milik Maya
21. Verifikasi aksi ditolak server
22. Maya meminta data tab Borrowed
23. Verifikasi baris pinjaman aset `Projector Epson EB-X06 - 11 {runId}` tetap berstatus `Waiting for Handover`

### Confirm Handover penugasan milik orang lain ditolak
24. Dedi mengirim Confirm dengan aset `Monitor Dell P2422H - 18 {runId}` dan pernyataan tercentang untuk sesi Handover penugasan milik Tono
25. Verifikasi aksi ditolak server
26. Tono meminta data tab Assigned
27. Verifikasi baris penugasan aset `Monitor Dell P2422H - 18 {runId}` tetap berstatus `Waiting for Handover`

### Cancel Borrow atas baris orang lain ditolak
28. Dedi mengirim Cancel Borrow untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 12 {runId}` milik Maya
29. Verifikasi aksi ditolak server
30. Rahmat mengirim Cancel Borrow untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 12 {runId}` milik Maya
31. Verifikasi aksi ditolak server walaupun Rahmat berperan Total Control
32. Maya meminta data tab Borrowed
33. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 12 {runId}` tetap berstatus `Waiting for Approval`

### Cancel Extension Request atas baris orang lain ditolak
34. Dedi mengirim Cancel Extension Request untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 13 {runId}` milik Maya
35. Verifikasi aksi ditolak server
36. Maya meminta data tab Borrowed
37. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 13 {runId}` tetap berstatus `Extension Request`

### Report Damaged atas baris orang lain ditolak
38. Dedi mengirim Report Damaged untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 14 {runId}` milik Maya
39. Verifikasi aksi ditolak server
40. Maya meminta data tab Borrowed
41. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 14 {runId}` tetap berstatus `Borrowed` tanpa badge `Reported Damaged`

### Report Missing atas baris orang lain ditolak
42. Dedi mengirim Report Missing untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 15 {runId}` milik Maya
43. Verifikasi aksi ditolak server
44. Maya meminta data tab Borrowed
45. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 15 {runId}` tetap berstatus `Borrowed` tanpa badge `Reported Missing`

### Cancel Damage Report atas laporan orang lain ditolak
46. Dedi mengirim Cancel Damage Report untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 16 {runId}` milik Maya
47. Verifikasi aksi ditolak server
48. Maya meminta data tab Borrowed
49. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 16 {runId}` tetap memuat badge `Reported Damaged`

### Cancel Missing Report atas laporan orang lain ditolak
50. Dedi mengirim Cancel Missing Report untuk baris pinjaman aset `Laptop Dell Latitude 5420 - 17 {runId}` milik Maya
51. Verifikasi aksi ditolak server
52. Maya meminta data tab Borrowed
53. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 17 {runId}` tetap memuat badge `Reported Missing`
