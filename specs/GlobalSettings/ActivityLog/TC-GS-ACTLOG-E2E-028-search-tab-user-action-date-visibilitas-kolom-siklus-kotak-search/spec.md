---
id: TC-GS-ACTLOG-E2E-028-search-tab-user-action-date-visibilitas-kolom-siklus-kotak-search
title: "Search Tab User Action: Date, Visibilitas Kolom, Siklus Kotak Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-154
  - TC-GS-ACTLOG-155
  - TC-GS-ACTLOG-158
coverage:
  web: automated
---

# Search Tab User Action: Date, Visibilitas Kolom, Siklus Kotak Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas log-terbatas segar milik spec ini, `Fixture.activityLog.entitasLog028` (entitas uji dengan log User Action terbatas, Tabel Data Uji Pre-setup baris 13; disediakan tim FE/BE, email ditetapkan tim FE), kredensial `Spectra.env.GS_LIMITLOG_TC_PASSWORD` (semua akun Total Control entitas log-terbatas berbagi password ini). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Activity Log > tab User Action.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md). Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun `Fixture.activityLog.entitasLog028` dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Environment variable: `GS_LIMITLOG_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Alasan entitas log-terbatas: TC-GS-ACTLOG-154 dan 155 mengasersi "tidak ada baris" untuk kata kunci `14 Jun 26`, `14 Jun 2026` dan `Division`; pada Client A yang dipakai bersama seluruh suite, kata kunci itu bisa cocok dengan baris milik spec lain. Entitas ini dipakai hanya oleh spec 028 dan tidak dipakai bersama spec lain.
- Kemampuan teknis (disediakan tim FE/BE, tanpa mengarang endpoint): seed BE dua entri User Action pada entitas log-terbatas di hook `before`, karena entri bertanggal 14 Jun 2026 tidak dapat dihasilkan aksi nyata dan log tidak dapat diubah atau dihapus (ACTLOG-LOGIC-01). Entitas segar, sehingga keadaan log sebelum spec berjalan adalah persis dua entri berikut (tidak ada entri lain pada entitas):

| Date | Action | Object | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| `14 Jun 26` (14 Jun 2026) | `Edit` | `User` | `Siti Nurbaya {runId}-028` | `Division` | `Marketing` | `Finance` | Admin entitas (nama tampil ditetapkan tim FE) |
| 15 Jun 2026 (bulan `Jun`) | `Import` | `Position` | `—` | `—` | `—` | `—` | `Wulan` |

  Entri kedua sengaja tidak memuat huruf `e` pada kolom mana pun (Action `Import`, Object `Position`, Modified By `Wulan`, Date bulan `Jun`) agar penyaringan kata kunci `e` pada TC-GS-ACTLOG-158 teramati.
- Format tanggal: General Settings Date Format entitas log-terbatas `DD MMM YY` (nilai Pre-setup, diasumsikan tim FE; spec tidak mengubahnya).
- Data uji Search: `14 Jun 26`, `14 Jun 2026` (TC-GS-ACTLOG-154); `Division`, `Siti` (TC-GS-ACTLOG-155); `e`, `edit` (TC-GS-ACTLOG-158).
- State global yang diubah: visibilitas kolom Field tabel User Action (disimpan di cache browser per user, per tab, PRD activity-log.md §4.1). Dipulihkan di langkah 20 dan di hook `after` sebagai cadangan (centang kolom Field kembali lewat Column Visibility).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-154: Kolom Date tidak dapat dicari lewat Search

1. Verifikasi tabel menampilkan entri `Edit` `User` `Siti Nurbaya {runId}-028` dengan Date `14 Jun 26`
2. Ketik Search `14 Jun 26`, tekan Enter
3. Verifikasi tabel tidak menampilkan baris berdasarkan tanggal
4. Verifikasi tampil `"No results found"`
5. Ganti isi kotak search dengan `14 Jun 2026`, tekan Enter
6. Verifikasi tabel tidak menampilkan baris berdasarkan tanggal
7. Verifikasi tampil `"No results found"`
8. Klik icon Filter
9. Verifikasi Filter Panel memuat field `Date` (penyaringan tanggal dilakukan lewat Filter Panel)
10. Klik icon Filter untuk menutup Filter Panel

### TC-GS-ACTLOG-155: Search terikat visibilitas kolom

11. Kosongkan isi kotak search, tekan Enter
12. Klik header `Column Visibility (⋯)`, hilangkan centang kolom Field
13. Verifikasi kolom Field hilang dari tabel
14. Verifikasi tabel menampilkan baris `Siti Nurbaya {runId}-028` tanpa kolom Field (pembanding sebelum pencarian `Division`)
15. Ketik Search `Division`, tekan Enter
16. Verifikasi tabel tidak menampilkan baris
17. Verifikasi tampil `"No results found"`
18. Ganti isi kotak search dengan `Siti`, tekan Enter
19. Verifikasi tabel menampilkan baris `Siti Nurbaya {runId}-028` (kolom Name tetap tampil)
20. Klik header `Column Visibility (⋯)`, centang kembali kolom Field
21. Verifikasi kolom Field tampil kembali
22. Ganti isi kotak search dengan `Division`, tekan Enter
23. Verifikasi tabel menampilkan baris `Siti Nurbaya {runId}-028`

