---
id: TC-AC-LA-E2E-048-notifikasi-submit-plan-owner-dan-approver
title: "Notifikasi In-App akibat Submit: Plan Owner dan Approver Pool"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-174
  - TC-AC-LA-505
  - TC-AC-LA-175
coverage:
  web: automated
---

# Notifikasi In-App akibat Submit: Plan Owner dan Approver Pool

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Default User Principal `defaultUserLic_automated_{namaCompany}@qwertysystem.net` (`Sari Pratama`, Pre-setup #2), password `Spectra.env.AC_LA_DEFAULT_USER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`; Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10, staf Plan Owner PT Maju Bersama), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`; Group Manager approve-only `gmApproveOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Rian Hartono`, Pre-setup #8), password `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`; Additional Approver `additionalApproverLic_automated_{namaCompany}@qwertysystem.net` (`Maya Tanjung`, Pre-setup #11), password `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), kantong wallet (#33), Product Price (#34: Concurrent User $365 per unit per tahun), Approval Config pada group Client uji dengan Additional Approver `Maya Tanjung` (#38). `Fajar Nugroho` juga didaftarkan sebagai Additional Approver pada group Client uji (multi-role), diatur fixture backend (disediakan tim FE/BE) di hook `before`.
- Toggle Require Approval for Allocation: OFF (#39) untuk TC-AC-LA-174 dan TC-AC-LA-505 (diatur di hook `before`), ON (#38) untuk TC-AC-LA-175 (diatur lewat langkah 15); diatur fixture backend dan dipulihkan ke keadaan awal di hook `after`.
- Data Dinamis: tiga alokasi Concurrent User +1 ke PT Sejahtera: oleh Sari P (Completed Active Free), oleh Dewi A (Completed Active Wallet), dan oleh Dewi A (Waiting for Approval). Notifikasi yang dihasilkan diidentifikasi lewat Allocation ID pada Body, sehingga baseline notifikasi nol per ID. Alokasi dan notifikasi tidak dapat dihapus; saldo kantong dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dan saldo kantong Distributor dicatat sebelum tiap blok.
- Kemampuan teknis: membuka notifikasi in-app tiap akun; membaca saldo kantong (disediakan tim FE/BE); menampilkan kolom Payment lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-174: Notifikasi Plan Owner saat Completed langsung oleh requester dari entitas lain (Principal)

1. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
2. Catat baseline Allocation ID baris di halaman pertama tab Current
3. Klik `[+ Allocation]`
4. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
5. Klik `[Submit]`
6. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 2; dicatat sebagai ID-A) berstatus `Active`
7. Verifikasi Payment baris baru: `Free`

### TC-AC-LA-505: Notifikasi Plan Owner dilewati bila requester berasal dari entitas Plan Owner

8. Ganti akun: logout `Sari P`, login sebagai `Dewi Anggraini` dengan `Spectra.env.AC_LA_DIST_FULL_PASSWORD`, buka Allocation > License Allocation tab Current
9. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo kantong Distributor
10. Klik `[+ Allocation]`
11. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`, lalu catat Cost preview
12. Klik `[Submit]`
13. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 9; dicatat sebagai ID-B) berstatus `Active`
14. Verifikasi saldo kantong Distributor berkurang sebesar Cost langkah 11

### TC-AC-LA-175: Notifikasi Waiting for Approval ke approver pool tanpa duplikat

15. Atur toggle Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend hingga tersimpan, lalu buka ulang Allocation > License Allocation tab Current
16. Catat baseline Allocation ID baris di halaman pertama tab Current
17. Klik `[+ Allocation]`
18. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
19. Klik `[Submit]`
20. Tunggu modal tertutup, lalu catat Allocation ID baris baru (tidak ada pada baseline langkah 16) berstatus `Waiting for Approval` sebagai ID-C
21. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
22. Buka notifikasi
23. Verifikasi notifikasi `License allocated` dengan Body `ID-A · Concurrent User · PT Sejahtera` (nilai ID-A langkah 6) diterima Plan Owner PT Maju Bersama karena entitas requester (Principal) berbeda dari entitas Plan Owner
24. Verifikasi notifikasi `Waiting for your approval` dengan Body `ID-C · Concurrent User · PT Sejahtera` dan tombol `[Detail]`
25. Verifikasi `Fajar Nugroho` (Total Control dan Additional Approver) menerima tepat satu notifikasi untuk ID-C
26. Verifikasi tidak ada notifikasi `License allocated` dengan Body `ID-B · Concurrent User · PT Sejahtera` (entitas requester sama dengan entitas Plan Owner)
27. Ganti akun: logout `Fajar N`, login sebagai `Rian Hartono` dengan `Spectra.env.AC_LA_GM_APPROVE_PASSWORD`
28. Buka notifikasi
29. Verifikasi notifikasi `Waiting for your approval` dengan Body `ID-C · Concurrent User · PT Sejahtera` dan tombol `[Detail]`
30. Ganti akun: logout `Rian H`, login sebagai `Maya Tanjung` dengan `Spectra.env.AC_LA_ADD_APPROVER_PASSWORD`
31. Buka notifikasi
32. Verifikasi notifikasi `Waiting for your approval` dengan Body `ID-C · Concurrent User · PT Sejahtera` dan tombol `[Detail]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 3 kali, kejadian menutup 3 (modal tertutup oleh Submit di langkah 5, 12, dan 19).
- Penyimpangan urutan (S-05, S-10): pembacaan notifikasi `Fajar Nugroho` untuk TC-AC-LA-174 dan TC-AC-LA-505 (Langkah 7 dan Langkah 2 TC) dilakukan di langkah 22 sampai 26 pada sesi yang sama dengan TC-AC-LA-175 supaya ganti akun ke `Fajar Nugroho` hanya satu kali. Notifikasi dibedakan lewat Allocation ID pada Body (ID-A, ID-B, ID-C), sehingga urutan pembacaan tidak memengaruhi hasil.
- Langkah penghubung (S-03): langkah 1 (menampilkan kolom Payment lewat Setup Column, tanpa `Verifikasi`; kolom Payment tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 2, 9, dan 16 (baseline; langkah 16 menjadi pembanding ID-C), langkah 15 (mengatur toggle), langkah 20 (menunggu aksi selesai dan mencatat ID-C), langkah 22, 28, dan 31 (membuka notifikasi).
- Asersi absence langkah 26 didahului Verifikasi notifikasi lain pada surface yang sama (langkah 23 sampai 25; bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-174 Expected b ("Payment `Free` tanpa mutasi wallet") untuk Principal tidak punya cara mengamati "mutasi wallet" (Principal tidak punya wallet); hanya Payment `Free` yang diasersi.
  - TC-AC-LA-174 dan TC-AC-LA-505 Data Uji menyebut entitas Plan Owner PT Maju Bersama tetapi tidak menyebut cara membuktikan penerima notifikasi selain akun `Fajar Nugroho`; spec memakai akun itu.
  - TC-AC-LA-175 Precondition mensyaratkan `Fajar Nugroho` juga Additional Approver pada group Client uji; mekanisme penyiapan tidak disebut TC dan disediakan tim FE/BE (S-13).
  - TC-AC-LA-175 Expected a menulis Body `[Allocation ID] · Concurrent User · PT Sejahtera`; spec menggantinya dengan nilai Allocation ID yang dicatat (ID-C), bentuk templat tidak diasersi.
