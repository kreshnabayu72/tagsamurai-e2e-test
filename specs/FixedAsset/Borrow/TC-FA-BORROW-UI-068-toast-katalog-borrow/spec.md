---
id: TC-FA-BORROW-UI-068-toast-katalog-borrow
title: "Katalog toast Borrow: copy sukses, gagal server, gangguan jaringan, dan toast netral"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-BRW-01", "T-BRW-02", "T-BRW-03", "T-BRW-04", "T-BRW-05", "T-BRW-06", "T-BRW-07", "T-BRW-08", "T-BRW-09", "T-BRW-10", "T-BRW-11", "T-BRW-17", "T-BRW-18", "T-BRW-21", "T-BRW-22", "T-BRW-24", "T-BRW-25", "T-BRW-26", "T-BRW-27", "T-BRW-28", "T-BRW-29", "T-BRW-30", "T-BRW-31", "T-BRW-32", "EB-FB-4"]
smoke: []
dependsOn: []
trace:
  "T-BRW-01": 2
  "T-BRW-02": [4, 6, 8, 9, 11]
  "T-BRW-03": [13, 15]
  "T-BRW-04": [17, 19]
  "T-BRW-05": 21
  "T-BRW-06": [23, 25, 27]
  "T-BRW-07": [29, 31]
  "T-BRW-08": [33, 35]
  "T-BRW-09": [37, 39]
  "T-BRW-10": [41, 43]
  "T-BRW-11": [45, 47, 49]
  "T-BRW-17": 51
  "T-BRW-18": 53
  "T-BRW-21": [55, 57]
  "T-BRW-22": 59
  "T-BRW-24": [115]
  "T-BRW-25": 61
  "T-BRW-26": [63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 113]
  "T-BRW-27": 87
  "T-BRW-28": 89
  "T-BRW-29": 91
  "T-BRW-30": 93
  "T-BRW-31": [95, 97]
  "T-BRW-32": [99, 101]
  "EB-FB-4": [105, 109, 111]
anchor: [103, 107]
coverage:
  web: automated
---

# Katalog toast Borrow: copy sukses, gagal server, gangguan jaringan, dan toast netral

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman yang memicu aksi tulis Borrow
- Komponen: Toast Borrow
- Data:
  - DU-068-1: Borrower `Budi Santoso`.
  - DU-068-2: BRW `BRW-2026-0153`, toast yang diharapkan saat BRW itu langsung Waiting for Handover `Success, borrow BRW-2026-0153 is ready for handover.`.
  - DU-068-3: Due date baru hasil Extend `12/12/2026`.
  - DU-068-4: batas pengembalian hasil Borrow Now `20/12/2026`.
