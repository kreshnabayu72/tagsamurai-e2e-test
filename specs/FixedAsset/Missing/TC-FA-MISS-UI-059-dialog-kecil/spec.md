---
id: TC-FA-MISS-UI-059-dialog-kecil
title: "Dialog Cancel Report, Cannot Mark as Found, dan Already Changed: judul, body, tombol, dan Reload"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§4.2.4#p7, §4.2.4#p10, §4.2.4#p13, §7.2#r3, §7.2#r6, §7.2#r9, §7.2#r18, §7.3#r11, §6#r10, §4.2.4#r23, §4.1#r7, §4.1#r10, §7.3#r2, §7.3#r3, EB-FB-1@cancel-report, EB-ERR-1@cancel-report]
smoke: []
dependsOn: []
trace:
  §4.2.4#p7: [2, 3, 4, 5, 12]
  §4.2.4#p10: [40, 41, 42, 44, 47, 50, 53, 56, 59]
  §4.2.4#p13: [29, 30, 33, 35, 37, 38, 62, 64, 65]
  §7.2#r3: [2, 3, 4, 5]
  §7.2#r6: [40, 41, 42, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59]
  §7.2#r9: [28, 29, 30, 32, 33, 35]
  §7.2#r18: [8, 28, 29]
  §7.3#r11: [8, 15]
  §6#r10: [28, 29]
  §4.2.4#r23: [37, 38, 64, 65]
  §4.1#r7: [2, 5]
  §4.1#r10: [40, 42]
  §7.3#r2: 8
  §7.3#r3: 2
  EB-FB-1@cancel-report: [8, 9, 15]
  EB-ERR-1@cancel-report: [15, 16, 17, 19, 20, 23, 24, 25]
anchor: []
coverage:
  web: automated
---
# Dialog Cancel Report, Cannot Mark as Found, dan Already Changed: judul, body, tombol, dan Reload

## Prerequisites
- Aktor: pelapor dari pemegang aset untuk K1 sampai K4 dan K13; Aktor Missing pada Group aset untuk K5 sampai K12.
- Layar awal: halaman Missing, tab Active; daftar My Asset untuk K13.
- Komponen: Dialog konfirmasi dan blok Missing (D-MIS-06, D-MIS-07, D-MIS-10)
- Data:
  - DU-059-1: Record `Scanner Zebra DS2208 - 2`, Asset ID `SCN-2026-0002`, Group `Warehouse`, status record `Waiting for Confirmation`.
  - DU-059-2: Aset `Camera Canon EOS - 1`, Asset ID `CAM-2026-0001`, Group `Head Office`.
  - DU-059-3: Aset `Printer HP LaserJet M404 - 5`, Asset ID `PRN-2026-0005`, Group `Head Office`, status record `In Disposal Process`.
  - DU-059-4: Record `Hand Pallet Truck - 3`, Asset ID `HPT-2026-0003`, Group `Warehouse`, status record `Waiting for Confirmation`.
- Kondisi:
  - K1: dialog Cancel Report dibuka untuk record DU-059-1; Cancel Report berhasil; toast yang diharapkan `Success, report has been canceled.`; bullet yang diharapkan `• Scanner Zebra DS2208`, dari Asset Name `Scanner Zebra DS2208`.
  - K2: dialog Cancel Report dibuka untuk record DU-059-1; Cancel Report pertama gagal karena error server, berikutnya berhasil.
  - K3: dialog Cancel Report dibuka untuk record DU-059-1; Cancel Report gagal karena timeout.
  - K4: dialog Cancel Report dibuka untuk record DU-059-1; saat Submit record sudah bukan Waiting for Confirmation karena diubah oleh Rina W; teks yang diharapkan `This record was changed by Rina W. Reload to see the latest status.`, dari User Name `Rina W`.
  - K5: dialog Already Changed dibuka untuk record DU-059-4 dengan `[Reload]` memuat ulang daftar tempat dialog dibuka.
  - K6: dialog Already Changed dibuka untuk record DU-059-4 yang diubah oleh System; teks yang diharapkan `This record was changed by System. Reload to see the latest status.`, dari User Name `System`.
  - K7: dialog Cannot Mark as Found dibuka untuk aset DU-059-2 yang tidak dilaporkan hilang; pesan yang diharapkan `Camera Canon EOS is not reported missing.`, dari Asset Name `Camera Canon EOS`.
  - K8: dialog Cannot Mark as Found dibuka untuk aset di luar akses Aktor Missing.
  - K9: dialog Cannot Mark as Found dibuka untuk aset DU-059-3 yang dalam disposal; pesan yang diharapkan `Printer HP LaserJet M404 is in disposal. Mark as Found is not available.`, dari Asset Name `Printer HP LaserJet M404`.
  - K10: dialog Cannot Mark as Found dibuka untuk aset yang terakhir dipegang oleh Aktor Missing itu sendiri.
  - K11: dialog Cannot Mark as Found dibuka untuk TAG yang tidak terdaftar pada aset mana pun.
  - K12: dialog Cannot Mark as Found dibuka untuk TAG yang tidak terbaca.
  - K13: dialog Cancel Report dibuka dari daftar My Asset untuk record DU-059-1; saat Submit record sudah bukan Waiting for Confirmation karena diubah oleh Rina W; `[Reload]` memuat ulang daftar My Asset tempat dialog dibuka.


