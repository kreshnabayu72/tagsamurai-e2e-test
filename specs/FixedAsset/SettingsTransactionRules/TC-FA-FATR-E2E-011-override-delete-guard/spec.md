---
id: TC-FA-FATR-E2E-011-override-delete-guard
title: "Delete override ditolak guard Allowed assignee"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r347, §4.4#r22, §6#r29, §6#r32, §6#r33, D-07, FI-01sampaiFI-14, §9.2#b113, §9.2#b118, §9.2#b186, §9.4.2#r75, §9.4.2#r76, §9.4.2#r77, §9.4.2#r80, §9.6#r30, §9.6#r33, §9.9#r22, §9.2#b110, §9.2#b114, §9.2#b188, §9.6#r31]
smoke: [§9.2#b110, §9.2#b114, §9.2#b188, §9.6#r31]
dependsOn: []
trace:
  §4.1#r347: [39, 40]
  §4.4#r22: [8, 10, 27, 30]
  §6#r29: [15, 37, 38]
  §6#r32: [30, 34]
  §6#r33: [32, 33]
  D-07: [10, 14, 30, 36]
  FI-01sampaiFI-14: [10, 12, 28]
  §9.2#b113: [10, 11]
  §9.2#b118: [30, 34]
  §9.2#b186: [10, 11]
  §9.4.2#r75: [10, 11, 30, 31]
  §9.4.2#r76: [12, 34]
  §9.4.2#r77: [15, 37]
  §9.4.2#r80: [30, 32, 33, 34]
  §9.6#r30: [10, 12]
  §9.6#r33: [30, 34]
  §9.9#r22: [11, 31]
  §9.2#b110: 10
  §9.2#b114: 15
  §9.2#b188: 15
  §9.6#r31: 15
anchor: [5, 21, 22]
coverage:
  web: automated
---

# Delete override ditolak guard Allowed assignee

## Prerequisites
- Aktor: Total Control; lalu `Andi {runId}`, user dengan Group Role Manage asset & TAG (Read + Update) pada Group `Proyek Guard {runId}` beserta turunannya.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-011-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-011-2: Group tingkat atas `Proyek Guard {runId}`.
  - DU-011-3: Group tingkat atas `Proyek Luar {runId}`.
  - DU-011-4: aset `Forklift FL25 {runId} - 1`, ber-Group `Proyek Guard {runId}` dan Category `Machinery {runId}`.
  - DU-011-5: override Group `Proyek Guard {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Allowed assignee: Division (ON)`.
  - DU-011-6: override Group `Proyek Guard {runId}` di All categories transaksi `Assign`, Overridden `Allowed assignee: Employee (OFF), Allowed assignee: Division (OFF)`.
  - DU-011-7: override Group `Proyek Luar {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Recipient acceptance (Optional)`.
  - DU-011-8: user `Andi {runId}`, Group Role Manage asset & TAG (Read + Update), cakupan Group `Proyek Guard {runId}` beserta turunannya.
- Kondisi:
  - Allow Assign bukan Deny untuk aset `Forklift FL25 {runId} - 1`.
  - Akun `Andi {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Delete satu override ditolak guard dan override tetap ada
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Assign`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tampil di tabel Overrides
6. Klik `⋯` pada baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)`
7. Klik `Delete`
8. Verifikasi dialog `Delete Override` terbuka untuk override `Allowed assignee: Division (ON)` milik `Proyek Guard {runId}`
9. Klik `[Delete]`
10. Verifikasi dialog `Cannot Delete Override` tampil
11. Verifikasi pesan `At least one assignee type must be enabled` tampil pada dialog `Cannot Delete Override`
12. Verifikasi toast `Success, override has been deleted.` tidak tampil
13. Klik `[OK]`
14. Verifikasi dialog `Cannot Delete Override` tertutup
15. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tetap tampil di tabel Overrides

### Bulk Delete seleksi yang ditolak guard dan di luar scope hanya menampilkan Dialog Blok
16. Masuk sebagai `Andi {runId}`
17. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
18. Klik node `Machinery {runId}` di Sidebar Category Tree
19. Klik tab `Assign`
20. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
21. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tampil di tabel Overrides sebagai baris di dalam scope
22. Verifikasi baris dengan Target `Proyek Luar {runId}` dan Overridden `Recipient acceptance (Optional)` tampil di tabel Overrides sebagai baris di luar scope
23. Centang baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)`
24. Centang baris `Proyek Luar {runId}`
25. Klik `Bulk Action` pada toolbar tabel Overrides
26. Klik `Delete`
27. Verifikasi dialog `Delete Overrides` terbuka untuk seleksi guard dan luar scope
28. Verifikasi paragraf `Some overrides are outside your scope and will be skipped:` tampil pada dialog `Delete Overrides` untuk seleksi guard dan luar scope
29. Klik `[Delete]`
30. Verifikasi dialog `Cannot Delete Override` tampil[^drift-1]
31. Verifikasi pesan `At least one assignee type must be enabled` tampil pada dialog `Cannot Delete Override`
32. Verifikasi bullet override `Proyek Guard {runId}` tampil pada dialog `Cannot Delete Override`
33. Verifikasi bullet override `Proyek Luar {runId}` tidak tampil pada dialog `Cannot Delete Override`
34. Verifikasi toast `Success, override has been deleted. Some items were skipped.` tidak tampil
35. Klik `[OK]`
36. Verifikasi dialog `Cannot Delete Override` tertutup
37. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` tetap tampil di tabel Overrides setelah Bulk Delete ditolak
38. Verifikasi baris dengan Target `Proyek Luar {runId}` dan Overridden `Recipient acceptance (Optional)` tetap tampil di tabel Overrides setelah Bulk Delete ditolak
39. Verifikasi baris dengan Target `Proyek Guard {runId}` dan Overridden `Allowed assignee: Division (ON)` masih tercentang
40. Verifikasi baris `Proyek Luar {runId}` masih tercentang

[^drift-1]: Drift PRD vs foundation. PRD §4.1 D-07: title dialog blok bentuk jamak untuk Bulk Delete (`Cannot Delete Overrides`, nama dialog pada langkah 30). foundation `toast-copy.md` §7 Template Title & Body butir 3: bila evaluasi bulk menyisakan satu item yang relevan, dialog «WAJIB sama persis» dengan dialog row-action single (title singular), karena formatnya ditentukan jumlah dan kondisi item di outcome akhir. Diasersi: foundation, karena Bulk Delete ini menyisakan satu baris ditolak guard (`Proyek Guard {runId}`) sehingga dialog memuat satu bullet dan judul singular (SB-4).
