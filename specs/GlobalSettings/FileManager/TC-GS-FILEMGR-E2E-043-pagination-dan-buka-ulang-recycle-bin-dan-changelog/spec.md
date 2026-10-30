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
- Suite serial (`parallel: false`): hitungan "16 baris" Recycle Bin hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin bersamaan. Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga hitungan entri tidak diasersi sebagai total absolut: hitungan dibatasi dengan Filter Date rentang Date Tabel A4 (`23/08/26` sampai `14/09/26`, inklusif; entri terlama 23/08/26 08:00 dan terbaru 14/09/26 02:00) yang hanya memuat populasi Tabel A4.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: memilih rentang Date `23/08/26` sampai `14/09/26` pada date range picker Filter Panel Changelog (Date entri Tabel A4 tetap, bukan relatif); membaca jumlah baris per halaman dan opsi ukuran halaman; membaca indikator sort, isi input Search, dan pilihan Filter.

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
11. Klik ikon Filter di toolbar modal, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik ikon Filter
12. Verifikasi halaman 1 Changelog memuat 10 entri
13. Pindah ke halaman 2
14. Verifikasi halaman 2 Changelog memuat 4 entri (total 14 entri dalam rentang Date Tabel A4)
15. Tutup modal Changelog lewat ikon close (X)

### TC-GS-FILEMGR-219: Modal Recycle Bin dan Changelog kembali ke default saat dibuka ulang

16. Klik tombol Recycle Bin di toolbar
17. Ketik Search `photo`, tekan Enter
18. Klik header Size sekali
19. Klik header Size sekali lagi
20. Klik ikon Filter di toolbar modal
21. Pilih `System` pada Deleted By, klik `[Apply]`
22. Tutup modal Recycle Bin lewat ikon close (X)
23. Klik tombol Recycle Bin di toolbar lagi
24. Verifikasi input Search kosong
25. Verifikasi Filter kosong
26. Verifikasi sort default Deleted Date Newest First
27. Verifikasi 16 baris tampil
28. Verifikasi halaman 1 memuat 10 baris
29. Tutup modal Recycle Bin lewat ikon close (X)
30. Klik ikon Changelog di toolbar
31. Klik ikon Filter di toolbar modal
32. Pilih `Delete` pada Action, klik `[Apply]`
33. Tutup modal Changelog lewat ikon close (X)
34. Klik ikon Changelog di toolbar lagi
35. Verifikasi Filter kosong
36. Klik ikon Filter di toolbar modal, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik ikon Filter
37. Verifikasi 14 entri tampil (rentang Date Tabel A4; bukan 2 entri hasil Filter Action `Delete` sebelumnya)
38. Verifikasi halaman 1 memuat 10 entri

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (218, 219). Ukuran halaman Recycle Bin yang diubah ke 25 pada TC-GS-FILEMGR-218 (langkah 7) ikut diuji kembali ke 10 pada langkah 28 ("halaman 1 memuat 10 baris"), yaitu bagian dari Expected a TC-GS-FILEMGR-219.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 15 (menutup modal sebelum membuka modal berikutnya, mengikuti TC-GS-FILEMGR-218 langkah 3), langkah 29 (menutup Recycle Bin sebelum membuka Changelog, mengikuti TC-GS-FILEMGR-219 langkah 3), langkah 11 dan 36 (menerapkan Filter Date rentang Tabel A4 supaya hitungan entri hanya dari populasi Tabel A4; tidak ada di TC dan dicatat per S-03). Langkah 18 dan 19 (dua klik header Size untuk mencapai Descending) menjabarkan "urutkan Size Descending".
- Panjang spec: 38 langkah, sedikit di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok berkelas sama (pagination dan state modal pada dua surface read-only, dataset Tabel A3 dan A4 yang sama, tanpa aksi tulis) dan memisah TC-GS-FILEMGR-219 dari TC-GS-FILEMGR-218 hanya menambah login ulang tanpa pemisah nyata (bagian 3, ukuran batas spec).
- Anchor: langkah 27 sampai 28 dan 37 sampai 38 membuktikan tabel termuat dengan baris sebelum asersi kosong; asersi "Filter kosong" (langkah 25, 35) didahului pembukaan ulang modal yang menampilkan toolbar.
- Temuan untuk QA:
  - TC-GS-FILEMGR-219 tidak menyebut cara membaca "Filter kosong" (Filter Panel kosong atau indikator filter aktif di toolbar); spec mengasersi pilihan pada Filter Panel kosong.
  - Mekanisme dan endpoint seeding Tabel A3 dan A4 tidak didefinisikan di TC (Q-4); hitungan baris Recycle Bin mengasumsikan dataset di-seed ulang dan suite serial (Q-7).
  - TC sumber (mis. TC-GS-FILEMGR-172 dan TC Changelog sejenis) menyatakan hitungan entri absolut ("14 entri", "5 baris") yang bertentangan dengan S-12 (Changelog tidak dapat di-seed ulang atau dibersihkan). Spec membatasi dengan Filter Date rentang Tabel A4 sebagai langkah penghubung; pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang Tabel A4 atau hitungan relatif. Spec juga mengasumsikan Filter Panel dapat ditutup lewat klik ikon Filter setelah `[Apply]` (TC tidak menyatakan perilaku panel).
  - Baris `due-photo.png` (sekarang − 31 hari) tampil sampai job auto-purge berikutnya sehingga hitungan 16 baris (langkah 4, 8, 27) tidak stabil bila job berjalan antara seeding dan asersi (Q-3).
