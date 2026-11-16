---
id: TC-FA-FACO-E2E-071-sort-used-by-dep-asset-class
title: "Sort kolom Used By lewat klik header mengurutkan angka secara natural dan kembali ke urutan default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r5"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  "§4.1.1#r5": [5, 7, 9]
anchor: [2, 3]
coverage:
  web: automated
---

# Sort kolom Used By lewat klik header mengurutkan angka secara natural dan kembali ke urutan default

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-071-1: Account Code `SUA-{runId}`, Account Name `Accumulated Depreciation Sort {runId}`, Account Function `Accumulated Depreciation`, Status Active, Last Used in Journal `—`, Used By `2`, dipakai 2 Asset Class (DU-071-5, DU-071-6).
  - DU-071-2: Account Code `SUB-{runId}`, Account Name `Equipment Cost Sort {runId}`, Account Function `Asset Cost`, Status Active, Last Used in Journal `—`, Used By `10`, dipakai 10 Asset Class (DU-071-5, DU-071-6, dan 8 Asset Class DU-071-7).
  - DU-071-3: Account Code `SUC-{runId}`, Account Name `Gain on Disposal Sort {runId}`, Account Function `Gain on Disposal`, Status Active, Last Used in Journal `—`, Used By `0`, tidak dipakai Asset Class.
  - DU-071-4: Account Code `SUD-{runId}`, Account Name `Depreciation Expense Sort {runId}`, Account Function `Depreciation Expense`, Status Active, Last Used in Journal `—`, Used By `1`, dipakai 1 Asset Class (DU-071-5).
  - DU-071-5: Asset Class `Sort Class 1 {runId}`, Status Active; Asset Cost `SUB-{runId}`, Accumulated Depreciation `SUA-{runId}`, Depreciation Expense `SUD-{runId}`.
  - DU-071-6: Asset Class `Sort Class 2 {runId}`, Status Active; Asset Cost `SUB-{runId}`, Accumulated Depreciation `SUA-{runId}`.
  - DU-071-7: 8 Asset Class `Sort Class {n} {runId}` untuk n 3 sampai 10, Status Active; Asset Cost `SUB-{runId}`.
  - Urutan default tabel adalah Account Code A-Z, sehingga baris DU-071-1 sampai DU-071-4 berurutan `SUA-{runId}`, `SUB-{runId}`, `SUC-{runId}`, `SUD-{runId}` dengan Used By `2`, `10`, `0`, `1`. Urutan itu berbeda dari urutan menaik Used By (`0`, `1`, `2`, `10`) dan dari urutan menurunnya (`10`, `2`, `1`, `0`).
  - Keempat nilai Used By berbeda satu sama lain, tanpa nilai kembar.

## Test Steps

### Urutan awal sebelum sort Used By
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi hasil Search memuat 4 baris data uji: `SUA-{runId}`, `SUB-{runId}`, `SUC-{runId}`, `SUD-{runId}`
3. Verifikasi urutan baris default menurut Account Code A-Z: `SUA-{runId}` (Used By `2`), `SUB-{runId}` (Used By `10`), `SUC-{runId}` (Used By `0`), `SUD-{runId}` (Used By `1`)

### Klik pertama mengurutkan Used By menaik secara natural
4. Klik header kolom Used By (klik pertama)
5. Verifikasi urutan baris menaik menurut Used By: `SUC-{runId}` (`0`), `SUD-{runId}` (`1`), `SUA-{runId}` (`2`), `SUB-{runId}` (`10`), sehingga `10` berada sesudah `2`, bukan sesudah `1`

### Klik kedua mengurutkan Used By menurun secara natural
6. Klik header kolom Used By (klik kedua)
7. Verifikasi urutan baris menurun menurut Used By: `SUB-{runId}` (`10`), `SUA-{runId}` (`2`), `SUD-{runId}` (`1`), `SUC-{runId}` (`0`), sehingga `10` berada sebelum `2`

### Klik ketiga mengembalikan urutan default
8. Klik header kolom Used By (klik ketiga)
9. Verifikasi urutan baris kembali ke urutan default menurut Account Code A-Z: `SUA-{runId}` (`2`), `SUB-{runId}` (`10`), `SUC-{runId}` (`0`), `SUD-{runId}` (`1`), bukan menaik maupun menurun menurut Used By
