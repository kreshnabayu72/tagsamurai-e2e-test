---
id: TC-AC-CS-E2E-076-job-scheduled-flip
title: "Job: Scheduled Flip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-287
  - TC-AC-CS-535
  - TC-AC-CS-288
coverage:
  web: automated
---

# Job: Scheduled Flip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup: term mode New Pending `SUBS-20260819-00002` (Client Percetakan Mega, FAMS, plan Professional, status Pending, tanggal 15/09/26 / 14/09/27, Plan Owner PT Maju Bersama (Distributor), #57) dengan Reserve $10,000.00, Client belum punya term Active lain, plan dibuat pada versi 3 dan versi 4 dipublikasikan sebelum flip (precondition TC-AC-CS-535, dipakai sebagai precondition, tidak diasersi); predecessor `SUBS-20250820-00001` (Client Toko Harapan Baru, FAMS, plan Growth, Active, 01/09/25 / 31/08/26, Plan Owner PT Maju Bersama (Distributor)) dan successor Pending `SUBS-20260810-00002` (plan Professional, Pending, 01/09/26 / 31/08/27) hasil Renew Change plan yang sudah di-Approve (#108). General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca saldo kantong Wallet (Reserve dan Capture), kemampuan baca Activation Email dan App Access per alamat, dan penyetelan versi plan; keduanya tidak memakai endpoint karangan (S-13).
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after` dan sebelum membuka log), serta state term Pre-setup yang berubah menjadi Active (dipulihkan fixture backend antar blok; efek: Last Updated dan entri audit trail permanen).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-287: Scheduled flip term mode New dari Pending ke Active pada Start Date

1. Atur jam server dan jam browser ke `14/09/26`, picu satu siklus job flip, dan poll hingga job selesai
2. Muat ulang List, ketik Search `SUBS-20260819-00002`, tekan Enter
3. Verifikasi term `SUBS-20260819-00002` masih berstatus Pending pada `14/09/26`
4. Verifikasi Reserve $10,000.00 masih ditahan pada `14/09/26`
5. Atur jam server dan jam browser ke `15/09/26`, picu satu siklus job flip, dan poll hingga term berstatus Active (kelas eventual)
6. Muat ulang List, ketik Search `SUBS-20260819-00002`, tekan Enter
7. Verifikasi term berstatus Active pada `15/09/26`
8. Verifikasi Reserve di-Capture
9. Pulihkan jam server dan jam browser ke jam normal
10. Buka modal Changelog, ketik Search `SUBS-20260819-00002`, tekan Enter
11. Verifikasi entri baru Changelog mencatat Action `Activate (efek terjadwal, diterapkan)`, Field `Status`, Old `Pending`, New `Active`, Modified By `System`
12. Tutup modal Changelog dengan `✕`, buka Activity Log, ketik Search `SUBS-20260819-00002`, tekan Enter
13. Verifikasi Activity Log mencatat entri yang sama dengan Modified By `System`
14. Buka System Log, ketik Search `SUBS-20260819-00002`, tekan Enter
15. Verifikasi sedikitnya satu entri lain tampil di System Log
16. Verifikasi System Log tidak memuat entri baru untuk aksi ini (jumlah entri sama dengan baseline)
17. Verifikasi Activation Email dan App Access terkirim sekali karena ini term pertama Client yang menjadi Active
18. Pulihkan baseline term lewat fixture backend

### TC-AC-CS-535: Scheduled flip memakai versi plan yang dikunci saat pengajuan

19. Atur jam server dan jam browser ke `15/09/26`, picu satu siklus job flip, dan poll hingga term berstatus Active
20. Muat ulang List, ketik Search `SUBS-20260819-00002`, tekan Enter, lalu klik baris untuk membuka Subscription Detail
21. Verifikasi term Active memakai plan `Professional` versi 3 yang dikunci saat pengajuan
22. Verifikasi versi plan tidak diambil ulang dari versi terbaru (versi 4)
23. Pulihkan jam server dan baseline term lewat fixture backend

### TC-AC-CS-288: Scheduled flip Renewal: successor Active dan predecessor Renewed dalam satu transaksi

24. Atur jam server dan jam browser ke `01/09/26` (Start Date successor), picu satu siklus job flip, dan poll hingga job selesai (kelas eventual)
25. Muat ulang tab "Current", ketik Search `Toko Harapan Baru`, tekan Enter
26. Verifikasi successor berstatus Active
27. Muat ulang halaman, klik tab "History", ketik Search `Toko Harapan Baru`, tekan Enter
28. Verifikasi predecessor berstatus Renewed dan pindah ke tab "History"
29. Pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `Toko Harapan Baru`, tekan Enter
30. Verifikasi entri baru Changelog mencatat Action `Renew (efek terjadwal, diterapkan)`, Field `Plan/End Date`, Old `Growth/31/08/26`, New `Professional/31/08/27`, Modified By `System`
31. Verifikasi Capture Reserve dilakukan pada saat flip
32. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline term lewat fixture backend

## Notes

- Langkah penghubung: Search (R-16: untuk menemukan baris target), muat ulang, penutupan modal Changelog, pemulihan jam dan baseline lewat fixture antar blok.
- Anchor positif: Verifikasi "sedikitnya satu entri lain tampil di System Log" mendahului asersi absence pada TC-AC-CS-287 butir d (8b.2).
- P-1: asersi "System Log tidak memuat entri" pada TC-AC-CS-287 butir d tetap di spec ini karena bergantung pada state berat (job flip sistem pada term Pending ber-Reserve dengan jam server digeser); asersi didahului Verifikasi entri Activity Log yang sama (anchor positif) dan memakai baseline jumlah entri System Log (S-12).
- Urutan TC: TC-AC-CS-287 dan TC-AC-CS-535 memakai term Pending yang sama dan dipulihkan antar blok; TC-AC-CS-288 memakai pasangan Renewal dan berada terakhir.
- Temuan untuk QA: (1) TC-AC-CS-287 Post Condition a, b, dan c (term tampil di tab Current, Wallet Capture, gate Asset Control terbuka) tidak punya langkah observasi di TC selain Expected a dan b; Post Condition c tidak diasersi. (2) TC-AC-CS-287 butir e menyebut Activation Email dan App Access terkirim bila ini term pertama Client; precondition menyatakan Client belum punya term Active lain sehingga spec menganggap kondisi itu terpenuhi. (3) TC-AC-CS-535 tidak menyebut tempat versi plan teramati; spec menulis pengamatan di Subscription Detail. (4) TC-AC-CS-288 Expected c ("Capture Reserve dilakukan pada saat flip") tidak menyebut cara cek; spec memakai kemampuan baca saldo Wallet. (5) Jam server absolut `14/09/26`, `15/09/26`, `01/09/26` tidak menyebut jam dalam hari; spec memakai awal hari sesuai nilai TC.
