---
id: TC-FA-MISS-E2E-008-tab-history-search
title: "Tab History: hasil Search per kolom searchable"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§5#r3, §4.1b#r2, §4.1b#r15]
smoke: []
dependsOn: []
trace:
  §5#r3: [5, 7, 11, 14, 16, 21, 24]
  §4.1b#r2: [11, 12]
  §4.1b#r15: [18, 19]
anchor: [9]
coverage:
  web: automated
---

# Tab History: hasil Search per kolom searchable

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-008-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-008-2: User `Dian Pertiwi {runId}`, role Manage asset & TAG (Update) yang menyelesaikan record DU-008-5.
  - DU-008-3: Record `Found` untuk aset `Papan Tulis Digital {runId}` (Group `Gudang Cari {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 20 hari pukul `09:00`, Resolved By `Rina Wijaya {runId}`, Resolved Date T0 − 14 hari pukul `14:10`.
  - DU-008-4: Record `Disposed` untuk aset `Layar Proyektor {runId}` (Group `Gudang Lain {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 50 hari pukul `09:00`, Resolved By `System`, Resolved Date T0 − 5 hari pukul `00:00`.
  - DU-008-5: Record `Rejected` untuk aset `Meja Rapat Besar {runId}` (Group `Gudang Lain {runId}`), Source `Reported by holder`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 9 hari pukul `10:00`, Resolved By `Dian Pertiwi {runId}`, Resolved Date T0 − 8 hari pukul `09:15`.
  - DU-008-6: kata kunci Search `apan Tulis {runId}`, potongan dari tengah nama DU-008-3.
  - DU-008-7: kata kunci Search `papan tulis digital {runId}`, nama DU-008-3 dengan huruf kapital berbeda.
  - DU-008-8: kata kunci Search `{runId} tidakada` yang tidak cocok dengan kolom mana pun.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.

## Test Steps

### Search baru berjalan sesudah Enter dan tanpa hasil
1. Klik tab `Missing` pada halaman Assets
2. Klik sub-tab `History`
3. Buka kotak Search pada toolbar
4. Ketik `{runId} tidakada` pada kotak Search tanpa menekan Enter
5. Verifikasi tabel tidak menampilkan `No results found` selama Enter belum ditekan
6. Tekan Enter
7. Verifikasi `No results found` tampil karena kata kunci tidak cocok dengan kolom mana pun
8. Ganti isi kotak search dengan `{runId}`, tekan Enter
9. Verifikasi tabel memuat baris untuk `Papan Tulis Digital {runId}`, `Layar Proyektor {runId}`, `Meja Rapat Besar {runId}`

### Substring di tengah nama dan huruf kapital berbeda
10. Ganti isi kotak search dengan `apan Tulis {runId}`, tekan Enter
11. Verifikasi baris `Papan Tulis Digital {runId}` tampil karena kata kunci berada di tengah kolom Name
12. Verifikasi baris `Layar Proyektor {runId}` dan `Meja Rapat Besar {runId}` tidak tampil
13. Ganti isi kotak search dengan `papan tulis digital {runId}`, tekan Enter
14. Verifikasi baris `Papan Tulis Digital {runId}` tampil walau huruf kapital kata kunci berbeda

### Kolom badge dan kolom Resolved By ikut dicari
15. Ganti isi kotak search dengan `Gudang Cari {runId}`, tekan Enter
16. Verifikasi baris `Papan Tulis Digital {runId}` tampil karena nilai badge kolom Group cocok, dan baris `Layar Proyektor {runId}` tidak tampil
17. Ganti isi kotak search dengan `Dian Pertiwi {runId}`, tekan Enter
18. Verifikasi baris `Meja Rapat Besar {runId}` tampil karena kolom Resolved By cocok
19. Verifikasi baris `Papan Tulis Digital {runId}` dan `Layar Proyektor {runId}` tidak tampil

### Tanggal tidak ikut dicari
20. Ganti isi kotak search dengan tanggal Resolved Date DU-008-3 dalam format `DD/MM/YY`, tekan Enter
21. Verifikasi `No results found` tampil karena kolom bertipe tanggal tidak ikut Search
22. Klik `(←)` pada kotak Search

### Placeholder kotak Search tab History
23. Buka kotak Search pada toolbar
24. Verifikasi placeholder kotak Search `Search asset name, asset ID...`
