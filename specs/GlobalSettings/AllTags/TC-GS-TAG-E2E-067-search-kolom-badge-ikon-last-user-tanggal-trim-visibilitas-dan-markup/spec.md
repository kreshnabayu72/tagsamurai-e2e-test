---
id: TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup
title: "Search Registri: Kolom Badge, Ikon TAG Type, Last User, Kolom Tanggal Tidak Searchable, Trim, Terikat Visibilitas Kolom, dan Markup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-190
  - TC-GS-TAG-191
  - TC-GS-TAG-192
  - TC-GS-TAG-193
  - TC-GS-TAG-194
  - TC-GS-TAG-195
  - TC-GS-TAG-196
coverage:
  web: automated
---

# Search Registri: Kolom Badge, Ikon TAG Type, Last User, Kolom Tanggal Tidak Searchable, Trim, Terikat Visibilitas Kolom, dan Markup

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya. Keyword tanggal TC-GS-TAG-193 (`16/09/26`, `14:30`) bersumber dari Last Scanned DD-01 (`16/09/26 14:30`).
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): preferensi kolom registri dihapus di browser sehingga visibilitas kembali ke default (Last Scanned In dan Last User tersembunyi, Brand tampil); kemampuan menghapus preferensi kolom di browser disediakan tim FE.
- Kemampuan teknis: mengetik pada kotak Search dan menekan Enter; membaca nilai input apa adanya (termasuk spasi depan dan belakang); memantau dialog browser (`alert`) dan error halaman tak tertangani selama langkah 33 sampai 36 (TC tidak mendefinisikan mekanismenya; disediakan tim FE; lihat Temuan untuk QA).

## Test Steps

### Persiapan kolom (TC-GS-TAG-190 butir d dan TC-GS-TAG-192 butir d)

1. Buka overlay Column Visibility lewat header kolom Actions (⋯), centang `Last Scanned In` dan `Last User`, lalu tutup overlay

### TC-GS-TAG-190: Search pada kolom badge

2. Ketik Search `zebra`, tekan Enter
3. Verifikasi baris Brand `Zebra` tampil (DD-01, DD-06, DD-07)
4. Ganti isi kotak search dengan `zt410`, tekan Enter
5. Verifikasi baris DD-01 tampil
6. Ganti isi kotak search dengan `damaged`, tekan Enter
7. Verifikasi baris Status `Damaged/Missing` tampil (DD-04)
8. Ganti isi kotak search dengan `fixed asset`, tekan Enter
9. Verifikasi baris dengan Last Scanned In Fixed Asset tampil (DD-01, DD-06, DD-07)

### TC-GS-TAG-191: Search pada kolom ikon TAG Type

10. Ganti isi kotak search dengan `nfc`, tekan Enter
11. Verifikasi 3 baris bertipe NFC tampil
12. Ganti isi kotak search dengan `gps`, tekan Enter
13. Verifikasi baris DD-09 tampil

### TC-GS-TAG-192: Search pada kolom Last User

14. Ganti isi kotak search dengan `budi`, tekan Enter
15. Verifikasi 6 baris dengan Last User `Budi S` tampil

### TC-GS-TAG-193: Kolom tanggal tidak dapat dicari

16. Ganti isi kotak search dengan `16/09/26`, tekan Enter
17. Verifikasi `No results found` tampil
18. Ganti isi kotak search dengan `14:30`, tekan Enter
19. Verifikasi `No results found` tampil

### TC-GS-TAG-194: Query Search di-trim saat Enter

20. Ganti isi kotak search dengan `Zebra`, tekan Enter
21. Verifikasi baris DD-01, DD-06, DD-07 tampil (baseline hasil keyword `Zebra`)
22. Ganti isi kotak search dengan ` Zebra ` (spasi depan dan belakang), tekan Enter
23. Verifikasi hasil identik dengan keyword `Zebra` (baris DD-01, DD-06, DD-07)
24. Verifikasi isi input tetap ` Zebra ` apa adanya

### TC-GS-TAG-195: Search terikat visibilitas kolom

25. Klik `(←)` pada kotak Search
26. Buka overlay Column Visibility, hapus centang `Brand`, lalu tutup overlay
27. Ketik Search `Kontakt.io`, tekan Enter
28. Verifikasi `No results found` tampil (`Kontakt.io` tidak mencocokkan baris saat `Brand` disembunyikan)
29. Klik `(←)` pada kotak Search
30. Buka overlay Column Visibility, centang kembali `Brand`, lalu tutup overlay
31. Ketik Search `Kontakt.io`, tekan Enter
32. Verifikasi baris DD-04 cocok

### TC-GS-TAG-196: Keyword berisi markup dicocokkan sebagai teks

33. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
34. Verifikasi `No results found` tampil
35. Verifikasi tidak ada skrip berjalan (tidak ada dialog `alert` browser)
36. Verifikasi tidak ada error tak tertangani pada halaman
37. Klik `(←)` pada kotak Search
38. Buka overlay Column Visibility, hapus centang `Last Scanned In` dan `Last User`, lalu tutup overlay

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (190 sampai 196). Spec tidak mengubah data registri; satu-satunya state yang diubah adalah visibilitas kolom, dipulihkan pada langkah 30 (Brand), 38 (Last Scanned In dan Last User), dan hook `after` sebagai cadangan.
- Panjang spec: 38 langkah, sedikit di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu topik (Search kolom registri) pada satu dataset (Seed Registri A) dan satu kelas harness biasa, setiap blok memakai keyword sendiri dan mengganti isi kotak Search sehingga tidak bergantung pada hasil blok sebelumnya, dan memecahnya hanya menambah login, hook, dan seeding tanpa memisahkan harness.
- P-5 butir b: TC-GS-TAG-196 (markup, kelas a) adalah satu-satunya TC objek-uji ringan kelas a di spec ini; tanpa request langsung ke server, tanpa harness eksternal, dan tanpa state berat, sehingga boleh berada di spec Search yang permukaannya sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (menampilkan Last Scanned In dan Last User, precondition TC butir d), langkah 25 dan 29 (mengosongkan Search), langkah 37 (mengosongkan Search), langkah 38 (memulihkan visibilitas kolom).
- Asersi tambahan di luar Expected TC (S-03): langkah 21 (baseline hasil `Zebra` supaya "hasil identik" pada Expected TC-GS-TAG-194 punya pembanding yang teramati).
- Absence hasil Search (langkah 17, 19, 28, 34) memakai empty state `No results found` sebagai anchor positif yang sah (bagian 8b butir 2). Kalimat kedua Expected TC-GS-TAG-193 ("penyaringan tanggal hanya lewat Filter Panel") adalah kesimpulan yang tidak teramati terpisah (S-03) sehingga tidak diberi `Verifikasi` sendiri.
- Pemisahan dari spec topik registri lain (Search, Filter, Sort, Pagination, Setup Column): ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Temuan untuk QA:
  - TC-GS-TAG-196 menyebut "tidak ada skrip berjalan dan tidak ada error tak tertangani" tanpa mendefinisikan cara mengamatinya (dialog `alert`, error console, atau lainnya); spec memakai pemantauan dialog dan error halaman yang disediakan tim FE, tanpa mengarang mekanisme.
  - TC-GS-TAG-194 hanya meminta pencarian ` Zebra `; pembanding "identik dengan keyword `Zebra`" dibangun spec lewat langkah 20 sampai 21.
  - TC-GS-TAG-195 langkah 3 ("Hapus keyword lalu centang kembali `Brand`") tidak menyebut cara menghapus keyword; spec memakai klik `(←)` pada kotak Search (bagian 8b butir 9).
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
