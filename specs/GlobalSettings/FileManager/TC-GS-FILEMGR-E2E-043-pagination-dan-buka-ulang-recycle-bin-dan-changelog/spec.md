---
id: TC-GS-FILEMGR-E2E-043-pagination-dan-buka-ulang-recycle-bin-dan-changelog
title: "Pagination dan Reset ke Default Saat Dibuka Ulang pada Modal Recycle Bin dan Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-218
  - TC-GS-FILEMGR-219
coverage:
  web: automated
---

# Pagination dan Reset ke Default Saat Dibuka Ulang pada Modal Recycle Bin dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji) dan Tabel A4 (14 entri Changelog). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A3/A4 karena asersi jumlah dan filter bergantung pada nama (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan "16 baris" dan "14 entri" hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin atau entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca jumlah baris per halaman dan opsi ukuran halaman; membaca indikator sort, isi input Search, dan pilihan Filter.

## Test Steps

### TC-GS-FILEMGR-218: Pagination modal Recycle Bin dan modal Changelog (ukuran default, opsi, pindah halaman)

1. Klik tombol Recycle Bin di toolbar
2. Verifikasi halaman 1 Recycle Bin memuat 10 baris
3. Pindah ke halaman 2
4. Verifikasi halaman 2 Recycle Bin memuat 6 baris
5. Buka selector ukuran halaman Recycle Bin
6. Verifikasi opsi ukuran `10`, `25`, `50`, `100`
7. Pilih ukuran halaman `25`
8. Verifikasi seluruh 16 baris tampil di halaman 1
9. Tutup modal Recycle Bin lewat ikon close (X)
10. Klik ikon Changelog di toolbar
11. Verifikasi halaman 1 Changelog memuat 10 entri
12. Pindah ke halaman 2
13. Verifikasi halaman 2 Changelog memuat 4 entri
14. Tutup modal Changelog lewat ikon close (X)

### TC-GS-FILEMGR-219: Modal Recycle Bin dan Changelog kembali ke default saat dibuka ulang

15. Klik tombol Recycle Bin di toolbar
16. Ketik Search `photo`, tekan Enter
17. Klik header Size sekali
18. Klik header Size sekali lagi
19. Klik ikon Filter di toolbar modal
20. Pilih `System` pada Deleted By, klik `[Apply]`
21. Tutup modal Recycle Bin lewat ikon close (X)
22. Klik tombol Recycle Bin di toolbar lagi
23. Verifikasi input Search kosong
24. Verifikasi Filter kosong
25. Verifikasi sort default Deleted Date Newest First
26. Verifikasi 16 baris tampil
27. Verifikasi halaman 1 memuat 10 baris
28. Tutup modal Recycle Bin lewat ikon close (X)
29. Klik ikon Changelog di toolbar
30. Klik ikon Filter di toolbar modal
31. Pilih `Delete` pada Action, klik `[Apply]`
32. Tutup modal Changelog lewat ikon close (X)
33. Klik ikon Changelog di toolbar lagi
34. Verifikasi Filter kosong
35. Verifikasi 14 entri tampil
36. Verifikasi halaman 1 memuat 10 entri

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (218, 219). Ukuran halaman Recycle Bin yang diubah ke 25 pada TC-GS-FILEMGR-218 (langkah 7) ikut diuji kembali ke 10 pada langkah 27 ("halaman 1 memuat 10 baris"), yaitu bagian dari Expected a TC-GS-FILEMGR-219.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 14 (menutup modal sebelum membuka modal berikutnya, mengikuti TC-GS-FILEMGR-218 langkah 3), langkah 28 (menutup Recycle Bin sebelum membuka Changelog, mengikuti TC-GS-FILEMGR-219 langkah 3). Langkah 17 dan 18 (dua klik header Size untuk mencapai Descending) menjabarkan "urutkan Size Descending".
- Panjang spec: 36 langkah, sedikit di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok berkelas sama (pagination dan state modal pada dua surface read-only, dataset Tabel A3 dan A4 yang sama, tanpa aksi tulis) dan memisah TC-GS-FILEMGR-219 dari TC-GS-FILEMGR-218 hanya menambah login ulang tanpa pemisah nyata (bagian 3, ukuran batas spec).
- Anchor: langkah 26 sampai 27 dan 35 sampai 36 membuktikan tabel termuat dengan baris sebelum asersi kosong; asersi "Filter kosong" (langkah 24, 34) didahului pembukaan ulang modal yang menampilkan toolbar.
- Temuan untuk QA:
  - TC-GS-FILEMGR-219 tidak menyebut cara membaca "Filter kosong" (Filter Panel kosong atau indikator filter aktif di toolbar); spec mengasersi pilihan pada Filter Panel kosong.
  - Mekanisme dan endpoint seeding Tabel A3 dan A4 tidak didefinisikan di TC (Q-4); hitungan baris dan entri mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Baris `due-photo.png` (sekarang − 31 hari) tampil sampai job auto-purge berikutnya sehingga hitungan 16 baris (langkah 4, 8, 26) tidak stabil bila job berjalan antara seeding dan asersi (Q-3).
