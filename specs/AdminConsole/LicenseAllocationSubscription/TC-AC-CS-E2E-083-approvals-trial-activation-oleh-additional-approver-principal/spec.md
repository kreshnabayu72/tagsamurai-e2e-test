---
id: TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal
title: "Approvals: Trial Activation oleh Additional Approver Principal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-303
  - TC-AC-CS-304
  - TC-AC-CS-557
  - TC-AC-CS-553
coverage:
  web: automated
---

# Approvals: Trial Activation oleh Additional Approver Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Maya Tanjung, Additional Approver Manage allocation Principal PT ABC (Pre-setup #4), password `Spectra.env.AC_SUB_APPROVER_PASSWORD` (akun pertama, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite). Ganti akun di tengah spec: Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`), lalu Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1, `Spectra.env.AC_SUB_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-083`, requester Distributor PT Maju Bersama; dibuat lewat sesi API di hook `before`, dihapus di hook `after`, dan di-seed ulang antar blok oleh fixture backend; Subscription ID dibaca lewat API seeding dan dirujuk di langkah sebagai nilai terbaca, S-12): Client `PT Bintang Timur+{runId}-083` (padanan #59) dengan pengajuan Trial `{idTrial}` (FAMS, plan Growth, badge Trial, Waiting for Approval, Duration 30, Asset 50, Concurrent User 10) untuk TC-AC-CS-303; Client `Client Tanpa Subscription A+{runId}-083` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial, padanan #48) dengan pengajuan Trial Growth Waiting for Approval untuk TC-AC-CS-304; Client `Klinik Gigi Ceria+{runId}-083` (binaan langsung PT Maju Bersama) belum pernah punya term Active (padanan #32) untuk TC-AC-CS-557; Client `Client Tanpa Subscription B+{runId}-083` belum pernah punya term Active (padanan #48) untuk TC-AC-CS-553. Pengajuan dibuat oleh requester lewat sesi API (Create-Only Distributor Fajar Nugroho, Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`) hingga pengajuan tersimpan; approver login UI.
- Toggle `Require Approval for Trial Activation` (#24): ON pada TC-AC-CS-303, TC-AC-CS-304, dan TC-AC-CS-557; OFF pada TC-AC-CS-553; diatur fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan): saldo kantong Wallet (Reserve dan Capture), notifikasi per user untuk requester, dan Activation Email serta App Access per alamat.
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- State global yang diubah: Toggle `Require Approval for Trial Activation`; trial yang aktif dan pengajuan dibersihkan fixture backend antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-303: Approve Trial Activation oleh approver Principal mengaktifkan trial

1. Buka Approvals > Client Subscription, klik `[Review]` pada pengajuan Trial `{idTrial}`, pilih Approve, lalu klik Submit
2. Tunggu aksi selesai (dialog/modal tertutup)
3. Buka Allocation > Client Subscription tab "Current", ketik Search `PT Bintang Timur+{runId}-083`, tekan Enter
4. Verifikasi Trial berstatus Active dengan Start Date waktu disetujui dan End Date Start Date + 30 hari - 1
5. Verifikasi saldo kuota lisensi diinisialisasi (Asset 50, Concurrent User 10)
6. Buka modal Subscription Log baris Trial
7. Verifikasi Subscription Log memuat entri `Subscription approved by Maya T`
8. Tutup modal, buka modal Changelog, ketik Search `{idTrial}`, tekan Enter
9. Verifikasi sedikitnya satu entri lain milik Trial tampil di Changelog
10. Verifikasi Changelog tidak memuat Action `Approve`
11. Verifikasi approver adalah Additional Approver Principal, bukan approver entitas Distributor
12. Tutup modal Changelog dengan `✕`, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-304: Reject Trial tidak menghitung terhadap eligibilitas satu kali per plan

13. Buka Approvals > Client Subscription, pilih radio Reject pada pengajuan Trial, isi `Rejection Reason` dengan `Kuota trial belum disepakati`, klik `[Submit Decision]`, lalu konfirmasi pada dialog Konfirmasi Reject
14. Tunggu aksi selesai (dialog/modal tertutup)
15. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Client Tanpa Subscription A+{runId}-083`, tekan Enter
16. Verifikasi Trial berstatus Rejected di tab "History"
17. Klik `[+ Activate Trial]`, pilih Client `Client Tanpa Subscription A+{runId}-083`, pilih Product `FAMS`, lalu buka dropdown Plan
18. Verifikasi Plan `Growth` tetap tampil di dropdown Plan dan dapat diajukan ulang
19. Verifikasi tidak ada kuota yang diinisialisasi
20. Tutup modal Activate Trial dengan `✕`, verifikasi dialog `Unsaved Changes` tampil, klik `[Leave]`, lalu bersihkan baseline lewat fixture backend

### TC-AC-CS-557: Activation Email dan App Access terkirim sekali setelah Approve Activate Trial pada term pertama Client

21. Logout, lalu login sebagai Create-Only Distributor Fajar Nugroho
22. Buka menu Allocation > Client Subscription
23. Klik `[+ Activate Trial]`, pilih Client `Klinik Gigi Ceria+{runId}-083`, Product `SAMS`, Plan `Growth`
24. Isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`, lalu klik `[Submit]`
25. Tunggu aksi selesai (dialog/modal tertutup)
26. Verifikasi tidak ada Activation Email dan App Access terkirim selama Waiting for Approval
27. Logout, lalu login sebagai Additional Approver Maya Tanjung
28. Buka Approvals > Client Subscription, pilih pengajuan Trial `Klinik Gigi Ceria+{runId}-083`, pilih Approve, lalu klik Submit
29. Tunggu aksi selesai (dialog/modal tertutup)
30. Verifikasi Activation Email dan App Access terkirim satu kali karena ini term pertama Client yang menjadi Active
31. Logout, lalu login sebagai Total Control Principal Hendra Wijaya
32. Buka menu Allocation > Client Subscription
33. Klik `[+ Activate Trial]`, pilih Client `Klinik Gigi Ceria+{runId}-083`, Product `SIEM`, Plan `SIEM`
34. Isi Trial Duration `30`, Trial Log Source Quota `10`, Trial Concurrent User Quota `10`, lalu klik `[Submit]`
35. Tunggu aksi selesai (dialog/modal tertutup)
36. Verifikasi trial SIEM Active dan tidak ada Activation Email maupun App Access kedua
37. Bersihkan baseline trial lewat fixture backend

### TC-AC-CS-553: Activation Email dan App Access terkirim sekali pada term pertama Client yang menjadi Active lewat Activate Trial langsung

38. Atur Toggle `Require Approval for Trial Activation` menjadi OFF lewat fixture backend, lalu klik `[+ Activate Trial]`, pilih Client `Client Tanpa Subscription B+{runId}-083`, Product `FAMS`, Plan `Growth`
39. Isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`, lalu klik `[Submit]`
40. Tunggu aksi selesai (dialog/modal tertutup)
41. Verifikasi trial Active dan Activation Email serta App Access terkirim satu kali karena ini term pertama Client yang menjadi Active
42. Klik `[+ Activate Trial]` lagi, pilih Client `Client Tanpa Subscription B+{runId}-083`, Product `SAMS`, Plan `Growth`
43. Isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`, lalu klik `[Submit]`
44. Tunggu aksi selesai (dialog/modal tertutup)
45. Verifikasi trial SAMS Active dan tidak ada Activation Email maupun App Access kedua
46. Pulihkan Toggle `Require Approval for Trial Activation` dan baseline lewat fixture backend

## Notes

- Langkah penghubung: navigasi menu, tab, Search (R-16: untuk menemukan baris target), penutupan modal, ganti akun (dengan `Buka menu Allocation > Client Subscription` sesudah login sebelum aksi List), `Tunggu aksi selesai` setelah tiap Submit atau keputusan (8b.8), dan pemulihan fixture antar blok.
- Urutan TC: TC-AC-CS-303 dan TC-AC-CS-304 (akun Additional Approver) lalu TC-AC-CS-557 (Distributor, Additional Approver, Total Control Principal) lalu TC-AC-CS-553 (Total Control Principal) agar ganti akun seminimal mungkin.
- P-1: asersi "modal Changelog tidak memuat Action `Approve`" (atau `Reject`) tetap di spec ini karena bergantung pada state berat (pengajuan ber-Reserve wallet yang diputuskan sekali dan tidak dapat diulang tanpa biaya besar); tiap asersi didahului Verifikasi entri lain milik term pada Changelog yang sama sebagai anchor positif dan memakai baseline jumlah entri (S-12). Approve dan Reject dicatat di Subscription Log, Activity Log, dan System Log approver (ACCS-LOGIC-06a).
- Alasan spec 46 langkah, di atas smell 35 langkah: keempat TC memakai halaman Approvals dan Activate Trial yang sama dengan seed sendiri dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan menambah hook, login, dan seeding tanpa menambah isolasi.
- Temuan untuk QA: (1) TC-AC-CS-304 tidak menyebut keadaan Toggle Trial; spec memakai ON sebagai precondition pengajuan. (2) TC-AC-CS-553 dan TC-AC-CS-557 membutuhkan kemampuan baca email per alamat yang tidak disebut TC (R-11); disediakan tim FE/BE. (3) TC-AC-CS-557 langkah 4 memakai Role Total Control (Principal) sementara aktor TC adalah Create-Only Distributor; ganti akun ditulis eksplisit. (4) TC-AC-CS-303 butir d ("Approver adalah Total Control atau Additional Approver Principal") bersifat penjelasan peran; spec memverifikasi approver Maya Tanjung sebagai Additional Approver Principal. (5) TC-AC-CS-304 butir c ("Tidak ada kuota yang diinisialisasi") tidak punya cara cek di TC; spec memakai kemampuan baca state BE.
