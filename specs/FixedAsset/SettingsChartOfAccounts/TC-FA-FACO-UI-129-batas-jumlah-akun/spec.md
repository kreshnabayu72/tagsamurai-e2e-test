---
id: TC-FA-FACO-UI-129-batas-jumlah-akun
title: "Tab Chart of Accounts: dialog blok saat batas jumlah akun tercapai"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-13", "§[F-FACO-01] Create Account#r5", "§9.4.2#r38", "EB-CON-4"]
smoke: []
dependsOn: []
trace:
  "D-13": [7, 8, 9, 12, 13, 16, 17]
  "§[F-FACO-01] Create Account#r5": [7, 8, 10, 18]
  "§9.4.2#r38": [7, 10, 16, 18]
  "EB-CON-4": [3, 4, 7, 8, 16, 17]
anchor: []
coverage:
  web: automated
---

# Tab Chart of Accounts: dialog blok saat batas jumlah akun tercapai

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Tab Chart of Accounts
- Data:
  - DU-129-1: 499 akun Active, Account Code `H-{n}`, Name `Akun Batas {n}`, Function `Asset Cost`, Used By `0`.
  - DU-129-2: 500 akun Active, Account Code `J-{n}`, Name `Akun Pas Batas {n}`, Function `Asset Cost`, Used By `0`.
  - DU-129-3: 501 akun Active, Account Code `K-{n}`, Name `Akun Lebih Batas {n}`, Function `Asset Cost`, Used By `0`.
- Kondisi:
  - K1: Master Data Count Limit akun bernilai `500` dan dibawa oleh respons daftar; tabel berisi DU-129-1.
  - K2: Master Data Count Limit akun bernilai `500` dan dibawa oleh respons daftar; tabel berisi DU-129-2.
  - K3: Master Data Count Limit akun bernilai `500` dan dibawa oleh respons daftar; tabel berisi DU-129-3 karena limit diturunkan sesudah akun dibuat.

## Test Steps

### Klik + Account satu di bawah batas
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Klik `+ Account`
3. Verifikasi modal `Add Account` tampil
4. Verifikasi dialog `Cannot Add Account` tidak tampil

### Klik + Account tepat di batas
5. Tampilkan Tab Chart of Accounts dengan kondisi K2
6. Klik `+ Account`
7. Verifikasi judul dialog `Cannot Add Account` tampil
8. Verifikasi teks `You've reached the platform limit of 500 records. Contact support if you need a higher limit.` tampil
9. Verifikasi tombol `[OK]` tampil
10. Verifikasi modal `Add Account` tidak tampil
11. Klik `[OK]`
12. Verifikasi dialog `Cannot Add Account` tidak tampil
13. Verifikasi baris `J-1` tampil

### Klik + Account melebihi batas
14. Tampilkan Tab Chart of Accounts dengan kondisi K3
15. Klik `+ Account`
16. Verifikasi judul dialog `Cannot Add Account` tampil
17. Verifikasi teks `You've reached the platform limit of 500 records. Contact support if you need a higher limit.` tampil
18. Verifikasi modal `Add Account` tidak tampil
