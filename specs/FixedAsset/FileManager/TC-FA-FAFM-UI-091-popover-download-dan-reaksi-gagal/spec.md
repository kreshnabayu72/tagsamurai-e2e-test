---
id: TC-FA-FAFM-UI-091-popover-download-dan-reaksi-gagal
title: "Popover Download: pilihan format, loading, dan reaksi Download gagal"
layer: ui-client
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["ACT-01d", "ACT-03f", "ARS-06c", "DIM-09c", "F-FAFM-02.k3", "F-FAFM-02d", "INV-10a", "INV-10b", "INV-10c", "S-19", "T-11", "T-12", "T-14", "TBL-06a", "V-02", "V-03", "V-10", "EB-DL-2@tabel-files", "EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "ACT-01d": 31
  "ACT-03f": 43
  "ARS-06c": [31, 35, 39, 43]
  "DIM-09c": [24, 26, 27]
  "F-FAFM-02.k3": [31, 35, 39, 43]
  "F-FAFM-02d": [31, 35, 39, 43]
  "INV-10a": 4
  "INV-10b": 2
  "INV-10c": [5, 6]
  "S-19": [31, 35, 39, 43]
  "T-11": 31
  "T-12": [35, 39, 47, 51, 55]
  "T-14": 43
  "TBL-06a": [5, 6]
  "V-02": 31
  "V-03": [35, 39, 47, 51, 55]
  "V-10": 43
  "EB-DL-2@tabel-files": [31, 35, 39, 43]
  "EB-DL-5": [10, 12, 13, 17, 19, 20, 24, 26, 27]
coverage:
  web: automated
---

# Popover Download: pilihan format, loading, dan reaksi Download gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager, tab `Asset Photo`.
- Komponen: Popover Download tabel
- Data:
  - DU-091-1: File `laptop-front.jpg`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 - 4`.
  - DU-091-2: File `monitor-lg-24.jpg`, Source `Asset Photo`, Asset `Monitor LG 24 - 7`.
  - DU-091-3: File `printer-hp-m404.jpg`, Source `Asset Photo`, Asset `Printer HP M404 - 1`.
  - DU-091-4: Jumlah baris tab `Asset Photo` yang cocok dengan Search dan Filter aktif `4999`, tepat di bawah ambang `5.000`.
  - DU-091-5: Jumlah baris tab `Asset Photo` yang cocok dengan Search dan Filter aktif `5000`, tepat di ambang `5.000`.
  - DU-091-6: Jumlah baris tab `Asset Photo` yang cocok dengan Search dan Filter aktif `5001`, tepat di atas ambang `5.000`.
- Kondisi:
  - K1: tab `Asset Photo` berisi DU-091-1 sampai DU-091-3.
  - K2: seperti K1 (halaman tampil memuat DU-091-1 sampai DU-091-3), dengan total baris yang cocok dilaporkan `4999` (DU-091-4), dan export CSV berhasil dengan respons yang tertahan sampai tes melepasnya.
  - K3: seperti K1 (halaman tampil memuat DU-091-1 sampai DU-091-3), dengan total baris yang cocok dilaporkan `5000` (DU-091-5), dan export CSV berhasil dengan respons yang tertahan sampai tes melepasnya.
  - K4: seperti K1 (halaman tampil memuat DU-091-1 sampai DU-091-3), dengan total baris yang cocok dilaporkan `5001` (DU-091-6), dan export CSV berhasil dengan respons yang tertahan sampai tes melepasnya.
  - K5: seperti K1, dan Download atas `laptop-front.jpg` gagal karena storage gagal.
  - K6: seperti K1, dan export dari toolbar gagal karena pembuatan export atau storage gagal.
  - K7: seperti K1, dan Download bulk ZIP atas seluruh file terpilih gagal karena pembuatan ZIP atau storage gagal.
  - K8: tab `Disposed & Unmanaged Assets` aktif, dan export dari toolbar gagal karena pembuatan export atau storage gagal.
  - K9: dialog Recycle Bin terbuka, dan export dari toolbar dialog gagal karena pembuatan export atau storage gagal.
  - K10: modal Changelog terbuka, dan export dari toolbar modal gagal karena pembuatan export atau storage gagal.

## Test Steps

### Tombol Download pada toolbar membuka popover dengan dua pilihan format
1. Tampilkan Popover Download tabel dengan kondisi K1
2. Verifikasi tombol `Download` tampil pada toolbar tab Files
3. Klik tombol `Download` pada toolbar
4. Verifikasi popover Download tampil
5. Verifikasi pilihan `Download as CSV` tampil pada popover Download
6. Verifikasi pilihan `Download as XLSX` tampil pada popover Download

### Download di bawah ambang 5.000 baris menampilkan loading lalu berkas terunduh
7. Tampilkan Popover Download tabel dengan kondisi K2
8. Klik tombol `Download` pada toolbar
9. Klik `Download as CSV`
10. Verifikasi `Downloading...` tampil pada area tombol `Download`
11. Biarkan respons export selesai
12. Verifikasi berkas CSV terunduh ke perangkat
13. Verifikasi tidak ada toast yang tampil

### Download tepat di ambang 5.000 baris menampilkan loading lalu berkas terunduh
14. Tampilkan Popover Download tabel dengan kondisi K3
15. Klik tombol `Download` pada toolbar
16. Klik `Download as CSV`
17. Verifikasi `Downloading...` tampil pada area tombol `Download`
18. Biarkan respons export selesai
19. Verifikasi berkas CSV terunduh ke perangkat
20. Verifikasi tidak ada toast yang tampil

### Download di atas ambang 5.000 baris memakai loading screen tanpa job background dan notifikasi
21. Tampilkan Popover Download tabel dengan kondisi K4
22. Klik tombol `Download` pada toolbar
23. Klik `Download as CSV`
24. Verifikasi `Downloading...` tampil pada area tombol `Download`
25. Biarkan respons export selesai
26. Verifikasi berkas CSV terunduh ke perangkat
27. Verifikasi tidak ada toast yang tampil

### Download single gagal menampilkan toast error dengan nama file
28. Tampilkan Popover Download tabel dengan kondisi K5
29. Klik `⋯` pada baris `laptop-front.jpg`
30. Klik `Download`
31. Verifikasi toast `Error, failed to download laptop-front.jpg.` tampil

### Download toolbar CSV gagal menampilkan toast error
32. Tampilkan Popover Download tabel dengan kondisi K6
33. Klik tombol `Download` pada toolbar
34. Klik `Download as CSV`
35. Verifikasi toast `Error, failed to download File-Manager-Files.` tampil setelah CSV gagal

### Download toolbar XLSX gagal menampilkan toast error
36. Tampilkan Popover Download tabel dengan kondisi K6
37. Klik tombol `Download` pada toolbar
38. Klik `Download as XLSX`
39. Verifikasi toast `Error, failed to download File-Manager-Files.` tampil setelah XLSX gagal

### Download bulk ZIP gagal menampilkan toast error
40. Tampilkan Popover Download tabel dengan kondisi K7
41. Centang checkbox header tabel
42. Klik `Download (ZIP)` pada Bulk Action Bar
43. Verifikasi toast `Error, failed to download file.` tampil

### Download toolbar tab Disposed & Unmanaged Assets gagal menyebut nama file tab itu
44. Tampilkan Popover Download tabel dengan kondisi K8
45. Klik tombol `Download` pada toolbar tab Asset Data
46. Klik `Download as CSV`
47. Verifikasi toast `Error, failed to download File-Manager-Asset-Data.` tampil setelah export gagal

### Download toolbar dialog Recycle Bin gagal menyebut nama file Recycle Bin
48. Tampilkan Popover Download tabel dengan kondisi K9
49. Klik tombol `Download` pada toolbar dialog Recycle Bin
50. Klik `Download as CSV`
51. Verifikasi toast `Error, failed to download File-Manager-Recycle-Bin.` tampil setelah export gagal

### Download toolbar modal Changelog gagal menyebut nama file Changelog
52. Tampilkan Popover Download tabel dengan kondisi K10
53. Klik tombol `Download` pada toolbar modal Changelog
54. Klik `Download as CSV`
55. Verifikasi toast `Error, failed to download Changelog-File-Manager.` tampil setelah export gagal
