---
id: TC-GS-NLU-E2E-073-auto-deactivate-temporary-user-oleh-sistem-dan-cascade-purge
title: "Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-192
  - TC-GS-NLU-409
  - TC-GS-NLU-410
coverage:
  web: automated
---

# Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto

## Prerequisites

- Mode: FE+BE (backend nyata). Spec menguji job latar (Cascade Purge dan Auto-Deactivate) dengan jam server dan polling worker.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Foto Purge {runId}-073` (Active, memiliki foto aktif dan foto lama di Recycle Bin File Manager), `Tanpa Foto {runId}-073` (Active, tanpa foto), `Auto Satu {runId}-073` (Active, Temporary Until kemarin), `Auto Dua {runId}-073` (Active, Temporary Until hari ini).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanismenya): mengatur jam server absolut dan memulihkannya; menjalankan job Auto-Deactivate lewat fixture pergeseran jam; seeding foto aktif dan foto Recycle Bin untuk `Foto Purge {runId}-073`; membaca daftar berkas File Manager dan Recycle Bin.
- Jam: hanya jam server yang diatur (job dan batas hari dihitung di server; UI tidak menghitung dari jam browser). Jam diatur absolut dalam zona waktu client (`Asia/Jakarta`, Pre-setup No. 16): 00.01 hari ini untuk TC-409; 23.59 lalu 00.01 hari berikutnya pada hari Temporary Until untuk TC-410. Jam dipulihkan sebelum aksi membuka Activity Log atau System Log (S-09); hook `after` memulihkan jam bila belum.
- Polling worker commit: muat ulang halaman tiap 5 detik sampai hasil job tampil, batas tunggu 2 menit (bagian 6).
- State global yang diubah: jam server (dipulihkan seperti di atas); suite berjalan serial. Entri audit trail bersifat permanen: asersi memakai nama bersuffix unik dan baseline jumlah.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).

## Test Steps


### TC-GS-NLU-192: Delete menghapus permanen seluruh foto secara asinkron (Cascade Purge)

1. Ketik Search `Foto Purge {runId}-073`, tekan Enter
2. Klik `⋯` pada baris `Foto Purge {runId}-073` > `Delete`
3. Klik `[Delete]`
4. Verifikasi toast sukses: `Success, non-login user has been deleted.`
5. Buka File Manager
6. Muat ulang File Manager tiap 5 detik sampai foto aktif dan foto di Recycle Bin milik user tidak ada (batas tunggu 2 menit)
7. Verifikasi daftar File Manager tampil dengan sedikitnya satu berkas lain
8. Verifikasi foto aktif milik `Foto Purge {runId}-073` terhapus permanen dari File Manager
9. Verifikasi foto lama milik `Foto Purge {runId}-073` di Recycle Bin terhapus permanen
10. Catat jumlah berkas File Manager dan Recycle Bin sebagai baseline
11. Kembali ke Global Settings > User > User List > sub-tab Non-Login User
12. Ketik Search `Tanpa Foto {runId}-073`, tekan Enter
13. Klik `⋯` pada baris `Tanpa Foto {runId}-073` > `Delete`
14. Klik `[Delete]`
15. Verifikasi toast sukses: `Success, non-login user has been deleted.`
16. Buka File Manager
17. Verifikasi jumlah berkas File Manager dan Recycle Bin sama dengan baseline (Delete tanpa foto tidak berefek di File Manager)

### TC-GS-NLU-409: Log Auto-Deactivate oleh sistem

18. Buka Detail Login User aktor (Siti Nurhaliza) > tab `System Log`, catat jumlah entri sebagai baseline, lalu kembali ke List Non-Login User
19. Ketik Search `Auto Satu {runId}-073`, tekan Enter
20. Atur jam server absolut ke 00.01 hari ini zona waktu client
21. Jalankan job Auto-Deactivate lewat fixture pergeseran jam
22. Pulihkan jam server
23. Muat ulang halaman tiap 5 detik sampai switch Active baris `Auto Satu {runId}-073` OFF (batas tunggu 2 menit)
24. Verifikasi switch Active baris `Auto Satu {runId}-073` menjadi OFF
25. Verifikasi tidak ada dialog konfirmasi yang tampil
26. Klik teks Name `Auto Satu {runId}-073` lalu klik tab `Changelog`
27. Verifikasi entri Changelog: Action `Auto-Deactivate`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `System`
28. Buka Global Settings > Activity Log
29. Verifikasi Activity Log memuat entri `Auto-Deactivate` dengan aktor `System` untuk `Auto Satu {runId}-073`
30. Buka Detail Login User aktor (Siti Nurhaliza) > tab `System Log`
31. Verifikasi jumlah entri System Log sama dengan baseline (tidak ada entri dari Auto-Deactivate karena tidak ada user aktor)

### TC-GS-NLU-410: Auto-Deactivate memperlakukan Temporary Until sebagai hari aktif terakhir

32. Kembali ke List Non-Login User
33. Ketik Search `Auto Dua {runId}-073`, tekan Enter
34. Atur jam server absolut ke 23.59 hari Temporary Until zona waktu client
35. Jalankan job Auto-Deactivate lewat fixture pergeseran jam
36. Muat ulang halaman
37. Verifikasi switch Active baris `Auto Dua {runId}-073` masih ON
38. Atur jam server absolut ke 00.01 hari berikutnya zona waktu client
39. Jalankan job Auto-Deactivate lewat fixture pergeseran jam
40. Pulihkan jam server
41. Muat ulang halaman tiap 5 detik sampai switch Active baris `Auto Dua {runId}-073` OFF (batas tunggu 2 menit)
42. Verifikasi switch Active baris `Auto Dua {runId}-073` menjadi OFF

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 10, 11, 18, 22, 26, 32, 40.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 12, 19, 33.
- P-1: asersi "tidak ada entri System Log" pada TC-409 (Expected d) bergantung pada state berat yang baru dibangun langkah sebelumnya (job Auto-Deactivate dengan jam server digeser); asersi ditulis sebagai jumlah entri terhadap baseline (S-12) di spec ini dengan anchor entri Changelog dan Activity Log yang tampil lebih dulu.
- Cascade Purge TC-192 dan Auto-Deactivate TC-409 dan TC-410 adalah job latar di server; spec ini memakai harness yang sama (polling worker commit dan jam server).
- Temuan untuk QA:
  - TC-192 Expected b menyebut "tanpa log jumlah foto" tanpa menyebut surface; klausa itu tidak diasersi.
  - TC-192 tidak menyebut cara mengidentifikasi foto milik user di File Manager atau Recycle Bin; spec memakai kemampuan baca File Manager yang disediakan tim FE/BE.
  - TC-409 dan TC-410 diberi Automation `Manual Only` di sumber karena job terjadwal tidak dapat dipicu dari klien; tetap ditulis sebagai spec dengan kemampuan menjalankan job disediakan tim FE/BE.
  - TC-410 Langkah Uji 1 mengamati switch pada pukul 23.59 tanpa menyebut pemicu job pada saat itu; spec menjalankan job pada 23.59 untuk membuktikan user masih Active.
  - TC-409 Expected d (tidak ada entri System Log) adalah klausa absence; diasersi sebagai selisih jumlah terhadap baseline.
- Alasan di atas 35 langkah: semua blok kelas d (job latar server dengan jam server atau polling worker), memakai record milik sendiri, dan berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
