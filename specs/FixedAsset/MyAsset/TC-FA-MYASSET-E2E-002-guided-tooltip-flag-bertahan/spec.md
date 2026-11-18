---
id: TC-FA-MYASSET-E2E-002-guided-tooltip-flag-bertahan
title: "Guided Tooltip My Asset tidak muncul lagi di sesi berikutnya sesudah selesai"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-10": [3, 6, 9, 12, 14, 20, 23, 25, 28, 31, 33, 36, 38]
anchor: [5, 8, 11, 19, 22, 27, 30, 35]
coverage:
  web: automated
---

# Guided Tooltip My Asset tidak muncul lagi di sesi berikutnya sesudah selesai

## Prerequisites
- Aktor: Borrower tanpa pinjaman dan tanpa penugasan, yang belum pernah membuka My Asset. Aktor kedua dan aktor ketiga: Borrower lain dengan akses yang sama, juga belum pernah membuka My Asset.
- Layar awal: halaman FAMS yang memuat navbar.
- Data:
  - DU-002-1: User `Dewi Anggraini {runId}`, Borrower tanpa pinjaman dan tanpa penugasan, belum pernah membuka My Asset.
  - DU-002-2: User `Bagas Prasetyo {runId}`, Borrower tanpa pinjaman dan tanpa penugasan, belum pernah membuka My Asset, belum mengubah preferensi Guided Tooltip.
  - DU-002-5: User `Citra Maharani {runId}`, Borrower tanpa pinjaman dan tanpa penugasan, belum pernah membuka My Asset, flag Guided Tooltip belum disetel.

## Test Steps

### Kunjungan pertama membuka Guided Tooltip otomatis
1. Klik avatar di navbar
2. Klik item `My Asset`
3. Verifikasi Guided Tooltip tampil otomatis di step pertama dengan judul `Confirm what you received`

### Skip menyetel flag dan Guided Tooltip tidak muncul lagi di sesi yang sama
4. Klik `[Skip]`
5. Verifikasi tab `Task` tampil
6. Verifikasi Guided Tooltip tidak tampil

### Flag tersimpan sesudah muat ulang halaman
7. Muat ulang halaman
8. Verifikasi tab `Task` tampil
9. Verifikasi Guided Tooltip tidak tampil

### Flag berlaku di perangkat lain untuk akun yang sama
10. Aktor `Dewi Anggraini {runId}` membuka My Asset dari menu profil pada sesi baru di perangkat lain
11. Verifikasi tab `Task` tampil
12. Verifikasi Guided Tooltip tidak tampil

### Aktor lain tetap mendapat Guided Tooltip pada kunjungan pertamanya
13. Aktor `Bagas Prasetyo {runId}` membuka My Asset dari menu profil
14. Verifikasi Guided Tooltip tampil otomatis di step pertama dengan judul `Confirm what you received`

### Done menyetel flag dan Guided Tooltip tidak muncul lagi sesudah muat ulang halaman
15. Klik `[Next]`
16. Klik `[Next]`
17. Klik `[Next]`
18. Klik `[Done]`
19. Verifikasi tab `Task` tampil
20. Verifikasi Guided Tooltip tidak tampil
21. Muat ulang halaman
22. Verifikasi tab `Task` tampil
23. Verifikasi Guided Tooltip tidak tampil

### Putar ulang lewat `[?]` tidak mereset flag
24. Klik `[?]`
25. Verifikasi Guided Tooltip tampil di step pertama dengan judul `Confirm what you received`
26. Ubah ukuran jendela browser
27. Verifikasi tab `Task` tampil
28. Verifikasi Guided Tooltip tidak tampil
29. Muat ulang halaman
30. Verifikasi tab `Task` tampil
31. Verifikasi Guided Tooltip tidak tampil

### Keluar tanpa selesai tidak menyetel flag
32. Aktor `Citra Maharani {runId}` membuka My Asset dari menu profil
33. Verifikasi Guided Tooltip tampil otomatis di step pertama dengan judul `Confirm what you received`
34. Ubah ukuran jendela browser
35. Verifikasi tab `Task` tampil
36. Verifikasi Guided Tooltip tidak tampil
37. Muat ulang halaman
38. Verifikasi Guided Tooltip tampil otomatis di step pertama dengan judul `Confirm what you received`
