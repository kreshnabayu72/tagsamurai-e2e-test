---
id: TC-AC-CS-E2E-151-job-flip-dilewati-dan-race-cancel-request
title: "Job: Flip Dilewati dan Race Cancel Request"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-290
  - TC-AC-CS-291
  - TC-AC-CS-546
coverage:
  web: automated
---

# Job: Flip Dilewati dan Race Cancel Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Ganti akun di tengah spec: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9, `Spectra.env.AC_SUB_DIST_TC_PASSWORD`), lalu Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data milik spec, dibuat lewat API (sesi API aktor requester) dan fixture backend yang disediakan tim FE/BE di hook `before`, dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-151`; Subscription ID dibangkitkan sistem dan dibaca saat seeding, ditulis di langkah sebagai `[Subscription ID ... seed]`):
  1. TC-AC-CS-290: Client `Toko Harapan Baru+{runId}-151` (setara #109) dengan predecessor SAMS plan Enterprise berstatus Archive (01/01/24 / 31/12/24, Plan Owner PT Maju Bersama (Distributor)) dan successor SAMS plan Enterprise berstatus Pending (01/01/25 / 31/12/25) ber-Reserve wallet dan Reserve alokasi, predecessor sudah Archive saat tick.
  2. TC-AC-CS-291: term FAMS plan Professional berstatus Pending (15/09/26 / 14/09/27, Plan Owner PT Maju Bersama (Distributor)) untuk Client `Percetakan Mega+{runId}-151` (setara #57), milik requester `Dewi A`, dengan Reserve $10,000.00.
  3. TC-AC-CS-546: term SIEM plan SIEM berstatus Pending (15/09/26 / 14/09/27, Plan Owner PT Maju Bersama (Distributor)) untuk Client `Apotek Sehat Sentosa+{runId}-151` (setara #90), milik Fajar Nugroho.
  General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state data milik spec yang diubah (term seed kembali ke baseline) dilakukan fixture backend yang disediakan tim FE/BE sebagai langkah penghubung antar blok TC; state global yang dipulihkan hanya jam server dan jam browser (S-06).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- Kemampuan teknis (disediakan tim FE/BE): picu job flip dengan predecessor yang sudah Archive (TC-AC-CS-290), kemampuan baca notifikasi per user untuk requester dan approver successor (TC-AC-CS-290 butir e), kemampuan baca saldo Wallet, dan pemicu scheduled flip yang aktif sebelum `[Cancel Request]` diklik (TC-AC-CS-546).
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after` dan antar blok); term seed yang berubah dipulihkan fixture backend antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-290: Flip dilewati bila predecessor sudah Archive: successor dibatalkan sistem

1. Atur jam server dan jam browser ke Start Date successor `01/01/25`, picu job flip, dan poll hingga job selesai
2. Muat ulang halaman, klik tab "History", ketik Search `Toko Harapan Baru+{runId}-151`, tekan Enter
3. Verifikasi status predecessor `[Subscription ID predecessor seed]` tidak berubah (tetap Archive) karena flip dilewati
4. Verifikasi successor `[Subscription ID successor seed]` berstatus Canceled
5. Verifikasi Reserve wallet term dan Reserve tiap alokasi successor dilepas penuh
6. Pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `Toko Harapan Baru+{runId}-151`, tekan Enter
7. Verifikasi entri baru Changelog mencatat Action `Scheduled Flip Auto-Cancel`, Field `Status`, Old `Pending`, New `Canceled`, Modified By `System`
8. Tutup modal Changelog dengan `✕`, klik ikon `⋯` pada baris successor
9. Verifikasi menu row action successor hanya berisi Detail dan Subscription Log (Resubmit tidak tersedia)
10. Verifikasi tidak ada notifikasi baru ke requester maupun approver successor (jumlah notifikasi sama dengan baseline)
11. Tutup menu, lalu pulihkan baseline term lewat fixture backend

### TC-AC-CS-291: Job flip melewati record yang sudah dibatalkan sebelum tick

12. Logout, lalu login sebagai Total Control Distributor Eko Saputra
13. Buka menu `Allocation > Client Subscription`
14. Ketik Search `[Subscription ID term 291 seed]`, tekan Enter, lalu klik ikon `⋯` pada baris itu dan pilih `Cancel Request`
15. Klik `[Cancel Request]`
16. Verifikasi dialog Cancel Request tertutup (respons selesai diproses)
17. Catat jumlah entri Changelog record dan saldo Wallet sebagai baseline
18. Atur jam server dan jam browser ke `15/09/26`, picu job flip, dan poll hingga job selesai
19. Muat ulang halaman, klik tab "History", ketik Search `[Subscription ID term 291 seed]`, tekan Enter
20. Verifikasi term tetap berstatus Canceled dan tidak diproses job
21. Pulihkan jam server dan jam browser ke jam normal
22. Buka modal Changelog, ketik Search `[Subscription ID term 291 seed]`, tekan Enter
23. Verifikasi jumlah entri Changelog record sama dengan baseline (tidak ada entri log tambahan)
24. Verifikasi tidak ada Capture pada saldo Wallet dibandingkan baseline
25. Pulihkan baseline term lewat fixture backend

### TC-AC-CS-546: Cancel Request ditolak saat term Pending sudah menjadi Active

26. Logout, lalu login sebagai Create-Only Distributor Fajar Nugroho
27. Buka menu `Allocation > Client Subscription`
28. Ketik Search `[Subscription ID term 546 seed]`, tekan Enter, lalu klik ikon `⋯` pada baris itu dan pilih `Cancel Request`
29. Atur jam server dan jam browser melewati Start Date `15/09/26`, picu scheduled flip, dan poll hingga term berstatus Active, lalu klik `[Cancel Request]`
30. Verifikasi dialog blok Title "Cannot Cancel Request" dengan Body "• Apotek Sehat Sentosa+{runId}-151 — SIEM" dan "This request has already been activated."
31. Verifikasi dialog hanya memiliki tombol tunggal `[OK]`
32. Klik `[OK]`, muat ulang List, ketik Search `[Subscription ID term 546 seed]`, tekan Enter
33. Verifikasi term tetap Active
34. Pulihkan jam server dan baseline term lewat fixture backend

## Notes

- Langkah penghubung: tab, Search (R-16: untuk menemukan baris target), muat ulang, penutupan modal dan menu, ganti akun (diikuti membuka Allocation > Client Subscription), serta pemulihan jam dan baseline lewat fixture antar blok.
- Urutan TC: TC-AC-CS-290 (akun default) lalu TC-AC-CS-291 (Eko Saputra) lalu TC-AC-CS-546 (Fajar Nugroho) agar ganti akun seminimal mungkin; ketiganya memakai term berbeda.
- P-1: TC-AC-CS-291 butir b ("tanpa entri log tambahan dan tanpa Capture") ditulis sebagai asersi jumlah terhadap baseline (bukan kelas g) di spec ini.
- Temuan untuk QA: (1) TC-AC-CS-290 butir e ("Tidak ada notifikasi ke requester maupun approver") tidak menyebut identitas requester dan approver successor; spec memakai kemampuan baca notifikasi per user (disediakan tim FE/BE). (2) TC-AC-CS-290 Post Condition a dan b (entri Canceled `System` di Approvals Tab History; Reserve dilepas di Wallet) tidak punya langkah observasi di TC selain Expected b; Post Condition a tidak diasersi. (3) TC-AC-CS-291 precondition aktor `Eko Saputra` tetapi term milik requester `Dewi A`; spec memakai Cancel Request oleh Eko sesuai TC. (4) TC-AC-CS-546 langkah 2 memakai dialog Cancel Request yang dibuka sebelum flip; spec membuka dialog lebih dulu lalu memicu flip, lalu klik `[Cancel Request]`.
