---
id: TC-FA-MISS-E2E-006-tab-active-download
title: "Tab Active: nama berkas, cakupan baris menurut Search dan Filter, kolom tersembunyi tidak ikut"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§5#r6, EB-DL-1@tabel-active, EB-DL-3@tabel-active, §8.2#b3, EB-DL-2@tabel-active, EB-DL-4]
smoke: [EB-DL-2@tabel-active, EB-DL-4]
dependsOn: []
trace:
  §5#r6: [2, 4]
  EB-DL-1@tabel-active: [6, 7, 15, 18, 24, 35, 42, 55]
  EB-DL-3@tabel-active: [4, 10]
  §8.2#b3: 46
  EB-DL-2@tabel-active: 5
  EB-DL-4: [29, 30, 42]
anchor: [39, 50]
coverage:
  web: automated
---

# Tab Active: nama berkas, cakupan baris menurut Search dan Filter, kolom tersembunyi tidak ikut

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets, tab Missing, sub-tab Active.
- Data:
  - DU-006-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-006-2: Group `Gudang Unduh {runId}` sebagai anak dari Group `Kantor Unduh {runId}`, sehingga hierarki penuhnya `Kantor Unduh {runId} > Gudang Unduh {runId}`.
  - DU-006-3: User `Wulan Prasetyo {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing.
  - DU-006-4: Sepuluh record `Missing` untuk sepuluh aset ber-nama sama `Unduh Aset {runId}` (Group `Gudang Unduh {runId}`, Brand `Kenmore {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`; record ke-n dilaporkan T0 − n hari pukul `09:00` sehingga Days Missing-nya n hari.
  - DU-006-5: Record `Waiting for Confirmation` untuk aset `Unduh Tunggu A {runId}` (Group `Gudang Unduh {runId}`, Brand `Kenmore {runId}`), Source `Reported by holder`, Last Holder `Wulan Prasetyo {runId}`, Reported By `Wulan Prasetyo {runId}`, dilaporkan T0 − 20 hari pukul `08:00`.
  - DU-006-7: Record `Waiting for Confirmation` untuk aset `Unduh Tunggu B {runId}` (Group `Gudang Unduh {runId}`, Brand `Kenmore {runId}`), Source `Reported by holder`, Last Holder `Wulan Prasetyo {runId}`, Reported By `Wulan Prasetyo {runId}`, dilaporkan T0 − 20 hari pukul `08:30`.
  - DU-006-8: Record `Found` untuk aset `Unduh Selesai {runId}` (Group `Gudang Unduh {runId}`, Brand `Kenmore {runId}`), Source `Manual`, Reported By `Rina Wijaya {runId}`; record ini sudah selesai sehingga hanya ada di tab History.
  - DU-006-6: kata kunci Search `{runId} tidakada` yang tidak cocok dengan kolom mana pun.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; Reported Date pada entri di atas dihitung relatif terhadap T0.
  - Ukuran halaman bernilai bawaan `10`, sehingga kedua belas record spec ini tidak muat dalam satu halaman.
  - Konfigurasi kolom milik aktor masih bawaan: kolom `Source` tampil dan kolom `Brand` tersembunyi.

## Test Steps

### Berkas CSV tanpa saringan memuat semua baris, tidak dibatasi halaman
1. Klik `Download` pada toolbar
2. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
3. Klik `Download as CSV`
4. Verifikasi berkas `Missing-Active.csv` terunduh
5. Verifikasi tidak ada toast sukses sesudah unduhan
6. Verifikasi berkas memuat baris untuk kedua belas record spec ini, termasuk yang tidak tampil di halaman 1 tabel
7. Verifikasi baris header berkas memuat kolom yang tampil dan tidak memuat kolom `Brand` yang tersembunyi

### Berkas XLSX memakai ekstensi sesuai pilihan
8. Klik `Download` pada toolbar
9. Klik `Download as XLSX`
10. Verifikasi berkas `Missing-Active.xlsx` terunduh dan memuat satu sheet bernama `Sheet1`

### Berkas hanya memuat hasil Search dan Filter yang aktif
11. Ketik Search `{runId}`, tekan Enter
12. Klik ikon Filter
13. Pada field `Status` pilih opsi `Missing`
14. Klik `[Apply]`
15. Verifikasi tabel memuat sepuluh baris `Unduh Aset {runId}` dan tidak memuat baris `Unduh Tunggu A {runId}` maupun `Unduh Tunggu B {runId}`
16. Klik `Download` pada toolbar
17. Klik `Download as CSV`
18. Verifikasi berkas memuat sepuluh baris `Unduh Aset {runId}` dan tidak memuat baris `Unduh Tunggu A {runId}` maupun `Unduh Tunggu B {runId}`, walau tabel hanya menampilkan sepuluh baris di halaman 1
19. Klik `[Clear Field]`
20. Klik `[Apply]`

### Urutan baris berkas mengikuti sort aktif
21. Klik header `Days Missing`
22. Klik `Download` pada toolbar
23. Klik `Download as CSV`
24. Verifikasi baris berkas berurutan menurut Days Missing dari yang terkecil: sepuluh baris `Unduh Aset {runId}` dengan Days Missing 1 sampai 10, lalu baris `Unduh Tunggu A {runId}` dan `Unduh Tunggu B {runId}` dengan Days Missing 20
25. Klik header `Days Missing`
26. Klik header `Days Missing`

### Isi berkas per tipe kolom
27. Klik `Download` pada toolbar
28. Klik `Download as CSV`
29. Verifikasi kolom Group pada berkas memuat hierarki penuh `Kantor Unduh {runId} > Gudang Unduh {runId}`
30. Verifikasi kolom Last Holder pada baris `Unduh Aset {runId}` berisi `-`, dan pada baris `Unduh Tunggu A {runId}` berisi nama lengkap `Wulan Prasetyo {runId}`

### Kolom yang disembunyikan tidak ikut berkas
31. Klik header kolom Actions
32. Hapus centang kolom `Source`
33. Klik `Download` pada toolbar
34. Klik `Download as CSV`
35. Verifikasi baris header berkas tidak memuat kolom `Source` dan tetap memuat kolom `Last Holder`
36. Klik header kolom Actions
37. Centang kolom `Source`

### Nol baris tetap menghasilkan berkas berisi header saja
38. Ganti isi kotak search dengan `{runId} tidakada`, tekan Enter
39. Verifikasi tabel tidak memuat baris spec ini karena kata kunci tidak cocok
40. Klik `Download` pada toolbar
41. Klik `Download as CSV`
42. Verifikasi berkas hanya memuat baris header kolom yang tampil tanpa baris data, dan tidak ada toast
43. Ganti isi kotak search dengan `{runId}`, tekan Enter

### Download tidak dicatat di Missing Log
44. Klik `⋯` pada baris `Unduh Tunggu A {runId}`
45. Klik `Missing Log` pada menu
46. Verifikasi dialog `Missing Log` memuat satu node `Reported missing by` dan tidak memuat node lain
47. Tekan Esc untuk menutup dialog `Missing Log`

### Berkas tab Active tidak memuat record tab History
48. Klik sub-tab `History`
49. Ketik Search `{runId}`, tekan Enter
50. Verifikasi baris `Unduh Selesai {runId}` tampil di tab History dengan Status `Found`
51. Klik sub-tab `Active`
52. Ketik Search `{runId}`, tekan Enter
53. Klik `Download` pada toolbar
54. Klik `Download as CSV`
55. Verifikasi berkas `Missing-Active.csv` tidak memuat baris `Unduh Selesai {runId}` karena record itu hanya ada di tab History