## Test Steps

### Dialog Cancel Report: judul, body, dan tombol
1. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K1
2. Verifikasi judul dialog `Cancel Report`
3. Verifikasi body memuat bullet `• Scanner Zebra DS2208`
4. Verifikasi body memuat pertanyaan `Are you sure you want to cancel it?`
5. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Report]`

### Cancel Report berhasil
6. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K1
7. Klik `[Cancel Report]`
8. Verifikasi toast `Success, report has been canceled.` tampil
9. Verifikasi dialog Cancel Report tertutup

### Go Back menutup dialog Cancel Report
10. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K1
11. Klik `[Go Back]`
12. Verifikasi dialog Cancel Report tertutup

### Cancel Report gagal karena error server: dialog dipertahankan dan submit ulang berhasil
13. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K2
14. Klik `[Cancel Report]`
15. Verifikasi toast `Error, failed to cancel report.` tampil
16. Verifikasi dialog Cancel Report tetap terbuka
17. Verifikasi `[Cancel Report]` aktif lagi
18. Klik `[Cancel Report]`
19. Verifikasi toast `Success, report has been canceled.` tampil
20. Verifikasi dialog Cancel Report tertutup

### Cancel Report gagal karena timeout
21. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K3
22. Klik `[Cancel Report]`
23. Verifikasi toast `Connection problem. Please try again.` tampil setelah Cancel Report
24. Verifikasi dialog Cancel Report tetap terbuka
25. Verifikasi `[Cancel Report]` aktif lagi

### Cancel Report atas record yang sudah berubah menampilkan Already Changed
26. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K4
27. Klik `[Cancel Report]`
28. Verifikasi dialog `Already Changed` tampil
29. Verifikasi dialog Already Changed memuat teks `This record was changed by Rina W. Reload to see the latest status.`
30. Verifikasi dialog Already Changed memuat tombol `[Reload]`

### Already Changed oleh System
31. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K6
32. Verifikasi dialog `Already Changed` tampil
33. Verifikasi dialog Already Changed memuat teks `This record was changed by System. Reload to see the latest status.`

### Reload pada Already Changed
34. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K5
35. Verifikasi dialog Already Changed memuat tombol `[Reload]`
36. Klik `[Reload]`
37. Verifikasi dialog Already Changed tertutup
38. Verifikasi daftar tempat dialog dibuka dimuat ulang

### Cannot Mark as Found: aset tidak dilaporkan hilang
39. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K7
40. Verifikasi judul dialog `Cannot Mark as Found`
41. Verifikasi body memuat pesan `Camera Canon EOS is not reported missing.`
42. Verifikasi dialog memuat tombol `[OK]`
43. Klik `[OK]`
44. Verifikasi dialog Cannot Mark as Found tertutup

### Cannot Mark as Found: tanpa akses ke aset
45. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K8
46. Verifikasi judul dialog `Cannot Mark as Found`
47. Verifikasi body memuat pesan `You don't have access to this asset.`

### Cannot Mark as Found: aset dalam disposal
48. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K9
49. Verifikasi judul dialog `Cannot Mark as Found`
50. Verifikasi body memuat pesan `Printer HP LaserJet M404 is in disposal. Mark as Found is not available.`

### Cannot Mark as Found: pengguna adalah Last holder
51. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K10
52. Verifikasi judul dialog `Cannot Mark as Found`
53. Verifikasi body memuat pesan `You were holding this asset. Ask another admin.`

### Cannot Mark as Found: TAG tidak terdaftar
54. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K11
55. Verifikasi judul dialog `Cannot Mark as Found`
56. Verifikasi body memuat pesan `This TAG is not registered to any asset.`

### Cannot Mark as Found: TAG tidak terbaca
57. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K12
58. Verifikasi judul dialog `Cannot Mark as Found`
59. Verifikasi body memuat pesan `Unable to read the TAG. Try again.`

### Reload pada Already Changed dari Cancel Report memuat ulang daftar tempat dialog dibuka
60. Tampilkan Dialog konfirmasi dan blok Missing dengan kondisi K13
61. Klik `[Cancel Report]`
62. Verifikasi dialog `Already Changed` tampil
63. Klik `[Reload]`
64. Verifikasi dialog Already Changed tertutup
65. Verifikasi daftar tempat dialog Cancel Report dibuka dimuat ulang
