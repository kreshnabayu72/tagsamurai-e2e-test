---
id: TC-FA-ASTL-E2E-038-activity-log-hapus-aset-dep-activity-log
title: "Pencatatan Activity Log"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-17y", "§8#r1", "§8#r2", "§8#r3", "§8#r4", "§8#r5", "§8#b3", "§8#b4", "§8#b5", "§8#b6"]
smoke: []
dependsOn: ["Activity Log: tab User Action"]
trace:
  "ASTL-LOGIC-17y": [35, 40]
  "§8#r1": 24
  "§8#r2": 24
  "§8#r3": 25
  "§8#r4": 23
  "§8#r5": 26
  "§8#b3": 27
  "§8#b4": 23
  "§8#b5": [35, 36, 50]
  "§8#b6": [62, 66, 68]
anchor: [39, 61]
coverage:
  web: automated
---

# Pencatatan Activity Log

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-038-1: aset `Server Rack {runId} - 1`, Group `IT {runId}`, Purchase Cost `Rp 52.000.000,00` dari `52000000`, Purchase Complete.
  - DU-038-3: aset `Laptop Pro 16 {runId} - 1`, Group `IT {runId}`.
  - DU-038-4: aset `Proyektor X2 {runId} - 1`, Group `IT {runId}`.
  - DU-038-5: label manual `Aset Kantor {runId}` ada di katalog label.
  - DU-038-6: aset `Tablet Inventaris {runId} - 1`, Group `Cabang Palembang {runId}`, Unmanaged; Available license Cabang Palembang {runId} `0`.
  - DU-038-7: aset `Printer Laser {runId} - 1`, Group `Cabang Palembang {runId}`, managed.
  - DU-038-8: aset `Genset 20kVA {runId} - 1`, Group `Cabang Palembang {runId}`, Unmanaged, Custody `Available`, tidak sedang dalam transaksi berjalan, tanpa penyusutan atau jurnal Posted dan tanpa Disposal, memiliki TAG terpasang, file terlampir, dan baris pada record multi-aset yang sudah selesai.
  - DU-038-9: aset `Meja Rapat {runId} - 1`, Group `Cabang Palembang {runId}`, Unmanaged, Custody `Available`, tidak sedang dalam transaksi berjalan, tanpa penyusutan atau jurnal Posted dan tanpa Disposal.
  - DU-038-10: aset `Kursi Kerja {runId} - 1`, Group `Cabang Palembang {runId}`, Unmanaged, Custody `Available`, tidak sedang dalam transaksi berjalan, tanpa penyusutan atau jurnal Posted dan tanpa Disposal.

## Test Steps

### Aksi tulis pada aset tercatat di Activity Log
1. Ketik Search `{runId}`, tekan Enter
2. Buka menu `⋯` baris `Server Rack {runId} - 1`
3. Klik `Edit Purchase`
4. Isi Purchase Cost `55000000`
5. Klik `[Save]`
6. Centang baris `Laptop Pro 16 {runId} - 1`
7. Centang baris `Proyektor X2 {runId} - 1`
8. Klik Bulk Action `Add Label`
9. Pilih label `Aset Kantor {runId}`
10. Klik `[Apply]`
11. Klik `×` pada bar Bulk untuk membatalkan seleksi
12. Centang baris `Laptop Pro 16 {runId} - 1`
13. Centang baris `Proyektor X2 {runId} - 1`
14. Klik Bulk Action `Remove Label`
15. Pilih label `Aset Kantor {runId}`
16. Klik `[Apply]`
17. Klik `×` pada bar Bulk untuk membatalkan seleksi
18. Buka menu `⋯` baris `Tablet Inventaris {runId} - 1`
19. Klik `Manage`
20. Centang baris `Printer Laser {runId} - 1` pada dialog `Switch Manage Asset`
21. Klik `[Switch]`
22. Buka Activity Log FAMS tab User Action
23. Verifikasi tab User Action memuat entri untuk aksi `Edit Purchase` atas `Server Rack {runId} - 1`, `Add Label` dan `Remove Label` atas `Laptop Pro 16 {runId} - 1` dan `Proyektor X2 {runId} - 1`, serta `Manage` atas `Tablet Inventaris {runId} - 1` dan `Switch Manage` atas `Printer Laser {runId} - 1`
24. Verifikasi entri-entri tersebut dicatat dengan entity `Asset` dan object path `Asset`
25. Verifikasi entri `Edit Purchase` memuat field `Purchase Cost` dan entri `Add Label` serta `Remove Label` memuat field `Label`
26. Verifikasi aksi `Add Label` massal atas dua aset menghasilkan satu entri untuk `Laptop Pro 16 {runId} - 1` dan satu entri untuk `Proyektor X2 {runId} - 1`
27. Verifikasi System Log aktor memuat entri untuk aksi `Manage` atas `Tablet Inventaris {runId} - 1` dan `Switch Manage` atas `Printer Laser {runId} - 1`

