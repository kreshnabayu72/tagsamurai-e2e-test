---
id: TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non
title: "Active Sessions: Search Reveal, Per Kelas Kolom, Kolom Tanggal Non-Searchable, dan Trim Spasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-262
  - TC-FA-LIC-263
  - TC-FA-LIC-264
  - TC-FA-LIC-265
coverage:
  web: automated
---

# Active Sessions: Search Reveal, Per Kelas Kolom, Kolom Tanggal Non-Searchable, dan Trim Spasi

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.sesiTabel` (berkas fixture belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel dan tidak mengubah data.
- Tabel "Search per kelas kolom" (parameter langkah 26 sampai 28):

  | Kolom | Kata kunci | Baris yang tampil |
  |---|---|---|
  | User Name | `rudi` | Rudi Hartono |
  | Email | `dewi@` | Dewi Lestari |
  | Position | `Gudang` | Rudi Hartono, Budi Santoso |
  | Division | `Keuangan` | Siti Rahma |
  | IP Address | `192.0.2` | Dewi Lestari, Siti Rahma, Budi Santoso |
  | Device / OS | `macOS` | Siti Rahma |
  | Browser | `Edge` | Dewi Lestari |

- Tabel "Kolom tanggal non-searchable" (parameter langkah 29 sampai 31):

  | Kolom | Kata kunci |
  |---|---|
  | Login Time | `09:20` |
  | Last Activity | `09:36` |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; sesi UI akun aktor.
- Kemampuan teknis: mengarahkan kursor ke ikon untuk membaca tooltip.

## Test Steps

### TC-FA-LIC-262: Search Active Sessions, reveal, auto-focus, placeholder, tooltip, Enter, clear, dan collapse

1. Klik tab Concurrent User
2. Klik ikon Search pada toolbar
3. Verifikasi Search bar melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder kotak Search `Search user name, email...`
6. Arahkan kursor ke ikon Search
7. Verifikasi tooltip `Search` tampil
8. Ketik 1 karakter `r` pada kotak Search tanpa menekan Enter
9. Verifikasi icon `(×)` muncul di dalam kotak
10. Verifikasi tabel belum tersaring dan masih menampilkan lima baris: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso
11. Ganti isi kotak search dengan `rudi`, tekan Enter
12. Verifikasi tabel tersaring: Rudi Hartono
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak Search tetap terbuka
16. Verifikasi kotak Search tetap fokus
17. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: Rudi Hartono
18. Tekan Enter pada kotak Search kosong
19. Verifikasi tabel mengembalikan semua baris: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso
20. Ketik kata kunci `rudi` pada kotak Search tanpa menekan Enter
21. Klik icon panah `(←)` di kiri toolbar
22. Verifikasi kotak Search menutup
23. Verifikasi tabel langsung kembali ke semua baris: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso
24. Klik ikon Search pada toolbar
25. Verifikasi keyword dikosongkan

### TC-FA-LIC-263: Search Active Sessions per kelas kolom teks Searchable

26. Untuk setiap baris tabel "Search per kelas kolom" (langkah 26 sampai 28): ketik Search kata kunci pada baris itu, tekan Enter
27. Verifikasi tabel menampilkan tepat baris yang tercantum pada kolom "Baris yang tampil" untuk baris tabel itu
28. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-264: Guard kolom non-searchable Login Time dan Last Activity

29. Untuk setiap baris tabel "Kolom tanggal non-searchable" (langkah 29 sampai 31): ketik Search kata kunci pada baris itu, tekan Enter
30. Verifikasi tabel menampilkan empty state `No results found` (kolom tidak dicari; penyaringan lewat Filter Panel)
31. Kosongkan isi kotak search, tekan Enter

### TC-FA-LIC-265: Spasi tepi di-trim saat Enter, spasi tengah dipertahankan, tidak case-sensitive

32. Ketik Search `  RUDI  ` (spasi di awal dan akhir, huruf kapital), tekan Enter
33. Verifikasi tabel menampilkan: Rudi Hartono
34. Verifikasi isi kotak Search di layar tetap `  RUDI  ` (spasi tepi tetap terlihat)
35. Klik icon panah `(←)` di kiri toolbar

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 24 (membuka kembali kotak Search untuk mengamati keyword kosong), langkah 28 dan 31 (mengosongkan Search antar iterasi, S-09), dan `(←)` di akhir TC-FA-LIC-265 (langkah 35, menutup kotak). Search untuk menemukan baris target tidak dipakai.
- Blok ulang: langkah 26 sampai 28 dijalankan 7 kali dan langkah 29 sampai 31 2 kali. Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok memakai satu tabel, satu dataset Pre-setup #26, dan satu kelas harness (fungsional), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Hover ikon Search (langkah 6 dan sesudahnya) dilakukan sesudah kotak terbuka, sebab TC tidak menyebut urutan pasti antara hover dan klik ikon.
- Temuan untuk QA: TC-FA-LIC-262 butir a menyebut tooltip `Search` muncul saat hover ikon tetapi langkah TC tidak memuat langkah hover; spec menambahkan langkah hover sebagai langkah penghubung. TC-FA-LIC-262 langkah 3 menulis "Ketik 1 karakter" tanpa menyebut karakternya; spec memakai `r`. TC-FA-LIC-262 butir f menyebut keyword dikosongkan oleh `(←)` tanpa cara mengamatinya; spec membuka kembali kotak Search untuk mengamati keyword kosong (langkah 24 dan 25).
