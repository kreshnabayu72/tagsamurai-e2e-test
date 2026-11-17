---
id: TC-FA-MYASSET-UI-102-guided-tooltip-langkah-dan-navigasi
title: "Guided Tooltip My Asset: isi empat langkah, navigasi, dan langkah untuk tab yang tidak tampil"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4", "§9.10#p1", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [3, 4, 5]
  "§4.7#r2": [10, 11, 12]
  "§4.7#r3": [15, 16, 17]
  "§4.7#r4": [20, 21, 22]
  "§9.10#p1": [57, 58, 59, 63, 64, 66, 67]
  EB-TBL-10: [2, 7, 9, 14, 19, 23, 24, 27, 32, 33, 38, 41, 46, 47, 51]
anchor: [6, 26, 37, 49, 53, 55, 61]
coverage:
  web: automated
---

# Guided Tooltip My Asset: isi empat langkah, navigasi, dan langkah untuk tab yang tidak tampil

## Prerequisites
- Aktor: Borrower, Assignee, dan PIC pengguna halaman My Asset.
- Layar awal: Halaman My Asset.
- Komponen: Guided Tooltip My Asset
- Data:
  - DU-102-1: plan dengan Borrowing level `Full` dan Assignment `Tersedia`, dengan flag Guided Tooltip `belum diset`.
  - DU-102-2: plan dengan Borrowing level `Basic` dan Assignment `Tidak tersedia`, dengan flag Guided Tooltip `belum diset`.
  - DU-102-3: plan dengan Borrowing level `None` dan Assignment `Tersedia`, dengan flag Guided Tooltip `belum diset`.
  - DU-102-4: plan dengan Borrowing level `Full` dan Assignment `Tersedia`, dengan flag Guided Tooltip `sudah diset`.
- Kondisi:
  - K1: plan DU-102-1; keempat tab Task, Borrowed, Assigned, dan History tampil.
  - K2: plan DU-102-4; keempat tab Task, Borrowed, Assigned, dan History tampil.
  - K3: plan DU-102-2; tab Task, Borrowed, dan History tampil.
  - K4: plan DU-102-3; tab Task, Assigned, dan History tampil.

## Test Steps

### Isi keempat langkah dan navigasi dari langkah pertama sampai Done
1. Tampilkan Guided Tooltip My Asset dengan kondisi K1
2. Verifikasi progres `Step 1 of 4` tampil
3. Verifikasi langkah pertama menyorot tab `Task`
4. Verifikasi judul `Confirm what you received` tampil
5. Verifikasi deskripsi `Confirm a handover to start your borrow, or review and confirm an assignment here.` tampil
6. Verifikasi tombol `[Next]` tampil
7. Verifikasi tombol `[Back]` tidak tampil
8. Klik `[Next]`
9. Verifikasi progres `Step 2 of 4` tampil
10. Verifikasi langkah kedua menyorot tab `Borrowed`
11. Verifikasi judul `Track your borrowed assets` tampil
12. Verifikasi deskripsi `See due dates, extend when you need more time, and return on time.` tampil
13. Klik `[Next]`
14. Verifikasi progres `Step 3 of 4` tampil
15. Verifikasi langkah ketiga menyorot tab `Assigned`
16. Verifikasi judul `See your assigned assets` tampil
17. Verifikasi deskripsi `Assets assigned to you stay here until an admin unassigns them.` tampil
18. Klik `[Next]`
19. Verifikasi progres `Step 4 of 4` tampil
20. Verifikasi langkah keempat menyorot tab `History`
21. Verifikasi judul `Review past activity` tampil
22. Verifikasi deskripsi `Your closed borrows and assignments stay here for reference.` tampil
23. Verifikasi tombol `[Done]` tampil
24. Verifikasi tombol `[Next]` tidak tampil
25. Klik `[Done]`
26. Verifikasi tab `History` tampil
27. Verifikasi Guided Tooltip tertutup

### Back kembali ke langkah sebelumnya
28. Tampilkan Guided Tooltip My Asset dengan kondisi K1
29. Klik `[Next]`
30. Klik `[Next]`
31. Klik `[Back]`
32. Verifikasi progres `Step 2 of 4` tampil
33. Verifikasi judul `Track your borrowed assets` tampil

### Skip menutup walkthrough
34. Tampilkan Guided Tooltip My Asset dengan kondisi K1
35. Klik `[Next]`
36. Klik `[Skip]`
37. Verifikasi tab `Borrowed` tampil
38. Verifikasi Guided Tooltip tertutup

### Putar ulang dari langkah pertama lewat tombol bantuan
39. Tampilkan Guided Tooltip My Asset dengan kondisi K2
40. Klik `[?]` di sebelah Breadcrumb
41. Verifikasi progres `Step 1 of 4` tampil
42. Klik `[Next]`
43. Klik `[Next]`
44. Klik `[Skip]`
45. Klik `[?]` di sebelah Breadcrumb
46. Verifikasi progres `Step 1 of 4` tampil
47. Verifikasi judul `Confirm what you received` tampil

### Mengubah ukuran jendela menutup walkthrough
48. Tampilkan Guided Tooltip My Asset dengan kondisi K1
49. Verifikasi progres `Step 1 of 4` tampil
50. Ubah ukuran jendela browser
51. Verifikasi Guided Tooltip tertutup

### Langkah tab Assigned dilewati pada plan tanpa Assignment
52. Tampilkan Guided Tooltip My Asset dengan kondisi K3
53. Verifikasi judul `Confirm what you received` tampil
54. Klik `[Next]`
55. Verifikasi judul `Track your borrowed assets` tampil
56. Klik `[Next]`
57. Verifikasi judul `Review past activity` tampil
58. Verifikasi judul `See your assigned assets` tidak tampil
59. Verifikasi tombol `[Done]` tampil

### Langkah tab Borrowed dilewati pada plan tanpa Borrowing
60. Tampilkan Guided Tooltip My Asset dengan kondisi K4
61. Verifikasi judul `Confirm what you received` tampil
62. Klik `[Next]`
63. Verifikasi judul `See your assigned assets` tampil
64. Verifikasi judul `Track your borrowed assets` tidak tampil
65. Klik `[Next]`
66. Verifikasi judul `Review past activity` tampil
67. Verifikasi tombol `[Done]` tampil
