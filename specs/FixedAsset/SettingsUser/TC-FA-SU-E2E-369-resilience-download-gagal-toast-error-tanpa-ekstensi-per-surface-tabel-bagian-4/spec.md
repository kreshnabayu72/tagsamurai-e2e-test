---
id: TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4
title: "Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-534
  - TC-FA-SU-636
  - TC-FA-SU-867
  - TC-FA-SU-891
coverage:
  web: automated
---

# Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada unduhan, resilience download). Data Pre-setup: Client `FaUserMain` (#20), Responsibilities (#25), Changelog (#27), User Log (#30). Pengguna target: Budi Santoso dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons permintaan unduhan di atas backend nyata (status 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan. Browser mengamati folder unduhan uji untuk asersi tidak ada berkas terunduh; folder dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept dan pembersihan folder unduhan.

## Test Steps

### TC-FA-SU-534: Download Sub-tab Pending Tasks gagal: toast error tanpa ekstensi

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks
2. Atur intercept respons unduhan menjadi 500
3. Klik icon Download
4. Pilih `Download as CSV`
5. Verifikasi toast error persist "Error, failed to download Pending-Tasks-Budi-Santoso." tampil (tanpa ekstensi)
6. Verifikasi tidak ada berkas terunduh
7. Verifikasi halaman tetap utuh
8. Lepas intercept respons unduhan
9. Tutup toast error

### TC-FA-SU-636: Download Modal Changelog User > Global Role gagal: toast error tanpa ekstensi

10. Buka Detail Budi Santoso > Tab Role > Sub-tab Global Role > icon Changelog
11. Atur intercept respons unduhan menjadi 500
12. Klik icon Download
13. Pilih `Download as CSV`
14. Verifikasi toast error persist "Error, failed to download Changelog-Budi-Santoso-Global-Role." tampil (tanpa ekstensi)
15. Verifikasi tidak ada berkas terunduh
16. Verifikasi halaman tetap utuh
17. Lepas intercept respons unduhan
18. Tutup toast error
19. Tutup modal Changelog

### TC-FA-SU-867: Download Tab User Log sub-tab Assignment gagal: toast error tanpa ekstensi

20. Buka Detail Budi Santoso > Tab User Log > Sub-tab Assignment
21. Atur intercept respons unduhan menjadi 500
22. Klik icon Download
23. Pilih `Download as CSV`
24. Verifikasi toast error persist "Error, failed to download User-Log-Assignment-Budi-Santoso." tampil (tanpa ekstensi)
25. Verifikasi tidak ada berkas terunduh
26. Verifikasi halaman tetap utuh
27. Lepas intercept respons unduhan
28. Tutup toast error

### TC-FA-SU-891: Download Tab User Log sub-tab Session gagal: toast error tanpa ekstensi

29. Buka Detail Budi Santoso > Tab User Log > Sub-tab Session
30. Atur intercept respons unduhan menjadi 500
31. Klik icon Download
32. Pilih `Download as CSV`
33. Verifikasi toast error persist "Error, failed to download User-Log-Budi-Santoso." tampil (tanpa ekstensi)
34. Verifikasi tidak ada berkas terunduh
35. Verifikasi halaman tetap utuh
36. Lepas intercept respons unduhan
37. Tutup toast error

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengatur dan melepas intercept respons unduhan serta menutup toast error persist, serta menutup modal Changelog.
- Pembagian TC lintas spec:
  - TC-FA-SU-534: format dan nama berkas TC-FA-SU-531 di spec 180, empty state, loading, dan error load TC-FA-SU-536 di spec 361, transformasi data TC-FA-SU-533 di spec 371.
  - TC-FA-SU-636: format dan nama berkas TC-FA-SU-633 di spec 211, empty state, loading, dan error load TC-FA-SU-638 di spec 376, transformasi data TC-FA-SU-635 di spec 372.
  - TC-FA-SU-867: format dan nama berkas TC-FA-SU-864 di spec 284, empty state, loading, dan error load TC-FA-SU-869 di spec 365, transformasi data TC-FA-SU-866 di spec 374.
  - TC-FA-SU-891: format dan nama berkas TC-FA-SU-888 di spec 291, empty state, loading, dan error load TC-FA-SU-893 di spec 365, transformasi data TC-FA-SU-890 di spec 374.
- Alasan melewati sekitar 35 langkah (37 langkah tertulis, 37 dengan ekspansi; tidak ada langkah yang diulang per iterasi): seluruh blok berkelas b (kegagalan unduhan yang dipaksa), tiap blok berdiri sendiri dan melepas intercept-nya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (S-15):
  - Butir b ("halaman tetap utuh") tidak mendefinisikan unsur yang diperiksa; spec menuliskannya apa adanya sebagai satu `Verifikasi` per TC.
  - TC hanya memicu kegagalan unduhan lewat `Download as CSV`; kegagalan unduhan XLSX tidak dicakup TC.
  - TC tidak menyatakan cara menutup toast error persist; spec memakai langkah penghubung `Tutup toast error` agar toast TC sebelumnya tidak terbawa ke TC berikutnya (R-12).
  - TC-FA-SU-891: nama berkas pada toast (`User-Log-Budi-Santoso`) tidak memuat kata Session, berbeda dari pola sub-tab Borrow dan Assignment (`User-Log-Borrow-Budi-Santoso`, `User-Log-Assignment-Budi-Santoso`); spec mengikuti TC dan selaras dengan nama berkas TC-FA-SU-888, mohon konfirmasi bahwa nama itu memang disengaja.
