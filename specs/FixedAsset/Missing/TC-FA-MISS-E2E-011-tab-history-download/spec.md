---
id: TC-FA-MISS-E2E-011-tab-history-download
title: "Tab History: nama berkas Missing-History dan cakupan baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§5#r6, §4.1b#p1]
smoke: []
dependsOn: []
trace:
  §5#r6: [6, 8, 13]
  §4.1b#p1: [4, 9, 10, 19]
anchor: []
coverage:
  web: automated
---

# Tab History: nama berkas Missing-History dan cakupan baris

## Prerequisites
- Aktor: Total Control `Rina Wijaya {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-011-1: User `Rina Wijaya {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-011-2: User `Sari Dewi {runId}`, pemegang (Borrower) aset tanpa hak Aktor Missing, kemudian dinonaktifkan; tampil sebagai `Sari D`.
  - DU-011-3: Record `Found` untuk aset `Rak Arsip {runId}` (Group `Gudang Berkas {runId}`), Source `Borrow`, Last Holder `Sari Dewi {runId}`, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 30 hari pukul `09:00`, Resolved By `Rina Wijaya {runId}`, Resolved Date T0 − 24 hari pukul `14:10`.
  - DU-011-4: Record `Disposed` untuk aset `Troli Dokumen {runId}` (Group `Gudang Berkas {runId}`), Source `Manual`, tanpa Last Holder, Reported By `Rina Wijaya {runId}`, Reported Date T0 − 70 hari pukul `08:00`, Resolved By `System`, Resolved Date T0 − 8 hari pukul `00:00`.
  - DU-011-5: Record `Canceled` untuk aset `Lemari Berkas {runId}` (Group `Gudang Berkas {runId}`), Source `Reported by holder`, Last Holder `Sari Dewi {runId}`, Reported By `Sari Dewi {runId}`, Reported Date T0 − 12 hari pukul `13:00`, Resolved By `Sari Dewi {runId}`, Resolved Date T0 − 11 hari pukul `08:20`.
- Kondisi:
  - Date Format bernilai `DD/MM/YY` dan Time Format bernilai `HH:mm`.
  - T0 adalah waktu spec dijalankan; tanggal pada entri di atas dihitung relatif terhadap T0.

## Test Steps

### Berkas CSV bernama Missing-History
1. Klik tab `Missing` pada halaman Assets
2. Klik sub-tab `History`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi tabel memuat baris untuk `Rak Arsip {runId}`, `Troli Dokumen {runId}`, `Lemari Berkas {runId}` sebagai record berstatus `Found`, `Disposed`, dan `Canceled`
5. Klik `Download` pada toolbar
6. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
7. Klik `Download as CSV`
8. Verifikasi berkas `Missing-History.csv` terunduh, dengan nama berbeda dari `Missing-Active`
9. Verifikasi berkas memuat baris untuk `Rak Arsip {runId}`, `Troli Dokumen {runId}`, `Lemari Berkas {runId}` saja sebagai record berstatus `Found`, `Disposed`, dan `Canceled`
10. Verifikasi kolom Last Holder pada baris `Rak Arsip {runId}` berisi nama lengkap `Sari Dewi {runId}` walau penggunanya sudah dinonaktifkan, dan pada baris `Troli Dokumen {runId}` berisi `-`

### Berkas XLSX bernama Missing-History
11. Klik `Download` pada toolbar
12. Klik `Download as XLSX`
13. Verifikasi berkas `Missing-History.xlsx` terunduh

### Berkas mengikuti Filter yang aktif
14. Klik ikon Filter
15. Pada field `Status` pilih opsi `Found`
16. Klik `[Apply]`
17. Klik `Download` pada toolbar
18. Klik `Download as CSV`
19. Verifikasi berkas memuat baris `Rak Arsip {runId}` dan tidak memuat baris `Troli Dokumen {runId}` maupun `Lemari Berkas {runId}`
20. Klik `[Clear Field]`
21. Klik `[Apply]`
