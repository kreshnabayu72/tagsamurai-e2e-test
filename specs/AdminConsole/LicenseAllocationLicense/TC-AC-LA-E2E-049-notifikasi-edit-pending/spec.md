---
id: TC-AC-LA-E2E-049-notifikasi-edit-pending
title: "Notifikasi In-App akibat Edit Pending"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-438
  - TC-AC-LA-495
coverage:
  web: automated
---

# Notifikasi In-App akibat Edit Pending

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10, staf Plan Owner PT Maju Bersama dan anggota approver pool), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Default User Principal `defaultUserLic_automated_{namaCompany}@qwertysystem.net` (`Sari Pratama`, Pre-setup #2), password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): Toko Serba Ada (#21, term Active `SUBS-20250201-J7K8L` dan term Pending `SUBS-20260819-00001`), kantong wallet (#33), Product Price (#34).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bukan baris Pre-setup #46 dan #67 bersama): alokasi Completed berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` oleh `Dewi A` (Cost $3,650.00 di-Reserve) untuk TC-AC-LA-438, dan alokasi Completed berstatus lisensi `Pending` Concurrent User +10 ke term Pending yang sama oleh `Sari P` (Payment Free tanpa Reserve) untuk TC-AC-LA-495. Allocation ID tiap seed dibaca dari hasil seeding. Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong, Reserve, dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Toggle Require Approval for Allocation: ON (#38) untuk TC-AC-LA-438 (diatur di hook `before`), OFF (#39) untuk TC-AC-LA-495 (diatur lewat langkah 11); diatur fixture backend (disediakan tim FE/BE) dan dipulihkan ke keadaan awal di hook `after`.
- Kemampuan teknis: seeding alokasi Pending lewat API; membuka notifikasi in-app tiap akun; menampilkan kolom Payment lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-438: Notifikasi Edit Pending yang kembali ke Waiting for Approval ke approver pool

1. Ketik Search Allocation ID seed Dewi (alokasi Pending Dewi A), tekan Enter
2. Klik `Edit` pada baris Pending tersebut
3. Ubah Quantity dari `10` menjadi `20`, lalu klik `[Save]`
4. Klik `[Send]` pada dialog D-04
5. Tunggu aksi selesai
6. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
7. Buka notifikasi
8. Verifikasi approver pool menerima notifikasi `Waiting for your approval` dengan Body `Allocation ID seed Dewi · Concurrent User · Toko Serba Ada`
9. Buka Approvals > License Allocation Tab Active
10. Verifikasi baris alokasi itu tampil kembali di Approvals > License Allocation Tab Active dengan status `Waiting for Approval`

### TC-AC-LA-495: Notifikasi Edit Pending ke Active diterima Plan Owner bila requester dari entitas lain

11. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan
12. Ganti akun: logout `Fajar N`, login sebagai `Sari Pratama` dengan `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`, buka Allocation > License Allocation tab Current
13. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
14. Ketik Search Allocation ID seed Sari (alokasi Pending Sari P), tekan Enter
15. Klik `Edit` pada baris Pending milik sendiri
16. Ganti Target ke term Active `SUBS-20250201-J7K8L`, pilih Type `Concurrent User`, isi Quantity `10`, lalu klik `[Save]`
17. Verifikasi status alokasi `Active`
18. Verifikasi Payment alokasi: `Free`
19. Tunggu aksi selesai
20. Ganti akun: logout `Sari P`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
21. Buka notifikasi
22. Verifikasi Plan Owner PT Maju Bersama menerima notifikasi `License allocated` dengan Body `Allocation ID seed Sari · Concurrent User · Toko Serba Ada`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Tidak ada form Allocate yang dibuka; form Edit dibuka lewat `Edit` pada baris dan ditutup oleh `[Save]` (langkah 3 dan 16).
- Langkah penghubung (S-03): langkah 13 (menampilkan kolom Payment lewat Setup Column, tanpa `Verifikasi`; kolom Payment tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 1 dan 14 (Search untuk menemukan baris target, R-16), langkah 5 dan 19 (menunggu aksi selesai karena langkah berikutnya ganti akun), langkah 11 (mengatur toggle), langkah 7, 9, 21 (membuka notifikasi dan Approvals), dan langkah 4 (mengonfirmasi dialog D-04 sebagai bagian dari TC-AC-LA-438 Langkah 1).
- Body notifikasi pada langkah 8 dan 22 memakai nilai Allocation ID seed (data milik spec), bukan templat `[Allocation ID]`.
- Penyimpangan data (S-06): TC memakai baris Pre-setup #46 (TC-AC-LA-438) dan #67 (TC-AC-LA-495); spec memakai seed milik spec dengan keadaan yang sama agar Pre-setup bersama tidak berubah.
- Temuan untuk QA:
  - TC-AC-LA-438 Langkah 1 menyebut dialog D-04 dengan tombol `[Send]` tanpa menyebut judul dan isi dialog; teks dialog tidak diasersi.
  - TC-AC-LA-438 Expected a menulis Body `[Allocation ID] · Concurrent User · Toko Serba Ada`; bentuk templat diganti nilai Allocation ID seed dan tidak diasersi sebagai templat.
  - TC-AC-LA-495 Langkah 2 mengganti Target ke term Active dan Type `Concurrent User`, tetapi tidak menyebut apakah Client ikut berubah; spec memakai Client Toko Serba Ada yang sama.
  - TC-AC-LA-495 Expected a ("tanpa mutasi wallet") untuk Principal tidak punya cara pengamatan selain Payment `Free`; hanya Payment `Free` yang diasersi.
