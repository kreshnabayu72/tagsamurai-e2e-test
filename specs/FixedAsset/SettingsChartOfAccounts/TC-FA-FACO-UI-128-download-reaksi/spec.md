---
id: TC-FA-FACO-UI-128-download-reaksi
title: "Tab Chart of Accounts: popover Download, gagal unduh, dan loading berkas besar"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["R-11", "T-09", "§5#b8", "§[F-FACO-11] Download Account List#r2", "§9.4.2#r27", "EB-DL-2@tabel-account-list", "EB-DL-5", "§7.2#b3"]
smoke: []
dependsOn: []
trace:
  "R-11": [11, 12, 16, 17, 21, 22]
  "T-09": [11, 16, 21, 27, 32, 41]
  "§5#b8": [3, 5, 6, 7, 26, 31]
  "§[F-FACO-11] Download Account List#r2": [36, 39, 40]
  "§9.4.2#r27": [36, 39]
  "EB-DL-2@tabel-account-list": [11, 16, 21, 27, 32]
  "EB-DL-5": [36, 37, 39, 40, 41]
  "§7.2#b3": [11, 16, 21]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: popover Download, gagal unduh, dan loading berkas besar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-128-1: 3 akun Active, Account Code `D-{n}`, Name `Akun Unduh {n}`, Function `Asset Cost`, Used By `0`.
  - DU-128-2: 4.999 akun Active, Account Code `E-{n}`, Name `Akun Di Bawah Ambang {n}`, Function `Asset Cost`, Used By `0`.
  - DU-128-3: 5.000 akun Active, Account Code `F-{n}`, Name `Akun Tepat Ambang {n}`, Function `Asset Cost`, Used By `0`.
  - DU-128-4: 5.001 akun Active, Account Code `G-{n}`, Name `Akun Lebih Ambang {n}`, Function `Asset Cost`, Used By `0`.
- Kondisi:
  - K1: tabel berisi DU-128-1; server menyiapkan berkas dengan benar.
  - K2: seperti K1; server menolak permintaan unduhan dengan error 5xx.
  - K3: seperti K1; server tidak menjawab permintaan unduhan sampai batas waktu.
  - K4: tabel berisi DU-128-2; server menyiapkan berkas dengan benar.
  - K5: tabel berisi DU-128-3; server menyiapkan berkas dengan benar.
  - K6: tabel berisi DU-128-4; server menahan berkas sampai pengujian melepasnya.

## Test Steps

### Popover Download
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Arahkan kursor ke ikon Download
3. Verifikasi tooltip `Download` tampil
4. Klik ikon Download
5. Verifikasi opsi `Download as CSV` tampil
6. Verifikasi opsi `Download as XLSX` tampil
7. Verifikasi tidak ada opsi unduhan selain `Download as CSV` dan `Download as XLSX`

### Unduhan CSV gagal karena error server
8. Tampilkan Tab Chart of Accounts dengan kondisi K2
9. Klik ikon Download
10. Klik `Download as CSV`
11. Verifikasi toast `Error, failed to download Chart-of-Accounts.` tampil
12. Verifikasi tombol Download dapat dipakai kembali

### Unduhan XLSX gagal karena error server
13. Tampilkan Tab Chart of Accounts dengan kondisi K2
14. Klik ikon Download
15. Klik `Download as XLSX`
16. Verifikasi toast `Error, failed to download Chart-of-Accounts.` tampil
17. Verifikasi tombol Download dapat dipakai kembali

### Unduhan gagal karena timeout
18. Tampilkan Tab Chart of Accounts dengan kondisi K3
19. Klik ikon Download
20. Klik `Download as CSV`
21. Verifikasi toast `Error, failed to download Chart-of-Accounts.` tampil
22. Verifikasi tombol Download dapat dipakai kembali

### Unduhan di bawah ambang 5.000 baris
23. Tampilkan Tab Chart of Accounts dengan kondisi K4
24. Klik ikon Download
25. Klik `Download as CSV`
26. Verifikasi server menerima satu permintaan unduhan Chart-of-Accounts
27. Verifikasi tidak ada toast yang tampil

### Unduhan tepat di ambang 5.000 baris
28. Tampilkan Tab Chart of Accounts dengan kondisi K5
29. Klik ikon Download
30. Klik `Download as XLSX`
31. Verifikasi server menerima satu permintaan unduhan Chart-of-Accounts
32. Verifikasi tidak ada toast yang tampil

### Unduhan lebih dari 5.000 baris memakai loading screen
33. Tampilkan Tab Chart of Accounts dengan kondisi K6
34. Klik ikon Download
35. Klik `Download as CSV`
36. Verifikasi loading screen unduhan tampil
37. Verifikasi tidak ada toast atau notifikasi in-app yang tampil selama loading screen
38. Lepaskan berkas dari server
39. Verifikasi loading screen unduhan tidak tampil
40. Verifikasi unduhan dimulai langsung
41. Verifikasi tidak ada toast yang tampil
