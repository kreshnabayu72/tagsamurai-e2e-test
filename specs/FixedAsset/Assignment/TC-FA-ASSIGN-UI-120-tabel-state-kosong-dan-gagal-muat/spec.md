---
id: TC-FA-ASSIGN-UI-120-tabel-state-kosong-dan-gagal-muat
title: "Tabel: state kosong, kosong tersaring, loading, dan gagal muat"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-ASG-15", "S-ASG-16", "S-ASG-17", "S-ASG-18", "S-ASG-19", "S-ASG-20", "S-ASG-21", "S-ASG-26", "S-ASG-27", "EB-TBL-1@tabel-transactions", "EB-TBL-1@tabel-drafts", "EB-TBL-1@tabel-assigned-assets", "EB-TBL-1@tabel-history", "EB-TBL-1@approvals-active", "EB-TBL-1@approvals-history"]
smoke: []
dependsOn: []
trace:
  "S-ASG-15": [2, 3, 25, 26]
  "S-ASG-16": [5, 6, 30, 31]
  "S-ASG-17": [8, 9, 35, 36]
  "S-ASG-18": [11, 12, 40, 41]
  "S-ASG-19": [14, 15, 45, 46]
  "S-ASG-20": [17, 18, 50, 51]
  "S-ASG-21": [20, 21, 55, 56]
  "S-ASG-26": 58
  "S-ASG-27": [60, 61, 64, 65, 68, 69, 72, 73, 76, 77, 80, 81, 84, 85]
  "EB-TBL-1@tabel-transactions": [2, 3, 25, 26, 60, 61, 62]
  "EB-TBL-1@tabel-drafts": [14, 15, 45, 46, 72, 73, 74]
  "EB-TBL-1@tabel-assigned-assets": [5, 6, 30, 31, 64, 65, 66, 84, 85, 86]
  "EB-TBL-1@tabel-history": [11, 12, 40, 41, 68, 69, 70]
  "EB-TBL-1@approvals-active": [17, 18, 50, 51, 76, 77, 78]
  "EB-TBL-1@approvals-history": [20, 21, 55, 56, 80, 81, 82]
coverage:
  web: automated
---

# Tabel: state kosong, kosong tersaring, loading, dan gagal muat

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk Approvals > Assignment (K6, K7, K13, K14, K20, K21).
- Layar awal: Transactions > Assignment, tab sesuai kondisi; Approvals > Assignment tab Active atau History untuk K6, K7, K13, K14, K20, K21.
- Komponen: Tabel Assignment
- Data:
  - DU-120-1: Assignment `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `09 Nov 2026, 19:00`, Last Updated `09 Nov 2026, 20:40`.
  - DU-120-2: Assigned asset Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Assigned`, Assigned Since `12 Oct 2026`, Transaction ID `ASG-2026-0041`, Assignee `Budi S`.
  - DU-120-3: Assigned asset milik satu Assignee Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Assigned`, Assigned Since `12 Oct 2026`, Transaction ID `ASG-2026-0041`.
  - DU-120-4: History Transaction ID `ASG-2026-0065`, Status `Unassigned`, Group `Head Office`, Assignee `Sari D`, Total Asset `1`, Requested By `Rina W`, Request Date `03 Nov 2026, 09:00`, Last Updated `08 Nov 2026, 17:12`.
  - DU-120-5: Draft Assignee `Budi S`, Assignee Type `Employee`, Group `Head Office`, Total Asset `2`, Origin `New`, Modified By `Rina W`, Last Updated `09 Nov 2026, 08:01`.
  - DU-120-6: Approval Active Transaction ID `ASG-2026-0070`, Group `Head Office`, Assignee `Sari D`, Total Asset `2`, Requested By `Agus P`, Request Date `09 Nov 2026, 14:00`.
  - DU-120-7: Approval History Transaction ID `ASG-2026-0066`, Status `Rejected`, Group `Head Office`, Assignee `Budi S`, Total Asset `1`, Requested By `Agus P`, Request Date `20 Oct 2026, 13:40`, Decided Date `21 Oct 2026, 16:05`.
  - DU-120-8: kata kunci Search yang tidak cocok dengan baris mana pun `Kalimantan`.
- Kondisi:
  - K1: daftar Transactions kosong.
  - K2: daftar Assigned Assets kosong.
  - K3: daftar halaman Assigned Asset kosong.
  - K4: daftar History kosong.
  - K5: daftar Drafts kosong.
  - K6: daftar Approvals > Assignment tab Active kosong.
  - K7: daftar Approvals > Assignment tab History kosong.
  - K8: daftar Transactions berisi DU-120-1.
  - K9: daftar Assigned Assets berisi DU-120-2.
  - K10: daftar halaman Assigned Asset berisi DU-120-3.
  - K11: daftar History berisi DU-120-4.
  - K12: daftar Drafts berisi DU-120-5.
  - K13: daftar Approvals > Assignment tab Active berisi DU-120-6.
  - K14: daftar Approvals > Assignment tab History berisi DU-120-7.
  - K15: daftar Transactions sedang dimuat dan belum dijawab.
  - K16: memuat daftar Transactions gagal karena error server.
  - K17: memuat daftar Assigned Assets gagal karena error server.
  - K18: memuat daftar History gagal karena error server.
  - K19: memuat daftar Drafts gagal karena error server.
  - K20: memuat daftar Approvals > Assignment tab Active gagal karena error server.
  - K21: memuat daftar Approvals > Assignment tab History gagal karena error server.
  - K22: memuat daftar halaman Assigned Asset gagal karena error server.

## Test Steps

### Kosong alami Transactions
1. Tampilkan Tabel Assignment dengan kondisi K1
2. Verifikasi judul `No assignments yet` tampil
3. Verifikasi deskripsi `Assignments in progress will appear here.` tampil

### Kosong alami Assigned Assets
4. Tampilkan Tabel Assignment dengan kondisi K2
5. Verifikasi judul `No assets are assigned right now` tampil
6. Verifikasi deskripsi `Assigned assets will appear here after handover.` tampil

### Kosong alami halaman Assigned Asset
7. Tampilkan Tabel Assignment dengan kondisi K3
8. Verifikasi judul `No assigned assets` tampil
9. Verifikasi deskripsi `This assignee doesn't hold any assets.` tampil

