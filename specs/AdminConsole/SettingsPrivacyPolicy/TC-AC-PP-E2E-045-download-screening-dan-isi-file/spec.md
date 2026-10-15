---
id: TC-AC-PP-E2E-045-download-screening-dan-isi-file
title: "Download Version History: Screening Overlay, Nama File, dan Isi File CSV dan XLSX"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-138
  - TC-AC-PP-139
  - TC-AC-PP-140
  - TC-AC-PP-142
  - TC-AC-PP-145
  - TC-AC-PP-146
  - TC-AC-PP-147
coverage:
  web: automated
---

# Download Version History: Screening Overlay, Nama File, dan Isi File CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat A untuk TC-AC-PP-138 sampai 145 dan 147, lalu Riwayat C (0 versi, belum pernah Publish) untuk TC-AC-PP-146 di akhir spec. (Version 3 Active, John Doe, 10 Aug 2026 20:30 UTC; Version 2, John Doe, 02 Jul 2026; Version 1, Jane Smith, 15 Jan 2026). Isi Version 3 memuat paragraf `This Privacy Policy describes how we collect, use, and protect your information.`. Hook `before` men-seed Riwayat A lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat, termasuk Riwayat C dengan 0 versi di langkah 43; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: membaca file CSV dan XLSX yang terunduh (nama file, header, baris data, nama sheet, isi sel) dan menyimpan unduhan ke folder uji yang dibersihkan di hook `after` (kelas f, binary buffer).
- Konfigurasi kolom tersimpan di cache browser; hook `before` mengosongkan cache konfigurasi kolom dan hook `after` memulihkannya.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide dan konfigurasi kolom memakai cache browser yang sama; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-138: Screening overlay Download di toolbar

1. Buka Settings > Privacy Policy lewat sidebar
2. Hover icon Download di toolbar
3. Verifikasi tooltip "Download" tampil
4. Klik icon Download
5. Verifikasi overlay berisi opsi "Download as CSV"
6. Verifikasi overlay berisi opsi "Download as XLSX"
7. Verifikasi overlay hanya berisi dua opsi tersebut
8. Tutup overlay Download dengan menekan Esc

### TC-AC-PP-139: Download as CSV menghasilkan file bernama Privacy-Policy-Version-History.csv tanpa toast sukses

9. Klik icon Download
10. Pilih "Download as CSV"
11. Verifikasi file terunduh dengan nama `Privacy-Policy-Version-History.csv`
12. Verifikasi tidak ada toast sukses atau toast lain

### TC-AC-PP-140: Download as XLSX menghasilkan file bernama Privacy-Policy-Version-History.xlsx dengan satu sheet Sheet1

13. Klik icon Download
14. Pilih "Download as XLSX"
15. Buka file yang terunduh
16. Verifikasi file terunduh dengan nama `Privacy-Policy-Version-History.xlsx` (ekstensi mengikuti pilihan format)
17. Verifikasi file memiliki satu sheet bernama `Sheet1`
18. Verifikasi tidak ada toast sukses

### TC-AC-PP-142: Isi file export: kolom, format tanggal, dan nama lengkap pada Published By

19. Klik icon Download
20. Pilih "Download as CSV"
21. Buka file yang terunduh
22. Verifikasi baris header file berisi tepat kolom `Version`, `Published At`, `Published By` (tanpa kolom Status)
23. Verifikasi baris data pertama: `Version 3`, `10 Aug 26`, `John Doe`
24. Verifikasi baris data kedua: `Version 2`, `02 Jul 26`, `John Doe`
25. Verifikasi baris data ketiga: `Version 1`, `15 Jan 26`, `Jane Smith`
26. Verifikasi Published By ditulis dengan nama lengkap snapshot (bukan `John D`)
27. Verifikasi tidak ada teks `Active` pada file

### TC-AC-PP-147: File export tidak memuat isi teks konten versi

28. Klik icon Download
29. Pilih "Download as XLSX"
30. Cari kalimat `This Privacy Policy describes how we collect` pada seluruh sel file
31. Verifikasi kalimat konten tidak ditemukan di sel mana pun pada file
32. Verifikasi tidak ada kolom isi konten

### TC-AC-PP-145: Export mengikuti kolom yang visible: kolom yang disembunyikan tidak ikut, dan ikut kembali setelah ditampilkan

33. Klik header kolom Actions `(⋯)` lalu uncheck `Published By` pada overlay Column Visibility
34. Klik icon Download lalu pilih "Download as CSV"
35. Buka file yang terunduh
36. Verifikasi file hanya memuat kolom `Version` dan `Published At`
37. Verifikasi tidak ada kolom `Published By` pada file
38. Verifikasi tidak ada toast peringatan
39. Klik header `(⋯)` lalu check kembali `Published By`
40. Klik icon Download lalu pilih "Download as CSV"
41. Buka file yang terunduh
42. Verifikasi file memuat kembali kolom `Version`, `Published At`, dan `Published By`

### TC-AC-PP-146: Download dengan nol baris tetap aktif dan menghasilkan file tanpa baris data

43. Seed ulang dataset menjadi Riwayat C (0 versi) lewat Fixture BE
44. Buka Settings > Privacy Policy lewat sidebar
45. Verifikasi icon Download aktif
46. Klik icon Download
47. Verifikasi opsi "Download as CSV" dapat dipilih
48. Pilih "Download as CSV"
49. Buka file yang terunduh
50. Verifikasi file terunduh tanpa baris data
51. Verifikasi tidak ada toast
52. Verifikasi baris header berisi kolom `Version`, `Published At`, `Published By`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: f (binary buffer, isi file CSV dan XLSX). Kegagalan download (TC-AC-PP-141) ada di spec Resilience; download pada Riwayat B dan 5.001 baris ada di spec 046 dan 047; Download oleh Read Only (TC-AC-PP-24) ada di spec Role Matrix.
- Urutan TC di spec ini 138, 139, 140, 142, 147, 145, 146 (TC sumber 138 sampai 140, 142, 145 sampai 147). TC-145 dipindah setelah TC-147 karena mengubah visibilitas kolom (cache browser) yang memengaruhi isi file TC lain, dan TC-146 di paling akhir karena butuh dataset Riwayat C (0 versi) yang membuang dataset Riwayat A (S-05, S-10).
- TC-AC-PP-146 (download nol baris) dipindah ke spec ini dari spec 003 karena memeriksa isi file CSV (kelas f); spec 003 hanya memuat screening empty state dan Read Only.
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 8 (tutup overlay Download), langkah 43 dan 44 (seed ulang Riwayat C lewat Fixture BE lalu buka halaman, precondition TC-146). Langkah 39 mengembalikan kolom `Published By` sebagai bagian TC-145; hook `after` menjadi cadangan pemulihan konfigurasi kolom.
- TC-AC-PP-139 Expected a dan b tidak mengasersi isi file; isi file ada di TC-AC-PP-142.
- Spec tidak membuat data dan tidak mengubah Pre-setup.
- Temuan untuk QA: TC-146 hanya menyebut format CSV pada Langkah Uji; format XLSX untuk nol baris tidak disebut sehingga tidak diasersi. Post Condition "Tidak ada perubahan data" tidak diasersi.
- Panjang spec (52 langkah) melewati perkiraan 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
