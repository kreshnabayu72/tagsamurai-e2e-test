---
id: TC-FA-FATR-UI-068-dialog-save
title: "Dialog Save Changes: isi dan tombol"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - §4.1#r8
  - §4.1#r257
  - §4.1#r258
  - §4.1#r260
  - §4.1#r261
  - §4.1#r262
  - §4.1#r263
  - §4.1#r264
  - §4.1#r265
  - §4.4#r8
  - §4.5#b4
  - §9.2#r12
  - §9.2#r13
  - D-01
  - §9.2#b20
  - §9.2#b21
  - §9.2#b22
  - §9.4.2#r12
  - §9.4.2#r13
  - §9.6#r18
  - §9.10.1#r13
  - EB-FB-2@save-changes
  - EB-FRM-1@save-changes
  - §9.2#b38
smoke: []
dependsOn: []
trace:
  §4.1#r8: [3, 4]
  §4.1#r257: 4
  §4.1#r258: [4, 14, 21, 24, 28, 50, 52, 54]
  §4.1#r260: [10, 18, 31, 32]
  §4.1#r261: [25, 26]
  §4.1#r262: [8, 19, 22]
  §4.1#r263: [10, 12, 15]
  §4.1#r264: [17, 18]
  §4.1#r265: [25, 26, 55, 56]
  §4.4#r8: [35, 36]
  §4.5#b4: [40, 42]
  §9.2#r12: 10
  §9.2#r13: 18
  D-01: [2, 3, 5, 6]
  §9.2#b20: 7
  §9.2#b21: 4
  §9.2#b22: [10, 18]
  §9.4.2#r12: 10
  §9.4.2#r13: 18
  §9.6#r18: 48
  §9.10.1#r13: 29
  EB-FB-2@save-changes: 37
  EB-FRM-1@save-changes: [45, 46, 48]
  §9.2#b38: [59, 60, 63, 64, 67, 68]
anchor: [35]
coverage:
  web: automated
---

# Dialog Save Changes: isi dan tombol

## Prerequisites
- Aktor: Total Control.
- Layar awal: Dialog Save Changes terbuka dari tombol `Save` pada Area utama halaman Transaction Settings.
- Komponen: Dialog Save Changes
- Data:
  - DU-068-1: Draft Company default pada All categories: Max duration tab Borrow diubah dari `14` menjadi `10`; Allow Borrow, Allow Assign, Allow Transfer, dan Allow Disposal tetap `Allow`; Require approval Disposal tetap `ON`.
  - DU-068-2: Draft Company default pada All categories: Allow Borrow, Allow Assign, Allow Transfer, dan Allow Disposal diubah menjadi `Deny`; Require approval Disposal tetap `ON`.
  - DU-068-3: Draft Company default pada All categories: Allow Borrow, Allow Assign, dan Allow Disposal diubah menjadi `Deny`; Allow Transfer tersimpan `Allow`.
  - DU-068-4: Draft Company default pada All categories: Allow Borrow, Allow Assign, dan Allow Disposal diubah menjadi `Deny`; Allow Transfer tetap `Allow`.
  - DU-068-5: Draft Company default pada All categories: Require approval Disposal diubah dari `ON` menjadi `OFF`; semua Allow [transaction] tetap `Allow`.
  - DU-068-6: Company default pada All categories tersimpan dengan Require approval Disposal `OFF`; draft hanya mengubah Min asset age warning dari `12` menjadi `6`.
  - DU-068-7: Draft Category leaf `Machinery`: Allow Borrow, Allow Assign, Allow Transfer, dan Allow Disposal `Deny`, Require approval Disposal `OFF`; Company default tidak diubah (semua Allow, Require approval Disposal `ON`).
  - DU-068-8: Draft Company default pada All categories: Transaction timeout Disposal diubah dari `7` menjadi `5`; Require approval Disposal tersimpan `ON` dan kontrolnya tidak dapat diubah.
  - DU-068-9: Draft Company default pada All categories: Allow Borrow, Allow Assign, Allow Transfer, dan Allow Disposal diubah menjadi `Deny`; Require approval Disposal diubah dari `ON` menjadi `OFF`.
  - DU-068-10: Draft Company default pada All categories: Max duration tab Borrow diubah dari `14` menjadi `10`; Company default tidak diubah (semua Allow [transaction] `Allow`, Require approval Disposal `ON`). Override yang sudah ada memberi `Deny` pada semua Allow [transaction] dan `OFF` pada Require approval Disposal.
  - DU-068-11: Draft Category leaf `Machinery`: Max duration tab Borrow berpindah dari Inherit (Company default `14`) ke bernilai sendiri `14`; semua field lain tetap Inherit.
  - DU-068-12: Draft Category leaf `Machinery`: Max duration tab Borrow berpindah dari bernilai sendiri tersimpan `14` ke Inherit (Company default `14`); Max extensions tab Borrow tetap bernilai sendiri tersimpan `2`.
