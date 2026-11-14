---
id: TC-FA-FATR-E2E-013-overrides-search
title: "Search tabel Overrides"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [§4.1#r239, §4.1#r241, §4.1#r242, §4.1#r244, §4.1#r240, §5#r3, EB-SRC-2@tabel-overrides, EB-SRC-3@tabel-overrides, EB-SRC-1]
smoke: [EB-SRC-1]
dependsOn: []
trace:
  §4.1#r239: [7, 8, 39, 40]
  §4.1#r241: [13, 14]
  §4.1#r242: [16, 18]
  §4.1#r244: [20, 22, 26]
  §4.1#r240: [10, 11]
  §5#r3: [7, 10, 13, 16, 26, 36]
  EB-SRC-2@tabel-overrides: [10, 36, 37, 44]
  EB-SRC-3@tabel-overrides: [46, 48, 50, 52]
  EB-SRC-1: [30, 32, 34]
anchor: [5, 42]
coverage:
  web: automated
---

# Search tabel Overrides

## Prerequisites
- Aktor: Total Control `Rina Wulandari`.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-013-1: Category leaf `Machinery {runId}`, ada di entitas aktor.
  - DU-013-2: Group tingkat atas `Proyek Karawang {runId}`.
  - DU-013-3: Group tingkat atas `Max Pool {runId}`.
  - DU-013-4: Asset Name `Excavator PC200 {runId}`, Code `EXC13-{runId}`, Category `Machinery {runId}`, UoM `Unit`.
  - DU-013-5: aset `Excavator PC200 {runId} - 1`, ber-Group `Proyek Karawang {runId}` dan Category `Machinery {runId}`.
  - DU-013-6: override Group `Proyek Karawang {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max duration (30 days)`, dibuat oleh `Rina Wulandari`; kata kunci Search yang dipakai atasnya: `Karawang {runId}`, `rawang {runId}`, `KARAWANG {runId}`, `Zzqx {runId}`, ` Karawang {runId} `, dan `ProyekKarawang {runId}`.
  - DU-013-7: override Asset Name `Excavator PC200 {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Max extensions (2)`, dibuat oleh `Rina Wulandari`.
  - DU-013-8: override Asset `Excavator PC200 {runId} - 1` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Allow Borrow (Deny)`, dibuat oleh `Rina Wulandari`.
  - DU-013-9: override Group `Max Pool {runId}` di Category `Machinery {runId}` transaksi `Borrow`, Overridden `Allow Borrow (Allow)`, dibuat oleh `Rina Wulandari`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Kolom `Category` tabel Overrides tidak ditampilkan (bawaan) untuk `Rina Wulandari`.
  - Keempat override dibuat pada hari yang sama, T0.

## Test Steps

### Search mencocokkan kolom Scope, Target, Overridden, dan Created By
1. Ketik Search Sidebar Category Tree `Machinery {runId}`, tekan Enter
2. Klik node `Machinery {runId}` di Sidebar Category Tree
3. Klik tab `Borrow`
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi keempat baris data uji tampil di tabel Overrides: Target `Proyek Karawang {runId}`, Target `Excavator PC200 {runId}`, Target `Excavator PC200 {runId} - 1`, dan Target `Max Pool {runId}`
6. Ganti isi kotak Search dengan `Asset Name`, tekan Enter
7. Verifikasi baris dengan Scope `Asset Name` dan Target `Excavator PC200 {runId}` tampil karena kolom Scope ikut dicari
8. Verifikasi baris dengan Scope `Asset` dan Target `Excavator PC200 {runId} - 1`, baris `Proyek Karawang {runId}`, dan baris `Max Pool {runId}` tidak tampil
9. Ganti isi kotak Search dengan `Karawang {runId}`, tekan Enter
10. Verifikasi baris dengan Scope `Group` dan Target `Proyek Karawang {runId}` tampil karena kolom Target ikut dicari pada badge Group
11. Verifikasi baris `Max Pool {runId}` dan baris `Excavator PC200 {runId}` tidak tampil
12. Ganti isi kotak Search dengan `Max extensions`, tekan Enter
13. Verifikasi baris dengan Target `Excavator PC200 {runId}` dan Overridden `Max extensions (2)` tampil karena kolom Overridden ikut dicari
14. Verifikasi baris `Proyek Karawang {runId}` tidak tampil karena Overridden `Max duration (30 days)` tidak memuat `Max extensions`
15. Ganti isi kotak Search dengan `Rina W`, tekan Enter
16. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Created By `Rina W` tampil karena kolom Created By ikut dicari
17. Ganti isi kotak Search dengan `Budi S`, tekan Enter
18. Verifikasi baris `Proyek Karawang {runId}` tidak tampil karena tidak ada override data uji yang dibuat oleh `Budi S`

### Search mengikuti visibilitas kolom Category
19. Ganti isi kotak Search dengan `{runId}`, tekan Enter
20. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil di tabel Overrides sebelum kolom Category dicari
21. Ganti isi kotak Search dengan `Machinery {runId}`, tekan Enter
22. Verifikasi `No results found` tampil di tabel Overrides karena kolom Category belum ditampilkan
23. Klik header kolom Actions pada tabel Overrides
24. Centang kolom `Category`
25. Ganti isi kotak Search dengan `Machinery {runId}` lagi, tekan Enter
26. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Category `Machinery {runId}` tampil karena kolom Category ditampilkan dan ikut dicari
27. Klik header kolom Actions pada tabel Overrides
28. Hapus centang kolom `Category`

### Search memakai substring, tanpa membedakan huruf besar dan kecil, dan menampilkan empty state bila tanpa hasil
29. Ganti isi kotak Search dengan `rawang {runId}`, tekan Enter
30. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil karena kata kunci cocok sebagai substring di tengah nama
31. Ganti isi kotak Search dengan `KARAWANG {runId}`, tekan Enter
32. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil karena huruf besar dan huruf kecil sama-sama cocok
33. Ganti isi kotak Search dengan `Zzqx {runId}`, tekan Enter
34. Verifikasi `No results found` tampil di tabel Overrides untuk kata kunci `Zzqx {runId}`

### Kata kunci cocok di dua kolom berbeda dan satu nilai memuat nilai lain
35. Ganti isi kotak Search dengan `Max`, tekan Enter
36. Verifikasi baris dengan Target `Max Pool {runId}` dan baris dengan Target `Excavator PC200 {runId}` serta Overridden `Max extensions (2)` tampil karena `Max` cocok di kolom Target dan di kolom Overridden
37. Verifikasi baris dengan Target `Excavator PC200 {runId} - 1` dan Overridden `Allow Borrow (Deny)` tidak tampil
38. Ganti isi kotak Search dengan `Asset`, tekan Enter
39. Verifikasi baris dengan Scope `Asset Name` dan Target `Excavator PC200 {runId}` serta baris dengan Scope `Asset` dan Target `Excavator PC200 {runId} - 1` tampil karena nilai `Asset` juga substring dari nilai `Asset Name`
40. Verifikasi baris `Max Pool {runId}` tidak tampil

### Tanggal tidak dicari, spasi dibuang di tepi, dan karakter khusus dicari sebagai teks
41. Ganti isi kotak Search dengan `{runId}`, tekan Enter
42. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan baris dengan Target `Max Pool {runId}` tampil di tabel Overrides sebelum kata kunci tanggal dicari
43. Ganti isi kotak Search dengan tanggal T0 dalam Date Format `dd/MM/yy`, tekan Enter
44. Verifikasi baris `Proyek Karawang {runId}` dan baris `Max Pool {runId}` tidak tampil karena kolom Created At tidak ikut dicari
45. Ganti isi kotak Search dengan ` Karawang {runId} `, tekan Enter
46. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil karena spasi di awal dan akhir kata kunci dibuang
47. Ganti isi kotak Search dengan `Proyek Karawang {runId}`, tekan Enter
48. Verifikasi baris dengan Target `Proyek Karawang {runId}` tampil karena spasi di tengah kata kunci dipertahankan
49. Ganti isi kotak Search dengan `ProyekKarawang {runId}`, tekan Enter
50. Verifikasi `No results found` tampil di tabel Overrides karena kata kunci tanpa spasi di tengah tidak cocok
51. Ganti isi kotak Search dengan `%`, tekan Enter
52. Verifikasi baris `Proyek Karawang {runId}` tidak tampil karena `%` dicari sebagai teks
