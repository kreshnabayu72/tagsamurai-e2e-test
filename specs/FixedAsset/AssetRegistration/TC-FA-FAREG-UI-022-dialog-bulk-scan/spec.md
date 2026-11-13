---
id: TC-FA-FAREG-UI-022-dialog-bulk-scan
title: "Dialog Bulk Scan: antrean aset dan navigasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-REG-23", "FI-REG-25", "FI-REG-26", "FI-REG-27", "FI-REG-28", "§4.1#r15", "§4.1#p28", "§4.8#r24"]
smoke: []
dependsOn: []
trace:
  "D-REG-23": [5, 6, 10, 12]
  "FI-REG-25": [18, 19]
  "FI-REG-26": [23, 27, 29]
  "FI-REG-27": [34, 36, 39]
  "FI-REG-28": [32, 40]
  "§4.1#r15": [2, 3, 5, 6, 12]
  "§4.1#p28": [2, 5, 7, 8, 9, 10, 14, 43, 46]
  "§4.8#r24": [43, 46]
anchor: [42, 45]
coverage:
  web: automated
---

# Dialog Bulk Scan: antrean aset dan navigasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft > Edit, tab `Asset`
- Komponen: Dialog `Bulk Scan` (`D-REG-23`)
- Data:
  - DU-022-1: Item `Laptop Dell Latitude 5440`, TAG Type `RFID`; aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, dan `Laptop Dell Latitude 5440 - 3`, semuanya `Unverified`.
  - DU-022-2: Item `Printer Epson L3250`, TAG Type `RFID` dan `NFC`; aset `Printer Epson L3250 - 1` dan `Printer Epson L3250 - 2`, semua slot `Unverified`.
  - DU-022-3: Item `Meja Lipat Aluminium`, TAG Type `Non-TAG`; aset `Meja Lipat Aluminium - 1`.
  - DU-022-4: Tag `RFID-001101`, tipe RFID, status `Available`.
  - DU-022-5: Tag `RFID-999998`, tidak ada di registri.
  - DU-022-6: Tag `NFC-001201`, tipe NFC, status `Available`.
- Kondisi:
  - K1: tab `Asset` form `Edit` draft tersimpan dengan Item DU-022-1, DU-022-2, dan DU-022-3; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC.
  - K2: sama dengan K1; pemindaian RFID menghasilkan DU-022-5.
  - K3: sama dengan K1; setiap pemindaian RFID menghasilkan DU-022-4.
  - K4: sama dengan K1; setiap pemindaian RFID menghasilkan DU-022-4 dan setiap pemindaian NFC menghasilkan DU-022-6.
  - K5: sama dengan K1 dalam mode read-only.

## Test Steps
### Tombol Bulk Scan per Item membuka dialog antrean Item itu saja
1. Tampilkan Dialog `Bulk Scan` dengan kondisi K1
2. Verifikasi tombol `Bulk Scan` tampil pada judul Item `Laptop Dell Latitude 5440`
3. Verifikasi tombol `Bulk Scan` tampil pada judul Item `Printer Epson L3250`
4. Klik `Bulk Scan` pada judul Item `Laptop Dell Latitude 5440`
5. Verifikasi dialog `Bulk Scan` tampil dengan aset aktif `Laptop Dell Latitude 5440 - 1`
6. Verifikasi dialog memuat tombol `< Prev` dan `Next >`
7. Verifikasi dialog memuat tombol `Scan RFID`
8. Verifikasi tombol `Scan QR` dan `Scan NFC` tidak tampil di dialog
9. Verifikasi aset `Meja Lipat Aluminium - 1` tidak tampil di dialog
10. Verifikasi dialog tidak memuat tombol `Close` di bagian bawah
11. Klik ikon X pada dialog
12. Verifikasi dialog `Bulk Scan` tertutup
13. Klik `Bulk Scan` pada judul Item `Printer Epson L3250`
14. Verifikasi dialog memuat tombol `Scan RFID` dan `Scan NFC` untuk aset aktif `Printer Epson L3250 - 1`

### Scan gagal membuat antrean tetap pada aset yang sama
15. Tampilkan Dialog `Bulk Scan` dengan kondisi K2
16. Klik `Bulk Scan` pada judul Item `Laptop Dell Latitude 5440`
17. Klik `Scan RFID` pada dialog
18. Verifikasi pesan `Error, can't recognize TAG.` tampil di dialog
19. Verifikasi aset aktif tetap `Laptop Dell Latitude 5440 - 1`

### Semua Tag wajib terpasang membuat antrean lanjut otomatis
20. Tampilkan Dialog `Bulk Scan` dengan kondisi K3
21. Klik `Bulk Scan` pada judul Item `Laptop Dell Latitude 5440`
22. Klik `Scan RFID` pada dialog
23. Verifikasi aset aktif berpindah ke `Laptop Dell Latitude 5440 - 2`
24. Tampilkan Dialog `Bulk Scan` dengan kondisi K4
25. Klik `Bulk Scan` pada judul Item `Printer Epson L3250`
26. Klik `Scan RFID` pada dialog
27. Verifikasi aset aktif tetap `Printer Epson L3250 - 1` karena slot NFC belum terpasang
28. Klik `Scan NFC` pada dialog
29. Verifikasi aset aktif berpindah ke `Printer Epson L3250 - 2`

### Pindah manual antar aset dan Next dinonaktifkan di aset terakhir
30. Tampilkan Dialog `Bulk Scan` dengan kondisi K1
31. Klik `Bulk Scan` pada judul Item `Laptop Dell Latitude 5440`
32. Verifikasi tombol `Next >` tidak Disabled pada aset aktif `Laptop Dell Latitude 5440 - 1`
33. Klik `Next >`
34. Verifikasi aset aktif berpindah ke `Laptop Dell Latitude 5440 - 2`
35. Klik `< Prev`
36. Verifikasi aset aktif kembali ke `Laptop Dell Latitude 5440 - 1`
37. Klik `Next >`
38. Klik `Next >`
39. Verifikasi aset aktif adalah `Laptop Dell Latitude 5440 - 3`
40. Verifikasi tombol `Next >` Disabled pada aset terakhir

### Tombol Bulk Scan Hidden untuk Item tanpa Tag wajib dan pada mode read-only
41. Tampilkan Dialog `Bulk Scan` dengan kondisi K1
42. Verifikasi tombol `Bulk Scan` tersedia pada Item `Laptop Dell Latitude 5440`
43. Verifikasi tombol `Bulk Scan` tidak tampil pada judul Item `Meja Lipat Aluminium`
44. Tampilkan Dialog `Bulk Scan` dengan kondisi K5
45. Verifikasi judul Item `Laptop Dell Latitude 5440` tampil
46. Verifikasi tombol `Bulk Scan` tidak tampil pada mode read-only
