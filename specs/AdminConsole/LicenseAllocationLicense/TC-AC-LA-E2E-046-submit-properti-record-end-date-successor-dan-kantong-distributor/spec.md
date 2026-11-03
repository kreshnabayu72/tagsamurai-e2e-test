---
id: TC-AC-LA-E2E-046-submit-properti-record-end-date-successor-dan-kantong-distributor
title: "Submit Allocate: End Date Snapshot, Term Successor, dan Kantong Tunggal Distributor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-167
  - TC-AC-LA-170
  - TC-AC-LA-172
coverage:
  web: automated
---

# Submit Allocate: End Date Snapshot, Term Successor, dan Kantong Tunggal Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`, End Date 31 Dec 2026), Toko Serba Ada (#21, term Active `SUBS-20250201-J7K8L` dan term Pending `SUBS-20260819-00001`), kantong wallet (#33), Product Price (#34: Concurrent User $365 per unit per tahun). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Jam (nilai absolut, disediakan tim FE/BE): tanggal server uji 22 Dec 2026 di hook `before` untuk TC-AC-LA-172 dan TC-AC-LA-170; digeser ke 31 Dec 2026 pada langkah 23 dan ke 1 Jan 2027 pada langkah 29 untuk TC-AC-LA-167. Jam server dan jam browser diatur bersama dan dipulihkan di hook `after`.
- Kemampuan teknis: menjalankan Expiry Transition pada jam server 1 Jan 2027 (job sistem yang hanya memicu kondisi yang diuji, `P-5`); membaca saldo kantong; menampilkan kolom Paid From lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Data Dinamis: tiga alokasi Concurrent User Completed: +1 PT Sejahtera (TC-AC-LA-172, Active), +10 ke term Pending Toko Serba Ada (TC-AC-LA-170, status lisensi Pending), dan +1 PT Sejahtera (TC-AC-LA-167, Active lalu Expired). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong, Reserve, dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum tiap `[Submit]`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-172: Distributor selalu memakai kantong tunggal tanpa pilihan Pay From

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
4. Klik `[Submit]`
5. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 1) berstatus `Active` tanpa Pay From dipilih
6. Tampilkan kolom Paid From lewat Setup Column
7. Verifikasi kolom Paid From baris baru `PT ABC (Principal)` sebagai sumber kantong Distributor

### TC-AC-LA-170: Alokasi ke term successor tidak menambah kuota term sebelumnya

8. Catat baseline Allocation ID baris di halaman pertama tab Current
9. Klik `[+ Allocation]`
10. Pilih Client `Toko Serba Ada`, Target `SUBS-20250201-J7K8L`, Type `Concurrent User`, lalu catat Current Quota term Active
11. Ganti Target ke `SUBS-20260819-00001`, pilih Type `Concurrent User`, isi Additional Quantity `10`, lalu catat Current Quota term Pending
12. Klik `[Submit]`
13. Tunggu modal tertutup dan baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 8)
14. Klik `[+ Allocation]`
15. Pilih Client `Toko Serba Ada`, Target `SUBS-20250201-J7K8L`, Type `Concurrent User`
16. Verifikasi Current Quota term Active tidak berubah dari nilai langkah 10
17. Ganti Target ke `SUBS-20260819-00001` dan pilih Type `Concurrent User`
18. Verifikasi ledger term successor bertambah 10 (Current Quota term Pending naik 10 dari nilai langkah 11, belum efektif)
19. Klik `[✕]` pada header
20. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
21. Klik `[Leave]`

### TC-AC-LA-167: Tanggal kedaluwarsa alokasi adalah snapshot End Date term Target

22. Atur jam server dan jam browser ke 31 Dec 2026 (End Date term), lalu buka ulang Allocation > License Allocation tab Current
23. Catat baseline Allocation ID baris di halaman pertama tab Current
24. Klik `[+ Allocation]`
25. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
26. Klik `[Submit]`
27. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 23) tetap berstatus `Active` pada 31 Dec 2026
28. Atur jam server dan jam browser ke 1 Jan 2027 lalu jalankan Expiry Transition
29. Buka Allocation > License Allocation tab History
30. Verifikasi alokasi (dicari berdasarkan Allocation ID baris langkah 27) berstatus `Expired`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 4 kali, kejadian menutup 4 (modal tertutup oleh Submit di langkah 4, 12, dan 26; dialog Leave di langkah 19 sampai 21).
- Penyimpangan urutan (S-05, S-10): TC-AC-LA-167 dijalankan paling akhir karena menggeser jam server ke 1 Jan 2027 sehingga term Active Toko Serba Ada (End Date 31 Dec 2026) dan PT Sejahtera berubah status; TC-AC-LA-172 dan TC-AC-LA-170 dijalankan lebih dahulu pada jam 22 Dec 2026. Jam dipulihkan di hook `after`.
- Langkah penghubung (S-03): langkah 1, 8, dan 23 (baseline), langkah 6 (menampilkan kolom Paid From), langkah 13 (menunggu aksi selesai), langkah 22 dan 28 (mengatur jam), dan langkah 14 sampai 21 (membuka form ulang untuk mengamati Current Quota lalu menutup form dirty, S-08).
- Pernyataan `P-5`: job Expiry Transition pada langkah 28 hanya memicu kondisi yang diuji (alokasi menjadi Expired); objek asersi adalah snapshot End Date, bukan job.
- Temuan untuk QA:
  - TC-AC-LA-167 Langkah 7 ("buka Allocation Log") tidak punya Expected yang menyebut Allocation Log; spec tidak membuka Allocation Log dan hanya mengasersi status `Active` lalu `Expired`.
  - TC-AC-LA-167 Expected a ("Alokasi tetap `Active` pada 31 Dec 2026") menyiratkan pengamatan pada tanggal tersebut; spec mengamati setelah Submit pada jam 31 Dec 2026 dan sebelum jam digeser.
  - TC-AC-LA-170 Expected a dan b ("Current Quota term Active tidak berubah", "ledger term successor bertambah 10 (belum efektif)") tidak menyebut lokasi pengamatan; spec mengamati Current Quota di form Allocate dan tidak mengasersi efektivitas.
  - TC-AC-LA-172 Expected b menyebut `PT ABC (Principal)` sebagai sumber kantong Distributor, sedangkan Distributor PT Maju Bersama memakai kantong wallet sendiri (Pre-setup #33); label Paid From `PT ABC (Principal)` untuk Distributor dicatat apa adanya dan perlu dikonfirmasi.
  - TC-AC-LA-167 menyebut Expiry Transition tanpa kemampuan menjalankan job; disediakan tim FE/BE tanpa endpoint karangan (S-13).
