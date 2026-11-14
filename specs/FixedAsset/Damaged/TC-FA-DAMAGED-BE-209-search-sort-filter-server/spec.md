---
id: TC-FA-DAMAGED-BE-209-search-sort-filter-server
title: "Server mencari per kelas kolom searchable, mengurutkan per tipe data dengan Status per label dan nilai kosong di ujung, menyaring AND antar-field dan OR dalam Status termasuk penanda, dan menyediakan opsi DISTINCT dalam cakupan Group"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-DMG-01", "T-DMG-02", "§5#r3", "§9.5#r2", "§9.5#r3", "§9.5#r7", "§9.2#b4", "EB-SRC-1", "EB-SRT-1", "EB-SRT-2", "EB-FLT-3"]
smoke: []
dependsOn: []
owner: BE
trace:
  "T-DMG-01": [2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 42, 46, 48, 50, 52]
  "T-DMG-02": [38, 40, 56, 59]
  "§5#r3": [2, 4, 6, 8, 10, 12, 14, 16, 18]
  "§9.5#r2": 36
  "§9.5#r3": 38
  "§9.5#r7": [46, 48, 54, 56]
  "§9.2#b4": [50, 52]
  "EB-SRC-1": [2, 20]
  "EB-SRT-1": [22, 24, 26, 28, 30, 40]
  "EB-SRT-2": [32, 34, 36, 61, 63, 65]
  "EB-FLT-3": [42, 44, 46]
---

# Server mencari per kelas kolom searchable, mengurutkan per tipe data dengan Status per label dan nilai kosong di ujung, menyaring AND antar-field dan OR dalam Status termasuk penanda, dan menyediakan opsi DISTINCT dalam cakupan Group

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, seluruh client.
  - Group Manager `Gunawan Hartono {runId}`, binaan Group `Head Office {runId}` beserta sub-group.
