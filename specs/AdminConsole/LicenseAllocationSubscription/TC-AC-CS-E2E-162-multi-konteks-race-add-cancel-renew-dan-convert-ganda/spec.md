---
id: TC-AC-CS-E2E-162-multi-konteks-race-add-cancel-renew-dan-convert-ganda
title: "Multi-konteks: Race Add, Cancel dan Renew, serta Convert Ganda"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-516
  - TC-AC-CS-517
  - TC-AC-CS-577
coverage:
  web: automated
---

# Multi-konteks: Race Add, Cancel dan Renew, serta Convert Ganda

## Prerequisites

- Mode: FE+BE.
- Kelas harness c (multi-konteks). Sesi A: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (konteks browser kedua, objek asersi): untuk TC-AC-CS-516 dan 517 Total Control Principal kedua `Fixture.license-allocation-subscription.principalSessionB`, password `Spectra.env.AC_SUB_TC_B_PASSWORD` (email tidak tertulis di Pre-setup TC; disediakan tim FE, lihat Temuan untuk QA); untuk TC-AC-CS-577 Group Manager Distributor (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, bypass), password `Spectra.env.AC_SUB_GM_PASSWORD`.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-162`):
  1. TC-AC-CS-516: Client `Client Tanpa Subscription+{runId}-162` (setara `Client Tanpa Subscription`, Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial), Product `SAMS`; nilai form Add yang sama pada kedua sesi dirujuk lewat `Fixture.license-allocation-subscription.addForm516`.
  2. TC-AC-CS-517: term Active FAMS Professional `T517a` (Subscription ID dibaca lewat API seeding; setara `SUBS-20250815-00001`, Pre-setup #69, Plan Owner PT Maju Bersama).
  3. TC-AC-CS-577: Client `Klinik Harapan Bunda+{runId}-162` dengan trial `T577` (Subscription ID dibaca lewat API seeding) SAMS Growth Active (Start 10/08/26, End 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS; setara Pre-setup #71); saldo Main Pocket $25,000.00 (Pre-setup #20) dan harga SAMS Professional $7,000.00 diatur dan dibaca lewat fixture.
- State global yang diubah (suite serial): saldo Main Pocket (#20) pada TC-AC-CS-516 dan 577; dipulihkan oleh fixture backend yang disediakan tim FE/BE di hook `before`, `after`, dan sebagai langkah penghubung (S-06, pengecualian 2026-10-30); efeknya (transaksi Wallet) tercatat di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): konteks browser kedua yang menekan tombol bersamaan dengan sesi A (sinkronisasi klik oleh runner); membaca jumlah term, status trial, dan transaksi Reserve/Capture Wallet; endpoint tulis tidak tertulis di TC, PRD, atau LLD (S-13). Konteks sesi B ditutup dan sesi login browser terkait dihapus saat sesi B berganti peran dan di akhir spec (S-09); jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after` (status trial Active dan Start Date Convert hari ini bergantung pada tanggal acuan).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen` untuk akun UI suite termasuk sesi B. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-516: Dua admin mengirim Add mode New untuk Client dan Product yang sama bersamaan

1. Buka sesi B (konteks browser kedua), login sebagai Total Control Principal kedua, buka Allocation > Client Subscription tab Current
2. Sesi A dan sesi B klik `[+ Subscription]`
3. Isi form yang sama pada kedua sesi: Client `Client Tanpa Subscription+{runId}-162`, Product `SAMS`, nilai lain dari `Fixture.license-allocation-subscription.addForm516`
4. Klik `[Submit]` pada kedua sesi hampir bersamaan
5. Verifikasi hanya satu term yang terbentuk untuk Client `Client Tanpa Subscription+{runId}-162` dan Product `SAMS`
6. Verifikasi sesi yang kalah ditolak dengan pesan "This client already has an active subscription for this product."
7. Verifikasi tidak ada Reserve ganda pada Wallet
8. Pada sesi yang kalah (form masih terbuka) klik `✕`
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`

### TC-AC-CS-517: Cancel Subscription bersamaan dengan Renew pada term yang sama

11. Sesi A dan sesi B ketik Search `T517a`, tekan Enter
12. Sesi A klik ikon `⋯` pada term `T517a`, klik `Cancel Subscription` (dialog terbuka)
13. Sesi B klik ikon `⋯` pada term `T517a`, klik `Renew`, pilih Keep current plan dan isi Duration `1`
14. Sesi A klik `[Cancel Subscription]` dan sesi B klik `[Submit]` hampir bersamaan
15. Verifikasi hasil mengikuti tepat salah satu urutan commit: bila Cancel lebih dulu, Renew ditolak dengan dialog blok "Cannot Renew Subscription" dan Body "Subscription no longer eligible for renewal"; bila Renew lebih dulu, successor Pending dibatalkan oleh Cancel dan dialog Cancel memuat baris successor
16. Pemulihan sesi: sesi A dan sesi B klik menu `Client Subscription` di sidebar (tutup dialog atau form yang tersisa)

