---
id: TC-FA-FAREG-BE-146-usage-event-dep-handheld-reader
title: "Handheld Usage Event Registration Scan"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.4#p1", "§8.4#r1", "§8.4#r2", "§8.4#r3", "§8.4#r4", "§8.4#r5", "§8.4#r6", "§8.4#b1", "§8.4#b2", "§8.4#b3", "§8.4#p4"]
smoke: []
dependsOn:
  - "Handheld Reader: Tab Usage"
owner: BE
trace:
  "§8.4#p1": 9
  "§8.4#r1": [16, 41, 49, 61, 62, 67, 68]
  "§8.4#r2": 10
  "§8.4#r3": 11
  "§8.4#r4": 12
  "§8.4#r5": [13, 40, 48, 61, 67]
  "§8.4#r6": 14
  "§8.4#b1": [9, 55, 56]
  "§8.4#b2": [9, 21, 27]
  "§8.4#b3": [7, 15]
  "§8.4#p4": [33, 40, 42]
---

# Handheld Usage Event Registration Scan

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Cirebon {runId}`) sebagai pemegang kunci sesi edit.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Cirebon {runId}`).
- Data:
  - DU-146-1: Group `Gudang Cirebon {runId}`, ada di entitas aktor.
  - DU-146-2: Handheld Reader `Reader Gudang {runId}` yang terdaftar di Global Settings dan dipakai Rina W.
  - DU-146-3: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-146-4: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `3`.
  - DU-146-5: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-146-6: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `1`, aset pertama sudah ber-Tag `E280-1460-0004 {runId}`.
  - DU-146-7: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-146-8: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `2`.
  - DU-146-9: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `1`.
  - DU-146-17: Handheld Reader `Reader Kantor {runId}` yang terdaftar di Global Settings dan dipakai Rina W.
  - DU-146-18: batch Draft milik Rina W di Group `Gudang Cirebon {runId}`, Item `Laptop {runId}` Quantity `2`.
  - DU-146-19: Group `Gudang Cirebon Approval {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-146-20: Group `Gudang Cirebon Langsung {runId}`, ber-toggle `Require Approval for Registration` OFF, ada di entitas aktor.
  - DU-146-21: batch Draft milik Rina W di Group `Gudang Cirebon Approval {runId}`, Item `Laptop {runId}` Quantity `1`, memenuhi Tingkat 2 selain slot Tag.
  - DU-146-22: batch Draft milik Rina W di Group `Gudang Cirebon Langsung {runId}`, Item `Laptop {runId}` Quantity `1`, memenuhi Tingkat 2 selain slot Tag.
- Kondisi:
  - Tag yang dipindai terdaftar di registri Global dengan status `Available`, kecuali Tag `E280-9999-1460 {runId}` yang tidak ada di registri Global.
  - kuota Group `Gudang Cirebon Approval {runId}` dan `Gudang Cirebon Langsung {runId}` serta kuota tenant cukup.

## Test Steps

### Satu event per pasangan reader dan sesi edit, ditulis saat kunci dilepas
1. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
2. Rina W membuka form batch DU-146-4 sehingga memegang kunci sesi edit
3. Rina W memindai Tag `E280-1460-0001 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
4. Rina W memindai Tag `E280-1460-0002 {runId}` pada aset kedua lewat Reader `Reader Gudang {runId}`
5. Rina W memindai Tag `E280-1460-0003 {runId}` pada aset ketiga lewat Reader `Reader Gudang {runId}`
6. Rina W menyimpan batch DU-146-4
7. Verifikasi jumlah event di Tab Usage belum bertambah dibanding catatan karena Save tidak melepas kunci sesi edit
8. Rina W keluar dari form batch DU-146-4 sehingga kunci sesi edit dilepas
9. Verifikasi tepat satu event baru tercatat di Tab Usage, bukan tiga, walau tiga Tag terpasang lewat Reader dalam sesi itu
10. Verifikasi event itu memuat Reader `Reader Gudang {runId}`
11. Verifikasi event itu memuat Product `Fixed Asset`
12. Verifikasi event itu memuat Event Type `Registration Scan`
13. Verifikasi event itu memuat PIC `Rina W` sebagai pemegang kunci sesi
14. Verifikasi event itu memuat Transaction ID kosong yang tampil `—` karena sesi edit adalah sesi Draft
15. Verifikasi event itu tidak memuat jumlah Tag
16. Verifikasi event itu memuat Date sama dengan waktu kunci sesi edit dilepas saat Rina W keluar dari form

### Sesi tanpa Tag terpasang lewat reader tidak menghasilkan event
17. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
18. Rina W membuka form batch DU-146-5 sehingga memegang kunci sesi edit
19. Rina W memindai Tag `E280-9999-1460 {runId}` yang tidak dikenal lewat Reader `Reader Gudang {runId}`
20. Rina W keluar dari form batch DU-146-5 sehingga kunci sesi edit dilepas
21. Verifikasi jumlah event di Tab Usage sama dengan catatan karena scan yang gagal saja tidak cukup

