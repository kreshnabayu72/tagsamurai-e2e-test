---
id: TC-FA-FAREG-UI-007-draft-seleksi-bulk-action
title: "Sub tab Draft: seleksi baris dan Bulk Action bar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#p5", "§4.8#p5", "§5#r5", "EB-BLK-1@tabel-draft", "EB-BLK-4"]
smoke: []
dependsOn: []
trace:
  "§4.1#p5": [2, 37, 71]
  "§4.8#p5": [3, 5]
  "§5#r5": [2, 5]
  EB-BLK-1@tabel-draft: [6, 8, 11, 12, 15, 17, 18, 23, 25, 32, 33, 40, 41, 42, 43, 44, 51]
  EB-BLK-4: [58, 59, 60, 67, 68, 69]
anchor: [10, 31, 50]
coverage:
  web: automated
---

# Sub tab Draft: seleksi baris dan Bulk Action bar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-007-1: 10 batch Draft Group `Gudang Cabang {n}` (n = 1 sampai 10), Origin `—`, Total Asset `3`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-007-2: batch Draft Group `Gudang Utara`, Origin `—`, Total Asset `6`, Progress `10%`, Requested By `Budi Santoso`, Last Updated `2026-11-03T08:00:00Z`.
  - DU-007-3: batch Draft Group `Kantor Selatan`, Origin `—`, Total Asset `9`, Progress `30%`, Requested By `Budi Santoso`, Last Updated `2026-11-02T08:00:00Z`.
  - DU-007-4: batch Draft Group `Gudang Cabang 11`, Origin `—`, Total Asset `3`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-01T08:15:00Z`.
- Kondisi:
  - K1: halaman 1 berisi DU-007-1 dan halaman 2 berisi DU-007-4.
  - K2: daftar berisi DU-007-2 dan DU-007-3; pencarian `Gudang Utara` hanya menghasilkan DU-007-2.
  - K3: sama dengan K2; hapus DU-007-2 berhasil, sehingga daftar sesudahnya hanya berisi DU-007-3.
  - K4: sama dengan K2; hapus gagal karena error server.
  - K5: sama dengan K2; hapus gagal karena timeout.

## Test Steps

### Kolom checkbox, Bulk Action bar, counter, dan tombol clear
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
2. Verifikasi kolom checkbox tampil pada tabel
3. Verifikasi Bulk Action bar tidak tampil
4. Centang baris `Gudang Utara`
5. Verifikasi Bulk Action bar tampil
6. Verifikasi counter `1 Draft selected`
7. Centang baris `Kantor Selatan`
8. Verifikasi counter `2 Drafts selected`
9. Klik `×` pada Bulk Action bar
10. Verifikasi baris `Gudang Utara` tampil kembali setelah tombol clear diklik
11. Verifikasi Bulk Action bar tidak tampil
12. Verifikasi checkbox baris `Gudang Utara` tidak tercentang

### Checkbox header dan status indeterminate
13. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
14. Centang baris `Gudang Cabang 1`
15. Verifikasi checkbox header berstatus indeterminate
16. Centang checkbox header
17. Verifikasi checkbox header berstatus tercentang
18. Verifikasi counter `10 Drafts selected`

### Seleksi bertahan saat pindah halaman
19. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
20. Centang baris `Gudang Cabang 1`
21. Klik halaman `2`
22. Centang baris `Gudang Cabang 11`
23. Verifikasi counter `2 Drafts selected`
24. Klik halaman `1`
25. Verifikasi checkbox baris `Gudang Cabang 1` tercentang

### Seleksi bertahan saat baris tersaring keluar oleh Search
26. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
27. Centang baris `Gudang Utara`
28. Centang baris `Kantor Selatan`
29. Klik ikon Search pada toolbar
30. Ketik Search `Gudang Utara`, tekan Enter
31. Verifikasi baris `Gudang Utara` tampil setelah Search dijalankan
32. Verifikasi baris `Kantor Selatan` tersaring keluar dan tidak tampil
33. Verifikasi counter `2 Drafts selected`

### Cancel pada dialog konfirmasi tidak memproses apa pun
34. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
35. Centang baris `Gudang Utara`
36. Klik `Bulk Action`
37. Verifikasi pilihan `Delete` tampil pada Bulk Action
38. Klik `Delete`
39. Klik `[Cancel]` pada dialog
40. Verifikasi dialog konfirmasi tertutup
41. Verifikasi baris `Gudang Utara` tampil sesudah dialog konfirmasi tertutup
42. Verifikasi toast tidak tampil setelah Cancel pada dialog konfirmasi bulk
43. Verifikasi Bulk Action bar tampil
44. Verifikasi counter `1 Draft selected`

### Seleksi bersih sesudah aksi selesai
45. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
46. Centang baris `Gudang Utara`
47. Klik `Bulk Action`
48. Klik `Delete`
49. Klik `[Delete]` pada dialog
50. Verifikasi baris `Kantor Selatan` tampil
51. Verifikasi Bulk Action bar tidak tampil

### Bulk gagal karena error server mempertahankan bar dan seleksi
52. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K4
53. Centang baris `Gudang Utara`
54. Centang baris `Kantor Selatan`
55. Klik `Bulk Action`
56. Klik `Delete`
57. Klik `[Delete]` pada dialog
58. Verifikasi toast `Error, failed to delete draft.`
59. Verifikasi Bulk Action bar tetap tampil
60. Verifikasi counter `2 Drafts selected`

### Bulk gagal karena timeout mempertahankan bar dan seleksi
61. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K5
62. Centang baris `Gudang Utara`
63. Centang baris `Kantor Selatan`
64. Klik `Bulk Action`
65. Klik `Delete`
66. Klik `[Delete]` pada dialog
67. Verifikasi toast `Connection problem. Please try again.`
68. Verifikasi Bulk Action bar tetap tampil
69. Verifikasi counter `2 Drafts selected`

### Kolom checkbox menjadi kolom pertama tabel
70. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
71. Verifikasi kolom checkbox adalah kolom pertama pada tabel, sebelum kolom `Group`
