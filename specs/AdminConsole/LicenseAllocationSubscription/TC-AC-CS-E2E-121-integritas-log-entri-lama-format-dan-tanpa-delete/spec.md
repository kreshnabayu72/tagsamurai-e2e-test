---
id: TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete
title: "Integritas Log: Entri Lama, Format, dan Tanpa Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-466
  - TC-AC-CS-467
  - TC-AC-CS-468
  - TC-AC-CS-469
coverage:
  web: automated
---

# Integritas Log: Entri Lama, Format, dan Tanpa Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-121`). Tidak ada baris Pre-setup bersama yang ditulis spec ini; entri Changelog, Activity Log, dan System Log yang terbentuk adalah audit trail permanen dan tidak dihapus:
  1. TC-AC-CS-466: Client `Apotek Sehat Sentosa+{runId}-121` dengan pengajuan Waiting for Approval Duration `1` year(s) (setara `SUBS-20260819-00001`, #49); Subscription ID-nya dibaca lewat API seeding dan dipakai sebagai `{idPengajuan466}`.
  2. TC-AC-CS-467: Client `Client Tanpa Subscription+{runId}-121` tanpa term (setara #48), Client `Toko Persetujuan+{runId}-121` dengan pengajuan Waiting for Approval SAMS (setara #124), dan Client `Toko Persetujuan Dua+{runId}-121` dengan pengajuan Waiting for Approval FAMS (setara #126).
- Pelaku `Dewi A` (Group Manager Pre-setup #5, password `Spectra.env.AC_SUB_GM_PASSWORD`) dan `Eko S` (Total Control Distributor Pre-setup #9, password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`) hanya bertindak lewat sesi API dan tidak login lewat UI.
- Entri `Hendra W` dan `Fajar N` yang diamati TC-AC-CS-468 adalah milik spec ini: `Fajar N` dari Edit pada TC-AC-CS-466 (sesi API dan UI), `Hendra W` dari pemicu sesi API Hendra W pada blok TC-AC-CS-468 (kemampuan sesi API disediakan tim BE/FE); entri seed #84 tidak dipakai untuk asersi.

## Test Steps

### TC-AC-CS-466: Entri log lama tidak berubah setelah record diubah lagi

1. Pemicu (sesi API): simpan Edit Duration `1` menjadi `2` pada pengajuan `{idPengajuan466}` hingga perubahan tersimpan (dipakai sebagai precondition TC, tidak diasersi)
2. Ketik Search `{idPengajuan466}`, tekan Enter
3. Klik ikon `⋯` pada baris `{idPengajuan466}`, pilih `Edit`, ubah Duration `2` menjadi `3`, lalu klik `[Save]`
4. Tunggu hingga dialog Edit tertutup dan perubahan Duration `3` tersimpan
5. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa+{runId}-121`, tekan Enter, dan cari entri Action `Edit (Duration, mode New/Renewal)` Field `Duration` untuk term itu
6. Verifikasi entri pertama tetap menampilkan Old `1 year(s)` dan New `2 year(s)`
7. Verifikasi entri kedua menampilkan Old `2 year(s)` dan New `3 year(s)`
8. Verifikasi entri lama tidak ter-overwrite oleh nilai terbaru
9. Ganti akun: klik Logout dari akun sebelumnya
10. Login sebagai `Hendra Wijaya` (`totalControlSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_TC_PASSWORD`)

### TC-AC-CS-467: Activity Log memakai Action, Field, Old, dan New yang identik dengan Changelog

11. Pemicu (sesi API Dewi A): tambah Subscription SAMS plan Growth untuk Client `Client Tanpa Subscription+{runId}-121` hingga perubahan tersimpan
12. Pemicu (sesi API Eko S): Approve pengajuan Client `Toko Persetujuan+{runId}-121` (SAMS) dan Reject pengajuan Client `Toko Persetujuan Dua+{runId}-121` (FAMS) sebagai approver hingga perubahan tersimpan
13. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `Client Tanpa Subscription+{runId}-121`, tekan Enter, dan cari entri Action `Add Subscription`
14. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
15. Verifikasi Action, Field, Old Value, dan New Value entri `Add Subscription` identik pada Changelog dan Activity Log
16. Verifikasi Activity Log menambah kolom Object bernilai `Client Subscription` dan Name sama dengan kolom Client — Product
17. Verifikasi Modified By Activity Log adalah aktor (`Dewi A`) untuk Add Subscription
18. Verifikasi Modified By Activity Log adalah approver (`Eko S`) untuk Approve dan Reject
19. Verifikasi entri Approve dan Reject tampil di Activity Log
20. Buka Detail user Eko S, tab System Log, dan cari entri Approve dan Reject
21. Verifikasi Approve dan Reject ada di System Log approver
22. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `+{runId}-121`, tekan Enter
23. Verifikasi tabel Changelog menampilkan sedikitnya satu entri lain (anchor positif)
24. Verifikasi tidak ada entri Approve dan Reject di Changelog

### TC-AC-CS-468: Modified By pada log berformat First Name dan inisial Last Name

25. Pemicu (sesi API Hendra W): simpan Edit Duration `3` menjadi `4` pada pengajuan `{idPengajuan466}` hingga perubahan tersimpan
26. Buka menu Allocation > Client Subscription, buka modal Changelog, ketik Search `Apotek Sehat Sentosa+{runId}-121`, tekan Enter, dan amati kolom Modified By entri `Hendra W` dan `Fajar N` milik spec ini
27. Verifikasi tabel Changelog menampilkan sedikitnya satu entri
28. Verifikasi nama tampil `Hendra W` dan `Fajar N` sebagai plain text, bukan badge dan bukan nama lengkap, pada Changelog
29. Arahkan kursor ke Modified By `Hendra W`
30. Verifikasi hover menampilkan nama lengkap pada modal Changelog (`Hendra Wijaya`)
31. Buka Admin Console > Activity Log, saring Object `Client Subscription`, cari entri Name `Apotek Sehat Sentosa+{runId}-121`, dan amati kolom nama pelaku
32. Verifikasi tabel Activity Log menampilkan sedikitnya satu entri
33. Verifikasi nama tampil `Hendra W` dan `Fajar N` sebagai plain text, bukan badge dan bukan nama lengkap, pada Activity Log
34. Buka Detail user Hendra W, tab System Log, cari entri Client `Apotek Sehat Sentosa+{runId}-121`, dan amati kolom nama pelaku
35. Verifikasi tabel System Log menampilkan sedikitnya satu entri
36. Verifikasi nama tampil `Hendra W` sebagai plain text, bukan badge dan bukan nama lengkap, pada System Log

### TC-AC-CS-469: Tidak ada Action Delete di modul ini

37. Buka menu Allocation > Client Subscription, buka modal Changelog, buka Filter Panel, lalu buka dropdown Action
38. Verifikasi opsi Action memuat `Cancel`, `Cancel Request`, dan `Timeout Auto-Cancel`
39. Verifikasi opsi Action tidak memuat `Delete`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-466 (Create-Only) lebih dulu, lalu TC-AC-CS-467, 468, dan 469 (Principal) sesudah ganti akun, agar ganti akun hanya satu kali (S-10).
- S-05 dan P-1: asersi absence Approve dan Reject di Changelog milik TC-AC-CS-467 bergantung pada Approve dan Reject yang baru dipicu pada langkah sebelumnya di spec ini (state berat), sehingga tetap di spec ini dengan baseline dan anchor positif.
- Alasan spec lebih dari sekitar 35 langkah: seluruh blok satu topik (integritas isi entri log lama dan format pada Changelog, Activity Log, dan System Log) dengan pola pembacaan log yang sama dan seed milik spec; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-AC-CS-468: Hendra W melakukan satu aksi terlacak pada seed milik spec (pemicu sesi API sebelum pengamatan), dan pengamatan di Changelog, Activity Log, serta System Log dipersempit ke entri `Apotek Sehat Sentosa+{runId}-121` dengan Verifikasi anchor lebih dulu; precondition TC hanya meminta entri kedua user ada.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris pengajuan target (langkah 2), langkah membuka kembali menu Allocation > Client Subscription sesudah Activity Log atau System Log dan entri target (R-16), langkah ganti akun (Logout lalu login), dan langkah membuka dropdown Action pada Filter Panel.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-467 Expected c menyebut Modified By `System` untuk job; TC tidak memberi pemicu job pada Langkah Uji, sehingga klausa itu tidak diasersi di spec ini dan teruji di spec 113 (Modified By `System` pada Changelog dan Activity Log).
  - TC-AC-CS-467 Expected d menyebut Action, Field, Old, dan New Approve dan Reject "sesuai §8.3" tanpa nilai konkret di TC; spec hanya memverifikasi entri Approve dan Reject tampil di Activity Log (langkah 19) dan di System Log (langkah 21). Nilai Field, Old, dan New perlu ditulis TC.
  - TC-AC-CS-467 Expected d (Approve dan Reject "bukan di Changelog") adalah asersi absence tanpa langkah observasi di Langkah Uji; spec menulis `Verifikasi` dengan anchor entri lain di Changelog dan baseline, sedangkan spec absence 119 memuat Approve dan Reject untuk TC-AC-CS-442, 443, dan 617 (S-05).
  - TC-AC-CS-468 butir Langkah Uji ke-1 membandingkan tiga surface tanpa menyebut entri target di Activity Log dan System Log; spec memakai entri `Hendra W` dan `Fajar N` yang tampil.
