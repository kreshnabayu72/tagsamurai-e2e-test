---
id: TC-GS-TAG-E2E-066-search-siklus-interaksi-substring-kolom-teks-dan-tanpa-hasil
title: "Search Registri: Siklus Interaksi, Substring Kolom Teks (Code, Device Name, SKU, Source, Type), dan Tanpa Hasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-21
  - TC-GS-TAG-188
  - TC-GS-TAG-189
coverage:
  web: automated
---

# Search Registri: Siklus Interaksi, Substring Kolom Teks (Code, Device Name, SKU, Source, Type), dan Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Tabel "Keyword substring kolom teks" (data langkah 24 sampai 35):

| Keyword | Kolom yang dicocokkan | Hasil yang diharapkan |
|---|---|---|
| `8A0002` | Code (potongan) | baris `E2801160600002054D8A0002` |
| `alien h3 tag` | Device Name (huruf kecil) | baris Device Name `Alien H3 Tag` (DD-02, DD-08) |
| `sku-8821` | SKU | baris DD-01 |
| `self-purchased` | Source | 6 baris Source Self-Purchased |
| `user tag` | Type | baris DD-02 (Type User TAG) |

- Kemampuan teknis: mengetik pada kotak Search, menekan Enter, membaca teks pagination `Showing ... of N TAGs`.

## Test Steps

### TC-GS-TAG-188: Siklus interaksi Search

1. Arahkan kursor ke ikon Search
2. Verifikasi tooltip ikon `Search`
3. Klik ikon Search
4. Verifikasi input Search melebar
5. Verifikasi kursor fokus di input Search
6. Verifikasi placeholder `Search code, name, SKU...`
7. Ketik `Zebra` tanpa menekan Enter
8. Verifikasi icon `(✕)` muncul di input
9. Verifikasi tabel belum tersaring (pagination `Showing 1 - 10 of 30 TAGs`)
10. Tekan `Enter`
11. Verifikasi tabel tersaring sesuai `Zebra` (baris DD-01, DD-06, DD-07 tampil)
12. Klik icon `(✕)` di input
13. Verifikasi teks di input terhapus
14. Verifikasi input tetap terbuka
15. Verifikasi tabel tetap menampilkan hasil `Zebra`
16. Tekan `Enter` pada input kosong
17. Verifikasi tabel kembali ke seluruh data (pagination `Showing 1 - 10 of 30 TAGs`)
18. Ketik Search `Alien`, tekan Enter
19. Klik icon `(←)`
20. Verifikasi kotak pencarian menutup
21. Verifikasi keyword dikosongkan
22. Verifikasi tabel langsung reset ke seluruh data (pagination `Showing 1 - 10 of 30 TAGs`)

### TC-GS-TAG-189: Search pada kolom teks

23. Klik ikon Search
24. Ketik Search `8A0002`, tekan Enter
25. Verifikasi baris `E2801160600002054D8A0002` tampil
26. Ganti isi kotak search dengan `alien h3 tag`, tekan Enter
27. Verifikasi baris Device Name `Alien H3 Tag` tampil (DD-02, DD-08)
28. Ganti isi kotak search dengan `sku-8821`, tekan Enter
29. Verifikasi baris DD-01 tampil
30. Ganti isi kotak search dengan `self-purchased`, tekan Enter
31. Verifikasi 6 baris Source Self-Purchased tampil
32. Ganti isi kotak search dengan `user tag`, tekan Enter
33. Verifikasi baris DD-02 (Type User TAG) tampil
34. Ganti isi kotak search dengan `ZZZ-NOTFOUND`, tekan Enter
35. Verifikasi judul `No results found` dan deskripsi `Try adjusting your search or filter.` tampil

### TC-GS-TAG-21: Search tanpa hasil menampilkan empty state No results found

36. Verifikasi empty state yang tampil adalah empty state hasil Search, bukan empty state S-01 (registri kosong)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 188 (screening siklus interaksi), 189, 21. Spec tidak mengubah data dan tidak menghapus apa pun, sehingga tidak ada aksi destruktif.
- Panjang spec: 36 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: ketiga blok satu topik (Search) pada satu dataset (Seed Registri A) dan satu kelas harness biasa; blok TC-GS-TAG-188 dan TC-GS-TAG-189 menutup atau mengganti isi kotak Search sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya. Kegagalan keras pada pembukaan kotak Search (langkah 3) akan membuat blok sesudahnya tidak berjalan; hal ini diakui, dan pemisahan tidak dilakukan karena ketiga blok memakai satu halaman dan satu dataset.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 23 (membuka kembali kotak Search yang ditutup langkah 19, untuk blok TC-GS-TAG-189).
- Pemisahan dari spec Filter, Sort, dan Pagination registri: kelas harness tidak sama dan tidak semua memakai data yang sama; ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Hitungan hasil (DD-01, DD-06, DD-07 untuk `Zebra`; 6 baris Self-Purchased; `Showing 1 - 10 of 30 TAGs`) diturunkan dari Seed Registri A dan teks pagination TC-GS-TAG-245; Expected TC-GS-TAG-188 hanya menyebut "tersaring sesuai `Zebra`".
- TC-GS-TAG-21 ditempatkan di spec ini (topik Search), bukan di spec empty state registri (spec 004).
- Temuan untuk QA:
  - TC-GS-TAG-21 Expected b ("Bukan empty state S-01") tidak menyebut copy S-01 sehingga pembeda yang bisa diasersi hanya teks `No results found`; spec mengasersi bahwa empty state yang tampil adalah milik hasil Search (langkah 36) dengan dasar teks pada langkah 35. Perlu copy S-01 agar pembedanya eksplisit.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
  - TC-GS-TAG-189 menyebut Source `self-purchased` memberi "6 baris"; hitungan cocok dengan Seed Registri A (DD-02, DD-03, DD-08, DD-11, DD-12, DD-13).
