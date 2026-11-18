---
id: TC-FA-ASSIGN-E2E-038-no-pic-handover-diblokir
title: "Baris No PIC: Handover diblokir sampai Change PIC"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-76, FI-ASG-40, S-ASG-11, ASSIGN-LOGIC-06m]
smoke: []
dependsOn: []
trace:
  EC-ASG-76: [10, 16, 17]
  FI-ASG-40: [6, 11]
  S-ASG-11: [5, 6]
  ASSIGN-LOGIC-06m: [5, 17]
anchor: [2, 9, 15]
coverage:
  web: automated
---

# Baris No PIC: Handover diblokir sampai Change PIC

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-038-1: Division `Field Survey`.
  - DU-038-2: User `Rudi Hartono`, mantan PIC Division `Field Survey`, berstatus nonaktif.
  - DU-038-3: User `Maya Lestari`, anggota aktif Division `Field Survey` dengan akun login, belum menjadi PIC.
  - DU-038-4: Aset `Alat Ukur Laser Bosch {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Waiting for Handover`.
  - DU-038-5: ASG dengan Assignee Division `Field Survey`, Group `Head Office`, memuat DU-038-4 dengan Approval `Not required` dan Purpose `Pemetaan lokasi proyek {runId}`; PIC `Rudi Hartono` nonaktif sehingga ASG berstatus `Waiting for Handover` dengan penanda `No PIC`.
- Kondisi:
  - Feature Suite Assignment pada level `Full`.

## Test Steps

### Hand Over diblokir selama No PIC
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi badge `No PIC` tampil pada kolom Status baris ASG DU-038-5
3. Klik menu ⋯ pada baris ASG DU-038-5
4. Arahkan kursor ke aksi `Hand Over`
5. Verifikasi aksi `Hand Over` disabled
6. Verifikasi alasan `Set a PIC for this division first.` tersampaikan pada aksi `Hand Over` yang disabled
7. Tekan Esc untuk menutup menu ⋯
8. Klik Transaction ID pada baris hasil pencarian
9. Verifikasi badge `No PIC` tampil pada baris judul Assignment Detail
10. Verifikasi kolom Status DU-038-4 menampilkan `Waiting for Handover`
11. Verifikasi tombol `[Change PIC]` tampil di bawah tabel Assets

### Change PIC membuka blokir Handover
12. Klik `[Change PIC]`
13. Pilih baris `Maya Lestari` pada dialog `Select User`
14. Klik `[Select]`
15. Verifikasi PIC pada header menampilkan `Maya Lestari`
16. Verifikasi badge `No PIC` tidak tampil pada header
17. Verifikasi tombol `[Hand Over]` tampil di bawah tabel Assets
