---
id: TC-FA-ASSIGN-UI-121-tabel-tampilan-nilai-kolom
title: "Tabel: nilai kosong, badge, nama user singkat, markup, status, dan format tanggal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-2@tabel-transactions", "EB-TBL-2@tabel-drafts", "EB-TBL-2@tabel-assigned-assets", "EB-TBL-2@tabel-history", "EB-TBL-4@kolom-requested-by-transactions", "EB-TBL-4@kolom-modified-by-drafts", "EB-TBL-8@tabel-transactions", "S-ASG-12", "EB-XM-1"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-2@tabel-transactions": 2
  "EB-TBL-2@tabel-drafts": [4, 5, 6, 7]
  "EB-TBL-2@tabel-assigned-assets": [9, 10, 64, 65, 66]
  "EB-TBL-2@tabel-history": [12, 13, 68, 69, 70, 71, 72, 73, 74, 75]
  "EB-TBL-4@kolom-requested-by-transactions": [15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35]
  "EB-TBL-4@kolom-modified-by-drafts": [37, 39]
  "EB-TBL-8@tabel-transactions": 41
  "S-ASG-12": [43, 44, 45, 46, 48, 49, 50, 52, 53, 55, 56]
  "EB-XM-1": [58, 59, 61, 62, 77, 78, 80, 81, 83, 84, 86, 87, 89, 91, 93, 95]
coverage:
  web: automated
---

# Tabel: nilai kosong, badge, nama user singkat, markup, status, dan format tanggal

