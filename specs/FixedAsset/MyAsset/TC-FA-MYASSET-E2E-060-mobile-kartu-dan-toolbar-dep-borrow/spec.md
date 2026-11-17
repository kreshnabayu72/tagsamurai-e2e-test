---
id: TC-FA-MYASSET-E2E-060-mobile-kartu-dan-toolbar-dep-borrow
title: "Mobile: isi kartu tiap tab, menu aksi kartu, dan Filter serta Download di menu toolbar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.6#p1", "§10#r6"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.6#p1": [3, 4, 5, 6, 8, 10, 12, 13, 17, 18, 19, 20, 22, 24, 26, 27, 31, 32, 33, 34, 36, 38, 40, 41]
  "§10#r6": 2
anchor: []
coverage:
  android: automated
---
# Mobile: isi kartu tiap tab, menu aksi kartu, dan Filter serta Download di menu toolbar

## Prerequisites
- Aktor: Borrower, karyawan aktif ber-akun login.
- Layar awal: menu profil di aplikasi Android.
- Data:
  - DU-060-1: pinjaman Admin milik aktor dengan aset `Laptop Dell Latitude 5420 {runId}`, Total Asset `2`, Task `Confirm Handover`; sesi Handover sedang menunggu konfirmasi aktor. Nomor transaksi dan Expires At dibentuk server dan dimiliki entri ini.
  - DU-060-2: pinjaman Admin milik aktor berstatus `Borrowed` dengan aset `Projector Epson EB-X06 {runId}`, Duration `3 days`. Due Date dan Remaining dibentuk server dan dimiliki entri ini.
  - DU-060-3: pinjaman Admin milik aktor berstatus `Returned` dengan aset `Meeting Mic Set {runId}`, Holder `Me`. Closed At dibentuk server dan dimiliki entri ini.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.

## Test Steps

### My Asset tersedia di aplikasi Android native
1. Klik `My Asset` pada menu profil
2. Verifikasi halaman `My Asset` terbuka di aplikasi Android native

### Kartu tab Task memuat nomor transaksi, badge, Total Asset, dan Expires At
3. Verifikasi kartu Task milik DU-060-1 tampil dengan nomor transaksinya
4. Verifikasi badge `Confirm Handover` tampil pada kartu Task milik DU-060-1
5. Verifikasi Total Asset `2` tampil pada kartu Task milik DU-060-1
6. Verifikasi Expires At tampil pada kartu Task milik DU-060-1 dengan Date Format `dd/MM/yy` dan Time Format `24 jam`
7. Klik menu ⋯ pada kartu Task milik DU-060-1
8. Verifikasi aksi `Confirm Handover` tersedia di menu ⋯ kartu Task milik DU-060-1
9. Tutup menu ⋯ pada kartu Task milik DU-060-1

### Filter dan Download di menu toolbar tab Task
10. Verifikasi ikon `Search` tampil pada toolbar tab Task
11. Klik menu ⋯ pada toolbar tab Task
12. Verifikasi `Filter` tersedia di menu ⋯ toolbar tab Task
13. Verifikasi `Download` tersedia di menu ⋯ toolbar tab Task
14. Tutup menu ⋯ pada toolbar tab Task

### Kartu tab Borrowed memuat nama, badge, Due Date, dan Remaining
15. Klik tab `Borrowed`
16. Ketik Search `Projector Epson EB-X06 {runId}`, tekan Enter
17. Verifikasi nama aset milik DU-060-2 tampil sebagai identitas utama kartu Borrowed
18. Verifikasi badge `Borrowed` tampil pada kartu Borrowed milik DU-060-2
19. Verifikasi Due Date tampil pada kartu Borrowed milik DU-060-2 dengan Date Format `dd/MM/yy`
20. Verifikasi Remaining tampil pada kartu Borrowed milik DU-060-2 dan bukan `—`
21. Klik menu ⋯ pada kartu Borrowed milik DU-060-2
22. Verifikasi aksi `Borrow Log` tersedia di menu ⋯ kartu Borrowed milik DU-060-2
23. Tutup menu ⋯ pada kartu Borrowed milik DU-060-2

### Filter dan Download di menu toolbar tab Borrowed
24. Verifikasi ikon `Search` tampil pada toolbar tab Borrowed
25. Klik menu ⋯ pada toolbar tab Borrowed
26. Verifikasi `Filter` tersedia di menu ⋯ toolbar tab Borrowed
27. Verifikasi `Download` tersedia di menu ⋯ toolbar tab Borrowed
28. Tutup menu ⋯ pada toolbar tab Borrowed

### Kartu tab History memuat nama, badge, Holder, dan Closed At
29. Klik tab `History`
30. Ketik Search `Meeting Mic Set {runId}`, tekan Enter
31. Verifikasi nama aset milik DU-060-3 tampil sebagai identitas utama kartu History
32. Verifikasi badge `Returned` tampil pada kartu History milik DU-060-3
33. Verifikasi Holder `Me` tampil pada kartu History milik DU-060-3
34. Verifikasi Closed At tampil pada kartu History milik DU-060-3 dengan Date Format `dd/MM/yy` dan Time Format `24 jam`
35. Klik menu ⋯ pada kartu History milik DU-060-3
36. Verifikasi aksi `Borrow Log` tersedia di menu ⋯ kartu History milik DU-060-3
37. Tutup menu ⋯ pada kartu History milik DU-060-3

### Filter dan Download di menu toolbar tab History
38. Verifikasi ikon `Search` tampil pada toolbar tab History
39. Klik menu ⋯ pada toolbar tab History
40. Verifikasi `Filter` tersedia di menu ⋯ toolbar tab History
41. Verifikasi `Download` tersedia di menu ⋯ toolbar tab History
42. Tutup menu ⋯ pada toolbar tab History
