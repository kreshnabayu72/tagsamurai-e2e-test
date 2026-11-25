---
id: TC-FA-DAMAGED-E2E-008-damage-log-dialog
title: "Dialog Damage Log menampilkan header, pihak, badge status, node per peristiwa, dan navigasi Prev/Next dari sub-tab Active dan History"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-11, "§4.1#r4", "§4.2.2#p1", "§8.1#p1", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#r6", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", S-DMG-15, "§9.2#b21", F-DMG-03, "§5#r7", "§8.2#b3", "§4.4#r11", T-DMG-02]
smoke: []
dependsOn: []
trace:
  D-DMG-11: [6, 15, 28]
  "§4.1#r4": [6]
  "§4.2.2#p1": [6, 28, 56, 60]
  "§8.1#p1": [6, 28, 52]
  "§8.1#r1": [6]
  "§8.1#r2": [7]
  "§8.1#r3": [17, 20, 24, 38, 42, 45]
  "§8.1#r4": [9, 20, 34]
  "§8.1#r5": [8, 33, 38, 42, 45]
  "§8.1#r6": [15]
  "§8.1#r7": [10, 21, 34, 35, 39, 46]
  "§8.1#r8": [22, 36]
  "§8.1#r9": [40]
  "§8.1#r10": [14, 18]
  "§8.1#r11": [18]
  "§8.1#r12": [43]
  "§8.1#r13": [11]
  "§8.1#r14": [12]
  "§8.1#r15": [13]
  "§8.1#r16": [47]
  S-DMG-15: [10]
  "§9.2#b21": [6, 33]
  F-DMG-03: [6]
  "§5#r7": [4]
  "§8.2#b3": [49]
  "§4.4#r11": [6]
  T-DMG-02: [33]
anchor: []
coverage:
  web: automated
---

# Dialog Damage Log menampilkan header, pihak, badge status, node per peristiwa, dan navigasi Prev/Next dari sub-tab Active dan History

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-008-1: record `Damaged` berpenanda `Missing`, Name `Log Aset {runId} - 1`, Asset ID `LOG-0001-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Rina W`, What happened `<script>alert(1)</script>`, node: `Reported damaged by Rina W`, `Disposal reported by Rina W`, `Disposal report declined by Agus P`, `Disposal reported by Rina W`, `Disposal report canceled by Rina W`, `Asset reported missing`.
  - DU-008-2: record `Damaged`, Name `Log Aset {runId} - 2`, Asset ID `LOG-0002-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `Budi S`, What happened `' OR '1'='1`, node: `Reported damaged by Budi S`, `Report confirmed by Rina W`.
  - DU-008-3: record `Rejected`, Name `Log Aset {runId} - 3`, Asset ID `LOG-0003-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `Tono R`, Reported By `Sinta M on behalf of Tono R`, What happened `{"$ne": null}`, node: `Reported damaged by Sinta M on behalf of Tono R`, `Report rejected by Rina W`.
  - DU-008-4: record `Canceled`, Name `Log Aset {runId} - 4`, Asset ID `LOG-0004-{runId}`, Group `Head Office {runId}`, Source `Reported by holder`, Last Holder `Dewi A`, Reported By `Dewi A`, What happened `<b>Finance</b>`, node: `Reported damaged by Dewi A`, `Report canceled by Dewi A`.
  - DU-008-5: record `Repaired`, Name `Log Aset {runId} - 5`, Asset ID `LOG-0005-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, What happened `Layar tidak menyala`, node: `Reported damaged by Agus P`, `Marked as repaired by Rina W`.
  - DU-008-6: record `Disposed`, Name `Log Aset {runId} - 6`, Asset ID `LOG-0006-{runId}`, Group `Head Office {runId}`, Source `Registration`, Last Holder `—`, Reported By `Rina W`, What happened `Casing retak saat registrasi`, node: `Reported damaged by Rina W`, `Disposal reported by Rina W`, `Disposed`.
  - DU-008-7: record `Damaged`, Name `Log Aset {runId} - 7`, Asset ID `LOG-0007-{runId}`, Group `Head Office {runId}`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, What happened `Kipas mati total`, node: `Reported damaged by Agus P`, `Asset reported missing`, `Missing report closed`, `Asset reported missing`, `Asset found`.
  - DU-008-8: Reason Disposal `Sudah tidak ekonomis`, Reason Decline `Masih bisa diperbaiki`, Reason Reject `Foto tidak menunjukkan kerusakan`, Repair note `Layar diganti`; Disposal No. milik DU-008-1 dan DU-008-6 dibentuk server.
  - DU-008-1, DU-008-2, dan DU-008-7 adalah record berjalan di sub-tab Active; DU-008-3, DU-008-4, DU-008-5, dan DU-008-6 adalah record selesai di sub-tab History. DU-008-6 tidak memiliki Damaged Photo; record lain memiliki Damaged Photo `foto-kerusakan.jpg`.
  - Reported Date setiap record pukul `09:00` dengan Days Damaged yang berurutan DU-008-1 lebih lama daripada DU-008-7 dan DU-008-2; Resolved Date DU-008-3 terbaru, lalu DU-008-4, DU-008-5, dan DU-008-6.
  - User `Rina W`, `Agus P`, `Budi S`, `Dewi A`, `Sinta M`, dan `Tono R` adalah user ber-runId; `Sinta M` adalah PIC yang melapor atas nama karyawan tanpa akun `Tono R`.

## Test Steps

### Damage Log dibuka dari kolom Name dan memuat node per peristiwa record Active
1. Buka tab `Damaged` pada halaman Assets
2. Klik ikon `Search`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi toolbar sub-tab Active tidak memiliki ikon `Changelog` karena riwayat record ada di Damage Log
5. Klik nama aset `Log Aset {runId} - 1`
6. Verifikasi dialog `Damage Log` terbuka untuk record `Log Aset {runId} - 1`
7. Verifikasi judul dialog tidak memuat nomor transaksi karena Damage record tidak punya nomor
8. Verifikasi badge status `Damaged` disertai penanda `Missing` pada dialog
9. Verifikasi pihak `Reported By` bernilai `Rina W` pada dialog
10. Verifikasi node `Reported damaged by Rina W` memuat What happened `<script>alert(1)</script>` sebagai teks apa adanya dan Damaged Photo `foto-kerusakan.jpg`
11. Verifikasi node `Disposal reported by Rina W` memuat Reason `Sudah tidak ekonomis`
12. Verifikasi node `Disposal report declined by Agus P` memuat Reason `Masih bisa diperbaiki`, dan Back to Damaged
13. Verifikasi node `Disposal report canceled by Rina W` memuat Back to Damaged
14. Verifikasi node `Asset reported missing` dengan pelaku `System` adalah node terbaru (kronologis terakhir) pada record `Log Aset {runId} - 1`
15. Verifikasi dialog `Damage Log` tidak memiliki footer `[Reject]` dan `[Confirm]` karena status record bukan `Waiting for Confirmation`

### Navigasi ke record berikutnya dan sebelumnya mengikuti baris tabel Active
16. Klik tombol navigasi ke record berikutnya pada dialog
17. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 7` yang menjadi baris berikutnya pada tabel
18. Verifikasi node `Asset reported missing` dan `Missing report closed` dengan pelaku `System` serta node `Asset found` tampil pada record `Log Aset {runId} - 7`
19. Klik tombol navigasi ke record berikutnya pada dialog
20. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 2` dengan Holder `Budi S` dan Reported By `Budi S`
21. Verifikasi node `Reported damaged by Budi S` memuat What happened `' OR '1'='1` sebagai teks apa adanya
22. Verifikasi node `Report confirmed by Rina W` tampil sesudah laporan
23. Klik tombol navigasi ke record sebelumnya pada dialog
24. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 7`
25. Tekan `Esc`

