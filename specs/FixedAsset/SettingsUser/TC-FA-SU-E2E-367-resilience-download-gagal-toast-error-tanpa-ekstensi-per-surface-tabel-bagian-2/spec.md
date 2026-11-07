---
id: TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2
title: "Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-572
  - TC-FA-SU-604
  - TC-FA-SU-668
  - TC-FA-SU-700
coverage:
  web: automated
---

# Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada unduhan, resilience download). Data Pre-setup: Client `FaUserMain` (#20), Non-Login User (#26), Changelog (#27). Pengguna target: Budi Santoso dari Client `FaUserMain`.
- Kemampuan teknis: `Spectra.intercept()` atas respons permintaan unduhan di atas backend nyata (status 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan. Browser mengamati folder unduhan uji untuk asersi tidak ada berkas terunduh; folder dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept dan pembersihan folder unduhan.

## Test Steps

### TC-FA-SU-572: Download Tab Non-Login User gagal: toast error tanpa ekstensi

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User
2. Atur intercept respons unduhan menjadi 500
3. Klik icon Download
4. Pilih `Download as CSV`
5. Verifikasi toast error persist "Error, failed to download Non-Login-User-Budi-Santoso." tampil (tanpa ekstensi)
6. Verifikasi tidak ada berkas terunduh
7. Verifikasi halaman tetap utuh
8. Lepas intercept respons unduhan
9. Tutup toast error

### TC-FA-SU-604: Download Tab Changelog gagal: toast error tanpa ekstensi

10. Buka Detail Budi Santoso > Tab Changelog
11. Atur intercept respons unduhan menjadi 500
12. Klik icon Download
13. Pilih `Download as CSV`
14. Verifikasi toast error persist "Error, failed to download Changelog-Budi-Santoso." tampil (tanpa ekstensi)
15. Verifikasi tidak ada berkas terunduh
16. Verifikasi halaman tetap utuh
17. Lepas intercept respons unduhan
18. Tutup toast error

### TC-FA-SU-668: Download Modal Changelog User > Group Role gagal: toast error tanpa ekstensi

19. Buka Detail Budi Santoso > Tab Role > Sub-tab Group Role > icon Changelog
20. Atur intercept respons unduhan menjadi 500
21. Klik icon Download
22. Pilih `Download as CSV`
23. Verifikasi toast error persist "Error, failed to download Changelog-Budi-Santoso-Group-Role." tampil (tanpa ekstensi)
24. Verifikasi tidak ada berkas terunduh
25. Verifikasi halaman tetap utuh
26. Lepas intercept respons unduhan
27. Tutup toast error
28. Tutup modal Changelog

### TC-FA-SU-700: Download Modal Changelog User > Transaction Role gagal: toast error tanpa ekstensi

29. Buka Detail Budi Santoso > Tab Role > Sub-tab Transaction Role > icon Changelog
30. Atur intercept respons unduhan menjadi 500
31. Klik icon Download
32. Pilih `Download as CSV`
33. Verifikasi toast error persist "Error, failed to download Changelog-Budi-Santoso-Transaction-Role." tampil (tanpa ekstensi)
34. Verifikasi tidak ada berkas terunduh
35. Verifikasi halaman tetap utuh
36. Lepas intercept respons unduhan
37. Tutup toast error
38. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengatur dan melepas intercept respons unduhan serta menutup toast error persist, serta menutup modal Changelog.
- Langkah penghubung tambahan (S-03): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16).
- Pembagian TC lintas spec:
  - TC-FA-SU-572: format dan nama berkas TC-FA-SU-569 di spec 191, empty state, loading, dan error load TC-FA-SU-574 di spec 362, transformasi data TC-FA-SU-571 di spec 371.
  - TC-FA-SU-604: format dan nama berkas TC-FA-SU-601 di spec 201, empty state, loading, dan error load TC-FA-SU-606 di spec 362, transformasi data TC-FA-SU-603 di spec 372.
  - TC-FA-SU-668: format dan nama berkas TC-FA-SU-665 di spec 221, empty state, loading, dan error load TC-FA-SU-670 di spec 363, transformasi data TC-FA-SU-667 di spec 372.
  - TC-FA-SU-700: format dan nama berkas TC-FA-SU-697 di spec 229, empty state, loading, dan error load TC-FA-SU-702 di spec 363, transformasi data TC-FA-SU-699 di spec 372.
- Alasan melewati sekitar 35 langkah (38 langkah tertulis, 38 dengan ekspansi; tidak ada langkah yang diulang per iterasi): seluruh blok berkelas b (kegagalan unduhan yang dipaksa), tiap blok berdiri sendiri dan melepas intercept-nya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (S-15):
  - Butir b ("halaman tetap utuh") tidak mendefinisikan unsur yang diperiksa; spec menuliskannya apa adanya sebagai satu `Verifikasi` per TC.
  - TC hanya memicu kegagalan unduhan lewat `Download as CSV`; kegagalan unduhan XLSX tidak dicakup TC.
  - TC tidak menyatakan cara menutup toast error persist; spec memakai langkah penghubung `Tutup toast error` agar toast TC sebelumnya tidak terbawa ke TC berikutnya (R-12).
