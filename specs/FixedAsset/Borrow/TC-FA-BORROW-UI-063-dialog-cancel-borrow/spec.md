---
id: TC-FA-BORROW-UI-063-dialog-cancel-borrow
title: "Dialog Cancel Borrow dan hapus Draft: bullet BRW, checkbox Save as Draft to edit, dan reaksi gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-BRW-01", "DM-BRW-01", "DM-BRW-02", "FLD-BRW-26", "EB-ERR-1@cancel-borrow", "EB-ERR-2@delete-draft"]
smoke: []
dependsOn: []
trace:
  "D-BRW-01": [2, 3, 4, 5, 6, 7, 8, 13, 17, 18, 19, 21, 22, 28, 29, 30, 31, 32, 36, 37, 38, 42, 43, 44, 45, 78, 79, 80, 82, 83, 84, 85, 87, 88, 89]
  "DM-BRW-01": [3, 10, 15, 24, 26]
  "DM-BRW-02": [28, 34, 36, 40, 47, 49, 50]
  "FLD-BRW-26": [5, 18, 22, 79, 84]
  "EB-ERR-1@cancel-borrow": [54, 55, 56, 58, 61, 62, 64]
  "EB-ERR-2@delete-draft": [67, 71, 74, 76]
anchor: [69]
coverage:
  web: automated
---