### Rescan yang mengganti Tag menghasilkan event
22. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
23. Rina W membuka form batch DU-146-6 sehingga memegang kunci sesi edit
24. Rina W memindai ulang aset pertama dengan Tag `E280-1460-0005 {runId}` lewat Reader `Reader Gudang {runId}`
25. Rina W menyimpan batch DU-146-6
26. Rina W keluar dari form batch DU-146-6 sehingga kunci sesi edit dilepas
27. Verifikasi tepat satu event baru tercatat di Tab Usage karena Rescan menggantikan Tag

### Scan QR lewat kamera tidak menghasilkan event
28. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
29. Rina W membuka form batch DU-146-7 sehingga memegang kunci sesi edit
30. Rina W memindai Tag `E280-1460-0006 {runId}` pada aset pertama lewat kamera QR
31. Rina W menyimpan batch DU-146-7
32. Rina W keluar dari form batch DU-146-7 sehingga kunci sesi edit dilepas
33. Verifikasi jumlah event di Tab Usage sama dengan catatan karena scan QR lewat kamera bukan pemakaian reader

### Take over mempertahankan event pemegang lama untuk Tag yang sudah tersimpan
34. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
35. Rina W membuka form batch DU-146-8 sehingga memegang kunci sesi edit
36. Rina W memindai Tag `E280-1460-0007 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
37. Rina W menyimpan batch DU-146-8
38. Rina W memindai Tag `E280-1460-0008 {runId}` pada aset kedua lewat Reader `Reader Gudang {runId}` tanpa menyimpan
39. Lina mengambil alih sesi edit batch DU-146-8 dengan Take over
40. Verifikasi tepat satu event baru tercatat di Tab Usage atas nama pemegang lama dengan PIC `Rina W`
41. Verifikasi event itu memuat Date sama dengan waktu kunci sesi edit direbut Lina lewat Take over
42. Verifikasi Tag `E280-1460-0008 {runId}` tidak tersimpan pada aset kedua karena scan yang belum tersimpan hilang bersama perubahannya

### Sesi yang kedaluwarsa tetap memakai pemegang kunci sebagai PIC
43. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
44. Rina W membuka form batch DU-146-9 sehingga memegang kunci sesi edit
45. Rina W memindai Tag `E280-1460-0009 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
46. Rina W menyimpan batch DU-146-9
47. Waktu berlalu sampai 10 menit tanpa aktivitas sehingga kunci sesi edit kedaluwarsa
48. Verifikasi tepat satu event baru tercatat di Tab Usage dengan PIC `Rina W` dan bukan `System`
49. Verifikasi event itu memuat Date sama dengan waktu kunci sesi edit kedaluwarsa

### Dua Handheld Reader dalam satu sesi menghasilkan satu event per Reader
50. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` dan untuk Reader `Reader Kantor {runId}` di Tab Usage Handheld Reader
51. Rina W membuka form batch DU-146-18 sehingga memegang kunci sesi edit
52. Rina W memindai Tag `E280-1460-0010 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
53. Rina W memindai Tag `E280-1460-0011 {runId}` pada aset kedua lewat Reader `Reader Kantor {runId}`
54. Rina W keluar dari form batch DU-146-18 sehingga kunci sesi edit dilepas
55. Verifikasi tepat satu event baru tercatat di Tab Usage untuk Reader `Reader Gudang {runId}`
56. Verifikasi tepat satu event baru tercatat di Tab Usage untuk Reader `Reader Kantor {runId}`

### Submit melepas kunci sesi edit dan menulis event
57. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
58. Rina W membuka form batch DU-146-21 sehingga memegang kunci sesi edit
59. Rina W memindai Tag `E280-1460-0012 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
60. Rina W mengirim Submit for Approval atas batch DU-146-21 sehingga kunci sesi edit dilepas
61. Verifikasi tepat satu event baru tercatat di Tab Usage dengan PIC `Rina W`
62. Verifikasi event itu memuat Date sama dengan waktu kunci sesi edit dilepas oleh Submit

### Activate melepas kunci sesi edit dan menulis event
63. Catat jumlah event `Registration Scan` untuk Reader `Reader Gudang {runId}` di Tab Usage Handheld Reader
64. Rina W membuka form batch DU-146-22 sehingga memegang kunci sesi edit
65. Rina W memindai Tag `E280-1460-0013 {runId}` pada aset pertama lewat Reader `Reader Gudang {runId}`
66. Rina W mengirim Activate atas batch DU-146-22 sehingga kunci sesi edit dilepas
67. Verifikasi tepat satu event baru tercatat di Tab Usage dengan PIC `Rina W`
68. Verifikasi event itu memuat Date sama dengan waktu kunci sesi edit dilepas oleh Activate
