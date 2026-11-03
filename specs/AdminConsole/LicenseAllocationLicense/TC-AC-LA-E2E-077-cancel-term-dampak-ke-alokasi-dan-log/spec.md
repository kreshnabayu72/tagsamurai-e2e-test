---
id: TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log
title: "Cancel Term: Dampak ke Alokasi Active, Pending, Station, Storage, dan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-274
  - TC-AC-LA-275
  - TC-AC-LA-276
  - TC-AC-LA-277
  - TC-AC-LA-397
  - TC-AC-LA-527
coverage:
  web: automated
---

# Cancel Term: Dampak ke Alokasi Active, Pending, Station, Storage, dan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (target aksi Cancel Subscription): Bengkel Cahaya Motor (#23), Toko Serba Ada (#21) dengan term Pending `SUBS-20260819-00001`, Klinik Harapan Bunda (#24) dengan FAMS Professional dan SAMS Growth Paid Active; kantong wallet (#33), Product Price (#34). Term yang di-Cancel adalah data Pre-setup yang tidak dapat dimiliki spec (satu Client hanya punya satu term Pending dan Subscription Paid Active yang dibatalkan), sehingga dipulihkan oleh fixture backend yang disediakan tim FE/BE di hook `before`, `after`, dan langkah penghubung antar blok (S-06, pengecualian 2026-10-30). Efek pada Last Updated Subscription dan audit trail dicatat di hook `after`.
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup yang disebut): alokasi `Active` Concurrent User +10 Bengkel Cahaya Motor oleh `Dewi A` (bentuk #47) untuk TC-AC-LA-274; alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke `SUBS-20260819-00001` Toko Serba Ada (bentuk #46, Cost $3,650.00 di-Reserve) untuk TC-AC-LA-275, TC-AC-LA-397, dan TC-AC-LA-527 (dibuat ulang oleh fixture backend sebelum tiap blok); alokasi `Active` Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide` Klinik Harapan Bunda (bentuk #52) untuk TC-AC-LA-276 dan TC-AC-LA-277. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): fixture backend yang memulihkan term yang di-Cancel dan seed alokasinya; tanggal acuan server uji 22 Dec 2026 (fixture waktu) untuk TC-AC-LA-527. Baseline entri log dicatat per Allocation ID seed (baseline nol karena seed baru, S-12).
- State global yang diubah: status Subscription pada Pre-setup #21, #23, #24; dipulihkan lewat fixture backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-274: Cancel term, alokasi Active menjadi Expired seketika tanpa refund

1. Cancel Subscription pada term FAMS Professional Bengkel Cahaya Motor yang memuat seed 274
2. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 274, tekan Enter
3. Verifikasi alokasi seed 274 `Expired` seketika
4. Verifikasi baris seed 274 berada di tab History
5. Buka Wallet
6. Verifikasi Balance kantong tidak dikembalikan (tanpa refund)
7. Buka Changelog, cari entri dengan Allocation ID seed 274
8. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
9. Buka Activity Log, cari entri dengan Allocation ID seed 274
10. Verifikasi Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
11. Buka Allocation Log seed 274
12. Verifikasi entri `Allocation expired` dengan `Reason: Subscription canceled`
13. Pulihkan term Bengkel Cahaya Motor lewat fixture backend hingga tersimpan

### TC-AC-LA-275: Cancel term, alokasi Pending menjadi Expired seketika dengan Release Reserve

14. Cancel Subscription pada term Pending `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 275
15. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 275, tekan Enter
16. Verifikasi alokasi Pending seed 275 `Expired` seketika
17. Buka Wallet
18. Verifikasi Reserve $3,650.00 dilepas (Release), Balance tidak berubah
19. Buka Changelog, cari entri dengan Allocation ID seed 275
20. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
21. Buka Activity Log, cari entri dengan Allocation ID seed 275
22. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
23. Pulihkan term Pending Toko Serba Ada dan seed alokasinya lewat fixture backend hingga tersimpan

### TC-AC-LA-397: Log Auto-Expire karena Cancel term pada alokasi Pending

24. Cancel term `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 397
25. Buka Changelog, cari entri dengan Allocation ID seed 397
26. Verifikasi entri tampil dengan Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
27. Buka Activity Log, cari entri dengan Allocation ID seed 397
28. Verifikasi Action `Auto-Expire`, Status `Pending` ke `Expired`, Modified By `System`
29. Buka System Log, ketik Search Allocation ID seed 397, tekan Enter
30. Verifikasi empty state `No results found` tampil pada System Log (anchor)
31. Verifikasi tidak ada entri System Log untuk seed 397
32. Pulihkan term Pending Toko Serba Ada dan seed alokasinya lewat fixture backend hingga tersimpan

### TC-AC-LA-527: Event Allocation Log Allocation expired karena Cancel term

33. Atur tanggal acuan server uji 22 Dec 2026 (fixture waktu)
34. Cancel Subscription pada term Pending `SUBS-20260819-00001` Toko Serba Ada yang memuat seed 527
35. Buka Allocation > License Allocation, klik tab `History`, ketik Search Allocation ID seed 527, tekan Enter, lalu klik row action `Allocation Log` pada baris itu
36. Verifikasi judul `Allocation expired` tanpa `by [PIC]`
37. Verifikasi Description `Reason: Subscription canceled`
38. Verifikasi entri memuat Date & Time sesuai General Settings
39. Verifikasi baris judul berupa teks biasa, bukan badge
40. Pulihkan term Pending Toko Serba Ada dan tanggal acuan server lewat fixture backend hingga tersimpan

### TC-AC-LA-276: Cancel term tidak memengaruhi alokasi Station dan Storage Client

41. Cancel Subscription FAMS Professional Klinik Harapan Bunda
42. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Station, tekan Enter
43. Verifikasi alokasi Station dan Storage tetap `Active` di tab Current
44. Buka Subscription Detail > License Quota Klinik Harapan Bunda
45. Verifikasi alokasi pada ledger term yang dibatalkan Expired sedangkan ledger Client tidak berubah

### TC-AC-LA-277: Station tetap Active tanpa job dan tanpa refund saat Client kehilangan semua Subscription Paid Active

46. Cancel Subscription SAMS Growth Klinik Harapan Bunda sehingga seluruh Subscription Paid Active Client di-Cancel
47. Buka Allocation > License Allocation tab Current dan Allocation Log alokasi Station
48. Verifikasi status alokasi Station tetap `Active` dan entri `Allocation created by [PIC]` (PIC = pelaku seed) Station tampil pada Allocation Log (anchor)
49. Verifikasi tidak ada entri log baru pada Allocation Log Station
50. Buka Wallet
51. Verifikasi tidak ada refund wallet
52. Pulihkan seluruh Subscription Klinik Harapan Bunda dan seed alokasinya lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti pengelompokan Pre-setup: TC-AC-LA-397 dan TC-AC-LA-527 sebelum TC-AC-LA-276 dan TC-AC-LA-277 yang membatalkan seluruh Subscription Client.
- Langkah penghubung (S-03): langkah 2, 15, 35, 42 (tab dan Search untuk menemukan baris target, R-16), 5, 7, 9, 11, 17, 19, 21, 25, 27, 29 (termasuk Search Allocation ID di System Log), 44, 47, 50 (membuka surface), 13, 23, 32, 40, 52 (memulihkan term lewat fixture backend), 33 (tanggal acuan).
- P-1: langkah 31 (tidak ada entri System Log) dan 49 (tidak ada entri log baru) berbaseline (S-12). Anchor positif langkah 31: langkah 30 (empty state `No results found` pada System Log setelah Search Allocation ID seed 397, pola spec 022 dan 072), karena anchor Changelog dan Activity Log (langkah 26, 28) berada di surface lain. Anchor positif langkah 49: langkah 48.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu topik aksi (Cancel term) dengan dataset yang sama, tiap blok berdiri sendiri lewat pemulihan fixture, dan blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-274 sampai 277, 397, 527 tidak menyebut jalur Cancel Subscription (halaman dan akun); spec memakai Subscription Detail dengan Pre-setup #10 dan jalur halaman disediakan tim FE.
  - TC-AC-LA-275, 397, 527 memakai satu alokasi Pre-setup #46 pada satu-satunya term Pending Toko Serba Ada; Cancel term sekali memakai habis term itu sehingga setiap blok memulihkan term dan seed lewat fixture backend.
  - TC-AC-LA-274 Expected a menulis "(dalam transaksi Cancel)"; sifat transaksi tidak teramati di UI dan hanya status `Expired` yang diasersi.
  - TC-AC-LA-276 Expected b ("ledger Client tidak berubah") tidak menyebut cara pengamatan ledger; spec memakai Subscription Detail > License Quota.
  - TC-AC-LA-277 Precondition b menyebut seluruh Subscription Paid Active di-Cancel tanpa langkah; spec menyalinnya sebagai langkah 46 dan memakai Post Condition tanpa observasi tambahan.
