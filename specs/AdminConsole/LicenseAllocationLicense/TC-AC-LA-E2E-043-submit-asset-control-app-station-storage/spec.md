---
id: TC-AC-LA-E2E-043-submit-asset-control-app-station-storage
title: "Submit Allocate: Asset Control App, Station, dan Storage"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-159
  - TC-AC-LA-160
  - TC-AC-LA-161
  - TC-AC-LA-516
coverage:
  web: automated
---

# Submit Allocate: Asset Control App, Station, dan Storage

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Bengkel Cahaya Motor (#23, FAMS Professional Paid Active, End Date 31 Dec 2026, belum punya Asset Control App), Klinik Harapan Bunda (#24), Toko Serba Ada (#21, term Pending `SUBS-20260819-00001`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Asset Control App flat $150.00, Asset Control Station $50.00 per Station, Storage $2 per GB). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Jam: tanggal acuan server uji 22 Dec 2026 (fixture waktu, nilai absolut, disediakan tim FE/BE) untuk TC-AC-LA-516; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: empat alokasi: Asset Control App ke Bengkel Cahaya Motor (Dinamis #2, Active), Asset Control Station +10 Client-wide Klinik Harapan Bunda, Storage +50 GB Client-wide Klinik Harapan Bunda, dan Asset Control App ke term Pending Toko Serba Ada (Pending, Reserve $150.00). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dan saldo kantong Distributor (Available, Reserved, Balance) dicatat sebelum tiap `[Submit]`.
- Kemampuan teknis: membaca saldo kantong (disediakan tim FE/BE); menampilkan kolom Cost lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-159: Submit Asset Control App tanpa Quantity mengaktifkan App pada Subscription

1. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
2. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo kantong Distributor
3. Klik `[+ Allocation]`
4. Pilih Client `Bengkel Cahaya Motor`, Target term FAMS Professional, Type `Asset Control App`
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, license has been allocated."
7. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 2): License Type `Addon (Asset Control App)`, Quantity `—`, Status `Active`
8. Verifikasi Cost `$150.00` sebagai biaya flat aktivasi sekali tanpa prorata
9. Buka Subscription Detail term FAMS Professional Bengkel Cahaya Motor
10. Verifikasi status Asset Control App pada Subscription itu `Active`

### TC-AC-LA-160: Submit Asset Control Station Client-wide tanpa tanggal kedaluwarsa

11. Buka Allocation > License Allocation tab Current, lalu catat baseline Allocation ID baris di halaman pertama
12. Klik `[+ Allocation]`
13. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Asset Control Station`, isi Additional Quantity `10`
14. Klik `[Submit]`
15. Verifikasi toast sukses "Success, license has been allocated."
16. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 11): License Type `Asset Control Station`, Product, Subscription ID, dan Plan Owner `—`, Status `Active`
17. Verifikasi Cost `$500.00`

### TC-AC-LA-161: Submit Storage Client-wide per GB

18. Catat baseline Allocation ID baris di halaman pertama tab Current
19. Klik `[+ Allocation]`
20. Pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type `Storage`, isi Additional Quantity `50`
21. Klik `[Submit]`
22. Verifikasi toast sukses "Success, license has been allocated."
23. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 18): Quantity `+50 GB`, Status `Active`
24. Verifikasi Cost `$100.00`
25. Verifikasi Subscription ID `—`

### TC-AC-LA-516: Asset Control App ke Target term Pending dengan toggle OFF

26. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Distributor
27. Klik `[+ Allocation]`
28. Pilih Client `Toko Serba Ada`, Target `SUBS-20260819-00001`, Type `Asset Control App`
29. Klik `[Submit]`
30. Verifikasi toast sukses "Success, license has been allocated."
31. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 26): License Type `Addon (Asset Control App)`, Quantity `—`, Status `Pending` severity warning
32. Verifikasi Reserve `$150.00` ditahan: Reserved naik `$150.00`
33. Verifikasi Available turun `$150.00`
34. Verifikasi Balance tidak berkurang (Capture terjadi saat term mulai)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 4 kali, kejadian menutup 4 (modal tertutup oleh Submit di langkah 5, 14, 21, dan 29).
- Spec 34 langkah; keempat blok satu topik (Submit alokasi jenis App, Station, dan Storage dengan toggle OFF) dan berdiri sendiri.
- Langkah penghubung (S-03): langkah 1 (menampilkan kolom Cost lewat Setup Column, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 2, 11, 18, dan 26 (baseline dan pindah halaman), langkah 9 (membuka Subscription Detail).
- Temuan untuk QA:
  - TC-AC-LA-159 Expected d ("Status Asset Control App pada Subscription itu menjadi `Active`") tidak menyebut lokasi pengamatan; spec membuka Subscription Detail term (langkah 9) tanpa menyebut bagian tertentu, lokasi ditentukan tim FE.
  - TC-AC-LA-159 Post Condition ("Tanggal kedaluwarsa = 31 Dec 2026") tidak punya langkah observasi; tidak diasersi.
  - TC-AC-LA-159 Langkah 3 dan TC-AC-LA-516 Langkah 3 memakai "term FAMS Professional" tanpa ID Subscription; Pre-setup #23 tidak mencantumkan ID.
  - TC-AC-LA-160 Post Condition ("Tidak ada tanggal kedaluwarsa; ledger Client bertambah 10") dan TC-AC-LA-161 Post Condition ("Ledger Storage Client bertambah 50 GB") tidak punya langkah observasi; tidak diasersi.
  - TC-AC-LA-516 Expected c menyebut pembacaan Reserved, Available, dan Balance yang tidak tampil di halaman License Allocation; spec memakai kemampuan baca saldo yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
