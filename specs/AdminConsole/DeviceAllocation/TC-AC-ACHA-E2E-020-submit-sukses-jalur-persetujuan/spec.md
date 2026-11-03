---
id: TC-AC-ACHA-E2E-020-submit-sukses-jalur-persetujuan
title: "Submit Allocate Device Sukses Jalur Persetujuan: Waiting for Approval dan Reserve per Role dan Entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-70
  - TC-AC-ACHA-141
  - TC-AC-ACHA-142
  - TC-AC-ACHA-143
coverage:
  web: automated
---

# Submit Allocate Device Sukses Jalur Persetujuan: Waiting for Approval dan Reserve per Role dan Entitas

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan pemakaian dalam spec):

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-08 | Group Member Distributor toggle ON Group Jakarta (Budi Santoso) | #32 | `memberOnDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_ON_PASSWORD` |
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo), dipakai sebagai approver | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-09 | Group Manager Group Surabaya dengan role Manage allocation di Group Jakarta, toggle ON (Rina Kusuma) | #30 | `groupManagerSurabaya_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_GM_SURABAYA_PASSWORD` |
| A-10 | Group Member Principal toggle ON Group Pusat (Dewi Lestari) | #24 | `memberOnPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_PRIN_PASSWORD` |
| A-11 | Group Member Partner `CV Mitra Solusi` toggle ON Group Bandung (Andi Wijaya) | #44 | `memberOnPartner1_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_MB_P1_PASSWORD` |

- Login A-08 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal #21, `AC_TC_PASSWORD`). Ganti akun dengan langkah logout dan login eksplisit. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec. Akun approver TC-141 tidak disebut TC; spec memakai A-02 (lihat Temuan untuk QA).
- Data Pre-setup: Client #7 `PT Sejahtera Logistik`, #8 `PT Retail Makmur`, #10 `PT Manufaktur Unggul`; kantong #16 PT Global Distribusi saldo $20,000.00 dan #17 CV Mitra Solusi saldo $2,000.00 (Reserved awal $0.00 pada keduanya); harga #14 dan #15. Hook `before` menyetel saldo dan Reserved kantong ke nilai Pre-setup lewat fixture API Pre-setup #20 (disediakan tim FE/BE).
- Data Dinamis: empat alokasi `Waiting for Approval` dibuat spec ini (TC-141 BLE Gateway 50, TC-70 BLE Gateway 50, TC-142 BLE Gateway 20, TC-143 NFC 10). Efek: Reserved kantong PT Global Distribusi dan CV Mitra Solusi bertambah; modul tanpa Delete. Allocation ID tiap transaksi ditangkap dari baris teratas List sebagai Dynamic Reference (Notes bukan bagian data TC sehingga tanpa `{runId}`). Pembersihan: hook `after` membatalkan keempat alokasi berdasarkan Allocation ID yang dicatat lewat sesi API aktor (kemampuan disediakan tim FE/BE) sehingga Reserve dilepas.
- Kolom Payment, Paid From, dan Cost pada List ditampilkan lewat Setup Column pada langkah pertama (precondition TC-141 dan TC-142) dan ditampilkan ulang lewat Setup Column sesudah ganti akun ke A-10 dan A-11 (akun yang asersinya memakai kolom itu), karena cakupan preferensi kolom lintas akun tidak diasumsikan; preferensi kolom dihapus di hook `after` (`suite.md`).
- Kemampuan teknis: kemampuan baca Wallet Balance (saldo, Reserved, tersedia), kuota Client, dan nilai panel `Allocated quota`; akses Approvals > Device Allocation Active Tab oleh approver; pelaku kedua tidak dipakai.
- Waktu: jam server dan jam browser sinkron dan tidak diubah.
- Hook suite: flag Guided Tooltip, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column, dan seed 30 baris dinyatakan di `suite.md`. Suite berjalan serial (`parallel: false`). Hook `after` memulihkan seed lewat fixture Pre-setup #20 (Lampiran A butir A-11).

## Test Steps

### Akun A-08 Group Member Distributor toggle ON: Reserve ditahan (TC-AC-ACHA-141)

1. Buka Setup Column, tampilkan kolom Cost, Payment, dan Paid From, klik `[Save]`
2. Baca nilai panel `Allocated quota` BLE Gateway dan kuota Client `PT Sejahtera Logistik` BLE Gateway sebagai baseline
3. Klik `[+ Allocation]`
4. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `50`
5. Klik `[Submit]`
6. Verifikasi toast sukses: "Success, device allocation has been submitted for approval."
7. Verifikasi baris baru berstatus `Waiting for Approval` (badge warning)
8. Catat Allocation ID baris teratas List (transaksi TC-141, penanda pembersihan di hook `after`)
9. Verifikasi baris baru: Cost `$100.00`
10. Buka modal Allocation Log transaksi baru
11. Verifikasi Last Updated baris baru sama dengan waktu entri `Allocation created` (waktu Created)
12. Tutup modal Allocation Log
13. Verifikasi panel `Allocated quota` BLE Gateway sama dengan baseline (kuota hanya bertambah saat Completed)
14. Verifikasi kuota Client `PT Sejahtera Logistik` BLE Gateway sama dengan baseline
15. Buka Wallet Balance kantong PT Global Distribusi
16. Verifikasi saldo tetap $20,000.00
17. Verifikasi Reserved $100.00
18. Verifikasi tersedia $19,900.00

### Akun A-02 approver: Subject muncul di Approvals (TC-AC-ACHA-141)

