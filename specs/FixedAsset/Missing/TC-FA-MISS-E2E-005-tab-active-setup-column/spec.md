---
id: TC-FA-MISS-E2E-005-tab-active-setup-column
title: "Tab Active: konfigurasi kolom bertahan sesudah muat ulang, kolom tersembunyi tidak ikut Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-KOL-2@tabel-active, EB-SRC-5@tabel-active, §4.1#p3]
smoke: []
dependsOn: []
trace:
  EB-KOL-2@tabel-active: [8, 10]
  EB-SRC-5@tabel-active: [2, 12, 14, 21, 23]
  §4.1#p3: [2, 8, 10]
anchor: []
coverage:
  web: automated
---

# Tab Active: konfigurasi kolom bertahan sesudah muat ulang, kolom tersembunyi tidak ikut Search

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets, tab Missing, sub-tab Active.
- Data:
  - DU-005-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-005-2: Record `Missing` untuk aset `Mesin Cuci {runId}` (Group `Gudang Konfig {runId}`, Brand `Zenith {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 4 hari pukul `09:00`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; Reported Date pada entri di atas dihitung relatif terhadap T0.
  - Konfigurasi kolom milik aktor masih bawaan: kolom `Group` tampil dan kolom `Brand` tersembunyi.

## Test Steps

### Kolom Curated tersembunyi awal tidak ikut Search
1. Ketik Search `Zenith {runId}`, tekan Enter
2. Verifikasi `No results found` tampil karena kolom `Brand` tersembunyi dan tidak ikut Search

### Konfigurasi kolom disimpan dan bertahan sesudah muat ulang
3. Klik header kolom Actions
4. Klik `Setup Column...`
5. Centang kolom `Brand`
6. Hapus centang kolom `Group`
7. Klik `[Save]`
8. Verifikasi kolom `Brand` tampil dan kolom `Group` tidak tampil di tabel
9. Muat ulang halaman
10. Verifikasi kolom `Brand` masih tampil dan kolom `Group` masih tidak tampil sesudah halaman dimuat ulang

### Kolom yang ditampilkan kembali ikut Search dan kolom yang disembunyikan tidak
11. Ketik Search `Zenith {runId}`, tekan Enter
12. Verifikasi baris `Mesin Cuci {runId}` tampil karena kolom `Brand` kini tampil
13. Ganti isi kotak search dengan `Gudang Konfig {runId}`, tekan Enter
14. Verifikasi `No results found` tampil karena kolom `Group` tersembunyi dan tidak ikut Search
15. Klik header kolom Actions
16. Klik `Setup Column...`
17. Centang kolom `Group`
18. Hapus centang kolom `Brand`
19. Klik `[Save]`
20. Ketik Search `Gudang Konfig {runId}`, tekan Enter
21. Verifikasi baris `Mesin Cuci {runId}` tampil lagi karena kolom `Group` kembali tampil
22. Ganti isi kotak search dengan `Zenith {runId}`, tekan Enter
23. Verifikasi `No results found` tampil karena kolom `Brand` kembali tersembunyi
24. Klik `(←)` pada kotak Search
