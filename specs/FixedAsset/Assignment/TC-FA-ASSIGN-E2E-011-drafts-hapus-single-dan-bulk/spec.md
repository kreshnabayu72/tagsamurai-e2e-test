---
id: TC-FA-ASSIGN-E2E-011-drafts-hapus-single-dan-bulk
title: "Hapus Draft satu per satu dan bulk"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [TS-ASG-11, TS-ASG-33, "EB-BLK-2@tabel-drafts", EB-BLK-3, EB-EDG-2, "§9.6#r15"]
smoke: []
dependsOn: []
trace:
  TS-ASG-11: [9, 13, 14, 21, 30]
  TS-ASG-33: [36, 37, 60, 63, 64, 65]
  "EB-BLK-2@tabel-drafts": [52, 54, 56]
  EB-BLK-3: [6, 7, 19, 23, 25, 27, 30, 31, 34, 40, 41, 42, 59, 60, 61]
  EB-EDG-2: [15, 17, 19, 34, 49, 45]
  "§9.6#r15": [13, 63]
anchor: [3]
coverage:
  web: automated
---

# Hapus Draft satu per satu dan bulk

## Prerequisites
- Aktor: Asset Admin `Agus Prasetyo {runId}` dengan cakupan Group `Head Office {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-011-1: User `Agus Prasetyo {runId}`, role Asset Admin dengan cakupan Group `Head Office {runId}` saja; ia aktor spec ini.
  - DU-011-2: Group `Head Office {runId}` di dalam cakupan aktor dan Group `Branch Surabaya {runId}` di luar cakupan aktor.
  - DU-011-3: Draft untuk Assignee Division `Tim Satu {runId}` di Group `Head Office {runId}` dengan aset `Meja Kerja Satu {runId}`; dihapus lewat row action `Delete`.
  - DU-011-4: Draft untuk Assignee Division `Tim Alfa {runId}` di Group `Head Office {runId}` dengan aset `Meja Kerja Alfa {runId}`; dihapus lewat bulk dengan satu item.
  - DU-011-5: Draft untuk Assignee Division `Tim Beta {runId}` di Group `Head Office {runId}` dengan aset `Meja Kerja Beta {runId}`; dihapus bersama DU-011-6.
  - DU-011-6: Draft untuk Assignee Division `Tim Gamma {runId}` di Group `Head Office {runId}` dengan aset `Meja Kerja Gamma {runId}`; dihapus bersama DU-011-5.
  - DU-011-7: Draft untuk Assignee Division `Tim Relevan {runId}` di Group `Head Office {runId}` dengan aset `Meja Kerja Relevan {runId}`; dihapus bersama satu Draft di luar cakupan.
  - DU-011-8: Draft untuk Assignee Division `Tim Sisa {runId}` dengan aset `Meja Sisa {runId}` di Group `Head Office {runId}` dan `Lemari Sisa {runId}` di Group `Branch Surabaya {runId}`; sebagian asetnya di luar cakupan aktor sehingga dilewati saat bulk Delete.
  - DU-011-9: Sembilan Draft untuk Assignee Division `Tim Massal {runId} {n}` di Group `Head Office {runId}` dengan aset `Meja Massal {n} {runId}`; dihapus bersama bulk besar.
  - DU-011-10: Empat Draft untuk Assignee Division `Tim Luar {runId} {n}` dengan aset `Meja Luar {n} {runId}` di Group `Head Office {runId}` dan `Lemari Luar {n} {runId}` di Group `Branch Surabaya {runId}`; sebagian asetnya di luar cakupan aktor sehingga dilewati saat bulk Delete.
  - DU-011-11: Draft untuk Assignee Division `Tim Akhir {runId}` di Group `Head Office {runId}` dengan aset `Meja Akhir {runId}`; menjadi satu-satunya Draft pada hasil Search `Tim Akhir {runId}` dan dihapus lewat row action `Delete`.
  - DU-011-12: Urutan pembuatan Draft dari yang pertama: `Tim Akhir {runId}`, `Tim Luar {runId} {n}`, `Tim Massal {runId} {n}`, `Tim Sisa {runId}`, `Tim Relevan {runId}`, `Tim Gamma {runId}`, `Tim Beta {runId}`, `Tim Alfa {runId}`, dan `Tim Satu {runId}`; dengan urutan Last Updated terbaru dulu, `Tim Satu {runId}`, `Tim Alfa {runId}`, `Tim Beta {runId}`, `Tim Gamma {runId}`, `Tim Relevan {runId}`, dan `Tim Sisa {runId}` berada di halaman pertama.

## Test Steps

### Hapus satu Draft lewat row action
1. Klik tab `Drafts`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi tabel memuat 20 Draft milik spec ini dengan laporan `Showing 1 to 10 of 20`
4. Klik `⋯` pada baris `Tim Satu {runId}`
5. Klik `Delete`
6. Verifikasi dialog `Delete Draft` memuat bullet `Tim Satu {runId} · Head Office {runId}` dan teks `This draft will be removed. Are you sure you want to delete it?`
7. Verifikasi dialog memuat tombol `[Go Back]` dan `[Delete]`
8. Klik `[Go Back]`
9. Verifikasi baris `Tim Satu {runId}` masih tampil karena Draft tidak dihapus
10. Klik `⋯` pada baris `Tim Satu {runId}`
11. Klik `Delete`
12. Klik `[Delete]`
13. Verifikasi toast `Success, draft has been deleted.` tampil
14. Verifikasi baris `Tim Satu {runId}` tidak lagi tampil dan laporan menjadi `Showing 1 to 10 of 19`

### Bulk Delete satu item memakai dialog bentuk tunggal
15. Verifikasi bulk action bar tidak tampil saat belum ada Draft terpilih
16. Centang baris `Tim Alfa {runId}`
17. Verifikasi teks `1 Draft selected` tampil
18. Klik `Bulk Action`, lalu klik `Delete`
19. Verifikasi dialog memuat bullet `Tim Alfa {runId} · Head Office {runId}` dan teks `This draft will be removed. Are you sure you want to delete it?` seperti dialog single
20. Klik `[Delete]`
21. Verifikasi toast `Success, draft has been deleted.` tampil dan baris `Tim Alfa {runId}` tidak lagi tampil

### Bulk Delete banyak item dengan konfirmasi klik ganda
22. Centang baris `Tim Beta {runId}` dan baris `Tim Gamma {runId}`
23. Verifikasi teks `2 Drafts selected` tampil
24. Klik `Bulk Action`, lalu klik `Delete`
25. Verifikasi dialog memuat bullet `Tim Beta {runId} · Head Office {runId}` dan `Tim Gamma {runId} · Head Office {runId}` dan teks `These drafts will be removed. Are you sure you want to delete them?`
26. Klik `[Go Back]`
27. Verifikasi teks `2 Drafts selected` masih tampil karena dialog ditutup tanpa menghapus
28. Klik `Bulk Action`, lalu klik `Delete`
29. Klik ganda `[Delete]`
30. Verifikasi toast `Success, draft has been deleted.` tampil satu kali
31. Verifikasi baris `Tim Beta {runId}` dan `Tim Gamma {runId}` tidak lagi tampil dan bulk action bar tidak lagi tampil

### Bulk Delete yang menyisakan satu item relevan
32. Centang baris `Tim Relevan {runId}` dan baris `Tim Sisa {runId}`
33. Klik `Bulk Action`, lalu klik `Delete`
34. Verifikasi dialog hanya memuat bullet `Tim Relevan {runId} · Head Office {runId}` dan teks `This draft will be removed. Are you sure you want to delete it?`
35. Klik `[Delete]`
36. Verifikasi toast `Success, draft has been deleted. Some items were skipped.` tampil
37. Verifikasi baris `Tim Relevan {runId}` tidak lagi tampil dan baris `Tim Sisa {runId}` masih tampil

### Bulk Delete saat semua item tidak bisa diproses
38. Centang baris `Tim Sisa {runId}` dan baris `Tim Luar {runId} 1`
39. Klik `Bulk Action`, lalu klik `Delete`
40. Verifikasi pesan error tampil dan tidak ada Draft yang dihapus karena semua Draft terpilih memuat aset di luar cakupan
41. Verifikasi teks `2 Drafts selected` masih tampil karena seleksi tidak direset
42. Verifikasi baris `Tim Sisa {runId}` dan baris `Tim Luar {runId} 1` masih tampil
43. Klik `×` pada bar seleksi

### Hapus Draft terakhir pada hasil Search
44. Ganti isi kotak search dengan `Tim Akhir {runId}`, tekan Enter
45. Verifikasi tabel memuat tepat satu Draft, yaitu `Tim Akhir {runId}`
46. Klik `⋯` pada baris `Tim Akhir {runId}`
47. Klik `Delete`
48. Klik `[Delete]`
49. Verifikasi empty state `No results found` tampil karena Draft terakhir pada hasil Search sudah terhapus
50. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Select All lintas halaman dan Bulk Delete sebagian dilewati
51. Centang checkbox header kolom Checkbox
52. Verifikasi tombol `Select All (14 records)` tampil karena seluruh Draft yang cocok dengan Search berjumlah 14
53. Klik `Select All (14 records)`
54. Verifikasi teks `14 Drafts selected` dan tombol `Unselect All` tampil
55. Hapus centang pada satu baris di halaman pertama
56. Verifikasi tombol kembali menjadi `Select All (14 records)` dengan jumlah tetap 14
57. Klik `Select All (14 records)`
58. Klik `Bulk Action`, lalu klik `Delete`
59. Verifikasi label `The following will be deleted:` memuat sembilan bullet `Tim Massal {runId} {n} · Head Office {runId}`
60. Verifikasi label `The following will be skipped because they include assets outside your groups:` memuat lima bullet, yaitu `Tim Sisa {runId}` dan empat `Tim Luar {runId} {n}`
61. Verifikasi dialog memuat penutup `Are you sure you want to continue?` dan tombol `[Go Back]` dan `[Continue]`
62. Klik `[Continue]`
63. Verifikasi toast `Success, draft has been deleted. Some items were skipped.` tampil
64. Verifikasi tabel memuat tepat 5 Draft, yaitu `Tim Sisa {runId}` dan empat `Tim Luar {runId} {n}`, tanpa satu pun `Tim Massal {runId} {n}`
65. Verifikasi bulk action bar tidak lagi tampil sesudah aksi ter-commit
