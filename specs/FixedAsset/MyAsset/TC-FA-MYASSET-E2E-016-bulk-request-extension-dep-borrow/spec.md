---
id: TC-FA-MYASSET-E2E-016-bulk-request-extension-dep-borrow
title: "Bulk Request Extension tab Borrowed: Select All, baris nonaktif, dan satu halaman Extension Request lintas BRW"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1b#p6", "§4.2.3#p1", "§4.4#r2", "§5#r5", "EB-BLK-2@tabel-borrowed"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#p6": [7, 19, 21, 36]
  "§4.2.3#p1": [18, 19, 36]
  "§4.4#r2": [22, 38, 39, 40, 41, 42, 45]
  "§5#r5": [5, 10, 31, 36]
  "EB-BLK-2@tabel-borrowed": [5, 7, 9, 12]
anchor: [44]
coverage:
  web: automated
---

# Bulk Request Extension tab Borrowed: Select All, baris nonaktif, dan satu halaman Extension Request lintas BRW

## Prerequisites
- Aktor: Borrower, pengguna ber-akun login yang hanya memiliki pinjaman pada Data di bawah, sehingga seluruh baris tab Borrowed miliknya adalah data spec ini.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-016-1: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 A {runId}`, Asset ID `HDS-A-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-2: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 B {runId}`, Asset ID `HDS-B-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-3: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 C {runId}`, Asset ID `HDS-C-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-4: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 D {runId}`, Asset ID `HDS-D-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-5: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 E {runId}`, Asset ID `HDS-E-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-6: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 F {runId}`, Asset ID `HDS-F-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-7: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 G {runId}`, Asset ID `HDS-G-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-8: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 H {runId}`, Asset ID `HDS-H-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-9: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 I {runId}`, Asset ID `HDS-I-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-10: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 J {runId}`, Asset ID `HDS-J-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-11: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed`, Source `Admin`, satu aset: Name `Headset Jabra Evolve2 K {runId}`, Asset ID `HDS-K-{runId}`, Brand `Jabra`, Model/Type `Evolve2 65`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-016-12: Pinjaman milik Borrower dari BRW sendiri berstatus `Waiting for Handover`, Source `Admin`, satu aset: Name `Webcam Logitech C920 {runId}`, Asset ID `WBC-C920-{runId}`, Brand `Logitech`, Model/Type `C920`, Group `Head Office`, Duration `5 days`.
  - DU-016-13: Pinjaman milik Borrower dari BRW sendiri berstatus `Borrowed` dengan pengajuan Extend yang menunggu review, sehingga Status tampil `Extension Request`, Source `Admin`, satu aset: Name `Webcam Logitech Brio {runId}`, Asset ID `WBC-BRIO-{runId}`, Brand `Logitech`, Model/Type `Brio`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
- Kondisi: Selection Limit bernilai `1000`, dan rows per page bernilai bawaan `10`.

## Test Steps

### Select All memilih lintas halaman dan tidak menghitung baris nonaktif
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Urutkan kolom `Name` dari A ke Z
4. Centang checkbox header tabel
5. Verifikasi tombol `Select All (11 records)` tampil
6. Klik `Select All (11 records)`
7. Verifikasi tombol `Unselect All ([N] records)` tampil dengan `[N]` bernilai `11`[^drift-1]
8. Pindah ke halaman `2` pada Pagination
9. Verifikasi jumlah terpilih pada bar seleksi bernilai `11`
10. Verifikasi checkbox baris `Webcam Logitech C920 {runId}` nonaktif dan tidak tercentang
11. Hapus centang baris `Headset Jabra Evolve2 K {runId}`
12. Verifikasi tombol `Select All (11 records)` tampil kembali dengan jumlah tetap `11`
13. Klik `×` pada bar seleksi

### Bulk Request Extension satu baris
14. Ganti isi kotak search dengan `Headset Jabra Evolve2 K {runId}`, tekan Enter
15. Centang baris `Headset Jabra Evolve2 K {runId}`
16. Klik `Bulk Action`
17. Klik `Request Extension`
18. Verifikasi breadcrumb `My Asset > Borrowed > Extension Request` tampil
19. Verifikasi tabel halaman Extension Request memuat aset `Headset Jabra Evolve2 K {runId}`
20. Klik `[Submit Request]`
21. Verifikasi baris `Headset Jabra Evolve2 K {runId}` berstatus `Extension Request`
22. Verifikasi kotak Search tetap berisi `Headset Jabra Evolve2 K {runId}`

### Bulk Request Extension banyak baris lintas BRW
23. Ganti isi kotak search dengan `{runId}`, tekan Enter
24. Urutkan kolom `Name` dari A ke Z
25. Klik ikon `Filter` pada toolbar
26. Klik field `Brand`
27. Centang opsi `Jabra`
28. Tekan `Esc` untuk menutup daftar opsi
29. Klik `[Apply]`
30. Centang checkbox header tabel
31. Verifikasi tombol `Select All (10 records)` tampil
32. Klik `Select All (10 records)`
33. Pindah ke halaman `2` pada Pagination
34. Klik `Bulk Action`
35. Klik `Request Extension`
36. Verifikasi tabel halaman Extension Request memuat `10` aset, masing-masing dari BRW yang berbeda
37. Klik `[Submit Request]`
38. Verifikasi kotak Search tetap berisi `{runId}`
39. Verifikasi kolom `Name` tetap terurut dari A ke Z
40. Verifikasi Filter Brand `Jabra` tetap ter-Apply
41. Verifikasi halaman aktif tetap `2`
42. Verifikasi rows per page tetap `10`
43. Pindah ke halaman `1` pada Pagination
44. Verifikasi baris `Headset Jabra Evolve2 A {runId}` berstatus `Extension Request`
45. Verifikasi bar seleksi tidak tampil

[^drift-1]: Drift PRD/foundation vs kontrak komponen. foundation `prd-conventions.md` §8: tombol berubah (toggle) menjadi `"Unselect All"`. Kontrak `BulkActionButton#11` dan `BulkActionButton#60`: begitu semua baris yang dapat dipilih terpilih, tombol berbunyi `Unselect All (N records)`, tepat ketika jumlah terpilih sama dengan N. Diasersi: kontrak komponen (SB-7), sehingga label memuat jumlah.