### Kosong alami History
10. Tampilkan Tabel Assignment dengan kondisi K4
11. Verifikasi judul `No finished assignments yet` tampil
12. Verifikasi deskripsi `Unassigned, rejected, and canceled assignments will appear here.` tampil

### Kosong alami Drafts
13. Tampilkan Tabel Assignment dengan kondisi K5
14. Verifikasi judul `No drafts` tampil
15. Verifikasi deskripsi `Saved drafts from you and your team will appear here.` tampil

### Kosong alami Approvals > Assignment tab Active
16. Tampilkan Tabel Assignment dengan kondisi K6
17. Verifikasi judul `No pending approvals` tampil
18. Verifikasi deskripsi `You have no pending approval requests at this moment.` tampil

### Kosong alami Approvals > Assignment tab History
19. Tampilkan Tabel Assignment dengan kondisi K7
20. Verifikasi judul `No history yet` tampil
21. Verifikasi deskripsi `Decided assignments will appear here.` tampil

### Kosong akibat Search Transactions
22. Tampilkan Tabel Assignment dengan kondisi K8
23. Klik ikon Search
24. Ketik Search `Kalimantan`, tekan Enter
25. Verifikasi judul `No results found` tampil
26. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search Assigned Assets
27. Tampilkan Tabel Assignment dengan kondisi K9
28. Klik ikon Search
29. Ketik Search `Kalimantan`, tekan Enter
30. Verifikasi judul `No results found` tampil
31. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search halaman Assigned Asset
32. Tampilkan Tabel Assignment dengan kondisi K10
33. Klik ikon Search
34. Ketik Search `Kalimantan`, tekan Enter
35. Verifikasi judul `No results found` tampil
36. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search History
37. Tampilkan Tabel Assignment dengan kondisi K11
38. Klik ikon Search
39. Ketik Search `Kalimantan`, tekan Enter
40. Verifikasi judul `No results found` tampil
41. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search Drafts
42. Tampilkan Tabel Assignment dengan kondisi K12
43. Klik ikon Search
44. Ketik Search `Kalimantan`, tekan Enter
45. Verifikasi judul `No results found` tampil
46. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search Approvals > Assignment tab Active
47. Tampilkan Tabel Assignment dengan kondisi K13
48. Klik ikon Search
49. Ketik Search `Kalimantan`, tekan Enter
50. Verifikasi judul `No results found` tampil
51. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Kosong akibat Search Approvals > Assignment tab History
52. Tampilkan Tabel Assignment dengan kondisi K14
53. Klik ikon Search
54. Ketik Search `Kalimantan`, tekan Enter
55. Verifikasi judul `No results found` tampil
56. Verifikasi deskripsi `Try adjusting your search or filter.` tampil

### Loading memakai Shimmer
57. Tampilkan Tabel Assignment dengan kondisi K15
58. Verifikasi area tabel ditandai sedang dimuat dengan Shimmer (`aria-busy`)

### Gagal muat Transactions
59. Tampilkan Tabel Assignment dengan kondisi K16
60. Verifikasi pesan `Unable to load this data.` tampil
61. Verifikasi tombol `[Try Again]` tampil
62. Verifikasi judul `No assignments yet` tidak tampil

### Gagal muat Assigned Assets
63. Tampilkan Tabel Assignment dengan kondisi K17
64. Verifikasi pesan `Unable to load this data.` tampil
65. Verifikasi tombol `[Try Again]` tampil
66. Verifikasi judul `No assets are assigned right now` tidak tampil

### Gagal muat History
67. Tampilkan Tabel Assignment dengan kondisi K18
68. Verifikasi pesan `Unable to load this data.` tampil
69. Verifikasi tombol `[Try Again]` tampil
70. Verifikasi judul `No finished assignments yet` tidak tampil

### Gagal muat Drafts
71. Tampilkan Tabel Assignment dengan kondisi K19
72. Verifikasi pesan `Unable to load this data.` tampil
73. Verifikasi tombol `[Try Again]` tampil
74. Verifikasi judul `No drafts` tidak tampil

### Gagal muat Approvals > Assignment tab Active
75. Tampilkan Tabel Assignment dengan kondisi K20
76. Verifikasi pesan `Unable to load this data.` tampil
77. Verifikasi tombol `[Try Again]` tampil
78. Verifikasi judul `No pending approvals` tidak tampil

### Gagal muat Approvals > Assignment tab History
79. Tampilkan Tabel Assignment dengan kondisi K21
80. Verifikasi pesan `Unable to load this data.` tampil
81. Verifikasi tombol `[Try Again]` tampil
82. Verifikasi judul `No history yet` tidak tampil

### Gagal muat halaman Assigned Asset
83. Tampilkan Tabel Assignment dengan kondisi K22
84. Verifikasi pesan `Unable to load this data.` tampil
85. Verifikasi tombol `[Try Again]` tampil
86. Verifikasi judul `No assigned assets` tidak tampil
