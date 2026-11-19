---
id: TC-FA-BORROW-E2E-016-draft-bersama-cakupan-konflik
title: "Draft bersama dapat dibaca dan diubah Aktor Borrow dalam cakupan Group, dan simpan bersamaan ditolak penyimpan kedua"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-45", "FI-BRW-46", "FI-BRW-47", "FI-BRW-48", "FI-BRW-49", "§2.2#p6", "§2.2#p7", "§2.2#p8", "§2.2#p9", "EB-AKS-6"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-45": 18
  "FI-BRW-46": 19
  "FI-BRW-47": [21, 22]
  "FI-BRW-48": [38, 41, 63, 67]
  "FI-BRW-49": [41, 42, 44, 45, 65, 69, 72]
  "§2.2#p6": [3, 7]
  "§2.2#p7": [18, 20, 21]
  "§2.2#p8": [25, 28, 30]
  "§2.2#p9": [4, 8, 11, 14]
  "EB-AKS-6": [53, 54]
anchor: [10, 13]
coverage:
  web: automated
---

# Draft bersama dapat dibaca dan diubah Aktor Borrow dalam cakupan Group, dan simpan bersamaan ditolak penyimpan kedua

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office` (konteks utama). Konteks kedua dan seterusnya: Asset Admin `Hendra Kurnia {runId}` dengan Group penugasan `Branch Surabaya`, Total Control `Tia Total Control {runId}`, Monitoring & Report `Monita Monitoring {runId}`, dan Read Only `Raka Read Only {runId}`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-016-1: Borrower `Sari Dewi {runId}`, Email `sari.dewi{runId}@example.com`, Position `Analyst {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-016-2: `Agus Pratama {runId}`, role Asset Admin, Group penugasan `Head Office`.
  - DU-016-3: `Hendra Kurnia {runId}`, role Asset Admin, Group penugasan `Branch Surabaya`.
  - DU-016-4: `Tia Total Control {runId}`, role Total Control (cakupan seluruh client).
  - DU-016-5: `Monita Monitoring {runId}`, role Monitoring & Report, Group penugasan `Head Office` dan `Branch Surabaya`.
  - DU-016-6: `Raka Read Only {runId}`, role Read Only.
  - DU-016-7: aset `Laptop Dell Inspiron {runId}`, Brand `Dell {runId}`, Model/Type `Inspiron 14 {runId}`, Group `Head Office`, Category `Laptop {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-016-8: aset `Proyektor Acer {runId}`, Brand `Acer {runId}`, Model/Type `X1123H {runId}`, Group `Head Office`, Category `Projector {runId}`, Custody `Available`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-016-9: aset `Toyota Calya {runId}`, Brand `Toyota {runId}`, Model/Type `Calya {runId}`, Group `Branch Surabaya`, Category `Car {runId}`, Custody `Available`, Max Duration `14 days`, Approval `Needs approval`.
  - DU-016-10: aset `Daihatsu Gran Max {runId}`, Brand `Daihatsu {runId}`, Model/Type `Gran Max {runId}`, Group `Branch Surabaya`, Category `Car {runId}`, Custody `Available`, Max Duration `14 days`, Approval `Needs approval`.
  - DU-016-11: aset `Honda Brio {runId}`, Brand `Honda {runId}`, Model/Type `Brio {runId}`, Group `Branch Surabaya`, Category `Car {runId}`, Custody `Available`, Max Duration `14 days`, Approval `Needs approval`.
  - DU-016-12: Draft pertama untuk Borrower `Sari Dewi {runId}` dengan empat aset (`Laptop Dell Inspiron {runId}`, `Proyektor Acer {runId}`, `Toyota Calya {runId}`, `Daihatsu Gran Max {runId}`), Total Asset `4`, Duration `3` dan Purpose `Training` pada setiap baris, Modified By `Tia Total Control {runId}`.
  - DU-016-13: Draft kedua untuk Borrower `Sari Dewi {runId}` hanya berisi aset `Honda Brio {runId}`, Total Asset `1`, Duration `2` dan Purpose `Kunjungan cabang`, Modified By `Tia Total Control {runId}`.
  - DU-016-14: ubahan Draft pertama: Purpose `Laptop Dell Inspiron {runId}` menjadi `Perubahan Tia` oleh `Tia Total Control {runId}`; Purpose `Proyektor Acer {runId}` menjadi `Perubahan Agus` oleh `Agus Pratama {runId}` yang tidak tersimpan; teks dialog Draft Changed `This draft was changed by Tia Total Control {runId} at [Time]. Reload to see the latest version; your unsaved changes will be lost.`; ubahan Draft kedua oleh `Hendra Kurnia {runId}`: Purpose `Honda Brio {runId}` menjadi `Perubahan Hendra` yang ditolak.
  - DU-016-15: ubahan Draft pertama oleh Submit: Purpose `Proyektor Acer {runId}` menjadi `Pembaruan Agus` oleh `Agus Pratama {runId}` dan tersimpan; teks dialog Draft Changed bagi `Tia Total Control {runId}` `This draft was changed by Agus Pratama {runId} at [Time]. Reload to see the latest version; your unsaved changes will be lost.`.
- Kondisi:
  - Akun `Agus Pratama {runId}`, `Hendra Kurnia {runId}`, `Tia Total Control {runId}`, `Monita Monitoring {runId}`, dan `Raka Read Only {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Draft terlihat oleh Aktor Borrow yang cakupannya meliputi minimal satu aset di Draft
1. Konteks `Agus Pratama {runId}`: Buka tab Drafts
2. Ketik Search `Sari Dewi {runId}`, tekan Enter
3. Verifikasi baris Draft dengan Total Asset `4` untuk Borrower `Sari Dewi {runId}` tampil di tab Drafts
4. Verifikasi Draft yang hanya berisi aset `Honda Brio {runId}` (Total Asset `1`) tidak tampil di tab Drafts
5. Konteks `Hendra Kurnia {runId}`: Buka tab Drafts
6. Ketik Search `Sari Dewi {runId}`, tekan Enter
7. Verifikasi baris Draft dengan Total Asset `4` untuk Borrower `Sari Dewi {runId}` tampil di tab Drafts
8. Verifikasi baris Draft dengan Total Asset `1` yang hanya berisi aset `Honda Brio {runId}` tampil di tab Drafts

### Monitoring & Report dan Read Only tidak melihat Draft
9. Konteks `Monita Monitoring {runId}`: Buka halaman Transactions > Borrow
10. Verifikasi tab `Transactions` tampil di halaman Borrow
11. Verifikasi tab `Drafts` tidak tampil (Hidden) bagi Monitoring & Report
12. Konteks `Raka Read Only {runId}`: Buka halaman Transactions > Borrow
13. Verifikasi tab `Transactions` tampil di halaman Borrow
14. Verifikasi tab `Drafts` tidak tampil (Hidden) bagi Read Only

### Baris aset di luar cakupan tampil read-only dan Submit disabled
15. Konteks `Agus Pratama {runId}`: Buka tab Drafts
16. Ketik Search `Sari Dewi {runId}`, tekan Enter
17. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
18. Verifikasi baris `Toyota Calya {runId}` dan baris `Daihatsu Gran Max {runId}` tampil read-only dengan nama aset, Group `Branch Surabaya`, dan keterangan `Outside your groups`
19. Verifikasi tombol hapus dan isian Duration serta Purpose pada baris `Toyota Calya {runId}` dan baris `Daihatsu Gran Max {runId}` nonaktif
20. Verifikasi isian Duration dan Purpose pada baris `Laptop Dell Inspiron {runId}` dan baris `Proyektor Acer {runId}` aktif dan dapat diubah
21. Verifikasi tombol `[Submit]` disabled karena ada baris di luar cakupan
22. Verifikasi alasan `Some assets are outside your groups. Ask [Name] to submit.` tersampaikan pada tombol `[Submit]` yang disabled, dengan [Name] diisi nama Aktor yang dapat men-Submit
23. Klik `[Cancel]` pada form yang belum diubah

### Submit dan Delete Draft hanya oleh Aktor yang cakupannya meliputi semua Group
24. Ketik Search `Sari Dewi {runId}`, tekan Enter
25. Verifikasi aksi `Delete` pada baris Draft dengan Total Asset `4` disabled dan alasan `Some assets are outside your groups. Ask [Name] to delete.` tersampaikan pada aksi itu
26. Konteks `Tia Total Control {runId}`: Buka tab Drafts
27. Ketik Search `Sari Dewi {runId}`, tekan Enter
28. Verifikasi aksi `Delete` pada baris Draft dengan Total Asset `4` aktif bagi Total Control
29. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
30. Verifikasi tombol `[Submit]` aktif bagi Total Control karena cakupannya meliputi Group `Head Office` dan `Branch Surabaya`
31. Klik `[Cancel]` pada form yang belum diubah

### Simpan bersamaan: penyimpan kedua mendapat dialog Draft Changed
32. Konteks `Agus Pratama {runId}`: Buka tab Drafts
33. Ketik Search `Sari Dewi {runId}`, tekan Enter
34. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
35. Konteks `Tia Total Control {runId}`: Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
36. Ganti Purpose baris `Laptop Dell Inspiron {runId}` dengan `Perubahan Tia`
37. Klik `[Save Draft]`
38. Verifikasi toast `Success, borrow has been saved as draft.` tampil bagi Total Control
39. Konteks `Agus Pratama {runId}`: Ganti Purpose baris `Proyektor Acer {runId}` dengan `Perubahan Agus`
40. Klik `[Save Draft]`
41. Verifikasi dialog `Draft Changed` tampil dengan teks `This draft was changed by Tia Total Control {runId} at [Time]. Reload to see the latest version; your unsaved changes will be lost.`
42. Verifikasi dialog `Draft Changed` memuat tombol `[Cancel]` dan `[Reload]`
43. Klik `[Reload]`
44. Verifikasi baris `Laptop Dell Inspiron {runId}` berisi Purpose `Perubahan Tia` sesudah Draft dimuat ulang
45. Verifikasi baris `Proyektor Acer {runId}` tidak berisi Purpose `Perubahan Agus` karena perubahan belum tersimpan hilang
46. Klik `[Cancel]` pada form yang belum diubah

### Pencabutan cakupan Group saat Draft terbuka
47. Konteks `Hendra Kurnia {runId}`: Buka tab Drafts
48. Ketik Search `Sari Dewi {runId}`, tekan Enter
49. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `1`
50. Konteks `Tia Total Control {runId}`: Cabut Group penugasan `Branch Surabaya` dari Asset Admin `Hendra Kurnia {runId}`
51. Konteks `Hendra Kurnia {runId}`: Ganti Purpose baris `Honda Brio {runId}` dengan `Perubahan Hendra`
52. Klik `[Save Draft]`
53. Verifikasi toast error `You don't have permission to do this.` tampil
54. Verifikasi aksi `[Save Draft]` dan `[Submit]` tidak lagi tersedia pada form karena Aktor tidak lagi berhak

### Submit atas Draft yang sudah diubah orang lain mendapat dialog Draft Changed
55. Konteks `Tia Total Control {runId}`: Buka tab Drafts
56. Ketik Search `Sari Dewi {runId}`, tekan Enter
57. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
58. Konteks `Agus Pratama {runId}`: Buka tab Drafts
59. Ketik Search `Sari Dewi {runId}`, tekan Enter
60. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `4`
61. Ganti Purpose baris `Proyektor Acer {runId}` dengan `Pembaruan Agus`
62. Klik `[Save Draft]`
63. Verifikasi toast `Success, borrow has been saved as draft.` tampil bagi Asset Admin `Agus Pratama {runId}`
64. Konteks `Tia Total Control {runId}`: Klik `[Submit]`
65. Verifikasi dialog `Draft Changed` tampil dengan teks `This draft was changed by Agus Pratama {runId} at [Time]. Reload to see the latest version; your unsaved changes will be lost.`
66. Klik `[Reload]`
67. Verifikasi baris `Proyektor Acer {runId}` berisi Purpose `Pembaruan Agus` sesudah Draft dimuat ulang
68. Klik `[Cancel]` pada form yang belum diubah
69. Verifikasi baris Draft dengan Total Asset `4` untuk Borrower `Sari Dewi {runId}` masih tampil di tab Drafts karena Submit tidak diproses
70. Buka tab Transactions
71. Ketik Search `Sari Dewi {runId}`, tekan Enter
72. Verifikasi empty state `No results found` tampil di tab Transactions karena tidak ada BRW untuk Borrower `Sari Dewi {runId}`
