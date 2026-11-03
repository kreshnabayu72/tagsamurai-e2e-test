---
id: TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal
title: "Approvals: Approve dan Reject Renewal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-301
  - TC-AC-CS-302
  - TC-AC-CS-551
  - TC-AC-CS-21
coverage:
  web: automated
---

# Approvals: Approve dan Reject Renewal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-081`, Plan Owner PT Maju Bersama (Distributor); dibuat di hook `before`, dihapus di hook `after`): pengajuan Renewal `{idRenew}` (Client `Toko Serba Ada+{runId}-081`, FAMS, plan Enterprise, Waiting for Approval, #67) atas predecessor `{idPred}` (plan Professional, Active, 01/09/25 / 31/08/26, #68) dengan Reserve wallet, dipakai pada TC-AC-CS-301, TC-AC-CS-302, dan TC-AC-CS-21; term FAMS Professional milik Client `Toko Cahaya Abadi+{runId}-081` `{idEdit}` yang kembali Waiting for Approval setelah Edit dengan dua alokasi lisensi Pending (Concurrent User 10 dan Maintenance 5) serta Reserve term dan Reserve tiap alokasi (#110) untuk TC-AC-CS-551 (dependensi TC-AC-CS-550 dibangun lewat seeding). Subscription ID `{idRenew}`, `{idPred}`, dan `{idEdit}` dibaca lewat API seeding setiap data dibuat atau di-seed ulang dan dirujuk di langkah sebagai nilai terbaca (S-12). Pengajuan dibuat oleh requester lewat sesi API (Create-Only Distributor Fajar Nugroho, Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`) hingga pengajuan tersimpan di hook `before`; approver login UI.
- Toggle `Require Approval for Allocation` untuk PT Maju Bersama ON (#23) dan Toggle `Require Approval for Trial Activation` (#24) diatur fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan): saldo kantong Wallet (Reserve dan Capture), notifikasi per user untuk requester, dan Activation Email serta App Access per alamat.
- Jam: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- State global yang diubah: keputusan Approve atau Reject mengubah state pengajuan dan predecessor; pengajuan di-seed ulang antar blok oleh fixture backend. Jam server dan jam browser diatur ke tanggal acuan `19/08/26` (dipulihkan di hook `after`).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-301: Approve Renewal atas predecessor Active menghasilkan Pending tanpa mengubah predecessor

1. Buka Approvals > Client Subscription, klik `[Review]` pada pengajuan `{idRenew}`, pilih Approve, lalu klik Submit
2. Tunggu aksi selesai (dialog/modal tertutup)
3. Buka Allocation > Client Subscription tab "Current", ketik Search `Toko Serba Ada+{runId}-081`, tekan Enter
4. Verifikasi successor berstatus Pending dengan Start Date `01/09/26`
5. Verifikasi predecessor `{idPred}` tetap Active sampai scheduled flip
6. Buka modal Subscription Log successor
7. Verifikasi Subscription Log memuat entri `Subscription approved by Eko Saputra`
8. Tutup modal, buka modal Changelog, ketik Search `{idRenew}`, tekan Enter
9. Verifikasi sedikitnya satu entri lain milik successor tampil di Changelog
10. Verifikasi Changelog tidak memuat Action `Approve`
11. Tutup modal Changelog dengan `✕`, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-302: Reject pengajuan: Rejected permanen, Reserve dilepas, predecessor tidak disentuh

12. Buka Approvals > Client Subscription, pilih radio Reject pada pengajuan `{idRenew}`, isi `Rejection Reason` dengan `Budget pengajuan belum disetujui`, klik `[Submit Decision]`, lalu konfirmasi pada dialog Konfirmasi Reject
13. Tunggu aksi selesai (dialog/modal tertutup)
14. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Toko Serba Ada+{runId}-081`, tekan Enter
15. Verifikasi term berstatus Rejected tampil di tab "History" dan permanen sebagai jejak audit
16. Verifikasi Reserve wallet dilepas
17. Buka modal Subscription Log term itu
18. Verifikasi Subscription Log memuat entri `Subscription rejected by Eko Saputra` dengan `Rejection Reason: Budget pengajuan belum disetujui`
19. Tutup modal, buka modal Changelog, ketik Search `{idRenew}`, tekan Enter
20. Verifikasi sedikitnya satu entri lain milik term tampil di Changelog
21. Verifikasi Changelog tidak memuat Action `Reject`
22. Verifikasi requester menerima notifikasi "Subscription rejected"
23. Klik tab "Current", ganti isi kotak search dengan `Toko Serba Ada+{runId}-081`, tekan Enter
24. Verifikasi predecessor `{idPred}` tidak disentuh: tetap di tab "Current" dengan status Active
25. Klik ikon `⋯` pada baris predecessor
26. Verifikasi row action Renew pada predecessor tersedia sehingga pengajuan Add atau Renew berikutnya tidak terhalang baris Rejected
27. Tutup menu dan modal Changelog, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-551: Reject term yang pernah Pending melepas Reserve term dan Reserve tiap alokasi

28. Buka Approvals > Client Subscription, pilih radio Reject pada pengajuan `{idEdit}`, isi `Rejection Reason` dengan `Perubahan term belum disetujui`, klik `[Submit Decision]`, lalu konfirmasi pada dialog Konfirmasi Reject
29. Tunggu aksi selesai (dialog/modal tertutup)
30. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Toko Cahaya Abadi+{runId}-081`, tekan Enter
31. Verifikasi term berstatus Rejected tampil di tab "History"
32. Klik baris term untuk membuka Detail term, lalu buka License Quota dan Wallet
33. Verifikasi Reserve wallet term dan Reserve tiap alokasi dilepas penuh
34. Verifikasi Balance tidak pernah berkurang
35. Seed ulang pengajuan lewat fixture backend

### TC-AC-CS-21: Successor Renew Rejected atau Canceled pindah ke History sementara predecessor tetap di Current

36. Buka Approvals > Client Subscription, pilih radio Reject pada successor `{idRenew}`, isi `Rejection Reason` dengan `Renewal belum disetujui`, klik `[Submit Decision]`, lalu konfirmasi pada dialog Konfirmasi Reject
37. Tunggu aksi selesai (dialog/modal tertutup)
38. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Toko Serba Ada+{runId}-081`, tekan Enter
39. Verifikasi successor berstatus Rejected tampil di tab "History"
40. Klik tab "Current", ganti isi kotak search dengan `Toko Serba Ada+{runId}-081`, tekan Enter
41. Verifikasi predecessor `{idPred}` tetap di tab "Current" dengan status Active
42. Klik ikon `⋯` pada baris predecessor
43. Verifikasi row action Renew pada predecessor tersedia kembali
44. Tutup menu, lalu pulihkan baseline pengajuan lewat fixture backend

## Notes

- Langkah penghubung: navigasi menu, tab, Search (R-16: untuk menemukan baris target), penutupan modal dan menu, serta seed ulang pengajuan lewat fixture antar blok, serta `Tunggu aksi selesai` setelah tiap keputusan Approve atau Reject (8b.8). Pengecekan predecessor pada TC-AC-CS-302 dilakukan di tab "Current" (tempat predecessor Active), bukan di tab "History".
- P-1: asersi "modal Changelog tidak memuat Action `Approve`" (atau `Reject`) tetap di spec ini karena bergantung pada state berat (pengajuan ber-Reserve wallet yang diputuskan sekali dan tidak dapat diulang tanpa biaya besar); tiap asersi didahului Verifikasi entri lain milik term pada Changelog yang sama sebagai anchor positif dan memakai baseline jumlah entri (S-12). Approve dan Reject dicatat di Subscription Log, Activity Log, dan System Log approver (ACCS-LOGIC-06a).
- Alasan spec 44 langkah, di atas smell 35 langkah: keempat TC memakai akun approver yang sama, halaman Approvals yang sama, dan alur keputusan atas pengajuan Renewal yang di-seed spec sendiri; tiap blok berdiri sendiri dengan seed ulang dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan menambah hook, login, dan seeding tanpa menambah isolasi.
- Temuan untuk QA: (1) TC-AC-CS-302 butir e ("Pengajuan Add atau Renew berikutnya tidak terhalang baris Rejected ini") tidak punya langkah observasi di TC; spec memverifikasi row action Renew predecessor tersedia (kesimpulan dari TC-AC-CS-21 butir c) dan mencatat bahwa pengajuan Add berikutnya tidak diuji. (2) TC-AC-CS-551 butir c ("Predecessor (bila ada) tidak disentuh") bersyarat dan precondition tidak menyebut predecessor; tidak diasersi. (3) TC-AC-CS-551 bergantung pada TC-AC-CS-550 (Edit) dan menyebut kembalinya term ke Waiting for Approval; spec men-seed state itu (S-06). (4) TC-AC-CS-301 dan TC-AC-CS-302 tidak menyebut tempat pengamatan notifikasi requester; spec memakai kemampuan baca notifikasi (disediakan tim FE/BE). (5) TC-AC-CS-302 Post Condition tidak punya langkah observasi dan tidak diasersi.
