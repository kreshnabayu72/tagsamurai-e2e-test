---
id: TC-FA-FATR-E2E-019-picker-group
title: "Dialog Select Group menampilkan Group menurut cakupan aktor"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [D-03, §9.5#r22, §11#r8]
smoke: []
dependsOn: []
trace:
  D-03: [8, 10, 11, 13, 15, 25, 27, 28]
  §9.5#r22: [8, 25, 28]
  §11#r8: [8, 10]
anchor: [8, 25]
coverage:
  web: automated
---

# Dialog Select Group menampilkan Group menurut cakupan aktor

## Prerequisites
- Aktor: Total Control; lalu `Andi {runId}`, user dengan Group Role Manage asset & TAG (Read + Update) pada Group `Proyek Karawang {runId}` beserta turunannya.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-019-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-019-2: Group tingkat atas `Proyek Karawang {runId}`, aktif.
  - DU-019-3: Group `Workshop {runId}`, aktif, turunan langsung dari `Proyek Karawang {runId}`.
  - DU-019-4: Group tingkat atas `Proyek Bekasi {runId}`, aktif.
  - DU-019-5: Group tingkat atas `Proyek Lama {runId}`, nonaktif.
  - DU-019-6: user `Andi {runId}`, Group Role Manage asset & TAG (Read + Update), cakupan Group `Proyek Karawang {runId}` beserta turunannya.
- Kondisi:
  - Akun `Andi {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Total Control melihat semua Group aktif dan memilih parent mencakup turunannya
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Klik `[+ Override]`
5. Pilih Scope `Group`
6. Klik `[Select Group]`
7. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
8. Verifikasi node `Proyek Karawang {runId}` dan node `Proyek Bekasi {runId}` tampil pada dialog Select Group
9. Klik ikon perluas pada node `Proyek Karawang {runId}`
10. Verifikasi node `Workshop {runId}` tampil sebagai turunan `Proyek Karawang {runId}` pada dialog Select Group
11. Verifikasi node `Proyek Lama {runId}` tidak tampil pada dialog Select Group karena Group itu nonaktif
12. Centang node `Proyek Karawang {runId}`
13. Verifikasi node `Workshop {runId}` ikut tercentang karena memilih parent mencakup turunannya
14. Klik `[Select]`
15. Verifikasi badge target `Proyek Karawang {runId}` tampil di bawah tombol `[Select Group]` pada dialog Add override
16. Klik `✕` pada dialog, lalu klik `[Leave]` pada dialog Unsaved Changes

### Manage asset & TAG hanya melihat Group yang di-assign beserta turunannya
17. Masuk sebagai `Andi {runId}`
18. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
19. Klik node `Machinery {runId}` di Sidebar Category Tree
20. Klik tab `Borrow`
21. Klik `[+ Override]`
22. Pilih Scope `Group`
23. Klik `[Select Group]`
24. Ketik Search `{runId}` pada dialog Select Group, tekan Enter
25. Verifikasi node `Proyek Karawang {runId}` tampil pada dialog Select Group untuk `Andi {runId}`
26. Klik ikon perluas pada node `Proyek Karawang {runId}`
27. Verifikasi node `Workshop {runId}` tampil sebagai turunan `Proyek Karawang {runId}` untuk `Andi {runId}`
28. Verifikasi node `Proyek Bekasi {runId}` tidak tampil pada dialog Select Group karena berada di luar penugasan `Andi {runId}`
