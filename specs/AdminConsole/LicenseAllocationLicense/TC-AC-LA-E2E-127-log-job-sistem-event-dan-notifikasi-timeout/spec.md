---
id: TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout
title: "Log Job Sistem: Event Expired, Entri Allocation Log Tanpa PIC, dan Notifikasi Timeout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-408
  - TC-AC-LA-412
  - TC-AC-LA-525
  - TC-AC-LA-526
  - TC-AC-LA-437
coverage:
  web: automated
---

# Log Job Sistem: Event Expired, Entri Allocation Log Tanpa PIC, dan Notifikasi Timeout

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Hendra Wijaya (pengamat log setelah job berjalan; job sistem berjalan tanpa aktor login); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Fajar Nugroho dan Dewi Anggraini dilakukan eksplisit pada blok notifikasi; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Hendra Wijaya | #1 | Total Control Principal (membuka log setelah job) | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver aktif, penerima notifikasi) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |
| Dewi Anggraini | #4 | Distributor PT Maju Bersama (requester, penerima notifikasi) | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE). Dewi Anggraini tidak tercantum di ACC TC-AC-LA-437 (lihat Temuan untuk QA).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), Bengkel Cahaya Motor (Pre-setup #23; FAMS Professional Paid Active, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Approval Timeout 3 day(s) (Pre-setup #40), Require Approval for Allocation ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41, #46, dan #47 bersama):
  - `{idTimeout}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idActivate}`: alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (bentuk Pre-setup #46);
  - `{idExpire}`: alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor (End Date 31 Dec 2026), requester Dewi Anggraini (bentuk Pre-setup #47).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture waktu untuk jam server dan jam browser dengan nilai absolut; kueri fixture status job; kemampuan membaca jumlah entri Allocation Log `{idTimeout}`, `{idActivate}`, dan `{idExpire}` (`{nLogTimeout}`, `{nLogActivate}`, `{nLogExpire}`) dan jumlah notifikasi berjudul `License allocation canceled automatically` pada akun Dewi Anggraini (`{nNotifDewi}`) dan Fajar Nugroho (`{nNotifFajar}`), semuanya dicatat di hook `before` setelah seeding dan sebelum jam digeser (S-12).
- State global: jam server dan jam browser diatur ke `1 Jan 2027 00:01` (zona waktu Plan Owner) satu kali untuk ketiga job: Timeout Auto-Cancel (jauh melewati SLA 3 hari sejak waktu terbit seed), Activation Transition (Start Date term Pending 1 Jan 2027 00:00 ditambah 1 menit), dan Expiry Transition (End Date 31 Dec 2026 berakhir 1 Jan 2027 00:00 ditambah 1 menit). Margin 1 menit dihitung dari Start Date dan End Date term seed. Jam dipulihkan sebelum Hendra Wijaya membuka Changelog atau Activity Log (S-09); hook `after` memulihkan jam sebagai cadangan. Job yang berjalan juga memproses alokasi lain yang memenuhi syarat; data Pre-setup yang terpengaruh dipulihkan baseline automation. Log bercap waktu masa depan dicari berdasarkan Allocation ID (S-12).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Menjalankan job sistem

1. Atur jam server dan jam browser ke `1 Jan 2027 00:01` (nilai absolut, zona waktu Plan Owner)
2. Tunggu satu siklus job hingga kueri fixture status job menyatakan Timeout Auto-Cancel, Activation Transition, dan Expiry Transition selesai (batas tunggu 2 menit)
3. Pulihkan jam server dan jam browser ke waktu nyata

### Allocation Log Allocation expired (TC-AC-LA-408, TC-AC-LA-526 butir a)

4. Klik tab `History`
5. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
6. Ketik Search `{idExpire}`, tekan Enter
7. Klik row action `Allocation Log` pada baris `{idExpire}`
8. Verifikasi judul entri `Allocation expired` tanpa `by [PIC]`
9. Verifikasi Description entri `Reason: Subscription term ended`
10. Verifikasi entri memuat Date & Time sesuai General Settings
11. Verifikasi baris judul berupa teks biasa, bukan badge
12. Verifikasi jumlah entri Allocation Log `{idExpire}` bertambah satu terhadap `{nLogExpire}`
13. Tutup modal Allocation Log

### Allocation Log Allocation activated (TC-AC-LA-525 butir a)

14. Klik tab `Current`
15. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
16. Ketik Search `{idActivate}`, tekan Enter
17. Klik row action `Allocation Log` pada baris `{idActivate}`
18. Verifikasi judul entri `Allocation activated` tanpa `by [PIC]`
19. Verifikasi jumlah entri Allocation Log `{idActivate}` bertambah satu terhadap `{nLogActivate}`
20. Tutup modal Allocation Log

### Allocation Log Allocation auto-canceled (TC-AC-LA-412 butir a)

21. Klik tab `History`
22. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
23. Ketik Search `{idTimeout}`, tekan Enter
24. Klik row action `Allocation Log` pada baris `{idTimeout}`
25. Verifikasi judul entri `Allocation auto-canceled` tanpa `by [PIC]`
26. Verifikasi jumlah entri Allocation Log `{idTimeout}` bertambah satu terhadap `{nLogTimeout}`
27. Tutup modal Allocation Log
28. Klik tab `Current`

### Changelog dan Activity Log dengan Modified By System (TC-AC-LA-412 butir b, TC-AC-LA-525 butir b, TC-AC-LA-526 butir b)

29. Klik ikon `Changelog` pada List
30. Ketik Search `{idTimeout}`, tekan Enter
31. Verifikasi Changelog memuat entri Modified By `System` untuk `{idTimeout}`
32. Ganti isi kotak search dengan `{idActivate}`, tekan Enter
33. Verifikasi Changelog memuat entri Modified By `System` untuk `{idActivate}`
34. Ganti isi kotak search dengan `{idExpire}`, tekan Enter
35. Verifikasi Changelog memuat entri Modified By `System` untuk `{idExpire}`
36. Tutup modal Changelog
37. Buka Activity Log Admin Console
38. Ketik Search `{idTimeout}`, tekan Enter
39. Verifikasi Activity Log memuat entri Modified By `System` untuk `{idTimeout}`
40. Ganti isi kotak search dengan `{idActivate}`, tekan Enter
41. Verifikasi Activity Log memuat entri Modified By `System` untuk `{idActivate}`
42. Ganti isi kotak search dengan `{idExpire}`, tekan Enter
43. Verifikasi Activity Log memuat entri Modified By `System` untuk `{idExpire}`

### Notifikasi Timeout Auto-Cancel (TC-AC-LA-437)

44. Ganti akun: Logout dari Hendra Wijaya
45. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
46. Buka daftar notifikasi in-app
47. Verifikasi notifikasi approver aktif dengan Title `License allocation canceled automatically` dan Body `{idTimeout} · Concurrent User · PT Sejahtera`
48. Verifikasi jumlah notifikasi berjudul `License allocation canceled automatically` pada akun Fajar Nugroho bertambah satu terhadap `{nNotifFajar}`
49. Ganti akun: Logout dari Fajar Nugroho
50. Login sebagai Dewi Anggraini (`dewiFullLic`, password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`)
51. Buka daftar notifikasi in-app
52. Verifikasi notifikasi requester dengan Title `License allocation canceled automatically` dan Body `Your request has expired after 3 days without a decision and has been automatically canceled. Please resubmit if still needed.`
53. Verifikasi jumlah notifikasi berjudul `License allocation canceled automatically` pada akun Dewi Anggraini bertambah satu terhadap `{nNotifDewi}`

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (job sistem dan pergeseran jam) dan satu topik (jejak log dan notifikasi dari job), berdiri sendiri pada tiga record seed. Satu pergeseran jam dan satu siklus job melayani ketiga record; blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung pada ambang smell.
- Penggabungan: TC-AC-LA-408 dan TC-AC-LA-526 memakai record `{idExpire}` yang sama; judul entri `Allocation expired` tanpa `by [PIC]` (langkah 8) memenuhi Expected kedua TC, dan Modified By `System` pada langkah 35 dan 43 memenuhi TC-AC-LA-526 butir b. TC-AC-LA-412 dan TC-AC-LA-437 memakai record `{idTimeout}` yang sama, dan TC-AC-LA-525 memakai `{idActivate}`.
- Langkah penghubung (S-03, R-16): langkah 1 dan 3 (mengatur dan memulihkan jam), langkah 2 (menunggu siklus job lewat kueri fixture status job), langkah 6, 16, 23, 30, 32, 34, 38, 40, dan 42 (Search baris atau entri berdasarkan Allocation ID), langkah 4, 14, 21, dan 28 (pindah tab; langkah 28 kembali ke tab Current karena ikon `Changelog` pada List tidak dirender di tab History), langkah 5, 15, dan 22 (mengosongkan kotak search tab tujuan secara eksplisit: klik `✕` pada Search lalu Enter; spec tidak mengandalkan apakah kotak Search terbawa atau ter-reset sesudah pindah tab), langkah 13, 20, 27, dan 36 (menutup modal), langkah 44 sampai 46 dan langkah 49 sampai 51 (ganti akun dan membuka notifikasi).
- Pembagian TC lintas spec: log Timeout Auto-Cancel, Auto-Expire, dan Auto-Activate pada Changelog, Activity Log, dan System Log serta Allocation Log `Allocation auto-canceled` dan `Allocation activated` (TC-AC-LA-395, 396, 398, 406, 407) ada di spec 126.
- Temuan untuk QA:
  - TC-AC-LA-408, 412, 525, dan 526 ber-Precondition "Tidak ada aktor login" dan tidak menyebut cara menemukan entri di Changelog dan Activity Log; spec memakai Hendra Wijaya (Pre-setup #1, sesuai TC-AC-LA-408) dan Search dengan Allocation ID.
  - TC-AC-LA-437 menyebut "Buka notifikasi requester dan approver" tanpa menyebut akun requester; ACC TC hanya #41, #40, dan #10. Spec memakai Dewi Anggraini (Pre-setup #4) sebagai requester sesuai definisi seed ("requester `Dewi A`").
  - Body notifikasi requester TC-AC-LA-437 tidak memuat Allocation ID sehingga tidak dapat dikaitkan ke record; spec memakai pertambahan jumlah notifikasi berjudul sama terhadap baseline.
  - TC-AC-LA-412, 525, dan 526 menyebut "Allocation Log ... menambah entri"; spec mengasersi pertambahan satu entri terhadap baseline yang dicatat di hook `before`.
  - Job juga memproses alokasi Pre-setup lain yang memenuhi syarat; pemulihannya bergantung baseline automation.
