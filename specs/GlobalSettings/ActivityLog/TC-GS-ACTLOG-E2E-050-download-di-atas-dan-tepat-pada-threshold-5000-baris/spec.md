---
id: TC-GS-ACTLOG-E2E-050-download-di-atas-dan-tepat-pada-threshold-5000-baris
title: "Download di Atas dan Tepat pada Threshold 5.000 Baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-136
  - TC-GS-ACTLOG-137
coverage:
  web: automated
---

# Download di Atas dan Tepat pada Threshold 5.000 Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Client Volume khusus spec ini (`Fixture.activityLog.clientVolume`, disediakan tim FE/BE; email ditetapkan tim FE); password dari `Spectra.env.GS_CLIENTVOL_TC_PASSWORD`. Login sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Entitas ini dipakai khusus spec ini karena seed volume tidak dapat dihapus dan akan mengubah jumlah baris di spec lain. Spec tidak mengganti akun.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client Volume dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE).
- Data volume (kelas volume data, prinsip 13e), disediakan lewat seed BE di entitas Client Volume:
  - Untuk TC-GS-ACTLOG-136: Tab Session dan Tab User Action masing-masing memuat 5.001 baris atau lebih.
  - Untuk TC-GS-ACTLOG-137: pada Tab Session dan Tab User Action, tersedia saringan (Search atau Filter) yang menghasilkan tepat 5.000 baris dan saringan yang menghasilkan tepat 5.001 baris. Bentuk saringan ditentukan tim FE/BE karena TC tidak menyebutnya; langkah menulis "saringan 5.000 baris" dan "saringan 5.001 baris".
  - Pembersihan: baris log tidak dapat dihapus lewat UI atau API modul ini; entitas Client Volume direset oleh tim BE di luar spec.
- Kemampuan teknis (disediakan tim FE/BE):
  - Kelas binary buffer (prinsip 13f): menangkap berkas unduhan browser ke direktori bersih per unduhan dan memeriksa nama berkas. Berkas unduhan dihapus di hook `after`.
  - Mengamati loading screen secara tepat waktu: muncul atau tidak muncul antara klik pilihan format dan berkas terunduh, memakai auto-wait tanpa intercept.
  - Mengamati ada atau tidaknya toast dan notifikasi in-app.
  - Penyetelan dan pemulihan flag Guided Tooltip untuk akun Client Volume (lihat Guided Tooltip di atas).
- State global yang diubah dan dipulihkan: Search dan Filter kedua tab (dibersihkan di langkah 21 dan 31).
- Suite serial (`parallel: false`).
- Hook `beforeEach`: kembali ke layar Global Settings > Activity Log > Session.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-136: Download melewati threshold 5.000 baris menampilkan loading screen lalu berkas terunduh, kedua tab

2. Klik icon Download, lalu klik `Download as CSV`
3. Verifikasi loading screen tampil sampai berkas siap
4. Verifikasi tidak ada toast sukses
5. Verifikasi tidak ada notifikasi in-app
6. Verifikasi berkas `Activity-Log-Session.csv` langsung terunduh
7. Klik tab "User Action", klik icon Download, lalu klik `Download as XLSX`
8. Verifikasi loading screen tampil sampai berkas siap
9. Verifikasi tidak ada toast sukses
10. Verifikasi tidak ada notifikasi in-app
11. Verifikasi berkas `Activity-Log-User-Action.xlsx` langsung terunduh

### TC-GS-ACTLOG-137: Batas tepat 5.000 baris diunduh langsung dan 5.001 baris menampilkan loading screen, kedua tab

12. Klik tab "Session", lalu terapkan saringan 5.000 baris
13. Klik icon Download, lalu klik `Download as CSV`
14. Verifikasi tab Session dengan 5.000 baris: tidak ada loading screen
15. Verifikasi tab Session dengan 5.000 baris: tidak ada toast
16. Verifikasi tab Session dengan 5.000 baris: berkas `Activity-Log-Session.csv` langsung terunduh
17. Ganti saringan menjadi saringan 5.001 baris
18. Klik icon Download, lalu klik `Download as CSV`
19. Verifikasi tab Session dengan 5.001 baris: loading screen tampil sampai berkas siap
20. Verifikasi tab Session dengan 5.001 baris: berkas `Activity-Log-Session.csv` terunduh
21. Bersihkan saringan Tab Session
22. Klik tab "User Action", lalu terapkan saringan 5.000 baris
23. Klik icon Download, lalu klik `Download as CSV`
24. Verifikasi tab User Action dengan 5.000 baris: tidak ada loading screen
25. Verifikasi tab User Action dengan 5.000 baris: tidak ada toast
26. Verifikasi tab User Action dengan 5.000 baris: berkas `Activity-Log-User-Action.csv` langsung terunduh
27. Ganti saringan menjadi saringan 5.001 baris
28. Klik icon Download, lalu klik `Download as CSV`
29. Verifikasi tab User Action dengan 5.001 baris: loading screen tampil sampai berkas siap
30. Verifikasi tab User Action dengan 5.001 baris: berkas `Activity-Log-User-Action.csv` terunduh
31. Bersihkan saringan Tab User Action

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`. Mode: FE+BE. Kelas volume data (prinsip 13e); kolom Automation kedua TC bernilai Manual Only di TC, tetapi itu bukan alasan keluar spec: kebutuhan teknisnya ada di `## Prerequisites`.
- Urutan TC dalam spec: 136 lalu 137 (tanpa saringan lebih dulu, lalu dengan saringan yang dibersihkan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab "Session" dan "User Action"; langkah 17 dan 27 (mengganti saringan dari 5.000 ke 5.001 baris); langkah 21 dan 31 (membersihkan saringan, S-09).
- Absence state sementara (bagian 8b butir 11 dan 5): loading screen dan toast diasersi segera setelah pemicu (klik pilihan format) dan sebelum asersi berkas terunduh (langkah 3 sampai 6, 8 sampai 11, 14 sampai 16, 24 sampai 26); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas.
- Format unduhan TC-GS-ACTLOG-137 pada Tab User Action: TC menulis "ulangi langkah 1", sehingga memakai `Download as CSV` seperti Tab Session.
- Pembagian TC lintas spec: TC-GS-ACTLOG-131 (unduhan di bawah atau sama dengan 5.000 baris tanpa toast) ada di spec 047; TC-GS-ACTLOG-132 di spec 049. Tidak ada TC yang terbelah.
- Temuan untuk QA:
  - TC-GS-ACTLOG-137: TC tidak menyebut cara menyaring hasil menjadi tepat 5.000 dan 5.001 baris; spec memakai saringan yang disediakan seed BE tanpa mengarang bentuknya (S-13).
  - TC-GS-ACTLOG-136 dan 137: TC tidak menyebut cara mengamati loading screen yang singkat; ditulis sebagai kemampuan teknis di Prerequisites.
  - TC-GS-ACTLOG-136 dan 137: kolom Automation bernilai Manual Only pada TC.
  - NC-03 di TC masih menulis respons antrean di openapi dan LLD sebagai temuan BE; PRD §4.3 S-07, openapi, dan LLD saat ini sejalan: loading screen sampai berkas siap, lalu langsung terunduh, tanpa respons antrean dan tanpa notifikasi in-app. Spec mengikuti Expected TC.
