---
id: TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom
title: "Search Modal Changelog Allocation Quota: Reveal, Kolom Teks dan Angka, Guard Kolom Date, dan Trim Spasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-331
  - TC-FA-LIC-332
  - TC-FA-LIC-333
  - TC-FA-LIC-334
  - TC-FA-LIC-335
coverage:
  web: automated
---

# Search Modal Changelog Allocation Quota: Reveal, Kolom Teks dan Angka, Guard Kolom Date, dan Trim Spasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- Data Uji Search kolom teks Searchable (TC-FA-LIC-332), dipakai langkah 25 sampai 27:

  | Kolom | Kata kunci | Hasil (Date) |
  |---|---|---|
  | Action | `remove` | 27/09/26 09:00, 25/09/26 08:45 |
  | Group Name | `Divisi IT` | 28/09/26 15:30, 25/09/26 08:45 |
  | Field | `Allocated` | 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45 |
  | Modified By | `dewi` | 28/09/26 15:30, 26/09/26 11:20 |

- Data Uji Search kolom angka (TC-FA-LIC-333), dipakai langkah 28 sampai 30:

  | Kolom | Kata kunci | Hasil (Date) |
  |---|---|---|
  | Old Value | `500` | 29/09/26 10:05 |
  | New Value | `50` | 29/09/26 10:05, 26/09/26 11:20 |

- Spec ini hanya membaca data dan tidak mengubah state global.
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Jumlah baris Changelog (6 baris pada langkah 10, 18, 22) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

### TC-FA-LIC-331: Reveal, auto-focus, placeholder, tooltip, Enter, clear, dan collapse

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Klik ikon Search pada toolbar
3. Verifikasi Search bar melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, group name...`
6. Arahkan kursor ke ikon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter `r` pada kotak Search
9. Verifikasi icon `(×)` muncul
10. Verifikasi tabel belum tersaring (6 baris tetap tampil, bukan live-as-you-type)
11. Ganti isi kotak search dengan `remove`, tekan Enter
12. Verifikasi tabel tersaring: 27/09/26 09:00, 25/09/26 08:45
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak tetap terbuka dan fokus
16. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: 27/09/26 09:00, 25/09/26 08:45
17. Tekan Enter pada kotak kosong
18. Verifikasi semua 6 baris kembali tampil
19. Ketik `remove` pada kotak Search
20. Klik icon panah `(←)` di kiri toolbar
21. Verifikasi kotak Search tertutup
22. Verifikasi tabel langsung kembali ke semua 6 baris
23. Klik ikon Search pada toolbar
24. Verifikasi kotak Search kosong (keyword dikosongkan)

### TC-FA-LIC-332: Search per kelas kolom teks Searchable (Action, Group Name, Field, Modified By)

Untuk setiap baris tabel "Data Uji Search kolom teks Searchable" (langkah 25 sampai 27):

25. Ketik Search kata kunci pada baris tabel, tekan Enter
26. Verifikasi tabel menampilkan Date hasil pada baris tabel yang sama
27. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-333: Search per kelas angka Old Value dan New Value

Untuk setiap baris tabel "Data Uji Search kolom angka" (langkah 28 sampai 30):

28. Ketik Search kata kunci pada baris tabel, tekan Enter
29. Verifikasi tabel menampilkan Date hasil pada baris tabel yang sama
30. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-334: Guard kolom non-searchable Date

31. Ketik Search `29/09/26`, tekan Enter
32. Verifikasi tabel menampilkan empty state `No results found` (kolom Date tidak dicari; penyaringan lewat Filter Panel)
33. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-335: Trim spasi tepi, spasi tengah dipertahankan, tidak case-sensitive

34. Ganti isi kotak search dengan `  REMOVE  ` (spasi di awal dan akhir, huruf kapital), tekan Enter
35. Verifikasi tabel menampilkan: 27/09/26 09:00, 25/09/26 08:45
36. Verifikasi isi kotak Search di layar tetap seperti yang diketik (spasi tepi tetap terlihat)
37. Klik icon panah `(←)` di kiri toolbar, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 27, 30, dan 33 mengosongkan Search antar kasus (S-09); langkah 37 menutup Search dan modal. Langkah 23 membuka kembali kotak Search untuk mengamati keyword yang sudah dikosongkan.
- Langkah yang diulang per baris tabel Data Uji: langkah 25 sampai 27 (4 iterasi) dan langkah 28 sampai 30 (2 iterasi) (bagian 8b butir 7).
- Spec di atas 35 langkah (37 langkah nominal dan sekitar 49 langkah dengan ekspansi): alasan dipertahankan, seluruh blok adalah Search pada modal yang sama dengan dataset yang sama dan berdiri sendiri; tiap kasus berawal dari kotak Search kosong, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-331 langkah 3 menyebut "Ketik 1 karakter" tanpa nilai; spec memakai `r`.
  - TC-FA-LIC-331 butir f menyebut keyword dikosongkan oleh `(←)` tanpa cara mengamatinya; spec membuka kembali kotak Search untuk mengamati keyword kosong (langkah 23 dan 24).
