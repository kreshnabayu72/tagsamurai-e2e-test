---
id: TC-FA-FAFM-UI-088-modal-changelog-tampilan-dan-state
title: "Modal Changelog: format sel, nilai kosong, dan state data"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-09a", "S-05", "S-29a", "S-29b", "T-FAFM-04", "EB-TBL-1@tabel-changelog", "EB-TBL-2@tabel-changelog", "EB-TBL-4@tabel-changelog", "EB-FLT-6@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "INV-09a": 2
  "S-05": [25, 28, 31]
  "S-29a": [25, 26, 28, 29, 31, 32]
  "S-29b": [35, 36]
  "T-FAFM-04": [4, 5, 6, 7, 9, 10]
  "EB-TBL-1@tabel-changelog": [25, 28, 31, 35, 38, 39, 41]
  "EB-TBL-2@tabel-changelog": 8
  "EB-TBL-4@tabel-changelog": [12, 13, 14, 15, 16, 17, 19, 21, 23]
  "EB-FLT-6@tabel-changelog": [46, 47, 51, 52, 53, 55, 56]
anchor: [50]
coverage:
  web: automated
---

# Modal Changelog: format sel, nilai kosong, dan state data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Komponen: Modal Changelog
- Data:
  - DU-088-1: Entri Changelog Date `2026-11-14 02:00`, Action `Permanently Delete`, File Name `old-label.png`, Field `File Name`, Old Value `old-label.png`, tanpa New Value, Modified By `System`.
    - Date yang diharapkan tampil `14/11/26 02:00`, dari `2026-11-14 02:00` dengan Date Format `dd/MM/yy` dan Time Format `HH:mm`.
  - DU-088-2: Entri Changelog Date `2026-11-01 10:00`, Action `Delete`, File Name `damage-01.jpg`, Field `File Name`, Old Value `damage-01.jpg`, tanpa New Value, Modified By `Rina Anggraini`.
    - Modified By yang diharapkan tampil `Rina A`, dengan nama lengkap `Rina Anggraini` saat hover.
  - DU-088-3: Entri Changelog Date `2026-10-20 13:45`, Action `Delete`, File Name `calibration-cert.pdf`, Field `File Name`, Old Value `calibration-cert.pdf`, tanpa New Value, Modified By `Alexander Graham Bell`.
    - Modified By yang diharapkan tampil `Alexander G`, dengan nama lengkap `Alexander Graham Bell` saat hover.
  - DU-088-4: Entri Changelog Date `2026-10-18 09:10`, Action `Delete`, File Name `warranty-card-mon0007.pdf`, Field `File Name`, Old Value `warranty-card-mon0007.pdf`, tanpa New Value, Modified By `Buzzlightyear Sumardi`.
    - Modified By yang diharapkan tampil `Buzzlightyear S`.
  - DU-088-5: Entri Changelog Date `2026-11-10 08:15`, Action `Delete`, File Name `draft-photo-01.jpg`, Field `File Name`, Old Value `draft-photo-01.jpg`, tanpa New Value, Modified By `Budi`.
  - DU-088-6: Entri Changelog Date `2026-10-22 11:20`, Action `Delete`, File Name `handover-brw0150.jpg`, Field `File Name`, Old Value `handover-brw0150.jpg`, tanpa New Value, Modified By `Dewi Anggraini`.
    - Modified By yang diharapkan tampil `Dewi A`, dengan nama lengkap `Dewi Anggraini` saat hover.
  - DU-088-7: Entri Changelog Date `2026-10-22 11:40`, Action `Delete`, File Name `handover-brw0151.jpg`, Field `File Name`, Old Value `handover-brw0151.jpg`, tanpa New Value, Modified By `Dewi Anggreni`.
    - Modified By yang diharapkan tampil `Dewi A`, dengan nama lengkap `Dewi Anggreni` saat hover.
  - DU-088-8: Daftar Changelog entitas tanpa file sama sekali.
  - DU-088-9: Daftar Changelog entitas yang memiliki file `laptop-front.jpg` tetapi belum ada Delete atau Permanently Delete yang tercatat.
  - DU-088-10: Entri Changelog atas file kelompok Purchase `invoice-lpt0004.pdf` yang tidak terlihat oleh role aktor.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.
  - K1: daftar berisi DU-088-1 sampai DU-088-7.
  - K2: daftar kosong, entitas tanpa file (DU-088-8), tanpa Search dan Filter aktif.
  - K3: daftar kosong, belum ada aksi yang tercatat (DU-088-9), tanpa Search dan Filter aktif.
  - K4: daftar kosong untuk aktor, karena satu-satunya entri (DU-088-10) tidak terlihat oleh role aktor.
  - K5: daftar berisi DU-088-1 sampai DU-088-7, dan Search `log-tidak-ada.png` tidak cocok dengan satu pun baris sehingga respons kosong.
  - K6: memuat daftar gagal karena error server pada percobaan pertama, dan percobaan berikutnya berhasil memuat DU-088-1 sampai DU-088-7.

