---
id: TC-FA-FASVC-E2E-001-gating-total-control
title: "Gating Total Control: Akses Penuh, Create All groups, dan Aksi Representatif"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#p1", "RA-FASVC-01", "RA-FASVC-02", "RA-FASVC-03", "RA-FASVC-04", "RA-FASVC-05", "FASVC-LOGIC-08a", "FASVC-LOGIC-08d", "FASVC-LOGIC-08e", "FASVC-LOGIC-08f", "FASVC-LOGIC-08g", "§Aturan Logika Modul#p4"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [4, 26, 35]
  "§2.1#r2": 24
  "§2.1#r3": [43, 44, 49, 50, 57, 58]
  "§2.1#r4": [63, 64]
  "§2.1#r5": 9
  "§4.8#r1": 2
  "§4.8#r2": [29, 35]
  "§4.8#r3": 5
  "§4.8#r4": [30, 31, 49]
  "§4.8#r5": [52, 57]
  "§4.8#r6": [32, 63]
  "§4.8#r7": 6
  "§4.8#r8": [7, 12]
  "§4.8#p1": [32, 52]
  "RA-FASVC-01": 29
  "RA-FASVC-02": 30
  "RA-FASVC-03": [33, 52, 55]
  "RA-FASVC-04": [31, 47, 53]
  "RA-FASVC-05": [32, 61]
  "FASVC-LOGIC-08a": [26, 35]
  "FASVC-LOGIC-08d": 24
  "FASVC-LOGIC-08e": 19
  "FASVC-LOGIC-08f": [18, 27]
  "FASVC-LOGIC-08g": [31, 40, 43, 57]
  "§Aturan Logika Modul#p4": [18, 43, 49]
anchor: []
coverage:
  web: automated
---

# Gating Total Control: Akses Penuh, Create All groups, dan Aksi Representatif

## Prerequisites
- Aktor: Total Control.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-001-1: Aktor dengan Role `Total Control`, cakupan seluruh pohon Group, ada di entitas aktor.
  - DU-001-2: Service Center `Servis Pendingin Kota {runId}`, Service type `Routine`, Available to `All groups`, City `Jakarta Selatan`, Company email `layanan@sejukabadi.co.id`, dibuat oleh langkah spec ini dan diubah City-nya menjadi `Jakarta Pusat`. Usage `0`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Menu Service Center tampil dan halaman daftar terbuka
1. Buka menu `Add-ons` pada sidebar
2. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
3. Klik `Service Center`
4. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`

### Toolbar daftar memuat Create, Download, dan Changelog
5. Verifikasi tombol `[+ Service Center]` tampil
6. Verifikasi tombol `[Download]` tampil
7. Verifikasi tombol `[Changelog]` tampil

### Download menyediakan pilihan unduhan
8. Klik `[Download]`
9. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
10. Tutup popover Download

### Changelog gabungan terbuka
11. Klik `[Changelog]`
12. Verifikasi modal `Changelog: Service Center` terbuka
13. Klik ikon close pada modal Changelog

### Create dengan Available to All groups tersimpan dan tampil
14. Klik `[+ Service Center]`
15. Isi Name `Servis Pendingin Kota {runId}`
16. Centang Service type `Routine`
17. Klik field Available to
18. Verifikasi node `All groups` tampil pada tree Available to dan tercentang
19. Verifikasi setiap node pada tree Available to bisa dipilih, tanpa node yang non-selectable
20. Klik `[Cancel]` pada dialog tree Available to
21. Isi City `Jakarta Selatan`
22. Isi Company email `layanan@sejukabadi.co.id`
23. Klik `[Submit]`
24. Verifikasi toast `Success, Servis Pendingin Kota {runId} has been added.` tampil
25. Ketik Search `Servis Pendingin Kota {runId}`, tekan Enter
26. Verifikasi baris `Servis Pendingin Kota {runId}` tampil di tabel
27. Verifikasi kolom Available To pada baris itu menampilkan `All groups`

### Aksi baris dan Detail untuk Service Center All groups yang Active
28. Klik `⋯` pada baris `Servis Pendingin Kota {runId}`
29. Verifikasi aksi `Detail` tampil
30. Verifikasi aksi `Edit` tampil
31. Verifikasi aksi `Inactivate` tampil
32. Verifikasi aksi `Delete` tampil dan tidak disabled
33. Verifikasi aksi `Activate` tidak tampil
34. Klik `Detail`
35. Verifikasi halaman Detail menampilkan nama `Servis Pendingin Kota {runId}`
36. Klik breadcrumb `Service Center`

### Edit Service Center All groups tersimpan
37. Ketik Search `Servis Pendingin Kota {runId}`, tekan Enter
38. Klik `⋯` pada baris `Servis Pendingin Kota {runId}`
39. Klik `Edit`
40. Verifikasi dialog `Edit Service Center` terbuka
41. Ganti isi City dengan `Jakarta Pusat`
42. Klik `[Save]`
43. Verifikasi toast `Success, Servis Pendingin Kota {runId} has been updated.` tampil
44. Verifikasi kolom City pada baris `Servis Pendingin Kota {runId}` menampilkan `Jakarta Pusat`

### Inactivate Service Center All groups
45. Klik `⋯` pada baris `Servis Pendingin Kota {runId}`
46. Klik `Inactivate`
47. Verifikasi dialog `Inactivate Service Center` tampil
48. Klik `[Inactivate]`
49. Verifikasi toast `Success, Servis Pendingin Kota {runId} has been inactivated.` tampil
50. Verifikasi kolom Status pada baris `Servis Pendingin Kota {runId}` menampilkan `Inactive`

### Activate Service Center yang Inactive
51. Klik `⋯` pada baris `Servis Pendingin Kota {runId}`
52. Verifikasi aksi `Activate` tampil dan tidak disabled
53. Verifikasi aksi `Inactivate` tidak tampil
54. Klik `Activate`
55. Verifikasi dialog `Activate Service Center` tampil
56. Klik `[Activate]`
57. Verifikasi toast `Success, Servis Pendingin Kota {runId} has been activated.` tampil
58. Verifikasi kolom Status pada baris `Servis Pendingin Kota {runId}` menampilkan `Active`

### Delete Service Center dengan Usage 0
59. Klik `⋯` pada baris `Servis Pendingin Kota {runId}`
60. Klik `Delete`
61. Verifikasi dialog `Delete Service Center` tampil
62. Klik `[Delete]`
63. Verifikasi toast `Success, Servis Pendingin Kota {runId} has been deleted.` tampil
64. Verifikasi empty state `No results found` tampil untuk Search `Servis Pendingin Kota {runId}`
