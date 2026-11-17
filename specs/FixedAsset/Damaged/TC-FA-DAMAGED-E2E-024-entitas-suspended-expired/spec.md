---
id: TC-FA-DAMAGED-E2E-024-entitas-suspended-expired
title: "Pada entitas Suspended atau Expired aksi tulis Damaged ditolak dengan toast baku dan aksi baca tetap berjalan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [EC-DMG-30, §9.4.4#r14, §9.4.1#r1, EB-AKS-7]
smoke: []
dependsOn: []
trace:
  EC-DMG-30: [16, 17, 18, 21, 29, 30, 31, 34]
  §9.4.4#r14: [17, 18, 30, 31]
  §9.4.1#r1: [2, 12, 16, 25, 29]
  EB-AKS-7: [6, 7, 16, 29]
anchor: []
coverage:
  web: automated
---

# Pada entitas Suspended atau Expired aksi tulis Damaged ditolak dengan toast baku dan aksi baca tetap berjalan

## Prerequisites
- Aktor: Total Control pada entitas Active (DU-024-4), entitas Suspended (DU-024-5), dan entitas Expired (DU-024-6); spec ini memakai entitas khusus yang tidak dipakai spec lain.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-024-1: Entitas `Client Aktif {runId}` berstatus Active.
  - DU-024-2: Entitas `Client Suspended {runId}` berstatus Suspended.
  - DU-024-3: Entitas `Client Expired {runId}` berstatus Expired.
  - DU-024-4: User `Rina Wijaya {runId}`, role Total Control pada entitas `Client Aktif {runId}`; cakupan: seluruh entitas itu.
  - DU-024-5: User `Agus Pratama {runId}`, role Total Control pada entitas `Client Suspended {runId}`; cakupan: seluruh entitas itu.
  - DU-024-6: User `Dewi Anggraeni {runId}`, role Total Control pada entitas `Client Expired {runId}`; cakupan: seluruh entitas itu.
  - DU-024-7: Damage record aset `Laptop Dell Latitude 5420 {runId}` di entitas `Client Aktif {runId}`, Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`.
  - DU-024-8: Damage record aset `Laptop Dell Latitude 5420 {runId}` di entitas `Client Suspended {runId}`, Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`.
  - DU-024-9: Damage record aset `Laptop Dell Latitude 5420 {runId}` di entitas `Client Expired {runId}`, Group `Head Office {runId}`, status `Waiting for Confirmation`, Source `Reported by holder`.

## Test Steps

### Aksi tulis berhasil pada entitas Active
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` pada entitas Active tampil di tabel dengan status `Waiting for Confirmation`
3. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
4. Klik `Review`
5. Klik `[Confirm]`
6. Verifikasi toast `Success, report has been confirmed.` tampil pada entitas Active
7. Verifikasi badge status record pada dialog `Damage Log` entitas Active `Damaged`
8. Klik `✕` pada dialog `Damage Log`

### Aksi tulis ditolak pada entitas Suspended
9. Masuk sebagai Agus Pratama {runId} pada entitas `Client Suspended {runId}`
10. Klik tab `Damaged`
11. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
12. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` pada entitas `Client Suspended {runId}` tampil di tabel dengan status `Waiting for Confirmation`
13. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Klik `Review`
15. Klik `[Confirm]`
16. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada entitas `Client Suspended {runId}`
17. Verifikasi badge status record pada dialog `Damage Log` entitas `Client Suspended {runId}` tetap `Waiting for Confirmation`
18. Verifikasi timeline entitas `Client Suspended {runId}` tidak memuat node `Report confirmed by`
19. Klik `✕` pada dialog `Damage Log`
20. Klik sub-tab `History`
21. Verifikasi sub-tab `History` entitas `Client Suspended {runId}` dapat dibuka dan menampilkan toolbar

### Aksi tulis ditolak pada entitas Expired
22. Masuk sebagai Dewi Anggraeni {runId} pada entitas `Client Expired {runId}`
23. Klik tab `Damaged`
24. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
25. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` pada entitas `Client Expired {runId}` tampil di tabel dengan status `Waiting for Confirmation`
26. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
27. Klik `Review`
28. Klik `[Confirm]`
29. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil pada entitas `Client Expired {runId}`
30. Verifikasi badge status record pada dialog `Damage Log` entitas `Client Expired {runId}` tetap `Waiting for Confirmation`
31. Verifikasi timeline entitas `Client Expired {runId}` tidak memuat node `Report confirmed by`
32. Klik `✕` pada dialog `Damage Log`
33. Klik sub-tab `History`
34. Verifikasi sub-tab `History` entitas `Client Expired {runId}` dapat dibuka dan menampilkan toolbar