### TC-AC-CS-577: Dua admin Convert pada trial Active yang sama, Convert kedua ditolak dengan dialog blok

17. Tutup konteks sesi B, hapus sesi login browser terkait; buka sesi B baru dan login sebagai Group Manager `Dewi Anggraini`, buka Allocation > Client Subscription tab Current
18. Atur saldo Main Pocket $25,000.00 lewat fixture
19. Sesi A dan sesi B ketik Search `T577`, tekan Enter
20. Sesi A dan sesi B klik ikon `⋯` pada trial `T577`, klik `Convert Trial` (modal terbuka pada kedua sesi)
21. Sesi A pilih Plan `Professional`, isi Duration `1`, klik `[Submit]`, klik `[Convert]` (konversi diproses lebih dulu)
22. Tunggu aksi selesai (dialog/modal tertutup) pada sesi A
23. Pada sesi A klik tab `History`, ganti isi kotak search dengan `T577`, tekan Enter
24. Verifikasi pada sesi A trial `T577` berstatus Converted
25. Pada sesi A klik tab `Current`, ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-162`, tekan Enter
26. Verifikasi pada sesi A satu term paid Active terbentuk
27. Sesi B (modal masih terbuka dari data lama) pilih Plan `Professional`, isi Duration `1`, klik `[Submit]`, klik `[Convert]`
28. Verifikasi dialog blok Title "Data has changed" pada sesi B
29. Verifikasi Body dialog "• Klinik Harapan Bunda+{runId}-162 — SAMS" dan "This trial has already been converted by another user."
30. Verifikasi dialog hanya memuat tombol tunggal `[OK]`
31. Klik `[OK]` pada sesi B
32. Pada sesi B klik tab `History`
33. Pada sesi B ganti isi kotak search dengan `T577`, tekan Enter
34. Verifikasi daftar memuat ulang dan baris trial `T577` tampil di tab `History` berstatus Converted
35. Verifikasi tidak ada term paid kedua, tidak ada Reserve atau Capture dari sesi B, tidak ada record Convert kedua, dan tidak ada status trial baru
36. Pada sesi B klik tab `Current`
37. Pada sesi B ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-162`, tekan Enter
38. Verifikasi satu term paid SAMS Professional Active ada di tab `Current`
39. Tutup konteks sesi B dan hapus sesi login browser terkait

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-483 dan 515 (race dua admin Principal) ada di spec 137; TC-AC-CS-578 (Convert setelah Approve jalur request) ada di spec 138.
- Kelas c: sesi UI kedua adalah objek asersi (hasil tampil di sesi B), sehingga `P-2` tidak dipakai. TC-AC-CS-516, 517, 577 berbagi harness (dua sesi bersamaan) dan satu jenis konteks kedua.
- Spec ini 39 langkah, di atas smell 35 langkah. Alasan: ketiga blok satu topik (race multi-konteks dua sesi, kelas c) memakai harness yang sama; Search dan klik tab pada sesi B (R-16, S-14) tidak bisa dilebur karena asersi sesi B harus diperiksa per tab.
- Langkah penghubung (S-03): langkah 1 dan 17 (membuka dan mengganti konteks kedua, S-09), langkah 8 sampai 10 (menutup form dirty pada sesi yang kalah, S-08), langkah 16 (pemulihan sesi), langkah 18 (mengatur saldo awal), langkah 22 (menunggu Convert sesi A selesai sebelum pindah tab, 8b.8), langkah 11, 19, 23, dan 25 (Search dan pindah tab dan Search untuk menemukan baris target, R-16; trial Converted diasersi di tab `History`), dan langkah 39 (menutup konteks kedua).
- Temuan untuk QA:
  - TC-AC-CS-516, 517, 577 (dan 483, 515) ditandai `Manual Only — (d) dua sesi paralel` di kolom Automation; spec mengotomasikannya dengan sinkronisasi klik oleh runner (kemampuan disediakan tim FE/BE).
  - TC-AC-CS-517 Expected a dan b adalah dua cabang urutan commit yang tidak dapat dipaksa pada satu term; langkah 15 memakai satu `Verifikasi` yang mengasersi tepat salah satu cabang. Perlu keputusan QA apakah urutan commit dikendalikan lewat intercept.
  - TC-AC-CS-516 dan 517 menyebut "dua sesi" tanpa menyebut akun sesi B; spec memakai Principal kedua yang disediakan tim FE (S-11).
  - TC-AC-CS-577 tidak menyebut apakah kotak Search tetap berisi sesudah pindah tab `History` dan `Current`; spec menulis "ganti isi kotak search dengan" pada langkah sesudah pindah tab (bagian 8b butir 9) dengan asumsi kotak tetap berisi, dan ketik Search biasa sesudah klik menu.
  - TC-AC-CS-516 Expected c ("tidak ada Reserve ganda") tidak menyebut surface; spec memakai pembacaan Wallet lewat fixture.
  - TC-AC-CS-577 Expected d berisi lima klausa negatif yang digabung dalam satu `Verifikasi` daftar yang disebut utuh (S-01, daftar elemen yang sama-sama tidak ada).
