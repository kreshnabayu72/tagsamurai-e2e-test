---
id: TC-FA-FAREG-E2E-110-hak-dicabut-saat-halaman-terbuka-dep-settings-role-permission
title: "Hak dicabut saat halaman terbuka: aksi berikutnya ditolak"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r58, EB-AKS-6, T-REG-07, FAREG-LOGIC-10f]
smoke: [T-REG-07, FAREG-LOGIC-10f]
dependsOn: ["Settings Role Permission: ubah role pengguna"]
trace:
  §9.4.2#r58: [6, 13]
  EB-AKS-6: [6, 9, 10]
  T-REG-07: 6
  FAREG-LOGIC-10f: [6, 13]
anchor: [8]
coverage:
  web: automated
---

# Hak dicabut saat halaman terbuka: aksi berikutnya ditolak

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Hak {runId}` saat spec dimulai.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang mengubah role Rina.
  - Toni, role Total Control (seluruh client), hanya sebagai pengamat keadaan draft.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-110-1: Group `Gudang Hak {runId}`, ada di entitas aktor.
  - DU-110-2: batch Draft `Gudang Hak {runId}` berisi 1 Item Asset Name `Meja Hak {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
  - DU-110-3: Quantity `5` yang diketik Rina sebelum hak dicabut.

## Test Steps

### Hak dicabut saat form draft terbuka
1. Ketik Search `Gudang Hak {runId}`, tekan Enter
2. Klik row action `Edit` pada baris batch `Gudang Hak {runId}`
3. Ganti Quantity menjadi `5`
4. Admin mengganti role Rina dari Manage asset & TAG menjadi Read Only
5. Klik `[Save draft]`
6. Verifikasi toast `You don't have permission to do this.`

### UI menyembunyikan aksi yang tidak lagi berhak
7. Muat ulang halaman
8. Verifikasi sub tab `Waiting for Approval` tampil
9. Verifikasi sub tab `Draft` tidak tampil
10. Verifikasi tombol `[+ Register Asset]` tidak tampil

### Draft tidak berubah
11. Toni membuka sub tab Draft
12. Toni mengetik Search `Gudang Hak {runId}`, menekan Enter
13. Verifikasi baris batch `Gudang Hak {runId}` tetap dengan Total Asset `2`