- Data:
  - DU-209-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-209-2: User `Gunawan Hartono {runId}`, Group Manager, cakupan Group `Head Office {runId}` beserta sub-group.
  - DU-209-3: Group `Head Office {runId}`.
  - DU-209-4: Group `Warehouse {runId}`.
  - DU-209-5: Group `Gudang Lama {runId}`, yang kemudian diganti nama menjadi `Gudang Baru {runId}`.
  - DU-209-6: Nama baru `Gudang Baru {runId}` untuk Group `Gudang Lama {runId}`.
  - DU-209-7: Aset `Laptop Lenovo ThinkPad - 1 {runId}`, Asset ID `LPT-0001-{runId}`, Brand `Lenovo {runId}`, Group `Head Office {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Budi S`, Reported By `—`, Reported Date `T0 − 9 hari, pukul 08:15`, Purchase Cost `12500000`, sub-tab Active.
  - DU-209-8: Aset `Laptop Lenovo ThinkPad - 2 {runId}`, Asset ID `LPT-0002-{runId}`, Brand `Lenovo {runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 7 hari, pukul 09:30`, Purchase Cost `4500000`, sub-tab Active.
  - DU-209-9: Aset `Laptop Lenovo ThinkPad - 10 {runId}`, Asset ID `LPT-0010-{runId}`, Brand `Lenovo {runId}`, Group `Head Office {runId}`, Status `Damaged` dengan penanda `Missing`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 5 hari, pukul 10:45`, Purchase Cost `7200000`, sub-tab Active.
  - DU-209-10: Aset `Printer Canon Pixma - 1 {runId}`, Asset ID `PRN-0001-{runId}`, Brand `Canon {runId}`, Group `Head Office {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 3 hari, pukul 11:00`, Purchase Cost `2100000`, sub-tab Active.
  - DU-209-11: Aset `Printer Canon Pixma - 2 {runId}`, Asset ID `PRN-0002-{runId}`, Brand `Canon {runId}`, Group `Head Office {runId}`, Status `Damaged` dengan penanda `Reported Missing`, Source `Borrowed asset`, Last Holder `Sari D`, Reported By `Agus P`, Reported Date `T0 − 11 hari, pukul 14:20`, Purchase Cost `3300000`, sub-tab Active.
  - DU-209-12: Aset `Drill Bosch GSB - 1 {runId}`, Asset ID `DRL-0001-{runId}`, Brand `Bosch {runId}`, Group `Warehouse {runId}`, Status `Damaged`, Source `Transfer receive`, Last Holder `—`, Reported By `Rina W`, Reported Date `T0 − 6 hari, pukul 13:05`, Purchase Cost `1800000`, sub-tab Active.
  - DU-209-13: Aset `Laptop Lenovo ThinkPad - 3 {runId}`, Asset ID `LPT-0003-{runId}`, Group `Head Office {runId}`, Status `Repaired`, Source `Manual`, Resolved By `Agus P`, Resolved Date `T0 − 2 hari, pukul 15:00`, sub-tab History.
  - DU-209-14: Aset `Printer Canon Pixma - 3 {runId}`, Asset ID `PRN-0003-{runId}`, Group `Head Office {runId}`, Status `Rejected`, Source `Reported by scan`, Resolved By `Rina W`, Resolved Date `T0 − 4 hari, pukul 12:10`, sub-tab History.
  - DU-209-15: Aset `Drill Bosch GSB - 2 {runId}`, Asset ID `DRL-0002-{runId}`, Group `Head Office {runId}`, Status `Disposed`, Source `Stock opname`, Resolved By `System`, Resolved Date `T0 − 1 hari, pukul 00:00`, sub-tab History.
  - DU-209-16: Aset `Printer Canon Pixma - 4 {runId}`, Asset ID `PRN-0004-{runId}`, Group `Gudang Lama {runId}`, Status `Canceled`, Source `Reported by holder`, Resolved By `Budi S`, Resolved Date `T0 − 6 hari, pukul 08:00`, sub-tab History.
  - DU-209-17: Aset `Scanner Zulu - 1 {runId}`, Asset ID `ZLU-0001-{runId}`, Brand `Zulu {runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 8 hari, pukul 09:30`, Purchase Cost `5000000`, sub-tab Active.
  - DU-209-18: Aset `Scanner Zulu - 2 {runId}`, Asset ID `ZLU-0002-{runId}`, Brand `Zulu {runId}`, Group `Head Office {runId}`, Status `Damaged`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Reported Date `T0 − 8 hari, pukul 09:30`, Purchase Cost `5000000`, sub-tab Active.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Kolom Brand dan Purchase Cost tampil di tabel `Agus Pratama {runId}` lewat Setup Column.

## Test Steps

### Search mencocokkan substring tanpa membedakan huruf besar atau kecil di kolom searchable
1. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `thinkpad - 1 {runId}`
2. Verifikasi `Laptop Lenovo ThinkPad - 1 {runId}` dan `Laptop Lenovo ThinkPad - 10 {runId}` terkembalikan karena substring dan huruf kecil sama-sama cocok
3. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `PRN-0002-{runId}`
4. Verifikasi `Printer Canon Pixma - 2 {runId}` terkembalikan karena kolom Asset ID searchable
5. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}`
6. Verifikasi `Laptop Lenovo ThinkPad - 1 {runId}`, `Laptop Lenovo ThinkPad - 2 {runId}`, dan `Laptop Lenovo ThinkPad - 10 {runId}` terkembalikan karena kolom Brand searchable
7. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Reported by holder`
8. Verifikasi `Laptop Lenovo ThinkPad - 1 {runId}` ikut terkembalikan karena kolom Source searchable
9. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Sari D`
10. Verifikasi `Printer Canon Pixma - 2 {runId}` ikut terkembalikan karena kolom Last Holder searchable
11. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `12500000`
12. Verifikasi `Laptop Lenovo ThinkPad - 1 {runId}` ikut terkembalikan karena kolom Purchase Cost searchable
13. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Damaged`
14. Verifikasi `Laptop Lenovo ThinkPad - 2 {runId}` ikut terkembalikan karena kolom Status searchable
15. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search berisi tanggal Reported Date `Laptop Lenovo ThinkPad - 2 {runId}` seperti tampil di tabel, yaitu `T0 − 7 hari` dalam format `dd/MM/yy`
16. Verifikasi `Laptop Lenovo ThinkPad - 2 {runId}` tidak terkembalikan karena Reported Date bukan kolom searchable
17. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `7 days`
18. Verifikasi `Laptop Lenovo ThinkPad - 2 {runId}` tidak terkembalikan karena Days Damaged bukan kolom searchable
19. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo-tidak-ada {runId}`
20. Verifikasi tidak ada record yang terkembalikan karena kata kunci tanpa kecocokan

### Sort sub-tab Active mengikuti tipe data, Status per label, dan nilai kosong di ujung
21. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}` dan sort Name ascending
22. Verifikasi urutan `Laptop Lenovo ThinkPad - 1 {runId}`, `Laptop Lenovo ThinkPad - 2 {runId}`, lalu `Laptop Lenovo ThinkPad - 10 {runId}` karena Increment diurutkan numerik natural
23. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}` dan sort Asset ID descending
24. Verifikasi urutan `LPT-0010-{runId}`, `LPT-0002-{runId}`, lalu `LPT-0001-{runId}`
25. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}` dan sort Reported Date Oldest First
26. Verifikasi urutan `Laptop Lenovo ThinkPad - 2 {runId}` lebih dulu daripada `Laptop Lenovo ThinkPad - 10 {runId}` karena dilaporkan lebih awal, dan sebaliknya saat Newest First
27. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `{runId}` dan sort Purchase Cost dari kecil ke besar
28. Verifikasi urutan `Laptop Lenovo ThinkPad - 2 {runId}` (`4500000`) mendahului `Laptop Lenovo ThinkPad - 10 {runId}` (`7200000`) dan `Laptop Lenovo ThinkPad - 1 {runId}` (`12500000`) secara numerik
29. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Canon {runId}` dan sort Status
30. Verifikasi urutan Status memakai label badge saja: `Printer Canon Pixma - 2 {runId}` (`Damaged` dengan penanda `Reported Missing`) mendahului `Printer Canon Pixma - 1 {runId}` (`Reported Disposal`) tanpa penanda ikut menentukan urutan
31. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}` dan sort Last Holder ascending
32. Verifikasi record dengan Last Holder kosong `—` berada di akhir
33. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Lenovo {runId}` dan sort Last Holder descending
34. Verifikasi record dengan Last Holder kosong `—` berada di awal
35. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `{runId}` tanpa sort
36. Verifikasi urutan default menempatkan `Waiting for Confirmation` di atas, lalu Days Damaged terlama dulu

