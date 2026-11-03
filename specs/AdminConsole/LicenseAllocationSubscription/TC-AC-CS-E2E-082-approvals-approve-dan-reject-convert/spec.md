---
id: TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert
title: "Approvals: Approve dan Reject Convert"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-306
  - TC-AC-CS-307
  - TC-AC-CS-308
  - TC-AC-CS-309
  - TC-AC-CS-300
coverage:
  web: automated
---

# Approvals: Approve dan Reject Convert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1). Ganti akun di tengah spec: Lestari Wulandari, Total Control Partner CV Karya Mandiri (Pre-setup #11, `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`) untuk TC-AC-CS-300.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-082`; dibuat lewat sesi API di hook `before`, dihapus di hook `after`, dan di-seed ulang antar blok oleh fixture backend; Subscription ID dibaca lewat API seeding setiap data dibuat atau di-seed ulang dan dirujuk di langkah sebagai nilai terbaca, S-12): pengajuan Convert jalur request mode New Plan `Professional`, Duration `1` milik Fajar Nugroho (requester biasa Create-Only Distributor, #6) atas trial Client `Klinik Harapan Bunda+{runId}-082` SAMS Growth Active (Start 10/08/26, End 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS, #71) dan Toggle Require Approval ON, dibuat dari dependensi TC-AC-CS-246 lewat seeding, untuk TC-AC-CS-306 dan TC-AC-CS-307; pengajuan Convert `{idConv}` disubmit `17/08/26` untuk trial `{idTrialExp}` yang End Date `18/08/26` terlewati sebelum approval `19/08/26` (#122) untuk TC-AC-CS-308; pengajuan Renewal `{idRenew}` (Client `Toko Serba Ada+{runId}-082`, padanan #67) atas predecessor `{idPred}` (padanan #68) yang dipindah job lifecycle ke Archive lewat fixture waktu sebelum Approve, requester `Fajar N`, untuk TC-AC-CS-309; Renewal atas predecessor `{idPredExp}` (Client `Bengkel Maju Jaya+{runId}-082`, SAMS, plan Growth, Expired, 19/08/25 / 18/08/26, Grace End 17/09/26, Plan Owner CV Karya Mandiri (Partner), padanan #50) disubmit `19/08/26` oleh Rina Pratama (Create-Only Partner, #12) dengan approval `20/08/26` untuk TC-AC-CS-300. Pengajuan dibuat oleh requester lewat sesi API (Create-Only Distributor Fajar Nugroho, Pre-setup #6, `Spectra.env.AC_SUB_CREATE_PASSWORD`) hingga pengajuan tersimpan di hook `before`; approver login UI. General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Toggle `Require Approval for Allocation` untuk PT Maju Bersama ON (#23) dan Toggle `Require Approval for Trial Activation` (#24) diatur fixture backend (disediakan tim FE/BE) dan dipulihkan di hook `after`.
- Kemampuan baca (disediakan tim FE/BE, tanpa endpoint karangan): saldo kantong Wallet (Reserve dan Capture), notifikasi per user untuk requester, dan Activation Email serta App Access per alamat.
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Kemampuan teknis tambahan (disediakan tim FE/BE): pemindahan predecessor ke Archive oleh job lifecycle lewat fixture waktu (TC-AC-CS-309, dua sesi paralel) sebagai pemicu state.
- State global yang diubah: jam server (blok TC-AC-CS-308, TC-AC-CS-309, dan TC-AC-CS-300), dipulihkan di hook `after` dan antar blok; keputusan mengubah state pengajuan (dibersihkan fixture backend).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-306: Approve Convert jalur request menulis dua record dan trial menjadi Converted

