---
id: TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial
title: "Resubmit dan Edit Renewal: Partner Trial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-282
  - TC-AC-CS-286
  - TC-AC-CS-615
  - TC-AC-CS-210
  - TC-AC-CS-216
coverage:
  web: automated
---

# Resubmit dan Edit Renewal: Partner Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Rina Pratama, Create-Only Partner CV Karya Mandiri (Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (dibuat lewat API di hook `before` lewat sesi API aktor requester, dihapus di hook `after`; Subscription ID dibaca lewat API seeding dan dirujuk di langkah sebagai nilai terbaca):
  - Client `Optik Cahaya+{runId}-074` (binaan langsung CV Karya Mandiri; padanan Pre-setup #34) dengan baris Trial Canceled FAMS Professional (badge Trial), tanpa tanggal, Plan Owner CV Karya Mandiri, Trial Duration 30 hari, Trial Asset Quota 50, Trial Concurrent User Quota 10, requester original `Rina Pratama` milik aktor (padanan #81).
  - Client `Toko Mitra Karya+{runId}-074` dengan predecessor SAMS Growth Active (01/09/25 sampai 31/08/26, Plan Owner CV Karya Mandiri (Partner)) dan successor Renewal `{idMitraRenewal}` SAMS Growth Waiting for Approval (tanggal -/-, Plan Owner CV Karya Mandiri (Partner), milik aktor `Rina P`, Pay From `Partner Pocket`; padanan #113).
- Data Pre-setup yang tidak ditulis spec: kantong Wallet Partner `Partner Pocket` $25,000.00 dan `Distributor Pocket` $12,000.00 (#21), hanya dibaca.
- Toggle `Require Approval for Trial Activation` (platform-wide, #24): hook `before` spec ini menyetelnya ON untuk blok TC-AC-CS-282 (nilai awal dicatat); langkah di blok TC-AC-CS-615 menyetelnya OFF dan memulihkannya ke ON lewat fixture backend (disediakan tim FE/BE); hook `after` memulihkan nilai awal. Toggle adalah state global bersama sehingga tidak dapat dibuat per spec.
- Data Dinamis: record Trial baru hasil Resubmit milik spec dibersihkan antar blok dan di hook `after` bersama Client seed; baris Pre-setup bersama tidak ditulis.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu (jam server dan jam browser absolut, tanggal acuan `19/08/26`; diatur di hook `before`, dipulihkan di hook `after`); klien HTTP atau fixture BE untuk request langsung ke server pada blok TC-AC-CS-286 (POST Activate Trial Client `Optik Cahaya` Product `FAMS` Plan `Professional` dengan token sesi aktor); endpoint tidak dikarang (S-13).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-282: Resubmit record Trial Canceled membuka form Activate Trial

1. Klik tab "History"
2. Ketik Search `Optik Cahaya+{runId}-074`, tekan Enter
3. Klik ikon `⋯` pada baris Trial Canceled `Optik Cahaya+{runId}-074`, pilih `Resubmit`
4. Verifikasi form Activate Trial terbuka dengan field Client, Product, dan Plan Disabled dan terisi dari record asal
5. Klik `[Submit]`
6. Tunggu aksi selesai (form tertutup)
7. Klik tab "Current", ganti isi kotak search dengan `Optik Cahaya+{runId}-074`, tekan Enter
8. Verifikasi record Trial baru dibuat dengan referensi asal menunjuk record lama
9. Buka modal Changelog, ketik Search dengan Subscription ID record Trial baru, tekan Enter
10. Verifikasi entri Changelog mencatat Action `Resubmit (Trial)`, Field `Status`, Old `—`, New `Waiting for Approval`
11. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline lewat fixture backend (record Trial baru dibersihkan)

### TC-AC-CS-615: Resubmit record Trial Canceled saat toggle Trial OFF langsung Active

12. Atur Toggle `Require Approval for Trial Activation` menjadi OFF lewat fixture backend
13. Klik tab "History"
14. Ganti isi kotak search dengan `Optik Cahaya+{runId}-074`, tekan Enter
15. Klik ikon `⋯` pada baris Trial Canceled `Optik Cahaya+{runId}-074`, pilih `Resubmit`
16. Verifikasi form Activate Trial terbuka dengan field Client, Product, dan Plan Disabled dan terisi dari record asal
17. Verifikasi Trial Duration `30` terisi dari record asal
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, trial has been activated for Optik Cahaya+{runId}-074 — Professional, 30 days."
20. Klik tab "Current", ganti isi kotak search dengan `Optik Cahaya+{runId}-074`, tekan Enter
21. Verifikasi record Trial baru berstatus Active (tanpa Waiting for Approval) dengan Start Date `19/08/26` dan Plan Owner `CV Karya Mandiri (Partner)`
22. Verifikasi record Trial baru memiliki referensi asal yang menunjuk record lama
23. Klik tab "History", ganti isi kotak search dengan `Optik Cahaya+{runId}-074`, tekan Enter
24. Verifikasi record lama tetap Canceled dan tidak berubah
25. Pulihkan Toggle `Require Approval for Trial Activation` ke ON dan bersihkan record Trial baru lewat fixture backend

### TC-AC-CS-210: Form Activate Trial dari Resubmit mengunci Client, Product, dan Plan

26. Ganti isi kotak search dengan `Optik Cahaya+{runId}-074`, tekan Enter
27. Klik ikon `⋯` pada baris Trial Canceled `Optik Cahaya+{runId}-074` di tab "History", pilih `Resubmit`
28. Verifikasi modal Activate Trial terbuka dengan field Client, Product, dan Plan Disabled dan terisi dari record Canceled
29. Verifikasi field Duration dan kuota ter-isi dari record asal dan dapat diubah
30. Tutup modal dengan `✕`, verifikasi dialog `Unsaved Changes` tampil, klik `[Leave]`

### TC-AC-CS-286: Activate Trial biasa atas trial Canceled ditolak dengan pesan V-17

31. Kirim request langsung ke server (klien HTTP tanpa melalui UI) dengan token sesi aktor: POST Activate Trial Client `Optik Cahaya+{runId}-074` Product `FAMS` Plan `Professional`
32. Verifikasi respons server menolak dengan pesan "Trial already used for Professional"

### TC-AC-CS-216: Field identitas dan Pay From terkunci pada Edit varian Renew

33. Klik tab "Current", ganti isi kotak search dengan `{idMitraRenewal}`, tekan Enter, lalu klik ikon `⋯` pada baris itu dan pilih `Edit`
34. Verifikasi modal Edit Subscription terbuka ter-isi dari record
35. Klik field Client, Product, Plan, Renewal Option, dan Pay From satu per satu
36. Verifikasi Client, Product, Plan, Renewal Option, dan Pay From Disabled dengan nilai record
37. Verifikasi tidak ada field itu yang dapat diubah

## Notes

- Langkah penghubung: tab, Search (R-16: untuk menemukan baris target), penutupan modal Changelog, pemulihan fixture antar blok (record Trial baru milik spec dan Toggle), serta `Tunggu aksi selesai` sesudah `[Submit]` Resubmit sebelum pindah tab.
- Urutan TC: TC-AC-CS-282 sebelum TC-AC-CS-615 karena keduanya meresubmit trial Canceled yang sama dan record baru dibersihkan antar blok; TC-AC-CS-210 dan TC-AC-CS-286 memakai trial Canceled yang kembali ke keadaan awal; TC-AC-CS-216 memakai term Renewal yang berbeda dan berakhir tanpa mengubah data. Modal Edit Subscription pada TC-AC-CS-216 tidak diubah sehingga tidak dirty.
- TC-AC-CS-286 adalah request langsung ke server (bagian 8b butir 1): yang diasersi hanya respons penolakan; state data tidak diasersi karena TC tidak memberi cara cek.
- Alasan melewati sekitar 35 langkah (37 langkah): semua blok satu topik (Resubmit dan Edit Renewal Partner Trial) dengan satu akun dan data seed milik spec, tanpa kelas harness lain.
- Temuan untuk QA: (1) TC-AC-CS-286 butir b ("Trial Canceled hanya dapat diminta kembali lewat Resubmit") tidak punya langkah observasi sehingga tidak diasersi terpisah (S-01). (2) TC-AC-CS-216 butir c ("Mengganti plan hanya lewat Cancel Request lalu Resubmit") bukan keadaan yang teramati di modal Edit; tidak diasersi. (3) TC-AC-CS-615 Post Condition a (record Trial Active tampil di tab Current) ditutup oleh Verifikasi record Trial baru di tab Current. (4) TC-AC-CS-282 tidak menyebut keadaan Toggle Trial pada precondition selain ON (#24); spec memakai ON. (5) TC-AC-CS-210 tidak menyatakan apakah modal ter-isi dihitung dirty; spec memakai penutupan S-08.