- Kondisi:
  - K1: node All categories terpilih, draft memakai DU-068-1, semua transaksi tersedia di plan.
  - K2: node All categories terpilih, draft memakai DU-068-2, semua transaksi tersedia di plan.
  - K3: node All categories terpilih, draft memakai DU-068-3, level Feature Suite Transfer None dan transaksi lain tersedia.
  - K4: node All categories terpilih, draft memakai DU-068-4, semua transaksi tersedia di plan.
  - K5: node All categories terpilih, draft memakai DU-068-5, semua transaksi tersedia di plan.
  - K6: node All categories terpilih, draft memakai DU-068-6.
  - K7: node Category leaf `Machinery` terpilih, draft memakai DU-068-7.
  - K8: node All categories terpilih, Approval Workflow tidak tersedia di plan, draft memakai DU-068-8.
  - K9: node All categories terpilih, draft memakai DU-068-9, semua transaksi tersedia di plan.
  - K10: sama dengan K1, respons Save ditahan sampai pengujian melepasnya.
  - K11: node All categories terpilih, draft memakai DU-068-10, semua transaksi tersedia di plan.
  - K12: sama dengan K1, server menjawab Save dengan sukses.
  - K13: node Category leaf `Machinery` terpilih, draft memakai DU-068-11, server menjawab Save dengan sukses.
  - K14: node Category leaf `Machinery` terpilih, draft memakai DU-068-12, server menjawab Save dengan sukses.

## Test Steps

### Isi dan tombol dialog
1. Tampilkan Dialog Save Changes dengan kondisi K1
2. Verifikasi judul dialog adalah `Save Changes`
3. Verifikasi dialog bergaya severity warning
4. Verifikasi paragraf pertama `The changes apply to new transactions.` tampil
5. Verifikasi tombol `Save` dan tombol `Cancel` tampil
6. Verifikasi dialog tidak memuat isian alasan
7. Verifikasi jumlah request Save yang terkirim nol selama `Save` di dialog belum diklik
8. Verifikasi dialog hanya memuat paragraf pertama karena draft tidak membuat kondisi paragraf tambahan menjadi benar

### Semua transaksi tersedia di-Deny
9. Tampilkan Dialog Save Changes dengan kondisi K2
10. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tampil

### Transaksi dengan level Feature Suite None tidak dihitung
11. Tampilkan Dialog Save Changes dengan kondisi K3
12. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tampil walau `Allow Transfer` bernilai `Allow`

### Sebagian transaksi masih Allow
13. Tampilkan Dialog Save Changes dengan kondisi K4
14. Verifikasi paragraf `The changes apply to new transactions.` tetap tampil
15. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tidak ada karena `Allow Transfer` masih `Allow`

### Require approval Disposal menjadi OFF
16. Tampilkan Dialog Save Changes dengan kondisi K5
17. Verifikasi peringatan pemisahan tugas tampil karena draft mengubah `Require approval` di tab `Disposal` menjadi `OFF`
18. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tampil
19. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tidak ada karena semua Allow [transaction] tetap `Allow`

### Require approval Disposal sudah OFF dan tidak diubah Save ini
20. Tampilkan Dialog Save Changes dengan kondisi K6
21. Verifikasi paragraf pertama dialog tampil untuk draft `Min asset age warning`
22. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tidak ada karena Save ini tidak mengubah Company default menjadi kondisi tersebut

