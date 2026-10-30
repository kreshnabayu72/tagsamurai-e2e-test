---
id: TC-GS-GSET-E2E-053-changelog-retensi-saringan-antar-halaman-dan-buka-ulang-kondisi-default
title: "Changelog General Settings: Retensi Search, Filter, dan Sort Antar Halaman serta Modal Dibuka Kembali Tampil Kondisi Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-181
  - TC-GS-GSET-182
coverage:
  web: automated
---

# Changelog General Settings: Retensi Search, Filter, dan Sort Antar Halaman serta Modal Dibuka Kembali Tampil Kondisi Default

## Prerequisites

- Mode: FE+BE. Spec tidak melakukan aksi tulis lewat UI; riwayat di-seed lewat API.
- Akun aktor UI: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding (sesi API, tanpa sesi UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2; `Fixture.generalSettings.totalControlB`, fixture belum ada), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Sesi API tiap aktor disediakan tim FE/BE.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- Seeding di hook `before` (17 PUT berurutan ke `/v2/enterprise-management/general-settings` full-replace, `global-settings/general-settings/API/openapi.yaml`; tiap PUT mengubah tepat satu field; pelaku dan perubahan): (1) Budi S `sessionIdleTimeout` 30 ke 60; (2) Andi W 60 ke 120; (3) sampai (10) Budi S bergantian 120 ke 60, 60 ke 120, dan seterusnya (delapan perubahan: 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120, 120 ke 60, 60 ke 120); (11) Budi S 120 ke 30; (12) Budi S `currencyCode` `IDR` ke `USD`; (13) Budi S `USD` ke `IDR`; (14) Budi S `timezone` `Asia/Jakarta` ke `UTC`; (15) Andi W `UTC` ke `Asia/Jakarta`; (16) Budi S `timeFormat` `HH:mm` ke `hh:mm a`; (17) Andi W `hh:mm a` ke `HH:mm`. Hook menunggu pergantian menit (maksimum 60 detik) antara PUT 14 dan PUT 15 supaya kolom Date berketelitian menit punya sedikitnya dua nilai distinct pada halaman 1 (S-11; bagian 6 konvensi). Record berakhir pada baseline. Hasil seeding: 17 baris Changelog (N dari seeding, bagian 8b butir 10), terdiri dari 14 baris oleh `Budi S` dan 3 baris oleh `Andi W`; Field `Session Idle Timeout` (11 baris, PUT 1 sampai 11, terlama), `Currency Code` (2), `Time Zone` (2), dan `Time Format` (2) sebagai enam baris terbaru (PUT 12 sampai 17), sehingga 10 baris terbaru (halaman 1 pada Date menurun dan page size 10) memuat Field `Currency Code`, `Time Zone`, `Time Format`, dan `Session Idle Timeout`. Dengan Search `Edit` (Action seluruh baris `Edit`) tersedia 17 baris (halaman 2 tersedia pada page size 10) dan dengan tambahan Filter Modified By `Budi S` tersedia 14 baris (sedikitnya 11, halaman 2 tersedia; Data Uji Dinamis No 4). Entri dari spec lain dan hook ikut menambah baris; total entri tidak diasersi sebagai angka (S-12).
- Data uji: kata kunci `Edit`, `Time`; Field `Session Idle Timeout`, `Currency Code`; Modified By `Budi S`; sort Field Ascending dan Modified By Ascending.
- State yang diubah dan dipulihkan: Search, Filter, Sort, dan halaman aktif Modal Changelog; dikosongkan dengan menutup lalu membuka kembali Modal Changelog (PRD §4.2b: kondisi default) pada langkah 29 dan 35 sampai 36.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-181: Pindah halaman mempertahankan Search, Filter, dan Sort

1. Klik icon Changelog di pojok kanan atas halaman
2. Ketik Search `Edit`, tekan Enter
3. Klik Filter di toolbar
4. Pilih Modified By `Budi S`
5. Klik `[Apply]`
6. Klik header kolom Field sekali (Ascending)
7. Klik halaman 2 pada Pagination
8. Verifikasi halaman 2 aktif pada Pagination
9. Verifikasi kotak Search tetap berisi `Edit`
10. Klik Filter di toolbar
11. Verifikasi chip Modified By `Budi S` tetap tampil di Filter Panel
12. Tutup Filter Panel dengan menekan `Esc`
13. Verifikasi indikator sort Field Ascending tetap aktif
14. Verifikasi halaman 2 menampilkan sedikitnya satu baris
15. Verifikasi setiap baris halaman 2 bernilai Modified By `Budi S`
16. Verifikasi setiap baris halaman 2 bernilai Action `Edit`
17. Verifikasi baris halaman 2 terurut Field A-Z
18. Klik halaman 1 pada Pagination
19. Verifikasi halaman 1 aktif pada Pagination
20. Verifikasi kotak Search tetap berisi `Edit`
21. Klik Filter di toolbar
22. Verifikasi chip Modified By `Budi S` tetap tampil di Filter Panel
23. Tutup Filter Panel dengan menekan `Esc`
24. Verifikasi indikator sort Field Ascending tetap aktif
25. Verifikasi halaman 1 menampilkan sedikitnya satu baris
26. Verifikasi setiap baris halaman 1 bernilai Modified By `Budi S`
27. Verifikasi setiap baris halaman 1 bernilai Action `Edit`
28. Verifikasi baris halaman 1 terurut Field A-Z
29. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-182: Modal Changelog dibuka kembali tampil kondisi default

