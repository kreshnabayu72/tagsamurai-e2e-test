---
id: TC-FA-DAMAGED-UI-117-dialog-cancel-report
title: "Dialog Cancel Report: bullet nama aset, pertanyaan penutup, Go Back, saving, toast, gagal 5xx, dan Already Changed bila laporan sudah diputuskan"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-DMG-08, "§4.2.4#p7", TS-DMG-07, "§9.6#r4", "§4.2.4#p5", EB-FB-1@cancel-report, EB-FB-2@go-back-cancel-report, EB-ERR-1@cancel-report]
smoke: []
dependsOn: []
trace:
  D-DMG-08: [2, 3, 4, 5, 6]
  "§4.2.4#p7": [2, 3, 4, 5, 6]
  TS-DMG-07: [9, 23]
  "§9.6#r4": [9, 10, 17, 18, 20, 23]
  "§4.2.4#p5": [34, 35, 36, 38, 41]
  EB-FB-1@cancel-report: [9, 23]
  EB-FB-2@go-back-cancel-report: [13, 14]
  EB-ERR-1@cancel-report: [23, 24, 25, 27, 30, 31]
anchor: []
coverage:
  web: automated
---

# Dialog Cancel Report: bullet nama aset, pertanyaan penutup, Go Back, saving, toast, gagal 5xx, dan Already Changed bila laporan sudah diputuskan

## Prerequisites
- Aktor: Pelapor, yaitu pemegang aset yang membuka Cancel Report dari My Asset (`Dewi A`).
- Layar awal: Dialog Cancel Report belum ditampilkan; setiap blok langkah menampilkannya dengan kondisi yang disebut.
- Komponen: Dialog Cancel Report (D-DMG-08)
- Data:
  - DU-117-1: laporan `Waiting for Confirmation` atas aset `Scanner Fujitsu fi-7160 - 2`, Asset ID `SCN-2026-0002`, pelapor `Dewi A`.
  - DU-117-2: perubahan status oleh admin `Rina W` yang menjadikan laporan DU-117-1 berstatus `Rejected`.
  - DU-117-3: perubahan status oleh `System` atas laporan DU-117-1.
- Kondisi:
  - K1: laporan DU-117-1 ditampilkan di dialog; respons simpan sukses.
  - K2: laporan DU-117-1; respons simpan lambat lalu sukses.
  - K3: laporan DU-117-1; respons simpan pertama gagal karena error server, respons berikutnya sukses.
  - K4: laporan DU-117-1; permintaan simpan melewati batas waktu.
  - K5: laporan DU-117-1; respons simpan menyatakan status laporan sudah diubah oleh `Rina W` (DU-117-2); sesudah muat ulang laporan berstatus `Rejected`.
  - K6: laporan DU-117-1; respons simpan menyatakan status laporan sudah diubah oleh `System` (DU-117-3).

## Test Steps

### Isi dialog Cancel Report
1. Tampilkan Dialog Cancel Report dengan kondisi K1
2. Verifikasi judul dialog `Cancel Report`
3. Verifikasi nama aset `Scanner Fujitsu fi-7160 - 2` tampil pada dialog Cancel Report
4. Verifikasi pertanyaan penutup `Are you sure you want to cancel it?` tampil
5. Verifikasi tombol `[Go Back]` tampil
6. Verifikasi tombol `[Cancel Report]` tampil

### Cancel Report sukses menampilkan toast
7. Tampilkan Dialog Cancel Report dengan kondisi K1
8. Klik `[Cancel Report]`
9. Verifikasi toast `Success, report has been canceled.` tampil
10. Verifikasi dialog Cancel Report tertutup sesudah simpan sukses

### Go Back menutup dialog tanpa toast
11. Tampilkan Dialog Cancel Report dengan kondisi K1
12. Klik `[Go Back]`
13. Verifikasi dialog Cancel Report tertutup oleh `[Go Back]`
14. Verifikasi tidak ada toast yang tampil sesudah `[Go Back]`

### Saving state selama Cancel Report berjalan
15. Tampilkan Dialog Cancel Report dengan kondisi K2
16. Klik `[Cancel Report]`
17. Verifikasi tombol `[Cancel Report]` berada dalam saving state dan tidak bisa diklik
18. Verifikasi tombol `[Go Back]` tidak bisa diklik selama simpan berjalan
19. Klik `[Cancel Report]` sekali lagi
20. Verifikasi hanya satu permintaan Cancel Report yang terkirim

### Gagal 5xx lalu berhasil sesudah pulih
21. Tampilkan Dialog Cancel Report dengan kondisi K3
22. Klik `[Cancel Report]`
23. Verifikasi toast `Error, failed to cancel report.` tampil
24. Verifikasi dialog Cancel Report tetap terbuka sesudah simpan gagal
25. Verifikasi tombol `[Cancel Report]` aktif lagi sesudah simpan gagal
26. Klik `[Cancel Report]`
27. Verifikasi toast `Success, report has been canceled.` tampil pada pengiriman ulang

### Timeout pada Cancel Report
28. Tampilkan Dialog Cancel Report dengan kondisi K4
29. Klik `[Cancel Report]`
30. Verifikasi toast `Connection problem. Please try again.` tampil untuk Cancel Report yang melewati batas waktu
31. Verifikasi dialog Cancel Report tetap terbuka sesudah timeout dengan tombol `[Cancel Report]` aktif

### Laporan sudah diputuskan admin menampilkan Already Changed
32. Tampilkan Dialog Cancel Report dengan kondisi K5
33. Klik `[Cancel Report]`
34. Verifikasi dialog `Already Changed` tampil
35. Verifikasi dialog `Already Changed` memuat pesan `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` berisi `Rina W`
36. Verifikasi tombol `[Reload]` tampil pada dialog `Already Changed`
37. Klik `[Reload]`
38. Verifikasi status laporan `Scanner Fujitsu fi-7160 - 2` ditampilkan ulang sebagai `Rejected`

### Pelaku perubahan status adalah System
39. Tampilkan Dialog Cancel Report dengan kondisi K6
40. Klik `[Cancel Report]`
41. Verifikasi dialog `Already Changed` memuat pesan `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` berisi `System`
