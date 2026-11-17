---
id: TC-FA-MYASSET-UI-112-tabel-borrowed-state-data-dan-download
title: "Tabel Borrowed: empty state, kosong tersaring, gagal muat, loading, dan Download gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§4.3#r8", "§5#r6", "§7.1#r2", "§7.1#r5", "§7.3#r13", "EB-TBL-1@tabel-borrowed", "EB-DL-2@tabel-borrowed", "EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "§4.3#r8": [18, 19, 20, 22]
  "§5#r6": [26, 31]
  "§7.1#r2": [2, 3, 4, 9]
  "§7.1#r5": [12, 13, 16]
  "§7.3#r13": [26, 31]
  "EB-TBL-1@tabel-borrowed": [5, 10, 12, 14]
  "EB-DL-2@tabel-borrowed": [26, 27, 31]
  "EB-DL-5": [35, 36, 38, 43, 48]
anchor: [42, 47]
coverage:
  web: automated
---

# Tabel Borrowed: empty state, kosong tersaring, gagal muat, loading, dan Download gagal

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > tab Borrowed.
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-112-1: baris pinjaman dengan Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0147`, Source `Self-service`, Duration `4 days`, Handed Over At `07/11/26, 09:10`.
  - DU-112-2: kata kunci Search `Printer`.
  - DU-112-3: 4.999 baris pinjaman dengan Name `Scanner Zebra DS2208 - {n}` (n dari 1 sampai 4999), Asset ID `SCN-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-112-4: 5.000 baris pinjaman dengan Name `Scanner Zebra DS2208 - {n}` (n dari 1 sampai 5000), Asset ID `SCN-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-112-5: 5.001 baris pinjaman dengan Name `Scanner Zebra DS2208 - {n}` (n dari 1 sampai 5001), Asset ID `SCN-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - Nama berkas Download tab Borrowed adalah `My-Asset-Borrowed`, tanpa ekstensi.
- Kondisi:
  - K1: daftar Borrowed kosong untuk Borrower, tanpa Search maupun filter aktif.
  - K2: daftar berisi DU-112-1, dan pencarian dengan kata kunci DU-112-2 dijawab dengan nol baris. Date Format bernilai `dd/MM/yy`.
  - K3: memuat daftar gagal karena error server, dan permintaan ulang sesudahnya dijawab dengan DU-112-1. Date Format bernilai `dd/MM/yy`.
  - K4: memuat daftar lambat: jawaban berisi DU-112-1 baru tiba sesudah beberapa saat. Date Format bernilai `dd/MM/yy`.
  - K5: daftar berisi DU-112-1, dan permintaan berkas Download dijawab dengan error server. Date Format bernilai `dd/MM/yy`.
  - K6: daftar berisi DU-112-5 (di atas ambang `5.000` baris), dan berkas Download baru siap sesudah beberapa saat.
  - K7: daftar berisi DU-112-4 (tepat di ambang `5.000` baris), dan berkas Download siap segera.
  - K8: daftar berisi DU-112-3 (di bawah ambang `5.000` baris), dan berkas Download siap segera.

## Test Steps

### Empty state saat belum ada pinjaman
1. Tampilkan Tabel Borrowed dengan kondisi K1
2. Verifikasi `You're not borrowing anything` tampil
3. Verifikasi `Assets you borrow will appear here.` tampil
4. Verifikasi empty state tab Borrowed tidak memiliki tombol aksi
5. Verifikasi `No results found` tidak tampil pada tabel yang kosong tanpa Search dan filter

### Kosong akibat Search
6. Tampilkan Tabel Borrowed dengan kondisi K2
7. Klik ikon Search
8. Ketik Search `Printer`, tekan Enter
9. Verifikasi `No results found` dan `Try adjusting your search or filter.` tampil
10. Verifikasi `You're not borrowing anything` tidak tampil pada hasil Search yang kosong

### Gagal memuat daftar
11. Tampilkan Tabel Borrowed dengan kondisi K3
12. Verifikasi `Unable to load this data.` tampil pada tab Borrowed
13. Verifikasi tombol `[Try Again]` tampil pada tab Borrowed
14. Verifikasi `You're not borrowing anything` tidak tampil pada keadaan gagal muat
15. Klik `[Try Again]`
16. Verifikasi `Laptop Dell Latitude 5420 - 2` tampil sesudah `[Try Again]` diklik

### Memuat daftar
17. Tampilkan Tabel Borrowed dengan kondisi K4
18. Verifikasi header kolom `Name` tetap tampil selama data dimuat
19. Verifikasi tabel berada dalam keadaan memuat data
20. Verifikasi `Laptop Dell Latitude 5420 - 2` belum tampil selama data dimuat
21. Waktu berlalu sampai jawaban daftar tiba
22. Verifikasi `Laptop Dell Latitude 5420 - 2` tampil sesudah data dimuat

### Download CSV gagal
23. Tampilkan Tabel Borrowed dengan kondisi K5
24. Klik ikon Download
25. Klik `Download as CSV`
26. Verifikasi `Error, failed to download My-Asset-Borrowed.` tampil
27. Verifikasi toast tidak memiliki tombol aksi seperti `[Try Again]`

### Download XLSX gagal
28. Tampilkan Tabel Borrowed dengan kondisi K5
29. Klik ikon Download
30. Klik `Download as XLSX`
31. Verifikasi `Error, failed to download My-Asset-Borrowed.` tampil untuk Download XLSX

### Download di atas ambang 5.000 baris
32. Tampilkan Tabel Borrowed dengan kondisi K6
33. Klik ikon Download
34. Klik `Download as CSV`
35. Verifikasi loading screen tampil selama berkas disiapkan
36. Verifikasi tidak ada toast informasional selama berkas disiapkan
37. Waktu berlalu sampai berkas siap
38. Verifikasi loading screen tidak tampil lagi sesudah berkas siap

### Download tepat di ambang 5.000 baris
39. Tampilkan Tabel Borrowed dengan kondisi K7
40. Klik ikon Download
41. Klik `Download as CSV`
42. Verifikasi `Scanner Zebra DS2208 - 1` tampil
43. Verifikasi tidak ada toast informasional sesudah Download pada `5.000` baris

### Download di bawah ambang 5.000 baris
44. Tampilkan Tabel Borrowed dengan kondisi K8
45. Klik ikon Download
46. Klik `Download as XLSX`
47. Verifikasi `Scanner Zebra DS2208 - 2` tampil
48. Verifikasi tidak ada toast informasional sesudah Download pada `4.999` baris
