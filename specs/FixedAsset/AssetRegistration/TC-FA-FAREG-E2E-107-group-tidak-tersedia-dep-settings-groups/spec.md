---
id: TC-FA-FAREG-E2E-107-group-tidak-tersedia-dep-settings-groups
title: "Group tidak tersedia: draft tampil No group yet"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [FAREG-LOGIC-08b, FAREG-LOGIC-08c, FAREG-LOGIC-08e, FAREG-LOGIC-18a, FAREG-LOGIC-18c, FAREG-LOGIC-18d, V-REG-01]
smoke: [V-REG-01]
dependsOn: ["Settings Groups: hapus atau ubah node Group"]
trace:
  FAREG-LOGIC-08b: [8, 10]
  FAREG-LOGIC-08c: [3, 5, 6]
  FAREG-LOGIC-08e: [3, 8, 10, 13]
  FAREG-LOGIC-18a: [18, 25]
  FAREG-LOGIC-18c: [18, 19]
  FAREG-LOGIC-18d: [19, 21]
  V-REG-01: 8
anchor: []
coverage:
  web: automated
---

# Group tidak tersedia: draft tampil No group yet

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Hapus {runId}` dan `Gudang Pengganti {runId}`, serta capability Update pada node Group `Gudang Hapus Approval {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu penghapusan node Group.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-107-1: Group `Gudang Hapus {runId}`, ada di entitas aktor.
  - DU-107-2: Group `Gudang Pengganti {runId}`, ada di entitas aktor.
  - DU-107-3: Group `Gudang Hapus Approval {runId}`, ada di entitas aktor.
  - DU-107-4: batch Draft `Gudang Hapus {runId}` berisi 1 Item Asset Name `Lemari Hapus {runId}` dengan TAG Type `Non-TAG`, Brand `Olympic`, Model `No Model`, Quantity `4`, dengan peringatan yang diharapkan `Gudang Hapus {runId} is not available. Choose another Group.`
  - DU-107-5: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Hapus Approval {runId}`, berisi 1 aset Asset Name `Lemari Hapus {runId}`, keputusan awal `Approve`.
- Kondisi: approval registrasi pada Group `Gudang Hapus Approval {runId}` bernilai ON.

## Test Steps

### Group dihapus saat draft tersimpan
1. Admin menghapus node Group `Gudang Hapus {runId}`
2. Ketik Search `No group yet`, tekan Enter
3. Verifikasi baris batch dengan Group `No group yet` dan Total Asset `4` tampil di sub tab Draft
4. Klik row action `Edit` pada baris batch dengan Group `No group yet`
5. Verifikasi `Alert` Warning `Gudang Hapus {runId} is not available. Choose another Group.` tampil di atas form
6. Verifikasi field Group dikosongkan: placeholder `Select group` tampil
7. Klik `[Save draft]`
8. Verifikasi error `Group must not be empty` tampil pada field Group
9. Klik `[Submit]`
10. Verifikasi dialog dengan `Are you sure you want to activate it?` tidak tampil
11. Pilih Group `Gudang Pengganti {runId}`
12. Klik `[Save draft]`
13. Verifikasi toast `Success, draft has been saved.`

### Group dihapus saat halaman Approval terbuka
14. Buka Approvals > Registration > Active
15. Ketik Search `Gudang Hapus Approval {runId}`, tekan Enter
16. Klik row action `Review` pada baris pengajuan `Gudang Hapus Approval {runId}`
17. Admin menghapus node Group `Gudang Hapus Approval {runId}`
18. Verifikasi baris aset `Lemari Hapus {runId}` ditandai `Unavailable` tanpa muat ulang halaman
19. Verifikasi `Alert` Warning `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.` tampil di atas tabel aset
20. Arahkan kursor ke tombol keputusan aset `Lemari Hapus {runId}`
21. Verifikasi tombol keputusan aset `Lemari Hapus {runId}` Disabled dengan tooltip `This asset uses master data that is no longer available.`
22. Klik `[Cancel]` pada halaman Approval
23. Ketik Search `Gudang Hapus Approval {runId}`, tekan Enter
24. Klik row action `Review` pada baris pengajuan `Gudang Hapus Approval {runId}`
25. Verifikasi baris aset `Lemari Hapus {runId}` tetap ditandai `Unavailable` saat halaman dibuka kembali
