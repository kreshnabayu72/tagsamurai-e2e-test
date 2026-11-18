---
id: TC-FA-MYASSET-UI-102-guided-tooltip-langkah-dan-navigasi
title: "Guided Tooltip My Asset: isi empat langkah, navigasi, dan langkah untuk tab yang tidak tampil"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4", "§9.10#p1", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [3, 4, 5]
  "§4.7#r2": [10, 11, 12]
  "§4.7#r3": [15, 16, 17]
  "§4.7#r4": [20, 21, 22]
  "§9.10#p1": [55, 56, 57, 61, 62, 64, 65]
  EB-TBL-10: [2, 7, 9, 14, 19, 23, 24, 26, 31, 32, 36, 39, 44, 45, 49]
anchor: [6, 47, 51, 53, 59]
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
26. Verifikasi Guided Tooltip tertutup

### Back kembali ke langkah sebelumnya
27. Tampilkan Guided Tooltip My Asset dengan kondisi K1
28. Klik `[Next]`
29. Klik `[Next]`
30. Klik `[Back]`
31. Verifikasi progres `Step 2 of 4` tampil
32. Verifikasi judul `Track your borrowed assets` tampil

### Skip menutup walkthrough
33. Tampilkan Guided Tooltip My Asset dengan kondisi K1
34. Klik `[Next]`
35. Klik `[Skip]`
36. Verifikasi Guided Tooltip tertutup

### Putar ulang dari langkah pertama lewat tombol bantuan
37. Tampilkan Guided Tooltip My Asset dengan kondisi K2
38. Klik `[?]` di sebelah Breadcrumb
39. Verifikasi progres `Step 1 of 4` tampil
40. Klik `[Next]`
41. Klik `[Next]`
42. Klik `[Skip]`
43. Klik `[?]` di sebelah Breadcrumb
44. Verifikasi progres `Step 1 of 4` tampil
45. Verifikasi judul `Confirm what you received` tampil

### Mengubah ukuran jendela menutup walkthrough
46. Tampilkan Guided Tooltip My Asset dengan kondisi K1
47. Verifikasi progres `Step 1 of 4` tampil
48. Ubah ukuran jendela browser
49. Verifikasi Guided Tooltip tertutup

### Langkah tab Assigned dilewati pada plan tanpa Assignment
50. Tampilkan Guided Tooltip My Asset dengan kondisi K3
51. Verifikasi judul `Confirm what you received` tampil
52. Klik `[Next]`
53. Verifikasi judul `Track your borrowed assets` tampil
54. Klik `[Next]`
55. Verifikasi judul `Review past activity` tampil
56. Verifikasi judul `See your assigned assets` tidak tampil
57. Verifikasi tombol `[Done]` tampil

### Langkah tab Borrowed dilewati pada plan tanpa Borrowing
58. Tampilkan Guided Tooltip My Asset dengan kondisi K4
59. Verifikasi judul `Confirm what you received` tampil
60. Klik `[Next]`
61. Verifikasi judul `See your assigned assets` tampil
62. Verifikasi judul `Track your borrowed assets` tidak tampil
63. Klik `[Next]`
64. Verifikasi judul `Review past activity` tampil
65. Verifikasi tombol `[Done]` tampil
