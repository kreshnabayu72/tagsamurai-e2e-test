---
id: TC-FA-ASSIGN-UI-123-guided-tooltip-halaman-assignment
title: "Guided Tooltip halaman Assignment dan Review"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4", "§4.7#r5", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [3, 4, 80]
  "§4.7#r2": [8, 9, 82]
  "§4.7#r3": [12, 13, 84]
  "§4.7#r4": [16, 17, 86]
  "§4.7#r5": [51, 52, 88]
  "EB-TBL-10": [2, 5, 7, 11, 15, 18, 22, 24, 30, 33, 36, 39, 42, 44, 48, 50, 53, 54, 59, 67, 73, 78, 80, 82, 84, 86, 88]
anchor: [41, 58, 66, 72]
coverage:
  web: automated
---

# Guided Tooltip halaman Assignment dan Review

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk K3 (halaman Review).
- Layar awal: Transactions > Assignment, tab Transactions; Approvals > Assignment > Active > Review untuk K3.
- Komponen: Guided Tooltip
- Kondisi:
  - K1: halaman Assignment dibuka akun ini untuk pertama kali, flag `guided_tooltip_seen_fams-assignment` belum ada.
  - K2: halaman Assignment dibuka akun yang flag `guided_tooltip_seen_fams-assignment` sudah ada.
  - K3: halaman Review dibuka akun ini untuk pertama kali, flag `guided_tooltip_seen_fams-assignment-approval` belum ada.
  - K4: halaman Assignment dibuka lagi oleh akun yang sama sesudah kunjungan pertamanya diakhiri dengan `[Skip]`.
  - K5: halaman Assignment dibuka lagi oleh akun yang sama sesudah kunjungan pertamanya diakhiri dengan `[Done]`.
  - K6: halaman Assignment dibuka lagi oleh akun yang sama sesudah kunjungan yang flag-nya sudah ada diputar ulang lewat `[?]` dan diakhiri dengan `[Skip]`.
  - K7: halaman Assignment dibuka lagi oleh akun yang sama sesudah kunjungan pertamanya diakhiri dengan perubahan ukuran jendela browser.

## Test Steps

### Walkthrough muncul otomatis di kunjungan pertama dan memuat konten tiap step
1. Tampilkan Guided Tooltip dengan kondisi K1
2. Verifikasi indikator `Step 1 of 4` tampil
3. Verifikasi judul `Find an assignment` tampil
4. Verifikasi deskripsi `Search or filter the list to find a specific assignment. Other actions here depend on your role.` tampil
5. Verifikasi tombol `[Back]` tidak tampil pada Step 1
6. Klik `[Next]`
7. Verifikasi indikator `Step 2 of 4` tampil
8. Verifikasi judul `Move between stages` tampil
9. Verifikasi deskripsi `Each tab shows one stage of an assignment. The tabs you see depend on your role and plan.` tampil
10. Klik `[Next]`
11. Verifikasi indikator `Step 3 of 4` tampil
12. Verifikasi judul `See who holds what` tampil
13. Verifikasi deskripsi `See which assets are held and by whom. Other actions here depend on your role.` tampil
14. Klik `[Next]`
15. Verifikasi indikator `Step 4 of 4` tampil
16. Verifikasi judul `One assignment, many assets` tampil
17. Verifikasi deskripsi `Each asset has its own status; the badge summarizes them.` tampil
18. Verifikasi tombol `[Done]` tampil pada Step 4

### Back dan Next berpindah step
19. Tampilkan Guided Tooltip dengan kondisi K1
20. Klik `[Next]`
21. Klik `[Next]`
22. Verifikasi indikator `Step 3 of 4` tampil sesudah dua kali `[Next]`
23. Klik `[Back]`
24. Verifikasi indikator `Step 2 of 4` tampil sesudah `[Back]`

### Done menutup walkthrough
25. Tampilkan Guided Tooltip dengan kondisi K1
26. Klik `[Next]`
27. Klik `[Next]`
28. Klik `[Next]`
29. Klik `[Done]`
30. Verifikasi walkthrough tertutup