- Kondisi:
  - K1: Save Draft berhasil disimpan.
  - K2: satu aset ditambahkan ke Borrow Draft, tidak ada yang dilewati.
  - K3: tiga aset ditambahkan ke Borrow Draft, tidak ada yang dilewati.
  - K4: dua aset ditambahkan ke Borrow Draft dan satu aset sudah ada di dalamnya.
  - K5: satu aset ditambahkan ke Borrow Draft dan dua aset sudah ada di dalamnya.
  - K6: Submit satu BRW DU-068-2 berhasil dan semua aset langsung Waiting for Handover.
  - K7: Submit dua BRW berhasil dan semua aset langsung Waiting for Handover.
  - K8: Submit satu BRW berhasil dan semua aset menunggu approval.
  - K9: Submit dua BRW berhasil dan semua aset menunggu approval.
  - K10: Submit berhasil menghasilkan dua BRW dengan total 3 aset, dengan hasil campuran: 1 dari 3 aset disetujui langsung dan 2 menunggu approval.
  - K11: keputusan approval berhasil dengan semua aset diputuskan Approve.
  - K12: keputusan approval berhasil dengan semua aset yang diputuskan ditolak.
  - K13: keputusan approval berhasil dan pengajuan masih menunggu approver lain.
  - K14: Handover satu aset selesai.
  - K15: Handover tiga aset selesai.
  - K16: Return satu aset selesai.
  - K17: Return tiga aset selesai.
  - K18: Extend berlaku langsung dengan satu Due date baru DU-068-3, Date Format bernilai `DD/MM/YYYY`.
  - K19: Extend berlaku langsung dengan Due date baru yang berbeda untuk tiga aset.
  - K20: Extend diajukan untuk satu BRW.
  - K21: Extend diajukan untuk dua BRW.
  - K22: Cancel Borrow berhasil.
  - K23: Delete Draft berhasil.
  - K24: Bulk Delete Draft berhasil untuk sebagian Draft dan sebagian dilewati karena di luar cakupan Group.
  - K25: Transaction ID DU-068-2 disalin.
  - K26: Cancel Extension Request berhasil.
  - K27: Borrow Now berhasil untuk satu aset, Date Format bernilai `DD/MM/YYYY`, batas pengembalian DU-068-4.
  - K28: Borrow Now berhasil untuk tiga aset, Date Format bernilai `DD/MM/YYYY`, batas pengembalian DU-068-4.
  - K29: Cancel Borrow dengan Save as Draft to edit berhasil.
  - K30: Review Extension Request berhasil.
  - K31: aksi save gagal karena error server.
  - K32: aksi add gagal karena error server.
  - K33: aksi submit gagal karena error server.
  - K34: aksi approve gagal karena error server.
  - K35: aksi reject gagal karena error server.
  - K36: aksi hand over gagal karena error server.
  - K37: aksi return gagal karena error server.
  - K38: aksi extend gagal karena error server.
  - K39: aksi cancel gagal karena error server.
  - K40: aksi delete gagal karena error server.
  - K41: aksi remove gagal karena error server.
  - K42: aksi review gagal karena error server.
  - K43: aksi tulis tidak mendapat respons karena koneksi putus.
  - K44: Submit form Edit tanpa perubahan nilai.
  - K45: Report Damaged berhasil dikirim.
  - K46: Remind Borrower berhasil untuk Borrower DU-068-1.
  - K47: Submit Extend oleh Aktor Borrow berhasil: 1 dari 2 aset langsung berlaku dan 1 menunggu approval.
  - K48: Submit Extend dari My Asset berhasil: 1 dari 2 aset langsung berlaku dan 1 menunggu review.
  - K49: Mark as Returned satu aset selesai.
  - K50: Mark as Returned tiga aset selesai.
  - K51: Cancel Borrow berhasil.
  - K52: aksi cancel gagal karena error server.
  - K54: aksi remind Borrower gagal karena error server.
  - K56: Submit Extend dari My Asset berhasil dan seluruh aset menunggu review.

## Test Steps

### Save Draft berhasil
1. Tampilkan Toast Borrow dengan kondisi K1
2. Verifikasi toast `Success, borrow has been saved as draft.` tampil sesuai katalog toast

### Add to Borrow Draft untuk satu aset
3. Tampilkan Toast Borrow dengan kondisi K2
4. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil sesuai katalog toast

### Add to Borrow Draft untuk beberapa aset
5. Tampilkan Toast Borrow dengan kondisi K3
6. Verifikasi toast `Success, 3 assets have been added to the draft.` tampil sesuai katalog toast

### Add to Borrow Draft dengan satu aset dilewati
7. Tampilkan Toast Borrow dengan kondisi K4
8. Verifikasi toast `Success, 2 assets have been added to the draft.` tampil sesuai katalog toast
9. Verifikasi pesan `1 was already in it.` tampil bersama toast Add to Borrow Draft

### Add to Borrow Draft dengan beberapa aset dilewati
10. Tampilkan Toast Borrow dengan kondisi K5
11. Verifikasi pesan `2 were already in it.` tampil bersama toast Add to Borrow Draft

### Submit BRW tunggal langsung Waiting for Handover
12. Tampilkan Toast Borrow dengan kondisi K6
13. Verifikasi toast `Success, borrow BRW-2026-0153 is ready for handover.` tampil sesuai katalog toast

### Submit beberapa BRW langsung Waiting for Handover
14. Tampilkan Toast Borrow dengan kondisi K7
15. Verifikasi toast `Success, 2 borrows are ready for handover.` tampil sesuai katalog toast

### Submit BRW tunggal menunggu approval
16. Tampilkan Toast Borrow dengan kondisi K8
17. Verifikasi toast `Success, borrow has been submitted for approval.` tampil sesuai katalog toast

### Submit beberapa BRW menunggu approval
18. Tampilkan Toast Borrow dengan kondisi K9
19. Verifikasi toast `Success, 2 borrows have been submitted for approval.` tampil sesuai katalog toast

### Submit campuran lintas BRW
20. Tampilkan Toast Borrow dengan kondisi K10
21. Verifikasi toast `Success, 1 of 3 assets have been approved. 2 submitted for approval.` tampil sesuai katalog toast, dengan hitungan gabungan seluruh aset dari kedua BRW

### Keputusan approval Approve
22. Tampilkan Toast Borrow dengan kondisi K11
23. Verifikasi toast `Success, borrow has been approved.` tampil sesuai katalog toast

