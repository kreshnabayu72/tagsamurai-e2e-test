---
id: TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire
title: "Job: Flip Lanjutan dan Race Auto-Expire"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-20
  - TC-AC-CS-289
  - TC-AC-CS-481
  - TC-AC-CS-254
coverage:
  web: automated
---

# Job: Flip Lanjutan dan Race Auto-Expire

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup: predecessor `SUBS-20250820-00001` (Client Toko Harapan Baru, FAMS, plan Growth, Active, 01/09/25 / 31/08/26, Plan Owner PT Maju Bersama (Distributor)) dan successor Pending `SUBS-20260810-00002` (plan Professional, Pending, 01/09/26 / 31/08/27) hasil Renew Change plan yang sudah di-Approve (#108); term Pending `SUBS-20260819-00002` (Client Percetakan Mega, FAMS, plan Professional, Pending, 15/09/26 / 14/09/27, Plan Owner PT Maju Bersama (Distributor), #57) dengan Client `Percetakan Mega` (#35) belum punya term Active lain; Trial `Klinik Harapan Bunda` SAMS Growth Active (Start 10/08/26, End 08/09/26), Plan Owner CV Karya Mandiri, tanpa term paid SAMS (#71). General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- Kemampuan teknis (disediakan tim FE/BE): picu job flip dan job lifecycle Expired pada tick yang sama (TC-AC-CS-289), picu job auto-expire trial yang commit lebih dulu daripada Convert (TC-AC-CS-254), dan kemampuan baca state term paid, Reserve, serta Capture. TC-AC-CS-289 dan TC-AC-CS-254 berklasifikasi dua proses paralel; spec memicu kedua proses lewat kemampuan itu.
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after` dan antar blok); state term Pre-setup yang berubah dipulihkan fixture backend antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-20: Predecessor berpindah dari Current ke History saat successor Renew menjadi Active

1. Atur jam server dan jam browser ke `01/09/26` (Start Date successor), picu satu siklus job flip, dan poll hingga successor berstatus Active (kelas eventual)
2. Muat ulang tab "Current", ketik Search `Toko Harapan Baru`, tekan Enter
3. Verifikasi successor tampil di tab "Current" dengan status Active
4. Verifikasi predecessor tidak lagi tampil di tab "Current"
5. Klik tab "History"
6. Verifikasi predecessor berstatus Renewed tampil di tab "History"
7. Pulihkan jam server dan baseline term lewat fixture backend

### TC-AC-CS-289: Scheduled flip didahulukan atas job lifecycle Expired

8. Atur jam server dan jam browser ke `01/09/26`, picu job flip dan job lifecycle Expired pada tick yang sama, dan poll hingga kedua job selesai
9. Muat ulang tab "Current", ketik Search `Toko Harapan Baru`, tekan Enter
10. Verifikasi successor berstatus Active
11. Verifikasi tidak ada baris predecessor berstatus Expired di tab "Current"
12. Klik tab "History"
13. Verifikasi predecessor berstatus Renewed dan bukan Expired
14. Pulihkan jam server dan baseline term lewat fixture backend

### TC-AC-CS-481: Gate Asset Control mengikuti term Active setelah scheduled flip

15. Ketik Search `Percetakan Mega`, tekan Enter, lalu klik nama Client `Percetakan Mega` untuk membuka Client Detail tab "Asset Control"
16. Verifikasi gate Asset Control belum terbuka karena term Pending
17. Atur jam server dan jam browser ke `15/09/26`, picu satu siklus job flip, dan poll hingga term berstatus Active (kelas eventual)
18. Muat ulang Client Detail tab "Asset Control"
19. Verifikasi gate Asset Control terbuka karena term Active
20. Pulihkan jam server dan baseline term lewat fixture backend

### TC-AC-CS-254: Convert jalur instan kalah dari job auto-expire trial

21. Klik menu Allocation > Client Subscription di sidebar, ketik Search `Klinik Harapan Bunda`, tekan Enter
22. Klik ikon `⋯` pada baris trial, pilih `Convert`
23. Verifikasi modal Convert Trial terbuka
24. Isi Plan dan Duration dengan nilai valid (nilai tidak ditetapkan TC dan disediakan tim FE, lihat Temuan untuk QA)
25. Atur jam server dan jam browser ke `09/09/26`, picu job auto-expire trial, dan poll hingga job commit
26. Klik `[Submit]`, lalu klik `[Convert]`
27. Verifikasi dialog blok Title "Data has changed" dengan Body "• Klinik Harapan Bunda — SAMS" dan "This trial has already expired. Refresh the page and try again."
28. Verifikasi dialog hanya memiliki tombol tunggal `[OK]`
29. Klik `[OK]`, muat ulang List, ketik Search `Klinik Harapan Bunda`, tekan Enter
30. Verifikasi trial berstatus Expired
31. Verifikasi tidak ada term paid, tidak ada Reserve atau Capture, dan tidak ada record Convert untuk Client `Klinik Harapan Bunda`
32. Pulihkan jam server dan baseline trial lewat fixture backend

## Notes

- Langkah penghubung: Search (R-16: untuk menemukan baris target), muat ulang, pemulihan jam dan baseline lewat fixture antar blok.
- TC-AC-CS-289 dan TC-AC-CS-254 berklasifikasi dua proses paralel; yang diuji adalah hasil akhir setelah job commit lebih dulu. TC-AC-CS-254 memicu job auto-expire sebelum `[Convert]` diklik sehingga job commit lebih dulu seperti precondition TC.
- Temuan untuk QA: (1) TC-AC-CS-254 langkah 2 "Isi Plan dan Duration" tidak menyebut nilai; spec tidak mengarang nilai dan menandai nilai valid disediakan tim FE. (2) TC-AC-CS-254 butir b ("tidak ada term paid, tidak ada Reserve atau Capture, tidak ada record Convert") tidak menyebut cara cek; spec memakai kemampuan baca state BE. (3) TC-AC-CS-20 tidak menyebut Plan Owner row yang diasersi; spec memakai Search Client. (4) TC-AC-CS-481 tidak menyebut nama tab Client Detail; spec memakai nama dari TC.
