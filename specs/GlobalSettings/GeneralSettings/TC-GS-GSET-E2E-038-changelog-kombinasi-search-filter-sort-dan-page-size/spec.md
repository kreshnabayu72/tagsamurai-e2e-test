---
id: TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size
title: "Changelog General Settings: Kombinasi Search, Filter, Sort, dan Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-151
  - TC-GS-GSET-152
  - TC-GS-GSET-153
  - TC-GS-GSET-154
coverage:
  web: automated
---

# Changelog General Settings: Kombinasi Search, Filter, Sort, dan Page Size

## Prerequisites

- Mode: FE+BE. Spec tidak melakukan aksi tulis lewat UI; riwayat di-seed lewat API.
- Akun aktor UI: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Akun pelaku seeding (sesi API, tanpa sesi UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2; `Fixture.generalSettings.totalControlB`, fixture belum ada), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Sesi API tiap aktor disediakan tim FE/BE.
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- Seeding di hook `before` (delapan PUT `/v2/enterprise-management/general-settings` full-replace, `global-settings/general-settings/API/openapi.yaml`; tiap PUT mengubah tepat satu field; urutan dan pelaku): (1) Budi S `sessionIdleTimeout` 30 ke 15 menit (`30 minutes` ke `15 minutes`); (2) Budi S 15 ke 60 (`15 minutes` ke `1 hour`); (3) Andi W 60 ke 120 (`1 hour` ke `2 hours`); (4) Budi S 120 ke 30 (`2 hours` ke `30 minutes`); (5) Budi S `timezone` `Asia/Jakarta` ke `UTC`; (6) Andi W `timezone` `UTC` ke `Asia/Jakarta`; (7) Budi S `timeFormat` `HH:mm` ke `hh:mm a`; (8) Andi W `timeFormat` `hh:mm a` ke `HH:mm`. Record berakhir pada baseline. Hasil: baris Field `Session Idle Timeout` (empat baris; tiga oleh `Budi S`, satu oleh `Andi W`; tepat satu baris, Old Value `30 minutes` New Value `15 minutes`, tidak memuat kata `hour`), `Time Zone` (dua baris, satu oleh tiap aktor), dan `Time Format` (dua baris, satu oleh tiap aktor), sehingga kolom Field dan Modified By punya sedikitnya dua nilai distinct (S-11). Entri dari spec lain dan hook ikut menambah baris; total entri tidak diasersi sebagai angka (S-12). Baris seeding adalah baris terbaru Changelog; asersi urutan Modified By pada langkah 52 memakai `Andi W`, nilai A-Z terkecil yang dijamin seeding. Langkah 46 mencatat total hasil Pagination sebagai baseline `{nHour}` dan langkah 49 membandingkannya secara relatif (S-12).
- Data uji: kata kunci `Time`, `hour`, `Edit`; Field `Time Zone`, `Session Idle Timeout`; Modified By `Budi S`; sort Field Ascending dan Modified By Ascending; page size 25.
- State yang diubah dan dipulihkan: Search, Filter, Sort, dan page size Modal Changelog; dikosongkan dengan menutup lalu membuka kembali Modal Changelog (PRD §4.2b: kondisi default) pada langkah 10, 21, dan 40.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-151: Search lalu Filter: hasil berupa irisan dan keyword tetap aktif

1. Klik icon Changelog di pojok kanan atas halaman
2. Ketik Search `Time`, tekan Enter
3. Verifikasi tabel memuat baris Field `Time Zone` dan baris Field `Time Format`
4. Klik Filter di toolbar
5. Pilih Field `Time Zone`
6. Klik `[Apply]`
7. Verifikasi tabel menampilkan sedikitnya satu baris
8. Verifikasi setiap baris tabel bernilai Field `Time Zone` (cocok dengan keyword `Time`)
9. Verifikasi kotak Search tetap berisi `Time` setelah Apply
10. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-152: Filter lalu Search: filter tetap aktif

11. Klik Filter di toolbar
12. Pilih Field `Session Idle Timeout`
13. Klik `[Apply]`
14. Ketik Search `hour`, tekan Enter
15. Verifikasi tabel menampilkan sedikitnya satu baris
16. Verifikasi setiap baris tabel bernilai Field `Session Idle Timeout`
17. Verifikasi Old Value atau New Value setiap baris tabel memuat `hour`
18. Klik Filter di toolbar
19. Verifikasi chip Field `Session Idle Timeout` tetap tampil di Filter Panel
20. Tutup Filter Panel dengan menekan `Esc`
21. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-153: Kombinasi Search, Filter, Sort, dan page size aktif bersamaan

22. Ketik Search `Edit`, tekan Enter
23. Verifikasi tabel memuat baris Modified By `Budi S` dan baris Modified By `Andi W`
24. Klik Filter di toolbar
25. Pilih Modified By `Budi S`
26. Klik `[Apply]`
27. Klik header kolom Field sekali (Ascending)
28. Ubah page size ke 25
29. Verifikasi tabel menampilkan sedikitnya satu baris
30. Verifikasi setiap baris tabel bernilai Action `Edit` (cocok dengan keyword `Edit`)
31. Verifikasi setiap baris tabel bernilai Modified By `Budi S`
32. Verifikasi baris terurut Field A-Z
33. Verifikasi tabel menampilkan paling banyak 25 baris per halaman
34. Klik Filter di toolbar
35. Verifikasi kotak Search tetap berisi `Edit`
36. Verifikasi chip Modified By `Budi S` tetap tampil di Filter Panel
37. Verifikasi indikator sort Field Ascending tetap aktif
38. Verifikasi page size 25 tetap aktif
39. Tutup Filter Panel dengan menekan `Esc`
40. Tutup Modal Changelog dengan menekan `Esc`, lalu klik icon Changelog di pojok kanan atas halaman

