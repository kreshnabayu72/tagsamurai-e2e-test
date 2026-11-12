---
id: TC-AC-LA-E2E-044-submit-status-awal-toggle-approval-requester-distributor
title: "Submit Allocate: Status Awal Berdasarkan Toggle Approval dan Target Pending (Distributor)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-162
  - TC-AC-LA-165
  - TC-AC-LA-166
coverage:
  web: automated
---

# Submit Allocate: Status Awal Berdasarkan Toggle Approval dan Target Pending (Distributor)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), Toko Serba Ada (#21, term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Concurrent User $365 per unit per tahun).
- Toggle Require Approval for Allocation: ON (#38) untuk TC-AC-LA-162 dan TC-AC-LA-166 (diatur di hook `before`), OFF (#39) untuk TC-AC-LA-165 (diatur lewat langkah 27); diatur fixture backend (disediakan tim FE/BE) dan dipulihkan ke keadaan awal di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE); jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: tiga alokasi Concurrent User +10: ke PT Sejahtera (Waiting for Approval, Reserve $100.00), ke term Pending Toko Serba Ada (Waiting for Approval, Reserve $3,650.00), dan ke term Pending Toko Serba Ada (Completed, status lisensi Pending, Reserve $3,650.00). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong, Reserve, dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current, saldo kantong Distributor (Available, Reserved, Balance), dan Current Quota dicatat sebelum tiap `[Submit]`.
- Kemampuan teknis: membaca saldo kantong (disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-162: Toggle ON dengan requester biasa menghasilkan Waiting for Approval dengan Reserve

1. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Distributor
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`, lalu catat Current Quota
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, license has been allocated."
6. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 1) berstatus `Waiting for Approval` severity warning
7. Verifikasi Available kantong berkurang `$100.00` (Reserved bertambah `$100.00`)
8. Verifikasi Balance kantong tidak berubah
9. Klik `[+ Allocation]`
10. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`
11. Verifikasi Current Quota term tidak berubah dari nilai langkah 3
12. Klik `[×]` pada header
13. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
14. Klik `[Leave]`

### TC-AC-LA-166: Toggle ON dengan Target Pending menghasilkan Waiting for Approval

15. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Distributor
16. Klik `[+ Allocation]`
17. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Concurrent User`, isi Additional Quantity `10`, lalu catat Current Quota
18. Klik `[Submit]`
19. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 15) berstatus `Waiting for Approval`
20. Verifikasi Reserve `$3,650.00` ditahan
21. Klik `[+ Allocation]`
22. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Concurrent User`
23. Verifikasi Current Quota term Pending tidak berubah dari nilai langkah 17 (kuota ledger belum berubah)
24. Klik `[×]` pada header
25. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
26. Klik `[Leave]`

### TC-AC-LA-165: Toggle OFF dengan Target Pending, Completed berstatus lisensi Pending dengan Reserve ditahan

27. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan, lalu buka ulang Allocation > License Allocation tab Current
28. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Distributor
29. Klik `[+ Allocation]`
30. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Concurrent User`, isi Additional Quantity `10`, lalu catat Current Quota
31. Klik `[Submit]`
32. Verifikasi baris baru di tab Current (Allocation ID tidak ada pada baseline langkah 28) berstatus `Pending` severity warning
33. Verifikasi Reserve `$3,650.00` ditahan (belum Capture) dan Balance tidak berkurang
34. Klik `[+ Allocation]`
35. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Concurrent User`
36. Verifikasi Current Quota term Pending bertambah 10 terhadap nilai langkah 30 (kuota dicatat di ledger term Pending)
37. Klik `[×]` pada header
38. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
39. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 6 kali, kejadian menutup 6 (modal tertutup oleh Submit di langkah 4, 18, dan 31; dialog Leave di langkah 12 sampai 14, 24 sampai 26, dan 37 sampai 39).
- Spec 39 langkah, di atas smell 35 langkah; ketiga blok satu topik (status awal hasil Submit Distributor menurut toggle dan Target) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pengamatan Current Quota (9 sampai 14, 21 sampai 26, 34 sampai 39) mengikuti Langkah 7 TC-AC-LA-162 dan Expected TC-AC-LA-166 dan TC-AC-LA-165 yang menyebut kuota ledger.
- Penyimpangan urutan (S-10): TC-AC-LA-166 dijalankan sebelum TC-AC-LA-165 supaya toggle ON (TC-AC-LA-162 dan TC-AC-LA-166) dan toggle OFF (TC-AC-LA-165) tidak bolak-balik.
- Langkah penghubung (S-03): langkah 1, 15, dan 28 (baseline), langkah 27 (mengatur toggle), langkah 12 sampai 14, 24 sampai 26, dan 37 sampai 39 (menutup form dirty, S-08).
- Temuan untuk QA:
  - TC-AC-LA-165 Expected c ("Kuota dicatat di ledger term Pending tetapi belum efektif") tidak menyebut tempat pengamatan atau cara membuktikan "belum efektif"; spec mengamati Current Quota form Allocate (bertambah 10) dan tidak mengasersi efektivitas.
  - TC-AC-LA-166 Expected b ("Kuota ledger belum berubah") menyiratkan pengamatan Current Quota term Pending; spec mengamati Current Quota form Allocate.
  - TC-AC-LA-162 Expected c menulis "Available kantong berkurang $100.00 (Reserved bertambah)" tanpa menyebut lokasi pembacaan saldo; spec memakai kemampuan baca saldo yang disediakan tim FE/BE.
  - Post Condition TC-AC-LA-162 ("Reserve $100.00 ditahan") dan TC-AC-LA-165 ("Ledger term Pending bertambah belum efektif; Reserve ditahan") diwakili oleh Expected yang sama; tidak ada langkah observasi tambahan.