# Dialog Cancel Borrow dan hapus Draft: bullet BRW, checkbox Save as Draft to edit, dan reaksi gagal

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`; pada K13 dialog dibuka oleh pengguna yang bukan Aktor Borrow.
- Layar awal: Halaman daftar yang memuat pemicu dialog
- Komponen: Dialog Cancel Borrow
- Data:
  - DU-063-1: BRW `BRW-2026-0153`, Status `Waiting for Approval`, tanpa baris Borrowed, Group `Finance`.
  - DU-063-2: BRW `BRW-2026-0147`, Status `Borrowed`, sudah punya baris Borrowed, Group `Finance`.
  - DU-063-3: Draft `Draft Peminjaman Finance 01`, Group `Finance`.
  - DU-063-4: Draft `Draft Peminjaman Finance 02`, Group `Finance`.
  - DU-063-5: Draft `Draft Peminjaman Gudang 03`, Group `Gudang Pusat`, di luar cakupan Aktor.
  - DU-063-6: BRW `BRW-2026-0160`, hanya berisi baris Overdue dan tanpa baris Borrowed, Group `Finance`.
  - DU-063-7: 12 Draft `Draft Pengadaan Finance {n}` (n = 1 sampai 12), Group `Finance`.
- Kondisi:
  - K1: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka dari Transactions untuk DU-063-1.
  - K2: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka dari Transactions untuk DU-063-2.
  - K3: level Feature Suite Borrowing bernilai `Basic`, dialog Cancel Borrow dibuka dari Transactions untuk DU-063-1 yang dibuat saat level `Full`.
  - K4: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka dari Borrow Detail untuk DU-063-1.
  - K5: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka dari Borrowed Assets untuk DU-063-1.
  - K6: dialog Delete Draft dibuka dari tab Drafts untuk DU-063-3.
  - K7: dialog Delete Draft dibuka dari tab Drafts untuk DU-063-3 dan DU-063-4.
  - K8: dialog Delete Draft dibuka dari tab Drafts untuk DU-063-3, DU-063-4, dan DU-063-5.
  - K9: dialog Delete Draft dibuka dari tab Drafts untuk DU-063-5 saja.
  - K10: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka untuk DU-063-1, konfirmasi pertama dijawab error server, konfirmasi berikutnya berhasil.
  - K11: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka untuk DU-063-1, konfirmasi pertama tidak mendapat respons karena koneksi putus, konfirmasi berikutnya berhasil.
  - K12: dialog Delete Draft dibuka dari tab Drafts untuk DU-063-3, yang dicentang, lewat bulk action `Delete` di bar aksi.
  - K13: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka untuk DU-063-1 oleh pengguna yang bukan Aktor Borrow.
  - K14: level Feature Suite Borrowing bernilai `Full`, dialog Cancel Borrow dibuka untuk DU-063-6.
  - K15: dialog Delete Draft dibuka dari tab Drafts untuk seluruh DU-063-7.

## Test Steps

### Dialog Cancel Borrow tanpa checkbox dicentang
1. Tampilkan Dialog Cancel Borrow dengan kondisi K1
2. Verifikasi judul dialog `Cancel Borrow` tampil
3. Verifikasi bullet `BRW-2026-0153` tampil di body dialog
4. Verifikasi dialog tidak memiliki field Reason
5. Verifikasi checkbox `Save as Draft to edit` tampil dan tidak tercentang
6. Verifikasi teks bantu `The assets become available again and the borrower and approvers are notified.` tampil
7. Verifikasi pertanyaan `Are you sure you want to cancel it?` tampil
8. Verifikasi tombol `[Go Back]` dan `[Cancel Borrow]` tampil
9. Klik `[Cancel Borrow]`
10. Verifikasi toast `Success, borrow has been canceled.` tampil

### Dialog Cancel Borrow dengan Save as Draft to edit dicentang
11. Tampilkan Dialog Cancel Borrow dengan kondisi K1
12. Centang checkbox `Save as Draft to edit`
13. Verifikasi teks bantu `The assets become available again and a new draft with the same details is created so you can fix and resubmit it.` tampil
14. Klik `[Cancel Borrow]`
15. Verifikasi toast `Success, borrow has been canceled and saved as a draft.` tampil

### Checkbox tidak tampil bila BRW sudah punya baris Borrowed
16. Tampilkan Dialog Cancel Borrow dengan kondisi K2
17. Verifikasi bullet `BRW-2026-0147` tampil di body dialog
18. Verifikasi checkbox `Save as Draft to edit` tidak tampil
19. Verifikasi teks bantu `The assets become available again and the borrower and approvers are notified.` tampil tanpa checkbox

### Checkbox tidak tampil pada level Basic
20. Tampilkan Dialog Cancel Borrow dengan kondisi K3
21. Verifikasi bullet `BRW-2026-0153` tampil di body dialog pada level `Basic`
22. Verifikasi checkbox `Save as Draft to edit` tidak tampil pada level `Basic`

### Dialog Cancel Borrow dari Borrow Detail
23. Tampilkan Dialog Cancel Borrow dengan kondisi K4
24. Verifikasi dialog `Cancel Borrow` untuk BRW `BRW-2026-0153` tampil dari Borrow Detail

### Dialog Cancel Borrow dari Borrowed Assets
25. Tampilkan Dialog Cancel Borrow dengan kondisi K5
26. Verifikasi dialog `Cancel Borrow` untuk BRW `BRW-2026-0153` tampil dari Borrowed Assets

### Dialog Delete Draft untuk satu Draft
27. Tampilkan Dialog Cancel Borrow dengan kondisi K6
28. Verifikasi judul dialog `Delete Draft` tampil
29. Verifikasi bullet `Draft Peminjaman Finance 01` tampil di body dialog
30. Verifikasi teks `This draft will be removed. Are you sure you want to delete it?` tampil
31. Verifikasi dialog Delete Draft tidak memiliki field Reason
32. Verifikasi tombol `[Go Back]` dan `[Delete]` tampil
33. Klik `[Delete]`
34. Verifikasi toast `Success, draft has been deleted.` tampil

### Dialog Delete Drafts untuk beberapa Draft
35. Tampilkan Dialog Cancel Borrow dengan kondisi K7
36. Verifikasi judul dialog `Delete Drafts` tampil
37. Verifikasi bullet `Draft Peminjaman Finance 01` dan `Draft Peminjaman Finance 02` tampil di body dialog
38. Verifikasi teks `Are you sure you want to delete them?` tampil
39. Klik `[Delete]`
40. Verifikasi toast `Success, draft has been deleted.` tampil sesudah Delete Drafts

### Dialog campuran untuk Draft yang dilewati
41. Tampilkan Dialog Cancel Borrow dengan kondisi K8
42. Verifikasi teks `The following will be deleted:` tampil dengan bullet `Draft Peminjaman Finance 01` dan `Draft Peminjaman Finance 02`
43. Verifikasi teks `The following have groups outside your access and will be skipped:` tampil dengan bullet `Draft Peminjaman Gudang 03`
44. Verifikasi teks `Are you sure you want to continue?` tampil
45. Verifikasi tombol `[Go Back]` dan `[Continue]` tampil
46. Klik `[Continue]`
47. Verifikasi toast `Success, draft has been deleted. Some items were skipped (outside your groups).` tampil

### Delete Draft diblokir bila tidak ada Draft yang dapat dihapus
48. Tampilkan Dialog Cancel Borrow dengan kondisi K9
49. Verifikasi dialog blok `Cannot Delete Drafts` tampil
50. Verifikasi teks `None of the selected drafts can be deleted because they have groups outside your access.` dan tombol `[OK]` tampil

### Cancel Borrow gagal karena error server lalu diulang
51. Tampilkan Dialog Cancel Borrow dengan kondisi K10
52. Centang checkbox `Save as Draft to edit`
53. Klik `[Cancel Borrow]`
54. Verifikasi toast `Error, failed to cancel borrow.` tampil
55. Verifikasi toast error Cancel Borrow tidak menampilkan tombol aksi `[Try Again]`
56. Verifikasi dialog tetap terbuka, checkbox `Save as Draft to edit` tetap tercentang, dan tombol `[Cancel Borrow]` aktif lagi
57. Klik `[Cancel Borrow]`
58. Verifikasi toast `Success, borrow has been canceled and saved as a draft.` tampil sesudah konfirmasi diulang

### Cancel Borrow gagal karena koneksi putus lalu diulang
59. Tampilkan Dialog Cancel Borrow dengan kondisi K11
60. Klik `[Cancel Borrow]`
61. Verifikasi toast `Connection problem. Please try again.` tampil setelah konfirmasi tidak mendapat respons
62. Verifikasi dialog tetap terbuka dan tombol `[Cancel Borrow]` aktif lagi setelah gangguan koneksi
63. Klik `[Cancel Borrow]`
64. Verifikasi toast `Success, borrow has been canceled.` tampil sesudah koneksi pulih

### Klik ganda Delete menghapus sekali
65. Tampilkan Dialog Cancel Borrow dengan kondisi K12
66. Klik ganda `[Delete]`
67. Verifikasi satu toast `Success, draft has been deleted.` tampil

### Esc menutup dialog Delete Draft tanpa menghapus
68. Tampilkan Dialog Cancel Borrow dengan kondisi K12
69. Verifikasi dialog `Delete Draft` tampil sebelum Esc ditekan
70. Tekan `Esc`
71. Verifikasi dialog `Delete Draft` tertutup dan tidak ada toast `Success, draft has been deleted.`

### Fokus terkunci di dialog dan kembali ke pemicu
72. Tampilkan Dialog Cancel Borrow dengan kondisi K12
73. Tekan `Tab` dua kali
74. Verifikasi fokus berada di dalam dialog `Delete Draft`
75. Klik `[Go Back]`
76. Verifikasi fokus kembali ke bulk action `Delete` yang membuka dialog

### Checkbox tidak tampil bagi pengguna yang bukan Aktor Borrow
77. Tampilkan Dialog Cancel Borrow dengan kondisi K13
78. Verifikasi bullet `BRW-2026-0153` tampil di body dialog
79. Verifikasi checkbox `Save as Draft to edit` tidak tampil bagi pengguna yang bukan Aktor Borrow
80. Verifikasi teks bantu `The assets become available again and the borrower and approvers are notified.` tampil tanpa checkbox

### Checkbox tidak tampil bila BRW hanya berisi baris Overdue
81. Tampilkan Dialog Cancel Borrow dengan kondisi K14
82. Verifikasi judul dialog `Cancel Borrow` tampil
83. Verifikasi bullet `BRW-2026-0160` tampil di body dialog
84. Verifikasi checkbox `Save as Draft to edit` tidak tampil
85. Verifikasi teks bantu `The assets become available again and the borrower and approvers are notified.` tampil tanpa checkbox

### Dialog Delete Drafts memuat banyak Draft dalam daftar yang dapat di-scroll
86. Tampilkan Dialog Cancel Borrow dengan kondisi K15
87. Verifikasi judul dialog `Delete Drafts` tampil
88. Verifikasi bullet 12 Draft `Draft Pengadaan Finance` tampil di dalam daftar yang dapat di-scroll sehingga seluruhnya terjangkau
89. Verifikasi tombol `[Go Back]` dan `[Delete]` tampil