### Sort default sub-tab History mengikuti Resolved Date terbaru dulu
37. Total Control `Agus Pratama {runId}` meminta daftar record History dengan Search `{runId}` tanpa sort
38. Verifikasi urutan `Drill Bosch GSB - 2 {runId}`, `Laptop Lenovo ThinkPad - 3 {runId}`, `Printer Canon Pixma - 3 {runId}`, lalu `Printer Canon Pixma - 4 {runId}` karena Resolved Date terbaru dulu
39. Total Control `Agus Pratama {runId}` meminta daftar record History dengan Search `{runId}` dan sort Resolved By ascending
40. Verifikasi `Drill Bosch GSB - 2 {runId}` dengan Resolved By `System` terurut menurut label bersama nama pelaku lain

### Filter: AND antar field dan OR dalam satu field termasuk penanda Status
41. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Filter Brand `Lenovo {runId}` dan Group `Head Office {runId}` serta Search `{runId}`
42. Verifikasi hanya `Laptop Lenovo ThinkPad - 1 {runId}`, `Laptop Lenovo ThinkPad - 2 {runId}`, dan `Laptop Lenovo ThinkPad - 10 {runId}` terkembalikan karena antar-field berlaku AND
43. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Filter Brand `Lenovo {runId}` dan Brand `Canon {runId}` serta Filter Group `Warehouse {runId}` dan Search `{runId}`
44. Verifikasi tidak ada record yang terkembalikan karena irisan Brand (OR dalam field) dan Group `Warehouse {runId}` kosong
45. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Filter Status `Damaged` dan `Missing` serta Search `Lenovo {runId}`
46. Verifikasi `Laptop Lenovo ThinkPad - 2 {runId}` dan `Laptop Lenovo ThinkPad - 10 {runId}` terkembalikan karena opsi `Damaged` memfilter status record termasuk record bertanda `Missing`, sedangkan opsi `Missing` memfilter record bertanda itu
47. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Filter Status `Reported Missing` serta Search `Canon {runId}`
48. Verifikasi hanya `Printer Canon Pixma - 2 {runId}` yang terkembalikan karena penanda `Reported Missing` memfilter record bertanda itu