### Damage Log dibuka dari aksi baris
26. Buka menu `⋯` pada baris `Log Aset {runId} - 2`
27. Klik `Damage Log`
28. Verifikasi dialog `Damage Log` terbuka untuk record `Log Aset {runId} - 2`
29. Tekan `Esc`

### Damage Log record selesai dari sub-tab History
30. Klik sub-tab `History`
31. Ketik Search `{runId}`, tekan Enter
32. Klik nama aset `Log Aset {runId} - 3`
33. Verifikasi dialog `Damage Log` terbuka untuk record `Log Aset {runId} - 3` dengan badge status `Rejected`
34. Verifikasi pihak `Holder` bernilai `Tono R` dan `Reported By` bernilai `Sinta M on behalf of Tono R`
35. Verifikasi node `Reported damaged by Sinta M on behalf of Tono R` memuat What happened `{"$ne": null}` sebagai teks apa adanya
36. Verifikasi node `Report rejected by Rina W` memuat Reason `Foto tidak menunjukkan kerusakan`
37. Klik tombol navigasi ke record berikutnya pada dialog
38. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 4` dengan badge status `Canceled`
39. Verifikasi node `Reported damaged by Dewi A` memuat What happened `<b>Finance</b>` sebagai teks apa adanya
40. Verifikasi node `Report canceled by Dewi A` tampil
41. Klik tombol navigasi ke record berikutnya pada dialog
42. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 5` dengan badge status `Repaired`
43. Verifikasi node `Marked as repaired by Rina W` memuat Repair note `Layar diganti`
44. Klik tombol navigasi ke record berikutnya pada dialog
45. Verifikasi dialog `Damage Log` menampilkan record `Log Aset {runId} - 6` dengan badge status `Disposed`
46. Verifikasi node `Reported damaged by Rina W` pada record `Log Aset {runId} - 6` memuat What happened `Casing retak saat registrasi` tanpa Damaged Photo
47. Verifikasi node `Disposed` dengan pelaku `System` memuat Disposal No. milik DU-008-6
48. Tekan `Esc`
49. Verifikasi toolbar sub-tab History tidak memiliki ikon `Changelog`

### Damage Log dibuka dari aksi baris sub-tab History
50. Buka menu `⋯` pada baris `Log Aset {runId} - 3`
51. Klik `Damage Log`
52. Verifikasi dialog `Damage Log` terbuka untuk record `Log Aset {runId} - 3` dengan badge status `Rejected`
53. Tekan `Esc`

### Sub-tab mengikuti status record saat Damage Log terbuka
54. Klik sub-tab `Active`
55. Klik nama aset `Log Aset {runId} - 2`
56. Verifikasi sub-tab `Active` aktif ketika dialog `Damage Log` record berjalan `Log Aset {runId} - 2` terbuka
57. Tekan `Esc`
58. Klik sub-tab `History`
59. Klik nama aset `Log Aset {runId} - 3`
60. Verifikasi sub-tab `History` aktif ketika dialog `Damage Log` record selesai `Log Aset {runId} - 3` terbuka
61. Tekan `Esc`
