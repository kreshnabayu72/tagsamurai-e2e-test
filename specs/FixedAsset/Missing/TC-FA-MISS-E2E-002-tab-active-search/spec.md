---
id: TC-FA-MISS-E2E-002-tab-active-search
title: "Tab Active: hasil Search per kolom searchable, pencocokan PIC, dan tanpa hasil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§5#r3, §4.1#p5, EB-SRC-2@tabel-active, EB-SRC-3@tabel-active, §9.11#b1, EB-SRC-1]
smoke: [EB-SRC-1]
dependsOn: []
trace:
  §5#r3: [3, 9, 12, 14, 16, 20, 27, 31, 33, 41, 49, 51, 56]
  §4.1#p5: [37, 39]
  EB-SRC-2@tabel-active: [14, 18, 20]
  EB-SRC-3@tabel-active: [22, 23, 25, 29, 35]
  §9.11#b1: 53
  EB-SRC-1: [5, 9, 10, 12]
anchor: [7]
coverage:
  web: automated
---

# Tab Active: hasil Search per kolom searchable, pencocokan PIC, dan tanpa hasil

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets, tab Missing, sub-tab Active.
- Data:
  - DU-002-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-002-2: Record berstatus `Missing` untuk aset `Plotter Delta {runId}` (Group `Finance Room {runId}`, TAG `RFID`, Brand `Zephyrion {runId}`, Purchase Cost `18250075`), Source `Manual`, tanpa Last Holder, pemindai terakhir reader `Lobby reader {runId}` pada T0 − 7 hari, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 6 hari pukul `09:00`. Asset ID dibentuk server dan menjadi milik entri ini.
  - DU-002-3: Record berstatus `Missing` untuk aset `Router Aksara {runId}` (Group `Delta {runId}`), Source `Transfer`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 5 hari pukul `10:00`.
  - DU-002-4: Record berstatus `Waiting for Confirmation` untuk aset `Hand Pallet Truck {runId}` (Group `Warehouse {runId}`), Source `Reported by holder`, Last Holder `Joko Susilo {runId}` (karyawan tanpa akun), Reported By PIC `Rudi Hartono {runId}` atas nama `Joko Susilo {runId}`, Reported Date T0 − 2 hari pukul `07:15`.
  - DU-002-5: Record berstatus `Missing` untuk aset `Cooler 50%_A {runId}` (Group `Warehouse {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 4 hari pukul `08:00`; namanya memuat karakter `%` dan `_`.
  - DU-002-6: Record berstatus `Missing` untuk aset `Cooler 500XA {runId}` (Group `Warehouse {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 4 hari pukul `08:30`; pengecoh yang akan cocok bila `%` dan `_` diperlakukan sebagai wildcard.
  - DU-002-7: Record berstatus `Missing` untuk aset `Printer Kantor {runId}` (Group `Warehouse {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 3 hari pukul `09:00`; namanya memakai satu spasi di tengah.
  - DU-002-8: Record berstatus `Missing` untuk aset `Server Room Utama {runId}` (Group `Warehouse {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 3 hari pukul `09:30`.
  - DU-002-9: kata kunci Search `lotter Delta {runId}`, potongan dari tengah nama DU-002-2.
  - DU-002-10: kata kunci Search `plotter delta {runId}`, nama DU-002-2 dengan huruf kapital berbeda.
  - DU-002-11: kata kunci Search `  Plotter Delta {runId}  `, nama DU-002-2 dengan dua spasi di awal dan dua spasi di akhir.
  - DU-002-12: kata kunci Search `   `, tiga spasi saja.
  - DU-002-13: kata kunci Search `Printer  Kantor {runId}`, nama DU-002-7 dengan dua spasi di tengah.
  - DU-002-14: kata kunci Search `Server Utama {runId}`, kata dari nama DU-002-8 yang tidak bersebelahan.
  - DU-002-15: kata kunci Search `{runId} tidakada` yang tidak cocok dengan kolom mana pun.
  - DU-002-16: kata kunci Search `50%_A {runId}`, potongan nama DU-002-5 yang memuat `%` dan `_`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; Reported Date pada entri di atas dihitung relatif terhadap T0.
  - Plan client membuka semua tipe TAG: `RFID`, `NFC`, `QR`, `BLE`, dan `GPS`.

## Test Steps

### Search baru berjalan sesudah Enter dan tanpa hasil
1. Buka kotak Search pada toolbar
2. Ketik `{runId} tidakada` pada kotak Search tanpa menekan Enter
3. Verifikasi tabel tidak menampilkan `No results found` selama Enter belum ditekan
4. Tekan Enter
5. Verifikasi `No results found` tampil karena kata kunci tidak cocok dengan kolom mana pun
6. Ganti isi kotak search dengan `{runId}`, tekan Enter
7. Verifikasi tabel memuat baris untuk `Plotter Delta {runId}`, `Router Aksara {runId}`, `Hand Pallet Truck {runId}`, `Cooler 50%_A {runId}`, `Cooler 500XA {runId}`, `Printer Kantor {runId}`, `Server Room Utama {runId}`

### Substring di tengah nama dan huruf kapital berbeda
8. Ganti isi kotak search dengan `lotter Delta {runId}`, tekan Enter
9. Verifikasi baris `Plotter Delta {runId}` tampil karena kata kunci berada di tengah kolom Name
10. Verifikasi baris `Router Aksara {runId}` tidak tampil
11. Ganti isi kotak search dengan `plotter delta {runId}`, tekan Enter
12. Verifikasi baris `Plotter Delta {runId}` tampil walau huruf kapital kata kunci berbeda

### Kolom badge dan kode ikut dicari
13. Ganti isi kotak search dengan `Finance Room {runId}`, tekan Enter
14. Verifikasi baris `Plotter Delta {runId}` tampil karena nilai badge kolom Group cocok
15. Ganti isi kotak search dengan Asset ID milik DU-002-2, tekan Enter
16. Verifikasi baris `Plotter Delta {runId}` tampil karena kolom Asset ID cocok

### Kata kunci yang cocok di dua kolom berbeda menampilkan kedua baris, dan tanggal tidak ikut dicari
17. Ganti isi kotak search dengan `Delta {runId}`, tekan Enter
18. Verifikasi baris `Plotter Delta {runId}` tampil karena kolom Name cocok, dan baris `Router Aksara {runId}` tampil karena badge Group `Delta {runId}` cocok
19. Ganti isi kotak search dengan tanggal Reported Date DU-002-2 dalam format `DD/MM/YY`, tekan Enter
20. Verifikasi `No results found` tampil karena kolom bertipe tanggal tidak ikut Search

### Karakter khusus dicari sebagai teks
21. Ganti isi kotak search dengan `50%_A {runId}`, tekan Enter
22. Verifikasi baris `Cooler 50%_A {runId}` tampil karena `%` dan `_` dicari sebagai teks
23. Verifikasi baris `Cooler 500XA {runId}` tidak tampil

### Spasi pada kata kunci
24. Ganti isi kotak search dengan `  Plotter Delta {runId}  `, tekan Enter
25. Verifikasi baris `Plotter Delta {runId}` tampil sama seperti kata kunci tanpa spasi di awal dan di akhir
26. Ganti isi kotak search dengan `Printer Kantor {runId}`, tekan Enter
27. Verifikasi baris `Printer Kantor {runId}` tampil
28. Ganti isi kotak search dengan `Printer  Kantor {runId}`, tekan Enter
29. Verifikasi baris `Printer Kantor {runId}` tampil karena setiap kata kunci muncul pada nilai barisnya[^drift-1]
30. Ganti isi kotak search dengan `Server Room Utama {runId}`, tekan Enter
31. Verifikasi baris `Server Room Utama {runId}` tampil
32. Ganti isi kotak search dengan `Server Utama {runId}`, tekan Enter
33. Verifikasi baris `Server Room Utama {runId}` tampil karena setiap kata kunci muncul pada nilai barisnya walau tidak bersebelahan[^drift-1]
34. Ganti isi kotak search dengan `   `, tekan Enter
35. Verifikasi `No results found` tidak tampil karena kata kunci yang hanya berisi spasi diperlakukan seperti kotak search kosong

### Laporan PIC atas nama dicari lewat nama PIC dan nama karyawan
36. Ganti isi kotak search dengan `Rudi Hartono {runId}`, tekan Enter
37. Verifikasi baris `Hand Pallet Truck {runId}` tampil karena nama PIC cocok
38. Ganti isi kotak search dengan `Joko Susilo {runId}`, tekan Enter
39. Verifikasi baris `Hand Pallet Truck {runId}` tampil karena nama karyawan yang diwakili cocok

### Kolom tersembunyi tidak ikut dicari
40. Ganti isi kotak search dengan `Zephyrion {runId}`, tekan Enter
41. Verifikasi `No results found` tampil karena kolom Brand tersembunyi
42. Klik header kolom Actions
43. Klik `Setup Column...`
44. Centang kolom `Brand`
45. Centang kolom `TAG`
46. Centang kolom `Purchase Cost`
47. Klik `[Save]`
48. Ganti isi kotak search dengan `Zephyrion {runId}`, tekan Enter
49. Verifikasi baris `Plotter Delta {runId}` tampil karena kolom Brand kini tampil

### Kolom ikon dan nilai finansial dicari bagi Total Control
50. Ganti isi kotak search dengan `RFID`, tekan Enter
51. Verifikasi baris `Plotter Delta {runId}` tampil karena label ikon `RFID` pada kolom TAG cocok
52. Ganti isi kotak search dengan `18250075`, tekan Enter
53. Verifikasi baris `Plotter Delta {runId}` tampil karena nilai kolom Purchase Cost `18250075` cocok bagi aktor yang berhak melihat nilai finansial
54. Klik `(←)` pada kotak Search

### Kolom Last Seen ikut dicari
55. Ganti isi kotak search dengan `Lobby reader {runId}`, tekan Enter
56. Verifikasi baris `Plotter Delta {runId}` tampil karena nama pemindai pada kolom Last Seen cocok
57. Klik `(←)` pada kotak Search

[^drift-1]: Drift foundation vs kontrak komponen. Foundation `prd-conventions.md` §9.16: «Spasi di tengah query menjadi bagian dari substring yang dicari ... query tidak dipecah menjadi beberapa kata». Kontrak `SearchButton#5`: baris cocok bila nilainya memuat seluruh query sebagai substring, atau bila setiap kata query (dipisah spasi) muncul di nilai baris, dengan urutan bebas dan boleh beda kolom. PRD §4.1 dan §5 tidak menyatakan tabel Missing server-driven, jadi `SearchButton#33` (bersyarat) tidak dipakai. Diasersi: kontrak, karena foundation tidak bisa terjadi bersama butir `Does` (SB-7).
