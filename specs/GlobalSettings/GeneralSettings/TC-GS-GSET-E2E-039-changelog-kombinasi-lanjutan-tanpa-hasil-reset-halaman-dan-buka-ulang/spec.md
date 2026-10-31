---
id: TC-GS-GSET-E2E-039-changelog-kombinasi-lanjutan-tanpa-hasil-reset-halaman-dan-buka-ulang
title: "Changelog General Settings: Kombinasi Lanjutan, Tanpa Hasil, dan Reset Halaman ke Halaman 1"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-155
  - TC-GS-GSET-156
  - TC-GS-GSET-157
coverage:
  web: automated
---

# Changelog General Settings: Kombinasi Lanjutan, Tanpa Hasil, dan Reset Halaman ke Halaman 1

## Prerequisites

- Mode: FE+BE. Spec tidak melakukan aksi tulis lewat UI; riwayat di-seed lewat API.
- Akun aktor UI: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding (sesi API, tanpa sesi UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2; `Fixture.generalSettings.totalControlB`, fixture belum ada), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Sesi API tiap aktor disediakan tim FE/BE.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- Seeding di hook `before` (17 PUT berurutan ke `/v2/enterprise-management/general-settings` full-replace, `global-settings/general-settings/API/openapi.yaml`; tiap PUT mengubah tepat satu field; pelaku dan perubahan): (1) Budi S `sessionIdleTimeout` 30 ke 60; (2) Andi W 60 ke 120; (3) sampai (10) Budi S bergantian 120 ke 60, 60 ke 120, dan seterusnya (delapan perubahan: 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120); (11) Budi S 120 ke 30; (12) Budi S `currencyCode` `IDR` ke `USD`; (13) Budi S `USD` ke `IDR`; (14) Budi S `timezone` `Asia/Jakarta` ke `UTC`; (15) Andi W `UTC` ke `Asia/Jakarta`; (16) Budi S `timeFormat` `HH:mm` ke `hh:mm a`; (17) Andi W `hh:mm a` ke `HH:mm`. Record berakhir pada baseline. Hasil seeding: 17 baris Changelog (N dari seeding, bagian 8b butir 10), terdiri dari 14 baris oleh `Budi S` dan 3 baris oleh `Andi W`; Field `Session Idle Timeout` (11 baris, PUT 1 sampai 11, terlama), `Currency Code` (2), `Time Zone` (2), dan `Time Format` (2) sebagai enam baris terbaru (PUT 12 sampai 17), sehingga 10 baris terbaru (halaman 1 pada Date menurun dan page size 10) memuat Field `Currency Code`, `Time Zone`, `Time Format`, dan `Session Idle Timeout`. Dengan Search `Edit` (Action seluruh baris `Edit`) tersedia 17 baris (halaman 2 tersedia pada page size 10). Entri dari spec lain dan hook ikut menambah baris; total entri tidak diasersi sebagai angka (S-12).
- Data uji: kata kunci `Edit`, `Time`; Field `Session Idle Timeout`, `Currency Code`; Modified By `Budi S`; sort Field Ascending dan Modified By Ascending.
- State yang diubah dan dipulihkan: Search, Filter, Sort, dan halaman aktif Modal Changelog; dikosongkan dengan menutup lalu membuka kembali Modal Changelog (PRD §4.2b: kondisi default) pada langkah 14 dan 25.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-155: Ganti kolom sort saat Search dan Filter aktif: saringan tidak di-reset

1. Klik icon Changelog di pojok kanan atas halaman
2. Ketik Search `Edit`, tekan Enter
3. Klik Filter di toolbar
4. Pilih Field `Session Idle Timeout`
5. Klik `[Apply]`
6. Klik header kolom Field sekali (Ascending)
7. Klik header kolom Modified By sekali (Ascending)
8. Verifikasi indikator sort Modified By Ascending aktif
9. Verifikasi indikator sort kolom Field tidak tampil
10. Verifikasi kotak Search tetap berisi `Edit`
11. Klik Filter di toolbar
12. Verifikasi chip Field `Session Idle Timeout` tetap tampil di Filter Panel
13. Tutup Filter Panel dengan menekan `Esc`
14. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-156: Kombinasi Search dan Filter tanpa hasil lalu Clear Field memulihkan tabel

