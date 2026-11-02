---
id: TC-AC-CS-E2E-075-resubmit-distributor-dan-principal
title: "Resubmit: Distributor dan Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-281
  - TC-AC-CS-284
  - TC-AC-CS-283
coverage:
  web: automated
---

# Resubmit: Distributor dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD` (akun pertama, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite). Ganti akun di tengah spec: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1, `Spectra.env.AC_SUB_TC_PASSWORD`), lalu Rina Pratama, Create-Only Partner CV Karya Mandiri (Pre-setup #12, `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`). Pelaku kedua Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9, `Spectra.env.AC_SUB_DIST_TC_PASSWORD`) lewat sesi API. Hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup: baris `SUBS-20260806-00001` (Client Salon Cantik Indah, FAMS, plan Growth, status Canceled, tanggal - / -, Plan Owner PT Maju Bersama (Distributor), #64) Canceled oleh requester sendiri (Cancel Request) milik Fajar Nugroho; Toggle `Require Approval for Allocation` ON (#23); Client `Salon Cantik Indah` belum punya term FAMS live pada awal blok TC-AC-CS-284; baris `SUBS-20260805-00001` (Optik Cahaya, FAMS, Growth, Canceled, Plan Owner CV Karya Mandiri (Partner), #56) milik requester `Rina P`; baris `SUBS-20241201-00001` (Client PT Abadi Jaya, SAMS, plan Enterprise, Canceled hasil Scheduled Flip Auto-Cancel, tanggal 01/01/25 / 31/12/25, Plan Owner CV Karya Mandiri (Partner), #93 dan #94) dengan requester original `Rina Pratama`.
- Jam: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pelaku kedua pada blok TC-AC-CS-284 membuat term FAMS Active untuk Client `Salon Cantik Indah` (Plan `Growth`, Duration `1`, Start Date `19/08/26`) lewat sesi API Eko Saputra hingga term tersimpan; term itu dibersihkan fixture backend setelah blok.
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- State global yang diubah: jam server dan jam browser (tanggal acuan `19/08/26`, dipulihkan di hook `after`). Record baru hasil Resubmit dan term FAMS milik pelaku kedua dibersihkan fixture backend antar blok; baris Pre-setup tidak diubah.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-281: Resubmit record Canceled hasil Cancel Request manual

1. Klik tab "History", ketik Search `SUBS-20260806-00001`, tekan Enter
2. Klik ikon `⋯` pada baris `SUBS-20260806-00001`, pilih `Resubmit`
3. Verifikasi form `+ Subscription` mode New terbuka ter-isi dari record asal
4. Verifikasi Footer form memuat checkbox "Stay on this form after submitting" di atas `[Clear Field]` dan `[Submit]` (varian Add)
5. Klik `[Submit]`
6. Tunggu aksi selesai (dialog/modal tertutup)
7. Klik tab "Current", ketik Search `Salon Cantik Indah`, tekan Enter
8. Verifikasi record baru berstatus Waiting for Approval karena Toggle `Require Approval for Allocation` ON dan aktor bukan bypass
9. Bersihkan record baru lewat fixture backend, lalu klik tab "History", ketik Search `SUBS-20260806-00001`, tekan Enter
10. Klik ikon `⋯` pada baris `SUBS-20260806-00001`, pilih `Resubmit`, lalu klik `[Submit]`
11. Tunggu aksi selesai (dialog/modal tertutup)
12. Klik tab "Current", ketik Search `Salon Cantik Indah`, tekan Enter
13. Verifikasi Resubmit kedua atas record yang sama diterima dan menghasilkan record berstatus Waiting for Approval (tidak ada limit jumlah Resubmit)
14. Bersihkan record baru lewat fixture backend

### TC-AC-CS-284: Resubmit mode New ditolak bila Client+Product kini punya term live

