---
id: TC-FA-FATR-E2E-041-efek-assign-dep-assign
title: "Setting Assign berlaku pada transaksi Assign"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.2#b166", "§9.7#r28", "EB-XM-2@assign", "§9.2#b221", "§9.2#b261"]
smoke: ["§9.2#b221", "§9.2#b261"]
dependsOn:
  - "Assign: pengajuan, handover, Reassign, dan Unassign"
trace:
  "§9.2#b166": 10
  "§9.7#r28": 30
  "EB-XM-2@assign": [10, 17, 24]
  "§9.2#b221": 27
  "§9.2#b261": [27, 28]
anchor: [2]
coverage:
  web: automated
---

# Setting Assign berlaku pada transaksi Assign

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update).
- Layar awal: Fixed Asset > Assign.
- Data:
  - DU-041-1: Group Name `Production {runId}`; Group tanpa Division.
  - DU-041-2: Category Name `Heavy Equipment {runId}`, Allow Assign `Allow`; Category leaf dengan Allow Assign nilai sendiri.
  - DU-041-3: User Name `Wahyu Nugroho {runId}`, Role `Employee`, Group `Production {runId}`; akun aktif.
  - DU-041-4: User Name `Lia Kurniawati {runId}`, Role `Employee`, Group `Production {runId}`; akun aktif.
  - DU-041-5: Asset Name `Hydraulic Press HP80 {runId}`, Category `Heavy Equipment {runId}`, Group `Production {runId}`, Status `Available`; aset.
  - DU-041-6: Asset Name `Welding Robot WR12 {runId}`, Category `Heavy Equipment {runId}`, Group `Production {runId}`, Status `Waiting for Approval`; aset.
  - DU-041-7: Asset Name `Cutting Machine CM55 {runId}`, Category `Heavy Equipment {runId}`, Group `Production {runId}`, Status `Waiting for Handover`; aset.
  - DU-041-8: Assign Asset `Welding Robot WR12 {runId}`, Assignee `Wahyu Nugroho {runId}`, Status `Waiting for Approval`, Diajukan `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-041-9: Assign Asset `Cutting Machine CM55 {runId}`, Assignee `Lia Kurniawati {runId}`, Status `Waiting for Handover`, Disetujui `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-041-10: Override Target `Welding Robot WR12 {runId}`, Scope `Asset`, Transaction `Assign`, Require approval `ON`; override Asset untuk Assign yang membuat pengajuan Assign aset itu menunggu approval.
- Kondisi:
  - Pengajuan Assign aset `Welding Robot WR12 {runId}` dan `Cutting Machine CM55 {runId}` sudah melewati batas Transaction timeout statusnya masing-masing.

## Test Steps
### Override Allow Assign Deny dan penghapusannya tercermin di Assign
1. Ketik Search `Hydraulic Press HP80 {runId}` pada daftar aset di Fixed Asset > Assign, tekan Enter
2. Verifikasi aksi Assign pada baris aset `Hydraulic Press HP80 {runId}` aktif
3. Buka tab Assign pada node Category `Heavy Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
4. Klik `[+ Override]` pada bagian Overrides
5. Isi Scope `Asset` dengan Target `Hydraulic Press HP80 {runId}`
6. Pilih Field `Allow Assign` dengan Value `Deny`
7. Klik `[Submit]`
8. Buka Fixed Asset > Assign
9. Ketik Search `Hydraulic Press HP80 {runId}` pada daftar aset di Fixed Asset > Assign, tekan Enter
10. Verifikasi aksi Assign pada baris aset `Hydraulic Press HP80 {runId}` disabled, dengan alasan dan kontak tersampaikan pada aksi itu
11. Buka tab Assign pada node Category `Heavy Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
12. Buka menu ⋯ pada baris override untuk `Hydraulic Press HP80 {runId}`
13. Klik `Delete`
14. Klik `[Delete]` pada dialog Delete Override
15. Buka Fixed Asset > Assign
16. Ketik Search `Hydraulic Press HP80 {runId}` pada daftar aset di Fixed Asset > Assign, tekan Enter
17. Verifikasi aksi Assign pada baris aset `Hydraulic Press HP80 {runId}` aktif lagi

### Perubahan nilai Category berlaku untuk penugasan baru
18. Buka tab Assign pada node Category `Heavy Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
19. Pilih nilai `Deny` pada field Allow Assign
20. Klik `[Save]`
21. Klik `[Save]` pada dialog Save Changes
22. Buka Fixed Asset > Assign
23. Ketik Search `Hydraulic Press HP80 {runId}` pada daftar aset di Fixed Asset > Assign, tekan Enter
24. Verifikasi aksi Assign pada baris aset `Hydraulic Press HP80 {runId}` disabled sesuai nilai baru Category `Heavy Equipment {runId}`

### Transaksi yang melewati Transaction timeout berakhir Canceled
25. Job Transaction timeout berjalan
26. Buka daftar Assign
27. Verifikasi penugasan aset `Welding Robot WR12 {runId}` yang menunggu approval berstatus `Canceled`
28. Verifikasi penugasan aset `Cutting Machine CM55 {runId}` yang menunggu handover berstatus `Canceled` dan bukan `Expired`
29. Buka detail penugasan aset `Welding Robot WR12 {runId}` di daftar Assign
30. Verifikasi daftar dan detail transaksi Assign aset `Welding Robot WR12 {runId}` sama-sama menampilkan status `Canceled`