### Keputusan approval Reject
24. Tampilkan Toast Borrow dengan kondisi K12
25. Verifikasi toast `Success, borrow has been rejected.` tampil sesuai katalog toast

### Keputusan approval masih menunggu approver lain
26. Tampilkan Toast Borrow dengan kondisi K13
27. Verifikasi toast `Success, your approval has been recorded. Waiting for the other approvers.` tampil sesuai katalog toast

### Handover selesai untuk satu aset
28. Tampilkan Toast Borrow dengan kondisi K14
29. Verifikasi toast `Success, 1 asset has been handed over.` tampil sesuai katalog toast

### Handover selesai untuk beberapa aset
30. Tampilkan Toast Borrow dengan kondisi K15
31. Verifikasi toast `Success, 3 assets have been handed over.` tampil sesuai katalog toast

### Return selesai untuk satu aset
32. Tampilkan Toast Borrow dengan kondisi K16
33. Verifikasi toast `Success, 1 asset has been returned.` tampil sesuai katalog toast

### Return selesai untuk beberapa aset
34. Tampilkan Toast Borrow dengan kondisi K17
35. Verifikasi toast `Success, 3 assets have been returned.` tampil sesuai katalog toast

### Extend berlaku dengan satu Due date baru
36. Tampilkan Toast Borrow dengan kondisi K18
37. Verifikasi toast `Success, due date has been changed to 12/12/2026.` tampil sesuai katalog toast

### Extend berlaku dengan beberapa Due date baru
38. Tampilkan Toast Borrow dengan kondisi K19
39. Verifikasi toast `Success, due date has been changed for 3 assets.` tampil sesuai katalog toast

### Extend diajukan untuk satu BRW
40. Tampilkan Toast Borrow dengan kondisi K20
41. Verifikasi toast `Success, extension has been submitted for approval.` tampil sesuai katalog toast

### Extend diajukan untuk beberapa BRW
42. Tampilkan Toast Borrow dengan kondisi K21
43. Verifikasi toast `Success, extension has been submitted for approval in 2 borrows.` tampil sesuai katalog toast

### Cancel Borrow berhasil
44. Tampilkan Toast Borrow dengan kondisi K22
45. Verifikasi toast `Success, borrow has been canceled.` tampil sesuai katalog toast

### Delete Draft berhasil
46. Tampilkan Toast Borrow dengan kondisi K23
47. Verifikasi toast `Success, draft has been deleted.` tampil sesuai katalog toast

### Bulk Delete Draft sebagian terhapus
48. Tampilkan Toast Borrow dengan kondisi K24
49. Verifikasi toast `Success, draft has been deleted. Some items were skipped (outside your groups).` tampil sesuai katalog toast

### Salin Transaction ID
50. Tampilkan Toast Borrow dengan kondisi K25
51. Verifikasi toast `Success, Transaction ID has been copied.` tampil sesuai katalog toast

### Cancel Extension Request berhasil
52. Tampilkan Toast Borrow dengan kondisi K26
53. Verifikasi toast `Success, extension request has been canceled.` tampil sesuai katalog toast

### Hasil Borrow Now untuk satu aset
54. Tampilkan Toast Borrow dengan kondisi K27
55. Verifikasi panel hasil `Success, 1 asset is now borrowed. Return by 20/12/2026.` tampil di halaman

### Hasil Borrow Now untuk beberapa aset
56. Tampilkan Toast Borrow dengan kondisi K28
57. Verifikasi panel hasil `Success, 3 assets are now borrowed. Return by 20/12/2026.` tampil di halaman

### Cancel dengan Save as Draft to edit
58. Tampilkan Toast Borrow dengan kondisi K29
59. Verifikasi toast `Success, borrow has been canceled and saved as a draft.` tampil sesuai katalog toast

### Review Extension Request selesai
60. Tampilkan Toast Borrow dengan kondisi K30
61. Verifikasi toast `Success, extension request has been reviewed.` tampil sesuai katalog toast

### Gagal server pada aksi save
62. Tampilkan Toast Borrow dengan kondisi K31
63. Verifikasi toast `Error, failed to save borrow.` tampil sesuai katalog toast

### Gagal server pada aksi add
64. Tampilkan Toast Borrow dengan kondisi K32
65. Verifikasi toast `Error, failed to add assets.` tampil sesuai katalog toast

### Gagal server pada aksi submit
66. Tampilkan Toast Borrow dengan kondisi K33
67. Verifikasi toast `Error, failed to submit borrow.` tampil sesuai katalog toast

### Gagal server pada aksi approve
68. Tampilkan Toast Borrow dengan kondisi K34
69. Verifikasi toast `Error, failed to approve borrow.` tampil sesuai katalog toast