### Pemulihan state antar TC

24. Klik `(←)` pada kotak Search (menutup kotak dan mereset tabel)

### TC-GS-ACTLOG-158: Siklus interaksi kotak Search toolbar Tab User Action

25. Arahkan kursor ke icon Search
26. Verifikasi tooltip `Search` tampil
27. Klik icon Search
28. Verifikasi kotak Search melebar
29. Verifikasi kursor otomatis fokus di kotak Search
30. Verifikasi placeholder kotak Search `"Search user action log..."`
31. Ketik `e` pada kotak Search
32. Verifikasi icon `(✕)` muncul di kanan dalam kotak
33. Verifikasi tabel belum tersaring (entri `Import` `Position` tetap tampil)
34. Tekan Enter
35. Verifikasi tabel tersaring sesuai `e` (baris `Edit` `Siti Nurbaya {runId}-028` tampil)
36. Verifikasi baris `Import` `Position` tidak tampil
37. Klik icon `(✕)` di dalam kotak
38. Verifikasi teks di kotak Search terhapus
39. Verifikasi kotak Search tetap terbuka dan fokus
40. Verifikasi tabel tetap menampilkan hasil `e` terakhir (baris `Import` `Position` tidak tampil)
41. Tekan Enter pada kotak kosong
42. Verifikasi tabel kembali menampilkan data tanpa saringan pencarian (baris `Edit` dan `Import` tampil)
43. Ketik Search `edit`, tekan Enter, klik icon `(←)`
44. Verifikasi kotak Search menutup menjadi icon Search
45. Verifikasi tabel langsung kembali menampilkan data tanpa saringan pencarian (baris `Edit` dan `Import` tampil)
46. Klik icon Search
47. Verifikasi isi kotak Search kosong

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Alasan spec di atas smell 35 langkah: 47 langkah, tanpa pengulangan. Ketiga TC satu topik (Search Tab User Action), satu akun, satu entitas, satu dataset seed, dan tidak memuat kelas harness lain; tiap TC berdiri sendiri (keadaan Search dibersihkan di antara TC) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah `Verifikasi` hasil pecahan klausa Expected (S-01).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (menutup Filter Panel), langkah 11 (mengosongkan Search `14 Jun 2026` dari TC-GS-ACTLOG-154 sebelum TC-GS-ACTLOG-155, yang dimulai dari tabel tanpa Search aktif), langkah 24 (menutup kotak Search sebelum TC-GS-ACTLOG-158), dan langkah 46 (membuka kembali kotak Search setelah `(←)` untuk memeriksa isinya).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 1 (anchor positif sebelum asersi "No results found" pada TC-GS-ACTLOG-154, 8b butir 2), langkah 9 (Expected b TC-GS-ACTLOG-154 menyebut "penyaringan tanggal dilakukan lewat Filter Panel"; diamati sebagai field `Date` di Filter Panel), langkah 14 (anchor baris sebelum asersi "No results found" pada TC-GS-ACTLOG-155), langkah 33 dan 36 (anchor baris yang diasersi tersaring pada TC-GS-ACTLOG-158), dan langkah 47 (Expected f menyebut isi dikosongkan; hanya teramati setelah kotak dibuka lagi).
- Urutan langkah 25 sampai 30 mengikuti urutan state (konvensi 8b butir 5): tooltip `Search` diasersi sebelum klik, karena hover menghilang setelah kotak melebar; Expected a TC-GS-ACTLOG-158 menyebut tooltip terakhir.
- Pembagian TC: TC-GS-ACTLOG-150 sampai 153, 156, 157 (Search kolom teks, case, nama, trim, multi-kolom) ada di spec 027.
- Temuan untuk QA:
  - TC-GS-ACTLOG-154 dan 155 mengasersi "tidak ada baris" untuk kata kunci tertentu: hanya benar pada entitas yang log User Action-nya terbatas. Entitas segar per spec (`Fixture.activityLog.entitasLog028`) dan isi dua entri pada Prerequisites ditetapkan spec; Tabel Data Uji Pre-setup baris 13 tidak merinci isi entitas itu.
  - TC-GS-ACTLOG-154: precondition menyebut tanggal `14 Jun 2026` dengan Date Format `DD MMM YY`, sehingga tampil `14 Jun 26`. TC tidak menyebut apakah jam ikut dicari (mis. `14 Jun 26, 14:05`); spec mengikuti dua kata kunci TC.
  - TC-GS-ACTLOG-158 langkah 2 mengasersi tabel "tersaring sesuai `e`" tanpa menyebut baris yang tersaring keluar; spec menambah entri `Import` `Position` tanpa huruf `e` di seed. Data TC "log User Action bervariasi" tidak cukup untuk asersi itu.
  - TC-GS-ACTLOG-158 Expected a menyebut tooltip hover `Search` tanpa menyebut elemen yang di-hover (sebelum atau sesudah kotak melebar); spec meng-hover icon sebelum klik.
