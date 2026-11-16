---
id: TC-FA-FACO-E2E-009-download-isi-berkas
title: "Isi berkas Download Account List mengikuti format sel PRD"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#b8", "§9.5#r12", "EB-DL-4"]
smoke: ["EB-DL-4"]
dependsOn: []
trace:
  "§5#b8": [7, 8, 10, 11, 17]
  "§9.5#r12": [10, 11, 18]
  "EB-DL-4": [6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 25]
anchor: [2, 22]
coverage:
  web: automated
---

# Isi berkas Download Account List mengikuti format sel PRD

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-009-1: akun `IB1-{runId}`, Account Name `Satu Isi {runId}`, Account Function `Asset Cost`, Status `Active`, belum pernah diekspor (Last Used in Journal kosong).
  - DU-009-2: akun `IB2-{runId}`, Account Name `Dua Isi {runId}`, Account Function `Depreciation Expense`, Status `Inactive`, belum pernah diekspor (Last Used in Journal kosong).
  - Search `Isi {runId}` hanya mencocokkan kedua akun ini.
- Kondisi:
  - Kolom `Active`, `Account Code`, `Account Name`, `Function`, `Used By`, dan `Last Used in Journal` tampil di tabel (kondisi bawaan).

## Test Steps
### Isi berkas CSV mengikuti format sel PRD
1. Ketik Search `Isi {runId}`, tekan Enter
2. Verifikasi baris `IB1-{runId}` dan `IB2-{runId}` tampil di tabel
3. Klik header kolom Account Name (klik pertama)
4. Klik ikon Download
5. Klik `Download as CSV`
6. Verifikasi berkas CSV memuat tepat dua baris data, urut `IB2-{runId}` lalu `IB1-{runId}`, mengikuti Sort aktif menaik menurut Account Name
7. Verifikasi sel Active baris `IB1-{runId}` bernilai `Active`
8. Verifikasi sel Active baris `IB2-{runId}` bernilai `Inactive`
9. Verifikasi sel Function baris `IB1-{runId}` bernilai `Asset Cost`, hanya teks label badge
10. Verifikasi sel Last Used in Journal baris `IB1-{runId}` bernilai `-`
11. Verifikasi sel Last Used in Journal baris `IB2-{runId}` bernilai `-`, bukan sel kosong, bukan `—`, dan bukan `null`
12. Verifikasi berkas CSV diawali BOM UTF-8

### Isi berkas XLSX mengikuti format sel PRD
13. Klik ikon Download
14. Klik `Download as XLSX`
15. Verifikasi berkas XLSX hanya memuat satu sheet bernama `Sheet1`
16. Verifikasi baris data berkas XLSX urut `IB2-{runId}` lalu `IB1-{runId}`
17. Verifikasi sel Active baris `IB2-{runId}` bernilai `Inactive` dan baris `IB1-{runId}` bernilai `Active`
18. Verifikasi sel Last Used in Journal baris `IB2-{runId}` bernilai `-`
19. Klik header kolom Account Name (klik kedua)
20. Klik header kolom Account Name (klik ketiga)

### Nol baris menghasilkan berkas yang hanya berisi header
21. Ketik Search `tidakada-{runId}`, tekan Enter
22. Verifikasi `No results found` tampil karena kata kunci Search tidak cocok dengan akun mana pun
23. Klik ikon Download
24. Klik `Download as CSV`
25. Verifikasi berkas CSV hanya berisi baris header, tanpa satu pun baris data
