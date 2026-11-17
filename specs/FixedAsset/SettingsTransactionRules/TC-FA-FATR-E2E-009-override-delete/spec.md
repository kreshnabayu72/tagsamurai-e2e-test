---
id: TC-FA-FATR-E2E-009-override-delete
title: "Delete satu override"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.4#r19, §4.4#r20, §4.4#r21, §9.4.2#r122, §9.4.2#r123, §9.6#r3, §9.6#r27, §9.7#r16, §7#r5, §9.2#b108, §9.2#b160, §9.4.2#r124, §9.6#r26, EB-FB-1@delete-override]
smoke: [§7#r5, §9.2#b108, §9.2#b160, §9.4.2#r124, §9.6#r26, EB-FB-1@delete-override]
dependsOn: []
trace:
  §4.4#r19: 9
  §4.4#r20: 12
  §4.4#r21: 11
  §9.4.2#r122: [9, 12]
  §9.4.2#r123: 11
  §9.6#r3: [12, 13]
  §9.6#r27: 11
  §9.7#r16: 12
  §7#r5: 11
  §9.2#b108: 9
  §9.2#b160: [20, 21]
  §9.4.2#r124: 12
  §9.6#r26: 12
  EB-FB-1@delete-override: 11
anchor: [5, 6, 19]
coverage:
  web: automated
---

# Delete satu override

## Prerequisites
- Aktor: Total Control; lalu `Andi {runId}`, user dengan Group Role Manage asset & TAG (Read + Update) pada Group `Proyek Bekasi {runId}` beserta turunannya.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-009-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-009-2: Group `Proyek Karawang {runId}`, `Proyek Bekasi {runId}`, dan `Proyek Cikarang {runId}`, masing-masing Group tingkat atas.
  - DU-009-3: override Group `Proyek Karawang {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (30 days)`; spec ini menghapusnya.
  - DU-009-4: override Group `Proyek Bekasi {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (20 days)`.
  - DU-009-5: override Group `Proyek Cikarang {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (25 days)`.
  - DU-009-6: user `Andi {runId}`, Group Role Manage asset & TAG (Read + Update), cakupan Group `Proyek Bekasi {runId}` beserta turunannya.
- Kondisi:
  - Akun `Andi {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Delete satu override dari menu baris
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days)` tampil di tabel Overrides
6. Verifikasi baris dengan Target `Proyek Bekasi {runId}` dan Overridden `Max duration (20 days)` tampil di tabel Overrides
7. Klik `⋯` pada baris `Proyek Karawang {runId}`
8. Klik `Delete`
9. Verifikasi dialog `Delete Override` terbuka
10. Klik ganda `[Delete]`
11. Verifikasi toast `Success, override has been deleted.` tampil
12. Verifikasi tidak ada baris dengan Target `Proyek Karawang {runId}` di tabel Overrides
13. Verifikasi baris dengan Target `Proyek Bekasi {runId}` dan Overridden `Max duration (20 days)` tetap tampil di tabel Overrides

### Aktor di luar scope tidak dapat menghapus override
14. Masuk sebagai `Andi {runId}`
15. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
16. Klik node `Machinery {runId}` di Sidebar Category Tree
17. Klik tab `Borrow`
18. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
19. Verifikasi menu `Delete` pada baris `Proyek Bekasi {runId}` aktif
20. Verifikasi menu `Delete` pada baris `Proyek Cikarang {runId}` disabled
21. Verifikasi alasan `This override is outside your scope.` tersampaikan pada menu `Delete` baris `Proyek Cikarang {runId}` yang disabled
