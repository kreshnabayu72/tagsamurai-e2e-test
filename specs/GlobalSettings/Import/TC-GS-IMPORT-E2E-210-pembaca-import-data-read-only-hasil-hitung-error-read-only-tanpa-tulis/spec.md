---
id: TC-GS-IMPORT-E2E-210-pembaca-import-data-read-only-hasil-hitung-error-read-only-tanpa-tulis
title: "Pembaca Import data (Read Only): hasil hitung error read-only tanpa tulis-balik, Banner Custom Field dapat ditutup tanpa mengubah draft"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-517
  - TC-GS-IMPORT-945
  - TC-GS-IMPORT-958
coverage:
  web: automated
---

# Pembaca Import data (Read Only): hasil hitung error read-only tanpa tulis-balik, Banner Custom Field dapat ditutup tanpa mengubah draft

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net` (kapabilitas Import data: R), password `Spectra.env.GS_IMPORTRO_PASSWORD` (nama env baru, didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API mengubah Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A untuk akun pembaca.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun Import data (Read Only) Client A (nilai awal dicatat dan dipulihkan hook suite `after`), lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4; Custom Field Active `Shift Notes` Optional dan kosong pada seluruh baris), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Custom Field Client A (Pre-setup, Optional, Active): Shift (Dropdown Pagi/Siang/Malam), Shift Notes. Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks Banner).
- Jeda 5 detik sebelum pembacaan fixture adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.
- Pembacaan status tersimpan: skrip fixture inspeksi data (disediakan tim FE/BE) membaca status tersimpan baris draft tanpa melalui UI.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): opsi `Siang` ditambahkan kembali ke `Shift`; `Shift` diaktifkan kembali; `Shift Notes` dikembalikan ke Optional; draft User Login Client A dipulihkan ke D-05. Pemulihan antar blok dilakukan sebagai langkah aksi.
- Kemampuan teknis: skrip seed D-05; skrip inspeksi data; sesi API Admin kedua.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Hasil hitung read-only setelah opsi dihapus (TC-GS-IMPORT-517)

1. Admin kedua Client A (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan
2. Pembaca Import data (Read Only) membuka Import > User Login
3. Verifikasi Row # 1 dan 2 tampil berstatus `error`
4. Verifikasi Staging Metric Cards: Ready to Import 6, Errors 2
5. Tunggu 5 detik tanpa memuat ulang halaman
6. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
7. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
8. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke Custom Field `Shift`, buat ulang draft D-05, muat ulang halaman

### Hasil hitung Required read-only (TC-GS-IMPORT-945)

9. Admin kedua Client A (sesi API) menjadikan Custom Field `Shift Notes` Required hingga tersimpan
10. Pembaca Import data (Read Only) membuka Import > User Login
11. Verifikasi seluruh 8 baris tampil berstatus `error`
12. Verifikasi Staging Metric Cards: Ready to Import 0, Errors 8
13. Tunggu 5 detik tanpa memuat ulang halaman
14. Baca status tersimpan Row # 1 sampai 8 lewat skrip fixture inspeksi data
15. Verifikasi status tersimpan seluruh baris masih `pending`
16. Pulihkan: Admin kedua mengembalikan `Shift Notes` ke Optional, buat ulang draft D-05, muat ulang halaman

### Banner Custom Field ditutup pembaca (TC-GS-IMPORT-958)

17. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
18. Pembaca Import data (Read Only) membuka Import > User Login
19. Verifikasi kolom Shift tampil
20. Verifikasi Banner Custom Field Deactivated tampil dengan tombol `[×]`
21. Klik `[×]` pada Banner Custom Field
22. Verifikasi banner tertutup
23. Verifikasi tidak ada dialog maupun toast
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Baca status tersimpan Row # 1 sampai 8 lewat skrip fixture inspeksi data
26. Verifikasi status tersimpan seluruh baris masih `pending`
27. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi pembaca.
- Langkah 8, 16, dan 27 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Membuka halaman di langkah 2, 10, dan 18 adalah pemuatan ulang halaman Import oleh pembaca (hook `beforeEach` sudah membuka layar sebelum Admin kedua mengubah Custom Field).
- Langkah 5, 13, dan 24 adalah langkah penghubung tanpa `Verifikasi` (jendela 5 detik tanpa memuat ulang halaman sebelum pembacaan fixture; penanda ini tidak ada di TC).
- Temuan untuk QA:
  - TC-GS-IMPORT-517 dan 945 serta 958 mengasersi status tersimpan lewat "skrip fixture inspeksi data"; TC tidak menjelaskan skrip itu (kemampuan membaca state BE yang tidak terlihat di UI, disediakan tim FE/BE; tidak ada endpoint karangan).
  - TC-GS-IMPORT-517 Precondition hanya merinci Shift `Siang` pada Row # 1 dan 2 dari D-05; spec memakai D-05 lengkap.
