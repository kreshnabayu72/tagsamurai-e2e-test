---
id: TC-FA-BORROW-UI-070-guided-tooltip-halaman-borrow
title: "Guided Tooltip halaman Borrow dan halaman Review"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.7#p1", "§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#p2", "§4.7#p3", "§4.7#r4", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#p1": 2
  "§4.7#r1": [4, 5, 6]
  "§4.7#r2": [11, 12, 13]
  "§4.7#r3": [17, 18, 19]
  "§4.7#p2": [42, 45]
  "§4.7#p3": [47, 48]
  "§4.7#r4": [49, 50, 51]
  "EB-TBL-10": [2, 3, 7, 8, 10, 14, 16, 20, 22, 25, 28, 31, 34, 37, 39, 47, 52, 55]
anchor: [30, 41, 44, 54]
coverage:
  web: automated
---

# Guided Tooltip halaman Borrow dan halaman Review

## Prerequisites
- Aktor: Aktor Borrow dengan tombol `+ Borrow` pada plan Full.
- Layar awal: Halaman Borrow
- Komponen: Guided Tooltip Borrow
- Data:
  - DU-070-1: walkthrough Halaman Borrow dengan tiga step: Step 1 target tombol `+ Borrow`, Step 2 target Tabs halaman Borrow, Step 3 target kolom Status.
  - DU-070-2: walkthrough Halaman Review dengan satu step: Step 1 target kolom Approval Rule tabel T-BRW-08.
- Kondisi:
  - K1: kunjungan pertama ke Halaman Borrow, flag walkthrough belum diset, plan Full, Aktor memiliki tombol `+ Borrow`.
  - K2: kunjungan ke Halaman Borrow, flag walkthrough sudah diset karena walkthrough sebelumnya di-Skip atau selesai, plan Full, Aktor memiliki tombol `+ Borrow`.
  - K3: kunjungan pertama ke Halaman Borrow sesudah walkthrough sebelumnya ditutup lewat perubahan ukuran jendela sehingga flag belum diset, plan Full, Aktor memiliki tombol `+ Borrow`.
  - K4: kunjungan pertama ke Halaman Borrow, flag belum diset, plan Full, Aktor tidak memiliki tombol `+ Borrow`.
  - K5: kunjungan pertama ke Halaman Borrow, flag belum diset, plan Basic.
  - K6: kunjungan pertama ke Halaman Review (`Approvals > Borrow > Active > Review`), flag walkthrough belum diset.
  - K7: kunjungan ke Halaman Review, flag walkthrough sudah diset.

## Test Steps

### Walkthrough Halaman Borrow berjalan di kunjungan pertama
1. Tampilkan Guided Tooltip Borrow dengan kondisi K1
2. Verifikasi walkthrough Halaman Borrow muncul otomatis di kunjungan pertama
3. Verifikasi indikator `Step 1 of 3` tampil
4. Verifikasi tombol `+ Borrow` disorot sebagai target Step 1
5. Verifikasi judul `Start a borrow` tampil pada Step 1
6. Verifikasi deskripsi `Pick a borrower, add assets, then set how long and why for each. The clock starts at handover.` tampil pada Step 1
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil pada Step 1
8. Verifikasi tombol `[Back]` tidak tampil pada Step 1
9. Klik `[Next]`
10. Verifikasi indikator `Step 2 of 3` tampil
11. Verifikasi Tabs halaman Borrow disorot sebagai target Step 2
12. Verifikasi judul `Pick up where others left off` tampil pada Step 2
13. Verifikasi deskripsi `Drafts don't lock assets, and anyone managing these groups can continue them.` tampil pada Step 2
14. Verifikasi tombol `[Back]` tampil pada Step 2
15. Klik `[Next]`
16. Verifikasi indikator `Step 3 of 3` tampil
17. Verifikasi kolom Status disorot sebagai target Step 3
18. Verifikasi judul `One borrow, many assets` tampil pada Step 3
19. Verifikasi deskripsi `Each asset has its own status; the badge summarizes them.` tampil pada Step 3
20. Verifikasi tombol `[Done]` tampil pada Step 3 sebagai ganti `[Next]`
21. Klik `[Back]`
22. Verifikasi indikator `Step 2 of 3` tampil sesudah `[Back]`
23. Klik `[Next]`
24. Klik `[Done]`
25. Verifikasi walkthrough Halaman Borrow tertutup sesudah `[Done]`

### Skip menutup walkthrough
26. Tampilkan Guided Tooltip Borrow dengan kondisi K1
27. Klik `[Skip]`
28. Verifikasi walkthrough Halaman Borrow tertutup sesudah `[Skip]`

### Walkthrough tidak muncul lagi sesudah Skip atau Done
29. Tampilkan Guided Tooltip Borrow dengan kondisi K2
30. Verifikasi tombol `+ Borrow` tampil di Halaman Borrow
31. Verifikasi walkthrough Halaman Borrow tidak muncul otomatis

### Replay lewat tombol bantuan
32. Tampilkan Guided Tooltip Borrow dengan kondisi K2
33. Klik tombol `[?]` untuk memutar ulang walkthrough
34. Verifikasi walkthrough Halaman Borrow dimulai dari `Step 1 of 3`

### Keluar tanpa selesai tidak menyetel flag
35. Tampilkan Guided Tooltip Borrow dengan kondisi K1
36. Ubah ukuran jendela browser
37. Verifikasi walkthrough Halaman Borrow tertutup sesudah ukuran jendela diubah

### Walkthrough muncul lagi sesudah keluar tanpa selesai
38. Tampilkan Guided Tooltip Borrow dengan kondisi K3
39. Verifikasi walkthrough Halaman Borrow muncul otomatis lagi di kunjungan berikutnya

### Walkthrough tidak tampil tanpa tombol Borrow
40. Tampilkan Guided Tooltip Borrow dengan kondisi K4
41. Verifikasi tabel Halaman Borrow tampil tanpa tombol `+ Borrow`
42. Verifikasi walkthrough Halaman Borrow tidak muncul bagi Aktor tanpa tombol `+ Borrow`

### Walkthrough tidak tampil pada plan Basic
43. Tampilkan Guided Tooltip Borrow dengan kondisi K5
44. Verifikasi tabel Halaman Borrow tampil pada plan Basic
45. Verifikasi walkthrough Halaman Borrow tidak muncul pada plan Basic

### Walkthrough Halaman Review
46. Tampilkan Guided Tooltip Borrow dengan kondisi K6
47. Verifikasi walkthrough Halaman Review muncul otomatis di kunjungan pertama
48. Verifikasi indikator `Step 1 of 1` tampil
49. Verifikasi kolom Approval Rule tabel T-BRW-08 disorot sebagai target Step 1
50. Verifikasi judul `See who decided` tampil pada Step 1
51. Verifikasi deskripsi `Any one approver, all approvers, or a single approver, as set for each asset. Select a progress cell to see who has decided.` tampil
52. Verifikasi tombol `[Done]` tampil pada Step 1

### Walkthrough Halaman Review tidak muncul lagi
53. Tampilkan Guided Tooltip Borrow dengan kondisi K7
54. Verifikasi tabel T-BRW-08 tampil di Halaman Review
55. Verifikasi walkthrough Halaman Review tidak muncul otomatis
