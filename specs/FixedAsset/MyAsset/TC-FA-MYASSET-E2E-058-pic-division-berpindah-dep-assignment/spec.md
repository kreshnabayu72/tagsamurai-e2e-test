---
id: TC-FA-MYASSET-E2E-058-pic-division-berpindah-dep-assignment
title: "Change PIC Division: baris dan Task pindah ke PIC baru dan PIC lama tidak melihatnya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§1.2#r49", "§9.4.2#r64", "§9.4.2#r65", "§9.7#r11"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "§1.2#r49": [10, 12, 15, 16]
  "§9.4.2#r64": [12, 13, 15, 16, 17]
  "§9.4.2#r65": [8, 10]
  "§9.7#r11": [8, 10, 12, 15, 16]
anchor: [2, 4]
coverage:
  web: automated
---

# Change PIC Division: baris dan Task pindah ke PIC baru dan PIC lama tidak melihatnya

## Prerequisites
- Aktor: PIC lama `Budi Santoso {runId}` dan PIC baru `Dewi Lestari {runId}` (keduanya karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`, tanpa hak Aktor Missing pada Group `Head Office`). Aktor Assignment `Rina Wijaya {runId}` (role `Asset Admin`, cakupan Group `Head Office`) hanya memicu perubahan.
- Layar awal: halaman My Asset, tab Task, dibuka oleh PIC lama.
- Data:
  - DU-058-1: pengguna `Budi Santoso {runId}`, role `Read Only`, cakupan Group `Head Office`, akun aktif, PIC Division `Finance {runId}` pada DU-058-6 dan DU-058-7 sebelum Change PIC, tanpa pinjaman dan tanpa penugasan pribadi.
  - DU-058-2: pengguna `Dewi Lestari {runId}`, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa penugasan lain sebelum Change PIC.
  - DU-058-3: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif, Aktor Assignment.
  - DU-058-4: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada Division `Finance {runId}`.
  - DU-058-5: aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, penugasan kepada Division `Finance {runId}` berstatus `Waiting for Handover`.
  - DU-058-6: penugasan Division `Finance {runId}` atas DU-058-4, status `Assigned`, PIC `Budi Santoso {runId}`.
  - DU-058-7: penugasan Division `Finance {runId}` atas DU-058-5, status `Waiting for Handover`, Need recipient confirmation `Yes`, PIC `Budi Santoso {runId}`, belum ada sesi Handover berjalan.
- Kondisi:
  - Akun `Dewi Lestari {runId}` aktif dan kredensialnya disediakan fase 2.
  - Jendela konfirmasi sesi Handover DU-058-7 belum habis selama spec berjalan.

## Test Steps

### PIC lama tidak lagi melihat Task dan baris sesudah Change PIC
1. Aktor Assignment `Rina Wijaya {runId}` menekan `[Request Confirmation]` pada Handover penugasan DU-058-7
2. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task` milik PIC lama `Budi Santoso {runId}` sebelum Change PIC
3. Klik tab `Assigned`
4. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` dan `Scanner Zebra DS2208 {runId}` tampil pada tab `Assigned` milik PIC lama sebelum Change PIC
5. Aktor Assignment `Rina Wijaya {runId}` mengganti PIC Division `Finance {runId}` pada penugasan DU-058-6 dari `Budi Santoso {runId}` menjadi `Dewi Lestari {runId}` (Change PIC)
6. Aktor Assignment `Rina Wijaya {runId}` mengganti PIC Division `Finance {runId}` pada penugasan DU-058-7 dari `Budi Santoso {runId}` menjadi `Dewi Lestari {runId}` (Change PIC)
7. Muat ulang halaman
8. Verifikasi `No assets are assigned to you` tampil pada tab `Assigned` milik PIC lama
9. Klik tab `Task`
10. Verifikasi `No tasks` tampil pada tab `Task` milik PIC lama

### PIC baru melihat Task dan baris yang berpindah
11. Masuk sebagai PIC baru `Dewi Lestari {runId}` lalu buka halaman My Asset
12. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task` milik PIC baru `Dewi Lestari {runId}`
13. Verifikasi sel Transaction ID baris Task memuat penanda ikon dan nama Division `Finance {runId}`
14. Klik tab `Assigned`
15. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` adalah `Assigned` pada tab `Assigned` milik PIC baru
16. Verifikasi Status baris `Scanner Zebra DS2208 {runId}` adalah `Waiting for Handover` pada tab `Assigned` milik PIC baru
17. Verifikasi kolom `Assigned To` kedua baris bernilai nama Division `Finance {runId}`