### Delete Asset Data satu aset tercatat di User Action
28. Kosongkan kolom Search
29. Ketik Search `Genset 20kVA {runId}`, tekan Enter
30. Buka menu `⋯` baris `Genset 20kVA {runId} - 1`
31. Klik `Delete Asset Data`
32. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
33. Klik `[Delete]`
34. Buka Activity Log FAMS tab User Action
35. Verifikasi tab User Action memuat satu entri `Delete Asset Data` untuk `Genset 20kVA {runId} - 1` yang berisi Asset ID milik DU-038-8, nama aset `Genset 20kVA {runId} - 1`, aktor Hendra Saputra, dan waktu hapus
36. Verifikasi tab User Action tidak memuat entri lain atas `Genset 20kVA {runId} - 1`, sehingga pelepasan TAG, penghapusan file terlampir, dan pengeluaran baris dari record modul lain tidak menulis entri tersendiri
37. Buka Fixed Asset > Assets (tab Assets)
38. Klik ikon `Changelog` pada toolbar
39. Verifikasi modal Changelog memuat entri milik `Server Rack {runId} - 1`
40. Verifikasi modal Changelog tidak memuat entri apa pun untuk `Genset 20kVA {runId} - 1`, termasuk entri penghapusan
41. Tutup modal Changelog

### Delete Asset Data massal satu entri per aset
42. Kosongkan kolom Search
43. Ketik Search `{runId}`, tekan Enter
44. Centang baris `Meja Rapat {runId} - 1`
45. Centang baris `Kursi Kerja {runId} - 1`
46. Klik Bulk Action `Delete Asset Data`
47. Centang `I understand that the asset data, all its logs, and all its attachments will be permanently deleted.`
48. Klik `[Delete]`
49. Buka Activity Log FAMS tab User Action
50. Verifikasi tab User Action memuat satu entri `Delete Asset Data` untuk `Meja Rapat {runId} - 1` dan satu entri untuk `Kursi Kerja {runId} - 1`, masing-masing berisi Asset ID, nama aset, aktor Hendra Saputra, dan waktu hapus

### Melihat, membuka, mengunduh, dan mencetak label tidak dicatat
51. Buka Fixed Asset > Assets (tab Assets)
52. Ketik Search `Server Rack {runId}`, tekan Enter
53. Klik kolom `Name` baris `Server Rack {runId} - 1`
54. Kembali ke daftar Fixed Asset > Assets
55. Klik `Download`
56. Pilih `Download as CSV`
57. Buka menu `⋯` baris `Server Rack {runId} - 1`
58. Klik `Print Label`
59. Klik `[Start Print]`
60. Buka Activity Log FAMS tab User Action
61. Verifikasi tab User Action memuat entri `Edit Purchase` atas `Server Rack {runId} - 1`
62. Verifikasi tab User Action tidak memuat entri baru atas `Server Rack {runId} - 1` untuk aksi membuka detail, Download, maupun Print Label

### Membuka detail, Download, dan Print Label tidak ada di Changelog Asset dan System Log
63. Buka Fixed Asset > Assets (tab Assets)
64. Ketik Search `Server Rack {runId}`, tekan Enter
65. Klik ikon `Changelog` pada toolbar
66. Verifikasi modal Changelog tidak memuat entri atas `Server Rack {runId} - 1` untuk aksi membuka detail, Download, maupun Print Label
67. Tutup modal Changelog
68. Verifikasi System Log aktor tidak memuat entri atas `Server Rack {runId} - 1` untuk aksi membuka detail, Download, maupun Print Label