1. Buka Approvals > Client Subscription, klik `[Review]` pada pengajuan Convert, pilih Approve, lalu klik Submit
2. Tunggu aksi selesai: dialog Review tertutup
3. Buka Allocation > Client Subscription tab "Current", ketik Search `Klinik Harapan Bunda+{runId}-082`, tekan Enter
4. Verifikasi term paid berstatus Active dengan Start Date hari approval (mode New terkunci hari ini)
5. Verifikasi Wallet di-Capture
6. Buka modal Subscription Log term paid
7. Verifikasi Subscription Log term paid memuat `Subscription approved by Eko Saputra`
8. Tutup modal, klik tab "History", ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-082`, tekan Enter
9. Verifikasi trial berstatus Converted bersamaan titik ini
10. Buka modal Subscription Log baris Trial
11. Verifikasi Subscription Log baris Trial memuat `Subscription converted by Eko Saputra`
12. Tutup modal, buka modal Changelog, ketik Search `Klinik Harapan Bunda+{runId}-082`, tekan Enter
13. Verifikasi Changelog memuat pada baris Trial `Convert` Field `Subscription Type` Old `Trial — Growth` New `Professional (Paid)`
14. Verifikasi Changelog tidak memuat Action `Approve`
15. Tutup modal Changelog dengan `✕`, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-307: Reject Convert jalur request: trial tetap Active dan dapat diajukan ulang

16. Buka Approvals > Client Subscription, pilih radio Reject pada pengajuan Convert, isi `Rejection Reason` dengan `Pembelian dari trial belum disetujui`, klik `[Submit Decision]`, lalu konfirmasi pada dialog Konfirmasi Reject
17. Tunggu aksi selesai: dialog Konfirmasi Reject tertutup
18. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Klinik Harapan Bunda+{runId}-082`, tekan Enter
19. Verifikasi term paid berstatus Rejected dan Reserve dilepas
20. Klik tab "Current", ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-082`, tekan Enter, lalu klik ikon `⋯` pada baris trial
21. Verifikasi trial tetap Active tidak tersentuh dan row action Convert masih tersedia
22. Verifikasi Plan Owner dan data trial tidak berubah
23. Tutup menu, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-308: Approve Convert saat trial sudah Expired: trial tetap Expired

24. Atur jam server dan jam browser ke `19/08/26`, buka Approvals > Client Subscription, klik `[Review]` pada pengajuan `{idConv}`, pilih Approve, lalu klik Submit
25. Tunggu aksi selesai: dialog Review tertutup
26. Buka Allocation > Client Subscription tab "Current", ketik Search `{idConv}`, tekan Enter
27. Verifikasi term paid diproses sebagai pembelian biasa mode New dengan Start Date `19/08/26` dan berstatus Active
28. Ganti isi kotak search dengan `{idTrialExp}`, tekan Enter
29. Verifikasi trial `{idTrialExp}` tetap Expired dan tidak menjadi Converted
30. Pulihkan jam server dan jam browser lewat fixture waktu
31. Ganti isi kotak search dengan `{idConv}`, tekan Enter
32. Buka modal Subscription Log term paid
33. Verifikasi Subscription Log term paid memuat `Subscription approved by Eko Saputra`
34. Tutup modal, ganti isi kotak search dengan `{idTrialExp}`, tekan Enter
35. Buka modal Subscription Log baris Trial
36. Verifikasi Subscription Log baris Trial memuat sedikitnya satu entri lain
37. Verifikasi Subscription Log baris Trial tidak memuat entri `Subscription converted`
38. Tutup modal, buka modal Changelog, ketik Search `{idTrialExp}`, tekan Enter
39. Verifikasi Changelog memuat sedikitnya satu entri lain milik `{idTrialExp}`
40. Verifikasi Changelog tidak memuat baris `Convert` maupun `Approve`
41. Tutup modal Changelog dengan `✕`, lalu seed ulang pengajuan lewat fixture backend

### TC-AC-CS-309: Approve Renewal ditolak saat predecessor sudah Archive

42. Pindahkan predecessor `{idPred}` ke Archive lewat job lifecycle (fixture waktu), buka Approvals > Client Subscription, klik `[Review]` pada pengajuan `{idRenew}`, pilih Approve, lalu klik Submit
43. Verifikasi dialog blok milik Approvals dengan Title "Cannot Renew Subscription" dan Body "Subscription no longer eligible for renewal"
44. Verifikasi Approve ditolak dan status pengajuan tetap Waiting for Approval
45. Tutup dialog blok, buka Allocation > Client Subscription, klik tab "History", ketik Search `{idPred}`, tekan Enter
46. Verifikasi predecessor tetap berstatus Archive dan tidak berubah
47. Pulihkan jam server dan baseline pengajuan lewat fixture backend

### TC-AC-CS-300: Approve Renewal atas predecessor Expired setelah hari submit direbase ke tanggal approval

48. Logout, lalu login sebagai Total Control Partner Lestari Wulandari
49. Atur jam server dan jam browser ke `20/08/26`, buka Approvals > Client Subscription, klik `[Review]` pada pengajuan Renewal atas `{idPredExp}`, pilih Approve, lalu klik Submit
50. Tunggu aksi selesai: dialog Review tertutup
51. Buka Allocation > Client Subscription tab "Current", ketik Search `Bengkel Maju Jaya+{runId}-082`, tekan Enter, lalu klik baris successor untuk membuka Detail term
52. Verifikasi Start Date `20/08/26` (tanggal approval, tidak retroaktif) dan End Date `19/08/27` (20/08/26 + 1 tahun - 1 hari)
53. Verifikasi term berstatus Active
54. Klik tab "History", ganti isi kotak search dengan `{idPredExp}`, tekan Enter
55. Verifikasi predecessor berstatus Renewed
56. Verifikasi penyesuaian tanggal tidak menghasilkan notifikasi tersendiri dan requester hanya menerima notifikasi "Subscription approved"
57. Pulihkan jam server, logout, lalu login kembali sebagai Total Control Distributor Eko Saputra

## Notes

- Langkah penghubung: navigasi menu, tab, Search (R-16: untuk menemukan baris target; termasuk ganti isi kotak search antara term paid `{idConv}` dan trial `{idTrialExp}` pada TC-AC-CS-308), `Tunggu aksi selesai` sesudah Submit, pemulihan jam sebelum Subscription Log dibuka, penutupan modal dan menu, ganti akun, serta seed ulang pengajuan dan pemulihan jam lewat fixture antar blok. Pada TC-AC-CS-309 dan TC-AC-CS-300 predecessor diperiksa di tab "History" lewat Search Subscription ID.
- P-1: asersi "modal Changelog tidak memuat Action `Approve`" (atau `Reject`) tetap di spec ini karena bergantung pada state berat (pengajuan ber-Reserve wallet yang diputuskan sekali dan tidak dapat diulang tanpa biaya besar); tiap asersi didahului Verifikasi entri lain milik term pada Changelog yang sama sebagai anchor positif dan memakai baseline jumlah entri (S-12). Approve dan Reject dicatat di Subscription Log, Activity Log, dan System Log approver (ACCS-LOGIC-06a).
- Alasan spec 57 langkah, di atas smell 35 langkah: kelima TC memakai halaman Approvals yang sama dan alur keputusan atas pengajuan Convert atau Renewal yang di-seed spec sendiri; tiap blok berdiri sendiri dengan seed ulang dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemecahan menambah hook, login, dan seeding tanpa menambah isolasi.
- Temuan untuk QA: (1) TC-AC-CS-306 dan TC-AC-CS-307 bergantung pada TC-AC-CS-246 (Convert jalur request) tanpa identitas pengajuan; spec men-seed pengajuan sendiri (S-06). (2) TC-AC-CS-307 butir a mencampur status Rejected dan Reserve dilepas; Reserve dibaca lewat kemampuan baca Wallet. (3) TC-AC-CS-309 diklasifikasikan dua sesi paralel; pemindahan predecessor ke Archive dipicu fixture waktu sebelum Approve. (4) TC-AC-CS-308 butir c menyebut Changelog tanpa `Convert` maupun `Approve` tanpa kolom identitas; spec mencari lewat Subscription ID trial. (5) TC-AC-CS-306 Expected c menyatakan dua record dengan satu Changelog; spec memverifikasi sesuai butir TC. (6) TC-AC-CS-300 precondition requester Create-Only Partner CV Karya Mandiri (#12) dan approver Total Control Partner; akun approver ditulis sebagai Lestari Wulandari (#11). (7) TC-AC-CS-309 butir c ("Predecessor dan data lain tidak berubah") tidak menyebut data lain mana; spec hanya mengamati status predecessor di tab "History" setelah dialog blok ditutup, dan "data lain" tidak diasersi. TC tidak menyebut tombol penutup dialog blok sehingga langkah memakai frasa umum "Tutup dialog blok".
