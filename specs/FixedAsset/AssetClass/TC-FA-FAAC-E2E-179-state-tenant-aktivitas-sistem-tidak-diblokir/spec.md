---
id: TC-FA-FAAC-E2E-179-state-tenant-aktivitas-sistem-tidak-diblokir
title: "State Tenant: Job Sistem Penerapan Versi, Posting, dan Export Tidak Diblokir saat Client Suspended"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-327
  - TC-FA-FAAC-343
  - TC-FA-FAAC-611
coverage:
  web: automated
---

# State Tenant: Job Sistem Penerapan Versi, Posting, dan Export Tidak Diblokir saat Client Suspended

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- State global yang diubah spec: status client (`Active`, `Suspended`). Pelaku perubahan status tidak disebut TC, PRD, atau LLD; fixture BE untuk mengubah status entitas "disediakan tim FE/BE" (tanpa akun atau endpoint karangan). Status awal `Active` dicatat di hook `before`; hook `after` memulihkan status ke `Active` walau spec gagal di tengah.
- Data seed (disediakan fixture BE, idempotent): Asset Class `B-JOBS` dengan versi Scheduled yang jatuh tempo (TC-327); Asset Class `B-LOCK` dengan Last Posted Period `Mar 2026` dan belum punya Last Exported Period (TC-343, sesuai NC-16); Asset Class milik spec Class Code literal `B-JB3` dan Class Name `Job Class {runId}-179` dengan versi Scheduled yang jatuh tempo serta periode yang dapat diposting dan diekspor (TC-611; TC tidak menyebut kode dan data Asset Class-nya). Hook `before` menghapus sisa `B-JB3` dari run sebelumnya dan hook `after` menghapus `B-JB3` lewat fixture BE dan memulihkan `B-JOBS` dan `B-LOCK` ke keadaan seed.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): memicu job penerapan versi terjadwal, seed posting periode `Apr 2026`, seed export periode `Mar 2026`, dan job posting, export, serta penerapan versi pada client `Suspended` di lingkungan uji; membaca jumlah entri Changelog Asset Class per Class Code (audit trail permanen, asersi memakai selisih terhadap baseline, bukan angka absolut). Jam server dan jam browser tidak digeser.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

1. Catat baseline lewat kemampuan baca BE: jumlah entri Changelog Asset Class untuk `B-JOBS`, `B-LOCK`, dan `B-JB3`
2. Atur lewat fixture BE status client menjadi `Suspended`, lalu muat ulang halaman

### TC-FA-FAAC-327: Versi Scheduled tetap berlaku otomatis saat entitas Suspended

3. Picu job penerapan versi terjadwal untuk `B-JOBS` di lingkungan uji pada client `Suspended`

### TC-FA-FAAC-343: Update Last Posted dan Last Exported Period tidak diblokir saat entitas Suspended

4. Picu seed posting periode `Apr 2026` dan export periode `Mar 2026` untuk `B-LOCK` pada client `Suspended`

### TC-FA-FAAC-611: Job tanpa user aktor tidak diblokir saat entitas Suspended atau Expired

5. Picu job posting, export, dan penerapan versi untuk `B-JB3` pada client `Suspended`
6. Atur lewat fixture BE status client kembali menjadi `Active`, lalu muat ulang halaman

### Pengamatan hasil setelah entitas aktif kembali

7. Ketik Search `B-JOBS`, tekan Enter
8. Klik link Class Code `B-JOBS` di tabel
9. Verifikasi Detail `B-JOBS` terbuka
10. Verifikasi versi Scheduled `B-JOBS` berlaku pada Effective From: Alert versi Scheduled tidak tampil lagi di Detail
11. Klik breadcrumb `Asset Class`
12. Ganti isi kotak search dengan `B-LOCK`, tekan Enter
13. Klik link Class Code `B-LOCK` di tabel
14. Verifikasi Last Posted Period `Apr 2026`
15. Verifikasi Last Exported Period `Mar 2026`
16. Klik breadcrumb `Asset Class`
17. Klik icon `Changelog`
18. Ketik Search `B-JOBS` pada Modal Changelog, tekan Enter
19. Verifikasi jumlah entri Changelog `B-JOBS` bertambah satu dibanding baseline
20. Verifikasi entri L-03 teratas untuk `B-JOBS` memuat Modified By `System`
21. Ganti isi kotak search dengan `B-LOCK`, tekan Enter
22. Verifikasi entri L-10 dan L-11 tertulis untuk `B-LOCK`: jumlah entri bertambah dua dibanding baseline
23. Ganti isi kotak search dengan `B-JB3`, tekan Enter
24. Verifikasi entri L-10, L-11, dan L-03 tertulis untuk `B-JB3`: jumlah entri bertambah tiga dibanding baseline
25. Verifikasi entri L-10, L-11, dan L-03 untuk `B-JB3` memuat Modified By `System`
26. Tutup Modal Changelog
27. Klik `(←)` pada kotak Search

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan diubah dari urutan TC: ketiga pemicu job dijalankan dalam satu jendela `Suspended` (langkah 2 sampai 6), lalu hasilnya diamati sesudah client `Active`, supaya status client hanya berganti satu kali; tiap TC tetap memakai Asset Class dan baseline sendiri (langkah 1) dan diamati dengan Class Code-nya sendiri (S-10, S-12).
2. P-2: job sistem sebagai pemicu yang diizinkan di spec kelas h (job tanpa user aktor tidak diblokir; keputusan 2026-10-21): job adalah objek uji TC-611 dan TC-327; spec ini tidak mengasersi kegagalan job (TC-328 ada di spec job penerapan versi suite ini).
3. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 2 dan 6 (mengganti status client); langkah 7, 12, 18, 21, dan 23 memakai Search untuk menemukan baris atau entri target (R-16); langkah 11 dan 16 (kembali ke tabel); langkah 26 dan 27 (menutup Modal Changelog dan mengosongkan Search).
4. Cara baca Changelog (S-12, S-14): entri baru dibaca sesudah selisih jumlah entri terhadap baseline dibuktikan; entri hasil job dalam menit yang sama dibaca sebagai himpunan baris teratas sebanyak selisih tanpa mengandalkan urutan di antaranya.
5. Pengecualian kode seed literal (S-06/S-12): TC mewajibkan `B-JOBS` dan `B-LOCK`; dipakai apa adanya tanpa suffix `{runId}`; seed dipulihkan fixture BE di hook `after`. `B-JB3` milik spec ini (Class Name `Job Class {runId}-179`).
6. Temuan untuk QA: TC-327 tidak menyebut apa yang diamati di Detail `B-JOBS` selain "Versi berlaku pada Effective From"; spec mengamati Alert versi Scheduled tidak tampil lagi (didahului pembacaan Detail yang berhasil dimuat sebagai anchor). TC-343 mengklik link Class Code `B-LOCK` sebelum pemicu seed dan membuka Detail lagi sesudah entitas aktif; spec membuka Detail `B-LOCK` satu kali setelah entitas aktif kembali, karena muat ulang halaman saat status client berganti menutup Detail yang terbuka. TC-343 tidak menyebut Modified By entri L-10 dan L-11 dan TC-611 tidak menyebut kode serta data Asset Class; spec memakai `Modified By` `System` hanya untuk TC-611 dan TC-327. TC-611 menyebut "Suspended atau Expired" pada judul tetapi preconditionnya hanya Suspended; spec hanya menguji Suspended.
7. Class Code `B-JB3` ditulis literal dan `{runId}-179` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `B-JB3{runId}-179` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu.
