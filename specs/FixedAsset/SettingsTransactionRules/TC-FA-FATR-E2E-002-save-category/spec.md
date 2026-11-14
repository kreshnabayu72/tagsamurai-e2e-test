---
id: TC-FA-FATR-E2E-002-save-category
title: "Save Changes di Category leaf tersimpan dan terbaca ulang"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§Aturan Logika Modul#r4", "§4.1#r220", "§4.4#r7", "§9.2#b54", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r81", "§9.4.2#r83", "§9.6#r12", "§9.6#r13", "EB-FB-3@save-changes", "EB-FRM-1@save-changes", "EB-FRM-9", "§7#r1", "§7#r8", "§8.1#b1", "§8.1#b2", "§9.2#b5", "§9.2#b20", "§9.2#b23", "§9.2#b25", "§9.2#b41", "§9.2#b53", "§9.6#r1", "§9.6#r7", "§9.6#r10", "§9.6#r11", "§9.8#r15", "EB-FB-1@save-changes"]
smoke: ["§7#r1", "§7#r8", "§8.1#b1", "§8.1#b2", "§9.2#b5", "§9.2#b20", "§9.2#b23", "§9.2#b25", "§9.2#b41", "§9.2#b53", "§9.6#r1", "§9.6#r7", "§9.6#r10", "§9.6#r11", "§9.8#r15", "EB-FB-1@save-changes"]
dependsOn: []
trace:
  "§Aturan Logika Modul#r4": [14, 21, 27]
  "§4.1#r220": [48, 54, 55]
  "§4.4#r7": [16, 21]
  "§9.2#b54": 40
  "§9.4.2#r5": [40, 43]
  "§9.4.2#r6": [20, 28, 29]
  "§9.4.2#r81": [21, 24]
  "§9.4.2#r83": 16
  "§9.6#r12": 16
  "§9.6#r13": 40
  "EB-FB-3@save-changes": [33, 43]
  "EB-FRM-1@save-changes": [27, 30, 31]
  "EB-FRM-9": [6, 21, 22, 60, 61, 62, 65]
  "§7#r1": 16
  "§7#r8": 40
  "§8.1#b1": 28
  "§8.1#b2": [40, 43]
  "§9.2#b5": 20
  "§9.2#b20": 14
  "§9.2#b23": 21
  "§9.2#b25": 24
  "§9.2#b41": 40
  "§9.2#b53": 40
  "§9.6#r1": [27, 43]
  "§9.6#r7": 40
  "§9.6#r10": 21
  "§9.6#r11": 21
  "§9.8#r15": 43
  "EB-FB-1@save-changes": 16
coverage:
  web: automated
---

# Save Changes di Category leaf tersimpan dan terbaca ulang

## Prerequisites
- Aktor: Total Control. Aktor lain pemicu perubahan: Total Control, user DU-002-3.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-002-1: Category leaf `Excavator {runId}`, tanpa sub-Category, ada di entitas aktor. Semua field di semua tab transaksi Inherit, dan belum ada entri Changelog untuk Category ini.
  - DU-002-2: Category leaf `Backhoe {runId}`, tanpa sub-Category, ada di entitas aktor. Semua field Inherit, dan belum ada entri Changelog untuk Category ini.
  - DU-002-3: User `Rina Hartono {runId}`, Global Role Manage transaction settings (Read + Update), aktif.
- Kondisi:
  - Company default entitas aktor bernilai bawaan: Max duration `14`, Max extensions `1`, Max assets per assignee (concurrent) `0`.
  - Plan entitas aktor menyediakan semua tab transaksi.

## Test Steps

### Draft tidak valid ditolak dengan pesan di bawah kontrol
1. Ketik Search Sidebar Category Tree `Excavator {runId}`, tekan Enter
2. Klik Category leaf `Excavator {runId}`
3. Klik `[Set own value]` pada field `Max duration`
4. Isi `Max duration` `0`
5. Klik `[Save]`
6. Verifikasi pesan `Value must be at least 1` tampil di bawah field `Max duration`
7. Isi `Max duration` `14`

