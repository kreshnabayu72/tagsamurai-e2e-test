---
id: TC-FA-FACO-E2E-001-tabel-account-list-tampilan
title: "Tabel Account List menampilkan nilai akun dari data tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r7", "§4.1.1#r8", "§5#b13", "EB-FRM-6@form-add-account"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [5, 6]
  "§4.1.1#r2": 2
  "§4.1.1#r3": [3, 7]
  "§4.1.1#r4": [4, 8]
  "§4.1.1#r7": [13, 18]
  "§4.1.1#r8": 14
  "§5#b13": [18, 23, 24, 29]
  "EB-FRM-6@form-add-account": 26
coverage:
  web: automated
---

# Tabel Account List menampilkan nilai akun dari data tersimpan

## Prerequisites
- Aktor: pengguna Total Control (nama lengkap terdiri dari nama depan dan nama belakang). Aktor lain pemicu: Admin B (DU-001-5).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-001-1: akun `A1-{runId}`, Account Name `Fixed Assets – Equipment {runId}`, Account Function `Asset Cost`, Status `Active`, tanpa entri Changelog sama sekali.
  - DU-001-2: akun `A2-{runId}`, Account Name `Fixed Assets – Equipment {runId}` (sama dengan DU-001-1), Account Function `Accumulated Depreciation`, Status `Inactive`.
  - DU-001-3: akun `A3-{runId}`, Account Name `Depreciation Expense – Admin {runId}`, Account Function `Depreciation Expense`, Status `Active`. Account Name sesudah Edit: `Depreciation Expense – Admin Pusat {runId}`.
  - DU-001-4: akun `A4-{runId}`, Account Name `<b>Finance</b> {runId}` (tersimpan sebagai teks ber-markup), Account Function `Gain on Disposal`, Status `Active`.
  - DU-001-5: Admin B, nama `Admin B {runId}`, role Total Control, cakupan seluruh client, nama tampilnya berbeda dari nama tampil aktor, akun aktif dan kredensialnya disediakan fase 2.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.
  - DU-001-3 dibuat lebih dari satu menit sebelum langkah 17 dijalankan, sehingga waktu dibuatnya berbeda menit dari waktu entri Changelog hasil Edit.

## Test Steps

### Nilai kolom default sesuai data tersimpan
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi Account Code `A1-{runId}` tampil sebagai nilai satu baris di tabel
3. Verifikasi Account Name baris `A1-{runId}` bernilai `Fixed Assets – Equipment {runId}`
4. Verifikasi Function baris `A1-{runId}` bernilai `Asset Cost`
5. Verifikasi switch Status baris `A1-{runId}` dalam keadaan `Active`
6. Verifikasi switch Status baris `A2-{runId}` dalam keadaan `Inactive`
7. Verifikasi Account Name baris `A2-{runId}` bernilai `Fixed Assets – Equipment {runId}`, sama dengan Account Name baris `A1-{runId}`
8. Verifikasi Function baris `A2-{runId}` bernilai `Accumulated Depreciation`

### Modified By dan Last Updated untuk akun tanpa entri Changelog
9. Klik header kolom Actions `⋯`
10. Centang `Modified By` pada panel Column Visibility
11. Centang `Last Updated` pada panel Column Visibility
12. Klik header kolom Actions `⋯` untuk menutup panel
13. Verifikasi Modified By baris `A1-{runId}` bernilai `System`
14. Verifikasi Last Updated baris `A1-{runId}` terisi waktu dengan Date Format `dd/MM/yy` diikuti Time Format `24h`

### Modified By dan Last Updated mengikuti entri Changelog terbaru
15. Klik `⋯` pada baris `A3-{runId}` > `Edit`
16. Ganti isi Account Name dengan `Depreciation Expense – Admin Pusat {runId}`
17. Klik `[Save]`
18. Verifikasi Modified By baris `A3-{runId}` menampilkan nama depan aktor diikuti inisial nama belakangnya, format `[First Name] [Last Initial]`
19. Catat nilai Last Updated baris `A3-{runId}`
20. Waktu berlalu sampai menit berganti sejak langkah 17
21. Admin B menyimpan akun `A3-{runId}` lewat Edit tanpa mengubah nilai apa pun
22. Ganti isi kotak Search dengan `A3-{runId}`, tekan Enter
23. Verifikasi Modified By baris `A3-{runId}` tetap sama dengan nilai pada langkah 18, bukan nama Admin B
24. Verifikasi Last Updated baris `A3-{runId}` tetap sama dengan nilai yang dicatat pada langkah 19

### Markup tersimpan tampil sebagai teks
25. Ganti isi kotak Search dengan `A4-{runId}`, tekan Enter
26. Verifikasi sel Account Name baris `A4-{runId}` menampilkan teks `<b>Finance</b> {runId}` apa adanya sebagai teks, bukan sebagai huruf tebal

### Last Updated sama dengan waktu entri Changelog terbaru
27. Klik ikon Changelog
28. Ketik Search `A3-{runId}` pada modal Changelog, tekan Enter
29. Verifikasi Date entri Changelog baris Field `Account Name` untuk Account Code `A3-{runId}` sama dengan nilai Last Updated yang dicatat pada langkah 19
30. Tutup modal Changelog
