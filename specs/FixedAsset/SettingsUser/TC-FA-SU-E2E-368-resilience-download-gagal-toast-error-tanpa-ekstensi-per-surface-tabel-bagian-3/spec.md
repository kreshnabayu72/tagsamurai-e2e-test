---
id: TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3
title: "Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-732
  - TC-FA-SU-762
  - TC-FA-SU-793
  - TC-FA-SU-834
coverage:
  web: automated
---

# Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada unduhan, resilience download). Data Pre-setup: Client `FaUserMain` (#20), Changelog (#27), System Log (#28), Transaction Admin Log (#29), User Log (#30). Pengguna target: Budi Santoso dari Client `FaUserMain`; surface User List memakai seluruh populasi Client.
- Kemampuan teknis: `Spectra.intercept()` atas respons permintaan unduhan di atas backend nyata (status 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan. Browser mengamati folder unduhan uji untuk asersi tidak ada berkas terunduh; folder dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept dan pembersihan folder unduhan.

## Test Steps

### TC-FA-SU-732: Download Modal Combined Changelog: User gagal: toast error tanpa ekstensi

1. Klik icon Changelog di halaman User List
2. Atur intercept respons unduhan menjadi 500
3. Klik icon Download
4. Pilih `Download as CSV`
5. Verifikasi toast error persist "Error, failed to download Changelog-User." tampil (tanpa ekstensi)
6. Verifikasi tidak ada berkas terunduh
7. Verifikasi halaman tetap utuh
8. Lepas intercept respons unduhan
9. Tutup toast error
10. Tutup modal Changelog

### TC-FA-SU-762: Download Tab System Log gagal: toast error tanpa ekstensi

11. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab System Log
12. Atur intercept respons unduhan menjadi 500
13. Klik icon Download
14. Pilih `Download as CSV`
15. Verifikasi toast error persist "Error, failed to download System-Log-Budi-Santoso." tampil (tanpa ekstensi)
16. Verifikasi tidak ada berkas terunduh
17. Verifikasi halaman tetap utuh
18. Lepas intercept respons unduhan
19. Tutup toast error

### TC-FA-SU-793: Download Tab Transaction Admin Log sub-tab Borrowing & Assignment gagal: toast error tanpa ekstensi

20. Buka Detail Budi Santoso > Tab Transaction Admin Log > Sub-tab Borrowing & Assignment
21. Atur intercept respons unduhan menjadi 500
22. Klik icon Download
23. Pilih `Download as CSV`
24. Verifikasi toast error persist "Error, failed to download Transaction-Admin-Log-Budi-Santoso-Borrowing-Assignment." tampil (tanpa ekstensi)
25. Verifikasi tidak ada berkas terunduh
26. Verifikasi halaman tetap utuh
27. Lepas intercept respons unduhan
28. Tutup toast error

### TC-FA-SU-834: Download Tab User Log sub-tab Borrow gagal: toast error tanpa ekstensi

29. Buka Detail Budi Santoso > Tab User Log > Sub-tab Borrow
30. Atur intercept respons unduhan menjadi 500
31. Klik icon Download
32. Pilih `Download as CSV`
33. Verifikasi toast error persist "Error, failed to download User-Log-Borrow-Budi-Santoso." tampil (tanpa ekstensi)
34. Verifikasi tidak ada berkas terunduh
35. Verifikasi halaman tetap utuh
36. Lepas intercept respons unduhan
37. Tutup toast error

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengatur dan melepas intercept respons unduhan serta menutup toast error persist, serta menutup modal Changelog. Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 11, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-732: format dan nama berkas TC-FA-SU-729 di spec 240, empty state, loading, dan error load TC-FA-SU-734 di spec 375, transformasi data TC-FA-SU-731 di spec 373.
  - TC-FA-SU-762: format dan nama berkas TC-FA-SU-759 di spec 250, empty state, loading, dan error load TC-FA-SU-764 di spec 364, transformasi data TC-FA-SU-761 di spec 373.
  - TC-FA-SU-793: format dan nama berkas TC-FA-SU-790 di spec 262, empty state, loading, dan error load TC-FA-SU-795 di spec 364, transformasi data TC-FA-SU-792 di spec 373.
  - TC-FA-SU-834: format dan nama berkas TC-FA-SU-831 di spec 274, empty state, loading, dan error load TC-FA-SU-836 di spec 376, transformasi data TC-FA-SU-833 di spec 373.
- Alasan melewati sekitar 35 langkah (37 langkah tertulis, 37 dengan ekspansi; tidak ada langkah yang diulang per iterasi): seluruh blok berkelas b (kegagalan unduhan yang dipaksa), tiap blok berdiri sendiri dan melepas intercept-nya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (S-15):
  - Butir b ("halaman tetap utuh") tidak mendefinisikan unsur yang diperiksa; spec menuliskannya apa adanya sebagai satu `Verifikasi` per TC.
  - TC hanya memicu kegagalan unduhan lewat `Download as CSV`; kegagalan unduhan XLSX tidak dicakup TC.
  - TC tidak menyatakan cara menutup toast error persist; spec memakai langkah penghubung `Tutup toast error` agar toast TC sebelumnya tidak terbawa ke TC berikutnya (R-12).
