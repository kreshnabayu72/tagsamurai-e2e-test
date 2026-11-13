---
id: TC-FA-FAREG-UI-021-form-tag-combined-perubahan-slot
title: "Form Register Asset: Tag combined, perubahan slot Tag, dan Tag direbut"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-01n", "§9.4.2#r42", "§9.4.2#r43", "§9.4.2#r44", "§9.4.2#r45", "§9.4.2#r46", "§9.4.2#r47", "§9.4.2#r48", "§9.4.2#r49", "§9.4.2#r50", "§9.4.2#r51", "§9.4.2#r53"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01n": [62, 63, 64]
  "§9.4.2#r42": [4, 6]
  "§9.4.2#r43": [10, 11]
  "§9.4.2#r44": [15, 16, 17]
  "§9.4.2#r45": [21, 22]
  "§9.4.2#r46": [26, 27, 28, 68, 69, 70]
  "§9.4.2#r47": [32, 33]
  "§9.4.2#r48": [37, 38, 39]
  "§9.4.2#r49": [43, 44, 45]
  "§9.4.2#r50": [55, 56]
  "§9.4.2#r51": [62, 63, 64, 60]
  "§9.4.2#r53": [49, 50, 51]
coverage:
  web: automated
---

# Form Register Asset: Tag combined, perubahan slot Tag, dan Tag direbut

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-021-1: Item `Printer Epson L3250`, TAG Type `RFID` dan `NFC`; aset `Printer Epson L3250 - 1`.
  - DU-021-2: Item `Laptop Dell Latitude 5440`, TAG Type `RFID`; aset `Laptop Dell Latitude 5440 - 1`.
  - DU-021-3: Item `Alat Ukur Laser Bosch`, TAG Type `RFID`, `QR`, dan `NFC`; aset `Alat Ukur Laser Bosch - 1`.
  - DU-021-4: Item `Kursi Kerja Ergonomis`, TAG Type `QR`; aset `Kursi Kerja Ergonomis - 1`.
  - DU-021-5: Tag combined `CMB-000801` berkomponen RFID `RFID-000801` dan NFC `NFC-000801`, semuanya `Available`.
  - DU-021-6: Tag combined `CMB-000802` berkomponen RFID `RFID-000802` dan NFC `NFC-000802`, semuanya `Available`.
  - DU-021-7: Tag `NFC-000901`, tipe NFC, `Verified` di slot NFC aset `Printer Epson L3250 - 1`.
  - DU-021-8: Tag combined `CMB-000803` berkomponen RFID `RFID-000803` yang tidak ada di registri dan NFC `NFC-000803` `Available`.
  - DU-021-9: Tag `RFID-000902`, tipe RFID, `Available`.
  - DU-021-10: Tag `RFID-000903`, tipe RFID, `Verified` di slot RFID aset `Printer Epson L3250 - 1`.
  - DU-021-11: Tag combined `CMB-000804` berkomponen RFID `RFID-000903` dan NFC `NFC-000804`.
  - DU-021-12: Tag `QR-000901`, tipe QR, `Verified` di slot QR aset `Kursi Kerja Ergonomis - 1`.
  - DU-021-13: Tag `RFID-000510`, tipe RFID, `Verified` di slot RFID aset `Laptop Dell Latitude 5440 - 1`.
  - DU-021-14: Item `Rak Gudang Pintar`, TAG Type `QR` dan `RFID`; aset `Rak Gudang Pintar - 1`.
  - DU-021-15: Tag combined `CMB-000805` berkomponen QR `QR-000805` dan RFID `RFID-000805`, semuanya `Available`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-021-1; aset `Printer Epson L3250 - 1` kedua slotnya `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-5.
  - K2: form `Edit` draft tersimpan dengan Item DU-021-3; aset `Alat Ukur Laser Bosch - 1` ketiga slotnya `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-6.
  - K3: form `Edit` draft tersimpan dengan Item DU-021-1; slot NFC aset `Printer Epson L3250 - 1` sudah `Verified` dengan DU-021-7 dan slot RFID `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-6.
  - K4: form `Edit` draft tersimpan dengan Item DU-021-2; aset `Laptop Dell Latitude 5440 - 1` hanya punya satu slot; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-5.
  - K5: form `Edit` draft tersimpan dengan Item DU-021-1; kedua slot aset `Printer Epson L3250 - 1` `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-8.
  - K6: form `Edit` draft tersimpan dengan Item DU-021-1; kedua slot aset `Printer Epson L3250 - 1` sudah `Verified` dari DU-021-5; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-9.
  - K7: form `Edit` draft tersimpan dengan Item DU-021-1; slot RFID aset `Printer Epson L3250 - 1` sudah `Verified` dengan DU-021-10 dan slot NFC `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-11.
  - K8: form `Edit` draft tersimpan dengan Item DU-021-4; slot QR aset `Kursi Kerja Ergonomis - 1` sudah `Verified` dengan DU-021-12; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC.
  - K9: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` sudah `Verified` dengan DU-021-13; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC.
  - K10: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` `Verified` dengan DU-021-13; Tag itu direbut sesi lain sehingga Save draft menyimpan draft tanpa Tag tersebut.
  - K11: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` `Verified` dengan DU-021-13; Tag itu direbut sesi lain sehingga Submit ditolak seluruhnya; Approval Workflow nonaktif; seluruh aset memenuhi Tingkat 2 dan seluruh slot Tag-nya terisi.
  - K12: form `Edit` draft tersimpan dengan Item DU-021-14; aset `Rak Gudang Pintar - 1` kedua slotnya `Unverified`; reader TAG terhubung; plan berperingkat `rank=0` sehingga tipe Tag RFID terkunci oleh plan dan tipe QR tersedia; pemindaian slot QR aset itu menghasilkan DU-021-15.

