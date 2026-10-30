---
id: TC-GS-IMPORT-E2E-200-kolom-date-changelog-import-mengikuti-date-time-format-dan-time-zone
title: "Kolom Date Changelog Import mengikuti Date, Time Format, dan Time Zone General Settings (modal seed dan entri hasil commit)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-757
  - TC-GS-IMPORT-800
coverage:
  web: automated
---

# Kolom Date Changelog Import mengikuti Date, Time Format, dan Time Zone General Settings (modal seed dan entri hasil commit)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah General Settings Client E (state global) dan melakukan commit sungguhan; worker commit berjalan normal (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru). Sesi API mengubah Time Format dan Time Zone General Settings Client E untuk TC-GS-IMPORT-800 dan memulihkannya; klien HTTP dan kontrak endpoint General Settings disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis: D-60 (30 entri seed Changelog Import Client E, bertanggal i Sep 2026 pukul 10:00 UTC+7 untuk i = 1 sampai 30, dibaca saja; skrip seed juga membersihkan entri hasil commit spec lain) untuk TC-GS-IMPORT-800; D-50 (draft Brand 12 baris `pending` di Client E dari `brand-12.csv`: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus) untuk TC-GS-IMPORT-757, disiapkan lewat skrip seed sebelum TC itu. Nama Brand literal dipakai karena Client E khusus commit dan record dibersihkan di hook `after`.
- General Settings Client E Pre-setup: Date Format `dd MMM yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`.
- Urutan: TC-GS-IMPORT-800 sebelum TC-GS-IMPORT-757, karena entri hasil commit TC-GS-IMPORT-757 bertanggal hari ini dan menjadi baris pertama sort default.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): General Settings Client E dipulihkan ke Date Format `dd MMM yy`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`; Brand hasil commit (Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus) dihapus lewat skrip reset Client E (D-47, reset hasil commit terakhir dan penanda Banner Hasil Commit); entri seed D-60 dibersihkan; draft Brand dibuang.
- Kemampuan teknis: pengubahan General Settings lewat sesi API Admin kedua; skrip seed D-50 dan D-60; skrip reset Client E.
- State global: General Settings Client E (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Time Format dan Time Zone pada modal seed (TC-GS-IMPORT-800)

1. Klik `[Changelog]`
2. Catat Date baris pertama
3. Verifikasi Date baris pertama `30 Sep 26` pukul `10:00`
4. Tutup modal Changelog
5. Admin kedua Client E (sesi API) mengubah Time Format menjadi `hh:mm a` dan Time Zone menjadi `(UTC+08:00) Kuala Lumpur, Singapore, Makassar` di General Settings hingga tersimpan
6. Tekan `F5` pada halaman Import
7. Klik `[Changelog]`
8. Catat Date baris pertama
9. Verifikasi Date baris pertama `30 Sep 26` pukul `11:00 AM`
10. Tutup modal Changelog
11. Admin kedua Client E (sesi API) memulihkan General Settings Client E ke Time Format `HH:mm` dan Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` hingga tersimpan

### Date Format dan Time Format hasil commit (TC-GS-IMPORT-757)

12. Seed draft D-50 lewat skrip seed, lalu muat ulang halaman Import > Brand
13. Buka halaman Global Settings > General Settings
14. Ubah Date Format menjadi `M/d/yy`
15. Ubah Time Format menjadi `hh:mm a`
16. Klik `[Save]`
17. Tunggu aksi selesai (permintaan mendapat respons)
18. Buka halaman Import > Brand
19. Klik `[Changelog]` dan catat jumlah total entri pada pagination sebagai baseline, lalu tutup modal Changelog
20. Klik `[Import (12)]`
21. Muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
22. Klik `[Changelog]`
23. Verifikasi jumlah total entri pada pagination bertambah satu dari baseline
24. Verifikasi Date pada entri baru `Import Brand` memakai pola `M/d/yy hh:mm a` (jam 12 dengan AM/PM)
25. Tutup modal Changelog
26. Pulihkan General Settings Client E ke Date Format `dd MMM yy` dan Time Format `HH:mm`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan 800 sebelum 757 mengikuti Data Dinamis D-60: entri commit hari ini menjadi baris pertama sort default dan menggeser asersi baris pertama TC-800 (S-05, perubahan urutan TC dicatat di sini).
- P-2: Admin kedua hanya memicu perubahan General Settings lewat sesi API; hasil diasersi hanya di sesi admin pertama, sehingga spec tidak masuk kelas c.
- Langkah 11 dan 26 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan. Langkah 17 menunggu `[Save]` General Settings selesai sebelum membuka Import.
- Langkah 23 memakai baseline jumlah entri (S-12), bukan posisi baris, karena D-60 menyisakan entri seed dengan tanggal Sep 2026.
- Langkah 21 memuat ulang halaman berulang sampai commit selesai; batas tunggu 2 menit mengikuti langkah 7 TC-GS-IMPORT-757.
- Temuan untuk QA:
  - TC-GS-IMPORT-757 Expected hanya menyebut pola Date `M/d/yy hh:mm a` tanpa isi entri; spec mengasersi pola (bukan nilai tanggal) dan jumlah entri bertambah satu.
  - TC-GS-IMPORT-757 Post Condition a, b, c (draft dihapus, satu entri ringkasan, General Settings dipulihkan) tidak punya langkah observasi di TC; tidak diasersi terpisah, General Settings dipulihkan sebagai langkah (S-01).
  - TC-GS-IMPORT-800 Precondition tidak menyebut mekanisme perubahan General Settings oleh Admin kedua; spec memakai sesi API (kemampuan disediakan tim FE/BE).
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
  - Penanda selesai untuk langkah 17 (`[Save]` General Settings) tidak disebut di TC-GS-IMPORT-757, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati (mis. toast atau tombol aktif kembali).
