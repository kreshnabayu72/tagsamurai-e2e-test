---
id: TC-FA-FAREG-E2E-106-master-berubah-saat-approval-dep-settings-asset-name
title: "Master berubah saat halaman Approval terbuka: aset Unavailable"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: [F-FAREG-06.k2, FAREG-LOGIC-08f, FAREG-LOGIC-18b, FAREG-LOGIC-18c, FAREG-LOGIC-18d, FAREG-LOGIC-18f, §4.2.4#b9, §9.4.2#r18, S-REG-24, S-REG-29]
smoke: [S-REG-24, S-REG-29]
dependsOn:
  - "Settings Asset Name: arsip, hapus, dan lepas Brand atau Model"
trace:
  F-FAREG-06.k2: [4, 7]
  FAREG-LOGIC-08f: 18
  FAREG-LOGIC-18b: [4, 5]
  FAREG-LOGIC-18c: [4, 15]
  FAREG-LOGIC-18d: [7, 12, 13, 15]
  FAREG-LOGIC-18f: [8, 18]
  §4.2.4#b9: [4, 5]
  §9.4.2#r18: [4, 5, 7, 15]
  S-REG-24: 5
  S-REG-29: 7
anchor: [17]
coverage:
  web: automated
---

# Master berubah saat halaman Approval terbuka: aset Unavailable

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan capability Update pada node Group `Gudang Approval {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu perubahan master.
- Layar awal: Approvals > Registration > Active.
- Data:
  - DU-106-1: Group `Gudang Approval {runId}`, ada di entitas aktor.
  - DU-106-2: Asset Name `Laptop Approval {runId}` dengan TAG Type `Non-TAG`, Brand `Dell`, Model `Latitude 5440`.
  - DU-106-3: Model `Latitude 7440` milik Brand `Dell` pada Asset Name `Laptop Approval {runId}`, ada di master.
  - DU-106-4: Asset Name `Monitor Approval {runId}` dengan TAG Type `Non-TAG`, Brand `LG`, Model `27UP850`, dan Asset Label `Label Approval {runId}`.
  - DU-106-5: Asset Name `Kursi Approval {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-106-6: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Approval {runId}`, berisi 3 aset: 1 aset `Laptop Approval {runId}`, 1 aset `Monitor Approval {runId}`, dan 1 aset `Kursi Approval {runId}`, semua dengan keputusan awal `Approve`.
- Kondisi: approval registrasi pada Group `Gudang Approval {runId}` bernilai ON.

## Test Steps

### Model dihapus saat halaman Approval terbuka
1. Ketik Search `Gudang Approval {runId}`, tekan Enter
2. Klik row action `Review` pada baris pengajuan `Gudang Approval {runId}`
3. Admin menghapus Model `Latitude 5440` dari Brand `Dell` pada Asset Name `Laptop Approval {runId}`
4. Verifikasi baris aset `Laptop Approval {runId}` menampilkan Badge `Unavailable` pada kolom Model tanpa muat ulang halaman
5. Verifikasi `Alert` Warning `1 asset uses master data that is no longer available. Correct it, return it to Draft, or reject it before deciding.` tampil di atas tabel aset
6. Arahkan kursor ke tombol keputusan aset `Laptop Approval {runId}`
7. Verifikasi tombol keputusan aset `Laptop Approval {runId}` Disabled dengan tooltip `This asset uses master data that is no longer available.`
8. Verifikasi tombol keputusan aset `Monitor Approval {runId}` aktif

### Koreksi dengan nilai pengganti yang valid membuka blokir
9. Klik row option `Edit` pada baris aset `Laptop Approval {runId}`
10. Pilih Model `Latitude 7440`
11. Klik `[Save correction]`
12. Verifikasi baris aset `Laptop Approval {runId}` tidak lagi ditandai `Unavailable`
13. Verifikasi tombol keputusan aset `Laptop Approval {runId}` aktif

### Asset Name dihapus saat halaman Approval terbuka
14. Admin menghapus Asset Name `Kursi Approval {runId}`
15. Verifikasi `Alert` Warning `1 asset uses master data that is no longer available. Return it to Draft or reject it before deciding.` tampil di atas tabel aset

### Master lain tidak memengaruhi pengajuan
16. Admin mengarsipkan Asset Label `Label Approval {runId}`
17. Verifikasi baris aset `Monitor Approval {runId}` tampil dengan Decision `Approve`
18. Verifikasi tidak ada Badge `Unavailable` pada baris aset `Monitor Approval {runId}`