### Perubahan di node Category tidak memicu paragraf tambahan
23. Tampilkan Dialog Save Changes dengan kondisi K7
24. Verifikasi paragraf pertama dialog tampil untuk draft node Category
25. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tidak ada walau draft Category memberi `Deny` pada semua Allow [transaction]
26. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tidak ada walau draft Category memberi `OFF` pada `Require approval` di tab `Disposal`

### Approval Workflow tidak tersedia di plan
27. Tampilkan Dialog Save Changes dengan kondisi K8
28. Verifikasi paragraf pertama dialog tampil untuk draft `Transaction timeout` di tab `Disposal`
29. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tidak ada karena `Require approval` di tab `Disposal` tidak dapat diubah

### Dua paragraf tambahan sekaligus
30. Tampilkan Dialog Save Changes dengan kondisi K9
31. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tampil bersama paragraf tambahan pemisahan tugas
32. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tampil bersama paragraf tambahan konfirmasi

### Cancel menutup dialog dan mempertahankan draft
33. Tampilkan Dialog Save Changes dengan kondisi K1
34. Klik `Cancel`
35. Verifikasi `Cancel` menutup dialog `Save Changes`
36. Verifikasi `Max duration` pada draft Area utama tetap `10`
37. Verifikasi toast tidak ada setelah Cancel

### Escape menutup dan klik backdrop tidak menutup
38. Tampilkan Dialog Save Changes dengan kondisi K1
39. Klik backdrop di luar dialog
40. Verifikasi dialog `Save Changes` tetap terbuka setelah klik backdrop
41. Tekan Escape
42. Verifikasi dialog `Save Changes` tertutup oleh Escape

### Save masuk keadaan saving
43. Tampilkan Dialog Save Changes dengan kondisi K10
44. Klik `Save`
45. Verifikasi tombol `Save` menampilkan keadaan loading dan disabled selama respons belum diterima
46. Verifikasi tombol `Cancel` disabled selama respons belum diterima
47. Klik `Save` sekali lagi
48. Verifikasi jumlah request Save yang terkirim setelah dua klik adalah satu

### Paragraf pertama tetap tampil bersama paragraf tambahan
49. Tampilkan Dialog Save Changes dengan kondisi K2
50. Verifikasi paragraf pertama `The changes apply to new transactions.` tetap tampil bersama paragraf tambahan
51. Tampilkan Dialog Save Changes dengan kondisi K9
52. Verifikasi paragraf pertama `The changes apply to new transactions.` tetap tampil bersama kedua paragraf tambahan

### Override tidak memicu paragraf tambahan
53. Tampilkan Dialog Save Changes dengan kondisi K11
54. Verifikasi paragraf pertama dialog tampil untuk draft `Max duration` di tab `Borrow`
55. Verifikasi paragraf tambahan `No transactions will be possible for any asset.` tidak ada walau override memberi `Deny` pada semua Allow [transaction]
56. Verifikasi paragraf tambahan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tidak ada walau override memberi `OFF` pada `Require approval` di tab `Disposal`

### Payload Save hanya memuat field yang nilainya berubah
57. Tampilkan Dialog Save Changes dengan kondisi K12
58. Klik `Save` pada dialog `Save Changes`
59. Verifikasi payload Save memuat `Max duration` tab `Borrow` bernilai `10`
60. Verifikasi payload Save tidak memuat `Allow Borrow` yang nilainya tetap `Allow`

### Payload Save memuat field yang berpindah dari Inherit ke nilai sendiri walau angkanya sama
61. Tampilkan Dialog Save Changes dengan kondisi K13
62. Klik `Save` pada dialog `Save Changes`
63. Verifikasi payload Save memuat `Max duration` tab `Borrow` dengan mode nilai sendiri `14`
64. Verifikasi payload Save tidak memuat `Max extensions` yang tetap Inherit

### Payload Save memuat field yang berpindah dari nilai sendiri ke Inherit walau angkanya sama
65. Tampilkan Dialog Save Changes dengan kondisi K14
66. Klik `Save` pada dialog `Save Changes`
67. Verifikasi payload Save memuat `Max duration` tab `Borrow` dengan mode Inherit
68. Verifikasi payload Save tidak memuat `Max extensions` yang tetap bernilai sendiri `2`
