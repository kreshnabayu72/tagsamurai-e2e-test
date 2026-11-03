---
id: TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1
title: "Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-363
  - TC-FA-SU-438
  - TC-FA-SU-467
  - TC-FA-SU-498
coverage:
  web: automated
---

# Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Kelas harness: b (fault injection pada unduhan, resilience download). Data Pre-setup: Client `FaUserMain` (#20), Responsibilities (#24), Responsibilities (#25). Pengguna target: Budi Santoso dari Client `FaUserMain`; surface User List memakai seluruh populasi Client.
- Kemampuan teknis: `Spectra.intercept()` atas respons permintaan unduhan di atas backend nyata (status 500); intercept dilepas oleh langkah `Lepas intercept` dan hook `after` melepasnya lagi sebagai cadangan. Browser mengamati folder unduhan uji untuk asersi tidak ada berkas terunduh; folder dibersihkan di hook `after`. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pelepasan intercept dan pembersihan folder unduhan.

## Test Steps

### TC-FA-SU-363: Download User List gagal: toast error tanpa ekstensi

1. Atur intercept respons unduhan menjadi 500
2. Klik icon Download
3. Pilih `Download as CSV`
4. Verifikasi toast error persist "Error, failed to download User." tampil (tanpa ekstensi)
5. Verifikasi tidak ada berkas terunduh
6. Verifikasi halaman tetap utuh
7. Lepas intercept respons unduhan
8. Tutup toast error

### TC-FA-SU-438: Download Sub-tab Borrowed Assets gagal: toast error tanpa ekstensi

9. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
10. Atur intercept respons unduhan menjadi 500
11. Klik icon Download
12. Pilih `Download as CSV`
13. Verifikasi toast error persist "Error, failed to download Borrowed-Assets-Budi-Santoso." tampil (tanpa ekstensi)
14. Verifikasi tidak ada berkas terunduh
15. Verifikasi halaman tetap utuh
16. Lepas intercept respons unduhan
17. Tutup toast error

### TC-FA-SU-467: Download Sub-tab Assigned Assets gagal: toast error tanpa ekstensi

18. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Assigned Assets
19. Atur intercept respons unduhan menjadi 500
20. Klik icon Download
21. Pilih `Download as CSV`
22. Verifikasi toast error persist "Error, failed to download Assigned-Assets-Budi-Santoso." tampil (tanpa ekstensi)
23. Verifikasi tidak ada berkas terunduh
24. Verifikasi halaman tetap utuh
25. Lepas intercept respons unduhan
26. Tutup toast error

### TC-FA-SU-498: Download Sub-tab Pending Approvals gagal: toast error tanpa ekstensi

27. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Approvals
28. Atur intercept respons unduhan menjadi 500
29. Klik icon Download
30. Pilih `Download as CSV`
31. Verifikasi toast error persist "Error, failed to download Pending-Approvals-Budi-Santoso." tampil (tanpa ekstensi)
32. Verifikasi tidak ada berkas terunduh
33. Verifikasi halaman tetap utuh
34. Lepas intercept respons unduhan
35. Tutup toast error

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; tiap TC memakai surface-nya sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Mode FE+BE: kegagalan dipaksa dengan `Spectra.intercept()` parsial di atas backend nyata (bagian 6 konvensi), bukan seluruh API di-mock. Kelas b (resilience) dikumpulkan per jenis aksi baca atau unduh; kelas lain tidak ada di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): mengatur dan melepas intercept respons unduhan serta menutup toast error persist.
- Pembagian TC lintas spec:
  - TC-FA-SU-363: format dan nama berkas TC-FA-SU-360 di spec 127, empty state, loading, dan error load TC-FA-SU-365 di spec 375, transformasi data TC-FA-SU-362 di spec 370.
  - TC-FA-SU-438: format dan nama berkas TC-FA-SU-435 di spec 147, empty state, loading, dan error load TC-FA-SU-440 di spec 360, transformasi data TC-FA-SU-437 di spec 370.
  - TC-FA-SU-467: format dan nama berkas TC-FA-SU-464 di spec 159, empty state, loading, dan error load TC-FA-SU-469 di spec 361, transformasi data TC-FA-SU-466 di spec 370.
  - TC-FA-SU-498: format dan nama berkas TC-FA-SU-495 di spec 167, empty state, loading, dan error load TC-FA-SU-500 di spec 361, transformasi data TC-FA-SU-497 di spec 371.
- Temuan untuk QA (S-15):
  - Butir b ("halaman tetap utuh") tidak mendefinisikan unsur yang diperiksa; spec menuliskannya apa adanya sebagai satu `Verifikasi` per TC.
  - TC hanya memicu kegagalan unduhan lewat `Download as CSV`; kegagalan unduhan XLSX tidak dicakup TC.
  - TC tidak menyatakan cara menutup toast error persist; spec memakai langkah penghubung `Tutup toast error` agar toast TC sebelumnya tidak terbawa ke TC berikutnya (R-12).