### TC-GS-GSET-154: Clear Search saat Filter dan Sort aktif: filter dan sort tetap berlaku

41. Klik Filter di toolbar
42. Pilih Field `Session Idle Timeout`
43. Klik `[Apply]`
44. Klik header kolom Modified By sekali (Ascending)
45. Ketik Search `hour`, tekan Enter
46. Catat total hasil pada Pagination sebagai `{nHour}`
47. Klik `✕` pada Search, tekan Enter pada input kosong
48. Verifikasi kotak Search kosong (keyword dilepas)
49. Verifikasi total hasil pada Pagination lebih besar dari `{nHour}` (keyword `hour` dilepas; baris Old Value `30 minutes` dan New Value `15 minutes` yang tidak memuat `hour` ikut dihitung)
50. Verifikasi setiap baris tabel bernilai Field `Session Idle Timeout` (filter Field tetap aktif)
51. Verifikasi indikator sort Modified By Ascending tetap aktif
52. Verifikasi baris pertama bernilai Modified By `Andi W` (urutan A-Z)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dari backend nyata). Pelaku kedua (Andi W) hanya memicu perubahan state lewat sesi API di hook `before`; tidak ada sesi UI kedua (P-2 tidak dipakai karena tanpa konteks kedua kelas c).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (151, 152, 153, 154) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog); langkah 10, 21, dan 40 (menutup Modal Changelog lalu membukanya kembali agar Search, Filter, Sort, dan page size kembali ke default dan blok berikutnya mulai bersih; PRD §4.2b); langkah 20 dan 39 (menutup Filter Panel yang dibuka untuk memeriksa chip); langkah 46 (mencatat `{nHour}`). Langkah 47 ditulis "klik `✕` pada Search, tekan Enter" sesuai TC (langkah 4 TC-154); kotak Search kosong pada saat Enter.
- Asersi tambahan (konkretisasi, S-03): langkah 3 dan 23 adalah pembanding positif (hasil Search sebelum Filter memuat lebih dari satu nilai Field atau Modified By) agar asersi universal pada langkah 8 dan 31 bermakna; langkah 7, 15, dan 29 adalah pembanding generik "sedikitnya satu baris" sebelum asersi universal (bagian 8b butir 2). Langkah 49 memastikan baris yang tidak memuat `hour` kembali tampil setelah keyword dilepas (total hasil lebih besar dari `{nHour}`), sehingga Expected a TC-154 ("semua baris Field `Session Idle Timeout`") terbukti, bukan hasil Search sebelumnya. Langkah 17 menjabarkan "yang Old Value atau New Value-nya memuat `hour`" dari Expected a TC-152.
- Langkah 35 sampai 38 memecah Expected d TC-153 (satu butir "keempat kondisi tetap aktif bersamaan") menjadi satu `Verifikasi` per kondisi; Expected a, b, dan c TC-153 punya `Verifikasi` sendiri (langkah 30 dan 31, 32, 33).
- Spec melewati sekitar 35 langkah (52 langkah) karena empat TC berbagi dataset Changelog yang sama pada satu kelas harness (fungsional, Search/Filter/Sort), tiap blok memerlukan pembukaan ulang modal agar state bersih (langkah 10, 21, 40), dan Expected dipecah satu `Verifikasi` per klausa (S-01). Blok-blok berdiri sendiri sesudah pembukaan ulang modal, sehingga kegagalan satu blok tidak menghilangkan makna blok lain; spec tidak dipecah karena dataset dan seeding identik dan pemecahan hanya menggandakan hook dan login.
- Dipisah dari spec 037, 039, dan 053 karena gabungan langkahnya melewati batas ukuran jauh (22 + 52 + 35 + 45 = 154 langkah) dan seeding berbeda (spec ini delapan PUT; spec 037 28 PUT; spec 039 dan 053 masing-masing 17 PUT).
- Pembagian TC lintas spec: TC-GS-GSET-155, 156, dan 157 (kombinasi lanjutan) ada di spec 039 dan TC-GS-GSET-181 dan 182 di spec 053; TC-GS-GSET-73 sampai 78 (Filter) di spec 030; TC-GS-GSET-66 sampai 70 (Search) di spec 028; TC-GS-GSET-82 dan 83 (Sort) di spec 033.
- Temuan untuk QA:
  - TC-GS-GSET-151, 152, 153, 154: TC tidak menyebut pelaku dan nilai data yang menjamin kolom Field dan Modified By punya lebih dari satu nilai; spec men-seed delapan perubahan oleh dua aktor (Prerequisites). TC-GS-GSET-152 mengharapkan baris yang Old Value atau New Value-nya memuat `hour`, tetapi seluruh baris `Session Idle Timeout` pada data uji dasar TC (30 minutes ke 1 hour) memuat kata itu; spec menambah satu baris `30 minutes` ke `15 minutes` agar penyaringan oleh keyword terbukti.
  - TC-GS-GSET-153: Expected b menyebut "Field A-Z" tanpa kriteria jika nilai Field sama; spec mengasersi urutan atas sedikitnya dua nilai Field distinct milik `Budi S`.
