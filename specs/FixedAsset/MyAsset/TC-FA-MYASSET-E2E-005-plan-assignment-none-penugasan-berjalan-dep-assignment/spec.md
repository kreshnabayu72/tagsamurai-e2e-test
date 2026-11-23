---
id: TC-FA-MYASSET-E2E-005-plan-assignment-none-penugasan-berjalan-dep-assignment
title: "Plan Assignment None dengan penugasan berjalan: tab Assigned read-only, tanpa Task Confirm Handover (Assignment), item My Asset hilang setelah penugasan terakhir ditutup"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r86", "§4.3#r9", "§9.10#p1", "§9.4.2#r97", "§9.4.2#r98", "§9.4.2#r99"]
smoke: []
dependsOn: ["Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
trace:
  "§1.2#r86": [12, 16, 20, 24]
  "§4.3#r9": [12, 16, 20, 24]
  "§9.10#p1": [3, 5, 6, 36, 38, 43]
  "§9.4.2#r97": [12, 16, 20]
  "§9.4.2#r98": [24, 29]
  "§9.4.2#r99": 43
anchor: [8, 9, 11, 15, 19, 23, 26, 28, 42]
coverage:
  web: automated
---

# Plan Assignment None dengan penugasan berjalan: tab Assigned read-only, tanpa Task Confirm Handover (Assignment), item My Asset hilang setelah penugasan terakhir ditutup

## Prerequisites
- Aktor: Assignee `Dian Pratiwi {runId}` di entitas khusus dengan plan Borrowing `None` dan Assignment `None`; entitas ini tidak dipakai spec lain. Aktor lain yang memicu perubahan: Aktor Assignment `Rina Wijaya {runId}`, yang menutup penugasan pada langkah 31 sampai 33 dan langkah 39 (LK-8).
- Layar awal: halaman FAMS yang memuat navbar.
- Data:
  - DU-005-1: Entitas `Entitas Level None Penugasan {runId}` dengan Borrowing level `None` dan Assignment level `None`; Borrowing dan Assignment tidak tersedia pada plan itu.
  - DU-005-2: User `Dian Pratiwi {runId}`, Assignee aktif di entitas DU-005-1, tanpa role admin, cakupan Group `Head Office`, tanpa pinjaman berjalan.
  - DU-005-3: User `Rina Wijaya {runId}`, Asset Admin dengan hak Aktor Assignment, cakupan Group `Head Office`, di entitas DU-005-1.
  - DU-005-4: penugasan atas nama `Dian Pratiwi {runId}`, aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Waiting for Handover`. Sesi Handover menunggu konfirmasi Assignee (Need recipient confirmation `Yes`, Aktor Assignment sudah menekan `[Request Confirmation]`) dan jendela konfirmasinya masih berlaku sampai langkah 31 selesai.
  - DU-005-5: penugasan atas nama `Dian Pratiwi {runId}`, aset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, Status `Assigned`.
  - DU-005-6: penugasan atas nama `Dian Pratiwi {runId}`, aset `Monitor Dell 24 inci {runId}`, Group `Head Office`, Status `Assigned` dengan badge `Reported Damaged`; Damage Report dilaporkan `Dian Pratiwi {runId}` dan berstatus `Waiting for Confirmation`.
  - DU-005-7: penugasan atas nama `Dian Pratiwi {runId}`, aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, Status `Assigned` dengan badge `Reported Missing`; laporan Missing dilaporkan `Dian Pratiwi {runId}` dan berstatus `Waiting for Confirmation`.
  - DU-005-8: penugasan atas nama `Dian Pratiwi {runId}`, aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, Status `Unassigned`.
- Kondisi:
  - Akun `Dian Pratiwi {runId}` aktif dan kredensialnya disediakan fase 2.
  - Entitas aktor memakai plan dengan Borrowing None dan Assignment None. Penugasan DU-005-4 sampai DU-005-7 sudah berjalan sebelum entitas diturunkan ke plan itu.
  - `Dian Pratiwi {runId}` tidak punya pinjaman berjalan dan tidak punya sesi Handover lain yang menunggu konfirmasinya selain DU-005-4.
  - Jendela konfirmasi sesi Handover DU-005-4 cukup panjang untuk seluruh langkah spec ini sampai langkah 31, sehingga tidak habis di tengah jalan.
  - Aktor Assignment dapat membatalkan penugasan yang menunggu Handover dan melepas penugasan (Unassign) yang sudah berjalan pada plan itu.

## Test Steps

### Item My Asset tampil dan tab disusun menurut level None selama ada penugasan berjalan
1. Masuk sebagai `Dian Pratiwi {runId}`
2. Klik avatar di navbar untuk membuka menu profil
3. Verifikasi item `My Asset` tampil di menu profil
4. Klik `My Asset`
5. Verifikasi tab `Task`, `Assigned`, dan `History` tampil
6. Verifikasi tab `Borrowed` tidak tampil

### Tab Assigned read-only: aksi laporan tidak tampil
7. Klik tab `Assigned`
8. Verifikasi baris `Printer HP LaserJet M404 {runId}`, `Laptop Lenovo ThinkPad T14 {runId}`, `Monitor Dell 24 inci {runId}`, dan `Scanner Zebra DS2208 {runId}` tampil di tabel Assigned
9. Verifikasi Status baris `Printer HP LaserJet M404 {runId}` adalah `Waiting for Handover`
10. Klik `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
11. Verifikasi menu baris `Laptop Lenovo ThinkPad T14 {runId}` memuat `Assignment Log`
12. Verifikasi `Report Damaged` dan `Report Missing` tidak tampil di menu baris `Laptop Lenovo ThinkPad T14 {runId}`
13. Tekan `Esc` untuk menutup menu baris
14. Klik `⋯` pada baris `Monitor Dell 24 inci {runId}`
15. Verifikasi menu baris `Monitor Dell 24 inci {runId}` memuat `Assignment Log`
16. Verifikasi `Cancel Damage Report` tidak tampil di menu baris `Monitor Dell 24 inci {runId}`
17. Tekan `Esc` untuk menutup menu baris
18. Klik `⋯` pada baris `Scanner Zebra DS2208 {runId}`
19. Verifikasi menu baris `Scanner Zebra DS2208 {runId}` memuat `Assignment Log`
20. Verifikasi `Cancel Missing Report` tidak tampil di menu baris `Scanner Zebra DS2208 {runId}`
21. Tekan `Esc` untuk menutup menu baris

### Task Confirm Handover (Assignment) tidak ada
22. Klik tab `Task`
23. Verifikasi empty state `No tasks` tampil pada tab Task
24. Verifikasi tidak ada baris Task `Confirm Handover` untuk penugasan DU-005-4

### Tab History read-only
25. Klik tab `History`
26. Verifikasi baris `Projector Epson EB-X06 {runId}` tampil di tab History dengan Status `Unassigned`
27. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
28. Verifikasi menu baris `Projector Epson EB-X06 {runId}` memuat `Assignment Log`
29. Verifikasi `Report Damaged`, `Report Missing`, `Cancel Damage Report`, dan `Cancel Missing Report` tidak tampil di menu baris `Projector Epson EB-X06 {runId}`
30. Tekan `Esc` untuk menutup menu baris

### Item My Asset dan alamat langsung tetap tersedia selama masih ada penugasan berjalan
31. Aktor Assignment `Rina Wijaya {runId}` membatalkan penugasan aset `Printer HP LaserJet M404 {runId}`
32. Aktor Assignment `Rina Wijaya {runId}` melepas penugasan aset `Laptop Lenovo ThinkPad T14 {runId}` (Unassign)
33. Aktor Assignment `Rina Wijaya {runId}` melepas penugasan aset `Monitor Dell 24 inci {runId}` (Unassign)
34. Muat ulang halaman
35. Klik avatar di navbar untuk membuka menu profil
36. Verifikasi item `My Asset` tetap tampil di menu profil karena penugasan `Scanner Zebra DS2208 {runId}` masih berjalan
37. Buka halaman My Asset lewat alamat langsung
38. Verifikasi halaman My Asset terbuka dan tidak ditolak, dengan tab `Assigned` tampil karena penugasan `Scanner Zebra DS2208 {runId}` masih berjalan

### Item My Asset hilang setelah penugasan terakhir ditutup
39. Aktor Assignment `Rina Wijaya {runId}` melepas penugasan aset `Scanner Zebra DS2208 {runId}` (Unassign)
40. Muat ulang halaman
41. Klik avatar di navbar untuk membuka menu profil
42. Verifikasi menu profil `Dian Pratiwi {runId}` memuat item akun lain
43. Verifikasi tidak ada item `My Asset` di menu profil karena Assignment dan Borrowing None dan tidak ada penugasan maupun pinjaman berjalan
