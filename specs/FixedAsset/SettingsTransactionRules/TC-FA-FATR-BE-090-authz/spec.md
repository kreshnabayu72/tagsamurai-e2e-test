---
id: TC-FA-FATR-BE-090-authz
title: "Authz per role dan cakupan Group"
layer: be-e2e
priority: Critical
caseType: Negative
status: draft
owner: BE
sourceRules: ["§2#p2", "§9.2#b1", "§9.2#b82", "§9.2#b126", "§9.2#b139", "§9.2#b156", "§9.2#b160", "§9.2#b307", "§9.2#b341", "§9.3#b1", "§9.3#b3", "§9.4.1#r16", "§9.4.1#r17", "§9.4.1#r18", "§9.4.1#r19", "§9.4.2#r3", "§9.4.2#r23", "§9.4.2#r30", "§9.4.3#b5", "§9.4.4#r1", "§9.4.4#r24", "§9.4.4#r25", "§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#r5", "§9.11#r6", "§9.11#r7", "§9.11#r8", "§9.11#r9", "§9.11#r10", "§10#b4", "§11#r1", EB-AKS-3@save-changes, EB-AKS-3@add-override, EB-AKS-3@delete-override]
smoke: []
dependsOn: []
trace:
  "§2#p2": [9, 17, 26, 50, 67]
  "§9.2#b1": [3, 5, 7]
  "§9.2#b82": [36, 52]
  "§9.2#b126": 90
  "§9.2#b139": [75, 80, 86, 106, 109]
  "§9.2#b156": [32, 40]
  "§9.2#b160": [63, 73, 77]
  "§9.2#b307": [98, 100]
  "§9.2#b341": 103
  "§9.3#b1": [7, 13, 38, 44, 52]
  "§9.3#b3": [3, 24, 96]
  "§9.4.1#r16": [3, 5, 7, 13]
  "§9.4.1#r17": [24, 28, 30, 34, 44, 84]
  "§9.4.1#r18": [36, 38, 52, 69, 71, 88]
  "§9.4.1#r19": [65, 73, 75]
  "§9.4.2#r3": 10
  "§9.4.2#r23": [22, 24, 32]
  "§9.4.2#r30": 63
  "§9.4.3#b5": [32, 34, 73]
  "§9.4.4#r1": 11
  "§9.4.4#r24": [22, 41, 42]
  "§9.4.4#r25": [73, 81, 82]
  "§9.11#r1": [15, 19]
  "§9.11#r2": [73, 92]
  "§9.11#r3": 94
  "§9.11#r4": [98, 102]
  "§9.11#r5": [54, 60, 90]
  "§9.11#r6": [40, 44, 46, 50, 84]
  "§9.11#r7": [52, 58, 71, 88]
  "§9.11#r8": 56
  "§9.11#r9": [48, 86]
  "§9.11#r10": [28, 30, 65]
  "§10#b4": [13, 19]
  "§11#r1": 13
  EB-AKS-3@save-changes: 3
  EB-AKS-3@add-override: 22
  EB-AKS-3@delete-override: 63
---
# Authz per role dan cakupan Group