## Test Steps

### Modal Changelog memuat tabel entri
1. Tampilkan Modal Changelog dengan kondisi K1
2. Verifikasi tabel dengan baris `old-label.png` tampil di dalam modal

### Format sel entri Changelog
3. Tampilkan Modal Changelog dengan kondisi K1
4. Verifikasi baris `old-label.png` menampilkan `14/11/26 02:00` pada kolom `Date`
5. Verifikasi baris `old-label.png` menampilkan `Permanently Delete` pada kolom `Action`
6. Verifikasi baris `old-label.png` menampilkan `File Name` pada kolom `Field`
7. Verifikasi baris `old-label.png` menampilkan `old-label.png` pada kolom `Old Value`
8. Verifikasi baris `old-label.png` menampilkan `—` pada kolom `New Value`
9. Verifikasi baris `damage-01.jpg` menampilkan `Delete` pada kolom `Action`
10. Verifikasi baris `old-label.png` menampilkan `System` pada kolom `Modified By`

### Nama pengguna pada Modified By tampil singkat dan lengkap saat hover
11. Tampilkan Modal Changelog dengan kondisi K1
12. Verifikasi baris `damage-01.jpg` menampilkan `Rina A` pada kolom `Modified By`
13. Verifikasi baris `calibration-cert.pdf` menampilkan `Alexander G` pada kolom `Modified By`
14. Verifikasi baris `warranty-card-mon0007.pdf` menampilkan `Buzzlightyear S` pada kolom `Modified By`
15. Verifikasi baris `draft-photo-01.jpg` menampilkan `Budi` pada kolom `Modified By`
16. Verifikasi baris `handover-brw0150.jpg` menampilkan `Dewi A` pada kolom `Modified By`
17. Verifikasi baris `handover-brw0151.jpg` menampilkan `Dewi A` pada kolom `Modified By`
18. Arahkan kursor ke `Alexander G` pada baris `calibration-cert.pdf`
19. Verifikasi nama lengkap `Alexander Graham Bell` tampil pada kolom `Modified By`
20. Arahkan kursor ke `Dewi A` pada baris `handover-brw0150.jpg`
21. Verifikasi nama lengkap `Dewi Anggraini` tampil pada kolom `Modified By`
22. Arahkan kursor ke `Dewi A` pada baris `handover-brw0151.jpg`
23. Verifikasi nama lengkap `Dewi Anggreni` tampil pada kolom `Modified By`

### Changelog kosong karena entitas tanpa file
24. Tampilkan Modal Changelog dengan kondisi K2
25. Verifikasi judul empty state `No changelog yet`
26. Verifikasi deskripsi empty state `Activities and changes will appear here.`

### Changelog kosong karena belum ada aksi tercatat
27. Tampilkan Modal Changelog dengan kondisi K3
28. Verifikasi judul empty state `No changelog yet`
29. Verifikasi deskripsi empty state `Activities and changes will appear here.`

### Changelog kosong karena entri tidak terlihat oleh aktor
30. Tampilkan Modal Changelog dengan kondisi K4
31. Verifikasi judul empty state `No changelog yet`
32. Verifikasi deskripsi empty state `Activities and changes will appear here.`

### Search tanpa hasil menampilkan empty state tersaring
33. Tampilkan Modal Changelog dengan kondisi K5
34. Ketik Search `log-tidak-ada.png`, tekan Enter
35. Verifikasi judul empty state `No results found` pada modal Changelog
36. Verifikasi deskripsi empty state `Try adjusting your search or filter.` pada modal Changelog

### Gagal memuat bukan empty state dan bisa dimuat ulang
37. Tampilkan Modal Changelog dengan kondisi K6
38. Verifikasi pesan `Unable to load this data.` pada modal Changelog
39. Verifikasi tombol `[Try Again]` pada modal Changelog
40. Klik `[Try Again]`
41. Verifikasi baris `old-label.png` tampil

### Menyembunyikan kolom tidak menghapus field filter dan tidak membatalkan filter ter-Apply
42. Tampilkan Modal Changelog dengan kondisi K1
43. Klik ikon `Filter` pada toolbar modal
44. Pilih `Delete` pada field `Action` di Filter Panel
45. Klik `[Apply]`
46. Verifikasi baris `damage-01.jpg` tampil pada tabel
47. Verifikasi baris `old-label.png` tidak tampil pada tabel
48. Klik header kolom Actions `⋯`
49. Hilangkan centang kolom `Action` pada panel Column Visibility
50. Verifikasi header kolom `Date` tetap tampil pada tabel
51. Verifikasi header kolom `Action` tidak tampil pada tabel
52. Verifikasi baris `damage-01.jpg` tetap tampil pada tabel
53. Verifikasi baris `old-label.png` tetap tidak tampil pada tabel
54. Klik ikon `Filter` pada toolbar modal
55. Verifikasi field `Action` tetap ada pada Filter Panel dengan pilihan `Delete`
56. Verifikasi titik penanda filter aktif tetap tampil pada ikon `Filter` modal Changelog