### Opsi filter DISTINCT dari data dalam cakupan Group
49. Total Control `Agus Pratama {runId}` meminta opsi Filter Source sub-tab Active
50. Verifikasi opsi memuat `Reported by holder`, `Manual`, `Stock opname`, `Borrowed asset`, dan `Transfer receive` yang ada pada data tabel seluruh client
51. Group Manager `Gunawan Hartono {runId}` meminta opsi Filter Source sub-tab Active
52. Verifikasi opsi memuat `Reported by holder`, `Manual`, `Stock opname`, dan `Borrowed asset` dari Group binaan tanpa `Transfer receive` yang hanya ada di Group `Warehouse {runId}`
53. Total Control `Agus Pratama {runId}` meminta opsi Filter Status sub-tab Active
54. Verifikasi opsi memuat `Waiting for Confirmation`, `Damaged`, `Reported Disposal`, `In Disposal Process`, serta penanda `Reported Missing` dan `Missing`, tanpa opsi nilai kosong
55. Total Control `Agus Pratama {runId}` meminta opsi Filter Status sub-tab History
56. Verifikasi opsi hanya memuat `Repaired`, `Disposed`, `Rejected`, dan `Canceled`, tanpa opsi nilai kosong
57. Group `Gudang Lama {runId}` diganti nama menjadi `Gudang Baru {runId}`
58. Total Control `Agus Pratama {runId}` meminta opsi Filter Group sub-tab History
59. Verifikasi opsi memuat nilai Group yang muncul pada data History menurut snapshot saat record selesai, yaitu `Gudang Lama {runId}`

### Nilai sort sama diurutkan menurut default sort lalu identifier, dengan arah mengikuti sort aktif
60. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Zulu {runId}` dan sort Source ascending
61. Verifikasi `Scanner Zulu - 1 {runId}` dan `Scanner Zulu - 2 {runId}` masing-masing terkembalikan satu kali meski Source dan Days Damaged keduanya sama
62. Total Control `Agus Pratama {runId}` meminta sekali lagi daftar record Active dengan Search `Zulu {runId}` dan sort Source ascending
63. Verifikasi urutan `Scanner Zulu - 1 {runId}` dan `Scanner Zulu - 2 {runId}` sama dengan permintaan sebelumnya karena urutan deterministik
64. Total Control `Agus Pratama {runId}` meminta daftar record Active dengan Search `Zulu {runId}` dan sort Source descending
65. Verifikasi urutan `Scanner Zulu - 1 {runId}` dan `Scanner Zulu - 2 {runId}` kebalikan dari urutan pada sort Source ascending karena arah identifier mengikuti arah sort aktif

