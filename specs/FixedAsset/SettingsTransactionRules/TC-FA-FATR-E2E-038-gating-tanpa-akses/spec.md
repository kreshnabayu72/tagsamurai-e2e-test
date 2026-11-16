---
id: TC-FA-FATR-E2E-038-gating-tanpa-akses
title: "Role tanpa akses tidak dapat membuka Transaction Settings"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§2#r4, §2#r11, EB-AKS-1, EB-AKS-2]
smoke: []
dependsOn: []
trace:
  §2#r4: [8, 11]
  §2#r11: [8, 10]
  EB-AKS-1: [3, 8]
  EB-AKS-2: [8, 10, 11, 12]
anchor: [7]
coverage:
  web: automated
---
# Role tanpa akses tidak dapat membuka Transaction Settings

## Prerequisites
- Aktor: pengguna Role lain `Bayu Santoso {runId}`, dengan pembanding pengguna Read Only `Hana Kusumawati {runId}`.
- Layar awal: Beranda Fixed Asset, halaman pertama yang terbuka setelah masuk.
- Data:
  - DU-038-1: User `Bayu Santoso {runId}`, Role lain: tanpa Global Role Manage transaction settings, tanpa Group Role Manage asset & TAG, bukan Total Control, bukan Default User, bukan Group Manager, tanpa tingkat akses Read Only, dengan akses baca ke modul Settings lain, ada di entitas aktor.
  - DU-038-2: User `Hana Kusumawati {runId}`, tingkat akses Read Only, ada di entitas aktor.
- Kondisi:
  - Akun `Bayu Santoso {runId}` dan `Hana Kusumawati {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Pengguna Read Only melihat item Transaction Settings di Sidebar sebagai pembanding
1. Masuk sebagai `Hana Kusumawati {runId}`
2. Klik menu `Settings` pada Sidebar
3. Verifikasi item `Transaction Settings` tampil pada Sidebar

### Role lain tidak melihat item Transaction Settings di Sidebar
4. Keluar dari akun `Hana Kusumawati {runId}`
5. Masuk sebagai `Bayu Santoso {runId}`
6. Klik menu `Settings` pada Sidebar
7. Verifikasi menu `Settings` memuat item modul Settings lain pada Sidebar
8. Verifikasi item `Transaction Settings` tidak tampil pada Sidebar

### Role lain membuka alamat halaman Transaction Settings secara langsung
9. Buka alamat halaman Transaction Settings secara langsung
10. Verifikasi toast `You don't have permission to do this.` tampil
11. Verifikasi isi halaman Transaction Settings tidak tampil
12. Verifikasi layar tidak dialihkan ke halaman lain