## Prerequisites
- Aktor: Maya Pengelola (DU-090-1), Total Control; Dewi Bawaan (DU-090-2), Default User; Tono Setelan (DU-090-3) dan Lina Baca Setelan (DU-090-4), pemegang Global Role Manage transaction settings; Sari Penata (DU-090-5) dan Gita Baca Aset (DU-090-6), pemegang Group Role Manage asset & TAG pada Group `Tim Survei {runId}`; Rafi Baca (DU-090-7), Read Only; Wati Gabungan (DU-090-8), gabungan Global Role dan Group Role; Hendra Tanpa Akses (DU-090-9).
- Data:
  - DU-090-1: User, pengelola Total Control: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`.
  - DU-090-2: User, pengguna Default User: Name `Dewi Bawaan {runId}`; Access Level `Default User`; Cakupan `seluruh Group`.
  - DU-090-3: User, pemegang Global Role Manage transaction settings (Read, Update) tanpa Total Control: Name `Tono Setelan {runId}`; Global Role `Manage transaction settings (Read, Update)`; Cakupan `seluruh entitas`.
  - DU-090-4: User, pemegang Global Role Manage transaction settings (Read): Name `Lina Baca Setelan {runId}`; Global Role `Manage transaction settings (Read)`; Cakupan `seluruh entitas`.
  - DU-090-5: User, pemegang Group Role Manage asset & TAG (Read, Update) pada satu Group: Name `Sari Penata {runId}`; Group Role `Manage asset & TAG (Read, Update)`; Cakupan `Group Tim Survei {runId} beserta turunannya`.
  - DU-090-6: User, pemegang Group Role Manage asset & TAG (Read) pada satu Group: Name `Gita Baca Aset {runId}`; Group Role `Manage asset & TAG (Read)`; Cakupan `Group Tim Survei {runId} beserta turunannya`.
  - DU-090-7: User, pengguna Read Only yang tetap memegang peran Update: Name `Rafi Baca {runId}`; Access Level `Read Only`; Global Role `Manage transaction settings (Read, Update)`; Group Role `Manage asset & TAG (Read, Update)`; Cakupan `Group Tim Survei {runId} beserta turunannya`.
  - DU-090-8: User, pengguna dengan gabungan Global Role dan Group Role: Name `Wati Gabungan {runId}`; Global Role `Manage transaction settings (Read, Update)`; Group Role `Manage asset & TAG (Read, Update)`; Cakupan `Group Tim Survei {runId} beserta turunannya`.
  - DU-090-9: User, pengguna tanpa peran yang memberi akses halaman: Name `Hendra Tanpa Akses {runId}`; Peran `tanpa Global Role dan Group Role yang memberi akses halaman`.
  - DU-090-10: Category, Category leaf untuk Save per role: Name `Perangkat Otorisasi {runId}`.
  - DU-090-11: Category, Category leaf untuk override per role: Name `Peralatan Otorisasi {runId}`.
  - DU-090-12: Group, Group tempat Sari Penata berhak: Name `Tim Survei {runId}`.
  - DU-090-13: Group, Group turunan Tim Survei dalam cakupan Sari Penata: Name `Seksi Survei {runId}`; Parent `Tim Survei {runId}`.
  - DU-090-14: Group, Group di luar cakupan Sari Penata: Name `Tim Lapangan {runId}`.
  - DU-090-15: Group, Group yang sudah dihapus sehingga override-nya tampil tidak berlaku: Name `Tim Dihapus Otorisasi {runId}`.
  - DU-090-16: Group, Group turunan Tim Survei yang override-nya dihapus Sari Penata: Name `Tim Hapus Dalam {runId}`; Parent `Tim Survei {runId}`.
  - DU-090-17: Group, Group target Add override oleh Default User: Name `Tim Dewi {runId}`.
  - DU-090-18: Asset, aset di Group dalam cakupan Sari Penata: Name `Drone Survei {runId}`; Asset Name `Drone Ukur {runId}`; Category `Peralatan Otorisasi {runId}`; Group `Tim Survei {runId}`.
  - DU-090-19: Asset, aset di Group di luar cakupan Sari Penata: Name `Drone Lapangan {runId}`; Asset Name `Drone Ukur {runId}`; Category `Peralatan Otorisasi {runId}`; Group `Tim Lapangan {runId}`.
  - DU-090-20: Asset, aset di Group dalam cakupan yang kemudian dipindah ke Group di luar cakupan: Name `Drone Pindah {runId}`; Asset Name `Drone Ukur {runId}`; Category `Peralatan Otorisasi {runId}`; Group `Tim Survei {runId}`.
  - DU-090-21: Asset, aset target Asset Name override oleh Default User: Name `Drone Dua {runId}`; Asset Name `Drone Ukur Dua {runId}`; Category `Peralatan Otorisasi {runId}`; Group `Tim Lapangan {runId}`.
  - DU-090-22: Asset, aset target Asset Name override yang dihapus: Name `Drone Hapus {runId}`; Asset Name `Drone Ukur Hapus {runId}`; Category `Peralatan Otorisasi {runId}`; Group `Tim Lapangan {runId}`.
  - DU-090-23: Override, override Group dalam cakupan Sari Penata: Scope `Group`; Target `Tim Survei {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-24: Override, override Group di luar cakupan Sari Penata: Scope `Group`; Target `Tim Lapangan {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-25: Override, override aset di luar cakupan Sari Penata: Scope `aset`; Target `Drone Lapangan {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-26: Override, override aset yang kelak dipindah ke Group di luar cakupan: Scope `aset`; Target `Drone Pindah {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-27: Override, override pada Group yang sudah dihapus, tampil tidak berlaku: Scope `Group`; Target `Tim Dihapus Otorisasi {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-090-28: Override, override Asset Name yang dihapus pemegang Update Manage transaction settings: Scope `Asset Name`; Target `Drone Ukur Hapus {runId}`; Category `All categories`; Transaksi `peminjaman`; Field `Max duration`; Value `5`.
  - DU-090-29: Override, override Group dalam cakupan yang dihapus Sari Penata: Scope `Group`; Target `Tim Hapus Dalam {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-30 sampai DU-090-34 adalah nilai input Save dan Add override di langkah masing-masing, bukan record yang sudah ada.
  - DU-090-35: Group, Group turunan Tim Survei yang kemudian dipindah ke luar cakupan Sari Penata: Name `Tim Pindah Otorisasi {runId}`; Parent `Tim Survei {runId}`.
  - DU-090-36: Override, override Group pada Group yang kemudian dipindah ke luar cakupan: Scope `Group`; Target `Tim Pindah Otorisasi {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
  - DU-090-37: Group, Group turunan Tim Lapangan yang kemudian dipindah ke dalam cakupan Sari Penata: Name `Tim Masuk Otorisasi {runId}`; Parent `Tim Lapangan {runId}`.
  - DU-090-38: Override, override Group pada Group yang kemudian dipindah ke dalam cakupan: Scope `Group`; Target `Tim Masuk Otorisasi {runId}`; Category `Peralatan Otorisasi {runId}`; Transaksi `penugasan`; Field `Allow Assign`; Value `Deny`.
- Kondisi:
  - Seluruh field Category `Perangkat Otorisasi {runId}` dan Category `Peralatan Otorisasi {runId}` bernilai Inherit sebelum spec dijalankan.
  - Plan entitas menempatkan Feature Suite Transfer pada level `None`, sehingga tab Transfer tidak dapat dibuka oleh role mana pun.
  - Override pada Group `Tim Dihapus Otorisasi {runId}` tampil sebagai tidak berlaku karena Group-nya sudah dihapus.
  - Jumlah entri Changelog dan Activity Log serta versi setting dibaca sebagai selisih terhadap nilai yang dicatat sebelum aksi.

## Test Steps

### Save dari role tanpa hak Update ditolak server walau UI dilewati
1. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log serta versi setting
2. Lina Baca Setelan mengirim langsung ke server Save Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `2`
3. Verifikasi Save dari Lina Baca Setelan ditolak, server menolak aksi tulis dari aktor tanpa capability walau UI dilewati, dan data tidak berubah
4. Gita Baca Aset mengirim langsung ke server Save Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `2`
5. Verifikasi Save dari Gita Baca Aset ditolak karena role ini bukan Total Control dan bukan pemegang Update Global Role Manage transaction settings
6. Sari Penata mengirim langsung ke server Save Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `2`
7. Verifikasi Save dari Sari Penata ditolak, karena hak Update Group Role Manage asset & TAG hanya untuk override dan bukan untuk ubah setting
8. Rafi Baca mengirim langsung ke server Save Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `2`
9. Verifikasi Save dari Rafi Baca ditolak walau ia memegang peran Update, karena tingkat akses Read Only membatasi seluruh haknya menjadi Read saja
10. Verifikasi Max extensions Category `Perangkat Otorisasi {runId}` tetap Inherit setelah keempat Save itu
11. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, karena aksi yang ditolak tidak dicatat

### Save dari Total Control, Default User, dan pemegang Update Manage transaction settings diterima
12. Tono Setelan menyimpan Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `2`
13. Verifikasi Save dari Tono Setelan diterima dan Max extensions Category `Perangkat Otorisasi {runId}` menjadi `2`, karena pemegang Update Global Role Manage transaction settings berhak mengubah setting
14. Dewi Bawaan menyimpan Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `3`
15. Verifikasi Save dari Dewi Bawaan diterima dan Max extensions Category `Perangkat Otorisasi {runId}` menjadi `3`, karena Default User setara Total Control
16. Wati Gabungan menyimpan Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `4`
17. Verifikasi Save dari Wati Gabungan diterima dan Max extensions Category `Perangkat Otorisasi {runId}` menjadi `4`, karena haknya adalah gabungan dari semua perannya
18. Maya Pengelola menyimpan Category `Perangkat Otorisasi {runId}` dengan Max extensions nilai sendiri `1`
19. Verifikasi Save dari Maya Pengelola diterima dan Max extensions Category `Perangkat Otorisasi {runId}` menjadi `1`, karena Total Control berhak mengubah setting

### Add override dari role tanpa hak atau di luar cakupan ditolak server walau UI dilewati
20. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log, versi setting, dan jumlah override Category `Peralatan Otorisasi {runId}`
21. Lina Baca Setelan mengirim langsung ke server Add override Group `Tim Dewi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
22. Verifikasi Add override dari Lina Baca Setelan ditolak, server menolak aksi tulis dari aktor tanpa capability walau UI dilewati, dan data tidak berubah
23. Gita Baca Aset mengirim langsung ke server Add override Group `Seksi Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
24. Verifikasi Add override dari Gita Baca Aset ditolak, karena Group Role Manage asset & TAG (Read) tidak memberi hak membuat override, walau UI dan server divalidasi independen
25. Rafi Baca mengirim langsung ke server Add override Group `Seksi Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
26. Verifikasi Add override dari Rafi Baca ditolak walau ia memegang peran Update, karena tingkat akses Read Only membatasi haknya menjadi Read saja
27. Tono Setelan mengirim langsung ke server Add override Group `Tim Dewi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
28. Verifikasi Add override Group dari Tono Setelan ditolak, karena pemegang Update Global Role Manage transaction settings tanpa Total Control tidak memiliki cakupan tulis pada Group override
29. Tono Setelan mengirim langsung ke server Add override aset `Drone Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
30. Verifikasi Add override aset dari Tono Setelan ditolak, karena ia tidak memiliki cakupan tulis pada override aset
31. Sari Penata mengirim langsung ke server Add override Group `Tim Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
32. Verifikasi Add override Group dari Sari Penata ditolak karena Group target di luar cakupan perannya
33. Sari Penata mengirim langsung ke server Add override aset `Drone Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
34. Verifikasi Add override aset dari Sari Penata ditolak karena aset berada di Group di luar cakupan perannya
35. Sari Penata mengirim langsung ke server Add override Asset Name `Drone Ukur {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `5`
36. Verifikasi Add override Asset Name dari Sari Penata ditolak, karena Asset Name override hanya untuk Total Control atau pemegang Update Global Role Manage transaction settings
37. Lina Baca Setelan mengirim langsung ke server Add override Asset Name `Drone Ukur {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `5`
38. Verifikasi Add override Asset Name dari Lina Baca Setelan ditolak, karena Global Role Manage transaction settings (Read) tidak memberi hak Update
39. Wati Gabungan mengirim langsung ke server Add override Group `Tim Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
40. Verifikasi Add override dari Wati Gabungan ditolak, karena penggabungan perannya tidak memperluas cakupan Group role ke Group di luar Group-nya
41. Verifikasi jumlah override Category `Peralatan Otorisasi {runId}` tidak bertambah dari yang dicatat
42. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah seluruh Add override yang ditolak

### Add override dari role yang berhak dan dalam cakupannya diterima
43. Sari Penata menambahkan override Group `Tim Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
44. Verifikasi override Group `Tim Survei {runId}` terbuat, karena Group itu dalam cakupan Group role Sari Penata
45. Sari Penata menambahkan override Group `Seksi Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
46. Verifikasi override Group `Seksi Survei {runId}` terbuat, karena cakupan Group role mencakup Group turunannya
47. Sari Penata menambahkan override aset `Drone Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
48. Verifikasi override aset `Drone Survei {runId}` terbuat, karena aset berada di Group dalam cakupan Group role Sari Penata
49. Wati Gabungan menambahkan override Group `Tim Hapus Dalam {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
50. Verifikasi override Group `Tim Hapus Dalam {runId}` terbuat, karena Group role Wati Gabungan berlaku bersama Global Role-nya
51. Tono Setelan menambahkan override Asset Name `Drone Ukur {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `5`
52. Verifikasi override Asset Name `Drone Ukur {runId}` terbuat, karena pemegang Update Global Role Manage transaction settings berhak atas Asset Name override
53. Dewi Bawaan menambahkan override Group `Tim Dewi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
54. Verifikasi override Group `Tim Dewi {runId}` terbuat, karena Default User berhak atas semua Group
55. Dewi Bawaan menambahkan override aset `Drone Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
56. Verifikasi override aset `Drone Lapangan {runId}` terbuat, karena Default User berhak atas semua aset
57. Dewi Bawaan menambahkan override Asset Name `Drone Ukur Dua {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `5`
58. Verifikasi override Asset Name `Drone Ukur Dua {runId}` terbuat, karena Default User berhak atas Asset Name override
59. Maya Pengelola menambahkan override Group `Tim Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman dengan Max duration `5`
60. Verifikasi override Group `Tim Lapangan {runId}` terbuat, karena Total Control berhak atas semua Group

### Delete override dari role tanpa hak atau di luar cakupan ditolak server, baris maupun bulk
61. Maya Pengelola mencatat jumlah entri Changelog dan Activity Log, versi setting, dan jumlah override Category `Peralatan Otorisasi {runId}`
62. Gita Baca Aset mengirim langsung ke server Delete override Group `Tim Hapus Dalam {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
63. Verifikasi Delete dari Gita Baca Aset ditolak, server menolak aksi tulis dari aktor tanpa capability walau UI dilewati, dan data tidak berubah
64. Tono Setelan mengirim langsung ke server Delete override Group `Tim Hapus Dalam {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
65. Verifikasi Delete dari Tono Setelan ditolak, karena ia tidak memiliki cakupan tulis pada Group override
66. Rafi Baca mengirim langsung ke server Delete override Group `Tim Hapus Dalam {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
67. Verifikasi Delete dari Rafi Baca ditolak walau ia memegang peran Update, karena tingkat akses Read Only membatasi haknya menjadi Read saja
68. Lina Baca Setelan mengirim langsung ke server Delete override Asset Name `Drone Ukur Hapus {runId}` untuk All categories pada transaksi peminjaman
69. Verifikasi Delete dari Lina Baca Setelan ditolak, karena Global Role Manage transaction settings (Read) tidak memberi hak Update
70. Sari Penata mengirim langsung ke server Delete override Asset Name `Drone Ukur Hapus {runId}` untuk All categories pada transaksi peminjaman
71. Verifikasi Delete dari Sari Penata ditolak, karena Asset Name override hanya untuk Total Control atau pemegang Update Global Role Manage transaction settings
72. Sari Penata mengirim langsung ke server Delete override Group `Tim Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
73. Verifikasi Delete dari Sari Penata ditolak karena override berada di luar cakupan perannya, dan override Group `Tim Lapangan {runId}` untuk transaksi penugasan masih ada
74. Sari Penata mengirim langsung ke server Delete override aset `Drone Lapangan {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
75. Verifikasi Delete dari Sari Penata ditolak karena aset berada di Group di luar cakupan perannya
76. Gita Baca Aset mengirim langsung ke server bulk Delete override Group `Tim Survei {runId}` dan Group `Tim Lapangan {runId}` untuk transaksi penugasan
77. Verifikasi bulk Delete dari Gita Baca Aset ditolak seluruhnya dan kedua override masih ada
78. Maya Pengelola memindahkan aset `Drone Pindah {runId}` ke Group `Tim Lapangan {runId}`
79. Sari Penata mengirim langsung ke server Delete override aset `Drone Pindah {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
80. Verifikasi Delete dari Sari Penata ditolak dan override aset `Drone Pindah {runId}` masih ada, karena hak Delete mengikuti Group aset saat ini menurut cakupan role
81. Verifikasi jumlah override Category `Peralatan Otorisasi {runId}` tidak berkurang dari yang dicatat
82. Verifikasi Changelog dan Activity Log tidak bertambah entri dan versi setting tidak naik dari yang dicatat, setelah seluruh Delete override yang ditolak

### Delete override dari role yang berhak dan dalam cakupannya diterima
83. Sari Penata menghapus override Group `Tim Hapus Dalam {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
84. Verifikasi override itu terhapus, karena Group-nya dalam cakupan Group role Sari Penata
85. Sari Penata menghapus override aset `Drone Survei {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman
86. Verifikasi override itu terhapus, karena hak Delete mengikuti Group aset `Drone Survei {runId}` yang masih dalam cakupan perannya
87. Tono Setelan menghapus override Asset Name `Drone Ukur Hapus {runId}` untuk All categories pada transaksi peminjaman
88. Verifikasi override itu terhapus, karena pemegang Update Global Role Manage transaction settings berhak atas Asset Name override
89. Maya Pengelola menghapus override Group `Tim Dihapus Otorisasi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi peminjaman, yang tampil tidak berlaku
90. Verifikasi override itu terhapus dengan aturan Delete yang sama seperti baris lain, karena Total Control berhak atas scope-nya

### Semua role yang bisa melihat halaman membaca override dan Changelog, dan mengekspor aturan
91. Gita Baca Aset membuka daftar override Category `Peralatan Otorisasi {runId}`
92. Verifikasi daftar memuat override Group `Tim Lapangan {runId}` yang berada di luar Group Gita Baca Aset, karena semua override semua Category dilihat semua role yang punya akses halaman
93. Lina Baca Setelan membuka Changelog
94. Verifikasi Changelog memuat entri Save Category `Perangkat Otorisasi {runId}` yang dibuat Tono Setelan, Dewi Bawaan, Wati Gabungan, dan Maya Pengelola, aktor lain selain Lina Baca Setelan, karena semua entri dilihat semua role yang punya akses halaman
95. Hendra Tanpa Akses mengirim langsung ke server permintaan membaca daftar override Category `Peralatan Otorisasi {runId}`
96. Verifikasi permintaan itu ditolak dan tidak ada data override yang dikembalikan, karena pembacaan data tetap menerapkan filter cakupan di server walau elemen UI disembunyikan
97. Gita Baca Aset menjalankan Export rules pada Category `Peralatan Otorisasi {runId}` dari tab peminjaman
98. Verifikasi berkas Export rules terunduh, karena Export rules tersedia untuk semua role yang bisa melihat halaman
99. Lina Baca Setelan menjalankan Export rules pada Category `Peralatan Otorisasi {runId}` dari tab penugasan
100. Verifikasi berkas Export rules terunduh dari tab mana pun
101. Rafi Baca menjalankan Export rules pada Category `Peralatan Otorisasi {runId}`
102. Verifikasi berkas Export rules terunduh untuk pengguna Read Only
103. Verifikasi berkas itu tidak memuat aturan transaksi yang tabnya tidak dapat dibuka, karena transaksi seperti itu tidak diekspor

### Hak Delete override Group mengikuti posisi Group target saat ini
104. Maya Pengelola memindahkan Group `Tim Pindah Otorisasi {runId}` menjadi turunan Group `Tim Lapangan {runId}`
105. Sari Penata mengirim langsung ke server Delete override Group `Tim Pindah Otorisasi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
106. Verifikasi Delete dari Sari Penata ditolak dan override Group `Tim Pindah Otorisasi {runId}` masih ada, karena hak Delete mengikuti posisi Group target saat ini yang kini di luar cakupan perannya
107. Maya Pengelola memindahkan Group `Tim Masuk Otorisasi {runId}` menjadi turunan Group `Tim Survei {runId}`
108. Sari Penata menghapus override Group `Tim Masuk Otorisasi {runId}` pada Category `Peralatan Otorisasi {runId}` untuk transaksi penugasan
109. Verifikasi override itu terhapus, karena hak Delete mengikuti posisi Group target saat ini yang kini dalam cakupan perannya
