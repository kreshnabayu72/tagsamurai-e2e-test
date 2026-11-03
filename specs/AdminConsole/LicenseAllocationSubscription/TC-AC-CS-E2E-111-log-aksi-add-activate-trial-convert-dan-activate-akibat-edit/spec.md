---
id: TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit
title: "Log Aksi: Add, Activate Trial, Convert, dan Activate akibat Edit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-432
  - TC-AC-CS-433
  - TC-AC-CS-434
  - TC-AC-CS-440
coverage:
  web: automated
---

# Log Aksi: Add, Activate Trial, Convert, dan Activate akibat Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Group Manager scope Group Jawa, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-111`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-432: Client `Client Tanpa Subscription+{runId}-111` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial; bentuk Pre-setup #48).
  2. TC-AC-CS-433: Client `Klinik Harapan Bunda+{runId}-111` (binaan PT Maju Bersama pada group `Jawa` dan CV Karya Mandiri) dengan Trial SAMS Growth status Active, Plan Owner CV Karya Mandiri, tanpa term paid SAMS (bentuk Pre-setup #43 dan #71).
  3. TC-AC-CS-434: Client `Client Tanpa Subscription Add+{runId}-111` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial; bentuk Pre-setup #48).
  4. TC-AC-CS-440: Client `Percetakan Mega+{runId}-111` dengan term Pending FAMS plan Professional, Plan Owner PT Maju Bersama (Distributor), diajukan Group Manager `Dewi A` (bentuk Pre-setup #57).

## Test Steps

### TC-AC-CS-432: Log Activate Trial

1. Pemicu (sesi API): aktifkan Trial plan Growth selama 30 days pada Client `Client Tanpa Subscription+{runId}-111` hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `Client Tanpa Subscription+{runId}-111`, tekan Enter, dan cari entri Action `Activate`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Activate`, Client — Product `Client Tanpa Subscription+{runId}-111`, Field `Subscription Type`, Old Value `—`, New Value `Trial — Growth, 30 days`, Modified By `Hendra W`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `Client Tanpa Subscription+{runId}-111`, Action `Activate`, Field `Subscription Type`, Old `—`, New `Trial — Growth, 30 days`, Modified By `Hendra W`
6. Buka Detail user Hendra W, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Hendra W baru: Action `Activate`, Object `Client Subscription`, Name `Client Tanpa Subscription+{runId}-111`, Field `Subscription Type`, Old `—`, New `Trial — Growth, 30 days`
8. Ganti akun: klik Logout dari akun sebelumnya
9. Login sebagai `Dewi Anggraini` (`groupManagerSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_GM_PASSWORD`)

### TC-AC-CS-433: Log Convert Trial

10. Pemicu (sesi API): konversi Trial `Klinik Harapan Bunda+{runId}-111` menjadi Professional (Paid) hingga perubahan tersimpan
11. Buka menu Allocation > Client Subscription
12. Buka modal Changelog, ketik Search `Klinik Harapan Bunda+{runId}-111`, tekan Enter, dan cari entri Action `Convert`
13. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Convert`, Client — Product `Klinik Harapan Bunda+{runId}-111`, Field `Subscription Type`, Old Value `Trial — Growth`, New Value `Professional (Paid)`, Modified By `Dewi A`
14. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
15. Verifikasi entri Activity Log `Client Subscription` baru: Name `Klinik Harapan Bunda+{runId}-111`, Action `Convert`, Field `Subscription Type`, Old `Trial — Growth`, New `Professional (Paid)`, Modified By `Dewi A`
16. Buka Detail user Dewi A, tab System Log, dan cari entri yang sama
17. Verifikasi entri System Log Detail user Dewi A baru: Action `Convert`, Object `Client Subscription`, Name `Klinik Harapan Bunda+{runId}-111`, Field `Subscription Type`, Old `Trial — Growth`, New `Professional (Paid)`

### TC-AC-CS-434: Log Add Subscription

18. Pemicu (sesi API): tambah Subscription SAMS plan Growth untuk Client `Client Tanpa Subscription Add+{runId}-111` hingga perubahan tersimpan
19. Buka menu Allocation > Client Subscription
20. Buka modal Changelog, ketik Search `Client Tanpa Subscription Add+{runId}-111`, tekan Enter, dan cari entri Action `Add Subscription`
21. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Add Subscription`, Client — Product `Client Tanpa Subscription Add+{runId}-111 — SAMS`, Field `Plan`, Old Value `—`, New Value `Growth`, Modified By `Dewi A`
22. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
23. Verifikasi entri Activity Log `Client Subscription` baru: Name `Client Tanpa Subscription Add+{runId}-111 — SAMS`, Action `Add Subscription`, Field `Plan`, Old `—`, New `Growth`, Modified By `Dewi A`
24. Buka Detail user Dewi A, tab System Log, dan cari entri yang sama
25. Verifikasi entri System Log Detail user Dewi A baru: Action `Add Subscription`, Object `Client Subscription`, Name `Client Tanpa Subscription Add+{runId}-111 — SAMS`, Field `Plan`, Old `—`, New `Growth`

### TC-AC-CS-440: Log Activate akibat Save Edit Start Date hari ini

26. Pemicu (sesi API): simpan Edit Start Date menjadi hari ini pada term Pending `Percetakan Mega+{runId}-111 — FAMS` hingga perubahan tersimpan
27. Buka menu Allocation > Client Subscription
28. Buka modal Changelog, ketik Search `Percetakan Mega+{runId}-111`, tekan Enter, dan cari entri Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`
29. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`, Client — Product `Percetakan Mega+{runId}-111 — FAMS`, Field `Status`, Old Value `Pending`, New Value `Active`, Modified By `Dewi A`
30. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
31. Verifikasi entri Activity Log `Client Subscription` baru: Name `Percetakan Mega+{runId}-111 — FAMS`, Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`, Field `Status`, Old `Pending`, New `Active`, Modified By `Dewi A`
32. Buka Detail user Dewi A, tab System Log, dan cari entri yang sama
33. Verifikasi entri System Log Detail user Dewi A baru: Action `Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`, Object `Client Subscription`, Name `Percetakan Mega+{runId}-111 — FAMS`, Field `Status`, Old `Pending`, New `Active`
34. Verifikasi entri ini berpasangan dengan entri `Edit` Field `Start Date` pada waktu Save yang sama

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-432 (akun Principal) lebih dulu, lalu TC-AC-CS-433, 434, dan 440 (akun Group Manager) sesudah ganti akun, agar ganti akun hanya satu kali (S-10).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 11, 19, dan 27) yang membuka List kembali sesudah login atau sesudah Activity Log dan System Log sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-440 Langkah Uji dan Expected menulis Action sebagai prosa (`Activate (Save Edit, mode New dengan Start Date hasil edit = hari ini; aktor)`), bukan literal UI Changelog; spec mempertahankan teks itu apa adanya sebagai nilai Action dan perlu literal Action yang sebenarnya tampil dari QA.
  - TC-AC-CS-440 Expected d (entri berpasangan dengan entri `Edit` Field `Start Date`) tidak menyebut nilai entri pasangan; spec hanya mengasersi keberadaan pasangannya pada waktu Save yang sama (nilai pasangan diasersi di spec lain suite ini).
