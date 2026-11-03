---
id: TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non
title: "Subscription History: Search (Reveal, Per Kelas Kolom, Guard Kolom Tanggal, dan Trim Spasi)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-189
  - TC-FA-LIC-190
  - TC-FA-LIC-191
  - TC-FA-LIC-192
  - TC-FA-LIC-193
coverage:
  web: automated
---
# Subscription History: Search (Reveal, Per Kelas Kolom, Guard Kolom Tanggal, dan Trim Spasi)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Anggota pencarian per kelas kolom (parameter langkah 23 sampai 25):

  | TC | Kolom | Kata kunci | Hasil tabel |
  |---|---|---|---|
  | TC-FA-LIC-190 | Subscription ID | `subs-2025` | SUBS-20250101-00001 |
  | TC-FA-LIC-191 | Plan | `Enterprise` | SUBS-20241201-00001 |
  | TC-FA-LIC-191 | Type | `Trial` | SUBS-20241201-00001 |
  | TC-FA-LIC-191 | Status | `Converted` | SUBS-20241201-00001 |
  | TC-FA-LIC-191 | Plan Owner | `ABC` | SUBS-20241201-00001 |

- Anggota guard kolom non-searchable (TC-FA-LIC-192, parameter langkah 26 sampai 28): Start Date `31/12/26` dan End Date `01/01/25`; hasil kedua anggota empty state `No results found`.
- Kemampuan teknis: hover ikon Search untuk mengamati tooltip dan pengamatan fokus kursor serta isi kotak Search (disediakan tim FE).
- State yang diubah dan dipulihkan: kotak Search tabel Subscription History (ditutup pada langkah 32).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-189: Siklus Search (reveal, auto-focus, placeholder, tooltip, Enter, clear, collapse)

2. Arahkan kursor ke ikon Search pada toolbar
3. Verifikasi tooltip `Search` tampil
4. Klik ikon Search
5. Verifikasi search bar melebar
6. Verifikasi kursor fokus di input
7. Verifikasi placeholder `Search subscription ID, plan...`
8. Ketik `s` (1 karakter) pada kotak Search tanpa menekan Enter
9. Verifikasi icon `(×)` muncul di dalam kotak
10. Verifikasi tabel belum tersaring (empat baris: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001)
11. Ganti isi kotak search dengan `subs-2025`, tekan Enter
12. Verifikasi tabel tersaring: SUBS-20250101-00001
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak Search tetap terbuka dan fokus
16. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: SUBS-20250101-00001
17. Tekan Enter pada kotak kosong
18. Verifikasi tabel menampilkan semua baris (empat baris)
19. Ketik `subs` pada kotak Search tanpa menekan Enter, lalu klik icon panah `(←)` di kiri toolbar
20. Verifikasi kotak Search tertutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung kembali ke semua baris (empat baris)

### TC-FA-LIC-190 dan TC-FA-LIC-191: Search per kelas kolom

Untuk setiap baris tabel "Anggota pencarian per kelas kolom" (langkah 23 sampai 25):

23. Ketik Search kata kunci baris tabel, tekan Enter
24. Verifikasi tabel menampilkan hasil baris tabel
25. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-192: Guard kolom non-searchable

Untuk setiap anggota guard kolom non-searchable (langkah 26 sampai 28):

26. Ketik Search nilai anggota, tekan Enter
27. Verifikasi tabel menampilkan empty state `No results found` (kolom tidak dicari; penyaringan lewat Filter Panel)
28. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-193: Trim spasi tepi

29. Ketik Search `  SUBS-2025  ` (spasi di awal dan akhir, huruf kapital), tekan Enter
30. Verifikasi tabel menampilkan: SUBS-20250101-00001
31. Verifikasi isi kotak Search di layar tetap `  SUBS-2025  ` (spasi tepi tetap terlihat)
32. Klik icon panah `(←)` di kiri toolbar

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (32 langkah nominal; 47 langkah setelah ekspansi dua blok ulang). Alasan: seluruh blok satu topik (Search tabel Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah diulang per kolom dengan parameter di tabel `## Prerequisites`: langkah 23 sampai 25 (lima iterasi) dan langkah 26 sampai 28 (dua iterasi); tiap iterasi memuat satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 25 dan 28 (mengosongkan Search antar anggota; Enter pada kotak kosong mengembalikan semua baris, TC-FA-LIC-189 (langkah TC 6)), dan langkah 32 (menutup kotak Search).
- Asersi di luar Expected TC (S-03): kata kunci langkah 8 (`s`) dipilih spec karena TC menulis "1 karakter"; hasil tabel awal empat baris pada langkah 10 dan 18 diturunkan dari Pre-setup #13 (4 term).
- Temuan untuk QA:
  - TC-FA-LIC-189 (langkah TC 3) menulis "Ketik 1 karakter" tanpa menyebut karakternya; spec memakai `s`.
  - TC-FA-LIC-192 memakai nilai `31/12/26` untuk Start Date dan `01/01/25` untuk End Date yang bukan nilai kolom itu pada Pre-setup #13 (Start Date 01/01/27, 01/01/26, 01/01/25, 01/12/24); kedua nilai tetap tidak dicari karena kolom tanggal non-searchable. Spec mengikuti TC.
  - TC-FA-LIC-189, 190, 191, 192, dan 193 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
