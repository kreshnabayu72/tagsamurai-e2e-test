---
id: TC-FA-ASSIGN-E2E-046-gating-approver
title: "Gating Approver: elemen Show, Hidden, dan Disabled menurut matriks role"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": 2
  "§2.1#r2": 2
  "§2.1#r3": 2
  "§2.1#r4": 2
  "§2.1#r5": 2
  "§2.1#r6": 9
  "§2.1#r7": 2
  "§2.1#r8": 2
  "§2.1#r9": 2
  "§2.1#r10": 2
  "§2.1#r11": 2
  "§2.1#r12": 2
  "§2.1#r13": 2
  "§2.1#r14": 2
  "§2.1#r15": 13
  "§2.1#r16": [7, 20, 21]
  "§4.8#r1": 2
  "§4.8#r2": 2
  "§4.8#r3": 2
  "§4.8#r4": 4
  "§4.8#r5": 2
  "§4.8#r6": 2
  "§4.8#r7": 2
  "§4.8#r8": 2
  "§4.8#r9": 2
  "§4.8#r10": 2
  "§4.8#r11": 2
  "§4.8#r12": 2
  "§4.8#r13": 2
  "§4.8#r14": 17
  "§4.8#r15": 1
  "§4.8#r16": 9
  "§4.8#r17": 13
anchor: [16]
coverage:
  web: automated
---

# Gating Approver: elemen Show, Hidden, dan Disabled menurut matriks role

## Prerequisites
- Aktor: Approver, user DU-046-1, mengerjakan seluruh langkah; Assignee dan pengaju adalah user lain di Data
- Layar awal: Fixed Asset, halaman mana pun dengan sidebar dan navbar tampil
- Data:
  - DU-046-1: User (Aktor Approver), Name `Putri Anggraini {runId}`, Role `Approver`, Cakupan `Group penugasan Head Office {runId} beserta descendant IT Head Office {runId}`, Tampil sebagai Assignee `Putri A`
  - DU-046-2: User (Assignee Employee), Name `Budi Santoso {runId}`, Role `tanpa role Assignment`, Tampil sebagai Assignee `Budi S`
  - DU-046-3: User (Pengaju pengajuan), Name `Agus Prasetyo {runId}`, Role `Asset Admin`, Cakupan `Head Office {runId}`, Tampil sebagai pengaju `Agus P`
  - DU-046-4: Group (Group utama), Name `Head Office {runId}`, Sub-group `IT Head Office {runId}`
  - DU-046-5: Assignment (ASG Waiting for Approval), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Waiting for Approval`, Aset `Server Dell R740 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Putri Anggraini {runId}`
  - DU-046-6: Assignment (ASG Assigned milik aktor sebagai Assignee), Assignee `Putri Anggraini {runId}`, Assignee Type `Employee`, Group `Head Office {runId}`, Status `Assigned`, Aset `Scanner Canon DR-C225 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Not required`
  - DU-046-7: Group (Group cabang), Name `Branch Surabaya {runId}`
  - DU-046-8: User (Approver Group cabang), Name `Dimas Pranoto {runId}`, Role `Approver`, Cakupan `Branch Surabaya {runId}`
  - DU-046-9: User (Pengaju Group cabang), Name `Maya Rahmawati {runId}`, Role `Asset Admin`, Cakupan `Branch Surabaya {runId}`
  - DU-046-10: Assignment (ASG Waiting for Approval di sub-group), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `IT Head Office {runId}`, Status `Waiting for Approval`, Aset `Laptop Lenovo ThinkPad T14 {runId}`, Requested By `Agus Prasetyo {runId}`, Approval `Waiting`, Approver aset `Putri Anggraini {runId}`
  - DU-046-11: Assignment (ASG Waiting for Approval di Group cabang), Assignee `Budi Santoso {runId}`, Assignee Type `Employee`, Group `Branch Surabaya {runId}`, Status `Waiting for Approval`, Aset `Drone DJI Mavic 3 {runId}`, Requested By `Maya Rahmawati {runId}`, Approval `Waiting`, Approver aset `Dimas Pranoto {runId}`
- Kondisi:
  - Feature Suite Assignment berada pada level `Full`
  - Aturan approval aset `Server Dell R740 {runId}` menunjuk aktor sebagai approver; pengaju bukan aktor

## Test Steps

### Menu Assignment di sidebar
1. Verifikasi menu `Approvals > Assignment` tampil di sidebar
2. Verifikasi menu `Transactions > Assignment` tidak tampil di sidebar sehingga tab, tombol, dan aksi baris Assignment tidak dapat dijangkau

### Quick Action tanpa Assign
3. Klik Quick Action pada navbar
4. Verifikasi item `Assign` tidak tampil pada menu Quick Action

### Antrean Approvals > Assignment dan keputusan per aset
5. Klik menu `Approvals > Assignment`
6. Ketik Search `{runId}`, tekan Enter
7. Verifikasi pengajuan dengan Assignee `Budi S` dan Group `Head Office {runId}` tampil pada tab `Active`
8. Klik `Review` pada pengajuan dengan Assignee `Budi S`
9. Verifikasi pilihan `Approve` dan `Reject` tampil pada kolom `Approval` aset `Server Dell R740 {runId}`
10. Klik `[Cancel]` pada footer halaman Review tanpa memutuskan

### Export riwayat approval
11. Klik menu `Approvals > Assignment`
12. Klik tab `History`
13. Verifikasi tombol `Download` tampil pada toolbar tab `History`[^drift-1]

### Task Confirm Handover di My Asset
14. Buka menu Profile pada navbar
15. Klik `My Asset`
16. Verifikasi aset `Scanner Canon DR-C225 {runId}` tampil pada tab `Assigned`
17. Verifikasi Task `Confirm Handover` tidak tampil

### Cakupan antrean Approver: Group penugasan beserta descendant
18. Klik menu `Approvals > Assignment`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi pengajuan atas aset `Laptop Lenovo ThinkPad T14 {runId}` dengan Group `IT Head Office {runId}` tampil pada tab `Active`
21. Verifikasi pengajuan atas aset `Drone DJI Mavic 3 {runId}` dengan Group `Branch Surabaya {runId}` tidak tampil pada tab `Active`

[^drift-1]: Drift PRD vs foundation. PRD §5 Global Table Rules baris Download: nama dan tooltip tombol toolbar adalah `Export`, bukan `Download`. foundation `prd-conventions.md` §9.1: icon toolbar bernama `Download` dengan tooltip `Download`, dan modul tidak menulis ulang teks tooltip itu. Diasersi: foundation, karena tombol unduh di toolbar tabel adalah pola bersama (SB-4).