## Test Steps
### Tag combined yang cocok mengisi semua slot terbuka
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Klik `Scan RFID` pada `Printer Epson L3250 - 1`
4. Verifikasi slot RFID dan slot NFC pada `Printer Epson L3250 - 1` berbadge `Verified`
5. Arahkan pointer ke Badge `Verified` pada slot RFID `Printer Epson L3250 - 1`
6. Verifikasi tooltip Badge menyebut `combined`

### Tag combined yang hanya mencakup sebagian slot
7. Tampilkan Halaman `Register Asset` dengan kondisi K2
8. Klik tab `Asset`
9. Klik `Scan RFID` pada `Alat Ukur Laser Bosch - 1`
10. Verifikasi slot RFID dan slot NFC pada `Alat Ukur Laser Bosch - 1` berbadge `Verified`
11. Verifikasi slot QR pada `Alat Ukur Laser Bosch - 1` tetap berbadge `Unverified`

### Tag combined yang menabrak slot berisi Tag tunggal ditolak
12. Tampilkan Halaman `Register Asset` dengan kondisi K3
13. Klik tab `Asset`
14. Klik `Scan RFID` pada `Printer Epson L3250 - 1`
15. Verifikasi pesan `This combined TAG doesn't match the open slots` tampil
16. Verifikasi slot NFC pada `Printer Epson L3250 - 1` tetap berbadge `Verified`
17. Verifikasi slot RFID pada `Printer Epson L3250 - 1` tetap berbadge `Unverified`

### Tag combined pada aset dengan satu slot ditolak
18. Tampilkan Halaman `Register Asset` dengan kondisi K4
19. Klik tab `Asset`
20. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
21. Verifikasi pesan `This TAG is combined. It can only fill multiple slots.` tampil
22. Verifikasi slot RFID pada `Laptop Dell Latitude 5440 - 1` berbadge `Unverified`

### Satu komponen Tag combined gagal validasi menolak seluruh scan
23. Tampilkan Halaman `Register Asset` dengan kondisi K5
24. Klik tab `Asset`
25. Klik `Scan RFID` pada `Printer Epson L3250 - 1`
26. Verifikasi pesan `Error, can't recognize TAG.` tampil untuk komponen RFID yang gagal
27. Verifikasi slot RFID pada `Printer Epson L3250 - 1` berbadge `Unverified`
28. Verifikasi slot NFC pada `Printer Epson L3250 - 1` berbadge `Unverified`