15. Klik Filter di toolbar
16. Pilih Field `Currency Code`
17. Klik `[Apply]`
18. Ketik Search `Time`, tekan Enter
19. Verifikasi empty state `No results found`
20. Verifikasi empty state `Try adjusting your search or filter.`
21. Klik Filter di toolbar
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Verifikasi tabel menampilkan baris yang cocok dengan keyword `Time`: baris Field `Time Zone`, `Time Format`, dan `Session Idle Timeout`
25. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-157: Search dan Apply Filter saat di halaman 2 mereset ke halaman 1

26. Klik halaman 2 pada Pagination
27. Verifikasi halaman 2 aktif pada Pagination
28. Ketik Search `Edit`, tekan Enter
29. Verifikasi halaman 1 aktif pada Pagination (tabel kembali ke halaman 1 setelah Search)
30. Klik halaman 2 pada Pagination
31. Verifikasi halaman 2 aktif pada Pagination
32. Klik Filter di toolbar
33. Pilih Modified By `Budi S`
34. Klik `[Apply]`
35. Verifikasi halaman 1 aktif pada Pagination (tabel kembali ke halaman 1 setelah Apply Filter)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dari backend nyata). Pelaku kedua (Andi W) hanya memicu perubahan state lewat sesi API di hook `before`; tidak ada sesi UI kedua.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (155, 156, 157) dipertahankan. TC-181 dan TC-182 ada di spec 053; slug folder (`...-reset-halaman-dan-buka-ulang`) mengikuti id yang tidak di-renumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog); langkah 14 dan 25 (menutup Modal Changelog lalu membukanya kembali agar Search, Filter, Sort, dan halaman kembali ke default dan blok berikutnya mulai bersih; PRD §4.2b); langkah 13 (menutup Filter Panel yang dibuka untuk memeriksa chip). Langkah 26 memakai Modal Changelog yang baru dibuka pada langkah 25; halaman 2 tersedia dari seeding 17 baris. Blok TC-157 tidak ditutup di akhir spec karena tidak ada blok sesudahnya.
- Asersi tambahan (konkretisasi, S-03): langkah 27 dan 31 (halaman aktif sebelum aksi) adalah anchor bagi asersi reset halaman. Langkah 9 (absence indikator sort Field) didahului langkah 8 (indikator Modified By tampil) sebagai anchor positif.
- Spec 35 langkah, dalam ambang sekitar 35 langkah. Tiga TC berbagi dataset Changelog yang sama (17 baris, dua aktor) pada satu kelas harness (fungsional, Search/Filter/Sort/Pagination) dan tiap blok membuka ulang modal agar state bersih.
- Pembagian TC lintas spec: TC-GS-GSET-181 dan 182 (retensi antar halaman dan buka ulang modal) ada di spec 053; TC-GS-GSET-151 sampai 154 (kombinasi awal) ada di spec 038; TC-GS-GSET-102 dan 180 (pagination) di spec 037; TC-GS-GSET-77 di spec 030; TC-GS-GSET-81 di spec 032.
- Temuan untuk QA:
  - TC-GS-GSET-156: Expected b menyebut baris Field `Time Zone`, `Time Format`, dan `Session Idle Timeout` cocok dengan keyword `Time` (substring `Time` pada `Timeout`). Langkah 1 memilih Field `Currency Code`, sehingga opsi itu hanya ada bila Changelog memuat sedikitnya satu baris Field `Currency Code` (opsi filter Field populate dari data tabel, PRD §9.5); TC tidak menyebut baris Currency pada data dasar. Spec men-seed dua baris Currency Code.
  - TC-GS-GSET-157: halaman 2 membutuhkan sedikitnya 11 baris; jumlah itu berasal dari seeding (Prerequisites), tidak dari tabel satu halaman.
