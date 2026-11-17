---
id: TC-FA-FATR-E2E-050-efek-asset-name-dep-asset-name
title: "Override mengikuti perubahan Asset Name"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r273, §4.1#r274, §9.4.2#r34, §9.2#b122, §9.2#b124, §9.2#b147, §9.2#b125]
smoke: []
dependsOn:
  - "Settings Asset Name: hapus, nonaktifkan, dan pindah Category"
trace:
  §4.1#r273: [7, 16]
  §4.1#r274: [8, 9, 17, 18]
  §9.4.2#r34: [6, 8, 15, 17]
  §9.2#b122: [6, 15]
  §9.2#b124: [7, 16]
  §9.2#b147: [6, 15]
  §9.2#b125: [8, 9, 17, 18]
anchor: [3, 12]
coverage:
  web: automated
---

# Override mengikuti perubahan Asset Name

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan akses penuh ke Asset Name.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-050-1: Category Name `Pumping Equipment {runId}`; Category leaf tempat override dibuat.
  - DU-050-2: Asset Name Name `Submersible Pump SP100 {runId}`, Category `Pumping Equipment {runId}`; Asset Name yang akan dihapus.
  - DU-050-3: Asset Name Name `Centrifugal Pump CP200 {runId}`, Category `Pumping Equipment {runId}`; Asset Name yang akan dinonaktifkan.
  - DU-050-4: Override Target `Submersible Pump SP100 {runId}`, Scope `Asset Name`, Category `Pumping Equipment {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Asset Name untuk Asset Name yang akan dihapus.
  - DU-050-5: Override Target `Centrifugal Pump CP200 {runId}`, Scope `Asset Name`, Category `Pumping Equipment {runId}`, Transaction `Borrow`, Max duration `12 Days`; override Asset Name untuk Asset Name yang akan dinonaktifkan.

## Test Steps

### Override tetap tampil dan tidak berlaku sesudah Asset Name dihapus
1. Masuk sebagai Default User
2. Buka tab `Borrow` pada node Category `Pumping Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
3. Verifikasi override untuk target `Submersible Pump SP100 {runId}` tampil di tabel Overrides
4. Hapus Asset Name `Submersible Pump SP100 {runId}`
5. Buka tab `Borrow` pada node Category `Pumping Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
6. Verifikasi override untuk target `Submersible Pump SP100 {runId}` tetap tersimpan dan tampil di tabel Overrides
7. Verifikasi nama terakhir target `Submersible Pump SP100 {runId}` tetap tampil pada baris override itu
8. Verifikasi `Not applied` tampil pada sel Target baris override untuk `Submersible Pump SP100 {runId}`
9. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target

### Override tetap tampil dan tidak berlaku sesudah Asset Name dinonaktifkan
10. Masuk sebagai Default User
11. Buka tab `Borrow` pada node Category `Pumping Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
12. Verifikasi override untuk target `Centrifugal Pump CP200 {runId}` tampil di tabel Overrides
13. Nonaktifkan Asset Name `Centrifugal Pump CP200 {runId}`
14. Buka tab `Borrow` pada node Category `Pumping Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
15. Verifikasi override untuk target `Centrifugal Pump CP200 {runId}` tetap tersimpan dan tampil di tabel Overrides
16. Verifikasi nama terakhir target `Centrifugal Pump CP200 {runId}` tetap tampil pada baris override itu
17. Verifikasi `Not applied` tampil pada sel Target baris override untuk `Centrifugal Pump CP200 {runId}`
18. Verifikasi alasan `This override doesn't apply because its target or category was deleted or deactivated.` tersampaikan pada `Not applied` di sel Target
