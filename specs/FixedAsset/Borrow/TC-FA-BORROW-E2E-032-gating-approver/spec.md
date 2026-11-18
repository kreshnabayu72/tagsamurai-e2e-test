---
id: TC-FA-BORROW-E2E-032-gating-approver
title: "Approver hanya melihat menu Approvals > Borrow dan keputusan atas aset yang eligible"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§2.1#r14", "§2.1#r15", "§2.1#r16", "§2.1#r17", "§2.1#r18", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [2, 5]
  "§4.8#r1": [2, 5]
  "§2.1#r2": [5]
  "§4.8#r2": [5]
  "§2.1#r3": [5]
  "§4.8#r3": [5]
  "§2.1#r4": [5]
  "§4.8#r4": [5]
  "§2.1#r5": [5]
  "§4.8#r5": [5]
  "§2.1#r6": [14, 15]
  "§4.8#r6": [5]
  "§2.1#r7": [5]
  "§4.8#r7": [5]
  "§2.1#r8": [5]
  "§4.8#r8": [5]
  "§2.1#r9": [5]
  "§4.8#r9": [5]
  "§2.1#r10": [5]
  "§4.8#r10": [5]
  "§2.1#r11": [5]
  "§4.8#r11": [5]
  "§2.1#r12": [5]
  "§4.8#r12": [5]
  "§2.1#r13": [5]
  "§4.8#r13": [5]
  "§2.1#r14": [5]
  "§4.8#r14": [5]
  "§2.1#r15": [5]
  "§4.8#r15": [5]
  "§2.1#r16": [5]
  "§4.8#r16": [1]
  "§2.1#r17": [19, 20]
  "§4.8#r17": [14]
  "§2.1#r18": [8, 10, 11]
  "§4.8#r18": [9, 20]
anchor: [4]
coverage:
  web: automated
---

# Approver hanya melihat menu Approvals > Borrow dan keputusan atas aset yang eligible

## Prerequisites
- Aktor: Approver (cakupan Group penugasan `Head Office {runId}` dan turunannya).
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-032-1: User `Budi Santoso {runId}`, Role Transaksi Approver pada Group `Head Office {runId}` dan turunannya, aktif.
  - DU-032-2: User `Agus Pratama {runId}`, role Asset Admin, Group penugasan `Head Office {runId}`, aktif.
  - DU-032-3: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-032-4: Karyawan `Dewi Lestari {runId}`, aktif, Home Group `Branch Surabaya {runId}`.
  - DU-032-5: Group `Head Office {runId}`, penugasan `Budi Santoso {runId}`.
  - DU-032-6: Group `IT Support {runId}`, turunan dari `Head Office {runId}`.
  - DU-032-7: Group `Branch Surabaya {runId}`, bukan penugasan `Budi Santoso {runId}`.
  - DU-032-8: BRW berstatus Waiting for Approval dengan `Budi Santoso {runId}` sebagai approver aset itu, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Agus Pratama {runId}`.
  - DU-032-9: BRW berstatus Waiting for Approval dengan `Budi Santoso {runId}` sebagai approver aset itu, Group `IT Support {runId}`, Borrower `Rudi Hartono {runId}`, aset `Router Cisco ISR {runId}`, Duration `3 days`, Purpose `Pemasangan jaringan`, Requested By `Agus Pratama {runId}`.
  - DU-032-10: BRW berstatus Waiting for Approval dengan approver lain, Group `Branch Surabaya {runId}`, Borrower `Dewi Lestari {runId}`, aset `Genset Perkins 20 kVA {runId}`, Duration `7 days`, Purpose `Cadangan listrik`, Requested By `Agus Pratama {runId}`.
  - DU-032-11: BRW berstatus Waiting for Handover setelah disetujui `Budi Santoso {runId}` (riwayat approval: Approved), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Projector Epson EB-X06 {runId}`, Duration `4 days`, Purpose `Presentasi vendor`, Requested By `Agus Pratama {runId}`.
- Kondisi:
  - Level Feature Suite Borrowing entitas aktor bernilai `Full`.

## Test Steps

### Menu Approvals > Borrow tampil dan menu Transactions > Borrow tidak tampil
1. Verifikasi menu `Approvals > Borrow` tampil di sidebar
2. Verifikasi menu `Transactions > Borrow` tidak tampil di sidebar

### URL langsung ke halaman Borrow tidak membuka isinya
3. Buka URL halaman `Transactions > Borrow` secara langsung
4. Verifikasi toast `You don't have permission to do this.` tampil untuk Approver
5. Verifikasi isi halaman Borrow (tab `Transactions`, `Drafts`, `Borrowed Assets`, `History`, tabel BRW, dan tombol `[+ Borrow]`) tidak dirender

### Antrean Active memuat pengajuan dalam Group penugasan dan turunannya
6. Klik menu `Approvals > Borrow`
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi pengajuan BRW milik DU-032-8 dengan Group `Head Office {runId}` tampil di tab `Active`
9. Verifikasi `Download` tidak tampil di toolbar tab `Active`
10. Verifikasi pengajuan BRW milik DU-032-9 dengan Group `IT Support {runId}` tampil di tab `Active`
11. Verifikasi pengajuan BRW milik DU-032-10 dengan Group `Branch Surabaya {runId}` tidak tampil di tab `Active`

### Keputusan atas aset yang eligible di halaman Review
12. Buka menu ⋯ pada baris pengajuan BRW milik DU-032-8
13. Klik `Review`
14. Verifikasi pilihan keputusan `Approve` dan `Reject` tampil dan dapat dipilih untuk aset `Meeting Mic Set {runId}`
15. Verifikasi tombol `[Submit]` tampil di footer halaman Review
16. Klik `[Cancel]` pada halaman Review; keputusan belum diisi sehingga tidak ada yang tersimpan

### Download riwayat approval di tab History
17. Klik tab `History`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi pengajuan BRW milik DU-032-11 tampil di tab `History`
20. Verifikasi `Download` tampil di toolbar tab `History`