### Save Changes menyimpan draft dari dua tab setelah dialog konfirmasi
8. Klik `[Set own value]` pada field `Max extensions`
9. Isi `Max extensions` `0`
10. Klik tab `Assign`
11. Klik `[Set own value]` pada field `Max assets per assignee (concurrent)`
12. Isi `Max assets per assignee (concurrent)` `5`
13. Klik `[Save]`
14. Verifikasi dialog `Save Changes` tampil
15. Klik ganda `[Save]` pada dialog Save Changes
16. Verifikasi toast `Success, settings have been saved.` tampil satu kali

### Perubahan bertahan sesudah muat ulang dan field lain tidak berubah
17. Muat ulang halaman
18. Ketik Search Sidebar Category Tree `Excavator {runId}`, tekan Enter
19. Klik Category leaf `Excavator {runId}`
20. Verifikasi field `Max duration` bernilai `14` sebagai nilai sendiri, dengan tombol `[Reset to inherit]` tampil
21. Verifikasi field `Max extensions` bernilai `0`
22. Verifikasi field `Duration unit` menampilkan teks `Inherit — Days (from Company default)`
23. Klik tab `Assign`
24. Verifikasi field `Max assets per assignee (concurrent)` bernilai `5`

### Changelog mencatat satu entri per field yang berubah
25. Klik ikon `Changelog` di header
26. Ketik Search Changelog `Excavator {runId}`, tekan Enter
27. Verifikasi jumlah baris hasil Search adalah `3`
28. Verifikasi Old Value `Inherit` pada baris Field `Borrow (Max duration)`
29. Verifikasi New Value `14 days` pada baris Field `Borrow (Max duration)`
30. Verifikasi New Value `No extension` pada baris Field `Borrow (Max extensions)`
31. Verifikasi baris Field `Assign (Max assets per assignee (concurrent))` tampil
32. Ganti isi kotak search dengan `Backhoe {runId}`, tekan Enter
33. Verifikasi empty state `No results found` tampil karena Category `Backhoe {runId}` tidak mendapat entri Changelog
34. Klik `✕` pada dialog Changelog

### Save tanpa selisih dengan nilai tersimpan diproses sebagai sukses tanpa perubahan
35. Klik tab `Borrow`
36. Rina Hartono {runId} mengubah Max extensions `Excavator {runId}` menjadi `5` dan menyimpannya
37. Isi `Max extensions` `5`
38. Klik `[Save]`
39. Klik `[Save]` pada dialog Save Changes
40. Verifikasi toast `No changes to save.`
41. Klik ikon `Changelog` di header
42. Ketik Search Changelog `Excavator {runId}`, tekan Enter
43. Verifikasi jumlah baris hasil Search adalah `4`, tiga dari Save pertama dan satu dari perubahan Rina Hartono {runId}
44. Klik `✕` pada dialog Changelog

### Reset to Default baru berlaku setelah Save
45. Klik `[Reset to Default]`
46. Klik ikon `Changelog` di header
47. Ketik Search Changelog `Excavator {runId}`, tekan Enter
48. Verifikasi jumlah baris hasil Search tetap `4`
49. Klik `✕` pada dialog Changelog
50. Klik `[Save]`
51. Klik `[Save]` pada dialog Save Changes
52. Klik ikon `Changelog` di header
53. Ketik Search Changelog `Excavator {runId}`, tekan Enter
54. Verifikasi jumlah baris hasil Search adalah `6`
55. Verifikasi New Value `Inherit` pada baris Field `Borrow (Max duration)` yang terbaru
56. Klik `✕` pada dialog Changelog

### Validasi yang gagal tidak menampilkan toast sukses dan tidak mengubah nilai tersimpan
57. Klik `[Set own value]` pada field `Max duration`
58. Isi `Max duration` `0`
59. Klik `[Save]`
60. Verifikasi pesan `Value must be at least 1` tampil di bawah field `Max duration`
61. Verifikasi dialog `Save Changes` tidak tampil
62. Verifikasi toast `Success, settings have been saved.` tidak tampil
63. Klik ikon `Changelog` di header
64. Ketik Search Changelog `Excavator {runId}`, tekan Enter
65. Verifikasi jumlah baris hasil Search tetap `6`
