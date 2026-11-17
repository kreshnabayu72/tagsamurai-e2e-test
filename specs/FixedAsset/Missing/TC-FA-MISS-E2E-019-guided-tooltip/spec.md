---
id: TC-FA-MISS-E2E-019-guided-tooltip
title: "Guided Tooltip halaman Missing: flag bertahan antar sesi sesudah Done"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "EB-TBL-10": [1, 10, 15, 19, 25, 29, 35, 39, 45, 50, 57]
anchor: [9, 14, 24, 34, 56]
coverage:
  web: automated
---

# Guided Tooltip halaman Missing: flag bertahan antar sesi sesudah Done

## Prerequisites
- Aktor: `Maya Tanjung {runId}`, Total Control, belum pernah menyelesaikan atau melewati Guided Tooltip halaman Missing; lalu `Bayu Ramadhan {runId}`, Total Control, yang Guided Tooltip halaman Missing-nya sudah selesai sebelum spec dimulai; lalu `Sari Wulandari {runId}`, `Dewi Anggraini {runId}`, dan `Hendra Pratama {runId}`, masing-masing Total Control yang belum pernah menyelesaikan atau melewati Guided Tooltip halaman Missing.
- Layar awal: halaman Missing.
- Data:
  - DU-019-1: Pengguna `Maya Tanjung {runId}`, role Total Control, seluruh client, flag Guided Tooltip halaman Missing belum terset.
  - DU-019-2: Pengguna `Bayu Ramadhan {runId}`, role Total Control, seluruh client, flag Guided Tooltip halaman Missing sudah terset.
  - DU-019-3: Pengguna `Sari Wulandari {runId}`, role Total Control, seluruh client, flag Guided Tooltip halaman Missing belum terset.
  - DU-019-4: Pengguna `Dewi Anggraini {runId}`, role Total Control, seluruh client, flag Guided Tooltip halaman Missing belum terset.
  - DU-019-5: Pengguna `Hendra Pratama {runId}`, role Total Control, seluruh client, flag Guided Tooltip halaman Missing belum terset.

## Test Steps

### Tur tampil di kunjungan pertama dan diselesaikan dengan Done
1. Verifikasi tur Guided Tooltip tampil otomatis di halaman Missing
2. Klik `[Next]`
3. Klik `[Next]`
4. Klik `[Next]`
5. Klik `[Done]`
### Flag bertahan sesudah masuk kembali di sesi baru
6. Keluar dari akun
7. Masuk kembali sebagai `Maya Tanjung {runId}`
8. Buka halaman Missing
9. Verifikasi tombol `Scan Found Asset` tampil di halaman Missing
10. Verifikasi tur Guided Tooltip tidak tampil sesudah masuk kembali
### Flag yang sudah terset tidak memunculkan tur
11. Keluar dari akun
12. Masuk sebagai `Bayu Ramadhan {runId}`
13. Buka halaman Missing
14. Verifikasi tombol `Scan Found Asset` tampil di halaman Missing
15. Verifikasi tur Guided Tooltip tidak tampil bagi pengguna dengan flag yang sudah terset
### Tur yang dilewati dengan `[Skip]` tidak tampil lagi
16. Keluar dari akun
17. Masuk sebagai `Sari Wulandari {runId}`
18. Buka halaman Missing
19. Verifikasi tur Guided Tooltip tampil otomatis di halaman Missing
20. Klik `[Skip]`
21. Keluar dari akun
22. Masuk kembali sebagai `Sari Wulandari {runId}`
23. Buka halaman Missing
24. Verifikasi tombol `Scan Found Asset` tampil di halaman Missing
25. Verifikasi tur Guided Tooltip tidak tampil sesudah `[Skip]`
### Tur yang ditutup dengan klik overlay tidak tampil lagi
26. Keluar dari akun
27. Masuk sebagai `Dewi Anggraini {runId}`
28. Buka halaman Missing
29. Verifikasi tur Guided Tooltip tampil otomatis di halaman Missing
30. Klik overlay tur
31. Keluar dari akun
32. Masuk kembali sebagai `Dewi Anggraini {runId}`
33. Buka halaman Missing
34. Verifikasi tombol `Scan Found Asset` tampil di halaman Missing
35. Verifikasi tur Guided Tooltip tidak tampil sesudah klik overlay
### Tur yang ditinggalkan tanpa Skip atau Done tampil lagi di kunjungan berikut
36. Keluar dari akun
37. Masuk sebagai `Hendra Pratama {runId}`
38. Buka halaman Missing
39. Verifikasi tur Guided Tooltip tampil otomatis di halaman Missing
40. Klik `[Next]`
41. Pindah ke tab Assets pada halaman Assets
42. Keluar dari akun
43. Masuk kembali sebagai `Hendra Pratama {runId}`
44. Buka halaman Missing
45. Verifikasi tur Guided Tooltip tampil otomatis lagi di halaman Missing
### Replay dengan `[?]` tidak mereset flag yang sudah terset
46. Keluar dari akun
47. Masuk sebagai `Bayu Ramadhan {runId}`
48. Buka halaman Missing
49. Klik `[?]`
50. Verifikasi tur Guided Tooltip tampil
51. Klik `[Next]`
52. Pindah ke tab Assets pada halaman Assets
53. Keluar dari akun
54. Masuk kembali sebagai `Bayu Ramadhan {runId}`
55. Buka halaman Missing
56. Verifikasi tombol `Scan Found Asset` tampil di halaman Missing
57. Verifikasi tur Guided Tooltip tidak tampil sesudah replay yang ditinggalkan sebelum selesai
