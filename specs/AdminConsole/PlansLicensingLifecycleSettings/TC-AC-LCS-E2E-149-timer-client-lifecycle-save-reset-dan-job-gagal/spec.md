---
id: TC-AC-LCS-E2E-149-timer-client-lifecycle-save-reset-dan-job-gagal
title: "Recalculation Timer Client Lifecycle: Save Post-Purge Saja, Reset, Save Berurutan, dan Job Per-Save Gagal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-524
  - TC-AC-LCS-525
  - TC-AC-LCS-526
  - TC-AC-LCS-527
coverage:
  web: automated
---

# Recalculation Timer Client Lifecycle: Save Post-Purge Saja, Reset, Save Berurutan, dan Job Per-Save Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) berstatus `Grace` pada hari masa tenggang yang diatur per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan memantau job recalculation, menunda dan melepaskan job, memaksa job per-Save gagal, dan memicu scheduled daily sweep.
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-524: Save hanya field Post-Purge Retention tidak memicu recalculation timer

1. Atur lewat Fixture BE: subscription PT Maju Jaya berstatus `Grace` pada hari ke-10 masa tenggang dan job recalculation terpantau lewat fixture BE (tidak ada job dikirim)
2. Klik tab `Client Lifecycle`
3. Ubah Post-Purge Retention dari `730` menjadi `800`
4. Klik `[Save]` dan tunggu toast sukses
5. Picu eksekusi job lifecycle lewat Fixture BE
6. Verifikasi fixture BE mencatat tidak ada job recalculation untuk Save ini
7. Buka Allocation > Client Subscription > List Subscriptions
8. Verifikasi status subscription PT Maju Jaya tetap `Grace`
9. Verifikasi timer subscription PT Maju Jaya tidak berubah

### TC-AC-LCS-525: Reset to Default Client Lifecycle dari nilai non-default menghitung ulang timer; Reset saat sudah default tidak

10. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Grace Period Duration tersimpan `20` dan subscription PT Maju Jaya berstatus `Grace` pada hari ke-25 masa tenggang, lalu muat ulang halaman Lifecycle Settings
11. Klik tab `Client Lifecycle`
12. Klik `[Reset to Default]`
13. Tunggu aksi selesai (nilai default tersimpan)
14. Picu eksekusi job lifecycle lewat Fixture BE
15. Buka Allocation > Client Subscription > List Subscriptions
16. Verifikasi status subscription PT Maju Jaya tetap `Grace` (batas baru 30 hari; dengan nilai `20` seharusnya sudah `Archive`)
17. Catat jumlah job recalculation yang tercatat lewat Fixture BE sebagai baseline
18. Klik `[Reset to Default]` lagi saat seluruh nilai sudah default
19. Verifikasi toast sukses "Success, client lifecycle settings have been reset to default." tampil
20. Verifikasi jumlah job recalculation lewat Fixture BE tidak bertambah dari baseline (selisih 0)

### TC-AC-LCS-526: Save berikutnya saat recalculation sebelumnya masih berjalan: job sebelumnya digantikan

21. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang dan recalculation job ditunda lewat fixture BE agar masih berjalan saat Save kedua
22. Klik tab `Client Lifecycle`
23. Ubah Grace Period Duration dari `30` menjadi `15`
24. Klik `[Save]` dan tunggu toast sukses
25. Sebelum job pertama selesai, ubah Grace Period Duration menjadi `40`
26. Klik `[Save]` dan tunggu toast sukses
27. Lepaskan penundaan job lewat Fixture BE dan tunggu job selesai lewat kueri status job (batas tunggu 2 menit), lalu picu eksekusi job lifecycle
28. Buka Allocation > Client Subscription > List Subscriptions
29. Verifikasi status subscription PT Maju Jaya tetap `Grace` (job mengikuti nilai tersimpan terakhir `40`)

### TC-AC-LCS-527: Job recalculation per-Save gagal: scheduled daily sweep menghitung ulang dan idempotent

30. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang dan job recalculation per-Save dipaksa gagal
31. Klik tab `Client Lifecycle`
32. Ubah Grace Period Duration dari `30` menjadi `15`
33. Klik `[Save]` dan tunggu toast sukses
34. Picu eksekusi job lifecycle lewat Fixture BE
35. Buka Allocation > Client Subscription > List Subscriptions
36. Verifikasi status subscription PT Maju Jaya tetap `Grace` (recalculation per-Save gagal)
37. Picu scheduled daily sweep lewat Fixture BE
38. Muat ulang halaman List Subscriptions
39. Verifikasi status subscription PT Maju Jaya `Archive`
40. Picu scheduled daily sweep sekali lagi lewat Fixture BE
41. Muat ulang halaman List Subscriptions
42. Verifikasi status subscription PT Maju Jaya tetap `Archive`
43. Verifikasi tidak ada email atau notifikasi duplikat

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Klik tab", "Picu eksekusi job ...", "Muat ulang halaman List Subscriptions", "Lepaskan penundaan job ..." (idiom polling kueri status job, batas 2 menit), dan "Pulihkan ..." antar TC (S-03, S-09, R-10); "Tunggu aksi selesai" (langkah 13) sesudah `[Reset to Default]` yang hasilnya tidak diasersi dan diikuti pemicu job (bagian 8b butir 8); "Catat jumlah job recalculation ... sebagai baseline" (langkah 17) sebelum `[Reset to Default]` kedua agar absence job baru memakai selisih 0 (S-12).
- Temuan untuk QA: Expected TC-AC-LCS-525 butir b hanya menyebut job recalculation baru yang tidak tercatat; spec tidak menambah baseline notifikasi karena TC tidak mengasersi notifikasi pada langkah itu.
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (state subscription diseed, nilai tab diubah atau direset, job dipicu, status dibaca), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-525 mengklik `[Reset to Default]` lagi saat seluruh nilai sudah default tanpa menyebut keadaan tombol; TC-AC-LCS-524 dan 525 mengasersi fixture BE yang memantau job tanpa mendefinisikan kemampuannya (S-13). Pengamatan "timer tidak berubah" (TC-AC-LCS-524) tidak punya elemen UI di TC; spec menulisnya sebagai `Verifikasi` timer subscription tanpa langkah observasi tambahan (S-02).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
