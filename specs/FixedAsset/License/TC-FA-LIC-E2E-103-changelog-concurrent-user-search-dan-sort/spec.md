---
id: TC-FA-LIC-E2E-103-changelog-concurrent-user-search-dan-sort
title: "Search Modal Changelog Concurrent User: Reveal, Kolom Searchable, dan Guard Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-567
  - TC-FA-LIC-568
  - TC-FA-LIC-586
coverage:
  web: automated
---

# Search Modal Changelog Concurrent User: Reveal, Kolom Searchable, dan Guard Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Concurrent User #31 (4 entri) lewat `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE).

  | Date | Action | User Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Force Logout | Budi Santoso | Session Status | Active | Force Logged Out | Rudi H |
  | 29/09/26 14:20 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |
  | 28/09/26 09:40 | Force Logout | Andi Pratama | Session Status | Active | Force Logged Out | Rudi H |
  | 27/09/26 16:05 | Force Logout | Siti Rahma | Session Status | Active | Force Logged Out | Dewi L |

- Data Uji Search kolom teks Searchable (TC-FA-LIC-567), dipakai langkah 25 sampai 27:

  | Kolom | Kata kunci | Hasil (Date) |
  |---|---|---|
  | Action | `force` | 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05 |
  | User Name | `andi` | 28/09/26 09:40 |
  | Field | `status` | 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05 |
  | Old Value | `active` | 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05 |
  | New Value | `logged out` | 30/09/26 11:15, 29/09/26 14:20, 28/09/26 09:40, 27/09/26 16:05 |
  | Modified By | `dewi` | 29/09/26 14:20, 27/09/26 16:05 |

- Spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar

### TC-FA-LIC-586: Search reveal, auto-focus, placeholder, tooltip, Enter, clear, dan collapse

2. Klik ikon Search pada toolbar
3. Verifikasi Search bar melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, user name...`
6. Arahkan kursor ke ikon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter `s` pada kotak Search
9. Verifikasi icon `(×)` muncul
10. Verifikasi tabel belum tersaring (4 baris tetap tampil, bukan live-as-you-type)
11. Ganti isi kotak search dengan `siti`, tekan Enter
12. Verifikasi tabel tersaring: 29/09/26 14:20, 27/09/26 16:05
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak tetap terbuka dan fokus
16. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: 29/09/26 14:20, 27/09/26 16:05
17. Tekan Enter pada kotak kosong
18. Verifikasi semua 4 baris kembali tampil
19. Ketik `siti` pada kotak Search
20. Klik icon panah `(←)` di kiri toolbar
21. Verifikasi kotak Search tertutup
22. Verifikasi tabel langsung kembali ke semua 4 baris
23. Klik ikon Search pada toolbar
24. Verifikasi kotak Search kosong (keyword dikosongkan)

### TC-FA-LIC-567: Search per kelas kolom teks Searchable

Untuk setiap baris tabel "Data Uji Search kolom teks Searchable" (langkah 25 sampai 27):

25. Ketik Search kata kunci pada baris tabel, tekan Enter
26. Verifikasi tabel menampilkan Date hasil pada baris tabel yang sama
27. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-568: Guard kolom non-searchable Date

28. Ketik Search `29/09/26`, tekan Enter
29. Verifikasi tabel menampilkan empty state `No results found` (kolom Date tidak dicari; penyaringan lewat Filter Panel)
30. Kosongkan isi kotak search, tekan Enter

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 27 dan 30 mengosongkan Search antar kasus (S-09); langkah 23 membuka kembali kotak Search untuk mengamati keyword kosong. TC-FA-LIC-569 dan 570 (Sort) ada di spec `TC-FA-LIC-E2E-171`.
- Langkah yang diulang per baris tabel Data Uji: langkah 25 sampai 27 (6 iterasi) (bagian 8b butir 7); tiap kasus berawal dari kotak Search kosong.
- Temuan untuk QA:
  - TC-FA-LIC-586 langkah 3 menyebut "Ketik 1 karakter" tanpa nilai; spec memakai `s`.
  - TC-FA-LIC-586 butir f menyebut keyword dikosongkan oleh `(←)` tanpa cara mengamatinya; spec membuka kembali kotak Search (langkah 23 dan 24).