### Pindai ulang slot hasil Tag combined
29. Tampilkan Halaman `Register Asset` dengan kondisi K6
30. Klik tab `Asset`
31. Klik `Scan RFID` pada `Printer Epson L3250 - 1`
32. Verifikasi slot RFID pada `Printer Epson L3250 - 1` berbadge `Verified` dengan kode Tag `RFID-000902`
33. Verifikasi slot NFC pada `Printer Epson L3250 - 1` kembali berbadge `Unverified`

### Tag combined yang memuat kode Tag lama aset ditolak
34. Tampilkan Halaman `Register Asset` dengan kondisi K7
35. Klik tab `Asset`
36. Klik `Scan RFID` pada `Printer Epson L3250 - 1`
37. Verifikasi pesan `This TAG is the same as the current TAG` tampil untuk Tag combined yang memuat kode Tag lama
38. Verifikasi slot RFID pada `Printer Epson L3250 - 1` tetap berbadge `Verified` dengan kode Tag `RFID-000903`
39. Verifikasi slot NFC pada `Printer Epson L3250 - 1` tetap berbadge `Unverified`

### Mengganti Asset Name mengubah slot Tag
40. Tampilkan Halaman `Register Asset` dengan kondisi K8
41. Klik tab `Asset`
42. Ganti Asset Name Item `Kursi Kerja Ergonomis` menjadi `Printer Epson L3250`
43. Verifikasi slot RFID dan slot NFC pada Item `Printer Epson L3250` berbadge `Unverified`
44. Verifikasi slot QR tidak lagi tampil pada Item `Printer Epson L3250`
45. Verifikasi peringatan perubahan slot Tag tampil di atas form
46. Tampilkan Halaman `Register Asset` dengan kondisi K9
47. Klik tab `Asset`
48. Ganti Asset Name Item `Laptop Dell Latitude 5440` menjadi `Kursi Kerja Ergonomis`
49. Verifikasi slot QR pada Item `Kursi Kerja Ergonomis` berbadge `Unverified`
50. Verifikasi kode Tag `RFID-000510` tidak lagi tampil pada Item `Kursi Kerja Ergonomis`
51. Verifikasi peringatan tampil di atas form

### Tag direbut sesi lain sebelum Save draft
52. Tampilkan Halaman `Register Asset` dengan kondisi K10
53. Klik tab `Asset`
54. Klik `[Save draft]`
55. Verifikasi slot RFID pada `Laptop Dell Latitude 5440 - 1` kembali berbadge `Unverified`
56. Verifikasi peringatan `RFID-000510 is no longer available. Scan another TAG.` tampil

### Tag direbut sesi lain sebelum Submit menolak seluruh Submit
57. Tampilkan Halaman `Register Asset` dengan kondisi K11
58. Klik tab `Asset`
59. Klik `[Submit]`
60. Verifikasi dialog konfirmasi `Activate Assets` memuat `Are you sure you want to activate it?`
61. Klik `[Activate]` pada dialog konfirmasi `Activate Assets`
62. Verifikasi slot RFID pada `Laptop Dell Latitude 5440 - 1` kembali berbadge `Unverified`
63. Verifikasi peringatan `RFID-000510 is no longer available. Scan another TAG.` tampil
64. Verifikasi Breadcrumb tetap menampilkan `Assets > Registration > Draft`

### Tag combined dengan komponen bertipe terkunci plan menolak seluruh scan
65. Tampilkan Halaman `Register Asset` dengan kondisi K12
66. Klik tab `Asset`
67. Klik `Scan QR` pada `Rak Gudang Pintar - 1`
68. Verifikasi pesan penolakan untuk komponen RFID yang terkunci plan tampil
69. Verifikasi slot QR pada `Rak Gudang Pintar - 1` berbadge `Unverified`
70. Verifikasi slot RFID pada `Rak Gudang Pintar - 1` berbadge `Unverified`
