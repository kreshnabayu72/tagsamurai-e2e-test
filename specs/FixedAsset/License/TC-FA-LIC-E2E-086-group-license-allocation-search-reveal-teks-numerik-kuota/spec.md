---
id: TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota
title: "Group License Allocation: Search Reveal, Kolom Teks, Numerik Kuota, dan Numerik Addon"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-299
  - TC-FA-LIC-300
  - TC-FA-LIC-301
  - TC-FA-LIC-302
coverage:
  web: automated
---

# Group License Allocation: Search Reveal, Kolom Teks, Numerik Kuota, dan Numerik Addon

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Data Pre-setup #12 (data kuota dan hierarki PT Sejahtera, dipulihkan fixture BE di hook `before`): client Paid Pre-setup #1 dengan `License allocation per group` ON; Total Asset License 5.000; hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan. Tabel Group License Allocation pada node All Groups menampilkan empat baris level 1 (urutan default Used by This Group tertinggi): Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.*` (berkas fixture belum ada, disiapkan tim FE); nilai pada langkah dan tabel di bawah adalah nilai fixture itu.
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Tabel "Search per kelas kolom" (parameter langkah 25 sampai 27):

  | TC | Kolom | Kata kunci | Baris yang tampil |
  |---|---|---|---|
  | 300 | Group Name | `medan` | Cabang Medan |
  | 300 | Group Code | `GRP-SBY` | Cabang Surabaya |
  | 301 | Allocated Quota | `1500` | Produksi, Kantor Pusat |
  | 301 | Used by This Group | `880` | Cabang Medan |
  | 301 | Reserved by This Group | `10` | Cabang Medan, Cabang Surabaya, Kantor Pusat |
  | 301 | Remaining Quota | `120` | Cabang Medan |
  | 302 | + IT Inventory | `40` | Produksi |
  | 302 | + Tracking | `20` | Produksi, Cabang Medan, Kantor Pusat |
  | 302 | + Maintenance Routine | `3` | Cabang Medan |

- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #12. Kemampuan teknis: mengarahkan kursor ke ikon untuk membaca tooltip.

## Test Steps

### TC-FA-LIC-299: Search Group License Allocation, reveal, auto-focus, placeholder, tooltip, Enter, clear, dan collapse

1. Klik tab Allocation Quota
2. Klik ikon Search pada toolbar
3. Verifikasi Search bar melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder kotak Search `Search group name, group code...`
6. Arahkan kursor ke ikon Search
7. Verifikasi tooltip `Search` tampil
8. Ketik 1 karakter `m` pada kotak Search tanpa menekan Enter
9. Verifikasi icon `(×)` muncul di dalam kotak
10. Verifikasi tabel belum tersaring dan masih menampilkan empat baris: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
11. Ganti isi kotak search dengan `medan`, tekan Enter
12. Verifikasi tabel tersaring: Cabang Medan
13. Klik icon `(×)` di dalam kotak
14. Verifikasi input kosong
15. Verifikasi kotak Search tetap terbuka
16. Verifikasi kotak Search tetap fokus
17. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: Cabang Medan
18. Tekan Enter pada kotak Search kosong
19. Verifikasi tabel mengembalikan semua baris: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
20. Ketik kata kunci `medan` pada kotak Search tanpa menekan Enter
21. Klik icon panah `(←)` di kiri toolbar
22. Verifikasi kotak Search menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke semua baris: Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat

### TC-FA-LIC-300, TC-FA-LIC-301, dan TC-FA-LIC-302: Search per kelas kolom (teks, numerik kuota, numerik addon)

25. Untuk setiap baris tabel "Search per kelas kolom" (langkah 25 sampai 27): ketik Search kata kunci pada baris itu, tekan Enter
26. Verifikasi tabel menampilkan tepat baris yang tercantum pada kolom "Baris yang tampil" untuk baris tabel itu
27. Kosongkan isi kotak search, tekan Enter

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 27 (mengosongkan Search antar iterasi, S-09). Search untuk menemukan baris target tidak dipakai.
- Blok ulang: langkah 25 sampai 27 dijalankan 9 kali (2 kolom teks TC-FA-LIC-300, 4 kolom kuota TC-FA-LIC-301, 3 kolom addon TC-FA-LIC-302). Setelah ekspansi spec ini melewati sekitar 35 langkah. Alasan: seluruh blok adalah Search satu tabel dengan satu dataset Pre-setup #12 dan satu kelas harness, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Hover ikon Search dilakukan sesudah kotak terbuka karena TC tidak menyebut urutan pasti antara hover dan klik ikon.
- Temuan untuk QA: TC-FA-LIC-299 butir a menyebut tooltip `Search` saat hover ikon, tetapi langkah TC tidak memuat langkah hover; spec menambahkannya sebagai langkah penghubung. TC-FA-LIC-299 langkah 3 menulis "Ketik 1 karakter" tanpa menyebut karakternya; spec memakai `m`.
