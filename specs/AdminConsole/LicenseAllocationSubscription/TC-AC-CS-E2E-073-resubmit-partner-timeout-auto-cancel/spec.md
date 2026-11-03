---
id: TC-AC-CS-E2E-073-resubmit-partner-timeout-auto-cancel
title: "Resubmit: Partner Timeout Auto-Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-280
  - TC-AC-CS-285
  - TC-AC-CS-23
coverage:
  web: automated
---

# Resubmit: Partner Timeout Auto-Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Rina Pratama, Create-Only Partner CV Karya Mandiri (Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup: baris `SUBS-20260805-00001` (Client Optik Cahaya, FAMS, plan Growth, status Canceled, tanggal - / -, Plan Owner CV Karya Mandiri (Partner), #56) yang Canceled oleh Timeout Auto-Cancel milik aktor; Toggle `Require Approval for Allocation` ON untuk CV Karya Mandiri dan aktor bukan bypass (#23); Partner `CV Karya Mandiri` punya dua kantong Wallet sumber, `Partner Pocket` saldo tersedia $25,000.00 (#21); Approval Timeout platform 3 hari (#26); harga FAMS Growth $4,000.00 per tahun.
- Dipakai sebagai precondition TC, tidak diasersi: pada blok TC-AC-CS-285 Approval Timeout platform diubah menjadi 5 hari dan harga FAMS Growth menjadi $4,500.00 per tahun oleh fixture backend (disediakan tim FE/BE) sebelum Resubmit.
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- State global yang diubah: Approval Timeout platform, harga FAMS Growth, jam server (dipulihkan di hook `after` dan sebagai langkah penghubung). Record baru hasil Resubmit dibersihkan fixture backend antar blok; baris Pre-setup `SUBS-20260805-00001` tidak berubah (Last Updated tetap). Entri Changelog dan audit trail bersifat permanen sehingga entri record baru dicari lewat Subscription ID record baru (baseline nol).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-280: Resubmit record Canceled hasil Timeout Auto-Cancel membuat record baru

1. Klik tab "History"
2. Ketik Search `SUBS-20260805-00001`, tekan Enter
3. Klik ikon `⋯` pada baris `SUBS-20260805-00001`, pilih `Resubmit`
4. Verifikasi form `+ Subscription` terbuka ter-isi Client `Optik Cahaya`, Product `FAMS`, dan Plan `Growth` dari field domain record lama (bukan field approval)
5. Verifikasi form masih terbuka tanpa submit otomatis sebelum `[Submit]` diklik
6. Pilih Pay From `Partner Pocket`, klik `[Submit]`
7. Tunggu aksi selesai (dialog/modal tertutup)
8. Klik tab "Current", ganti isi kotak search dengan `Optik Cahaya`, tekan Enter, lalu klik baris berstatus Waiting for Approval untuk membuka Subscription Detail
9. Verifikasi record baru bernomor `SUBS-` yang berbeda dari `SUBS-20260805-00001` dan berstatus Waiting for Approval
10. Verifikasi record baru memiliki SLA approval baru
11. Verifikasi card Subscription Info record baru menampilkan referensi asal yang menunjuk `SUBS-20260805-00001`
12. Verifikasi card Subscription Info menampilkan catatan kecil non-intrusive `Resubmitted From` berisi `SUBS-20260805-00001`
13. Klik menu Allocation > Client Subscription di sidebar, klik tab "History", ketik Search `SUBS-20260805-00001`, tekan Enter
14. Verifikasi baris `SUBS-20260805-00001` tetap berstatus Canceled dan tidak berubah
15. Buka modal Changelog, ketik Search dengan Subscription ID record baru, tekan Enter
16. Verifikasi entri Changelog record baru mencatat Action `Resubmit`, Field `Plan`, Old `—`, New `Growth`
17. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline lewat fixture backend (record baru dibersihkan)

### TC-AC-CS-285: Resubmit memakai nilai timeout dan harga saat ini

