---
id: TC-GS-FILEMGR-E2E-041-kombinasi-search-filter-recycle-bin
title: "Kombinasi Search dan Filter Modal Recycle Bin: Irisan Simetris dan Independensi Clear"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-210
  - TC-GS-FILEMGR-211
  - TC-GS-FILEMGR-212
coverage:
  web: automated
---

# Kombinasi Search dan Filter Modal Recycle Bin: Irisan Simetris dan Independensi Clear

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file literal sesuai Tabel A3 karena asersi Search, Filter, dan Sort bergantung pada nama, ukuran, dan Deleted By (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan baris hasil kombinasi hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: membaca indikator sort pada header kolom, isi input Search, dan pilihan terpilih pada Filter Panel.

## Test Steps

1. Klik tombol Recycle Bin di toolbar

### TC-GS-FILEMGR-210: Search lebih dulu lalu Filter menghasilkan irisan

2. Ketik Search `photo`, tekan Enter
3. Verifikasi tabel memuat 14 baris: `legacy-photo.jpeg`, `due-photo.png`, dan `recycled-photo-01.jpg` s.d. `recycled-photo-12.jpg`
4. Klik ikon Filter di toolbar modal
5. Pilih `System` pada Deleted By, klik `[Apply]`
6. Verifikasi tabel memuat 5 baris: `legacy-photo.jpeg`, `recycled-photo-09.jpg` s.d. `recycled-photo-12.jpg`
7. Verifikasi kata kunci `photo` tetap terisi di input Search

### TC-GS-FILEMGR-211: Filter lebih dulu lalu Search menghasilkan irisan yang sama

8. Klik `[Clear Field]`, klik `[Apply]`
9. Klik ikon panah (←) di kiri input Search
10. Pilih `System` pada Deleted By, klik `[Apply]`
11. Verifikasi tabel memuat 5 baris
12. Ketik Search `photo`, tekan Enter
13. Verifikasi tabel memuat 5 baris yang sama: `legacy-photo.jpeg`, `recycled-photo-09.jpg` s.d. `recycled-photo-12.jpg`
14. Verifikasi pilihan `System` pada Deleted By tetap terpilih di Filter Panel

### TC-GS-FILEMGR-212: Clear Filter dan Clear Search saling independen dengan Sort aktif

15. Klik header Size sekali
16. Klik header Size sekali lagi
17. Klik `[Clear Field]` pada Filter, klik `[Apply]`
18. Verifikasi kata kunci `photo` tetap terisi di input Search
19. Verifikasi sort Size Descending tetap aktif
20. Verifikasi tabel memuat 14 baris
21. Verifikasi `legacy-photo.jpeg` berada di baris pertama
22. Pilih `System` pada Deleted By, klik `[Apply]`
23. Klik ikon (✕) di input Search, tekan Enter
24. Verifikasi pilihan `System` pada Deleted By tetap terpilih di Filter Panel
25. Verifikasi sort Size Descending tetap aktif
26. Verifikasi tabel memuat 5 baris
27. Verifikasi `legacy-photo.jpeg` berada di baris pertama

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (210, 211, 212): TC-GS-FILEMGR-212 memakai state keyword `photo` dan filter `System` yang sama dengan akhir TC-GS-FILEMGR-211, sehingga hanya perlu menambah sort (langkah 15 dan 16).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 dan 9 (membersihkan filter dan Search sisa TC-GS-FILEMGR-210 sebelum TC-GS-FILEMGR-211), langkah 15 dan 16 (dua klik header Size untuk mencapai Descending, mengikuti siklus sort Ascending lalu Descending; TC-GS-FILEMGR-212 langkah 1 menulis "urutkan Size Descending").
- Langkah 11 memverifikasi hasil Filter sebelum Search sehingga langkah 13 memiliki pembanding yang sama.
- Anchor: langkah 3, 6, dan 11 membuktikan tabel termuat dengan baris sebelum asersi baris pertama atau jumlah.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`; spec mengikuti langkah TC dan memakai `[Clear Field]`/`[Apply]` berurutan. Perlu konfirmasi perilaku panel agar skrip menulis langkah buka-ulang yang benar.
  - TC tidak menyebut indikator tempat "filter tetap aktif" teramati; spec mengasersi pilihan `System` pada Deleted By tetap terpilih di Filter Panel (langkah 14 dan 24). Perlu konfirmasi bila ada indikator filter aktif di toolbar.
  - Mekanisme dan endpoint seeding Tabel A3 tidak didefinisikan di TC (Q-4); hitungan baris mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - Baris `due-photo.png` dan `legacy-photo.jpeg` bergantung pada Deleted Date relatif; `due-photo.png` (sekarang − 31 hari) tampil sampai job auto-purge berikutnya sehingga hitungan 14 baris (langkah 3, 20) tidak stabil bila job berjalan antara seeding dan asersi (Q-3).
