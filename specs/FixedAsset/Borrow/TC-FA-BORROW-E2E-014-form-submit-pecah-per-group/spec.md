---
id: TC-FA-BORROW-E2E-014-form-submit-pecah-per-group
title: "Form Borrow Request mengelompokkan aset per Group, dan Submit membuat satu BRW per Group dengan aset Days dan Hours dalam satu BRW"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FI-BRW-33", "V-BRW-18", "§4.4#r3"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-33": [16, 26, 27, 28, 31]
  "V-BRW-18": [23, 30]
  "§4.4#r3": 15
anchor: []
coverage:
  web: automated
---

# Form Borrow Request mengelompokkan aset per Group, dan Submit membuat satu BRW per Group dengan aset Days dan Hours dalam satu BRW

## Prerequisites
- Aktor: Asset Admin `Asset Admin Dua Group {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-014-1: Borrower `Bayu Peminjam {runId}`, Email `bayu.peminjam{runId}@example.com`, Position `Staff {runId}`, Division `Operations {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-014-2: Aktor `Asset Admin Dua Group {runId}`, role Asset Admin, Group penugasan `Head Office` dan `Branch Surabaya`.
  - DU-014-3: Approver `Dian Approver {runId}`, role Approver, Group penugasan `Head Office` dan `Branch Surabaya` (approver eligible bagi semua aset di bawah).
  - DU-014-4: aset `Laptop Asus Vivobook {runId}`, Brand `Asus {runId}`, Model/Type `Vivobook 14 {runId}`, Group `Head Office`, Category `Laptop {runId}`, Custody `Available`, satuan Days, Max Duration `7 days`, Approval `Needs approval`.
  - DU-014-5: aset `Mic Wireless Shure {runId}`, Brand `Shure {runId}`, Model/Type `MXW8 {runId}`, Group `Head Office`, Category `Audio {runId}`, Custody `Available`, satuan Hours, Max Duration `6 hours`, Approval `Needs approval`.
  - DU-014-6: aset `Toyota Innova {runId}`, Brand `Toyota {runId}`, Model/Type `Innova {runId}`, Group `Branch Surabaya`, Category `Car {runId}`, Custody `Available`, satuan Days, Max Duration `14 days`, Approval `Needs approval`.
  - DU-014-7: isian form Borrow Request: Duration `3` dan Purpose `Training` untuk `Laptop Asus Vivobook {runId}`; Duration `4` dan Purpose `Training` untuk `Mic Wireless Shure {runId}`; Duration `5` dan Purpose `Training` untuk `Toyota Innova {runId}`.

## Test Steps

### Form mengelompokkan aset per Group dan menampilkan pembagian BRW
1. Klik `[+ Borrow]`
2. Klik `[Select Borrower]`
3. Ketik Search `Bayu Peminjam {runId}`, tekan Enter
4. Pilih baris `Bayu Peminjam {runId}`
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Laptop Asus Vivobook {runId}`
9. Centang baris `Mic Wireless Shure {runId}`
10. Klik `[Select]`
11. Klik `[+ Asset]`
12. Ketik Search `{runId}`, tekan Enter
13. Centang baris `Toyota Innova {runId}`
14. Klik `[Select]`
15. Verifikasi alert pemecahan `This will create 2 borrows (Head Office, Branch Surabaya).` tampil sesudah aset dari Group berbeda ditambahkan
16. Verifikasi baris `Laptop Asus Vivobook {runId}` dan `Mic Wireless Shure {runId}` tampil dalam satu kelompok Group `Head Office` dan baris `Toyota Innova {runId}` tampil dalam kelompok Group `Branch Surabaya`
17. Isi Duration baris `Laptop Asus Vivobook {runId}` dengan `3`
18. Isi Purpose baris `Laptop Asus Vivobook {runId}` dengan `Training`
19. Isi Duration baris `Mic Wireless Shure {runId}` dengan `4`
20. Isi Purpose baris `Mic Wireless Shure {runId}` dengan `Training`
21. Isi Duration baris `Toyota Innova {runId}` dengan `5`
22. Isi Purpose baris `Toyota Innova {runId}` dengan `Training`
23. Verifikasi satuan Duration baris `Laptop Asus Vivobook {runId}` adalah `days` dan baris `Mic Wireless Shure {runId}` adalah `hours` dalam form yang sama

### Submit membuat satu BRW per Group
24. Klik `[Submit]`
25. Klik `[Submit]` pada dialog `Submit Borrow`
26. Verifikasi halaman pindah ke tab Transactions karena hasil Submit lebih dari satu BRW
27. Verifikasi toast `Success, 2 borrows have been submitted for approval.` tampil sebagai toast tunggal untuk seluruh hasil Submit
28. Verifikasi tabel Transactions memuat dua baris BRW untuk Borrower `Bayu Peminjam {runId}`, satu BRW untuk Group `Head Office` dan satu BRW untuk Group `Branch Surabaya`
29. Buka Borrow Detail BRW yang Group-nya `Head Office`
30. Verifikasi tabel Assets memuat baris `Laptop Asus Vivobook {runId}` dengan Duration `3 days` dan baris `Mic Wireless Shure {runId}` dengan Duration `4 hours` dalam BRW yang sama
31. Verifikasi tabel Assets BRW `Head Office` tidak memuat baris `Toyota Innova {runId}`