19. Logout, lalu login sebagai A-02 (`PT Global Distribusi`), buka Approvals > Device Allocation
20. Verifikasi subject transaksi dengan Allocation ID yang dicatat pada langkah 8 muncul pada Approvals Active Tab > Device Allocation

### Akun A-09 Group Manager di group lain (TC-AC-ACHA-70)

21. Logout, lalu login sebagai A-09 (`Rina Kusuma`), buka Allocation > Device Allocation
22. Klik `[+ Allocation]`
23. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `50`
24. Klik `[Submit]`
25. Verifikasi toast sukses: "Success, device allocation has been submitted for approval."
26. Verifikasi transaksi baru berstatus `Waiting for Approval` (toggle dibaca dari role Manage allocation pada Group Jakarta yang aktif; status Group Manager di Group Surabaya tidak memberi auto-bypass dan role lain milik aktor tidak memengaruhi hasil)
27. Catat Allocation ID baris teratas List (transaksi TC-70, penanda pembersihan di hook `after`)

### Akun A-10 Group Member Principal: tanpa Reserve (TC-AC-ACHA-142)

28. Logout, lalu login sebagai A-10 (`Dewi Lestari`), buka Allocation > Device Allocation
29. Buka Setup Column, tampilkan kolom Cost, Payment, dan Paid From, klik `[Save]`
30. Klik `[+ Allocation]`
31. Pilih Category `Hardware - BLE Gateway`, Client `PT Manufaktur Unggul`, isi Quantity `20`
32. Klik `[Submit]`
33. Verifikasi toast sukses: "Success, device allocation has been submitted for approval."
34. Verifikasi baris baru berstatus `Waiting for Approval`
35. Catat Allocation ID baris teratas List (transaksi TC-142, penanda pembersihan di hook `after`)
36. Verifikasi baris baru: Payment `Free`, Paid From `—`, Cost `—` (tidak ada Reserve karena Principal tanpa wallet)

### Akun A-11 Group Member Partner: Reserve kantong Partner (TC-AC-ACHA-143)

37. Logout, lalu login sebagai A-11 (`Andi Wijaya`), buka Allocation > Device Allocation
38. Buka Setup Column, tampilkan kolom Cost, klik `[Save]`
39. Klik `[+ Allocation]`
40. Pilih Category `TAG - NFC`, Client `PT Retail Makmur`, isi Quantity `10`
41. Klik `[Submit]`
42. Verifikasi toast sukses: "Success, device allocation has been submitted for approval."
43. Verifikasi baris baru berstatus `Waiting for Approval`
44. Catat Allocation ID baris teratas List (transaksi TC-143, penanda pembersihan di hook `after`)
45. Verifikasi baris baru: Cost `$15.00`
46. Buka Wallet Balance kantong CV Mitra Solusi
47. Verifikasi saldo kantong CV Mitra Solusi $2,000.00
48. Verifikasi Reserved kantong CV Mitra Solusi $15.00

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec di atas sekitar 35 langkah: semua blok satu topik (Submit jalur persetujuan yang berhasil) dan satu kelas; tiap blok akun (A-08, A-02, A-09, A-10, A-11) berdiri sendiri dengan langkah ganti akun eksplisit sehingga kegagalan satu blok tidak menghilangkan makna blok lain (konvensi bagian 3, pemisah (b)). Semua aksi membuat data, jadi tidak ada pemisah antara pembuat dan bukan pembuat data.
- Penyimpangan urutan (S-10): dalam TC-141 asersi panel `Allocated quota` dan kuota Client (butir d) didahulukan sebelum Wallet Balance (butir c) karena panel ada di halaman Device Allocation yang sama dengan List; subject di Approvals (butir e) berada di blok akun approver A-02 yang beda akun dengan langkah ganti akun eksplisit. Blok akun dikelompokkan menurut urutan pemakaian dan masing-masing berdiri sendiri.
- Langkah penghubung (S-03): tampilkan kolom lewat Setup Column (juga sesudah ganti akun ke A-10 dan A-11, langkah 29 dan 38), baca baseline panel dan kuota, catat Allocation ID tiap transaksi baru, buka dan tutup modal Allocation Log, logout dan login ganti akun, navigasi ke Wallet Balance dan Approvals.
- Asersi gabungan sesuai S-03: pada TC-70 butir b (Group Manager di Surabaya tidak auto-bypass) adalah kesimpulan yang tidak teramati terpisah dari status `Waiting for Approval` dan diasersi sebagai satu `Verifikasi`; pada TC-142 butir c (tidak ada Reserve) diasersi sebagai bagian `Verifikasi` Payment, Paid From, dan Cost.
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment); spec tidak men-seed data dinamis bernama.
- Temuan untuk QA:
  - TC-141 butir b menyebut "Last Updated sama dengan waktu Created" tanpa kolom Created di List; spec membaca waktu Created dari entri `Allocation created` pada Allocation Log.
  - TC-141 butir e menyebut "sebagai approver" tanpa menyebut akun; Catatan TC hanya menyebut approver Section 3e, 5, 7, 8, dan 9. Spec memakai Total Control Distributor #27 (Pre-setup menandainya sebagai approver).
  - TC-70 memakai Category `BLE Gateway` (tanpa awalan `Hardware - `), sedangkan label opsi dropdown adalah `Hardware - BLE Gateway` (TC-94); spec memakai label opsi.
  - Post Condition semua TC (notifikasi in-app, widget Dashboard Pending Device Allocation, Approvals Active Tab TC-70/142/143, Wallet Transaction List) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-141 butir d menyebut kuota Client tanpa halaman pengamatan; spec memakai kemampuan baca kuota Client yang disediakan tim FE/BE.