### Gagal server pada aksi reject
70. Tampilkan Toast Borrow dengan kondisi K35
71. Verifikasi toast `Error, failed to reject borrow.` tampil sesuai katalog toast

### Gagal server pada aksi hand over
72. Tampilkan Toast Borrow dengan kondisi K36
73. Verifikasi toast `Error, failed to hand over assets.` tampil sesuai katalog toast

### Gagal server pada aksi return
74. Tampilkan Toast Borrow dengan kondisi K37
75. Verifikasi toast `Error, failed to return assets.` tampil sesuai katalog toast

### Gagal server pada aksi extend
76. Tampilkan Toast Borrow dengan kondisi K38
77. Verifikasi toast `Error, failed to extend assets.` tampil sesuai katalog toast

### Gagal server pada aksi cancel
78. Tampilkan Toast Borrow dengan kondisi K39
79. Verifikasi toast `Error, failed to cancel borrow.` tampil sesuai katalog toast

### Gagal server pada aksi delete
80. Tampilkan Toast Borrow dengan kondisi K40
81. Verifikasi toast `Error, failed to delete draft.` tampil sesuai katalog toast

### Gagal server pada aksi remove
82. Tampilkan Toast Borrow dengan kondisi K41
83. Verifikasi toast `Error, failed to remove assets.` tampil sesuai katalog toast

### Gagal server pada aksi review
84. Tampilkan Toast Borrow dengan kondisi K42
85. Verifikasi toast `Error, failed to review extension request.` tampil sesuai katalog toast

### Gangguan jaringan
86. Tampilkan Toast Borrow dengan kondisi K43
87. Verifikasi toast `Connection problem. Please try again.` tampil sesuai katalog toast

### Submit tanpa perubahan
88. Tampilkan Toast Borrow dengan kondisi K44
89. Verifikasi toast `No changes to save.` tampil sesuai katalog toast

### Report Damaged dikirim
90. Tampilkan Toast Borrow dengan kondisi K45
91. Verifikasi toast `Success, damage report has been sent to the Asset Admin.` tampil sesuai katalog toast

### Remind Borrower berhasil
92. Tampilkan Toast Borrow dengan kondisi K46
93. Verifikasi toast `Success, reminder has been sent to Budi Santoso.` tampil sesuai katalog toast

### Submit Extend campuran oleh Aktor Borrow
94. Tampilkan Toast Borrow dengan kondisi K47
95. Verifikasi toast `Success, due date has been changed for 1 of 2 assets. 1 submitted for approval.` tampil sesuai katalog toast

### Submit Extend campuran dari My Asset
96. Tampilkan Toast Borrow dengan kondisi K48
97. Verifikasi toast `Success, due date has been changed for 1 of 2 assets. 1 sent for review.` tampil sesuai katalog toast

### Mark as Returned selesai untuk satu aset
98. Tampilkan Toast Borrow dengan kondisi K49
99. Verifikasi toast `Success, asset has been marked as returned.` tampil sesuai katalog toast

### Mark as Returned selesai untuk beberapa aset
100. Tampilkan Toast Borrow dengan kondisi K50
101. Verifikasi toast `Success, 3 assets have been marked as returned.` tampil sesuai katalog toast

### Toast sukses hilang sendiri
102. Tampilkan Toast Borrow dengan kondisi K51
103. Verifikasi toast `Success, borrow has been canceled.` tampil sesuai katalog toast sebelum waktu berlalu
104. Waktu berlalu sampai 4 detik sejak toast tampil
105. Verifikasi toast `Success, borrow has been canceled.` hilang sendiri

### Toast error bertahan sampai ditutup
106. Tampilkan Toast Borrow dengan kondisi K52
107. Verifikasi toast `Error, failed to cancel borrow.` tampil sesuai katalog toast sebelum waktu berlalu
108. Waktu berlalu sampai 60 detik sejak toast tampil
109. Verifikasi toast `Error, failed to cancel borrow.` masih tampil
110. Klik tombol tutup pada toast `Error, failed to cancel borrow.`
111. Verifikasi toast `Error, failed to cancel borrow.` hilang sesudah ditutup

### Gagal server pada aksi remind
112. Tampilkan Toast Borrow dengan kondisi K54
113. Verifikasi toast `Error, failed to remind borrower.` tampil sesuai katalog toast

### Submit Extend dari My Asset yang seluruhnya menunggu review
114. Tampilkan Toast Borrow dengan kondisi K56
115. Verifikasi toast pengajuan Extend untuk seluruh aset yang menunggu review tampil, dengan copy yang dimiliki katalog lain
