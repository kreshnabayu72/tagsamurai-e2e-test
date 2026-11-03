---
id: TC-FA-FAAM-E2E-224-import-kuota-paket-dan-penyemaian-policy
title: "Import: Ditolak Kuota Paket Growth dan Penyemaian Policy Transaksi ke Registrasi Aset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-606
  - TC-FA-FAAM-741
coverage:
  web: automated
---

# Import: Ditolak Kuota Paket Growth dan Penyemaian Policy Transaksi ke Registrasi Aset

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor pertama: Import Data `importData_automated_{namaCompany}@qwertysystem.net` pada client utama (Tabel Data Uji Pre-setup No. 9 dan No. 28c; `Spectra.env.FA_IMPORT_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor lain (ganti akun atau ganti client eksplisit): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client utama (Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`); Total Control dan Import Data pada client Growth `AutoGrowth50` (Pre-setup No. 16g; email tidak tertulis di Pre-setup TC dan disediakan tim FE; `Spectra.env.FA_GROWTH_TC_PASSWORD` dan `Spectra.env.FA_GROWTH_IMPORT_PASSWORD`, nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo). Password tidak ditulis di spec atau fixture.
- Env var: `FA_IMPORT_PASSWORD`, `FA_TC_PASSWORD`, `FA_GROWTH_TC_PASSWORD`, `FA_GROWTH_IMPORT_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 16g (client `AutoGrowth50`, plan Growth, 50 Asset Name tanpa Category Locked, kuota Growth 50; Import tersedia pada plan Growth), No. 28c (client utama).
- Data Dinamis: `Imported Policy Item 741 {runId}-224` (Tabel Data Uji Dinamis No. 107; dibuat lewat Import oleh aktor Import Data pada TC-FA-FAAM-741) dan `Blocked Import Item {runId}-224` (baris impor yang ditolak pada TC-FA-FAAM-606). Berkas impor satu baris disediakan tim FE (TC tidak menyebut format berkas).
- Kemampuan teknis: modul Import tab Asset Name (impor sampai batch ter-commit dan status baris); polling worker commit (muat ulang tiap 5 detik, batas 60 detik; bagian 6 konvensi); Modal Changelog dan Search di dalamnya; client Growth `AutoGrowth50`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Imported Policy Item 741 {runId}-224` pada client utama lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-741: login sebagai Import Data pada client utama dan berada di modul Import tab Asset Name. Precondition TC-FA-FAAM-606: client Growth berisi 50 Asset Name dan aktor Total Control tersedia untuk pengamatan.

## Test Steps

### TC-FA-FAAM-741: Asset Name hasil Import menyemai policy transaksi dan tersedia di dropdown Registrasi Aset

1. Buka modul Import tab Asset Name
2. Impor satu baris Asset Name `Imported Policy Item 741 {runId}-224` sampai batch ter-commit
3. Tunggu aksi selesai
4. Logout lalu login sebagai Total Control
5. Buka Registrasi Aset
6. Buka dropdown Asset Name
7. Ketik di kotak dropdown `Imported Policy Item 741 {runId}-224`
8. Muat ulang Registrasi Aset dan ulangi langkah 6 dan 7 tiap 5 detik sampai opsi muncul, batas 60 detik
9. Verifikasi `Imported Policy Item 741 {runId}-224` ada di dropdown Registrasi Aset setelah batch ter-commit
10. Buka FAMS > Settings > Asset Transactional Policy
11. Ketik Search `Imported Policy Item 741 {runId}-224`, tekan Enter
12. Verifikasi baris policy `Imported Policy Item 741 {runId}-224` memuat Borrow `On`, Assign `On`, Transfer `On`, Self Service Borrow `Off`
13. Buka Fixed Asset > Settings > Asset Master > Asset Name
14. Klik icon Changelog
15. Ketik Search `Imported Policy Item 741 {runId}-224`, tekan Enter
16. Verifikasi Changelog memuat satu baris Create untuk `Imported Policy Item 741 {runId}-224` tanpa entri untuk penyemaian policy
17. Tutup Modal Changelog

### TC-FA-FAAM-606: Create lewat Import ditolak saat kuota Asset Name paket Growth tercapai

18. Logout lalu login sebagai Total Control pada client Growth `AutoGrowth50`
19. Buka Fixed Asset > Settings > Asset Master > Asset Name
20. Logout lalu login sebagai Import Data pada client Growth `AutoGrowth50`
21. Buka modul Import tab Asset Name
22. Impor satu baris Asset Name baru `Blocked Import Item {runId}-224` sampai batch ter-commit
23. Verifikasi baris `Blocked Import Item {runId}-224` berstatus `error`
24. Verifikasi pesan baris `This would exceed your plan's asset name limit. Upgrade to add more.`
25. Tunggu aksi selesai
26. Logout lalu login sebagai Total Control pada client Growth `AutoGrowth50`
27. Buka Fixed Asset > Settings > Asset Master > Asset Name dan muat ulang tab Asset Name
28. Verifikasi tab Asset Name berisi 50 baris (jumlah dari seeding Pre-setup No. 16g)
29. Ketik Search `Blocked Import Item {runId}-224`, tekan Enter
30. Verifikasi empty state `No results found`, sehingga `Blocked Import Item {runId}-224` tidak ada
31. Klik icon Changelog
32. Ketik Search `Blocked Import Item {runId}-224`, tekan Enter
33. Verifikasi empty state `No results found` pada Changelog (tanpa entri log untuk `Blocked Import Item {runId}-224`)

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 21 (membuka modul Import), langkah 3 dan 25 (menunggu Import selesai sebelum ganti akun), langkah 5, 6, 7, 10, 13, 19, 27 (navigasi), langkah 8 (polling worker commit), langkah 11, 14, 15, 17, 29, 31, 32 (Search atau Modal Changelog), dan langkah 18, 20, 26 (ganti akun atau client eksplisit; S-07).
- Urutan TC: TC-FA-FAAM-741 sebelum TC-FA-FAAM-606 karena aktor pertama dan client berbeda.
- Langkah 30 dan 33 adalah asersi absence dengan anchor empty state `No results found` hasil Search (bagian 8b butir 2). Absence log pada TC-FA-FAAM-606 butir c diasersi lewat Search atas nama bersuffix unik (baseline nol); TC-FA-FAAM-606 butir c berisi klausa absence log tanpa spec kelas g, sehingga keputusan pemilik: pindahkan ke spec kelas g atau terima asersi ini.
- Temuan untuk QA:
  - Pre-setup No. 16g tidak memuat email akun Total Control dan Import Data pada client Growth.
  - TC-FA-FAAM-606 mensyaratkan Total Control mencatat "total baris List dan entri teratas Changelog" pada langkah 1; spec memakai jumlah dari seeding (50) dan Search atas nama bersuffix sebagai pengganti baseline Changelog (audit trail permanen).
  - Berkas impor satu baris tidak didefinisikan TC; disediakan tim FE.
