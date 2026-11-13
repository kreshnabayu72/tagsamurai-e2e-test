---
id: TC-FA-FAREG-UI-021-form-tag-combined-perubahan-slot
title: "Form Register Asset: Tag combined, perubahan slot Tag, dan Tag direbut"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-01n", "§9.4.2#r42", "§9.4.2#r43", "§9.4.2#r44", "§9.4.2#r45", "§9.4.2#r46", "§9.4.2#r47", "§9.4.2#r48", "§9.4.2#r49", "§9.4.2#r50", "§9.4.2#r51", "§9.4.2#r53"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01n": [60, 61, 62]
  "§9.4.2#r42": [4, 6]
  "§9.4.2#r43": [10, 11]
  "§9.4.2#r44": [15, 16, 17]
  "§9.4.2#r45": [21, 22]
  "§9.4.2#r46": [26, 27, 28]
  "§9.4.2#r47": [32, 33]
  "§9.4.2#r48": [37, 38]
  "§9.4.2#r49": [42, 43, 44]
  "§9.4.2#r50": [54, 55]
  "§9.4.2#r51": [60, 61, 62]
  "§9.4.2#r53": [48, 49, 50]
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
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-021-1; aset `Printer Epson L3250 - 1` kedua slotnya `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-5.
  - K2: form `Edit` draft tersimpan dengan Item DU-021-3; aset `Alat Ukur Laser Bosch - 1` ketiga slotnya `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-6.
  - K3: form `Edit` draft tersimpan dengan Item DU-021-1; slot NFC aset `Printer Epson L3250 - 1` sudah `Verified` dengan DU-021-7 dan slot RFID `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-6.
  - K4: form `Edit` draft tersimpan dengan Item DU-021-2; aset `Laptop Dell Latitude 5440 - 1` hanya punya satu slot; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-5.
  - K5: form `Edit` draft tersimpan dengan Item DU-021-1; kedua slot aset `Printer Epson L3250 - 1` `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-8.
  - K6: form `Edit` draft tersimpan dengan Item DU-021-1; kedua slot aset `Printer Epson L3250 - 1` sudah `Verified` dari DU-021-5; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot RFID aset itu menghasilkan DU-021-9.
  - K7: form `Edit` draft tersimpan dengan Item DU-021-1; slot RFID aset `Printer Epson L3250 - 1` sudah `Verified` dengan DU-021-10 dan slot NFC `Unverified`; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; pemindaian slot NFC aset itu menghasilkan DU-021-11.
  - K8: form `Edit` draft tersimpan dengan Item DU-021-4; slot QR aset `Kursi Kerja Ergonomis - 1` sudah `Verified` dengan DU-021-12; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC.
  - K9: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` sudah `Verified` dengan DU-021-13; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC.
  - K10: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` `Verified` dengan DU-021-13; Tag itu direbut sesi lain sehingga Save draft menyimpan draft tanpa Tag tersebut.
  - K11: form `Edit` draft tersimpan dengan Item DU-021-2; slot RFID aset `Laptop Dell Latitude 5440 - 1` `Verified` dengan DU-021-13; Tag itu direbut sesi lain sehingga Submit ditolak seluruhnya.

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
36. Klik `Scan NFC` pada `Printer Epson L3250 - 1`
37. Verifikasi pesan `This TAG is the same as the current TAG` tampil untuk Tag combined yang memuat kode Tag lama
38. Verifikasi slot NFC pada `Printer Epson L3250 - 1` tetap berbadge `Unverified`

### Mengganti Asset Name mengubah slot Tag
39. Tampilkan Halaman `Register Asset` dengan kondisi K8
40. Klik tab `Asset`
41. Ganti Asset Name Item `Kursi Kerja Ergonomis` menjadi `Printer Epson L3250`
42. Verifikasi slot RFID dan slot NFC pada Item `Printer Epson L3250` berbadge `Unverified`
43. Verifikasi slot QR tidak lagi tampil pada Item `Printer Epson L3250`
44. Verifikasi peringatan perubahan slot Tag tampil di atas form
45. Tampilkan Halaman `Register Asset` dengan kondisi K9
46. Klik tab `Asset`
47. Ganti Asset Name Item `Laptop Dell Latitude 5440` menjadi `Kursi Kerja Ergonomis`
48. Verifikasi slot QR pada Item `Kursi Kerja Ergonomis` berbadge `Unverified`
49. Verifikasi kode Tag `RFID-000510` tidak lagi tampil pada Item `Kursi Kerja Ergonomis`
50. Verifikasi peringatan tampil di atas form

### Tag direbut sesi lain sebelum Save draft
51. Tampilkan Halaman `Register Asset` dengan kondisi K10
52. Klik tab `Asset`
53. Klik `[Save draft]`
54. Verifikasi slot RFID pada `Laptop Dell Latitude 5440 - 1` kembali berbadge `Unverified`
55. Verifikasi peringatan `RFID-000510 is no longer available. Scan another TAG.` tampil

### Tag direbut sesi lain sebelum Submit menolak seluruh Submit
56. Tampilkan Halaman `Register Asset` dengan kondisi K11
57. Klik tab `Asset`
58. Klik `[Submit]`
59. Konfirmasi pada dialog yang tampil sesudah `[Submit]`
60. Verifikasi slot RFID pada `Laptop Dell Latitude 5440 - 1` kembali berbadge `Unverified`
61. Verifikasi peringatan `RFID-000510 is no longer available. Scan another TAG.` tampil
62. Verifikasi Breadcrumb tetap menampilkan `Assets > Registration > Draft`
