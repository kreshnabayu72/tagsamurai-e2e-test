---
id: TC-FA-MYASSET-E2E-051-confirm-handover-penugasan-ditolak-dep-assignment
title: "Confirm Handover penugasan ditolak: sesi dibatalkan Aktor dan transaksi tidak aktif lagi"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r72", "§3#p7", "§4.2.5#p11", "§4.2.5#r6", "§9.4.2#r52", "§9.4.2#r53", "§9.4.2#r54", "§9.4.2#r55", "§9.4.2#r56", "§9.7#r7"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "§1.2#r72": [12, 26]
  "§3#p7": [12, 14, 26]
  "§4.2.5#p11": [9, 24]
  "§4.2.5#r6": [8, 9, 11, 12, 14, 23, 24, 26]
  "§9.4.2#r52": [8, 23]
  "§9.4.2#r53": [12, 26]
  "§9.4.2#r54": 14
  "§9.4.2#r55": [12, 26]
  "§9.4.2#r56": [8, 23]
  "§9.7#r7": [12, 26]
anchor: [2, 17]
coverage:
  web: automated
---

# Confirm Handover penugasan ditolak: sesi dibatalkan Aktor dan transaksi tidak aktif lagi

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`). Aktor Assignment `Rina Wijaya {runId}` (role `Asset Admin`, cakupan Group `Head Office`) hanya memicu perubahan.
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-051-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa Task lain dan tanpa penugasan lain.
  - DU-051-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif.
  - DU-051-3: aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-051-4: aset `Tablet Samsung Galaxy Tab A9 {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-051-5: penugasan dengan Assignee `Budi Santoso {runId}`, memuat DU-051-3, status `Waiting for Handover`, Need recipient confirmation `Yes`, belum ada sesi Handover berjalan.
  - DU-051-6: penugasan dengan Assignee `Budi Santoso {runId}`, memuat DU-051-4, status `Waiting for Handover`, Need recipient confirmation `Yes`, belum ada sesi Handover berjalan.
- Kondisi:
  - Jendela konfirmasi tiap sesi Handover belum habis selama spec berjalan.

## Test Steps

### Sesi Handover dibatalkan Aktor saat dialog Confirm Handover terbuka
1. Aktor Assignment `Rina Wijaya {runId}` menekan `[Request Confirmation]` pada Handover penugasan DU-051-5
2. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task` sebelum sesi dibatalkan
3. Klik `⋯` pada baris Task
4. Klik `[Confirm Handover]` pada menu baris Task
5. Aktor Assignment `Rina Wijaya {runId}` membatalkan sesi Handover penugasan DU-051-5
6. Centang pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
7. Klik `[Confirm]` pada footer dialog

### Dialog Handover No Longer Available untuk sesi yang dibatalkan Aktor
8. Verifikasi dialog `Handover No Longer Available` tampil sebagai penolakan Confirm
9. Verifikasi dialog memuat teks `[Admin] canceled this handover request. Ask them to start again if you still need the assets.` dengan `[Admin]` diisi nama Aktor Assignment penyerah
10. Klik `[OK]` pada dialog `Handover No Longer Available`
11. Verifikasi dialog `Handover No Longer Available` tertutup sesudah `[OK]`
12. Verifikasi `No tasks` tampil pada tab `Task` sesudah sesi dibatalkan

### Baris penugasan tetap Waiting for Handover sesudah sesi dibatalkan
13. Klik tab `Assigned`
14. Verifikasi aset `Scanner Zebra DS2208 {runId}` tetap berstatus `Waiting for Handover` sesudah penolakan

### Transaksi penugasan dibatalkan saat dialog Confirm Handover terbuka
15. Klik tab `Task`
16. Aktor Assignment `Rina Wijaya {runId}` menekan `[Request Confirmation]` pada Handover penugasan DU-051-6
17. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task` sebelum transaksi dibatalkan
18. Klik `⋯` pada baris Task
19. Klik `[Confirm Handover]` pada menu baris Task
20. Aktor Assignment `Rina Wijaya {runId}` membatalkan transaksi penugasan DU-051-6
21. Centang pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
22. Klik `[Confirm]` pada footer dialog

### Dialog Handover No Longer Available untuk transaksi yang tidak aktif lagi
23. Verifikasi dialog `Handover No Longer Available` tampil sebagai penolakan Confirm atas transaksi yang dibatalkan
24. Verifikasi dialog memuat teks `This assignment is no longer active.`
25. Klik `[OK]` pada dialog `Handover No Longer Available`
26. Verifikasi `No tasks` tampil pada tab `Task` sesudah transaksi dibatalkan