## Prerequisites
- Aktor: Aktor Assignment; Approver untuk Approvals > Assignment (K20).
- Layar awal: Transactions > Assignment, tab sesuai kondisi; Approvals > Assignment tab History untuk K20.
- Komponen: Tabel Assignment
- Data:
  - DU-121-1: Assignment Transaction ID `ASG-2026-0101`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Suharti`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-2: Assignment Transaction ID `ASG-2026-0102`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `John Lennon`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-3: Assignment Transaction ID `ASG-2026-0103`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Alexander Graham Bell`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-4: Assignment Transaction ID `ASG-2026-0104`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Buzzlightyear Sumardi`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-5: Assignment Transaction ID `ASG-2026-0105`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Budi`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-6: Assignment Transaction ID `ASG-2026-0106`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Dewi Anggraini`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-7: Assignment Transaction ID `ASG-2026-0107`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Dewi Anggreni`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-8: Draft Assignee kosong, Assignee Type kosong, Group kosong, Total Asset `0`, Origin `New`, Modified By `Rina Wijaya`, Last Updated `2026-11-09 08:01 WIB`.
  - DU-121-9: Draft Assignee `Budi S`, Assignee Type `Employee`, Group `Head Office`, Total Asset `2`, Origin `New`, Modified By `John Lennon`, Last Updated `2026-11-09 08:01 WIB`.
  - DU-121-10: Assigned asset Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Assigned`, Assigned Since `2026-10-12 09:00 WIB`, Transaction ID `ASG-2026-0041`, Assignee `Budi S`.
  - DU-121-11: Assigned asset Photo `printer-hp-m404.jpg`, Name `Printer HP M404 - 2`, Asset ID `PRN-2026-0002`, Brand kosong, Model/Type kosong, Group `Branch Surabaya`, Status `Assigned + Reported Damaged`, Assigned Since `2026-11-06 09:00 WIB`, Transaction ID `ASG-2026-0069`, Assignee `Finance`.
  - DU-121-12: Assigned asset Photo `projector-epson-eb-x49.jpg`, Name `Projector Epson EB-X49 - 3`, Asset ID `PRJ-2026-0003`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Assigned + Reported Missing`, Assigned Since `2026-11-09 09:00 WIB`, Transaction ID `ASG-2026-0067`, Assignee `Sari D`.
  - DU-121-13: History asset Photo `laptop-dell-latitude-5420-62.jpg`, Name `Laptop Dell Latitude 5420 - 62`, Asset ID `LPT-2026-0062`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Canceled`, Handed Over At kosong, Unassigned At kosong, Transaction ID `ASG-2026-0063`, Assignee `Sari D`, Last Updated `2026-11-08 17:12 WIB`.
  - DU-121-14: History asset Photo `laptop-dell-latitude-5420-61.jpg`, Name `Laptop Dell Latitude 5420 - 61`, Asset ID `LPT-2026-0061`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Unassigned + Damaged`, Handed Over At `2026-11-03 09:00 WIB`, Unassigned At `2026-11-08 17:12 WIB`, Transaction ID `ASG-2026-0065`, Assignee `Sari D`, Last Updated `2026-11-08 17:12 WIB`.
  - DU-121-15: History asset Photo `printer-hp-m404-5.jpg`, Name `Printer HP M404 - 5`, Asset ID `PRN-2026-0005`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Unassigned + Missing`, Handed Over At `2026-11-03 09:00 WIB`, Unassigned At `2026-11-08 17:12 WIB`, Transaction ID `ASG-2026-0064`, Assignee `Budi S`, Last Updated `2026-11-08 17:12 WIB`.
  - DU-121-16: Assignment Transaction ID `ASG-2026-0108`, Status `Assigned`, Group `<b>Head Office</b>`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Rina W`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-17: Assignment Transaction ID `ASG-2026-0070`, Status `Waiting for Approval`, Group `Head Office`, Assignee `Sari D`, Assignee Type `Employee`, Total Asset `2`, Requested By `Agus P`, Request Date `2026-11-09 14:00 WIB`, Last Updated `2026-11-09 14:00 WIB`.
  - DU-121-18: Assignment Transaction ID `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-09 20:40 WIB`.
  - DU-121-19: Assignment Transaction ID `ASG-2026-0069`, Status `Assigned`, Group `Branch Surabaya`, Assignee `Finance`, Assignee Type `Division`, Total Asset `4`, Requested By `Agus P`, Request Date `2026-11-05 11:00 WIB`, Last Updated `2026-11-06 09:20 WIB`.
  - DU-121-20: Assignment Transaction ID `ASG-2026-0072`, Status `Waiting for Handover + No PIC`, Group `Branch Surabaya`, Assignee `Field Survey`, Assignee Type `Division`, Total Asset `2`, Requested By `Agus P`, Request Date `2026-11-10 10:15 WIB`, Last Updated `2026-11-11 08:00 WIB`.
  - DU-121-21: History transaction Transaction ID `ASG-2026-0065`, Status `Unassigned`, Group `Head Office`, Assignee `Sari D`, Total Asset `1`, Requested By `Rina W`, Request Date `2026-11-03 09:00 WIB`, Last Updated `2026-11-08 17:12 WIB`.
  - DU-121-22: History transaction Transaction ID `ASG-2026-0066`, Status `Rejected`, Group `Head Office`, Assignee `Budi S`, Total Asset `1`, Requested By `Agus P`, Request Date `2026-10-20 13:40 WIB`, Last Updated `2026-10-21 16:05 WIB`.
  - DU-121-23: History transaction Transaction ID `ASG-2026-0063`, Status `Canceled`, Group `Head Office`, Assignee `Sari D`, Total Asset `1`, Requested By `Agus P`, Request Date `2026-10-14 09:00 WIB`, Last Updated `2026-10-21 09:00 WIB`.
  - DU-121-24: Assignment Transaction ID `ASG-2026-0109`, Status `Assigned`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `2`, Requested By `Rina W`, Request Date `2026-11-09 19:00 WIB`, Last Updated `2026-11-10 08:00 WIB`.
  - DU-121-25: Assigned asset Photo kosong, Name `Monitor LG 24 - 8`, Asset ID `MON-2026-0008`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Assigned`, TAG `Non TAG`, Assigned Since `2026-11-04 09:00 WIB`, Transaction ID `ASG-2026-0073`, Assignee `Sari D`, Purpose kosong.
  - DU-121-26: History asset Photo kosong, Name `Camera Sony A7 - 9`, Asset ID `CAM-2026-0009`, Brand kosong, Model/Type kosong, Group `Head Office`, Status `Unassigned`, TAG `Non TAG`, Handed Over At `2026-11-03 09:00 WIB`, Unassigned At `2026-11-08 17:12 WIB`, Transaction ID `ASG-2026-0065`, Assignee `Sari D`, Reason kosong, Handover Photo kosong, Unassign Photo kosong, Purpose kosong, Last Updated `2026-11-08 17:12 WIB`.
  - DU-121-27: Approval History Transaction ID `ASG-2026-0066`, Status `Rejected`, Group `Head Office`, Assignee `Budi S`, Total Asset `1`, Requested By `Agus P`, Request Date `2026-10-20 13:40 WIB`, Decided Date `2026-10-21 16:05 WIB`.
  - Tampilan nama singkat yang diharapkan di kolom Requested By: `Suharti` dari `Suharti`, `John L` dari `John Lennon`, `Alexander G` dari `Alexander Graham Bell`, `Buzzlightyear S` dari `Buzzlightyear Sumardi`, `Budi` dari `Budi`, dan `Dewi A` dari `Dewi Anggraini` maupun `Dewi Anggreni`.
  - Tampilan tanggal yang diharapkan pada K9: Request Date `09/11/26, 19:00` dari `2026-11-09 19:00 WIB` dan Last Updated `10/11/26, 08:00` dari `2026-11-10 08:00 WIB`. Pada K10: Request Date `09 Nov 26, 19:00` dari `2026-11-09 19:00 WIB` dan Last Updated `10 Nov 26, 08:00` dari `2026-11-10 08:00 WIB`.
  - Tampilan tanggal yang diharapkan pada K13: Request Date `11/9/26, 19:00` dari `2026-11-09 19:00 WIB` dan Last Updated `11/10/26, 08:00` dari `2026-11-10 08:00 WIB`. Pada K14: Request Date `Mon, Nov 09, 26, 19:00` dari `2026-11-09 19:00 WIB` dan Last Updated `Tue, Nov 10, 26, 08:00` dari `2026-11-10 08:00 WIB`. Pada K15: Request Date `Mon, Nov 09, 2026, 19:00` dari `2026-11-09 19:00 WIB` dan Last Updated `Tue, Nov 10, 2026, 08:00` dari `2026-11-10 08:00 WIB`. Pada K16: Request Date `09/11/26, 08:00 PM` dari `2026-11-09 19:00 WIB` yang bergeser satu jam ke WITA, dan Last Updated `10/11/26, 09:00 AM` dari `2026-11-10 08:00 WIB` yang bergeser satu jam ke WITA.
  - Tampilan tanggal yang diharapkan pada K17: Last Updated `09 Nov 26, 08:01` dari `2026-11-09 08:01 WIB`. Pada K18: Assigned Since memuat `12 Oct 26` dari `2026-10-12 09:00 WIB`. Pada K19: Handed Over At memuat `03 Nov 26` dari `2026-11-03 09:00 WIB`. Pada K20: Decided Date memuat `21 Oct 26` dari `2026-10-21 16:05 WIB`.
- Kondisi:
  - K1: daftar Tabel Transactions berisi DU-121-1 sampai DU-121-7.
  - K2: daftar Tabel Transactions berisi DU-121-16.
  - K3: daftar Tabel Transactions berisi DU-121-17 sampai DU-121-20.
  - K4: daftar Tabel Drafts berisi DU-121-8.
  - K5: daftar Tabel Drafts berisi DU-121-9.
  - K6: daftar tabel Assigned Assets By Asset berisi DU-121-10 sampai DU-121-12.
  - K7: daftar tabel History By Asset berisi DU-121-13 sampai DU-121-15.
  - K8: daftar tabel History By Transaction berisi DU-121-21 sampai DU-121-23.
  - K9: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `dd/MM/yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K10: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `dd MMM yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K11: daftar tabel Assigned Assets By Asset berisi DU-121-25, dengan kolom TAG dan Purpose ditampilkan.
  - K12: daftar tabel History By Asset berisi DU-121-26, dengan kolom TAG, Reason, Handover Photo, Unassign Photo, dan Purpose ditampilkan.
  - K13: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `M/d/yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K14: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `DDD, MMM dd, yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K15: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `DDD, MMM dd, yyyy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K16: daftar Tabel Transactions berisi DU-121-24, Date Format bernilai `dd/MM/yy`, Time Format bernilai `12 jam`, dan Time Zone bernilai `WITA`.
  - K17: daftar Tabel Drafts berisi DU-121-9, Date Format bernilai `dd MMM yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K18: daftar tabel Assigned Assets By Asset berisi DU-121-10, Date Format bernilai `dd MMM yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K19: daftar tabel History By Asset berisi DU-121-14, Date Format bernilai `dd MMM yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.
  - K20: daftar tabel Approvals > Assignment tab History berisi DU-121-27, Date Format bernilai `dd MMM yy`, Time Format bernilai `24 jam`, dan Time Zone bernilai `WIB`.

## Test Steps

### Nilai kolom Tabel Transactions selalu terisi
1. Tampilkan Tabel Assignment dengan kondisi K3
2. Verifikasi setiap kolom data pada baris `ASG-2026-0071` terisi

### Sel kosong Tabel Drafts
3. Tampilkan Tabel Assignment dengan kondisi K4
4. Verifikasi sel Assignee menampilkan `No assignee yet`
5. Verifikasi sel Assignee Type menampilkan `—`
6. Verifikasi sel Group menampilkan `—`
7. Verifikasi sel Total Asset menampilkan `0`

### Sel kosong tabel Assigned Assets By Asset
8. Tampilkan Tabel Assignment dengan kondisi K6
9. Verifikasi sel Brand pada baris `Laptop Dell Latitude 5420 - 4` menampilkan `—`
10. Verifikasi sel Model/Type pada baris `Laptop Dell Latitude 5420 - 4` menampilkan `—`

### Sel kosong tabel History By Asset
11. Tampilkan Tabel Assignment dengan kondisi K7
12. Verifikasi sel Handed Over At pada baris `Laptop Dell Latitude 5420 - 62` menampilkan `—`
13. Verifikasi sel Unassigned At pada baris `Laptop Dell Latitude 5420 - 62` menampilkan `—`

### Nama user singkat pada kolom Requested By
14. Tampilkan Tabel Assignment dengan kondisi K1
15. Verifikasi sel Requested By pada baris `ASG-2026-0101` menampilkan `Suharti`
16. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0101`
17. Verifikasi tooltip `Suharti` tampil
18. Verifikasi sel Requested By pada baris `ASG-2026-0102` menampilkan `John L`
19. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0102`
20. Verifikasi tooltip `John Lennon` tampil
21. Verifikasi sel Requested By pada baris `ASG-2026-0103` menampilkan `Alexander G`
22. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0103`
23. Verifikasi tooltip `Alexander Graham Bell` tampil
24. Verifikasi sel Requested By pada baris `ASG-2026-0104` menampilkan `Buzzlightyear S`
25. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0104`
26. Verifikasi tooltip `Buzzlightyear Sumardi` tampil
27. Verifikasi sel Requested By pada baris `ASG-2026-0105` menampilkan `Budi`
28. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0105`
29. Verifikasi tooltip `Budi` tampil
30. Verifikasi sel Requested By pada baris `ASG-2026-0106` menampilkan `Dewi A`
31. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0106`
32. Verifikasi tooltip `Dewi Anggraini` tampil
33. Verifikasi sel Requested By pada baris `ASG-2026-0107` menampilkan `Dewi A`
34. Arahkan kursor ke sel Requested By pada baris `ASG-2026-0107`
35. Verifikasi tooltip `Dewi Anggreni` tampil

### Nama user singkat pada kolom Modified By Tabel Drafts
36. Tampilkan Tabel Assignment dengan kondisi K5
37. Verifikasi sel Modified By menampilkan `John L`
38. Arahkan kursor ke sel Modified By
39. Verifikasi tooltip `John Lennon` tampil

### Markup pada sel tampil apa adanya sebagai teks
40. Tampilkan Tabel Assignment dengan kondisi K2
41. Verifikasi sel Group pada baris `ASG-2026-0108` menampilkan teks `<b>Head Office</b>` apa adanya

### Badge status pada tabel Transactions
42. Tampilkan Tabel Assignment dengan kondisi K3
43. Verifikasi badge `Waiting for Approval` pada baris `ASG-2026-0070` memakai token `warning`
44. Verifikasi badge `Waiting for Handover` pada baris `ASG-2026-0071` memakai token `warning`
45. Verifikasi badge `Assigned` pada baris `ASG-2026-0069` memakai token `primary`
46. Verifikasi badge `No PIC` pada baris `ASG-2026-0072` memakai token `danger`

### Badge status pada tabel History By Transaction
47. Tampilkan Tabel Assignment dengan kondisi K8
48. Verifikasi badge `Unassigned` pada baris `ASG-2026-0065` memakai token `success`
49. Verifikasi badge `Rejected` pada baris `ASG-2026-0066` memakai token `danger`
50. Verifikasi badge `Canceled` pada baris `ASG-2026-0063` memakai token `danger`

### Badge penanda pada tabel History By Asset
51. Tampilkan Tabel Assignment dengan kondisi K7
52. Verifikasi badge `Damaged` pada baris `LPT-2026-0061` memakai token `danger`
53. Verifikasi badge `Missing` pada baris `PRN-2026-0005` memakai token `danger`

### Badge penanda pada tabel Assigned Assets By Asset
54. Tampilkan Tabel Assignment dengan kondisi K6
55. Verifikasi badge `Reported Damaged` pada baris `PRN-2026-0002` memakai token `danger`
56. Verifikasi badge `Reported Missing` pada baris `PRJ-2026-0003` memakai token `danger`

### Format tanggal dan waktu mengikuti General Settings dd/MM/yy
57. Tampilkan Tabel Assignment dengan kondisi K9
58. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `09/11/26, 19:00`
59. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `10/11/26, 08:00`

### Format tanggal dan waktu mengikuti General Settings dd MMM yy
60. Tampilkan Tabel Assignment dengan kondisi K10
61. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `09 Nov 26, 19:00`
62. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `10 Nov 26, 08:00`

### Sel kosong tambahan tabel Assigned Assets By Asset
63. Tampilkan Tabel Assignment dengan kondisi K11
64. Verifikasi sel Photo pada baris `Monitor LG 24 - 8` menampilkan placeholder gambar standar
65. Verifikasi sel TAG pada baris `Monitor LG 24 - 8` menampilkan `—`
66. Verifikasi sel Purpose pada baris `Monitor LG 24 - 8` menampilkan `—`

### Sel kosong tambahan tabel History By Asset
67. Tampilkan Tabel Assignment dengan kondisi K12
68. Verifikasi sel Brand pada baris `Camera Sony A7 - 9` menampilkan `—`
69. Verifikasi sel Model/Type pada baris `Camera Sony A7 - 9` menampilkan `—`
70. Verifikasi sel Photo pada baris `Camera Sony A7 - 9` menampilkan placeholder gambar standar
71. Verifikasi sel TAG pada baris `Camera Sony A7 - 9` menampilkan `—`
72. Verifikasi sel Reason pada baris `Camera Sony A7 - 9` menampilkan `—`
73. Verifikasi sel Handover Photo pada baris `Camera Sony A7 - 9` menampilkan `—`
74. Verifikasi sel Unassign Photo pada baris `Camera Sony A7 - 9` menampilkan `—`
75. Verifikasi sel Purpose pada baris `Camera Sony A7 - 9` menampilkan `—`

### Format tanggal dan waktu mengikuti General Settings M/d/yy
76. Tampilkan Tabel Assignment dengan kondisi K13
77. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `11/9/26, 19:00`
78. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `11/10/26, 08:00`

### Format tanggal dan waktu mengikuti General Settings DDD, MMM dd, yy
79. Tampilkan Tabel Assignment dengan kondisi K14
80. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `Mon, Nov 09, 26, 19:00`
81. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `Tue, Nov 10, 26, 08:00`

### Format tanggal dan waktu mengikuti General Settings DDD, MMM dd, yyyy
82. Tampilkan Tabel Assignment dengan kondisi K15
83. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `Mon, Nov 09, 2026, 19:00`
84. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `Tue, Nov 10, 2026, 08:00`

### Time Format 12 jam dan Time Zone WITA mengikuti General Settings
85. Tampilkan Tabel Assignment dengan kondisi K16
86. Verifikasi sel Request Date pada baris `ASG-2026-0109` menampilkan `09/11/26, 08:00 PM`
87. Verifikasi sel Last Updated pada baris `ASG-2026-0109` menampilkan `10/11/26, 09:00 AM`

### Last Updated Tabel Drafts mengikuti General Settings
88. Tampilkan Tabel Assignment dengan kondisi K17
89. Verifikasi sel Last Updated pada baris `Budi S` menampilkan `09 Nov 26, 08:01`

### Assigned Since mengikuti General Settings
90. Tampilkan Tabel Assignment dengan kondisi K18
91. Verifikasi sel Assigned Since pada baris `Laptop Dell Latitude 5420 - 4` memuat tanggal `12 Oct 26`

### Handed Over At mengikuti General Settings
92. Tampilkan Tabel Assignment dengan kondisi K19
93. Verifikasi sel Handed Over At pada baris `LPT-2026-0061` memuat tanggal `03 Nov 26`

### Decided Date mengikuti General Settings
94. Tampilkan Tabel Assignment dengan kondisi K20
95. Verifikasi sel Decided Date pada baris `ASG-2026-0066` memuat tanggal `21 Oct 26`