15. Buat term FAMS Active untuk Client `Salon Cantik Indah` (Plan `Growth`, Duration `1`, Start Date `19/08/26`) lewat sesi API Eko Saputra hingga term tersimpan
16. Ketik Search `Salon Cantik Indah`, tekan Enter, lalu catat jumlah baris tab "Current" sebagai baseline
17. Klik tab "History", ganti isi kotak search dengan `SUBS-20260806-00001`, tekan Enter
18. Klik ikon `⋯` pada baris `SUBS-20260806-00001`, pilih `Resubmit`, lalu klik `[Submit]`
19. Verifikasi Submit ditolak dengan pesan "This client already has an active subscription for this product."
20. Tutup form dengan `✕`, verifikasi dialog `Unsaved Changes` tampil, klik `[Leave]`
21. Verifikasi baris `SUBS-20260806-00001` tetap berstatus Canceled dan tidak berubah
22. Klik tab "Current", ganti isi kotak search dengan `Salon Cantik Indah`, tekan Enter
23. Verifikasi jumlah baris tab "Current" sama dengan baseline (tidak ada record baru)
24. Bersihkan term FAMS Active milik pelaku kedua lewat fixture backend

### TC-AC-CS-283: Resubmit Hidden bagi non-requester dan Canceled hasil Scheduled Flip Auto-Cancel

25. Logout, lalu login sebagai Total Control Principal Hendra Wijaya
26. Buka menu Allocation > Client Subscription
27. Klik tab "History", ketik Search `SUBS-20260805-00001`, tekan Enter, lalu klik ikon `⋯` pada baris itu
28. Verifikasi menu baris milik requester lain hanya berisi Detail dan Subscription Log
29. Tutup menu, ganti isi kotak search dengan `SUBS-20241201-00001`, tekan Enter, lalu klik ikon `⋯` pada baris Canceled hasil Scheduled Flip Auto-Cancel
30. Verifikasi menu baris Canceled hasil Scheduled Flip Auto-Cancel hanya berisi Detail dan Subscription Log
31. Tutup menu, logout, lalu login sebagai Create-Only Partner Rina Pratama (requester original)
32. Buka menu Allocation > Client Subscription
33. Klik tab "History", ketik Search `SUBS-20241201-00001`, tekan Enter, lalu klik ikon `⋯` pada baris itu
34. Verifikasi menu baris yang sama bagi requester original `Rina Pratama` tetap hanya berisi Detail dan Subscription Log
35. Verifikasi Resubmit tidak tersedia bagi siapa pun termasuk requester original (EC-81)
36. Tutup menu, logout, lalu login kembali sebagai Create-Only Distributor Fajar Nugroho

## Notes

- Langkah penghubung: tab, Search (R-16: untuk menemukan baris target), penutupan menu, pembersihan record lewat fixture antar blok, ganti akun, `Buka menu Allocation > Client Subscription` sesudah tiap login ganti akun, dan `Tunggu aksi selesai` setelah `[Submit]` (8b.8).
- Spec ini 36 langkah, di atas smell 35 langkah. Alasan: ketiga blok satu topik (Resubmit record Canceled) pada baris Pre-setup yang sama dan berdiri sendiri; TC-AC-CS-283 butuh tiga ganti akun dengan langkah `Buka menu` dan Search per akun sehingga tidak dapat dipersingkat.
- Spec memakai tiga akun: TC-AC-CS-283 berprecondition Total Control (Principal) tetapi langkah 3 memakai login sebagai `Rina Pratama` (Pre-setup #12); ketiganya tertulis di Prerequisites.
- TC-AC-CS-281 butir c ("Tidak ada limit jumlah Resubmit") tidak punya langkah di TC; spec mengamatinya lewat Resubmit kedua atas record yang sama setelah record baru dibersihkan.
- Temuan untuk QA: (1) TC-AC-CS-283 precondition akun aktor Total Control (Principal) tetapi langkah 3 meminta login sebagai `Rina Pratama`. (2) TC-AC-CS-284 butir b ("Tidak ada record baru dan record lama tidak berubah") tidak menyebut cara cek; spec memakai baseline jumlah baris Search `Salon Cantik Indah` dan status baris lama. (3) TC-AC-CS-281 dan TC-AC-CS-284 tidak menyatakan apakah form Resubmit ter-isi dihitung dirty; spec memakai penutupan S-08 pada kasus ditolak.
