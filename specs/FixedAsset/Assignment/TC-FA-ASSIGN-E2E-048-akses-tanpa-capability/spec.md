---
id: TC-FA-ASSIGN-E2E-048-akses-tanpa-capability
title: "Aktor tanpa capability: sidebar dan URL langsung"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-AKS-1", "EB-AKS-2", "§2.1#p1"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-1": [3, 9, 12]
  "EB-AKS-2": [5, 6, 7]
  "§2.1#p1": [3, 12]
anchor: [2, 11]
coverage:
  web: automated
---

# Aktor tanpa capability: sidebar dan URL langsung

## Prerequisites
- Aktor: Aktor tanpa capability `Dewi Lestari {runId}` (DU-048-1), lalu Read Only `Rudi Kurniawan {runId}` (DU-048-2), lalu PIC Division `Gita Permata {runId}` (DU-048-6)
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-048-1: User (Aktor tanpa capability di modul Assignment yang juga Assignee), Name `Dewi Lestari {runId}`, Role `tanpa capability di modul Assignment`, Cakupan `Head Office {runId}`
  - DU-048-2: User (Aktor Read Only), Name `Rudi Kurniawan {runId}`, Role `Read Only`, Cakupan `Seluruh client`
  - DU-048-3: Group (Group utama), Name `Head Office {runId}`
  - DU-048-4: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`
  - DU-048-5: Assignment (ASG Assigned dengan Assignee aktor tanpa capability), Assignee `Dewi Lestari {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Scanner Canon DR-C225 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-048-6: User (Aktor PIC Division tanpa capability di modul Assignment), Name `Gita Permata {runId}`, Role `tanpa capability di modul Assignment`, Cakupan `Head Office {runId}`
  - DU-048-7: Division (Division dengan Gita sebagai PIC), Name `Operations {runId}`, PIC `Gita Permata {runId}`, Anggota lain `Rina Wijaya {runId}`
  - DU-048-8: Assignment (ASG Assigned dengan Assignee Division yang PIC-nya aktor), Assignee `Operations {runId}`, Assignee Type `Division`, Group `Head Office {runId}`, Status `Assigned`, Aset `Docking Station Dell WD19 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`, PIC `Gita Permata {runId}`
- Kondisi:
  - Akun `Dewi Lestari {runId}`, `Rudi Kurniawan {runId}`, dan `Gita Permata {runId}` aktif, dan kredensial ketiganya disediakan fase 2
  - Feature Suite Assignment berada pada level `Full`

## Test Steps

### Aktor tanpa capability tidak melihat menu Assignment
1. Masuk sebagai aktor tanpa capability `Dewi Lestari {runId}`
2. Verifikasi sidebar menampilkan item menu lain yang boleh diakses aktor
3. Verifikasi menu `Transactions > Assignment` tidak tampil di sidebar

### URL langsung ke halaman Assignment ditolak
4. Buka alamat halaman Assignment secara langsung
5. Verifikasi toast `You don't have permission to do this.` tampil
6. Verifikasi aktor tidak diarahkan ke halaman lain
7. Verifikasi tab `Transactions`, `Assigned Assets`, dan `History` tidak tampil

### Aktor Read Only melihat menu Assignment
8. Masuk sebagai Read Only `Rudi Kurniawan {runId}`
9. Verifikasi menu `Transactions > Assignment` tampil di sidebar

### Aktor PIC Division tidak melihat menu Assignment
10. Masuk sebagai aktor PIC Division `Gita Permata {runId}`
11. Verifikasi sidebar menampilkan item menu lain yang boleh diakses aktor
12. Verifikasi menu `Transactions > Assignment` tidak tampil di sidebar