### Skip menutup walkthrough
31. Tampilkan Guided Tooltip dengan kondisi K1
32. Klik `[Skip]`
33. Verifikasi walkthrough tertutup sesudah `[Skip]`

### Klik overlay menutup walkthrough seperti Skip
34. Tampilkan Guided Tooltip dengan kondisi K1
35. Klik overlay di luar spotlight
36. Verifikasi walkthrough tertutup sesudah klik overlay

### Esc menutup walkthrough seperti Skip
37. Tampilkan Guided Tooltip dengan kondisi K1
38. Tekan Esc
39. Verifikasi walkthrough tertutup sesudah `Esc`

### Walkthrough tidak muncul lagi bila flag sudah ada, dan `[?]` memutar ulang dari Step 1
40. Tampilkan Guided Tooltip dengan kondisi K2
41. Verifikasi halaman Assignment menampilkan tab `Transactions`
42. Verifikasi walkthrough tidak tampil otomatis
43. Klik `[?]` di sebelah kanan Breadcrumb
44. Verifikasi indikator `Step 1 of 4` tampil sesudah `[?]`

### Mengubah ukuran jendela menutup walkthrough
45. Tampilkan Guided Tooltip dengan kondisi K1
46. Klik `[Next]`
47. Ubah ukuran jendela browser
48. Verifikasi walkthrough tertutup sesudah ukuran jendela berubah

### Walkthrough halaman Review
49. Tampilkan Guided Tooltip dengan kondisi K3
50. Verifikasi indikator `Step 1 of 1` tampil
51. Verifikasi judul `See who decided` tampil
52. Verifikasi deskripsi `Any one approver, all approvers, or a single approver, as set for each asset. Select a progress cell to see who has decided.` tampil
53. Verifikasi tombol `[Done]` tampil pada Step 1 of 1
54. Verifikasi tombol `[Next]` tidak tampil pada Step 1 of 1

### Skip menyetel flag sehingga kunjungan berikutnya tidak memunculkan walkthrough
55. Tampilkan Guided Tooltip dengan kondisi K1
56. Klik `[Skip]`
57. Tampilkan Guided Tooltip dengan kondisi K4
58. Verifikasi halaman Assignment menampilkan tab `Transactions`
59. Verifikasi walkthrough tidak tampil otomatis

### Done menyetel flag sehingga kunjungan berikutnya tidak memunculkan walkthrough
60. Tampilkan Guided Tooltip dengan kondisi K1
61. Klik `[Next]`
62. Klik `[Next]`
63. Klik `[Next]`
64. Klik `[Done]`
65. Tampilkan Guided Tooltip dengan kondisi K5
66. Verifikasi halaman Assignment menampilkan tab `Transactions`
67. Verifikasi walkthrough tidak tampil otomatis

### Replay lewat `[?]` tidak mereset flag
68. Tampilkan Guided Tooltip dengan kondisi K2
69. Klik `[?]` di sebelah kanan Breadcrumb
70. Klik `[Skip]`
71. Tampilkan Guided Tooltip dengan kondisi K6
72. Verifikasi halaman Assignment menampilkan tab `Transactions`
73. Verifikasi walkthrough tidak tampil otomatis

### Keluar karena ukuran jendela berubah tidak menyetel flag
74. Tampilkan Guided Tooltip dengan kondisi K1
75. Klik `[Next]`
76. Ubah ukuran jendela browser
77. Tampilkan Guided Tooltip dengan kondisi K7
78. Verifikasi indikator `Step 1 of 4` tampil

### Spotlight menyorot elemen target tiap step
79. Tampilkan Guided Tooltip dengan kondisi K1
80. Verifikasi spotlight Step 1 menyorot toolbar tabel (Search dan Filter)
81. Klik `[Next]`
82. Verifikasi spotlight Step 2 menyorot tabs navigasi
83. Klik `[Next]`
84. Verifikasi spotlight Step 3 menyorot tab `Assigned Assets`
85. Klik `[Next]`
86. Verifikasi spotlight Step 4 menyorot header kolom `Status`
87. Tampilkan Guided Tooltip dengan kondisi K3
88. Verifikasi spotlight Step 1 menyorot kolom `Approval Rule`
