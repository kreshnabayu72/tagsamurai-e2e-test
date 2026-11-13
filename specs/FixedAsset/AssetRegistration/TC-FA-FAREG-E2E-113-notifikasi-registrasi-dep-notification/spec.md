---
id: TC-FA-FAREG-E2E-113-notifikasi-registrasi-dep-notification
title: "Notifikasi registrasi bagi approver dan pengaju"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06j, FAREG-LOGIC-21c, §9.8#p1, §9.8#r1, §9.8#r2, EB-NTF-1, EB-XM-2@notification]
smoke: []
dependsOn: ["Notification: notifikasi in-app"]
trace:
  FAREG-LOGIC-06j: 10
  FAREG-LOGIC-21c: 17
  §9.8#p1: [7, 15, 19]
  §9.8#r1: 7
  §9.8#r2: [15, 19]
  EB-NTF-1: [7, 19]
  EB-XM-2@notification: [7, 8]
anchor: []
coverage:
  web: automated
---

# Notifikasi registrasi bagi approver dan pengaju

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Notif {runId}`, pengaju pengajuan.
  - Budi, role Manage asset & TAG dengan capability Update pada node Group `Gudang Notif {runId}`, approver.
  - Dewi, role Group Manager dengan Group binaan `Gudang Notif {runId}`, approver lain.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-113-1: Group `Gudang Notif {runId}`, ada di entitas aktor.
  - DU-113-2: Asset Name `Meja Notif {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-113-3: batch Draft `Gudang Notif {runId}` milik Rina berisi 1 Item Asset Name `Meja Notif {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
- Kondisi: approval registrasi pada Group `Gudang Notif {runId}` bernilai ON.

## Test Steps

### Submit memicu notifikasi actionable bagi approver dan tidak bagi pengaju
1. Rina mencatat jumlah notifikasi actionable di panel notifikasinya
2. Rina mengetik Search `Gudang Notif {runId}`, menekan Enter
3. Rina klik row action `Edit` pada baris batch `Gudang Notif {runId}`
4. Rina klik `[Submit]`
5. Rina klik `[Submit for Approval]`
6. Budi membuka panel notifikasi
7. Verifikasi notifikasi actionable dari pengajuan `Gudang Notif {runId}` tampil bagi Budi dengan tombol `[Detail]` dan `[Mark as Read]`
8. Verifikasi notifikasi actionable yang sama tampil bagi Dewi
9. Rina membuka panel notifikasinya
10. Verifikasi jumlah notifikasi actionable Rina sama dengan jumlah yang dicatat

### Keputusan approver menandai notifikasi approver lain sebagai Read
11. Budi klik `[Detail]` pada notifikasi pengajuan `Gudang Notif {runId}`
12. Budi klik `[Submit]` pada halaman Approval
13. Budi klik `[Submit]` pada dialog `Submit Approval`
14. Rina membuka panel notifikasinya
15. Verifikasi notifikasi hasil keputusan pengajuan `Gudang Notif {runId}` tampil bagi Rina
16. Dewi membuka panel notifikasi
17. Verifikasi notifikasi actionable pengajuan `Gudang Notif {runId}` milik Dewi berstatus Read
18. Rina membuka notifikasi hasil keputusan
19. Verifikasi notifikasi hasil keputusan Rina hanya memiliki tombol `[Mark as Read]`