18. Atur Approval Timeout platform menjadi 5 hari dan harga FAMS Growth menjadi $4,500.00 per tahun lewat fixture backend
19. Klik tab "History", ketik Search `SUBS-20260805-00001`, tekan Enter, lalu klik ikon `⋯` pada baris itu dan pilih `Resubmit`
20. Isi Duration `1` dan pilih Pay From `Partner Pocket`
21. Verifikasi Estimated Cost `1 year(s) × $4,500.00/year` = $4,500.00 (harga saat Resubmit, bukan snapshot record lama $4,000.00)
22. Klik `[Submit]`, lalu catat waktu submit
23. Tunggu aksi selesai (dialog/modal tertutup)
24. Atur jam server ke 4 hari setelah waktu submit, picu satu siklus job Timeout, dan poll hingga job selesai
25. Klik tab "Current", ganti isi kotak search dengan `Optik Cahaya`, tekan Enter
26. Verifikasi record baru tetap Waiting for Approval (batas lama 3 hari tidak dipakai)
27. Atur jam server ke 5 hari 1 jam setelah waktu submit, picu satu siklus job Timeout, dan poll hingga job selesai
28. Klik tab "History", ganti isi kotak search dengan `Optik Cahaya`, tekan Enter
29. Verifikasi record baru berstatus Canceled oleh Timeout Auto-Cancel (batas 5 hari saat ini)
30. Pulihkan jam server, Approval Timeout platform 3 hari, harga FAMS Growth $4,000.00, dan record baru lewat fixture backend

### TC-AC-CS-23: Term Canceled tampil di History dan hasil Resubmit tampil di Current

31. Klik tab "History", ketik Search `SUBS-20260805-00001`, tekan Enter, lalu klik row action `Resubmit` pada baris itu
32. Pilih Pay From `Partner Pocket`, klik `[Submit]`
33. Tunggu aksi selesai (dialog/modal tertutup)
34. Klik tab "Current", ganti isi kotak search dengan `Optik Cahaya`, tekan Enter
35. Verifikasi record baru bernomor `SUBS-` baru berstatus Waiting for Approval tampil di tab "Current"
36. Klik tab "History", ganti isi kotak search dengan `SUBS-20260805-00001`, tekan Enter
37. Verifikasi baris `SUBS-20260805-00001` tetap berstatus Canceled di tab "History" dan tidak berubah

## Notes

- Langkah penghubung: tab, Search (R-16: untuk menemukan baris target), `Tunggu aksi selesai` setelah tiap `[Submit]` (8b.8), penutupan modal Changelog, pemulihan fixture antar blok, serta pemulihan jam dan state global.
- Urutan TC: TC-AC-CS-285 mengubah Approval Timeout dan harga lalu berakhir dengan record Canceled oleh Timeout, sehingga TC-AC-CS-23 memakai nilai awal kembali setelah pemulihan. Resubmit berikutnya atas baris yang sama hanya sah bila record baru blok sebelumnya sudah dibersihkan (V-07), sehingga pemulihan fixture ditulis antar blok.
- Spec ini 37 langkah, di atas smell 35 langkah. Alasan: ketiga blok satu topik (Resubmit record Canceled oleh Timeout Auto-Cancel) pada baris Pre-setup yang sama dan berdiri sendiri; TC-AC-CS-285 butuh dua pergeseran jam dan Search antar tab sehingga tidak dapat dipersingkat.
- Post Condition TC-AC-CS-280 (record baru tampil di tab Current dan Approvals > Client Subscription; record lama di tab History) tidak punya langkah observasi di Approvals; yang diasersi hanya List (S-01).
- Temuan untuk QA: (1) TC-AC-CS-280 tidak menyatakan cara mencari entri di modal Changelog; spec memakai Search dengan Subscription ID record baru. (2) TC-AC-CS-285 langkah 3 dan 4 menyebut geser jam relatif terhadap waktu submit tanpa nilai absolut; spec mencatat waktu submit sesudah klik `[Submit]` (bagian 8b butir 3), margin terhadap batas 5 hari kurang dari 5 menit. (3) Email akun Pre-setup #12 dirujuk lewat fixture yang belum ada.
