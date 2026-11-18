---
id: TC-FA-DAMAGED-E2E-010-review-reject
title: "Reject laporan lewat D-DMG-04 dengan Reason memindahkan record ke History sebagai Rejected dan menambah node Report rejected by"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, D-DMG-04, §4.2.4#p4, §4.2.4#r13, §4.4#r6, §4.4#p1, §8.1#b1, §8.1#r8, TS-DMG-04, §Aturan Logika Modul#r52, §Aturan Logika Modul#r22, §9.7#r6, FLD-DMG-06, §9.6#r3, F-DMG-04, EB-FB-1@reject, EB-FRM-1@reject-report]
smoke: [EB-FB-1@reject, EB-FRM-1@reject-report]
dependsOn: []
trace:
  T-DMG-01: [3, 5]
  D-DMG-04: [9, 18, 25]
  §4.2.4#p4: 9
  §4.2.4#r13: [9, 12, 16]
  §4.4#r6: [7, 9, 12]
  §4.4#p1: [13, 14, 15, 16, 17, 22]
  §8.1#b1: [13, 15, 17]
  §8.1#r8: [17, 18]
  TS-DMG-04: 12
  §Aturan Logika Modul#r52: [16, 18]
  §Aturan Logika Modul#r22: [16, 25]
  §9.7#r6: [21, 22, 25]
  FLD-DMG-06: 18
  §9.6#r3: [12, 16, 17]
  F-DMG-04: [12, 16, 25]
  EB-FB-1@reject: 12
  EB-FRM-1@reject-report: [19, 26]
anchor: []
coverage:
  web: automated
---

# Reject laporan lewat D-DMG-04 dengan Reason memindahkan record ke History sebagai Rejected dan menambah node Report rejected by

## Prerequisites
- Aktor: Total Control (DU-010-4).
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-010-1: Damage record aset `Camera Canon EOS {runId}` di Group `Head Office`, status `Waiting for Confirmation`, Source `Reported by holder`, dilaporkan pemegang aset DU-010-3 dengan What happened `Lensa kamera berembun dan gambar tidak fokus`; Damage Log hanya memuat node `Reported damaged by`.
  - DU-010-3: User `Dewi Anggraeni {runId}`, pelapor umum pemegang aset DU-010-1, tanpa hak Aktor Damaged; cakupan: aset yang ia pegang.
  - DU-010-4: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client.

## Test Steps

### Reject dari footer Damage Log membuka dialog Reject Report
1. Catat jumlah pada badge tab `Damaged` sebagai jumlah awal
2. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
3. Verifikasi baris aset `Camera Canon EOS {runId}` tampil di tabel dengan status `Waiting for Confirmation`
4. Klik `⋯` pada baris `Camera Canon EOS {runId}`
5. Verifikasi item `Review` tampil pada menu baris
6. Klik `Review`
7. Verifikasi footer dialog `Damage Log` memuat tombol `[Reject]` dan `[Confirm]` yang aktif
8. Klik `[Reject]`
9. Verifikasi dialog `Reject Report` terbuka dengan nama aset `Camera Canon EOS {runId}`

### Reject dengan Reason memindahkan record ke History sebagai Rejected
10. Isi Reason `Foto kerusakan berbeda dari aset yang dilaporkan`
11. Klik `[Reject]` pada dialog `Reject Report`
12. Verifikasi toast `Success, report has been rejected.` tampil
13. Verifikasi dialog `Damage Log` tetap terbuka
14. Verifikasi dialog `Reject Report` tidak lagi tampil
15. Verifikasi tombol `[Reject]` dan `[Confirm]` tidak lagi tampil di footer dialog `Damage Log`
16. Verifikasi badge status record pada dialog `Damage Log` `Rejected`
17. Verifikasi timeline memuat node `Report rejected by` dengan aktor yang sedang masuk sebagai pelaku
18. Verifikasi node `Report rejected by` memuat baris detail Reason `Foto kerusakan berbeda dari aset yang dilaporkan`
19. Verifikasi timeline memuat tepat satu node `Report rejected by`
20. Klik `✕` pada dialog `Damage Log`
21. Verifikasi badge tab `Damaged` berkurang satu dari jumlah awal
22. Verifikasi sub-tab Active menampilkan `No results found` untuk Search `Camera Canon EOS {runId}`
23. Klik sub-tab `History`
24. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
25. Verifikasi baris aset `Camera Canon EOS {runId}` tampil di tabel History dengan status `Rejected`
26. Verifikasi hasil Search di History berjumlah satu baris