30. Ketik Search `Edit`, tekan Enter
31. Klik Filter di toolbar
32. Pilih Field `Session Idle Timeout`
33. Klik `[Apply]`
34. Klik header kolom Modified By sekali (Ascending)
35. Tutup Modal Changelog dengan menekan `Esc`
36. Klik icon Changelog di pojok kanan atas halaman
37. Verifikasi kotak Search kosong
38. Verifikasi tabel tidak tersaring oleh Search dan Filter: tabel memuat baris Field `Time Zone` dan baris Field `Session Idle Timeout`
39. Klik Filter di toolbar
40. Verifikasi field Field menampilkan placeholder `All fields` (Filter Panel tanpa kriteria)
41. Tutup Filter Panel dengan menekan `Esc`
42. Verifikasi tidak ada indikator sort aktif pada kolom Modified By
43. Verifikasi urutan baris Date descending (Newest First)
44. Verifikasi Pagination menampilkan halaman 1
45. Verifikasi page size 10

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dari backend nyata). Pelaku kedua (Andi W) hanya memicu perubahan state lewat sesi API di hook `before`; tidak ada sesi UI kedua.
- TC-181 dan TC-182 ada di spec ini; TC-155 sampai 157 ada di spec 039. Seeding, akun, dan hook sama dengan spec 039 kecuali jeda ganti menit yang hanya ada di spec ini (tiap spec berdiri sendiri, S-04, S-06). Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (181, 182) dipertahankan; TC-182 di akhir karena menguji pembukaan ulang modal (prinsip 6 konvensi: buka ulang terakhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog); langkah 29 (menutup Modal Changelog lalu membukanya kembali agar blok TC-182 mulai bersih); langkah 12, 23, dan 41 (menutup Filter Panel yang dibuka untuk memeriksa chip atau placeholder). Langkah 35 dan 36 adalah aksi TC-182 (tutup lalu buka kembali modal).
- Asersi tambahan (konkretisasi, S-03): langkah 8 dan 19 (halaman aktif sesudah pindah halaman) adalah anchor bagi asersi retensi; langkah 14 dan 25 adalah pembanding generik "sedikitnya satu baris" sebelum asersi universal pada langkah 15 dan 26 (bagian 8b butir 2); langkah 16 dan 27 mengasersi Action `Edit` pada setiap baris halaman 2 dan halaman 1 (kriteria keyword `Edit` pada Expected b TC-181); langkah 38 menjabarkan "tabel tidak tersaring" dengan dua nilai Field distinct.
- Langkah 37 sampai 45 memecah Expected a, b, c, dan d TC-182 satu `Verifikasi` per klausa (S-01): Expected c ("tidak ada indikator sort aktif pada Modified By; urutan Date descending") menjadi langkah 42 dan 43; Expected d menjadi langkah 44 dan 45. Langkah 9 sampai 13 dan 20 sampai 24 memecah Expected a TC-181 (tiga kondisi) per klausa untuk halaman 2 dan halaman 1.
- Spec melewati sekitar 35 langkah (45 langkah) karena TC-181 memverifikasi empat kondisi pada dua halaman (blok langkah 8 sampai 17 dan 19 sampai 28 berpola sama untuk halaman 2 lalu halaman 1; lihat 8b butir 7: parameter iterasi halaman 2 dan halaman 1) dan TC-182 memecah empat Expected menjadi sembilan `Verifikasi` (S-01). Kedua TC berbagi dataset Changelog yang sama (17 baris, dua aktor) pada satu kelas harness (fungsional, Search/Filter/Sort/Pagination). Pemecahan lebih lanjut menggandakan hook dan login tanpa menambah makna; blok 182 membuka modal dan menyetel saringannya sendiri sehingga tetap bermakna bila blok 181 gagal.
- Langkah 17 dan 28 mengasersi arah urutan Field A-Z pada baris `Budi S` hasil Search `Edit`; urutan Field bukan urutan Date, sehingga seeding tidak menjamin dua nilai Field distinct pada halaman teramati (baris `Budi S` dari spec lain ikut menambah baris), dan kedua langkah tidak dihitung bukti sort penuh (S-14). Seeding terbaru hanya menjamin komposisi halaman 1 pada urutan Date menurun (langkah 38 dan 43).
- Pembagian TC lintas spec: TC-GS-GSET-155 sampai 157 (kombinasi lanjutan, reset halaman) di spec 039; TC-GS-GSET-151 sampai 154 di spec 038; TC-GS-GSET-102 dan 180 (pagination) di spec 037.
- Temuan untuk QA:
  - TC-GS-GSET-181 Expected b: semua baris Changelog bernilai Action `Edit`, sehingga klausa keyword `Edit` pada langkah 16 dan 27 tidak membedakan hasil Search dari hasil tanpa keyword; keterbatasan ini ada pada TC (keyword `Edit` tidak menyaring apa pun).
  - TC-GS-GSET-181: halaman 2 membutuhkan hasil Search dan Filter sedikitnya 11 baris; jumlah itu berasal dari seeding (Prerequisites), tidak dari tabel satu halaman.
  - TC-GS-GSET-182 Expected c: urutan Date descending hanya teramati bila ada sedikitnya dua nilai Date berbeda; TC tidak menyebut jeda antar-Save. Spec memakai jeda menit di seeding.
