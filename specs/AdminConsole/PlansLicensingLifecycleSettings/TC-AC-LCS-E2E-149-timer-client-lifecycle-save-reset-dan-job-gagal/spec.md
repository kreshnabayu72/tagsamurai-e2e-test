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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan memantau job recalculation, menunda dan melepaskan job, memaksa job per-Save gagal, dan memicu scheduled daily sweep, serta membaca jumlah email dan notifikasi lifecycle per penerima (baseline sebelum sweep kedua).
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
8. Ketik Search `PT Maju Jaya`, tekan Enter
9. Verifikasi status subscription PT Maju Jaya tetap `Grace`
10. Verifikasi timer subscription PT Maju Jaya tidak berubah

### TC-AC-LCS-525: Reset to Default Client Lifecycle dari nilai non-default menghitung ulang timer; Reset saat sudah default tidak

11. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Grace Period Duration tersimpan `20` dan subscription PT Maju Jaya berstatus `Grace` pada hari ke-25 masa tenggang, lalu buka Plans & Licensing > Lifecycle Settings
12. Klik tab `Client Lifecycle`
13. Klik `[Reset to Default]`
14. Tunggu aksi selesai (nilai default tersimpan)
15. Picu eksekusi job lifecycle lewat Fixture BE
16. Buka Allocation > Client Subscription > List Subscriptions
17. Ketik Search `PT Maju Jaya`, tekan Enter
18. Verifikasi status subscription PT Maju Jaya tetap `Grace` (batas baru 30 hari; dengan nilai `20` seharusnya sudah `Archive`)
19. Catat jumlah job recalculation yang tercatat lewat Fixture BE sebagai baseline
20. Buka Plans & Licensing > Lifecycle Settings, klik tab `Client Lifecycle`
21. Klik `[Reset to Default]` lagi saat seluruh nilai sudah default
22. Verifikasi toast sukses "Success, client lifecycle settings have been reset to default." tampil
23. Verifikasi jumlah job recalculation lewat Fixture BE tidak bertambah dari baseline (selisih 0)

### TC-AC-LCS-526: Save berikutnya saat recalculation sebelumnya masih berjalan: job sebelumnya digantikan

24. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang dan recalculation job ditunda lewat fixture BE agar masih berjalan saat Save kedua, lalu buka Plans & Licensing > Lifecycle Settings
25. Klik tab `Client Lifecycle`
26. Ubah Grace Period Duration dari `30` menjadi `15`
27. Klik `[Save]` dan tunggu toast sukses
28. Sebelum job pertama selesai, ubah Grace Period Duration menjadi `40`
29. Klik `[Save]` dan tunggu toast sukses
30. Lepaskan penundaan job lewat Fixture BE dan tunggu job selesai lewat kueri status job (batas tunggu 2 menit), lalu picu eksekusi job lifecycle
31. Buka Allocation > Client Subscription > List Subscriptions
32. Ketik Search `PT Maju Jaya`, tekan Enter
33. Verifikasi status subscription PT Maju Jaya tetap `Grace` (job mengikuti nilai tersimpan terakhir `40`)

### TC-AC-LCS-527: Job recalculation per-Save gagal: scheduled daily sweep menghitung ulang dan idempotent

34. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription PT Maju Jaya berstatus `Grace` pada hari ke-20 masa tenggang dan job recalculation per-Save dipaksa gagal, lalu buka Plans & Licensing > Lifecycle Settings
35. Klik tab `Client Lifecycle`
36. Ubah Grace Period Duration dari `30` menjadi `15`
37. Klik `[Save]` dan tunggu toast sukses
38. Picu eksekusi job lifecycle lewat Fixture BE
39. Buka Allocation > Client Subscription > List Subscriptions
40. Ketik Search `PT Maju Jaya`, tekan Enter
41. Verifikasi status subscription PT Maju Jaya tetap `Grace` (recalculation per-Save gagal)
42. Picu scheduled daily sweep lewat Fixture BE
43. Muat ulang halaman List Subscriptions
44. Ketik Search `PT Maju Jaya`, tekan Enter
45. Verifikasi status subscription PT Maju Jaya `Archive`
46. Catat jumlah email dan notifikasi lifecycle subscription PT Maju Jaya per penerima lewat Fixture BE sebagai baseline
47. Picu scheduled daily sweep sekali lagi lewat Fixture BE
48. Muat ulang halaman List Subscriptions
49. Ketik Search `PT Maju Jaya`, tekan Enter
50. Verifikasi status subscription PT Maju Jaya tetap `Archive`
51. Verifikasi jumlah email dan notifikasi lifecycle per penerima lewat Fixture BE tidak bertambah dari baseline (selisih 0)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Klik tab", "Picu eksekusi job ...", "Muat ulang halaman List Subscriptions", "Ketik Search `PT Maju Jaya`, tekan Enter" sebelum tiap `Verifikasi` status baris (langkah 8, 17, 32, 40, 44, 49; R-16, bagian 8b butir 13, R-23), "Lepaskan penundaan job ..." (idiom polling kueri status job, batas 2 menit), dan "Pulihkan ..." antar TC, yang pada langkah 11, 24, 34 diakhiri "lalu buka Plans & Licensing > Lifecycle Settings" (S-03, S-07, S-09, R-10); "Buka Plans & Licensing > Lifecycle Settings, klik tab `Client Lifecycle`" (langkah 20) mengembalikan layar dari List Subscriptions sebelum `[Reset to Default]` kedua (S-07, S-14); "Tunggu aksi selesai" (langkah 14) sesudah `[Reset to Default]` yang hasilnya tidak diasersi dan diikuti pemicu job (bagian 8b butir 8); "Catat jumlah job recalculation ... sebagai baseline" (langkah 19) sebelum `[Reset to Default]` kedua agar absence job baru memakai selisih 0 (S-12); "Catat jumlah email dan notifikasi lifecycle ... per penerima ... sebagai baseline" (langkah 46) sebelum sweep kedua agar absence duplikat memakai selisih 0 (bagian 8b butir 10).
- Temuan untuk QA: Expected TC-AC-LCS-525 butir b hanya menyebut job recalculation baru yang tidak tercatat; spec tidak menambah baseline notifikasi karena TC tidak mengasersi notifikasi pada langkah itu. TC-AC-LCS-527 butir c menyebut "email atau notifikasi duplikat" tanpa menentukan penerima; spec membaca jumlah per penerima lewat Fixture BE dan penerima perlu dilengkapi di TC.
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (state subscription diseed, nilai tab diubah atau direset, job dipicu, status dibaca), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-525 mengklik `[Reset to Default]` lagi saat seluruh nilai sudah default tanpa menyebut keadaan tombol; TC-AC-LCS-524 dan 525 mengasersi fixture BE yang memantau job tanpa mendefinisikan kemampuannya (S-13). Pengamatan "timer tidak berubah" (TC-AC-LCS-524) tidak punya elemen UI di TC; spec menulisnya sebagai `Verifikasi` timer subscription tanpa langkah observasi tambahan (S-02).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
