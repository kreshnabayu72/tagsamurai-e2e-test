---
id: TC-FA-FAREG-UI-009-draft-guided-tooltip
title: "Sub tab Draft: Guided Tooltip `fa-registration`"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#p3", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [3, 5, 6]
  "§4.7#r2": [11, 12, 13]
  "§4.7#r3": [17, 18, 19]
  "§4.7#p3": [69, 70, 71, 73, 74, 75]
  EB-TBL-10: [2, 4, 7, 8, 10, 14, 16, 20, 21, 23, 26, 28, 30, 33, 35, 38, 41, 43, 44, 48, 50, 53, 55, 57, 59, 62, 64, 67, 76]
anchor: [27, 32, 37, 40, 47, 61, 66]
coverage:
  web: automated
---

# Sub tab Draft: Guided Tooltip `fa-registration`

## Prerequisites
- Aktor: Total Control; pada kondisi K3 Manage purchase.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-009-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
- Kondisi:
  - K1: daftar berisi DU-009-1; kunjungan pertama aktor ke halaman Registration (flag tur belum disetel).
  - K2: daftar berisi DU-009-1; flag tur sudah disetel sehingga tur tidak mulai otomatis.
  - K3: sama dengan K1; aktor Manage purchase, sehingga tombol `[+ Register Asset]` Hidden.
  - Lebar viewport uji: awal `1440` px, lalu diubah menjadi `768` px.

## Test Steps

### Konten dan navigasi tur dari Step 1 sampai Done
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Verifikasi tur Guided Tooltip mulai otomatis pada kunjungan pertama
3. Verifikasi overlay gelap menutupi halaman dengan spotlight pada tabel sub tab Draft
4. Verifikasi step indicator `Step 1 of 3`
5. Verifikasi judul tooltip `See what's missing`
6. Verifikasi deskripsi tooltip `Open a draft to fill the missing fields.`
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil pada tooltip
8. Verifikasi tombol `[Back]` tidak tampil
9. Klik `[Next]`
10. Verifikasi step indicator `Step 2 of 3`
11. Verifikasi judul tooltip `Start a draft`
12. Verifikasi deskripsi tooltip `Only a few fields are needed to save a draft.`
13. Verifikasi spotlight berpindah ke tombol `[+ Register Asset]`
14. Verifikasi tombol `[Back]` tampil
15. Klik `[Next]`
16. Verifikasi step indicator `Step 3 of 3`
17. Verifikasi judul tooltip `Follow your requests`
18. Verifikasi deskripsi tooltip `Each activation or submission creates a request.`
19. Verifikasi spotlight pada Sub tab `Waiting for Approval`
20. Verifikasi tombol `[Done]` tampil
21. Verifikasi tombol `[Next]` tidak tampil
22. Klik `[Back]`
23. Verifikasi step indicator `Step 2 of 3`
24. Klik `[Next]`
25. Klik `[Done]`
26. Verifikasi tur tertutup
27. Verifikasi tabel sub tab Draft tampil
28. Verifikasi overlay tur tidak tampil

### Skip menutup tur
29. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
30. Verifikasi step indicator `Step 1 of 3`
31. Klik `[Skip]`
32. Verifikasi tabel sub tab Draft tampil
33. Verifikasi overlay tur tidak tampil

### Klik overlay sama dengan Skip
34. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
35. Verifikasi step indicator `Step 1 of 3`
36. Klik area overlay di luar tooltip
37. Verifikasi tabel sub tab Draft tampil
38. Verifikasi overlay tur tidak tampil

### Replay lewat tombol bantuan
39. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
40. Verifikasi tabel sub tab Draft tampil
41. Verifikasi overlay tur tidak tampil
42. Klik `[?]` di sebelah kanan Breadcrumb
43. Verifikasi step indicator `Step 1 of 3`
44. Verifikasi judul tooltip `See what's missing`
45. Klik `[Next]`
46. Klik `[Skip]`
47. Verifikasi tabel sub tab Draft tampil
48. Verifikasi overlay tur tidak tampil
49. Klik `[?]` di sebelah kanan Breadcrumb
50. Verifikasi step indicator `Step 1 of 3`

### Navigasi keyboard
51. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
52. Klik `[?]` di sebelah kanan Breadcrumb
53. Verifikasi tooltip menerima keyboard focus
54. Tekan `Enter`
55. Verifikasi step indicator `Step 2 of 3`
56. Tekan `→`
57. Verifikasi step indicator `Step 3 of 3`
58. Tekan `←`
59. Verifikasi step indicator `Step 2 of 3`
60. Tekan `Esc`
61. Verifikasi tabel sub tab Draft tampil
62. Verifikasi overlay tur tidak tampil

### Resize menutup tur
63. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
64. Verifikasi step indicator `Step 1 of 3`
65. Ubah lebar viewport browser dari `1440` px menjadi `768` px
66. Verifikasi tabel sub tab Draft tampil
67. Verifikasi overlay tur tidak tampil

### Langkah bertarget Hidden dilewati
68. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
69. Verifikasi tabel sub tab Draft tampil
70. Verifikasi tombol `[+ Register Asset]` tidak tampil
71. Verifikasi judul tooltip `See what's missing`
72. Klik `[Next]`
73. Verifikasi judul tooltip `Follow your requests`
74. Verifikasi spotlight pada Sub tab `Waiting for Approval`
75. Verifikasi judul tooltip `Start a draft` tidak tampil
76. Verifikasi tombol `[Done]` tampil
