---
id: TC-AC-LA-E2E-064-approve-screening-detail-approval-dan-hasil-active
title: "Approve: Screening Detail Approval, Hasil Active, dan Target Pending"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-241
  - TC-AC-LA-242
  - TC-AC-LA-243
coverage:
  web: automated
---

# Approve: Screening Detail Approval, Hasil Active, dan Target Pending

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (Pre-setup #10, Total Control Distributor PT Maju Bersama); halaman License Allocation dibuka hook `beforeEach` suite (tab Current), dan spec ini berpindah ke Approvals sebagai langkah pertama.
- Akun: `totalControlDistLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34).
- Konfigurasi: Require Approval for Allocation ON (Pre-setup #38), dipastikan di hook `before` oleh fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before` oleh requester Dewi Anggraini, Pre-setup #4; tidak memakai baris Pre-setup #41 dan #81 bersama):
  - `{idAktif}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $150.00 di-Reserve, term Target Active (bentuk Pre-setup #41);
  - `{idPending}`: alokasi `Waiting for Approval` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, Cost $3,650.00 di-Reserve (bentuk Pre-setup #81).
- Data uji: Approval Note `Disetujui`.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, kemampuan membaca saldo kantong (Balance, Reserved), Current Quota/kuota term, jumlah entri Changelog modul (baseline dicatat di hook `before`), serta notifikasi `License allocated` Plan Owner (baseline jumlah dicatat pada langkah 13).
- Kemampuan teknis tambahan (disediakan tim FE/BE): seeding satu notifikasi Plan Owner PT Maju Bersama yang tidak terkait `{idAktif}` sehingga daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain sebagai anchor asersi absence notifikasi (langkah 21). Jendela tunggu 5 detik tanpa memuat ulang halaman (langkah 22) adalah pilihan spec, bukan nilai TC atau PRD (bagian 6).
- State global: saldo kantong dan kuota term berubah akibat Approve; dikembalikan oleh pembersihan record seed di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Detail Approval

1. Buka Approvals > License Allocation
2. Klik `[Review]` pada alokasi Concurrent User PT Sejahtera `{idAktif}`
3. Verifikasi Header Detail Approval menampilkan Allocation ID, License Type `Concurrent User`, Client `PT Sejahtera`, dan Target `SUBS-20260101-A1B2C · FAMS`
4. Verifikasi Body menampilkan Requested By dan Requested At
5. Verifikasi Body menampilkan Quantity `5`
6. Verifikasi Body menampilkan Payment `Wallet` (derived)
7. Verifikasi Radio Approve / Reject tampil tanpa pilihan default
8. Verifikasi field Approval Note / Rejection Reason tampil
9. Verifikasi Footer menampilkan tombol Submit
10. Verifikasi tidak ada tombol Approve atau Reject lain di Footer

### Approve dengan hasil Active

11. Pilih Approve
12. Isi Approval Note `Disetujui`
13. Catat jumlah notifikasi `License allocated` Plan Owner PT Maju Bersama sebagai baseline
14. Klik Submit
15. Verifikasi toast sukses: "Success, transaction has been approved."
16. Verifikasi alokasi `{idAktif}` `Completed` berstatus lisensi `Active`
17. Verifikasi kuota term bertambah 5
18. Verifikasi Balance kantong berkurang `$150.00` (Reserve di-Capture tanpa hitung ulang)
19. Verifikasi Reserved kantong turun
20. Buka notifikasi Plan Owner PT Maju Bersama
21. Verifikasi daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain (daftar termuat, anchor)
22. Tunggu 5 detik tanpa memuat ulang halaman
23. Verifikasi tidak ada notifikasi `License allocated` ke Plan Owner PT Maju Bersama karena entitas requester Dewi Anggraini (PT Maju Bersama) sama dengan entitas Plan Owner PT Maju Bersama (jumlah notifikasi `License allocated` sama dengan baseline langkah 13)
24. Buka Allocation > License Allocation
25. Ketik Search `{idAktif}`, tekan Enter
26. Klik row action `Allocation Log`
27. Verifikasi Allocation Log memuat entri `Allocation approved by Fajar N` dengan baris `Approval Note: Disetujui`
28. Tutup modal Allocation Log
29. Verifikasi Changelog modul tidak bertambah: jumlah entri Changelog sama dengan baseline
30. Buka Activity Log
31. Verifikasi Activity Log mencatat Approve atas `{idAktif}` oleh `Fajar N`

### Approve ke Target Pending

32. Buka Approvals > License Allocation
33. Klik `[Review]` pada alokasi `{idPending}`
34. Pilih Approve
35. Klik Submit
36. Verifikasi toast sukses: "Success, transaction has been approved."
37. Verifikasi status persetujuan `Completed`
38. Verifikasi status lisensi `Pending`
39. Verifikasi kuota belum efektif
40. Verifikasi Reserve `$3,650.00` tetap ditahan
41. Verifikasi Balance tidak berkurang

## Notes

- Langkah penghubung (S-03): langkah 13 (mencatat baseline jumlah notifikasi `License allocated` Plan Owner sebelum Approve), langkah 1, 24, 30, dan 32 (berpindah halaman), langkah 25 (Search untuk menemukan baris seed, R-16), langkah 28 (menutup modal Allocation Log), langkah 22 (jendela tunggu 5 detik tanpa Verifikasi, bagian 6).
- Langkah 20 (membuka notifikasi Plan Owner) dan 22 (jendela tunggu 5 detik tanpa Verifikasi, bagian 6) adalah langkah penghubung; langkah 21 (`Verifikasi`) adalah anchor positif asersi absence notifikasi pada langkah 23 (daftar notifikasi Plan Owner termuat dan memuat notifikasi lain; teks notifikasi lain itu tidak ada di katalog PRD sehingga tidak ditulis).
- Langkah 23 diletakkan segera setelah Approve dan sebelum navigasi; status `Active` pada langkah 16 menjadi anchor positif bagi asersi ketiadaan notifikasi (8b butir 2 dan 11). Pada langkah 29, Changelog modul dibandingkan dengan baseline (selisih nol); entri Allocation Log pada langkah 27 menjadi anchor bahwa aksi sudah tercatat.
- Satu seed `{idAktif}` dipakai berurutan oleh TC-AC-LA-241 (screening, tanpa mengubah record) dan TC-AC-LA-242 (Approve); screening tidak mengubah state sehingga urutan itu tidak melanggar S-06.
- Spec melewati sekitar 35 langkah (41 langkah). Alasan pertahanan: seluruh blok satu topik (Approve dari Detail Approval oleh Fajar Nugroho) pada dataset dan kelas harness fungsional yang sama; kelebihan langkah berasal dari langkah penghubung, anchor asersi absence notifikasi (bagian 6), dan pemecahan `Verifikasi` per klausa (S-01), serta blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-242 butir f dan butir e: akun pengamat Plan Owner untuk notifikasi `License allocated` tidak disebut; spec memakai kemampuan baca notifikasi Plan Owner yang disediakan tim FE.
  - TC-AC-LA-242 butir e menyebut "Activity Log" tanpa menyebut jalur menu; langkah 30 hanya menulis "Buka Activity Log".
  - TC-AC-LA-242 butir b dan c menyebut kuota term dan saldo kantong tanpa menyebut cara membacanya; spec memakai kemampuan baca state BE dari tim FE/BE.
  - TC-AC-LA-243 butir b ("kuota belum efektif") tidak menyebut cara mengamati; langkah 37 memakai kemampuan baca kuota term.
  - TC-AC-LA-241 Body butir "Requested By dan Requested At" tidak menyebut nilai yang diharapkan; spec mengasersi keberadaan kedua field.
