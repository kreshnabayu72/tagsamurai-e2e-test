<!-- Ditulis stage spec-from-prd saat close. Jangan diubah tangan: run berikutnya menimpanya. -->

Suite: `specs/FixedAsset/FileManager`. Sumber: PRD `fixed-asset@1836c1a` (sha `7a66273b026439ed`), foundation@a25f734-dirty, kontrak komponen wangs-ui@1.0.0. Stage: `prd-harness@42accb5`, ditutup 2026-11-22T14:31:19Z.

# Matriks data File Manager (7a6cbb0c5e52fec8)

- Entri: 847 (awal 719, dibuat 23, dicoba 105)
- Checker: ERROR 0, REVIEW 20

## Target × varian

✓ entri yang memenuhi, ✗ belum ada entri, — tidak berlaku beserta alasannya.

### kolom-searchable@tabel-files · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:teks` | ✓ DU-002-15 |
| `per-kelas-kolom:badge` | ✓ DU-002-18 |
| `per-kelas-kolom:numerik` | ✓ DU-002-17 |
| `substring-tengah` | ✓ DU-002-15 |
| `beda-kapital` | ✓ DU-002-16 |
| `tanpa-hasil` | ✓ DU-002-19 |
| `kolom-non-searchable` | ✓ DU-002-20 |
| `kolom-tersembunyi` | ✓ DU-002-29 |
| `lintas-kolom` | ✓ DU-002-21 |
| `karakter-pola` | ✓ DU-002-27, DU-002-28 |
| `query-spasi-tepi` | ✓ DU-002-22 |
| `query-spasi-saja` | ✓ DU-002-23 |
| `query-spasi-tengah` | ✓ DU-002-24 |
| `query-kata-tidak-bersebelahan` | ✓ DU-002-25 |
| `nilai-substring-nilai-lain` | ✓ DU-002-26 |
| `kolom-icon-label` | — §4.1 T-FAFM-01: tidak ada kolom ber-ikon pada tab Files |
| `kolom-homogen` | — §4.1 T-FAFM-01: PRD tidak menyatakan kolom yang bernilai seragam di semua baris |
| `record-tab-non-default` | — §4.4: Search dan state dipertahankan per tab; tidak ada Search Global lintas tab |
| `cocok-di-anak-saja` | — §4.1 T-FAFM-01: tabel datar, tidak ada node anak |

### kolom-sortable@tabel-files · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-003-1, DU-003-2, DU-003-3 |
| `sama-tiebreak` | ✓ DU-003-18, DU-003-19, DU-003-20, DU-003-21 |
| `beda-kapital` | ✓ DU-003-3 |
| `natural` | ✓ DU-003-10, DU-003-11, DU-003-13 |
| `per-tipe-kolom:tanggal` | ✓ DU-003-15, DU-003-16, DU-003-17 |
| `per-tipe-kolom:badge` | ✓ DU-003-18, DU-003-19, DU-003-20, DU-003-21 |
| `aksen` | ✓ DU-003-4, DU-003-5, DU-003-6 |
| `diawali-angka-simbol` | ✓ DU-003-7, DU-003-8, DU-003-9 |
| `default-beda` | ✓ DU-003-1, DU-003-2, DU-003-3 |
| `sisip-beda-default` | ✓ DU-003-1, DU-003-2, DU-003-3 |
| `lintas-halaman` | ✓ DU-003-27 |
| `sama-melintasi-halaman` | ✓ DU-003-27 |
| `sama-di-kolom-dan-default` | ✓ DU-003-22, DU-003-23 |
| `format-komposit` | ✓ DU-003-12, DU-003-14 |
| `nama-tampil-beda-nama-penuh` | ✓ DU-003-24, DU-003-25, DU-003-26 |
| `kosong` | — §4.1 T-FAFM-01 kolom Nilai Kosong: setiap kolom bersort «Tidak pernah kosong»; Reference «Tampil —» hanya untuk Source Asset Photo (§4.2d SRC-01) yang tabnya tidak menampilkan kolom Reference, sehingga tidak ada nilai null di kolom sortable mana pun |
| `jumlah-chip-sama` | — §4.1 T-FAFM-01: tidak ada kolom multi-badge atau ikon aktif pada tab Files |
| `jumlah-aktif-sama` | — §4.1 T-FAFM-01: tidak ada kolom multi-badge atau ikon aktif pada tab Files |
| `campuran-tipe` | — §4.1 T-FAFM-01: tidak ada kolom bertipe data campuran pada tab Files |
| `urutan-custom` | — §4.1 T-FAFM-01: kolom Group diurutkan Alphabetical (A-Z), PRD tidak menetapkan urutan custom per nilai |
| `urutan-beda-antar-kolom` | — §4.1 T-FAFM-01: tiap kolom memakai urutan Alphabetical, Numeric, atau tanggal standar tanpa urutan khusus |

### field-filter@tabel-files · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-004-2 |
| `tidak-cocok` | ✓ DU-004-1 |
| `and-a-saja` | ✓ DU-004-1 |
| `and-b-saja` | ✓ DU-004-2 |
| `and-keduanya` | ✓ DU-004-3 |
| `and-tidak-keduanya` | ✓ DU-004-4 |
| `or-dalam-field` | ✓ DU-004-1 |
| `search-saja` | ✓ DU-004-7 |
| `filter-saja` | ✓ DU-004-8 |
| `search-dan-filter` | ✓ DU-004-6 |
| `irisan-kosong` | ✓ DU-004-9 |
| `kolom-tersembunyi` | ✓ DU-004-6 |
| `rentang-dalam` | ✓ DU-004-17, DU-004-35 |
| `rentang-luar` | ✓ DU-004-14, DU-004-15, DU-004-19, DU-004-35 |
| `rentang-tepat-awal` | ✓ DU-004-16, DU-004-35 |
| `rentang-tepat-akhir` | ✓ DU-004-18, DU-004-35 |
| `rentang-sehari` | ✓ DU-004-17, DU-004-36 |
| `range-tepat-min` | ✓ DU-004-11, DU-004-31 |
| `range-tepat-max` | ✓ DU-004-12, DU-004-31 |
| `range-hanya-min` | ✓ DU-004-12, DU-004-13, DU-004-32 |
| `range-hanya-max` | ✓ DU-004-10, DU-004-11, DU-004-33 |
| `range-min-lebih-max` | ✓ DU-004-13 |
| `per-kelas-kontrol:Multi-select searchable` | ✓ DU-004-1 |
| `per-kelas-kontrol:Tree picker multi-select` | ✓ DU-004-37 |
| `per-kelas-kontrol:Range Min–Max` | ✓ DU-004-10 |
| `per-kelas-kontrol:Date range picker` | ✓ DU-004-14, DU-004-38 |
| `filter-only` | — §4.1 T-FAFM-01: setiap field Filter Panel tab Files memiliki kolom tabel |
| `boolean-kedua-nilai` | — §4.1 T-FAFM-01: tidak ada field filter boolean atau switch pada tab Files |
| `custom-field-per-tipe` | — §4.1 T-FAFM-01: tab Files tidak memiliki field filter custom field |
| `mutasi-keluar-saringan` | — §4.1 T-FAFM-01: File Manager tidak punya Edit; nilai kolom filter berubah hanya lewat Transfer aset (EC-14) yang dimiliki spec -dep-transfer |
| `mutasi-masuk-saringan` | — §4.1 T-FAFM-01: File Manager tidak punya Edit; nilai kolom filter berubah hanya lewat Transfer aset (EC-14) yang dimiliki spec -dep-transfer |
| `create-tidak-cocok` | — L112 FAFM-LOGIC-01a: File Manager tidak membuat file, jadi tidak ada Create dari modul ini |
| `status-dikecualikan` | — §4.1 T-FAFM-01: tab Files tidak memiliki status internal yang dikecualikan dari filter |
| `default-filter-lolos` | — §4.1 T-FAFM-01: tidak ada filter pre-applied pada tab Files |
| `default-filter-tersaring` | — §4.1 T-FAFM-01: tidak ada filter pre-applied pada tab Files |

### opsi-filter@tabel-files · VD-T4

| Varian | Entri |
|---|---|
| `nilai-berulang` | ✓ DU-004-1 |
| `kolom-tanpa-null` | ✓ DU-004-1 |
| `master-tak-terpakai` | ✓ DU-004-23, DU-004-24 |
| `nilai-di-cakupan-lain` | ✓ DU-004-20 |
| `opsi-tidak-dipersempit-search` | ✓ DU-004-9 |
| `nilai-baru-saat-uji` | ✓ DU-004-25 |
| `opsi-hilang` | ✓ DU-004-39 |
| `entitas-rename-berhistori` | ✓ DU-004-21, DU-004-27 |
| `opsi-banyak-overflow` | ✓ DU-004-22 |
| `cari-opsi-substring` | ✓ DU-004-29 |
| `cari-opsi-beda-kapital` | ✓ DU-004-28 |
| `cari-opsi-tanpa-hasil` | ✓ DU-004-30 |
| `kosong` | — §4.1 T-FAFM-01: kolom filterable tab Files «Tidak pernah kosong» |
| `enum-sebagian-terisi` | — §4.4: opsi filter diisi dari nilai di tabel tanpa daftar statis, jadi bukan enum tetap |
| `per-anggota-enum` | — §4.4: opsi filter diisi dari nilai di tabel tanpa daftar statis, jadi bukan enum tetap |
| `nilai-kondisional` | — §4.1 T-FAFM-01: opsi filter tab Files tidak bersyarat pada keadaan lain |
| `opsi-tetap-worm` | — §4.1 T-FAFM-01: tab Files bukan log WORM |
| `entitas-terhapus-berhistori` | — §4.4: opsi diturunkan dari nilai yang ada di tabel; file yang terhapus tidak meninggalkan opsi |
| `sumber-kosong` | — §7.1 S-26a: tab Files kosong menampilkan empty state; PRD tidak menetapkan isi Filter Panel tanpa data |
| `satu-nilai-distinct` | — §4.1 T-FAFM-01: PRD tidak menetapkan perilaku field filter yang hanya punya satu nilai |
| `dua-nilai-distinct` | — §4.1 T-FAFM-01: PRD tidak menetapkan perilaku field filter yang hanya punya dua nilai |

### paginasi@tabel-files · VD-T5

| Varian | Entri |
|---|---|
| `lebih-satu-halaman` | ✓ DU-084-1 |
| `satu-baris-halaman-terakhir` | ✓ DU-084-2 |
| `tepat-ukuran-halaman` | ✓ DU-084-3 |
| `lebih-ukuran-terpilih:25` | ✓ DU-084-4 |
| `lebih-ukuran-maks` | ✓ DU-084-5 |
| `tersaring-lebih-satu-halaman` | ✓ DU-084-6 |
| `nomor-halaman-invalid` | ✓ DU-084-1 |

### empty-state@tabel-files · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-016-1, DU-079-4 |
| `kosong-untuk-aktor-ini` | ✓ DU-079-5 |
| `jadi-kosong-setelah-hapus` | ✓ DU-079-1 |
| `log-kosong` | — §7.1 S-26a: tab Files bukan log |
| `relasi-kosong` | — §4.1 T-FAFM-01: tab Files tidak menampilkan relasi induk-anggota |
| `node-tanpa-anak` | — §4.1 T-FAFM-01: tab Files bukan tree |

### empty-state@tabel-asset-data · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-086-7 |
| `kosong-untuk-aktor-ini` | ✓ DU-086-6 |
| `log-kosong` | — §7.1 S-27a: tab Asset Data bukan log |
| `relasi-kosong` | — §4.1 T-FAFM-02: tidak ada relasi induk-anggota |
| `node-tanpa-anak` | — §4.1 T-FAFM-02: tab Asset Data bukan tree |
| `jadi-kosong-setelah-hapus` | — L169 FAFM-LOGIC-08d: tab Asset Data read-only tanpa aksi hapus; aset keluar dari tab lewat Delete Asset Data di menu Asset atau kembali Active |

### empty-state@tabel-recycle-bin · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-087-10 |
| `kosong-untuk-aktor-ini` | ✓ DU-087-11 |
| `jadi-kosong-setelah-hapus` | ✓ DU-087-5 |
| `log-kosong` | — §7.1 S-28a: Recycle Bin bukan log |
| `relasi-kosong` | — §4.1 T-FAFM-03: tidak ada relasi induk-anggota |
| `node-tanpa-anak` | — §4.1 T-FAFM-03: Recycle Bin bukan tree |

### empty-state@tabel-changelog · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-016-1, DU-088-8 |
| `log-kosong` | ✓ DU-088-9 |
| `kosong-untuk-aktor-ini` | ✓ DU-088-10 |
| `relasi-kosong` | — §4.1 T-FAFM-04: tidak ada relasi induk-anggota |
| `node-tanpa-anak` | — §4.1 T-FAFM-04: Changelog bukan tree |
| `jadi-kosong-setelah-hapus` | — §8.1: Changelog hanya bertambah oleh Delete dan Permanently Delete; entri tidak dihapus |

### sel@tabel-files · VD-T7

| Varian | Entri |
|---|---|
| `null` | ✓ DU-078-3 |
| `string-kosong` | ✓ DU-078-4 |
| `teks-panjang` | ✓ DU-078-6 |
| `angka-ribuan` | ✓ DU-078-11 |
| `angka-pembulatan` | ✓ DU-078-12 |
| `nilai-turunan` | ✓ DU-078-9 |
| `nilai-beda-antar-kolom` | ✓ DU-078-1 |
| `aktor-system` | ✓ DU-078-10 |
| `referensi-terhapus` | ✓ DU-078-5 |
| `array-kosong` | — §4.1 T-FAFM-01: tab Files tidak punya kolom bertipe array, boolean, atau foto |
| `nol-numerik` | — §4.1 T-FAFM-01: Size «Tidak pernah kosong», PRD tidak menetapkan tampilan file berukuran nol |
| `boolean-null` | — §4.1 T-FAFM-01: tab Files tidak punya kolom bertipe array, boolean, atau foto |
| `tanggal-null` | — §4.1 T-FAFM-01: Upload Date «Tidak pernah kosong» |
| `kosong-tidak-pernah-diisi` | — §4.1 T-FAFM-01: Reference kosong tampil «—» dan sudah dicakup varian null |
| `kosong-setelah-dihapus` | — L121 FAFM-LOGIC-02c: rujukan yang dikosongkan memindahkan file ke Recycle Bin, bukan menampilkan baris kosong di tab Files |
| `teks-panjang-multibaris` | — §4.1 T-FAFM-01: tidak ada kolom teks multibaris |
| `per-nilai-badge` | — §4.1 T-FAFM-01: kolom Group adalah satu jenis badge severity primary tanpa varian per nilai |
| `tanpa-foto` | — §4.1 T-FAFM-01: tab Files tidak punya kolom bertipe array, boolean, atau foto |
| `asal-jalur` | — L118 FAFM-LOGIC-01g: File Manager tidak menerima file dari Import atau seed lewat jalur lain |
| `referensi-diarsipkan` | — §4.1 T-FAFM-01: PRD tidak mengenal rujukan berstatus arsip |

### kolom-nama-user@tabel-files · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-078-3 |
| `dua-kata` | ✓ DU-078-1 |
| `tiga-kata-lebih` | ✓ DU-078-7 |
| `nama-panjang` | ✓ DU-078-6 |
| `tanpa-last-name` | ✓ DU-078-3 |
| `nama-mirip` | ✓ DU-078-4, DU-078-5 |

### kolom-nama-user@tabel-recycle-bin · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-087-5 |
| `dua-kata` | ✓ DU-087-2 |
| `tiga-kata-lebih` | ✓ DU-087-6 |
| `nama-panjang` | ✓ DU-087-7 |
| `tanpa-last-name` | ✓ DU-087-5 |
| `nama-mirip` | ✓ DU-087-8, DU-087-9 |

### kolom-nama-user@tabel-changelog · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-088-5 |
| `dua-kata` | ✓ DU-088-2 |
| `tiga-kata-lebih` | ✓ DU-088-3 |
| `nama-panjang` | ✓ DU-088-4 |
| `tanpa-last-name` | ✓ DU-088-5 |
| `nama-mirip` | ✓ DU-088-6, DU-088-7 |

### kolom-group@tabel-files · VD-T9

| Varian | Entri |
|---|---|
| `tepat-25` | ✓ DU-078-7 |
| `lebih-25` | ✓ DU-078-8 |
| `hierarki-hover` | ✓ DU-078-9 |
| `tepat-10-mobile` | — §4.6: kartu file mobile hanya memuat File Name, Source, Asset, dan Size; kolom Group tidak tampil di mobile |
| `lebih-10-mobile` | — §4.6: kartu file mobile hanya memuat File Name, Source, Asset, dan Size; kolom Group tidak tampil di mobile |
| `per-tipe-label` | — §4.1 T-FAFM-01: kolom Group adalah satu jenis badge |

### seleksi-baris@tabel-files · VD-T14

| Varian | Entri |
|---|---|
| `satu-baris` | ✓ DU-085-1 |
| `banyak-baris` | ✓ DU-085-1 |
| `halaman-penuh` | ✓ DU-085-1 |
| `lintas-halaman` | ✓ DU-085-1 |
| `tersembunyi-filter` | ✓ DU-085-1 |
| `checkbox-disabled` | — §4.8: checkbox tab Files Show untuk semua aktor yang bisa membaca; Disabled hanya pada Recycle Bin |
| `homogen` | — §4.1a#p5: semua file terpilih diproses seragam, tidak ada seleksi per state |
| `campuran-state` | — §4.1a#p5: semua file terpilih diproses seragam, tidak ada kondisi skip karena state |
| `single-select-ganti` | — §4.1a: tab Files memakai multi-select, tidak ada single-select |

### bulk-delete-biasa@tabel-files · VD-A1

| Varian | Entri |
|---|---|
| `n-banyak` | ✓ DU-021-2, DU-021-3 |
| `daftar-melebihi-tampil` | ✓ DU-021-2, DU-021-3 |
| `item-beranotasi` | ✓ DU-021-2, DU-021-3 |
| `n-1` | — §7#p2: item dilewati atau gagal ditangani target bulk-delete-dilewati@tabel-files dan bulk-delete-satu@tabel-files |
| `campuran` | — §7#p2: item dilewati atau gagal ditangani target bulk-delete-dilewati@tabel-files dan bulk-delete-satu@tabel-files |
| `semua-ditolak` | — §7#p2: item dilewati atau gagal ditangani target bulk-delete-dilewati@tabel-files dan bulk-delete-satu@tabel-files |
| `semua-ditolak-alasan-single` | — L120 FAFM-LOGIC-02b: tidak ada kondisi Disabled-by-target maupun dialog blok pada Delete |
| `nol-item` | — §4.1a#p3 ACT-04a: Bulk Delete tampil hanya bila ≥1 baris terpilih |
| `jadi-tidak-eligible-saat-submit` | — §7#p2: item dilewati atau gagal ditangani target bulk-delete-dilewati@tabel-files dan bulk-delete-satu@tabel-files |
| `gagal-banyak` | — §7#p2: bulk yang seluruh itemnya gagal memakai satu toast T-05, tanpa penggabungan per item |
| `sisa-satu-relevan` | — §7#p2: item dilewati atau gagal ditangani target bulk-delete-dilewati@tabel-files dan bulk-delete-satu@tabel-files |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada POV Aktor×Target; semua file setara dan tidak ada baris terlindungi |

### bulk-delete-satu@tabel-files · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-022-2 |
| `sisa-satu-relevan` | ✓ DU-022-3 |
| `n-banyak` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `campuran` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `semua-ditolak` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `semua-ditolak-alasan-single` | — L120 FAFM-LOGIC-02b: tidak ada dialog blok pada Delete; tidak ada kondisi Disabled-by-target |
| `nol-item` | — §4.1a ACT-04a: Bulk Delete tampil hanya bila ≥1 baris terpilih |
| `jadi-tidak-eligible-saat-submit` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `gagal-banyak` | — §7#p3: satu file terpilih memakai toast single T-04 |
| `daftar-melebihi-tampil` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `item-beranotasi` | — §7#p3: hanya bulk dengan satu file terpilih yang memakai bentuk tunggal; varian lain dimiliki target bulk-delete-biasa@tabel-files dan bulk-delete-dilewati@tabel-files |
| `termasuk-baris-terlindungi` | — L120 FAFM-LOGIC-02b: tidak ada dialog blok pada Delete; tidak ada kondisi Disabled-by-target |

### bulk-delete-dilewati@tabel-files · VD-A1

| Varian | Entri |
|---|---|
| `campuran` | ✓ DU-023-2, DU-023-3 |
| `semua-ditolak` | ✓ DU-023-4, DU-023-5 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-023-3, DU-023-4, DU-023-5 |
| `n-1` | — §7#p2: varian ini dimiliki target bulk-delete-biasa@tabel-files atau bulk-delete-satu@tabel-files |
| `n-banyak` | — §7#p2: varian ini dimiliki target bulk-delete-biasa@tabel-files atau bulk-delete-satu@tabel-files |
| `semua-ditolak-alasan-single` | — L120 FAFM-LOGIC-02b: tidak ada dialog blok pada Delete; item yang tidak tersedia dilewati lewat T-03 atau T-13 |
| `nol-item` | — §4.1a ACT-04a: Bulk Delete tampil hanya bila ≥1 baris terpilih |
| `gagal-banyak` | — §7#p2: hanya hasil dihapus, dilewati, dan gagal per item; tidak ada penggabungan toast untuk banyak item gagal |
| `daftar-melebihi-tampil` | — §7#p2: varian ini dimiliki target bulk-delete-biasa@tabel-files atau bulk-delete-satu@tabel-files |
| `item-beranotasi` | — §7#p2: varian ini dimiliki target bulk-delete-biasa@tabel-files atau bulk-delete-satu@tabel-files |
| `sisa-satu-relevan` | — §7#p2: varian ini dimiliki target bulk-delete-biasa@tabel-files atau bulk-delete-satu@tabel-files |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada baris terlindungi pada File Manager |

### bulk-permanently-delete@tabel-recycle-bin · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-026-5 |
| `n-banyak` | ✓ DU-026-2, DU-026-3 |
| `campuran` | ✓ DU-027-3, DU-027-4, DU-027-5 |
| `semua-ditolak` | ✓ DU-027-6, DU-027-7 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-027-4, DU-027-6, DU-027-7 |
| `daftar-melebihi-tampil` | ✓ DU-026-2, DU-026-3 |
| `sisa-satu-relevan` | ✓ DU-026-6 |
| `semua-ditolak-alasan-single` | — L140 FAFM-LOGIC-05g: Permanently Delete tidak punya dialog blok; item yang tidak tersedia dilewati lewat T-08 |
| `nol-item` | — §4.1a ACT-06a: Bulk Permanently Delete tampil hanya bila ≥1 baris terpilih |
| `gagal-banyak` | — §7#p2: bulk yang seluruh itemnya gagal memakai satu toast T-10 |
| `item-beranotasi` | — L1428 D-04: dialog bulk Permanently Delete memuat nama file tanpa anotasi |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada baris terlindungi; checkbox Disabled hanya pada baris di luar group Delete aktor (§4.8) |

### download@tabel-files · VD-D1

| Varian | Entri |
|---|---|
| `tanpa-saringan-lebih-satu-halaman` | ✓ DU-006-1 |
| `hasil-tersaring` | ✓ DU-006-2, DU-006-3, DU-006-5, DU-006-6 |
| `per-tab` | ✓ DU-006-4 |
| `urutan-sort-aktif` | ✓ DU-006-1, DU-006-3 |
| `kolom-tersembunyi` | ✓ DU-006-1 |
| `nol-baris` | — §7.1 S-26a: tab Files tanpa baris menampilkan empty state; PRD tidak menetapkan berkas Download untuk nol baris |

### berkas-isi@tabel-files · VD-D2

| Varian | Entri |
|---|---|
| `hierarki-penuh` | ✓ DU-070-4, DU-070-5 |
| `leaf-sama-parent-beda` | ✓ DU-070-4, DU-070-5 |
| `nama-user-lengkap` | ✓ DU-070-3 |
| `numerik-terformat` | ✓ DU-070-9 |
| `kolom-foto` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `kolom-ikon` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `switch-kedua-nilai` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `per-nilai-badge` | — §4.1 T-FAFM-01: kolom Group adalah satu jenis badge tanpa nilai enum per varian |
| `multi-badge` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `lebih-dua-badge` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `item-flat` | — §4.1 T-FAFM-01: tab Files tidak punya kolom Brand atau Model yang ditulis tanpa hierarki |
| `boolean-kedua-nilai` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `mata-uang` | — §4.1 T-FAFM-01: tab Files tidak punya kolom foto, ikon, switch, boolean, multi-badge, atau mata uang |
| `nilai-kosong` | — §4.1 T-FAFM-01: satu-satunya kolom Files bernilai kosong `—` adalah Reference, dan Reference tidak ditampilkan pada Kategori Asset Photo (§4.2d SRC-01 Reference `—`); kolom lain Tidak pernah kosong. Kolom yang tidak ada pada Kategori aktif tidak ikut ekspor (§5 TBL-06e), jadi nilai kosong tidak pernah sampai ke berkas Download tab Files; Recycle Bin dan Asset Data butuh record modul lain |

### berkas-csv@tabel-files · VD-D3

| Varian | Entri |
|---|---|
| `nilai-koma` | ✓ DU-070-9 |
| `nilai-kutip` | ✓ DU-070-7 |
| `non-ascii` | ✓ DU-070-10 |
| `nilai-baris-baru` | — §4.1 T-FAFM-01: kolom Files bertipe Text, Badge, Number, atau Date satu baris, tanpa kolom teks multibaris, dan §4.2d memetakan Reference ke ID, section, atau nama field satu baris; PRD tidak menetapkan nilai berisi baris baru pada tab Files |

### volume-download@tabel-files · VD-A13

| Varian | Entri |
|---|---|
| `di-bawah-ambang` | ✓ DU-091-4 |
| `tepat-ambang` | ✓ DU-091-5 |
| `lebih-ambang` | ✓ DU-091-6 |

### kolom-total-size@tabel-asset-data · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-010-3, DU-010-7 |
| `sama-tiebreak` | ✓ DU-010-4 |
| `natural` | ✓ DU-010-5, DU-010-7 |
| `per-tipe-kolom:badge` | ✓ DU-010-5 |
| `default-beda` | ✓ DU-010-5 |
| `lintas-halaman` | ✓ DU-010-9 |
| `format-komposit` | ✓ DU-010-4, DU-010-6 |
| `kosong` | — §4.1 T-FAFM-02: kolom Data & Log Size dan Files Size tampil «0.0 KB» dan Total Size «Tidak pernah kosong» |
| `beda-kapital` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `aksen` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `diawali-angka-simbol` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `sisip-beda-default` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `sama-melintasi-halaman` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `sama-di-kolom-dan-default` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `jumlah-chip-sama` | — §4.1 T-FAFM-02: tab Asset Data tidak punya kolom multi-badge atau ikon aktif yang diurutkan menurut jumlah |
| `jumlah-aktif-sama` | — §4.1 T-FAFM-02: tab Asset Data tidak punya kolom multi-badge atau ikon aktif yang diurutkan menurut jumlah |
| `campuran-tipe` | — §4.1 T-FAFM-02: tidak ada kolom bertipe data campuran |
| `nama-tampil-beda-nama-penuh` | — TBL-04e: mekanik sort (kapital, aksen, awalan simbol, tiebreak dan pembagian halaman) seragam dengan §9.7 dan diuji pada tab Files |
| `urutan-custom` | — §4.1 T-FAFM-02: kolom Status diurutkan Alphabetical tanpa urutan lifecycle custom |
| `urutan-beda-antar-kolom` | — §4.1 T-FAFM-02: tiap kolom memakai urutan standar |

### kolom-filter@tabel-asset-data · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-010-1, DU-010-18, DU-010-19, DU-010-26 |
| `tidak-cocok` | ✓ DU-010-2, DU-010-8 |
| `rentang-dalam` | ✓ DU-010-3, DU-010-20, DU-010-24 |
| `rentang-luar` | ✓ DU-010-23, DU-010-25 |
| `range-hanya-min` | ✓ DU-010-5, DU-010-21 |
| `range-hanya-max` | ✓ DU-010-4, DU-010-22 |
| `per-kelas-kontrol:Multi-select searchable` | ✓ DU-010-6 |
| `per-kelas-kontrol:Tree picker multi-select` | ✓ DU-010-1 |
| `per-kelas-kontrol:Range Min–Max` | ✓ DU-010-3 |
| `per-kelas-kontrol:Date range picker` | ✓ DU-010-4, DU-010-24 |
| `and-a-saja` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-b-saja` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-keduanya` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-tidak-keduanya` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `or-dalam-field` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-saja` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-saja` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-dan-filter` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `irisan-kosong` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `kolom-tersembunyi` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-only` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `boolean-kedua-nilai` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `rentang-tepat-awal` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-tepat-akhir` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-sehari` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-tepat-min` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-tepat-max` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-min-lebih-max` | — §4.4 dan TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `custom-field-per-tipe` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `mutasi-keluar-saringan` | — L169 FAFM-LOGIC-08d: tab Asset Data read-only; baris berubah hanya lewat Delete Asset Data atau perubahan status lisensi yang dimiliki spec -dep |
| `mutasi-masuk-saringan` | — L169 FAFM-LOGIC-08d: tab Asset Data read-only; baris berubah hanya lewat Delete Asset Data atau perubahan status lisensi yang dimiliki spec -dep |
| `create-tidak-cocok` | — L169 FAFM-LOGIC-08d: tab Asset Data read-only; baris berubah hanya lewat Delete Asset Data atau perubahan status lisensi yang dimiliki spec -dep |
| `status-dikecualikan` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-lolos` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-tersaring` | — §4.1 T-FAFM-02: tab Asset Data tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |

### kolom-status@tabel-asset-data · VD-T7

| Varian | Entri |
|---|---|
| `null` | ✓ DU-086-2, DU-086-3 |
| `nol-numerik` | ✓ DU-086-3 |
| `teks-panjang` | ✓ DU-086-4, DU-086-9 |
| `per-nilai-badge:Disposed` | ✓ DU-086-1 |
| `per-nilai-badge:Unmanaged` | ✓ DU-086-2 |
| `tanpa-foto` | ✓ DU-086-2 |
| `angka-ribuan` | ✓ DU-086-4 |
| `angka-pembulatan` | ✓ DU-086-1 |
| `nilai-turunan` | ✓ DU-086-5 |
| `string-kosong` | — §4.1 T-FAFM-02: Name, Asset ID, Group, Status, dan Total Size «Tidak pernah kosong» |
| `array-kosong` | — §4.1 T-FAFM-02: kolom lain pada tab Asset Data tidak bertipe array, boolean, atau memuat aktor System |
| `boolean-null` | — §4.1 T-FAFM-02: kolom lain pada tab Asset Data tidak bertipe array, boolean, atau memuat aktor System |
| `tanggal-null` | — §4.1 T-FAFM-02: Name, Asset ID, Group, Status, dan Total Size «Tidak pernah kosong» |
| `kosong-tidak-pernah-diisi` | — §4.1 T-FAFM-02: Name, Asset ID, Group, Status, dan Total Size «Tidak pernah kosong» |
| `kosong-setelah-dihapus` | — L169 FAFM-LOGIC-08d: tab Asset Data read-only; aset keluar dari tab bukan menampilkan nilai kosong |
| `teks-panjang-multibaris` | — §4.1 T-FAFM-02: tidak ada kolom teks multibaris |
| `nilai-beda-antar-kolom` | — §4.1 T-FAFM-02: PRD tidak menetapkan kolom yang rawan tertukar |
| `aktor-system` | — §4.1 T-FAFM-02: kolom lain pada tab Asset Data tidak bertipe array, boolean, atau memuat aktor System |
| `asal-jalur` | — L166 FAFM-LOGIC-08a: baris tab Asset Data diturunkan dari status aset, bukan dari jalur Import |
| `referensi-terhapus` | — L166 FAFM-LOGIC-08a: aset yang dihapus lewat Delete Asset Data keluar dari tab |
| `referensi-diarsipkan` | — §4.1 T-FAFM-02: PRD tidak mengenal rujukan berstatus arsip |

### kolom-auto-purge-in@tabel-recycle-bin · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-011-3, DU-011-5 |
| `sama-tiebreak` | ✓ DU-011-3, DU-011-4 |
| `natural` | ✓ DU-011-5, DU-011-6 |
| `per-tipe-kolom:tanggal` | ✓ DU-011-7 |
| `lintas-halaman` | ✓ DU-011-8 |
| `kosong` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `beda-kapital` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `aksen` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `diawali-angka-simbol` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `sisip-beda-default` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `sama-melintasi-halaman` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `sama-di-kolom-dan-default` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `jumlah-chip-sama` | — §4.1 T-FAFM-03: Recycle Bin tidak punya kolom multi-badge atau ikon aktif |
| `jumlah-aktif-sama` | — §4.1 T-FAFM-03: Recycle Bin tidak punya kolom multi-badge atau ikon aktif |
| `campuran-tipe` | — §4.1 T-FAFM-03: tidak ada kolom bertipe data campuran |
| `format-komposit` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `nama-tampil-beda-nama-penuh` | — TBL-04e: mekanik sort seragam §9.7 dan diuji pada tab Files |
| `urutan-custom` | — §4.1 T-FAFM-03: tidak ada urutan custom per nilai |
| `urutan-beda-antar-kolom` | — §4.1 T-FAFM-03: tiap kolom memakai urutan standar |
| `default-beda` | — §4.1 T-FAFM-03 Auto-Purge In: Deleted Date + durasi retensi Lifecycle Settings (satu nilai untuk seluruh item; pengaturan retensi di luar scope, Ringkasan Cepat), sehingga default Deleted Date menurun (§5 TBL-04c, §9.5) selalu sama dengan Auto-Purge In menurun; batas purge per item hanya ditulis ulang job Lifecycle Settings (§9.7), bukan aksi File Manager |

### auto-purge-in@tabel-recycle-bin · VD-A9

| Varian | Entri |
|---|---|
| `di-recycle-bin` | ✓ DU-011-3, DU-011-4, DU-011-5, DU-011-8 |
| `sisa-waktu-beragam` | ✓ DU-011-3, DU-011-5, DU-011-6, DU-011-7 |
| `bin-kosong` | — S-04 / §7.1: copy Recycle Bin genuinely kosong dimiliki target empty-state@tabel-recycle-bin:entitas-kosong di UI-087; Recycle Bin dipakai bersama seluruh spec suite dan E2E-011 tidak punya entitas khusus (IN-2), sehingga bin kosong tidak dibentuk di spec ui-e2e |
| `recover-per-state-asal` | — L126 FAFM-LOGIC-03b: tidak ada Recover atau Restore pada File Manager |
| `recover-dengan-relasi` | — L126 FAFM-LOGIC-03b: tidak ada Recover atau Restore pada File Manager |
| `bin-sampai-10` | — L127 FAFM-LOGIC-03c: tidak ada Empty All, sehingga tidak ada body konfirmasi berdasarkan jumlah item |
| `bin-lebih-10` | — L127 FAFM-LOGIC-03c: tidak ada Empty All, sehingga tidak ada body konfirmasi berdasarkan jumlah item |

### kolom-filter@tabel-recycle-bin · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-011-2, DU-011-9, DU-011-10, DU-011-11 |
| `tidak-cocok` | ✓ DU-011-1 |
| `rentang-dalam` | ✓ DU-011-12, DU-011-16, DU-011-17 |
| `rentang-luar` | ✓ DU-011-15, DU-011-18 |
| `range-hanya-min` | ✓ DU-011-13 |
| `range-hanya-max` | ✓ DU-011-14 |
| `per-kelas-kontrol:Multi-select searchable` | ✓ DU-011-9 |
| `per-kelas-kontrol:Tree picker multi-select` | ✓ DU-011-2 |
| `per-kelas-kontrol:Range Min–Max` | ✓ DU-011-12 |
| `per-kelas-kontrol:Date range picker` | ✓ DU-011-17 |
| `and-a-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-b-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-keduanya` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-tidak-keduanya` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `or-dalam-field` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-dan-filter` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `irisan-kosong` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `kolom-tersembunyi` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-only` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `boolean-kedua-nilai` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `rentang-tepat-awal` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-tepat-akhir` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-sehari` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-tepat-min` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-tepat-max` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-min-lebih-max` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `custom-field-per-tipe` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `mutasi-keluar-saringan` | — L125 FAFM-LOGIC-03a: baris Recycle Bin berubah hanya lewat Delete, Permanently Delete, auto-purge, atau cascade purge |
| `mutasi-masuk-saringan` | — L125 FAFM-LOGIC-03a: baris Recycle Bin berubah hanya lewat Delete, Permanently Delete, auto-purge, atau cascade purge |
| `create-tidak-cocok` | — L125 FAFM-LOGIC-03a: baris Recycle Bin berubah hanya lewat Delete, Permanently Delete, auto-purge, atau cascade purge |
| `status-dikecualikan` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-lolos` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-tersaring` | — §4.1 T-FAFM-03: Recycle Bin tidak punya field filter boolean, custom field, filter-only, atau filter pre-applied |

### kolom-filter@tabel-changelog · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-012-3, DU-012-4, DU-012-8, DU-012-9, DU-012-10, DU-012-13, DU-012-14 |
| `tidak-cocok` | ✓ DU-012-5, DU-012-7 |
| `rentang-dalam` | ✓ DU-012-3, DU-012-4, DU-012-11 |
| `rentang-luar` | ✓ DU-012-12 |
| `per-kelas-kontrol:Multi-select searchable` | ✓ DU-012-5, DU-012-10 |
| `per-kelas-kontrol:Date range picker` | ✓ DU-012-11 |
| `and-a-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-b-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-keduanya` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `and-tidak-keduanya` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `or-dalam-field` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-saja` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `search-dan-filter` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `irisan-kosong` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `kolom-tersembunyi` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `filter-only` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `boolean-kedua-nilai` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `rentang-tepat-awal` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-tepat-akhir` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `rentang-sehari` | — TBL-03d: mekanik Filter Panel, gabungan Search dan Filter, serta AND dan OR seragam §9.8 dan diuji pada tab Files |
| `range-tepat-min` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `range-tepat-max` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `range-hanya-min` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `range-hanya-max` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `range-min-lebih-max` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `custom-field-per-tipe` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `mutasi-keluar-saringan` | — §8.1: Changelog append-only; entri tidak diubah atau dibuat lewat jalur lain |
| `mutasi-masuk-saringan` | — §8.1: Changelog append-only; entri tidak diubah atau dibuat lewat jalur lain |
| `create-tidak-cocok` | — §8.1: Changelog append-only; entri tidak diubah atau dibuat lewat jalur lain |
| `status-dikecualikan` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-lolos` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |
| `default-filter-tersaring` | — §4.1 T-FAFM-04: Changelog tidak punya filter numerik Min-Max, boolean, custom field, filter-only, atau filter pre-applied |

### aksi@tabel-changelog · VD-L1

| Varian | Entri |
|---|---|
| `delete` | ✓ DU-012-3 |
| `per-baris-pencatatan:Delete` | ✓ DU-012-3, DU-012-5, DU-012-6 |
| `per-baris-pencatatan:Permanently Delete` | ✓ DU-012-4, DU-012-7 |
| `nilai-kosong` | ✓ DU-012-3, DU-012-4 |
| `create` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `edit-per-field` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `bulk` | — §8.1#r6: bulk menulis satu entri per file yang diproses; dicakup varian delete pada pemilik be-log |
| `per-aksi-non-crud` | — §8.1: aksi yang dicatat hanya Delete dan Permanently Delete |
| `per-varian-jalur` | — §8.1#r5: jalur non-form dicakup target jalur@tabel-changelog |
| `per-sub-konteks` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `field-sub-item` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `field-permission` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `field-badge-enum` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `field-tanpa-teks` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `nilai-awal` | — §8.1: File Manager tidak punya aksi approval, event sesi, atau log per-record dengan katalog event |
| `assign` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `remove` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `update-setelah-assign` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `approve-dari-approvals` | — §8.1: File Manager tidak punya aksi approval, event sesi, atau log per-record dengan katalog event |
| `reject-dari-approvals` | — §8.1: File Manager tidak punya aksi approval, event sesi, atau log per-record dengan katalog event |
| `settings-tanpa-nama` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `reset-ke-default` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `reset-sudah-default` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |
| `per-event` | — §8.1: File Manager tidak punya aksi approval, event sesi, atau log per-record dengan katalog event |
| `event-sesi` | — §8.1: File Manager tidak punya aksi approval, event sesi, atau log per-record dengan katalog event |
| `edit-multi-field` | — §8.1: Changelog File Manager hanya mencatat Delete dan Permanently Delete atas Field File Name |

### jalur@tabel-changelog · VD-A8

| Varian | Entri |
|---|---|
| `per-jalur:auto-transition` | ✓ DU-073-16 |
| `per-jalur:auto-purge` | ✓ DU-073-19 |
| `per-jalur:cascade purge` | ✓ DU-073-20 |
| `per-jalur:Delete manual` | ✓ DU-073-11 |
| `dengan-aktor` | ✓ DU-073-11 |
| `tanpa-aktor` | ✓ DU-073-19 |
| `butuh-normalisasi` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |
| `pasangan-manual-setara` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |
| `duplikat-dalam-batch` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |
| `duplikat-dengan-data-ada` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |
| `import-semua-valid` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |
| `import-sebagian-error` | — L118 FAFM-LOGIC-01g: File Manager tidak punya Create atau Edit dan tidak menerima Import, sehingga varian jalur form dan Import tidak ada |

### tanpa-log@tabel-changelog · VD-L2

| Varian | Entri |
|---|---|
| `efek-samping-tanpa-log` | ✓ DU-073-22 |
| `record-lain-tak-terlibat` | ✓ DU-073-15 |
| `bulk-dengan-skip` | ✓ DU-073-14 |
| `tanpa-perubahan` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit, jadi tidak ada Save tanpa perubahan |
| `entri-entitas-lain` | — §9.11#p1: baris Changelog dibatasi scope client aktor; isolasi tenant dicakup target scope@tabel-files |

### snapshot@tabel-changelog · VD-L3

| Varian | Entri |
|---|---|
| `snapshot-setelah-rename` | ✓ DU-073-2 |
| `timestamp-sama` | ✓ DU-073-12, DU-073-13 |
| `multi-entri-aktor-beda` | ✓ DU-073-11 |
| `record-tanpa-entri` | ✓ DU-073-21 |
| `edit-beruntun` | — §8.1: File Manager tidak punya Edit atau rename file, jadi tidak ada edit beruntun |
| `edit-nama-sendiri` | — §8.1: File Manager tidak punya Edit atau rename file, jadi tidak ada edit beruntun |
| `edit-beruntun-dua-aktor` | — §8.1: File Manager tidak punya Edit atau rename file, jadi tidak ada edit beruntun |

### aktor@tabel-changelog · VD-L4

| Varian | Entri |
|---|---|
| `aktor-system` | ✓ DU-012-6, DU-012-7, DU-058-7, DU-093-3 |
| `aktor-beda-target` | ✓ DU-012-2, DU-012-5, DU-093-2 |
| `asal-modul-lain` | ✓ DU-012-6, DU-058-2 |
| `log-entitas-terkait` | — §8.1#b2: entri Delete Asset Data dimiliki log asset-list, bukan Changelog File Manager |

### matriks-role@tabel-files · VD-P1

| Varian | Entri |
|---|---|
| `per-baris-matriks:Total Control` | ✓ DU-031-1 |
| `per-baris-matriks:Read Only` | ✓ DU-032-1 |
| `per-baris-matriks:Group Manager` | ✓ DU-033-1 |
| `per-baris-matriks:Manage files: Read` | ✓ DU-034-1 |
| `per-baris-matriks:Manage files: Delete` | ✓ DU-035-1 |
| `tanpa-akses` | ✓ DU-030-1 |
| `read-only-saja` | ✓ DU-032-1 |
| `capability-tunggal:Delete` | ✓ DU-035-1, DU-036-1 |
| `tanpa-capability-aksi:Delete` | ✓ DU-032-1 |
| `tanpa-bulk` | ✓ DU-032-1 |
| `kombinasi-permission` | — §9.3: File Manager hanya memiliki capability Read dan Delete; tidak ada Create atau Update |
| `per-kombinasi-crud` | — §9.3: File Manager hanya memiliki capability Read dan Delete; tidak ada Create atau Update |
| `tanpa-single-action` | — §4.8: aksi baris Delete dan Permanently Delete mengikuti capability Delete yang sama dengan bulk |
| `tanpa-sesi` | — §9.3#p1: penegakan server dimiliki target request langsung pada spec be-pertahanan |
| `access-level-null-plus-individual` | — §2: File Manager tidak memakai access level dan hanya memakai role Total Control, Read Only, Group Manager, dan Manage files |
| `zero-assignment` | — §2#r2: Manage files diberikan per group yang di-assign; PRD tidak menetapkan role tanpa assignment group |
| `can-read-false` | — §9.3: PRD tidak menetapkan assignment dengan can_read bernilai false |
| `assignment-retained` | — §2: File Manager tidak memakai switch role dengan assignment tersimpan |
| `entitas-diblok-punya-role` | — §9.4.1#r1: aktor dari client Suspended, Expired, atau Grace tetap dapat membaca; aksi tulis dimiliki target state-entitas@tabel-files |
| `per-jenis-entitas` | — §9.11: File Manager hanya melayani aktor Client; tidak ada varian Principal, Distributor, atau Partner |
| `per-peran-alur` | — §4.1a: tidak ada alur requester atau approver pada File Manager |

### scope@tabel-files · VD-P2

| Varian | Entri |
|---|---|
| `luar-entitas` | ✓ DU-033-5 |
| `luar-group` | ✓ DU-033-4 |
| `multi-group` | ✓ DU-033-3 |
| `scope-sub-tree` | ✓ DU-033-1 |
| `assignment-node-descendant` | ✓ DU-033-3 |
| `dua-aktor-scope-beda` | ✓ DU-033-4 |
| `client-multi-partner` | — §9.11: File Manager hanya melayani aktor Client; tidak ada Client yang dipegang dua Partner |
| `client-transitif` | — §9.11: File Manager hanya melayani aktor Client; tidak ada jaringan Distributor atau Partner |
| `target-write-transitif` | — §9.11: tidak ada target write lewat jaringan Distributor atau Partner |
| `target-write-langsung` | — §9.11: tidak ada target write lewat bind langsung antar entitas |
| `field-termask` | — §9.11#r1: kolom «Semua field», tidak ada field yang di-mask |
| `field-terbatas-per-role` | — §9.11: kolom «Semua field» untuk seluruh role |
| `scope-exact-match` | — L137 FAFM-LOGIC-05d: Manage files berlaku pada group yang di-assign beserta descendant, bukan exact match |

### state-entitas@tabel-files · VD-A4

| Varian | Entri |
|---|---|
| `active` | ✓ DU-028-1 |
| `suspended` | ✓ DU-028-1 |
| `expired` | ✓ DU-028-1 |
| `job-sistem` | ✓ DU-028-7 |
| `per-interval:Grace` | ✓ DU-028-1 |
| `deleted` | — §9.4.1#r1: PRD hanya menyatakan Suspended, Expired, dan Grace; entitas terhapus tidak disebut |
| `per-jenis-entitas-pemilik` | — §9.11: File Manager hanya melayani aktor Client |
| `per-peran-entitas` | — §9.11: tidak ada peran penerima atau pengalokasi pada File Manager |
| `aksi-reaktivasi` | — §9.4.1#r1: File Manager tidak memiliki aksi reaktivasi |

### akses-url@modul-file-manager · VD-P4

| Varian | Entri |
|---|---|
| `aktor-tanpa-read` | ✓ DU-030-1 |
| `id-sudah-dihapus` | ✓ DU-030-2 |
| `id-milik-entitas-lain` | ✓ DU-030-3 |
| `id-tidak-ada` | — §4.1a#p13: File Manager tidak punya Detail page berbasis ID di URL; ID file hanya dipakai aksi |

### capability-dicabut@modul-file-manager · VD-P7

| Varian | Entri |
|---|---|
| `capability-dicabut-halaman-terbuka` | ✓ DU-029-1 |
| `email-diganti-token-lama` | — §2: File Manager tidak menangani email atau token |
| `password-diganti-sesi-aktif` | — §2: File Manager tidak menangani kredensial |
| `role-dicabut-sesi-aktif` | — §9.3: pencabutan diasersi sebagai pencabutan capability Delete pada halaman terbuka |

### scope-purchase@tabel-files · VD-P2

| Varian | Entri |
|---|---|
| `luar-group` | ✓ DU-037-5 |
| `field-terbatas-per-role` | ✓ DU-037-3 |
| `dua-aktor-scope-beda` | ✓ DU-037-1, DU-037-2 |
| `luar-entitas` | — §9.11: File Manager hanya melayani aktor Client |
| `multi-group` | — §9.11#r8: visibilitas Purchase bergantung pada akses Attachments kelompok Purchase, bukan pada kombinasi group |
| `client-multi-partner` | — §9.11: File Manager hanya melayani aktor Client |
| `client-transitif` | — §9.11: File Manager hanya melayani aktor Client |
| `target-write-transitif` | — §9.11: File Manager hanya melayani aktor Client |
| `target-write-langsung` | — §9.11: File Manager hanya melayani aktor Client |
| `field-termask` | — §9.11#r8: baris Attachment kelompok Purchase tidak ada, bukan di-mask |
| `scope-sub-tree` | — §9.11#r8: visibilitas Purchase tidak bergantung pada tree group |
| `scope-exact-match` | — §9.11#r8: visibilitas Purchase tidak bergantung pada scope group |
| `assignment-node-descendant` | — §9.11#r8: visibilitas Purchase tidak bergantung pada assignment node |

### aksi-tulis@file · VD-A7

| Varian | Entri |
|---|---|
| `dihapus-pihak-lain` | ✓ DU-072-13, DU-072-17 |
| `per-pasangan-aksi:Delete-Delete` | ✓ DU-072-8 |
| `per-pasangan-aksi:Delete-auto-transition` | ✓ DU-072-9 |
| `per-pasangan-aksi:Permanently Delete-Permanently Delete` | ✓ DU-072-11 |
| `per-pasangan-aksi:Permanently Delete-auto-purge` | ✓ DU-072-12 |
| `diubah-pihak-lain` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `target-sama-nilai-beda` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `target-beda` | — §9.4.1#r6: PRD hanya menyatakan balapan atas file yang sama |
| `create-nilai-sama-serentak` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `create-bersamaan` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `status-diubah-pihak-lain` | — L124 FAFM-LOGIC-02f: status record sumber tidak mengubah aksi File Manager |
| `jadi-dipakai-saat-confirm` | — L120 FAFM-LOGIC-02b: File Manager tidak punya guard in-use, jadi tidak ada keadaan «jadi dipakai saat confirm» |
| `bulk-semua-jadi-dipakai` | — L120 FAFM-LOGIC-02b: File Manager tidak punya guard in-use, jadi tidak ada keadaan «jadi dipakai saat confirm» |
| `bulk-sebagian-jadi-dipakai` | — L120 FAFM-LOGIC-02b: File Manager tidak punya guard in-use, jadi tidak ada keadaan «jadi dipakai saat confirm» |
| `nilai-guard-berubah` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `dibuat-pihak-lain` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |
| `pihak-lain-cocok-saringan` | — §4.4: tidak ada live update antar-aktor yang dinyatakan PRD; Delete memperbarui tab Files dan Recycle Bin hanya lewat refresh |
| `pihak-lain-tidak-cocok-saringan` | — §4.4: tidak ada live update antar-aktor yang dinyatakan PRD; Delete memperbarui tab Files dan Recycle Bin hanya lewat refresh |
| `pihak-lain-halaman-lain` | — §4.4: tidak ada live update antar-aktor yang dinyatakan PRD; Delete memperbarui tab Files dan Recycle Bin hanya lewat refresh |
| `pihak-lain-ubah-baris-terseleksi` | — §4.4: tidak ada live update antar-aktor yang dinyatakan PRD; Delete memperbarui tab Files dan Recycle Bin hanya lewat refresh |
| `permintaan-basi` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit atau Create, jadi tidak ada konflik nilai antar-aktor |

### rujukan-file@modul-sumber · VD-A11

| Varian | Entri |
|---|---|
| `linked-item` | ✓ DU-024-2, DU-024-6, DU-024-10, DU-024-12 |
| `pending-in-flight` | ✓ DU-024-4 |
| `punya-anak` | — §4.1a#p13: File Manager tidak punya relasi induk-anak antar file |
| `tanpa-anak` | — §4.1a#p13: File Manager tidak punya relasi induk-anak antar file |
| `log-menunjuk` | — §8.1#b1: entri log modul sumber dicakup spec dep-activity-log |
| `assignment-luar-constraint` | — §9.4.1#r14: PRD tidak menyatakan assignment yang dicabut otomatis oleh Delete file |

### selection-limit@tabel-files · VD-A6

| Varian | Entri |
|---|---|
| `per-jenis-limit:Selection Limit` | ✓ DU-085-1 |
| `di-bawah` | ✓ DU-085-2 |
| `tepat-batas` | ✓ DU-085-3 |
| `lebih-batas` | ✓ DU-085-4 |
| `tersaring-lebih-limit` | ✓ DU-085-5 |
| `sisa-satu` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `over-cap-downgrade` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `tersimpan-melebihi-batas-baru` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `berurutan-stay-on-form` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `saldo-cukup` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `saldo-kurang` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `kuota-status-akun` | — §9.10: File Manager tidak punya limit Master Data atau limit Storage sendiri |
| `limit-diturunkan` | — §4.1a#p11: Selection Limit dikelola `plans-licensing-lifecycle-settings` §9.9 dan tidak disalin di PRD ini; §9.10#p1 File Manager tidak punya limit sendiri. Suite memakai satu nilai lingkungan 1000 dan tidak mengubahnya (IN-2, RC-17), sehingga limit yang lebih kecil bukan keadaan yang dibentuk spec |
| `tanpa-cap-mobile` | — §4.6#p3: Select All mobile ada di selection mode kartu Android (spec E2E-039), bukan di tabel web spec ini (PF-7); tanpa cap hanya teramati pada lebih dari 1000 kartu termuat, volume yang tidak dibentuk di ui-e2e (RC-4) |

### konsumen@modul-sumber · VD-X1

| Varian | Entri |
|---|---|
| `konsumen-relasi` | ✓ DU-047-2 |
| `konsumen-sudah-ada` | ✓ DU-047-2 |
| `arah-b-ke-a` | ✓ DU-047-3 |
| `propagasi-event` | ✓ DU-047-3 |
| `konsumen-snapshot` | — §8.1#b3: Changelog menyimpan snapshot kelompok file dan dicakup target aksi@tabel-changelog |
| `fk-create` | — L112 FAFM-LOGIC-01a: File Manager tidak membuat record yang dikonsumsi modul lain |
| `fk-edit` | — L138 FAFM-LOGIC-05e: File Manager tidak punya Edit |
| `fk-delete` | — L121 FAFM-LOGIC-02c: yang dihapus adalah file, bukan record yang dirujuk modul sumber sebagai opsi dropdown |
| `per-konsekuensi-lifecycle` | — §9.7: konsekuensi lifecycle yang dinyatakan PRD hanya Delete file |
| `arah-a-ke-b` | — L1989 SYN-01e: arah efek hanya dari File Manager ke modul sumber |
| `state-reflected` | — L2060 SYN-11a: state reflected hanya durasi retensi, dimiliki target setting@recycle-bin |
| `per-konsumen` | — §11#r1: PRD mencantumkan modul sumber sebagai satu baris konsumen; efeknya diasersi per modul pada spec -dep masing-masing |
| `state-dari-modul-trigger` | — §9.7#p2: PRD tidak menyatakan state yang dikirim modul pemicu selain rujukan file |
| `turunan` | — L1993 SYN-01i: label tab hanya dihitung ulang server pada pembacaan berikutnya |

### setting@recycle-bin · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-055-1 |
| `nilai-diubah` | ✓ DU-055-2 |
| `record-sebelum-perubahan` | ✓ DU-055-4 |
| `record-sesudah-perubahan` | ✓ DU-055-5 |
| `per-nilai-setting` | — L2065 SYN-11f: durasi retensi dipakai sebagai satu angka; varian per nilai dicakup nilai-default dan nilai-diubah |
| `per-opsi-format-tanggal` | — §4.1: bukan setting format tanggal |
| `zona-waktu-non-default` | — §4.1: bukan setting zona waktu |
| `format-regional-beda-entitas` | — L2060 SYN-11a: durasi retensi berlaku platform-wide |

### format-tanggal@modul · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-057-1 |
| `nilai-diubah` | ✓ DU-057-2 |
| `per-opsi-format-tanggal:dd/MM/yy` | ✓ DU-057-1 |
| `per-opsi-format-tanggal:M/d/yy` | ✓ DU-057-2 |
| `per-opsi-format-tanggal:dd MMM yy` | ✓ DU-057-3 |
| `per-opsi-format-tanggal:DDD, MMM dd, yy` | ✓ DU-057-4 |
| `per-opsi-format-tanggal:DDD, MMM dd, yyyy` | ✓ DU-057-5 |
| `per-nilai-setting` | — §4.1: setting yang dibaca hanya Date Format dan Time Format |
| `record-sebelum-perubahan` | — L337 INV-11d: kolom tanggal memakai format setting saat dibaca, tanpa snapshot format saat record dibuat |
| `record-sesudah-perubahan` | — L337 INV-11d: kolom tanggal memakai format setting saat dibaca |
| `zona-waktu-non-default` | — §4.1 T-FAFM-01: PRD tidak menetapkan perilaku khusus zona waktu selain format General Settings |
| `format-regional-beda-entitas` | — §4.1: PRD tidak menetapkan perilaku dua entitas dengan format berbeda dalam satu spec |

### flag@guided-tooltip · VD-S3

| Varian | Entri |
|---|---|
| `flag-belum` | ✓ DU-015-1, DU-015-2 |
| `flag-sudah` | ✓ DU-015-1 |
| `flag-sudah-device-lain` | ✓ DU-015-1 |
| `aktor-lain` | ✓ DU-015-2 |

### preferensi@setup-column · VD-S3

| Varian | Entri |
|---|---|
| `flag-belum` | ✓ DU-014-1, DU-014-2 |
| `flag-sudah` | ✓ DU-014-1, DU-014-3 |
| `flag-sudah-device-lain` | ✓ DU-014-1 |
| `aktor-lain` | ✓ DU-014-2 |

### status-aset@tab-asset-data · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Active` | ✓ DU-010-10 |
| `per-status:Disposed` | ✓ DU-010-3, DU-010-4, DU-010-5 |
| `per-status:Unmanaged` | ✓ DU-010-6, DU-010-7, DU-010-8, DU-010-9 |
| `per-status:Draft` | ✓ DU-010-11 |
| `transisi-valid` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `transisi-mundur` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `transisi-ilegal` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `state-final` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `sudah-di-state-tujuan` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `state-transien` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `flag-terkunci` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `per-kondisi-disabled` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `koheren-rantai-gate` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |

### draft-asset@tab-files · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Draft` | ✓ DU-044-4 |
| `transisi-valid` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `transisi-mundur` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `transisi-ilegal` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `state-final` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `sudah-di-state-tujuan` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `state-transien` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `flag-terkunci` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `per-kondisi-disabled` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |
| `koheren-rantai-gate` | — §9.4.1#r3: File Manager tidak memiliki transisi status record sendiri; status aset dimiliki modul lain |

### search@tabel-files · VD-F17

| Varian | Entri |
|---|---|
| `payload-xss` | ✓ DU-002-30 |
| `payload-sqli` | ✓ DU-002-31 |
| `payload-nosqli` | ✓ DU-002-32 |
| `markup-tersimpan` | ✓ DU-002-33 |

### kartu-storage-usage@kartu · VD-T11

| Varian | Entri |
|---|---|
| `angka-unik-per-metric` | ✓ DU-017-2, DU-017-3, DU-017-4, DU-017-5, DU-017-9 |
| `nol` | ✓ DU-017-6 |
| `mutasi-penggeser` | ✓ DU-017-4 |
| `detail-lintas-halaman` | — §4.2c: kartu Storage Usage tidak punya aksi ke daftar rinci |
| `detail-dikecualikan` | — §4.2c: kartu Storage Usage tidak punya aksi ke daftar rinci |

## Entri

- **DU-001-1** File (awal), File Asset Photo milik aset Active: File Name `laptop-front-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-2** File (awal), Attachment kelompok General: File Name `warranty-card-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-3** File (awal), Custom Field Document milik aset Unmanaged: File Name `warranty-scan-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-4** File (awal), Damaged Photo: File Name `damage-01-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Damaged Photo` (13 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar), Size `900.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-001-5** File (awal), Repair Photo: File Name `repair-02-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Repair Photo` (12 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar), Size `880.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-001-6** File (awal), Found Photo: File Name `found-01-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Found Photo` (11 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar), Size `700.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-7** File (awal), Maintenance Before Photo aktif milik aset Disposed: File Name `maint-before-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `750.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-001-8** File (awal), Maintenance After Photo: File Name `maint-after-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Maintenance After Photo` (23 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `1.9 MB` (6 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-9** File (awal), Disposal Document milik aset Disposed: File Name `dsp-auction-receipt-{runId}.pdf` (31 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `3.2 MB` (6 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-10** File (awal), Handover Photo dari Borrow: File Name `handover-brw-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-001-11** File (awal), Return Photo dari Borrow: File Name `return-brw-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Return Photo` (12 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `610.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-12** File (awal), Handover Photo dari Assignment: File Name `handover-asg-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `630.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-13** File (awal), Return Photo dari Assignment: File Name `return-asg-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Return Photo` (12 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `600.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-14** File (awal), Send Photo dari Transfer: File Name `send-trf-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Send Photo` (10 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `560.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-15** File (awal), Receive Photo dari Transfer: File Name `receive-trf-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Receive Photo` (13 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `570.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-16** File (awal), Maintenance Before Photo yang sudah di-soft-delete: File Name `maint-before-old-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `700.0 KB` (8 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-001-17** Kata kunci Search (dicoba), Kata kunci Search nama berkas di Recycle Bin: Kata Kunci `maint-before-old-{runId}` (24 kar) · sumber turunan penulis
- **DU-002-1** File (awal), File di tab Asset Documents: File Name `Procurement-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `150.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-2** File (awal), File di tab Asset Documents: File Name `numerik-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `412.7 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-3** File (awal), File di tab Asset Documents: File Name `divisi-aset-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Aset {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-4** File (awal), File di tab Asset Documents: File Name `lintas-{runId}-a.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-5** File (awal), File di tab Asset Documents: File Name `scan-dokumen-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer lintas-{runId}` (22 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-6** File (awal), File di tab Asset Documents: File Name `laporan_100%-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-7** File (awal), File di tab Asset Documents: File Name `laporanA1000-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-8** File (awal), File di tab Asset Documents: File Name `budget-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-9** File (awal), File di tab Asset Documents: File Name `annual report-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-10** File (awal), File di tab Asset Documents: File Name `Head Office Room-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-11** File (awal), File di tab Asset Documents: File Name `cabang-utama-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Cabang {runId}` (14 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-12** File (awal), File di tab Asset Documents: File Name `cabang-utara-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Cabang {runId} Utara` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-13** File (awal), File di tab Asset Documents: File Name `garansi-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Kartu Garansi {runId}` (21 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-14** File (awal), File di tab Asset Documents: File Name `<b>Finance</b>-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber PRD §4.1 Files Example Data
- **DU-002-15** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `curement-{runId}` (16 kar) · sumber EB-SRC-1
- **DU-002-16** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `procurement-{runId}` (19 kar) · sumber EB-SRC-1
- **DU-002-17** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `412.7` (5 kar) · sumber turunan penulis
- **DU-002-18** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Divisi Aset {runId}` (19 kar) · sumber EB-SRC-2@tabel-files
- **DU-002-19** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `zzqx-{runId}` (12 kar) · sumber EB-SRC-1
- **DU-002-20** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `bagian tanggal dari Upload Date baris lintas-{runId}-a.pdf` (58 kar) · sumber EB-SRC-2@tabel-files
- **DU-002-21** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `lintas-{runId}` (14 kar) · sumber EB-SRC-2@tabel-files
- **DU-002-22** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci ` budget-{runId} ` (16 kar) · sumber EB-SRC-3@tabel-files
- **DU-002-23** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `   ` (3 kar) · sumber EB-SRC-3@tabel-files
- **DU-002-24** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `annual report-{runId}` (21 kar) · sumber EB-SRC-3@tabel-files
- **DU-002-25** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Head Room-{runId}` (17 kar) · sumber TBL-03c
- **DU-002-26** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Cabang {runId}` (14 kar) · sumber TBL-03c
- **DU-002-27** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `_100%-{runId}` (13 kar) · sumber EB-SRC-3@tabel-files
- **DU-002-28** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `.*-{runId}` (10 kar) · sumber EB-SRC-3@tabel-files
- **DU-002-29** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Kartu Garansi {runId}` (21 kar) · sumber EB-SRC-5@tabel-files
- **DU-002-30** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `<script>alert(1)</script>` (25 kar) · sumber turunan penulis
- **DU-002-31** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `' OR '1'='1` (11 kar) · sumber turunan penulis
- **DU-002-32** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `{"$ne": null}` (13 kar) · sumber turunan penulis
- **DU-002-33** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `<b>Finance</b>-{runId}` (22 kar) · sumber turunan penulis
- **DU-002-34** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `PDF` (3 kar) · sumber turunan penulis
- **DU-002-35** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Custom Field Document` (21 kar) · sumber turunan penulis
- **DU-002-36** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Asset ID milik DU-002-5` (23 kar) · sumber turunan penulis
- **DU-002-37** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Dewi L` (6 kar) · sumber turunan penulis
- **DU-002-38** File (awal), File di tab selain Asset Documents: File Name `foto-depan-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `800.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber T-FAFM-01
- **DU-002-39** File (awal), File di tab selain Asset Documents: File Name `penemuan-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Found Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Divisi Umum {runId}` (19 kar), Size `700.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber T-FAFM-01
- **DU-002-40** File (awal), File di tab selain Asset Documents: File Name `dsp-bukti-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Asset `Mesin Fotokopi Canon {runId}` (28 kar), Group `Divisi Umum {runId}` (19 kar), Size `300.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber T-FAFM-01
- **DU-002-41** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `foto-depan-{runId}` (18 kar) · sumber T-FAFM-01
- **DU-002-42** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Asset Photo` (11 kar) · sumber T-FAFM-01
- **DU-002-43** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `penemuan-{runId}` (16 kar) · sumber T-FAFM-01
- **DU-002-44** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Found Photo` (11 kar) · sumber T-FAFM-01
- **DU-002-45** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `dsp-bukti-{runId}` (17 kar) · sumber T-FAFM-01
- **DU-002-46** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `Disposal Document` (17 kar) · sumber T-FAFM-01
- **DU-003-1** File (awal), File di tab Asset Documents: File Name `charlie-nm-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-2** File (awal), File di tab Asset Documents: File Name `alpha-nm-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-3** File (awal), File di tab Asset Documents: File Name `Bravo-nm-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-4** File (awal), File di tab Asset Documents: File Name `Ezra-ak-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-5** File (awal), File di tab Asset Documents: File Name `Elan-ak-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-6** File (awal), File di tab Asset Documents: File Name `Élan-ak-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-7** File (awal), File di tab Asset Documents: File Name `alpha-sy-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-8** File (awal), File di tab Asset Documents: File Name `3D-printer-sy-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-9** File (awal), File di tab Asset Documents: File Name `#gudang-sy-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-10** File (awal), File di tab Asset Documents: File Name `s100-sz-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-11** File (awal), File di tab Asset Documents: File Name `s2-sz-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `2.0 KB` (6 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-12** File (awal), File di tab Asset Documents: File Name `s1200-sz-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `1.2 MB` (6 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-13** File (awal), File di tab Asset Documents: File Name `s10-sz-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `10.0 KB` (7 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-14** File (awal), File di tab Asset Documents: File Name `s900-sz-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `900.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-15** File (awal), File di tab Asset Documents: File Name `tgl1-dt-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-16** File (awal), File di tab Asset Documents: File Name `tgl2-dt-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-17** File (awal), File di tab Asset Documents: File Name `tgl3-dt-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-18** File (awal), File di tab Asset Documents: File Name `grp1-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-19** File (awal), File di tab Asset Documents: File Name `grp2-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Beta {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-20** File (awal), File di tab Asset Documents: File Name `grp3-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-21** File (awal), File di tab Asset Documents: File Name `grp4-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Beta {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-22** File (awal), File di tab Asset Documents: File Name `tie1-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Gamma {runId}` (18 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-23** File (awal), File di tab Asset Documents: File Name `tie2-gr-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Gamma {runId}` (18 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-24** File (awal), File di tab Asset Documents: File Name `up2-up-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Nama Lengkap Pengunggah `Budi Sanjaya {runId}` (20 kar) · sumber turunan penulis
- **DU-003-25** File (awal), File di tab Asset Documents: File Name `up3-up-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Agus W` (6 kar), Nama Lengkap Pengunggah `Agus Wibowo {runId}` (19 kar) · sumber turunan penulis
- **DU-003-26** File (awal), File di tab Asset Documents: File Name `up1-up-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Nama Lengkap Pengunggah `Budi Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-003-27** File (awal; 12 record), File di tab Asset Documents: File Name `vol-{n}-pg-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Aset Alfa {runId}` (17 kar), Size `{n}0.0 KB` (9 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-28** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-nm-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-29** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-ak-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-30** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-sy-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-31** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-sz-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-32** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-dt-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-33** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-gr-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-34** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-up-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-35** Kata kunci Search (dicoba), Akhiran nama berkas untuk mempersempit tabel ke data spec ini: Kata Kunci `-pg-{runId}` (11 kar) · sumber turunan penulis
- **DU-003-36** File (awal), File untuk sort kolom teks A-Z: File Name `ala-az-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Urut Beta {runId}` (22 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-37** File (awal), File untuk sort kolom teks A-Z: File Name `bmb-az-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Custom Field Document` (21 kar), Reference `Kartu Urut {runId}` (18 kar), Asset `Aset Urut Alfa {runId}` (22 kar), Group `Aset Alfa {runId}` (17 kar), Size `100.0 KB` (8 kar), Uploaded By `Sari U` (6 kar) · sumber turunan penulis
- **DU-003-38** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `-az-{runId}` (11 kar) · sumber turunan penulis
- **DU-004-1** File (awal), File di tab Asset Documents: File Name `aa-pdf-att-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-2** File (awal), File di tab Asset Documents: File Name `bb-jpg-cfd-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Custom Field Document` (21 kar), Reference `Kartu Filter {runId}` (20 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-3** File (awal), File di tab Asset Documents: File Name `ab-pdf-cfd-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Kartu Filter {runId}` (20 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-4** File (awal), File di tab Asset Documents: File Name `nn-jpg-att-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-5** File (awal), File di tab Asset Documents: File Name `or-png-att-{runId}.png` (22 kar), File Format `PNG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-6** File (awal), File di tab Asset Documents: File Name `laporan-sf-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-7** File (awal), File di tab Asset Documents: File Name `laporan-sf-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-8** File (awal), File di tab Asset Documents: File Name `gambar-sf-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-9** File (awal), File di tab Asset Documents: File Name `gambar-sf-{runId}.png` (21 kar), File Format `PNG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-10** File (awal), File di tab Asset Documents: File Name `sz100-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-11** File (awal), File di tab Asset Documents: File Name `sz200-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `200.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-12** File (awal), File di tab Asset Documents: File Name `sz300-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `300.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-13** File (awal), File di tab Asset Documents: File Name `sz400-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `400.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-14** File (awal), File di tab Asset Documents: File Name `dt10-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 10 hari, pukul 11:20` (25 kar) · sumber turunan penulis
- **DU-004-15** File (awal), File di tab Asset Documents: File Name `dt07-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 7 hari, pukul 11:20` (24 kar) · sumber turunan penulis
- **DU-004-16** File (awal), File di tab Asset Documents: File Name `dt06-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 6 hari, pukul 11:20` (24 kar) · sumber turunan penulis
- **DU-004-17** File (awal), File di tab Asset Documents: File Name `dt05-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 5 hari, pukul 11:20` (24 kar) · sumber turunan penulis
- **DU-004-18** File (awal), File di tab Asset Documents: File Name `dt02-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 2 hari, pukul 11:20` (24 kar) · sumber turunan penulis
- **DU-004-19** File (awal), File di tab Asset Documents: File Name `dt01-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar), Upload Date `T0 − 1 hari, pukul 11:20` (24 kar) · sumber turunan penulis
- **DU-004-20** File (awal), File di tab Asset Documents: File Name `dmg-lain-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Damaged Photo` (13 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-21** File (awal; dimutasi TC-FA-FAFM-E2E-004-tab-files-filter), File di tab Asset Documents: File Name `rename-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer Lama {runId}` (20 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-22** File (awal; 8 record), File di tab Asset Documents: File Name `overflow-{n}-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Panjang {n} Untuk Uji Overflow Chip {runId}` (48 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-23** Group (awal), Group tanpa file: Group `Grup Kosong {runId}` (19 kar) · sumber turunan penulis
- **DU-004-24** User (awal), User tanpa file: Nama Lengkap `Pengunggah Kosong {runId}` (25 kar) · sumber turunan penulis
- **DU-004-25** File (dibuat), File baru ditambahkan pengguna lain saat uji: File Name `baru-opsi-{runId}.odt` (21 kar), File Format `ODT` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Filter {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Rudi H` (6 kar) · sumber turunan penulis
- **DU-004-26** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `laporan-sf-{runId}` (18 kar) · sumber turunan penulis
- **DU-004-27** Nama aset (dicoba), Nama aset sesudah diubah pengguna lain: Asset `Printer Baru {runId}` (20 kar) · sumber turunan penulis
- **DU-004-28** Kata kunci Search (dicoba), Kata kunci dalam dropdown filter: Kata Kunci `aset panjang` (12 kar) · sumber turunan penulis
- **DU-004-29** Kata kunci Search (dicoba), Kata kunci dalam dropdown filter: Kata Kunci `Panjang 3` (9 kar) · sumber turunan penulis
- **DU-004-30** Kata kunci Search (dicoba), Kata kunci dalam dropdown filter: Kata Kunci `zzqx-{runId}` (12 kar) · sumber turunan penulis
- **DU-004-31** Rentang Size (dicoba), Min dan Max inklusif: Min `200` (3 kar), Max `300` (3 kar) · sumber turunan penulis
- **DU-004-32** Rentang Size (dicoba), Hanya Min: Min `300` (3 kar) · sumber turunan penulis
- **DU-004-33** Rentang Size (dicoba), Hanya Max: Max `200` (3 kar) · sumber turunan penulis
- **DU-004-35** Rentang Upload Date (dicoba), Rentang beberapa hari: Mulai `T0 − 6 hari` (11 kar), Selesai `T0 − 2 hari` (11 kar) · sumber turunan penulis
- **DU-004-36** Rentang Upload Date (dicoba), Rentang satu hari: Mulai `T0 − 5 hari` (11 kar), Selesai `T0 − 5 hari` (11 kar) · sumber turunan penulis
- **DU-004-37** Pilihan filter (dicoba), Opsi Tree picker Group: Group `Grup Filter {runId}` (19 kar) · sumber turunan penulis
- **DU-004-38** Pilihan filter (dicoba), Rentang tanggal sebagai kontrol: Upload Date `Select date` (11 kar) · sumber turunan penulis
- **DU-004-39** File (awal; dimutasi TC-FA-FAFM-E2E-004-tab-files-filter), File pembawa nilai opsi Asset terakhir, dihapus aktor lain saat uji: File Name `hilang-opsi-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Aset Hilang {runId}` (19 kar), Group `Grup Filter {runId}` (19 kar), Size `100.0 KB` (8 kar), Uploaded By `Wulan S` (7 kar) · sumber turunan penulis
- **DU-004-40** Kata kunci Search (dicoba), Kata kunci Search yang mencocokkan beberapa file: Kata Kunci `sf-{runId}` (10 kar) · sumber turunan penulis
- **DU-004-41** Nama aset (dicoba), Nama aset sesudah diubah lagi pengguna lain sehingga tidak cocok dengan Search: Asset `Printer Akhir {runId}` (21 kar) · sumber turunan penulis
- **DU-004-42** Kata kunci Search (dicoba), Kata kunci Search nama aset sebelum diubah: Kata Kunci `Printer Baru {runId}` (20 kar) · sumber turunan penulis
- **DU-004-43** Pilihan filter (dicoba), Opsi Uploaded By pengunggah file: Uploaded By `Wulan Sari {runId}` (18 kar) · sumber turunan penulis
- **DU-005-1** File (awal; 21 record; dimutasi TC-FA-FAFM-E2E-005-tab-files-paginasi-select-all), File Asset Photo di entitas khusus: File Name `foto-{n}-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 Unit {n} {runId}` (42 kar), Group `Gudang Utama {runId}` (20 kar), Size `500.0 KB` (8 kar), Uploaded By `Maya P` (6 kar) · sumber turunan penulis
- **DU-006-1** File (awal; 9 record), File di tab Asset Documents: File Name `dok-{n}-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Mesin Cetak {runId}` (19 kar), Group `Gudang Pusat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Citra D` (7 kar) · sumber turunan penulis
- **DU-006-2** File (awal; 2 record), File di tab Asset Documents: File Name `gbr-{n}-{runId}.png` (19 kar), File Format `PNG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Mesin Cetak {runId}` (19 kar), Group `Gudang Pusat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Citra D` (7 kar) · sumber turunan penulis
- **DU-006-3** File (awal; 3 record), File di tab Asset Documents: File Name `lap-{n}-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Mesin Cetak {runId}` (19 kar), Group `Gudang Pusat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Citra D` (7 kar) · sumber turunan penulis
- **DU-006-4** File (awal; 3 record), File di tab Asset Photo: File Name `foto-{n}-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Mesin Cetak {runId}` (19 kar), Group `Gudang Pusat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Citra D` (7 kar) · sumber turunan penulis
- **DU-006-5** Kata kunci Search (dicoba), Kata kunci Search: Kata Kunci `lap-` (4 kar) · sumber turunan penulis
- **DU-006-6** Pilihan filter (dicoba), Filter File Format: File Format `PNG` (3 kar) · sumber turunan penulis
- **DU-007-1** File (awal; dimutasi TC-FA-FAFM-E2E-007-download-asset-data-recycle-bin-changelog), File di tab Asset Documents yang di-delete: File Name `kontrak-sewa-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer Canon iR2206 {runId}` (28 kar), Group `Kantor Pusat {runId}` (20 kar), Size `250.0 KB` (8 kar), Uploaded By `Wulan P` (7 kar) · sumber turunan penulis
- **DU-007-2** Asset (awal), Aset Disposed di tab Asset Data: Name `Printer Canon iR2206 {runId}` (28 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Disposed` (8 kar) · sumber turunan penulis
- **DU-007-3** Asset (awal), Aset Unmanaged di tab Asset Data: Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Unmanaged` (9 kar) · sumber turunan penulis
- **DU-008-1** File (awal), File di tab Asset Documents: File Name `proposal-vendor-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Genset Cummins C220 {runId}` (27 kar), Group `Pabrik Karawang {runId}` (23 kar), Size `300.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber turunan penulis
- **DU-008-2** File (awal), File di tab Asset Documents: File Name `spesifikasi-teknis-{runId}.pdf` (30 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Genset Cummins C220 {runId}` (27 kar), Group `Pabrik Karawang {runId}` (23 kar), Size `450.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber turunan penulis
- **DU-008-3** File (awal), File di tab Asset Documents: File Name `foto-instalasi-{runId}.png` (26 kar), File Format `PNG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Genset Cummins C220 {runId}` (27 kar), Group `Pabrik Karawang {runId}` (23 kar), Size `200.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber turunan penulis
- **DU-008-4** File (awal; dimutasi TC-FA-FAFM-E2E-008-download-file-dan-zip), File di tab Asset Documents: File Name `berita-acara-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Genset Cummins C220 {runId}` (27 kar), Group `Pabrik Karawang {runId}` (23 kar), Size `150.0 KB` (8 kar), Uploaded By `Dewi L` (6 kar) · sumber turunan penulis
- **DU-009-1** File (awal), File di tab Asset Documents: File Name `laporan-inspeksi-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Toyota 8FD25 {runId}` (29 kar), Group `Gudang Cikarang {runId}` (23 kar), Size `400.0 KB` (8 kar), Uploaded By `Hendra W` (8 kar) · sumber turunan penulis
- **DU-009-2** File (awal), File di tab Asset Documents: File Name `denah-lokasi-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Toyota 8FD25 {runId}` (29 kar), Group `Gudang Cikarang {runId}` (23 kar), Size `250.0 KB` (8 kar), Uploaded By `Hendra W` (8 kar) · sumber turunan penulis
- **DU-009-3** File (awal), File di tab Asset Documents: File Name `rekap-biaya-{runId}.xlsx` (24 kar), File Format `XLSX` (4 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Forklift Toyota 8FD25 {runId}` (29 kar), Group `Gudang Cikarang {runId}` (23 kar), Size `120.0 KB` (8 kar), Uploaded By `Hendra W` (8 kar) · sumber turunan penulis
- **DU-009-4** File (awal), File di tab Asset Documents: File Name `notulen-vendor-{runId}.docx` (27 kar), File Format `DOCX` (4 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Toyota 8FD25 {runId}` (29 kar), Group `Gudang Cikarang {runId}` (23 kar), Size `90.0 KB` (7 kar), Uploaded By `Hendra W` (8 kar) · sumber turunan penulis
- **DU-009-5** File (awal; dimutasi TC-FA-FAFM-E2E-009-preview-file-web), File di tab Asset Documents: File Name `notulen-rapat-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Toyota 8FD25 {runId}` (29 kar), Group `Gudang Cikarang {runId}` (23 kar), Size `180.0 KB` (8 kar), Uploaded By `Hendra W` (8 kar) · sumber turunan penulis
- **DU-010-1** Group (awal), Group induk aset Disposed: Name `Kantor Pusat {runId}` (20 kar) · sumber turunan penulis
- **DU-010-2** Group (awal), Group aset Unmanaged: Name `Cabang Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-010-3** Asset (awal; dimutasi TC-FA-FAFM-E2E-010-tab-asset-data), Aset Disposed: Name `Excavator Komatsu PC200 {runId}` (31 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Disposed` (8 kar), Register Date `T0 − 30 hari` (12 kar), Files Size `6.0 MB (dari 4.0 MB + 2.0 MB)` (29 kar), Division `Logistik {runId}` (16 kar), Alias Name `Ekskavator Proyek Timur {runId}` (31 kar), Brand `Komatsu Indonesia {runId}` (25 kar), Model/Type `PC200-8M0 {runId}` (17 kar), Category `Alat Berat {runId}` (18 kar) · sumber turunan penulis
- **DU-010-4** Asset (awal), Aset Disposed: Name `Forklift Heli CPCD30 {runId}` (28 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Disposed` (8 kar), Register Date `T0 − 20 hari` (12 kar), Files Size `900.0 KB (dari 900.0 KB)` (24 kar), Division `Logistik {runId}` (16 kar) · sumber turunan penulis
- **DU-010-5** Asset (awal), Aset Disposed: Name `Mixer Beton Schwing {runId}` (27 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Disposed` (8 kar), Register Date `T0 − 10 hari` (12 kar), Files Size `10.0 MB (dari 10.0 MB)` (22 kar), Division `Logistik {runId}` (16 kar), Alias Name `Mixer Proyek Barat {runId}` (26 kar), Brand `Schwing Stetter {runId}` (23 kar), Model/Type `SP500-M {runId}` (15 kar), Category `Alat Berat {runId}` (18 kar) · sumber turunan penulis
- **DU-010-6** Asset (awal), Aset Unmanaged: Name `Printer Epson L3250 {runId}` (27 kar), Group `Cabang Surabaya {runId}` (23 kar), Status `Unmanaged` (9 kar), Register Date `T0 − 4 hari` (11 kar), Files Size `1.2 MB (dari 1.2 MB)` (20 kar), Division `Keuangan {runId}` (16 kar), Alias Name `Printer Lantai Dua {runId}` (26 kar), Brand `Epson Indonesia {runId}` (23 kar), Model/Type `EcoTank Seri 3 {runId}` (22 kar), Category `Perangkat Kantor {runId}` (24 kar) · sumber turunan penulis
- **DU-010-7** Asset (awal), Aset Unmanaged: Name `Scanner Canon DR-C225 {runId}` (29 kar), Group `Cabang Surabaya {runId}` (23 kar), Status `Unmanaged` (9 kar), Register Date `T0 − 3 hari` (11 kar), Files Size `2.0 MB (dari 2.0 MB)` (20 kar), Division `Logistik {runId}` (16 kar) · sumber turunan penulis
- **DU-010-8** Asset (awal), Aset Unmanaged: Name `Router Mikrotik RB4011 {runId}` (30 kar), Group `Cabang Surabaya {runId}` (23 kar), Status `Unmanaged` (9 kar), Register Date `T0 − 2 hari` (11 kar), Files Size `0.0 KB` (6 kar) · sumber turunan penulis
- **DU-010-9** Asset (awal; 8 record), Aset Unmanaged: Name `Aset Massal {n} {runId}` (23 kar), Group `Cabang Surabaya {runId}` (23 kar), Status `Unmanaged` (9 kar), Register Date `T0 − 2 hari` (11 kar), Files Size `0.0 KB` (6 kar) · sumber turunan penulis
- **DU-010-10** Asset (awal), Aset Active tidak didaftar: Name `Truk Hino 500 {runId}` (21 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-010-11** Asset (awal), Aset Draft tidak didaftar: Name `Kompresor Atlas Copco {runId}` (29 kar), Group `Kantor Pusat {runId}` (20 kar), Status `Draft` (5 kar) · sumber turunan penulis
- **DU-010-12** File (awal), File di tab Asset Documents: File Name `serah-terima-ekskavator-{runId}.pdf` (35 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Excavator Komatsu PC200 {runId}` (31 kar), Group `Kantor Pusat {runId}` (20 kar), Size `4.0 MB` (6 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-13** File (awal; dimutasi TC-FA-FAFM-E2E-010-tab-asset-data), File di tab Asset Documents: File Name `foto-lelang-ekskavator-{runId}.pdf` (34 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Excavator Komatsu PC200 {runId}` (31 kar), Group `Kantor Pusat {runId}` (20 kar), Size `2.0 MB` (6 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-14** File (awal), File di tab Asset Documents: File Name `manual-forklift-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Heli CPCD30 {runId}` (28 kar), Group `Kantor Pusat {runId}` (20 kar), Size `900.0 KB` (8 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-15** File (awal), File di tab Asset Documents: File Name `kontrak-mixer-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Mixer Beton Schwing {runId}` (27 kar), Group `Kantor Pusat {runId}` (20 kar), Size `10.0 MB` (7 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-16** File (awal), File di tab Asset Documents: File Name `invoice-printer-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer Epson L3250 {runId}` (27 kar), Group `Cabang Surabaya {runId}` (23 kar), Size `1.2 MB` (6 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-17** File (awal), File di tab Asset Documents: File Name `panduan-scanner-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Scanner Canon DR-C225 {runId}` (29 kar), Group `Cabang Surabaya {runId}` (23 kar), Size `2.0 MB` (6 kar), Uploaded By `Rahmat H` (8 kar) · sumber turunan penulis
- **DU-010-18** Kata kunci Search (dicoba), Kata kunci Search nama aset: Kata Kunci `PC200 {runId}` (13 kar) · sumber turunan penulis
- **DU-010-19** Kata kunci Search (dicoba), Kata kunci Search Group: Kata Kunci `Cabang Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-010-26** Kata kunci Search (dicoba), Kata kunci Search nama file: Kata Kunci `foto-lelang-ekskavator-{runId}` (30 kar) · sumber turunan penulis
- **DU-010-20** Rentang Files Size (dicoba), Rentang Files Size dalam: Min `1000` (4 kar), Max `7000` (4 kar) · sumber turunan penulis
- **DU-010-21** Rentang Files Size (dicoba), Hanya batas bawah: Min `5000` (4 kar) · sumber turunan penulis
- **DU-010-22** Rentang Files Size (dicoba), Hanya batas atas: Max `1000` (4 kar) · sumber turunan penulis
- **DU-010-23** Rentang Files Size (dicoba), Rentang di luar nilai: Min `20000` (5 kar), Max `30000` (5 kar) · sumber turunan penulis
- **DU-010-24** Rentang Register Date (dicoba), Rentang tanggal dalam: Dari `T0 − 25 hari` (12 kar), Sampai `T0 − 15 hari` (12 kar) · sumber turunan penulis
- **DU-010-25** Rentang Register Date (dicoba), Rentang tanggal di luar: Dari `T0 − 60 hari` (12 kar), Sampai `T0 − 40 hari` (12 kar) · sumber turunan penulis
- **DU-010-27** User (awal), Group Manager dengan cakupan satu group: Nama Lengkap `Bima Pengelola {runId}` (22 kar), Role `Group Manager` (13 kar), Group yang dikelola `Cabang Surabaya {runId}` (23 kar) · sumber matriks role PRD
- **DU-011-1** Group (awal), Group induk file: Name `Kantor Pusat {runId}` (20 kar) · sumber turunan penulis
- **DU-011-2** Group (awal), Group aset Damaged: Name `Cabang Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-011-3** File (awal), File di Recycle Bin: File Name `kontrak-lama-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Asset `Genset Perkins 404 {runId}` (26 kar), Group `Kantor Pusat {runId}` (20 kar), Size `1.0 MB` (6 kar), Deleted Date `T0 − 5 hari` (11 kar), Deleted By `Bagus P` (7 kar), Auto-Purge In `25 days (dari Deleted Date dan retensi 30 hari)` (47 kar) · sumber turunan penulis
- **DU-011-4** File (awal), File di Recycle Bin: File Name `panduan-genset-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Custom Field Document` (21 kar), Asset `Genset Perkins 404 {runId}` (26 kar), Group `Kantor Pusat {runId}` (20 kar), Size `500.0 KB` (8 kar), Deleted Date `T0 − 6 hari` (11 kar), Deleted By `Bagus P` (7 kar), Auto-Purge In `24 days` (7 kar) · sumber turunan penulis
- **DU-011-5** File (awal), File di Recycle Bin: File Name `foto-kerusakan-truk-{runId}.jpg` (31 kar), File Format `JPG` (3 kar), Category `Damaged` (7 kar), Source `Damaged Photo` (13 kar), Asset `Truk Mitsubishi Fuso {runId}` (28 kar), Group `Cabang Surabaya {runId}` (23 kar), Size `900.0 KB` (8 kar), Deleted Date `T0 − 20 hari` (12 kar), Deleted By `System` (6 kar), Auto-Purge In `10 days (dari Deleted Date dan retensi 30 hari)` (47 kar) · sumber turunan penulis
- **DU-011-6** File (awal), File di Recycle Bin: File Name `foto-perbaikan-truk-{runId}.jpg` (31 kar), File Format `JPG` (3 kar), Category `Damaged` (7 kar), Source `Repair Photo` (12 kar), Asset `Truk Mitsubishi Fuso {runId}` (28 kar), Group `Cabang Surabaya {runId}` (23 kar), Size `750.0 KB` (8 kar), Deleted Date `T0 − 28 hari` (12 kar), Deleted By `Bagus P` (7 kar), Auto-Purge In `2 days (dari Deleted Date dan retensi 30 hari)` (46 kar) · sumber turunan penulis
- **DU-011-7** File (awal), File di Recycle Bin: File Name `foto-sebelum-servis-{runId}.jpg` (31 kar), File Format `JPG` (3 kar), Category `Maintenance` (11 kar), Source `Maintenance Before Photo` (24 kar), Asset `Mesin Bubut Krisbow {runId}` (27 kar), Group `Kantor Pusat {runId}` (20 kar), Size `1.2 MB` (6 kar), Deleted Date `T0 − 29 hari` (12 kar), Deleted By `System` (6 kar), Auto-Purge In `1 day (dari Deleted Date dan retensi 30 hari)` (45 kar) · sumber turunan penulis
- **DU-011-8** File (awal; 8 record), File di Recycle Bin: File Name `arsip-{n}-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Asset `Genset Perkins 404 {runId}` (26 kar), Group `Kantor Pusat {runId}` (20 kar), Size `100.0 KB` (8 kar), Deleted Date `T0 − 3 hari` (11 kar), Deleted By `System` (6 kar), Auto-Purge In `27 days (dari Deleted Date dan retensi 30 hari)` (47 kar) · sumber turunan penulis
- **DU-011-9** Pilihan filter (dicoba), Filter Category: Category `Damaged` (7 kar) · sumber turunan penulis
- **DU-011-10** Kata kunci Search (dicoba), Kata kunci Search nama file: Kata Kunci `kontrak-lama-{runId}` (20 kar) · sumber turunan penulis
- **DU-011-11** Kata kunci Search (dicoba), Kata kunci Search Asset: Kata Kunci `Truk Mitsubishi Fuso {runId}` (28 kar) · sumber turunan penulis
- **DU-011-12** Rentang Size (dicoba), Rentang Size dalam: Min `600` (3 kar), Max `1000` (4 kar) · sumber turunan penulis
- **DU-011-13** Rentang Size (dicoba), Hanya batas bawah: Min `1200` (4 kar) · sumber turunan penulis
- **DU-011-14** Rentang Size (dicoba), Hanya batas atas: Max `400` (3 kar) · sumber turunan penulis
- **DU-011-15** Rentang Size (dicoba), Rentang di luar nilai: Min `5000` (4 kar), Max `6000` (4 kar) · sumber turunan penulis
- **DU-011-16** Rentang Auto-Purge In (dicoba), Rentang sisa hari: Min `20` (2 kar), Max `26` (2 kar) · sumber turunan penulis
- **DU-011-17** Rentang Deleted Date (dicoba), Rentang tanggal dalam: Dari `T0 − 6 hari` (11 kar), Sampai `T0 − 4 hari` (11 kar) · sumber turunan penulis
- **DU-011-18** Rentang Deleted Date (dicoba), Rentang tanggal di luar: Dari `T0 − 60 hari` (12 kar), Sampai `T0 − 40 hari` (12 kar) · sumber turunan penulis
- **DU-012-1** User (awal), User pencatat entri: Name `Wahyu Pratama {runId}` (21 kar), Tampil `Wahyu P` (7 kar) · sumber turunan penulis
- **DU-012-2** User (awal), User pencatat entri: Name `Nadia Rahayu {runId}` (20 kar), Tampil `Nadia R` (7 kar) · sumber turunan penulis
- **DU-012-3** Changelog (awal), Entri Changelog Delete: Date `T0 − 10 hari, pukul 10:00` (25 kar), Action `Delete` (6 kar), File Name `laporan-bulanan-{runId}.pdf` (27 kar), Field `File Name` (9 kar), Old Value `laporan-bulanan-{runId}.pdf` (27 kar), New Value `—` (1 kar), Modified By `Wahyu P` (7 kar) · sumber turunan penulis
- **DU-012-4** Changelog (awal), Entri Changelog Permanently Delete: Date `T0 − 9 hari, pukul 11:30` (24 kar), Action `Permanently Delete` (18 kar), File Name `laporan-bulanan-{runId}.pdf` (27 kar), Field `File Name` (9 kar), Old Value `laporan-bulanan-{runId}.pdf` (27 kar), New Value `—` (1 kar), Modified By `Wahyu P` (7 kar) · sumber turunan penulis
- **DU-012-5** Changelog (awal), Entri Changelog Delete: Date `T0 − 5 hari, pukul 14:00` (24 kar), Action `Delete` (6 kar), File Name `kontrak-vendor-{runId}.pdf` (26 kar), Field `File Name` (9 kar), Old Value `kontrak-vendor-{runId}.pdf` (26 kar), New Value `—` (1 kar), Modified By `Nadia R` (7 kar) · sumber turunan penulis
- **DU-012-6** Changelog (awal), Entri Changelog Delete: Date `T0 − 3 hari, pukul 08:15` (24 kar), Action `Delete` (6 kar), File Name `foto-lama-{runId}.jpg` (21 kar), Field `File Name` (9 kar), Old Value `foto-lama-{runId}.jpg` (21 kar), New Value `—` (1 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-012-7** Changelog (awal), Entri Changelog Permanently Delete: Date `T0 − 2 hari, pukul 02:00` (24 kar), Action `Permanently Delete` (18 kar), File Name `arsip-lama-{runId}.png` (22 kar), Field `File Name` (9 kar), Old Value `arsip-lama-{runId}.png` (22 kar), New Value `—` (1 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-012-8** Pilihan filter (dicoba), Filter Action: Action `Permanently Delete` (18 kar) · sumber turunan penulis
- **DU-012-9** Pilihan filter (dicoba), Filter File Name: File Name `arsip-lama-{runId}.png` (22 kar) · sumber turunan penulis
- **DU-012-10** Pilihan filter (dicoba), Filter Modified By: Modified By `Nadia Rahayu {runId}` (20 kar) · sumber turunan penulis
- **DU-012-11** Rentang Date (dicoba), Rentang tanggal dalam: Dari `T0 − 11 hari` (12 kar), Sampai `T0 − 9 hari` (11 kar) · sumber turunan penulis
- **DU-012-12** Rentang Date (dicoba), Rentang tanggal di luar: Dari `T0 − 60 hari` (12 kar), Sampai `T0 − 40 hari` (12 kar) · sumber turunan penulis
- **DU-012-13** Kata kunci Search (dicoba), Kata kunci Search File Name: Kata Kunci `laporan-bulanan-{runId}` (23 kar) · sumber turunan penulis
- **DU-012-14** Kata kunci Search (dicoba), Kata kunci Search File Name: Kata Kunci `arsip-lama-{runId}` (18 kar) · sumber turunan penulis
- **DU-013-1** File (awal; 10 record), File tab Asset Documents: File Name `berkas-{n}-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar), Reference `General` (7 kar) · sumber turunan penulis
- **DU-013-2** File (awal), File tab Asset Documents: File Name `berkas-k-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar), Reference `General` (7 kar) · sumber turunan penulis
- **DU-013-3** File (awal), File tab Asset Documents: File Name `berkas-l-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar), Reference `General` (7 kar) · sumber turunan penulis
- **DU-013-4** File (awal), File tab Asset Photo: File Name `foto-a-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar) · sumber turunan penulis
- **DU-013-5** File (awal), File tab Asset Photo: File Name `foto-b-{runId}.png` (18 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar) · sumber turunan penulis
- **DU-013-6** File (awal), File di Recycle Bin: File Name `lama-a-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar) · sumber turunan penulis
- **DU-013-7** File (awal), File di Recycle Bin: File Name `lama-b-{runId}.pdf` (18 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Pompa Hidran {runId}` (20 kar), Group `Gudang Timur {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Fajar N` (7 kar) · sumber turunan penulis
- **DU-013-8** Pilihan filter (dicoba), Filter File Format: File Format `JPG` (3 kar) · sumber turunan penulis
- **DU-013-9** Kata kunci Search (dicoba), Kata kunci Search file Recycle Bin: Kata Kunci `lama-a-{runId}` (14 kar) · sumber turunan penulis
- **DU-013-10** Rows per page (dicoba), Rows per page: Rows per page `25` (2 kar) · sumber turunan penulis
- **DU-013-11** Pilihan filter (dicoba), Pilihan File Format untuk state filter: File Format `PDF` (3 kar) · sumber turunan penulis
- **DU-014-1** User (awal), Aktor pertama pemilik preferensi: Name `Gita Maharani {runId}` (21 kar), Tampil `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-2** User (awal), Aktor kedua tanpa preferensi: Name `Hendra Wijaya {runId}` (21 kar), Tampil `Hendra W` (8 kar) · sumber turunan penulis
- **DU-014-3** Pilihan Column Visibility (dicoba), Kolom Files yang disembunyikan aktor pertama: Kolom disembunyikan `Group` (5 kar) · sumber turunan penulis
- **DU-014-4** File (awal), File tab Asset Documents: File Name `rencana-kerja-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-5** Aset (awal), Aset Disposed untuk tab Asset Data: Name `Bor Tangan Afkir {runId}` (24 kar), Status `Disposed` (8 kar), Group `Gudang Barat {runId}` (20 kar) · sumber turunan penulis
- **DU-014-6** File (awal), File di Recycle Bin: File Name `lama-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar) · sumber turunan penulis
- **DU-014-7** Changelog (awal), Entri Changelog Delete: Date `T0 − 2 hari, pukul 09:00` (24 kar), Action `Delete` (6 kar), File Name `lama-{runId}.pdf` (16 kar), Field `File Name` (9 kar), Old Value `lama-{runId}.pdf` (16 kar), New Value `—` (1 kar), Modified By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-8** Kata kunci Search (dicoba), Kata kunci Search file Changelog: Kata Kunci `lama-{runId}` (12 kar) · sumber turunan penulis
- **DU-014-9** File (awal), File di Recycle Bin untuk uji urutan modal: File Name `sortir-a-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Deleted Date `T0 − 1 hari` (11 kar) · sumber turunan penulis
- **DU-014-10** File (awal), File di Recycle Bin untuk uji urutan modal: File Name `sortir-b-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Deleted Date `T0 − 1 hari` (11 kar) · sumber turunan penulis
- **DU-014-11** Changelog (awal), Entri Changelog untuk uji urutan modal: Date `T0 − 1 hari` (11 kar), Action `Delete` (6 kar), File Name `sortir-a-{runId}.pdf` (20 kar), Field `File Name` (9 kar), Old Value `sortir-a-{runId}.pdf` (20 kar), New Value `—` (1 kar), Modified By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-12** Changelog (awal), Entri Changelog untuk uji urutan modal: Date `T0 − 1 hari` (11 kar), Action `Delete` (6 kar), File Name `sortir-b-{runId}.pdf` (20 kar), Field `File Name` (9 kar), Old Value `sortir-b-{runId}.pdf` (20 kar), New Value `—` (1 kar), Modified By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-14** Pilihan filter (dicoba), Pilihan untuk state tabel modal: Action `Delete` (6 kar) · sumber turunan penulis
- **DU-014-15** Rows per page (dicoba), Pilihan untuk state tabel modal: Rows per page `25` (2 kar) · sumber turunan penulis
- **DU-014-16** Pilihan Setup Column (dicoba), Pilihan untuk state tabel modal: Kolom ditambahkan `Division` (8 kar) · sumber turunan penulis
- **DU-014-17** Pilihan Setup Column (dicoba), Pilihan untuk state tabel modal: Kolom dipindahkan `Size` (4 kar) · sumber turunan penulis
- **DU-014-18** Pilihan Setup Column (dicoba), Pilihan untuk state tabel modal: Kolom di-pin `File Name` (9 kar) · sumber turunan penulis
- **DU-014-13** File (awal; 9 record), File di Recycle Bin untuk uji halaman modal: File Name `massal-{n}-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Deleted Date `T0 − 4 hari` (11 kar) · sumber turunan penulis
- **DU-014-19** Changelog (awal; 9 record), Entri Changelog untuk uji halaman modal: Date `T0 − 4 hari` (11 kar), Action `Delete` (6 kar), File Name `massal-{n}-{runId}.pdf` (22 kar), Field `File Name` (9 kar), Old Value `massal-{n}-{runId}.pdf` (22 kar), New Value `—` (1 kar), Modified By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-20** File (awal), File untuk uji tab Kategori: File Name `foto-aset-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Gita M` (6 kar) · sumber turunan penulis
- **DU-014-21** File (awal), File untuk uji tab Kategori: File Name `kerusakan-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Damaged Photo` (13 kar), Asset `Kompresor Udara {runId}` (23 kar), Group `Gudang Barat {runId}` (20 kar), Size `100.0 KB` (8 kar), Uploaded By `Gita M` (6 kar) · sumber turunan penulis
- **DU-015-1** User (awal; dimutasi TC-FA-FAFM-E2E-015-guided-tooltip-flag), Aktor pertama tanpa flag: Name `Indra Kusuma {runId}` (20 kar), Tampil `Indra K` (7 kar), guided_tooltip_seen_fams-file-manager `belum tersetel` (14 kar) · sumber turunan penulis
- **DU-015-2** User (awal; dimutasi TC-FA-FAFM-E2E-015-guided-tooltip-flag), Aktor kedua tanpa flag: Name `Jihan Safitri {runId}` (21 kar), Tampil `Jihan S` (7 kar), guided_tooltip_seen_fams-file-manager `belum tersetel` (14 kar) · sumber turunan penulis
- **DU-016-1** User (awal), Aktor pembuka halaman pada entitas tanpa file: Name `Kartika Lestari {runId}` (23 kar), Tampil `Kartika L` (9 kar) · sumber turunan penulis
- **DU-017-1** Entitas (awal), Entitas khusus untuk kartu Storage Usage: Name `FAMS Kartu Storage {runId}` (26 kar) · sumber turunan penulis
- **DU-017-2** File (awal), File aktif Asset Photo 300.0 KB: File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `300.0 KB` (8 kar), Ukuran mentah `307200 byte` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-017-3** File (awal), File aktif Damaged Photo 200.0 KB: File Name `damage-01-{runId}.jpg` (21 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `200.0 KB` (8 kar), Ukuran mentah `204800 byte` (11 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-017-4** File (awal; dimutasi TC-FA-FAFM-E2E-017-kartu-storage-usage-nilai), File Recycle Bin 150.0 KB yang dihapus permanen sebagai penggeser: File Name `laptop-old-{runId}.png` (22 kar), Source `Asset Photo` (11 kar), Size `150.0 KB` (8 kar), Ukuran mentah `153600 byte` (11 kar), Deleted By `System` (6 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-017-5** File (awal), File Recycle Bin 100.0 KB yang tetap ada: File Name `repair-02-{runId}.jpg` (21 kar), Source `Repair Photo` (12 kar), Size `100.0 KB` (8 kar), Ukuran mentah `102400 byte` (11 kar), Deleted By `Rina A` (6 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-017-6** Kategori (awal), Kategori Missing tanpa file aktif: Kategori `Missing` (7 kar), File aktif `tidak ada` (9 kar), Total Size `0.0 KB` (6 kar) · sumber turunan penulis
- **DU-017-7** Kuota Storage (awal), Storage Quota entitas khusus: Storage Quota `50.0 GB` (7 kar) · sumber PRD §4.2c Example Data
- **DU-017-8** Aset (awal), Aset Disposed tanpa file yang Data & Log Size-nya masuk Fixed Asset: Name `Printer HP LaserJet {runId}` (27 kar), Status `Disposed` (8 kar), Group `Head Office` (11 kar) · sumber FAFM-LOGIC-06b
- **DU-017-9** File (awal), File di luar aset (Other files) 50.0 KB: File Name `lampiran-servis-{runId}.pdf` (27 kar), Source `Other files` (11 kar), Size `50.0 KB` (7 kar), Ukuran mentah `51200 byte` (10 kar) · sumber FAFM-LOGIC-06b
- **DU-018-1** Entitas (awal), Entitas khusus untuk kartu sesudah Delete: Name `FAMS Kartu Delete {runId}` (25 kar) · sumber turunan penulis
- **DU-018-2** File (awal), File aktif Asset Photo 300.0 KB yang tidak berubah: File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `300.0 KB` (8 kar), Ukuran mentah `307200 byte` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-018-3** File (awal; dimutasi TC-FA-FAFM-E2E-018-kartu-setelah-delete), File aktif Damaged Photo 200.0 KB yang di-Delete: File Name `damage-01-{runId}.jpg` (21 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `200.0 KB` (8 kar), Ukuran mentah `204800 byte` (11 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-018-4** File (awal), File Recycle Bin 100.0 KB yang tetap ada: File Name `repair-02-{runId}.jpg` (21 kar), Source `Repair Photo` (12 kar), Size `100.0 KB` (8 kar), Ukuran mentah `102400 byte` (11 kar), Deleted By `Rina A` (6 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-019-1** Entitas (awal), Entitas khusus untuk kartu sesudah Permanently Delete: Name `FAMS Kartu Permanen {runId}` (27 kar) · sumber turunan penulis
- **DU-019-2** Aset (awal), Aset Active dengan file aktif Asset Photo 300.0 KB: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Status `Active` (6 kar), Group `Head Office` (11 kar), File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `300.0 KB` (8 kar), Ukuran mentah `307200 byte` (11 kar) · sumber turunan penulis
- **DU-019-3** Aset (awal), Aset Disposed pemilik file Recycle Bin: Name `Printer HP LaserJet {runId}` (27 kar), Status `Disposed` (8 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-019-4** File (awal; dimutasi TC-FA-FAFM-E2E-019-kartu-setelah-permanently-delete), File Recycle Bin 150.0 KB milik aset Disposed yang dihapus permanen: File Name `disposal-old-{runId}.pdf` (24 kar), Source `Disposal Document` (17 kar), Size `150.0 KB` (8 kar), Ukuran mentah `153600 byte` (11 kar), Deleted By `System` (6 kar), Asset `Printer HP LaserJet {runId}` (27 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-020-1** Aset (awal), Aset pemilik file yang dihapus: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-020-2** File (awal; dimutasi TC-FA-FAFM-E2E-020-delete-file-single), File Asset Photo yang dihapus single: File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `300.0 KB` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Uploaded By `Budi S` (6 kar) · sumber turunan penulis
- **DU-021-1** Aset (awal), Aset pemilik delapan file Damaged: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-021-2** File (awal; 4 record; dimutasi TC-FA-FAFM-E2E-021-delete-file-bulk), Empat file Damaged Photo bernama panjang untuk bulk Delete: File Name `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` (81 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `150.0 KB` (8 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-021-3** File (awal; 4 record; dimutasi TC-FA-FAFM-E2E-021-delete-file-bulk), Empat file Repair Photo bernama panjang untuk bulk Delete: File Name `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` (81 kar), Source `Repair Photo` (12 kar), Kategori `Damaged` (7 kar), Size `120.0 KB` (8 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-022-1** Aset (awal), Aset pemilik empat file: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-022-2** File (awal; dimutasi TC-FA-FAFM-E2E-022-delete-file-bulk-satu-item), File aktif yang tersisa terpilih pada bulk Delete: File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `300.0 KB` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-022-3** File (awal), File aktif yang dipilih lalu dibatalkan pilihannya pada bulk Delete: File Name `laptop-back-{runId}.jpg` (23 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `280.0 KB` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-022-4** File (awal; dimutasi TC-FA-FAFM-E2E-022-delete-file-bulk-satu-item), File Recycle Bin yang tersisa terpilih pada bulk Permanently Delete: File Name `laptop-old-satu-{runId}.png` (27 kar), Source `Asset Photo` (11 kar), Size `150.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-022-5** File (awal), File Recycle Bin yang dipilih lalu dibatalkan pilihannya: File Name `laptop-old-dua-{runId}.png` (26 kar), Source `Asset Photo` (11 kar), Size `160.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-023-1** Aset (awal), Aset pemilik empat file: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar) · sumber turunan penulis
- **DU-023-2** File (awal; dimutasi TC-FA-FAFM-E2E-023-delete-file-sudah-tidak-tersedia), File yang tetap tersedia dan diproses pada bulk campuran: File Name `scanner-front-{runId}.jpg` (25 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `200.0 KB` (8 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar) · sumber turunan penulis
- **DU-023-3** File (awal; dimutasi TC-FA-FAFM-E2E-023-delete-file-sudah-tidak-tersedia), File yang dihapus permanen aktor kedua setelah dialog bulk terbuka, bersama file tersedia: File Name `scanner-back-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `210.0 KB` (8 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar) · sumber turunan penulis
- **DU-023-4** File (awal; dimutasi TC-FA-FAFM-E2E-023-delete-file-sudah-tidak-tersedia), File pertama dari dua file yang seluruhnya sudah dihapus permanen saat submit: File Name `scanner-left-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `220.0 KB` (8 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar) · sumber turunan penulis
- **DU-023-5** File (awal; dimutasi TC-FA-FAFM-E2E-023-delete-file-sudah-tidak-tersedia), File kedua dari dua file yang seluruhnya sudah dihapus permanen saat submit: File Name `scanner-right-{runId}.jpg` (25 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `230.0 KB` (8 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar) · sumber turunan penulis
- **DU-024-1** Aset (awal), Aset dengan record Damaged aktif: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-024-2** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File Damaged Photo yang dirujuk record Damaged wajib: File Name `damage-bumper-{runId}.jpg` (25 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `400.0 KB` (8 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber EC-02
- **DU-024-3** Aset (awal), Aset dengan transaksi Borrow yang belum Return: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-024-4** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File Handover Photo pada transaksi Borrow yang masih berjalan: File Name `handover-borrow-{runId}.jpg` (27 kar), Source `Handover Photo` (14 kar), Kategori `Borrow` (6 kar), Size `500.0 KB` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber DIM-14d
- **DU-024-5** Aset (awal), Aset Disposed pemilik dokumen Disposal: Name `Printer HP M404 {runId}` (23 kar), Status `Disposed` (8 kar), Group `Branch Bandung` (14 kar) · sumber ACT-02c
- **DU-024-6** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File Disposal Document milik aset Disposed: File Name `dsp-auction-receipt-{runId}.pdf` (31 kar), Source `Disposal Document` (17 kar), Kategori `Disposal` (8 kar), Size `600.0 KB` (8 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar) · sumber ACT-02c
- **DU-024-7** Aset (awal), Aset Unmanaged pemilik file aktif: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Unmanaged` (9 kar) · sumber ACT-02c
- **DU-024-8** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File aktif milik aset Unmanaged: File Name `unmanaged-photo-{runId}.jpg` (27 kar), Source `Asset Photo` (11 kar), Kategori `Asset Photo` (11 kar), Size `250.0 KB` (8 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar) · sumber ACT-02c
- **DU-024-9** Aset (awal), Aset dengan record Damaged aktif untuk bulk Delete: Name `Honda Vario {runId}` (19 kar), Group `Fleet` (5 kar) · sumber FAFM-LOGIC-02a
- **DU-024-10** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File Damaged Photo pertama yang dirujuk record Damaged dan dipilih bulk: File Name `damage-spion-{runId}.jpg` (24 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `180.0 KB` (8 kar), Asset `Honda Vario {runId}` (19 kar), Group `Fleet` (5 kar) · sumber FAFM-LOGIC-02a
- **DU-024-11** Aset (awal), Aset kedua dengan record Damaged aktif untuk bulk Delete: Name `Suzuki Ertiga {runId}` (21 kar), Group `Fleet` (5 kar) · sumber FAFM-LOGIC-02a
- **DU-024-12** File (awal; dimutasi TC-FA-FAFM-E2E-024-delete-file-dirujuk-record), File Damaged Photo kedua yang dirujuk record Damaged dan dipilih bulk: File Name `damage-rem-{runId}.jpg` (22 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `220.0 KB` (8 kar), Asset `Suzuki Ertiga {runId}` (21 kar), Group `Fleet` (5 kar) · sumber FAFM-LOGIC-02a
- **DU-025-1** Aset (awal), Aset pemilik file yang dihapus permanen: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-025-2** File (awal; dimutasi TC-FA-FAFM-E2E-025-permanently-delete-single), File Recycle Bin yang dihapus permanen single: File Name `laptop-old-{runId}.png` (22 kar), Source `Asset Photo` (11 kar), Size `150.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-025-3** Aset (awal), Aset pemilik file pembanding Recycle Bin: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-025-4** File (awal), File Recycle Bin pembanding yang tidak dihapus: File Name `repair-02-{runId}.jpg` (21 kar), Source `Repair Photo` (12 kar), Size `120.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-1** Aset (awal), Aset pemilik file Recycle Bin: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-2** File (awal; 4 record; dimutasi TC-FA-FAFM-E2E-026-permanently-delete-bulk), Empat file Damaged Photo di Recycle Bin bernama panjang: File Name `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` (81 kar), Source `Damaged Photo` (13 kar), Size `150.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-3** File (awal; 4 record; dimutasi TC-FA-FAFM-E2E-026-permanently-delete-bulk), Empat file Repair Photo di Recycle Bin bernama panjang: File Name `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` (81 kar), Source `Repair Photo` (12 kar), Size `120.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-4** File (awal), File pembanding Recycle Bin yang tidak dipilih: File Name `foto-sisa-kendaraan-cabang-medan-{runId}.jpg` (44 kar), Source `Damaged Photo` (13 kar), Size `100.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-5** File (awal; dimutasi TC-FA-FAFM-E2E-026-permanently-delete-bulk), File Recycle Bin satu-satunya yang tetap terpilih pada bulk: File Name `foto-perbaikan-satu-{runId}.jpg` (31 kar), Source `Repair Photo` (12 kar), Size `110.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-026-6** File (awal), File Recycle Bin yang pilihannya dibatalkan sehingga bulk menyisakan satu file: File Name `foto-perbaikan-dua-{runId}.jpg` (30 kar), Source `Repair Photo` (12 kar), Size `115.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-1** Aset (awal), Aset pemilik enam file Recycle Bin: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-2** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File Recycle Bin yang dihapus permanen aktor kedua pada aksi single: File Name `damage-race-{runId}.jpg` (23 kar), Source `Damaged Photo` (13 kar), Size `150.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-3** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File Recycle Bin yang masih tersedia pada bulk campuran (pertama): File Name `damage-1-sebagian-{runId}.jpg` (29 kar), Kata kunci Search `sebagian-{runId}` (16 kar), Source `Damaged Photo` (13 kar), Size `160.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-4** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File Recycle Bin yang dihapus permanen aktor kedua setelah dialog bulk terbuka: File Name `damage-2-sebagian-{runId}.jpg` (29 kar), Source `Damaged Photo` (13 kar), Size `170.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-5** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File Recycle Bin yang masih tersedia pada bulk campuran (ketiga): File Name `damage-3-sebagian-{runId}.jpg` (29 kar), Source `Damaged Photo` (13 kar), Size `180.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-6** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File pertama dari dua file yang seluruhnya sudah dihapus permanen saat submit: File Name `damage-1-seluruh-{runId}.jpg` (28 kar), Kata kunci Search `seluruh-{runId}` (15 kar), Source `Damaged Photo` (13 kar), Size `190.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-027-7** File (awal; dimutasi TC-FA-FAFM-E2E-027-permanently-delete-sudah-tidak-tersedia), File kedua dari dua file yang seluruhnya sudah dihapus permanen saat submit: File Name `damage-2-seluruh-{runId}.jpg` (28 kar), Source `Damaged Photo` (13 kar), Size `200.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-028-1** Entitas (awal), Entitas khusus yang diubah statusnya oleh operator: Name `FAMS State {runId}` (18 kar), Status awal `Active` (6 kar) · sumber turunan penulis
- **DU-028-2** User (awal), Total Control pelaku: Name `Maya Putri {runId}` (18 kar), Role `Total Control` (13 kar) · sumber turunan penulis
- **DU-028-3** User (awal), Operator Admin Console di luar tenant: Name `Operator Admin Console {runId}` (30 kar) · sumber turunan penulis
- **DU-028-4** Aset (awal), Aset pemilik file: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-028-5** File (awal), File aktif pertama yang ditolak di-Delete: File Name `damage-aktif-1-{runId}.jpg` (26 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `200.0 KB` (8 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-028-6** File (awal), File aktif kedua pada Delete bulk: File Name `damage-aktif-2-{runId}.jpg` (26 kar), Source `Damaged Photo` (13 kar), Kategori `Damaged` (7 kar), Size `210.0 KB` (8 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-028-7** File (awal), File Recycle Bin pemicu job auto-purge: File Name `damage-bin-1-{runId}.jpg` (24 kar), Source `Damaged Photo` (13 kar), Size `150.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-028-8** File (awal), File Recycle Bin kedua pada Permanently Delete bulk: File Name `damage-bin-2-{runId}.jpg` (24 kar), Source `Damaged Photo` (13 kar), Size `160.0 KB` (8 kar), Deleted By `System` (6 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-029-1** User (awal; dimutasi TC-FA-FAFM-E2E-029-capability-dicabut-halaman-terbuka), Pemegang Manage files Read dan Delete pada group Head Office yang capability Delete-nya dicabut saat halaman terbuka: Name `Sari Pengelola File {runId}` (27 kar), Role `Pengelola File Head Office {runId}` (34 kar), Capability `Manage files: Read, Delete` (26 kar), Group `Head Office` (11 kar) · sumber matriks role PRD
- **DU-029-2** User (awal), Admin Total Control yang mencabut capability: Name `Admin Pusat {runId}` (19 kar), Role `Total Control` (13 kar), Group `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-029-3** File (awal), File Asset Photo di group Head Office yang dicoba dihapus: File Name `laptop-front-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `milik aset DU-029-3` (19 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 3 hari, pukul 14:30` (24 kar) · sumber PRD §4.1 Files Example Data
- **DU-030-1** User (awal), Aktor tanpa capability File Manager apa pun: Name `Rahmat Tanpa Akses {runId}` (26 kar), Role `Pengguna tanpa capability File Manager` (38 kar), Capability `tidak ada` (9 kar) · sumber matriks role PRD
- **DU-030-2** File (awal), File yang sudah dihapus permanen sebelum spec dimulai: File Name `bukti-hapus-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `milik aset DU-030-2` (19 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 20 hari, pukul 09:00` (25 kar), Status `sudah dihapus permanen` (22 kar) · sumber PRD §6 V-11
- **DU-030-3** File (awal), File milik entitas lain: File Name `dokumen-entitas-lain-{runId}.pdf` (32 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Asset ID `milik aset DU-030-3` (19 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 12 hari, pukul 08:45` (25 kar), Entitas `entitas lain, bukan entitas aktor` (33 kar) · sumber PRD §6 V-11
- **DU-031-1** User (awal), Aktor Total Control seluruh group: Name `Tari Pengelola Pusat {runId}` (28 kar), Role `Total Control` (13 kar), Group `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-031-2** File (awal; dimutasi TC-FA-FAFM-E2E-031-gating-total-control), File Asset Photo di group Head Office, dihapus lewat bulk Delete: File Name `foto-printer-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Asset ID `milik aset DU-031-2` (19 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 3 hari, pukul 14:30` (24 kar) · sumber PRD §4.1 Files Example Data
- **DU-031-3** File (awal; dimutasi TC-FA-FAFM-E2E-031-gating-total-control), File Asset Photo di group Branch Bandung, dihapus lewat bulk Delete lalu dihapus permanen: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Asset ID `milik aset DU-031-3` (19 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 5 hari, pukul 08:45` (24 kar) · sumber PRD §4.1 Files Example Data
- **DU-031-4** Asset (awal), Aset Disposed yang tampil di tab Asset Data: Name `Monitor LG 24 {runId}` (21 kar), Asset ID `milik aset DU-031-4` (19 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-032-1** User (awal), Aktor Read Only seluruh group: Name `Rio Pembaca File {runId}` (24 kar), Role `Read Only` (9 kar), Group `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-032-2** File (awal), File Asset Photo di group Head Office, upload lebih baru: File Name `foto-rak-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Rak Arsip {runId}` (17 kar), Asset ID `milik aset DU-032-2` (19 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 3 hari, pukul 14:30` (24 kar) · sumber turunan penulis
- **DU-032-3** File (awal), File Asset Photo di group Branch Bandung, upload lebih lama: File Name `foto-lemari-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Lemari Besi {runId}` (19 kar), Asset ID `milik aset DU-032-3` (19 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 8 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-032-4** File (awal), File yang sudah di Recycle Bin, group Head Office: File Name `foto-bin-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Rak Arsip {runId}` (17 kar), Group `Head Office` (11 kar), Size `450.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 2 hari, pukul 10:00` (24 kar) · sumber turunan penulis
- **DU-032-5** Asset (awal), Aset Disposed yang tampil di tab Asset Data: Name `Monitor LG 24 {runId}` (21 kar), Asset ID `milik aset DU-032-5` (19 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-033-1** User (awal), Group Manager untuk Head Office beserta descendant Fleet: Name `Gita Manajer Group {runId}` (26 kar), Role `Group Manager` (13 kar), Group `Head Office beserta descendant Fleet` (36 kar) · sumber PRD §9.11 Contoh skenario Scope Group Manager
- **DU-033-2** File (awal; dimutasi TC-FA-FAFM-E2E-033-gating-group-manager), File Asset Photo di group yang dikelola (Head Office): File Name `foto-genset-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Genset Cadangan {runId}` (23 kar), Asset ID `milik aset DU-033-2` (19 kar), Group `Head Office` (11 kar), Size `700.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 4 hari, pukul 10:00` (24 kar) · sumber turunan penulis
- **DU-033-3** File (awal; dimutasi TC-FA-FAFM-E2E-033-gating-group-manager), File Asset Photo di group descendant (Fleet), dalam satu tabel dengan group yang dikelola: File Name `foto-forklift-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Forklift Gudang {runId}` (23 kar), Asset ID `milik aset DU-033-3` (19 kar), Group `Fleet` (5 kar), Size `900.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 6 hari, pukul 13:15` (24 kar) · sumber PRD §9.11 Contoh skenario Scope Group Manager
- **DU-033-4** File (awal), File Asset Photo di group di luar scope (Branch Bandung), terlihat aktor dengan scope lain: File Name `foto-ruang-rapat-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Proyektor Ruang Rapat {runId}` (29 kar), Asset ID `milik aset DU-033-4` (19 kar), Group `Branch Bandung` (14 kar), Size `500.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 7 hari, pukul 09:30` (24 kar) · sumber PRD §9.11 Contoh skenario Scope Group Manager
- **DU-033-5** File (awal), File milik entitas lain: File Name `foto-gudang-entitas-lain-{runId}.jpg` (36 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Rak Gudang {runId}` (18 kar), Asset ID `milik aset DU-033-5` (19 kar), Group `Head Office` (11 kar), Size `400.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 9 hari, pukul 11:00` (24 kar), Entitas `entitas lain, bukan entitas aktor` (33 kar) · sumber PRD §9.11 Tidak ada baris lintas client
- **DU-033-6** Asset (awal), Aset Disposed di group descendant yang tampil di tab Asset Data: Name `Truk Box {runId}` (16 kar), Asset ID `milik aset DU-033-6` (19 kar), Group `Fleet` (5 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-034-1** User (awal), Pemegang Manage files Read saja pada group Fleet: Name `Maya Pembaca File {runId}` (25 kar), Role `Pengelola File Fleet Baca {runId}` (33 kar), Capability `Manage files: Read` (18 kar), Group `Fleet` (5 kar) · sumber matriks role PRD
- **DU-034-2** File (awal), File Asset Photo di group yang di-assign (Fleet): File Name `foto-truk-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Truk Pengangkut {runId}` (23 kar), Asset ID `milik aset DU-034-2` (19 kar), Group `Fleet` (5 kar), Size `880.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 2 hari, pukul 15:00` (24 kar) · sumber turunan penulis
- **DU-034-3** File (awal), File Asset Photo di group di luar yang di-assign (Head Office): File Name `foto-kantor-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Meja Kantor {runId}` (19 kar), Asset ID `milik aset DU-034-3` (19 kar), Group `Head Office` (11 kar), Size `600.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 6 hari, pukul 10:30` (24 kar) · sumber PRD §9.11 Contoh skenario Scope Manage files
- **DU-034-4** File (awal), File di Recycle Bin pada group yang di-assign (Fleet): File Name `foto-bin-truk-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Truk Pengangkut {runId}` (23 kar), Group `Fleet` (5 kar), Size `450.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 1 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-034-5** Asset (awal), Aset Disposed di group yang di-assign yang tampil di tab Asset Data: Name `Mobil Operasional {runId}` (25 kar), Asset ID `milik aset DU-034-5` (19 kar), Group `Fleet` (5 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-034-6** Group (awal), Group turunan langsung dari group yang di-assign (Fleet): Name `Fleet Workshop {runId}` (22 kar), Parent Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-034-7** File (awal), File Asset Photo di group turunan dari group yang di-assign: File Name `foto-ban-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Ban Cadangan Truk {runId}` (25 kar), Asset ID `milik aset DU-034-7` (19 kar), Group `Fleet Workshop {runId}` (22 kar), Size `520.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 4 hari, pukul 10:45` (24 kar) · sumber turunan penulis
- **DU-034-8** File (awal), File di Recycle Bin pada group turunan dari group yang di-assign: File Name `foto-bin-bengkel-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Ban Cadangan Truk {runId}` (25 kar), Group `Fleet Workshop {runId}` (22 kar), Size `380.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 2 hari, pukul 13:00` (24 kar) · sumber turunan penulis
- **DU-034-9** Asset (awal), Aset Disposed di group turunan dari group yang di-assign yang tampil di tab Asset Data: Name `Forklift Bengkel {runId}` (24 kar), Asset ID `milik aset DU-034-9` (19 kar), Group `Fleet Workshop {runId}` (22 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-035-1** User (awal), Pemegang Manage files: Delete pada Fleet dan Read pada Head Office (dua assignment): Name `Dani Pengelola Hapus {runId}` (28 kar), Role `Pengelola File Hapus {runId}` (28 kar), Assignment 1 `Manage files: Delete pada Fleet` (31 kar), Assignment 2 `Manage files: Read pada Head Office` (35 kar) · sumber matriks role PRD
- **DU-035-2** File (awal; dimutasi TC-FA-FAFM-E2E-035-gating-manage-files-delete), File Asset Photo di group Delete (Fleet), dihapus oleh spec: File Name `foto-excavator-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Excavator Mini {runId}` (22 kar), Asset ID `milik aset DU-035-2` (19 kar), Group `Fleet` (5 kar), Size `950.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 3 hari, pukul 11:00` (24 kar) · sumber turunan penulis
- **DU-035-3** File (awal), File Asset Photo kedua di group Delete (Fleet): File Name `foto-crane-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Crane Pelabuhan {runId}` (23 kar), Asset ID `milik aset DU-035-3` (19 kar), Group `Fleet` (5 kar), Size `820.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 5 hari, pukul 13:45` (24 kar) · sumber turunan penulis
- **DU-035-4** File (awal), File Asset Photo di group Read saja (Head Office): File Name `foto-printer-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer Kantor {runId}` (22 kar), Asset ID `milik aset DU-035-4` (19 kar), Group `Head Office` (11 kar), Size `410.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 6 hari, pukul 09:20` (24 kar) · sumber PRD §4.8 seleksi campuran pemegang Manage files
- **DU-035-5** File (awal), File Asset Photo di group tanpa assignment (Branch Bandung): File Name `foto-lemari-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Lemari Arsip {runId}` (20 kar), Asset ID `milik aset DU-035-5` (19 kar), Group `Branch Bandung` (14 kar), Size `360.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 7 hari, pukul 15:10` (24 kar) · sumber PRD §9.11 Contoh skenario Scope Manage files
- **DU-035-6** File (awal), File di Recycle Bin pada group Delete (Fleet): File Name `foto-bin-fleet-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Crane Pelabuhan {runId}` (23 kar), Group `Fleet` (5 kar), Size `300.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 1 hari, pukul 08:30` (24 kar), Changelog `aksi Delete` (11 kar) · sumber turunan penulis
- **DU-035-7** File (awal), File di Recycle Bin pada group Read saja (Head Office): File Name `foto-bin-kantor-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Printer Kantor {runId}` (22 kar), Group `Head Office` (11 kar), Size `280.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 1 hari, pukul 08:45` (24 kar) · sumber PRD §4.8 seleksi campuran pemegang Manage files
- **DU-035-8** File (awal), File di Recycle Bin pada group tanpa assignment (Branch Bandung): File Name `foto-bin-lemari-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Lemari Arsip {runId}` (20 kar), Group `Branch Bandung` (14 kar), Size `250.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 2 hari, pukul 10:00` (24 kar), Changelog `aksi Delete` (11 kar) · sumber PRD §9.11 Contoh skenario Scope Manage files
- **DU-035-9** Asset (awal), Aset Disposed di group Fleet yang tampil di tab Asset Data: Name `Pick-up Operasional {runId}` (27 kar), Asset ID `milik aset DU-035-9` (19 kar), Group `Fleet` (5 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-035-10** Group (awal), Group turunan langsung dari group Delete (Fleet): Name `Fleet Workshop {runId}` (22 kar), Parent Group `Fleet` (5 kar) · sumber turunan penulis
- **DU-035-11** File (awal), File Asset Photo di group turunan dari group Delete: File Name `foto-forklift-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Forklift Bengkel {runId}` (24 kar), Asset ID `milik aset DU-035-11` (20 kar), Group `Fleet Workshop {runId}` (22 kar), Size `700.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 4 hari, pukul 10:30` (24 kar) · sumber turunan penulis
- **DU-035-12** File (awal), File di Recycle Bin pada group turunan dari group Delete: File Name `foto-bin-bengkel-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Forklift Bengkel {runId}` (24 kar), Group `Fleet Workshop {runId}` (22 kar), Size `220.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 2 hari, pukul 14:00` (24 kar) · sumber turunan penulis
- **DU-036-1** User (awal), Pemegang Manage files Delete saja pada group Fleet: Name `Eka Penghapus Permanen {runId}` (30 kar), Role `Pengelola File Fleet Hapus {runId}` (34 kar), Capability `Manage files: Delete` (20 kar), Group `Fleet` (5 kar) · sumber matriks role PRD
- **DU-036-2** File (awal; dimutasi TC-FA-FAFM-E2E-036-gating-manage-files-delete-permanently), File di Recycle Bin pada group yang di-assign, dihapus permanen oleh spec: File Name `foto-bin-derek-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Derek Armada {runId}` (20 kar), Group `Fleet` (5 kar), Size `640.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 2 hari, pukul 14:00` (24 kar) · sumber turunan penulis
- **DU-036-3** File (awal), File kedua di Recycle Bin pada group yang di-assign, tetap tampil: File Name `foto-bin-tangki-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Tangki BBM {runId}` (18 kar), Group `Fleet` (5 kar), Size `520.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 3 hari, pukul 16:20` (24 kar) · sumber turunan penulis
- **DU-037-1** User (awal), Pemegang Manage files Read pada Head Office dengan akses Attachments kelompok Purchase: Name `Alya Akses Purchase {runId}` (27 kar), Role `Pembaca File Purchase {runId}` (29 kar), Capability `Manage files: Read` (18 kar), Group `Head Office` (11 kar), Akses Attachments Purchase `Ya` (2 kar) · sumber PRD §9.11 File kelompok Purchase
- **DU-037-2** User (awal), Pemegang Manage files Read pada Head Office tanpa akses Attachments kelompok Purchase: Name `Bima Tanpa Purchase {runId}` (27 kar), Role `Pembaca File Non-Purchase {runId}` (33 kar), Capability `Manage files: Read` (18 kar), Group `Head Office` (11 kar), Akses Attachments Purchase `Tidak` (5 kar) · sumber PRD §9.11 File kelompok Purchase
- **DU-037-3** File (awal), File Attachment kelompok Purchase di Head Office, terlihat hanya oleh role berhak: File Name `invoice-forklift-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Forklift Gudang {runId}` (23 kar), Asset ID `milik aset DU-037-3` (19 kar), Group `Head Office` (11 kar), Size `420.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `T0 − 3 hari, pukul 10:15` (24 kar) · sumber PRD §9.11 File kelompok Purchase
- **DU-037-4** File (awal), File Attachment kelompok General di Head Office, terlihat kedua aktor: File Name `warranty-forklift-{runId}.pdf` (29 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Gudang {runId}` (23 kar), Asset ID `milik aset DU-037-4` (19 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `T0 − 5 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-037-5** File (awal), File Attachment kelompok Purchase di group di luar scope kedua aktor: File Name `invoice-bandung-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Genset Bandung {runId}` (22 kar), Asset ID `milik aset DU-037-5` (19 kar), Group `Branch Bandung` (14 kar), Size `380.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `T0 − 4 hari, pukul 14:00` (24 kar) · sumber turunan penulis
- **DU-037-6** File (awal), File Attachment kelompok Purchase di Recycle Bin dengan entri Changelog: File Name `invoice-lama-{runId}.pdf` (24 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Forklift Gudang {runId}` (23 kar), Group `Head Office` (11 kar), Size `260.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 1 hari, pukul 09:00` (24 kar), Changelog `aksi Delete` (11 kar) · sumber turunan penulis
- **DU-037-7** File (awal), File Attachment kelompok General di Recycle Bin dengan entri Changelog: File Name `warranty-lama-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Forklift Gudang {runId}` (23 kar), Group `Head Office` (11 kar), Size `150.0 KB` (8 kar), Deleted By `Rina A` (6 kar), Deleted Date `T0 − 1 hari, pukul 09:30` (24 kar), Changelog `aksi Delete` (11 kar) · sumber turunan penulis
- **DU-038-1** Asset (awal), Aset Active pemilik foto dan dokumen: Asset Name `Laptop Dell Latitude {runId}` (28 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber T-FAFM-01
- **DU-038-2** File (awal), Foto aset pada Kategori Asset Photo: File Name `laptop-front-{runId}.jpg` (24 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Size `820.4 KB` (8 kar), Ukuran mentah `840090 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber T-FAFM-01
- **DU-038-3** File (awal), Dokumen Attachment pada Kategori Asset Documents: File Name `warranty-card-{runId}.pdf` (25 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `310.0 KB` (8 kar), Ukuran mentah `317440 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber T-FAFM-01
- **DU-038-4** Asset (awal), Aset Disposed dengan dokumen Disposal: Asset Name `Printer HP M404 {runId}` (23 kar), Status `Disposed` (8 kar), Group `Fleet` (5 kar), Data & Log Size `50.0 KB` (7 kar), Files Size `3.2 MB` (6 kar) · sumber T-FAFM-02
- **DU-038-5** File (awal), Dokumen lelang pada Kategori Disposal: File Name `dsp-auction-receipt-{runId}.pdf` (31 kar), Source `Disposal Document` (17 kar), Category `Disposal` (8 kar), Size `3.2 MB` (6 kar), Ukuran mentah `3355443 byte` (12 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber T-FAFM-01
- **DU-038-6** Asset (awal), Aset Unmanaged tanpa file: Asset Name `Monitor LG 24 {runId}` (21 kar), Status `Unmanaged` (9 kar), Group `Fleet` (5 kar), Data & Log Size `50.0 KB` (7 kar), Files Size `0.0 KB` (6 kar) · sumber T-FAFM-02
- **DU-038-7** File (awal), Foto Found Photo pada Kategori Missing: File Name `found-photo-{runId}.jpg` (23 kar), Source `Found Photo` (11 kar), Category `Missing` (7 kar), Size `45.0 KB` (7 kar), Ukuran mentah `46080 byte` (10 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber §4.6#p2
- **DU-039-1** Asset (awal), Aset Active pemilik dokumen Attachment: Asset Name `Laptop Dell Latitude {runId}` (28 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber §4.6#p3
- **DU-039-2** File (awal), Dokumen Attachment untuk Bulk Download ZIP: File Name `warranty-card-{runId}.pdf` (25 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `310.0 KB` (8 kar), Ukuran mentah `317440 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber §4.6#p3
- **DU-039-3** File (awal), Dokumen Attachment kedua untuk Bulk Download ZIP: File Name `service-manual-{runId}.pdf` (26 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `1.2 MB` (6 kar), Ukuran mentah `1258291 byte` (12 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber §4.6#p3
- **DU-039-4** File (awal; dimutasi TC-FA-FAFM-E2E-039-android-selection-mode-bulk-download), Dokumen Attachment pertama untuk Bulk Delete: File Name `insurance-letter-{runId}.pdf` (28 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `450.2 KB` (8 kar), Ukuran mentah `461005 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber §4.6#p3
- **DU-039-5** File (awal; dimutasi TC-FA-FAFM-E2E-039-android-selection-mode-bulk-download), Dokumen Attachment kedua untuk Bulk Delete: File Name `handover-note-{runId}.pdf` (25 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `120.0 KB` (8 kar), Ukuran mentah `122880 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber §4.6#p3
- **DU-039-6** Asset (awal), Aset Disposed untuk tab tanpa selection mode: Asset Name `Printer HP M404 {runId}` (23 kar), Status `Disposed` (8 kar), Group `Fleet` (5 kar) · sumber §4.6#p3
- **DU-040-1** Asset (awal), Aset pemilik foto yang diganti: Asset Name `Laptop Dell Latitude {runId}` (28 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber T-FAFM-03
- **DU-040-2** RecycleBinFile (awal), Foto aset yang diganti, dihapus 2 hari lalu: File Name `laptop-old-{runId}.png` (22 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar), Size `1.0 MB` (6 kar), Ukuran mentah `1048576 byte` (12 kar), Deleted Date `T0 − 2 hari` (11 kar), Deleted By `System` (6 kar), Auto-Purge In `28 days` (7 kar) · sumber T-FAFM-03
- **DU-040-3** Asset (awal), Aset pemilik foto kerusakan dan perbaikan: Asset Name `Toyota Avanza {runId}` (21 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber T-FAFM-03
- **DU-040-4** RecycleBinFile (awal), Foto kerusakan, dihapus 5 hari lalu: File Name `damage-01-{runId}.jpg` (21 kar), Source `Damaged Photo` (13 kar), Category `Damaged` (7 kar), Asset `Toyota Avanza {runId}` (21 kar), Size `900.0 KB` (8 kar), Ukuran mentah `921600 byte` (11 kar), Deleted Date `T0 − 5 hari` (11 kar), Deleted By `System` (6 kar), Auto-Purge In `25 days` (7 kar) · sumber T-FAFM-03
- **DU-040-5** RecycleBinFile (awal), Foto perbaikan, dihapus 28 hari lalu: File Name `repair-02-{runId}.jpg` (21 kar), Source `Repair Photo` (12 kar), Category `Damaged` (7 kar), Asset `Toyota Avanza {runId}` (21 kar), Size `880.0 KB` (8 kar), Ukuran mentah `901120 byte` (11 kar), Deleted Date `T0 − 28 hari` (12 kar), Deleted By `System` (6 kar), Auto-Purge In `2 days` (6 kar) · sumber T-FAFM-03
- **DU-040-6** Asset (awal), Aset pemilik foto maintenance: Asset Name `Printer HP M404 {runId}` (23 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber T-FAFM-03
- **DU-040-7** RecycleBinFile (awal), Foto maintenance, dihapus 29 hari lalu: File Name `maint-before-{runId}.jpg` (24 kar), Source `Maintenance Before Photo` (24 kar), Category `Maintenance` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Size `750.0 KB` (8 kar), Ukuran mentah `768000 byte` (11 kar), Deleted Date `T0 − 29 hari` (12 kar), Deleted By `System` (6 kar), Auto-Purge In `1 day` (5 kar) · sumber T-FAFM-03
- **DU-041-1** Asset (awal), Aset pemilik foto kerusakan dan perbaikan: Asset Name `Toyota Avanza {runId}` (21 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber T-FAFM-04
- **DU-041-2** File (awal; dimutasi TC-FA-FAFM-E2E-041-android-changelog-bottom-sheet), Foto kerusakan yang di-Delete lalu di-Permanently Delete: File Name `damage-01-{runId}.jpg` (21 kar), Source `Damaged Photo` (13 kar), Category `Damaged` (7 kar), Size `900.0 KB` (8 kar), Ukuran mentah `921600 byte` (11 kar), Asset `Toyota Avanza {runId}` (21 kar) · sumber T-FAFM-04
- **DU-041-3** File (awal; dimutasi TC-FA-FAFM-E2E-041-android-changelog-bottom-sheet), Foto perbaikan yang di-Delete: File Name `repair-02-{runId}.jpg` (21 kar), Source `Repair Photo` (12 kar), Category `Damaged` (7 kar), Size `880.0 KB` (8 kar), Ukuran mentah `901120 byte` (11 kar), Asset `Toyota Avanza {runId}` (21 kar) · sumber T-FAFM-04
- **DU-042-1** Asset (awal), Aset pemilik file preview: Asset Name `Laptop Dell Latitude {runId}` (28 kar), Status `Active` (6 kar), Group `Fleet` (5 kar) · sumber PRV-08
- **DU-042-2** File (awal), Gambar JPG dengan Dimensions terbaca: File Name `laptop-front-{runId}.jpg` (24 kar), Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Size `820.4 KB` (8 kar), Ukuran mentah `840090 byte` (11 kar), Dimensions `1600 × 1200 px` (14 kar), Uploaded By `System` (6 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber PRV-08
- **DU-042-3** File (awal), Dokumen PDF tanpa Dimensions: File Name `warranty-card-{runId}.pdf` (25 kar), Format `PDF` (3 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `310.0 KB` (8 kar), Ukuran mentah `317440 byte` (11 kar), Uploaded By `System` (6 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber PRV-08
- **DU-042-4** File (awal), Gambar JPG yang gagal dimuat: File Name `corrupt-photo-{runId}.jpg` (25 kar), Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Size `100.0 KB` (8 kar), Ukuran mentah `102400 byte` (11 kar), Dimensions `—` (1 kar), Uploaded By `System` (6 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber PRV-09
- **DU-042-5** File (awal; dimutasi TC-FA-FAFM-E2E-042-android-file-preview-bottom-sheet), Gambar yang dihapus permanen aktor pemicu sebelum Preview: File Name `old-label-{runId}.png` (21 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Size `1.0 MB` (6 kar), Ukuran mentah `1048576 byte` (12 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber S-12
- **DU-042-6** File (awal; dimutasi TC-FA-FAFM-E2E-042-android-file-preview-bottom-sheet), Dokumen yang dihapus permanen aktor pemicu sebelum Download: File Name `old-invoice-{runId}.pdf` (23 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Size `450.2 KB` (8 kar), Ukuran mentah `461005 byte` (11 kar), Asset `Laptop Dell Latitude {runId}` (28 kar) · sumber V-01
- **DU-043-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-043-delete-asset-data-dep-asset-list), Aset Disposed dengan file aktif dan file di Recycle Bin: Asset Name `Printer HP M404 {runId}` (23 kar), Status `Disposed` (8 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-043-2** File (awal; dimutasi TC-FA-FAFM-E2E-043-delete-asset-data-dep-asset-list), File Disposal Document aktif milik aset DU-043-1: File Name `dsp-receipt-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Category `Disposal` (8 kar), Asset `Printer HP M404 {runId}` (23 kar), Size `3.2 MB` (6 kar) · sumber PRD §4.1 Example Data
- **DU-043-3** File (awal; dimutasi TC-FA-FAFM-E2E-043-delete-asset-data-dep-asset-list), File Maintenance After Photo aktif milik aset DU-043-1: File Name `maint-after-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Maintenance After Photo` (23 kar), Category `Maintenance` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Size `1.9 MB` (6 kar) · sumber PRD §4.1 Example Data
- **DU-043-4** File (awal; dimutasi TC-FA-FAFM-E2E-043-delete-asset-data-dep-asset-list), File Maintenance Before Photo di Recycle Bin milik aset DU-043-1: File Name `maint-before-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Category `Maintenance` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Size `700.0 KB` (8 kar) · sumber PRD §4.1 Example Data
- **DU-044-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration), Aset Active hasil registrasi dari Draft, dipindah ke group lain sesudah Draft, fotonya akan di-Delete: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Status `Active` (6 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-044-2** File (awal; dimutasi TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration), Foto aktif aset DU-044-1 yang diunggah di field Photo registrasi: File Name `laptop-front-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.1 Example Data
- **DU-044-3** File (awal), Foto lama yang diganti saat aset masih Draft, di Recycle Bin dengan snapshot: File Name `laptop-old-{runId}.png` (22 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `—` (1 kar), Group `Head Office` (11 kar), Deleted By `System` (6 kar) · sumber PRD §4.1 Example Data
- **DU-044-4** Asset (awal; dimutasi TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration), Aset Draft yang akan dihapus: Asset Name `Printer Epson L3250 {runId}` (27 kar), Status `Draft` (5 kar), Group `Head Office` (11 kar) · sumber PRD §9.2 F-FAFM-01g
- **DU-044-5** File (awal; dimutasi TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration), Foto registrasi aktif aset Draft, tidak didaftar di tab Files: File Name `draft-photo-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Printer Epson L3250 {runId}` (27 kar), Size `2.4 MB` (6 kar) · sumber PRD §9.2 F-FAFM-01g
- **DU-044-6** File (awal; dimutasi TC-FA-FAFM-E2E-044-draft-asset-dep-asset-registration), Foto lama aset Draft di Recycle Bin dengan snapshot, ikut cascade purge: File Name `draft-old-{runId}.png` (21 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `—` (1 kar), Group `Head Office` (11 kar), Deleted By `System` (6 kar), Size `1.1 MB` (6 kar) · sumber PRD §9.2 F-FAFM-01i
- **DU-044-7** User (awal), Group Manager yang mengelola group snapshot Recycle Bin: Name `Manajer Pusat {runId}` (21 kar), Role `Group Manager` (13 kar), Group `Head Office` (11 kar) · sumber matriks role PRD
- **DU-044-8** User (awal), Group Manager yang hanya mengelola group aset saat ini: Name `Manajer Bandung {runId}` (23 kar), Role `Group Manager` (13 kar), Group `Branch Bandung` (14 kar) · sumber matriks role PRD
- **DU-045-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail), Aset Active yang fotonya diganti lalu dikosongkan: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Status `Active` (6 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-045-2** File (awal; dimutasi TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail), Foto aktif lama aset DU-045-1: File Name `laptop-old-{runId}.png` (22 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.1 Example Data
- **DU-045-3** File (dibuat; dimutasi TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail), Foto pengganti yang dipilih di Change photo: File Name `laptop-front-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.1 Example Data
- **DU-045-4** File (dibuat), Dokumen Attachment section General: File Name `warranty-card-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Category `Asset Documents` (15 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.2d Source & Titik Upload
- **DU-045-5** File (dibuat), Dokumen Attachment section Purchase: File Name `invoice-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Category `Asset Documents` (15 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.2d Source & Titik Upload
- **DU-045-6** Asset (awal; dimutasi TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail), Aset Active yang fotonya di-Remove: Asset Name `Scanner Epson DS-530 {runId}` (28 kar), Status `Active` (6 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-045-7** File (awal; dimutasi TC-FA-FAFM-E2E-045-change-photo-attachment-dep-asset-detail), Foto aktif aset DU-045-6 yang akan di-Remove: File Name `scanner-photo-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Category `Asset Photo` (11 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber PRD §4.1 Example Data
- **DU-046-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-046-custom-field-document-dep-custom-fields), Aset Active dengan dua nilai Custom Field Document: Asset Name `Scanner Epson DS-530 {runId}` (28 kar), Status `Active` (6 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-046-2** File (awal; dimutasi TC-FA-FAFM-E2E-046-custom-field-document-dep-custom-fields), Nilai Custom Field Document Warranty Card yang akan di-Delete lewat File Manager: File Name `warranty-card-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card {runId}` (21 kar), Category `Asset Documents` (15 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber PRD §4.1 Example Data
- **DU-046-3** File (awal; dimutasi TC-FA-FAFM-E2E-046-custom-field-document-dep-custom-fields), Nilai Custom Field Document Service Manual yang ikut terhapus bersama definisi field: File Name `service-manual-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Service Manual {runId}` (22 kar), Category `Asset Documents` (15 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber FAFM-LOGIC-07h
- **DU-046-4** File (awal; dimutasi TC-FA-FAFM-E2E-046-custom-field-document-dep-custom-fields), Nilai Custom Field Document Insurance Certificate yang ikut di-soft-delete saat tipe definisi field diganti: File Name `insurance-certificate-{runId}.pdf` (33 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Insurance Certificate {runId}` (29 kar), Category `Asset Documents` (15 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber FAFM-LOGIC-07h
- **DU-047-1** Asset (awal), Aset dengan record Damaged yang sudah Repaired: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar) · sumber PRD §4.1 Example Data
- **DU-047-2** Damaged (awal; dimutasi TC-FA-FAFM-E2E-047-damaged-photo-dep-damaged), Record Damaged yang sudah ada sebelum Delete, dengan Damaged Photo dan Repair Photo terisi: Asset Name `Toyota Avanza {runId}` (21 kar), Damaged Photo `damage-{runId}.jpg` (18 kar), Repair Photo `repair-{runId}.jpg` (18 kar) · sumber PRD §9.2 Contoh skenario Hapus bukti
- **DU-047-3** File (awal; dimutasi TC-FA-FAFM-E2E-047-damaged-photo-dep-damaged), Damaged Photo yang dirujuk record Damaged dan di-Delete lewat File Manager: File Name `damage-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Damaged Photo` (13 kar), Category `Damaged` (7 kar), Asset `Toyota Avanza {runId}` (21 kar), Size `900.0 KB` (8 kar), Reference `ID record Damaged milik DU-047-2` (32 kar) · sumber PRD §9.2 Contoh skenario Hapus bukti
- **DU-047-4** File (awal), Repair Photo yang tetap dirujuk record Damaged sebagai pembanding: File Name `repair-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Repair Photo` (12 kar), Category `Damaged` (7 kar), Asset `Toyota Avanza {runId}` (21 kar), Size `880.0 KB` (8 kar), Reference `ID record Damaged milik DU-047-2` (32 kar) · sumber PRD §4.1 Example Data
- **DU-048-1** Asset (awal), Aset dengan record Missing yang sudah Found: Asset Name `MacBook Pro 14 {runId}` (22 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-048-2** Missing (awal; dimutasi TC-FA-FAFM-E2E-048-found-photo-dep-missing), Record Missing dengan Found Photo terisi: Asset Name `MacBook Pro 14 {runId}` (22 kar), Found Photo `found-{runId}.jpg` (17 kar) · sumber PRD §4.2d SRC-07
- **DU-048-3** File (awal; dimutasi TC-FA-FAFM-E2E-048-found-photo-dep-missing), Found Photo yang dirujuk record Missing dan di-Delete lewat File Manager: File Name `found-{runId}.jpg` (17 kar), File Format `JPG` (3 kar), Source `Found Photo` (11 kar), Category `Missing` (7 kar), Asset `MacBook Pro 14 {runId}` (22 kar), Reference `ID record Missing milik DU-048-2` (32 kar) · sumber PRD §4.2d SRC-07
- **DU-049-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-049-maintenance-photo-dep-maintenance-routine), Aset dengan task maintenance yang memuat Before photo dan After photo: Asset Name `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-049-2** File (awal; dimutasi TC-FA-FAFM-E2E-049-maintenance-photo-dep-maintenance-routine), Before photo task yang di-Delete lewat File Manager: File Name `maint-before-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Category `Maintenance` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Reference `ID task milik aset DU-049-1` (27 kar) · sumber PRD §4.1 Example Data
- **DU-049-3** File (awal), After photo task yang tetap dirujuk sebagai pembanding: File Name `maint-after-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Maintenance After Photo` (23 kar), Category `Maintenance` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Reference `ID task milik aset DU-049-1` (27 kar) · sumber PRD §4.1 Example Data
- **DU-050-1** Asset (awal), Aset Active dengan transaksi Disposal yang belum Execute: Asset Name `Printer HP M404 {runId}` (23 kar), Status `Active` (6 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-050-2** Disposal (awal; dimutasi TC-FA-FAFM-E2E-050-disposal-document-dep-disposal), Transaksi Disposal sebelum Execute dengan Disposal Document terisi: Asset Name `Printer HP M404 {runId}` (23 kar), Disposal Document `dsp-pending-{runId}.pdf` (23 kar) · sumber PRD §9.4.1 DIM-14d
- **DU-050-3** File (awal; dimutasi TC-FA-FAFM-E2E-050-disposal-document-dep-disposal), Disposal Document transaksi yang belum Execute, di-Delete lewat File Manager: File Name `dsp-pending-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Category `Disposal` (8 kar), Asset `Printer HP M404 {runId}` (23 kar), Reference `ID transaksi milik DU-050-2` (27 kar) · sumber PRD §4.2d SRC-10
- **DU-050-4** Asset (awal; dimutasi TC-FA-FAFM-E2E-050-disposal-document-dep-disposal), Aset Active dengan transaksi Disposal siap Execute: Asset Name `Monitor LG 24 {runId}` (21 kar), Status `Active` (6 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-050-5** File (dibuat), Disposal Document yang dipilih di halaman Execute: File Name `dsp-auction-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Category `Disposal` (8 kar), Asset `Monitor LG 24 {runId}` (21 kar), Reference `ID transaksi Disposal milik aset DU-050-4` (41 kar) · sumber PRD §4.2d SRC-10
- **DU-051-1** Asset (awal), Aset dengan transaksi Borrow yang belum Return: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-051-2** Borrow (awal; dimutasi TC-FA-FAFM-E2E-051-borrow-photo-dep-borrow), Transaksi Borrow sebelum Return dengan Handover Photo terisi: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Handover Photo `handover-{runId}.jpg` (20 kar) · sumber PRD §9.4.1 DIM-14d
- **DU-051-3** File (awal; dimutasi TC-FA-FAFM-E2E-051-borrow-photo-dep-borrow), Handover Photo transaksi yang belum Return, di-Delete lewat File Manager: File Name `handover-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Category `Borrow` (6 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Reference `ID transaksi milik DU-051-2` (27 kar) · sumber PRD §4.1 Example Data
- **DU-051-4** Asset (awal), Aset dengan transaksi Borrow yang sudah Return: Asset Name `Camera Canon EOS R6 {runId}` (27 kar), Group `Head Office` (11 kar) · sumber PRD §4.2d SRC-12
- **DU-051-5** File (awal), Return Photo transaksi Borrow yang sudah Return: File Name `return-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Return Photo` (12 kar), Category `Borrow` (6 kar), Asset `Camera Canon EOS R6 {runId}` (27 kar), Reference `ID transaksi Borrow milik aset DU-051-4` (39 kar) · sumber PRD §4.2d SRC-12
- **DU-052-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-052-assignment-photo-dep-assignment), Aset dengan transaksi Assignment yang memuat Handover Photo dan Return Photo: Asset Name `Projector Epson EB-X49 {runId}` (30 kar), Group `Head Office` (11 kar) · sumber PRD §4.2d SRC-11
- **DU-052-2** File (awal), Handover Photo transaksi Assignment yang tetap dirujuk sebagai pembanding: File Name `asg-handover-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Category `Assignment` (10 kar), Asset `Projector Epson EB-X49 {runId}` (30 kar), Reference `ID transaksi Assignment milik aset DU-052-1` (43 kar) · sumber PRD §4.2d SRC-11
- **DU-052-3** File (awal; dimutasi TC-FA-FAFM-E2E-052-assignment-photo-dep-assignment), Return Photo transaksi Assignment yang di-Delete lewat File Manager: File Name `asg-return-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Return Photo` (12 kar), Category `Assignment` (10 kar), Asset `Projector Epson EB-X49 {runId}` (30 kar), Reference `ID transaksi Assignment milik aset DU-052-1` (43 kar) · sumber PRD §4.2d SRC-12
- **DU-053-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Aset yang dipindah ke group Fleet (tetap dalam scope aktor): Asset Name `Server Dell R750 {runId}` (24 kar), Group `Head Office` (11 kar) · sumber PRD §9.11 Contoh skenario
- **DU-053-2** Asset (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Aset yang dipindah ke group Branch Bandung (keluar dari scope aktor): Asset Name `Printer Zebra ZT230 {runId}` (27 kar), Group `Head Office` (11 kar) · sumber PRD §9.11 Contoh skenario
- **DU-053-3** Transfer (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Transaksi Transfer yang sudah Send ke Fleet dan belum selesai: Asset Name `Server Dell R750 {runId}` (24 kar), Group Tujuan `Fleet` (5 kar), Send Photo `send-x-{runId}.jpg` (18 kar) · sumber PRD §4.2d SRC-13
- **DU-053-4** Transfer (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Transaksi Transfer yang sudah Send ke Branch Bandung dan belum selesai: Asset Name `Printer Zebra ZT230 {runId}` (27 kar), Group Tujuan `Branch Bandung` (14 kar), Send Photo `send-y-{runId}.jpg` (18 kar) · sumber PRD §4.2d SRC-13
- **DU-053-5** File (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Send Photo transaksi ke Fleet; group baris ikut berubah, lalu di-Delete: File Name `send-x-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Send Photo` (10 kar), Category `Transfer` (8 kar), Asset `Server Dell R750 {runId}` (24 kar), Group `Head Office` (11 kar), Reference `ID transaksi Transfer milik DU-053-3` (36 kar) · sumber PRD §4.2d SRC-13
- **DU-053-6** File (awal; dimutasi TC-FA-FAFM-E2E-053-transfer-photo-dep-transfer), Send Photo transaksi ke Branch Bandung; keluar dari scope aktor setelah Transfer: File Name `send-y-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Send Photo` (10 kar), Category `Transfer` (8 kar), Asset `Printer Zebra ZT230 {runId}` (27 kar), Group `Head Office` (11 kar), Reference `ID transaksi Transfer milik DU-053-4` (36 kar) · sumber PRD §9.4.2 EC-14
- **DU-053-7** File (dibuat), Receive Photo transaksi ke Fleet: File Name `recv-x-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Receive Photo` (13 kar), Category `Transfer` (8 kar), Asset `Server Dell R750 {runId}` (24 kar), Group `Fleet` (5 kar), Reference `ID transaksi Transfer milik DU-053-3` (36 kar) · sumber PRD §4.2d SRC-14
- **DU-053-8** File (dibuat), Receive Photo transaksi ke Branch Bandung: File Name `recv-y-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Receive Photo` (13 kar), Category `Transfer` (8 kar), Asset `Printer Zebra ZT230 {runId}` (27 kar), Group `Branch Bandung` (14 kar), Reference `ID transaksi Transfer milik DU-053-4` (36 kar) · sumber PRD §4.2d SRC-14
- **DU-054-1** Asset (awal; dimutasi TC-FA-FAFM-E2E-054-status-unmanaged-dep-license), Aset Active yang status lisensinya diubah menjadi Unmanaged lalu kembali Active: Asset Name `Scanner Epson DS-530 {runId}` (28 kar), Status `Active` (6 kar), Group `Branch Bandung` (14 kar) · sumber PRD §4.1 Example Data
- **DU-054-2** File (awal), File aktif aset DU-054-1 yang tetap ada selama aset Unmanaged: File Name `unmanaged-scan-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber PRD §9.2 EC-18
- **DU-054-3** Asset (awal), Aset yang sudah Unmanaged sebagai pembanding baris tab Asset Data: Asset Name `Monitor LG 24 {runId}` (21 kar), Status `Unmanaged` (9 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-055-1** Setting (awal; dimutasi TC-FA-FAFM-E2E-055-retensi-recycle-bin-dep-lifecycle-settings), Durasi retensi Recycle Bin pada nilai awal: Durasi retensi Recycle Bin `30 hari` (7 kar) · sumber foundation recycle-bin pattern: permanently_delete_days default 30 hari (ACRB-05)
- **DU-055-2** Setting (dibuat), Durasi retensi Recycle Bin pengganti yang disimpan di Lifecycle Settings: Durasi retensi Recycle Bin `45 hari` (7 kar), Auto-Purge In `45 days` (7 kar) · sumber turunan penulis
- **DU-055-3** Asset (awal), Aset pemilik dua file yang di-Delete sebelum dan sesudah perubahan retensi: Asset Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-055-4** File (awal; dimutasi TC-FA-FAFM-E2E-055-retensi-recycle-bin-dep-lifecycle-settings), File yang di-Delete sebelum durasi retensi diubah: File Name `retensi-before-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber PRD §4.2 Recycle Bin
- **DU-055-5** File (awal; dimutasi TC-FA-FAFM-E2E-055-retensi-recycle-bin-dep-lifecycle-settings), File yang di-Delete sesudah durasi retensi diubah: File Name `retensi-after-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber PRD §4.2 Recycle Bin
- **DU-056-1** Entitas (awal; dimutasi TC-FA-FAFM-E2E-056-kuota-dan-laporan-dep-global-settings), Entitas khusus dengan Storage penuh (Total Used di atas kuota): Entity Name `Entitas Storage {runId}` (23 kar), Total Used `50.4 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `48.8 GB` (7 kar) · sumber PRD §4.2c Example Data
- **DU-056-2** Top-up Storage (dibuat), Top-up kuota Storage entitas khusus: Top-up `25.0 GB` (7 kar), Storage Quota `75.0 GB` (7 kar), Progress `67%` (3 kar) · sumber turunan penulis
- **DU-056-3** Asset (awal), Aset pemilik file di entitas khusus: Asset Name `Forklift Gudang {runId}` (23 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-056-4** File (awal; dimutasi TC-FA-FAFM-E2E-056-kuota-dan-laporan-dep-global-settings), File di Recycle Bin yang dihapus permanen sesudah laporan terakhir: File Name `arsip-recycle-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Forklift Gudang {runId}` (23 kar), Size `2.0 GB` (6 kar) · sumber turunan penulis
- **DU-056-5** File (awal; dimutasi TC-FA-FAFM-E2E-056-kuota-dan-laporan-dep-global-settings), File aktif yang di-Delete sesudah laporan terakhir: File Name `aktif-delete-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Forklift Gudang {runId}` (23 kar), Size `1.0 GB` (6 kar) · sumber turunan penulis
- **DU-057-1** Setting (awal; dimutasi TC-FA-FAFM-E2E-057-format-tanggal-dep-general-settings), Date Format dan Time Format General Settings pada nilai awal: Date Format `dd/MM/yy` (8 kar), Time Format `24 jam` (6 kar) · sumber PRD §4.1 INV-11d
- **DU-057-2** Setting (dibuat), Date Format opsi M/d/yy: Date Format `M/d/yy` (6 kar) · sumber foundation prd-conventions §32
- **DU-057-3** Setting (dibuat), Date Format opsi dd MMM yy: Date Format `dd MMM yy` (9 kar) · sumber foundation prd-conventions §32
- **DU-057-4** Setting (dibuat), Date Format opsi DDD, MMM dd, yy: Date Format `DDD, MMM dd, yy` (15 kar) · sumber foundation prd-conventions §32
- **DU-057-5** Setting (dibuat), Date Format opsi DDD, MMM dd, yyyy: Date Format `DDD, MMM dd, yyyy` (17 kar) · sumber foundation prd-conventions §32
- **DU-057-6** Setting (dibuat), Time Format 12 jam: Time Format `12 jam` (6 kar) · sumber foundation prd-conventions §32
- **DU-057-7** Asset (awal), Aset pemilik file uji format tanggal: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-057-8** File (awal), Foto aset yang Upload Date-nya dibaca di tiap format: File Name `format-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §4.1 Example Data
- **DU-057-9** Setting (dibuat), Time Zone pengganti satu jam lebih maju dari Time Zone awal: Time Zone `awal ditambah satu jam` (22 kar) · sumber turunan penulis
- **DU-057-10** File (awal; dimutasi TC-FA-FAFM-E2E-057-format-tanggal-dep-general-settings), File yang di-Delete untuk membaca Deleted Date dan Date Changelog: File Name `format-hapus-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber turunan penulis
- **DU-057-11** Asset (awal), Aset Unmanaged untuk membaca Register Date di tab Asset Data: Asset Name `Camera Canon EOS R6 {runId}` (27 kar), Status `Unmanaged` (9 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-058-1** Asset (awal), Aset dengan foto yang di-Delete satu per satu: Asset Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-058-2** File (awal; dimutasi TC-FA-FAFM-E2E-058-log-modul-sumber-dep-activity-log), Foto aset yang dirujuk record sumber dan di-Delete single: File Name `log-single-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber PRD §8.1 Delta modul ini
- **DU-058-3** Asset (awal), Aset pemilik foto bulk pertama: Asset Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-058-4** File (awal; dimutasi TC-FA-FAFM-E2E-058-log-modul-sumber-dep-activity-log), Foto bulk pertama yang di-Delete lalu di-Permanently Delete bulk: File Name `log-bulk-a-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Monitor LG 24 {runId}` (21 kar) · sumber PRD §8.3
- **DU-058-5** Asset (awal), Aset pemilik foto bulk kedua: Asset Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-058-6** File (awal; dimutasi TC-FA-FAFM-E2E-058-log-modul-sumber-dep-activity-log), Foto bulk kedua yang di-Delete lalu di-Permanently Delete bulk: File Name `log-bulk-b-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar) · sumber PRD §8.3
- **DU-058-7** File (awal), File yang sudah dihapus permanen oleh auto-purge: File Name `log-purge-{runId}.png` (21 kar), File Format `PNG` (3 kar), Modified By `System` (6 kar) · sumber PRD §12 OI-01
- **DU-059-1** Asset (awal), Aset pemilik foto, dokumen, dan servis dengan lampiran: Asset Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-059-2** File (awal; dimutasi TC-FA-FAFM-E2E-059-lampiran-servis-dep-service-center), Foto aset pembanding; di-Delete agar Recycle Bin memuat satu baris: File Name `servis-foto-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber PRD §4.1 Example Data
- **DU-059-3** File (awal), Dokumen aset Attachment pembanding di tab Asset Documents: File Name `servis-dokumen-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Category `Asset Documents` (15 kar), Asset `Printer HP M404 {runId}` (23 kar) · sumber PRD §4.1 Example Data
- **DU-059-4** Lampiran Service Center (awal; dimutasi TC-FA-FAFM-E2E-059-lampiran-servis-dep-service-center), Lampiran servis yang tidak melekat pada aset: File Name `servis-lampiran-{runId}.pdf` (27 kar), File Format `PDF` (3 kar) · sumber PRD §4.2d
- **DU-059-5** Lampiran Service Center (dibuat), Lampiran servis yang diunggah di dalam spec untuk membaca dampaknya pada angka Fixed Asset: File Name `servis-hitung-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Size `3.0 MB` (6 kar) · sumber turunan penulis
- **DU-093-1** Asset (awal), Aset pemilik foto yang di-Delete lalu di-Permanently Delete aktor: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar) · sumber PRD §4.1 Example Data
- **DU-093-2** File (awal; dimutasi TC-FA-FAFM-E2E-093-system-log-aktor-dep-user), Foto aset yang di-Delete dan di-Permanently Delete manual oleh aktor: File Name `syslog-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber PRD §8.2
- **DU-093-3** File (awal), File yang sudah dihapus permanen oleh auto-purge ber-aktor System: File Name `syslog-purge-{runId}.png` (24 kar), File Format `PNG` (3 kar), Modified By `System` (6 kar) · sumber PRD §12 OI-01
- **DU-060-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-060-2** User (awal), Aktor Read Only: Name `Sari Wulandari {runId}` (22 kar), Role `Read Only` (9 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-060-3** User (awal), Pemegang Manage files Read di satu group dan Delete di group lain: Name `Rahmat Hidayat {runId}` (22 kar), Role `Manage files` (12 kar), Cakupan Read `Branch Bandung beserta descendant` (33 kar), Cakupan Delete `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-060-4** User (awal), Pemegang Manage files Read saja: Name `Wulan Anggraini {runId}` (23 kar), Role `Manage files` (12 kar), Cakupan Read `Branch Bandung beserta descendant` (33 kar), Cakupan Delete `tidak ada` (9 kar) · sumber matriks role PRD
- **DU-060-5** Aset (awal), Aset group Head Office dengan foto aktif dan file di Recycle Bin: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-060-8` (14 kar) · sumber turunan penulis
- **DU-060-6** Aset (awal), Aset group Branch Bandung dengan foto aktif dan file di Recycle Bin: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar), Photo `milik DU-060-9` (14 kar) · sumber turunan penulis
- **DU-060-7** Aset (awal; dimutasi TC-FA-FAFM-BE-060-authz-per-role-sisi-server), Aset group Head Office dengan foto yang akan di-Delete: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-060-12` (15 kar) · sumber turunan penulis
- **DU-060-8** File (awal), File aktif group Head Office yang dirujuk Photo aset: File Name `foto-laptop-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-060-9** File (awal), File aktif group Branch Bandung yang dirujuk Photo aset: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-060-10** File (awal; dimutasi TC-FA-FAFM-BE-060-authz-per-role-sisi-server), File group Head Office di Recycle Bin dalam masa retensi: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-060-11** File (awal), File group Branch Bandung di Recycle Bin dalam masa retensi: File Name `scanner-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-060-12** File (awal; dimutasi TC-FA-FAFM-BE-060-authz-per-role-sisi-server), File aktif group Head Office yang dirujuk Photo aset dan akan di-Delete: File Name `foto-monitor-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-061-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-061-2** User (awal), Aktor Group Manager group Head Office: Name `Hendra Gunawan {runId}` (22 kar), Role `Group Manager` (13 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-061-3** User (awal), Pemegang Manage files Read group Branch Bandung: Name `Wulan Anggraini {runId}` (23 kar), Role `Manage files` (12 kar), Cakupan Read `Branch Bandung beserta descendant` (33 kar), Cakupan Delete `tidak ada` (9 kar) · sumber matriks role PRD
- **DU-061-4** User (awal), Aktor dengan akses Attachments kelompok Purchase: Name `Maya Kartika {runId}` (20 kar), Role `role dengan akses Attachments kelompok Purchase` (47 kar), Cakupan Read `Head Office beserta descendant` (30 kar) · sumber PRD §9.11
- **DU-061-5** User (awal), Pemegang Manage files tanpa akses Attachments kelompok Purchase: Name `Dimas Prakoso {runId}` (21 kar), Role `Manage files` (12 kar), Cakupan Read `Head Office beserta descendant` (30 kar), Cakupan Delete `Head Office beserta descendant` (30 kar), Akses Purchase `tanpa akses Attachments kelompok Purchase` (41 kar) · sumber PRD §9.11
- **DU-061-6** Aset (awal), Aset group Head Office dengan foto aktif dan file di Recycle Bin: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-061-7** Aset (awal), Aset group Branch Bandung di luar scope Group Manager Head Office: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-061-8** Aset (awal; dimutasi TC-FA-FAFM-BE-061-scope-client-group-dan-purchase), Aset yang group-nya berpindah dari Head Office ke Branch Bandung: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-061-9** Aset (awal), Aset Disposed dengan file kelompok Purchase dan General: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar), Files Size role dengan akses Purchase `750.2 KB` (8 kar), Dasar hitung Files Size `450.2 KB + 300.0 KB` (19 kar), Files Size role tanpa akses Purchase `300.0 KB` (8 kar) · sumber turunan penulis
- **DU-061-10** File (awal), File aktif group Head Office dalam scope Group Manager: File Name `laptop-ho-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-061-11** File (awal; dimutasi TC-FA-FAFM-BE-061-scope-client-group-dan-purchase), File di Recycle Bin yang masih tersedia untuk Download lalu dihapus permanen: File Name `laptop-ho-lama-{runId}.png` (26 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-061-12** File (awal), File aktif group Branch Bandung di luar scope Group Manager Head Office: File Name `scan-bb-{runId}.jpg` (19 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-061-13** File (awal), File group Branch Bandung di Recycle Bin di luar scope Group Manager Head Office: File Name `scan-bb-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-061-14** File (awal; dimutasi TC-FA-FAFM-BE-061-scope-client-group-dan-purchase), File aktif yang di-Delete sebelum aset berpindah group: File Name `foto-monitor-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-061-15** File (awal; dimutasi TC-FA-FAFM-BE-061-scope-client-group-dan-purchase), File Attachment General yang ikut berpindah scope bersama aset: File Name `manual-monitor-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-061-16** File (awal), File Attachment kelompok Purchase: File Name `invoice-printer-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-061-17** File (awal), File Attachment kelompok General pada aset yang sama dengan Purchase: File Name `warranty-printer-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-061-18** File (awal), File aktif milik klien lain: File Name `dokumen-klien-lain-{runId}.pdf` (30 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Entitas `klien lain, bukan entitas aktor` (31 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-061-19** File (awal), File di Recycle Bin milik klien lain: File Name `arsip-klien-lain-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Entitas `klien lain, bukan entitas aktor` (31 kar), Size `300.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-061-20** File (awal), File Attachment kelompok Purchase di Recycle Bin: File Name `kuitansi-laptop-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `200.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-062-2** File (awal), File aktif yang di-Delete saat entitas diblok: File Name `foto-laptop-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-062-3** File (awal), File aktif kedua pada Delete bulk saat entitas diblok: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-062-4** File (awal), File di Recycle Bin yang di-Permanently Delete saat entitas diblok: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-5** File (awal), File kedua di Recycle Bin pada Permanently Delete bulk saat entitas diblok: File Name `scanner-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-6** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File aktif yang di-Delete untuk membuktikan tanpa gating plan: File Name `tanpa-gating-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `500.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-062-8** Aset (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), Aset Disposed yang Asset Data-nya dihapus lalu cascade purge saat entitas Suspended: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-062-9** Aset (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), Aset Disposed yang Asset Data-nya dihapus lalu cascade purge saat entitas Expired: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar) · sumber turunan penulis
- **DU-062-10** Aset (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), Aset Disposed yang Asset Data-nya dihapus lalu cascade purge saat entitas dalam masa Grace: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar) · sumber turunan penulis
- **DU-062-11** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File aset yang dihapus oleh cascade purge saat entitas Suspended: File Name `dsp-printer-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Reference `ID transaksi DSP- milik aset DU-062-8` (37 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `3.2 MB` (6 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-062-12** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File aset yang dihapus oleh cascade purge saat entitas Expired: File Name `dsp-monitor-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Reference `ID transaksi DSP- milik aset DU-062-9` (37 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `1.5 MB` (6 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-062-13** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File aset yang dihapus oleh cascade purge saat entitas dalam masa Grace: File Name `dsp-projector-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Reference `ID transaksi DSP- milik aset DU-062-10` (38 kar), Asset `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Bandung` (14 kar), Size `2.0 MB` (6 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-062-14** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File di Recycle Bin yang di-auto-purge saat entitas Suspended: File Name `purge-suspended-{runId}.png` (27 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `700.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-15** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File di Recycle Bin yang di-auto-purge saat entitas Expired: File Name `purge-expired-{runId}.png` (25 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `710.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-16** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File di Recycle Bin yang di-auto-purge saat entitas dalam masa Grace: File Name `purge-grace-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `720.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-062-17** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File aktif yang di-Delete untuk membuktikan ledger Storage tidak berubah: File Name `ledger-hapus-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `530.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-062-18** File (awal; dimutasi TC-FA-FAFM-BE-062-state-entitas-dan-plan), File di Recycle Bin yang di-Permanently Delete untuk membuktikan ledger Storage tidak berubah: File Name `ledger-permanen-{runId}.png` (27 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `540.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-063-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-063-2** Aset (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), Aset dengan dua rujukan file: Photo dan field custom Document: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-063-6` (14 kar), Warranty Card `milik DU-063-7` (14 kar) · sumber turunan penulis
- **DU-063-3** Aset (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), Aset dengan Photo yang ikut di-Delete lewat bulk: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar), Photo `milik DU-063-8` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-063-4** Aset (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), Aset dengan dokumen Attachment kelompok General: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Attachment General `milik DU-063-9` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-063-5** Aset (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), Aset dengan Photo yang di-Delete lewat konfirmasi ganda: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-063-10` (15 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-063-6** File (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), File Asset Photo yang dirujuk Photo aset dan di-Delete single: File Name `foto-laptop-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-063-7** File (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), File Custom Field Document pada aset yang sama dengan Photo: File Name `warranty-card-lpt-{runId}.pdf` (29 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-063-8** File (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), File Asset Photo pada aset lain dalam Delete bulk Source campuran: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-063-9** File (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), File Attachment kelompok General dalam Delete bulk Source campuran: File Name `manual-printer-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-063-10** File (awal; dimutasi TC-FA-FAFM-BE-063-soft-delete-atomik), File Asset Photo yang dikonfirmasi Delete dua kali serentak: File Name `foto-monitor-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-064-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-064-2** User (awal), Aktor Group Manager group Head Office: Name `Hendra Gunawan {runId}` (22 kar), Role `Group Manager` (13 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-064-3** File (awal; dimutasi TC-FA-FAFM-BE-064-bulk-delete-hasil-per-item), File aktif dalam scope yang dihapus pada bulk campuran: File Name `foto-printer-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-064-4** File (awal; dimutasi TC-FA-FAFM-BE-064-bulk-delete-hasil-per-item), File aktif kedua dalam scope yang dihapus pada bulk campuran: File Name `foto-monitor-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-064-5** File (awal), File aktif di luar scope group aktor yang dilewati: File Name `foto-proyektor-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-064-6** File (awal), File yang sudah di Recycle Bin dan tidak berubah oleh Delete bulk: File Name `printer-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-064-7** File (awal; dimutasi TC-FA-FAFM-BE-064-bulk-delete-hasil-per-item), File di Recycle Bin yang dihapus permanen sebelum bulk sehingga tidak tersedia: File Name `monitor-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-064-8** File (awal), File aktif di luar scope group aktor pada bulk yang seluruh itemnya dilewati: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `700.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-064-9** File (awal), File yang sudah di Recycle Bin pada bulk bersama item di luar scope dan tidak berubah: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.2 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-065-2** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File di Recycle Bin yang dihapus permanen single lalu diulang: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-065-3** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File di Recycle Bin yang dihapus pada bulk campuran: File Name `printer-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-4** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File di Recycle Bin group Branch Bandung yang dihapus pada bulk campuran: File Name `scanner-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-5** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File Branch Bandung di Recycle Bin yang masuk Select All: File Name `monitor-lama-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Branch Bandung` (14 kar), Size `750.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-6** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File Branch Bandung di Recycle Bin yang masuk Select All: File Name `proyektor-lama-{runId}.png` (26 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Bandung` (14 kar), Size `820.4 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-7** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File Branch Bandung di Recycle Bin yang masuk Select All: File Name `tablet-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Branch Bandung` (14 kar), Size `700.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-8** File (awal), File Head Office di Recycle Bin di luar saringan Select All, hanya di-Download: File Name `kamera-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Size `1.2 MB` (6 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-9** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File di Recycle Bin yang dihapus permanen oleh permintaan serentak single dan bulk: File Name `race-satu-{runId}.png` (21 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `510.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-10** File (awal; dimutasi TC-FA-FAFM-BE-065-permanently-delete-sisi-server), File kedua di Recycle Bin pada bulk serentak: File Name `race-dua-{runId}.png` (20 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `520.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-11** File (awal), File di Recycle Bin pada penyimpanan tidak terjangkau: File Name `gagal-satu-{runId}.png` (22 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `530.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-065-12** File (awal), File kedua di Recycle Bin pada penyimpanan tidak terjangkau: File Name `gagal-dua-{runId}.png` (21 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `540.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-066-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-066-2** Aset (awal; dimutasi TC-FA-FAFM-BE-066-auto-purge-harian), Aset pemilik file Repair Photo yang di-purge: Name `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar), Status `Disposed` (8 kar) · sumber turunan penulis
- **DU-066-3** Aset (awal; dimutasi TC-FA-FAFM-BE-066-auto-purge-harian), Aset pemilik file Damaged Photo yang di-purge: Name `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Status `Unmanaged` (9 kar) · sumber turunan penulis
- **DU-066-4** Aset (awal), Aset pemilik file yang belum eligible: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-066-5** Aset (awal), Aset pemilik file pada skenario kegagalan penyimpanan: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-066-6** File (awal; dimutasi TC-FA-FAFM-BE-066-auto-purge-harian), File Recycle Bin dengan batas purge tersimpan terlampaui: File Name `repair-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Repair Photo` (12 kar), Reference `—` (1 kar), Asset `Toyota Avanza {runId}` (21 kar), Group `Fleet` (5 kar), Size `880.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `0 days` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-066-7** File (awal; dimutasi TC-FA-FAFM-BE-066-auto-purge-harian), File Recycle Bin dengan batas purge tersimpan tercapai tepat hari kalender UTC job berjalan: File Name `damage-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Damaged Photo` (13 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `0 days` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-066-8** File (awal), File Recycle Bin dengan batas purge tersimpan belum tercapai: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `29 days` (7 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-066-9** File (awal; dimutasi TC-FA-FAFM-BE-066-auto-purge-harian), File Recycle Bin eligible yang gagal dihapus dari penyimpanan lalu dicoba lagi: File Name `gagal-{runId}.jpg` (17 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `530.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `0 days` (6 kar) · sumber turunan penulis
- **DU-067-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-067-2** Aset (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), Aset yang fotonya diganti dua kali: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-067-6` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-067-3** Aset (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), Aset yang fotonya dikosongkan: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar), Photo `milik DU-067-9` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-067-4** Aset (awal), Aset dengan form basi yang masih membawa rujukan ke file di Recycle Bin: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Attachment General `milik DU-067-10 (sudah di Recycle Bin)` (38 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-067-5** Aset (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), Aset yang fotonya diganti serentak dengan Delete manual: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-067-11` (15 kar) · sumber turunan penulis
- **DU-067-6** File (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), File lama yang diganti pada penggantian pertama: File Name `foto-laptop-lama-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-067-7** File (dibuat; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), File baru pengganti pertama, juga file lama pada penggantian kedua: File Name `foto-laptop-baru-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-8** File (dibuat), File baru pengganti kedua: File Name `foto-laptop-baru2-{runId}.jpg` (29 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `700.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-9** File (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), File yang dikosongkan tanpa pengganti: File Name `foto-scanner-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-10** File (awal), File Attachment yang sudah di Recycle Bin namun masih dirujuk form basi: File Name `manual-printer-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-067-11** File (awal; dimutasi TC-FA-FAFM-BE-067-auto-transition-modul-sumber), File lama yang disentuh Delete manual dan auto-transition serentak: File Name `foto-monitor-lama-{runId}.jpg` (29 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `880.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-12** File (dibuat), File baru pengganti pada skenario serentak: File Name `foto-monitor-baru-{runId}.jpg` (29 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `600.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-13** Aset (awal), Aset pada skenario kegagalan transaksi: Name `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar), Photo `milik DU-067-14` (15 kar) · sumber turunan penulis
- **DU-067-14** File (awal), File lama yang tetap aktif saat transaksi gagal: File Name `foto-tablet-lama-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-067-15** File (dicoba), File baru yang batal dibuat saat transaksi gagal: File Name `foto-tablet-baru-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Branch Bandung` (14 kar), Size `1.0 MB` (6 kar), Status File `tidak ada` (9 kar) · sumber turunan penulis
- **DU-067-16** Aset (awal), Aset dengan form basi yang masih membawa rujukan ke file yang sudah dihapus permanen: Name `Projector Epson EB-X49 {runId}` (30 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Attachment General `milik DU-067-17 (sudah dihapus permanen)` (40 kar) · sumber turunan penulis
- **DU-067-17** File (awal), File Attachment yang sudah dihapus permanen namun masih dirujuk form basi: File Name `panduan-projector-{runId}.pdf` (29 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Projector Epson EB-X49 {runId}` (30 kar), Group `Head Office` (11 kar), Size `450.0 KB` (8 kar), Status File `dihapus permanen` (16 kar) · sumber turunan penulis
- **DU-068-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-068-2** Aset (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), Aset aktif dengan tiga file (dua aktif, satu di Recycle Bin) yang di-Delete Asset Data: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Jumlah file `3 (2 aktif, 1 di Recycle Bin)` (29 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-068-3** Aset (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), Aset Draft dengan satu file yang dihapus: Name `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Status `Draft` (5 kar), Jumlah file `1 (aktif)` (9 kar) · sumber turunan penulis
- **DU-068-4** Aset (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), Aset dengan dua file aktif pada skenario retry cascade purge: Name `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar), Jumlah file `2 (aktif)` (9 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-068-5** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File Asset Photo aktif milik aset yang dihapus: File Name `foto-laptop-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-068-6** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File Custom Field Document aktif milik aset yang dihapus: File Name `warranty-card-lpt-{runId}.pdf` (29 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-068-7** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File di Recycle Bin milik aset yang dihapus, belum mencapai batas purge: File Name `laptop-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `29 days` (7 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-068-8** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File aktif milik aset Draft yang dihapus: File Name `foto-draft-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-068-9** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File aktif yang berhasil dihapus pada upaya pertama cascade purge: File Name `printer-ok-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-068-10** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File aktif yang gagal dihapus pada upaya pertama lalu berhasil pada retry: File Name `printer-gagal-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-068-11** Aset (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), Aset dengan tiga file pada skenario jeda cascade purge: Name `Monitor LG 24MK430H {runId}` (27 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Asset ID `dibentuk server, milik DU-068-11` (32 kar), Jumlah file `3 (2 aktif, 1 di Recycle Bin)` (29 kar) · sumber turunan penulis
- **DU-068-12** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File Asset Photo aktif yang dibaca, di-Preview, dan di-Download selama jeda: File Name `monitor-depan-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24MK430H {runId}` (27 kar), Group `Head Office` (11 kar), Size `410.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-068-13** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File Attachment aktif yang di-Delete selama jeda: File Name `monitor-manual-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Monitor LG 24MK430H {runId}` (27 kar), Group `Head Office` (11 kar), Size `280.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-068-14** File (awal; dimutasi TC-FA-FAFM-BE-068-cascade-purge-aset), File di Recycle Bin yang di-Permanently Delete selama jeda: File Name `monitor-bin-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24MK430H {runId}` (27 kar), Group `Head Office` (11 kar), Size `190.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `29 days` (7 kar) · sumber turunan penulis
- **DU-068-15** User (awal), Aktor Group Manager group Head Office: Name `Hendra Gunawan {runId}` (22 kar), Role `Group Manager` (13 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-068-16** User (awal), Pemegang Manage files Read group Branch Bandung: Name `Wulan Anggraini {runId}` (23 kar), Role `Manage files` (12 kar), Cakupan Read `Branch Bandung beserta descendant` (33 kar), Cakupan Delete `tidak ada` (9 kar) · sumber matriks role PRD
- **DU-069-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-069-2** User (awal), Aktor Custom dengan Manage files Read pada Branch Bandung saja: Name `Wulan Anggraini {runId}` (23 kar), Role `Custom` (6 kar), Manage files `Read pada Branch Bandung` (24 kar), Cakupan `Branch Bandung` (14 kar) · sumber matriks role PRD
- **DU-069-3** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Disposed dengan dua file aktif dan dua file di Recycle Bin: Name `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar), Jumlah file `4 (2 aktif, 2 di Recycle Bin)` (29 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-069-4** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Disposed dengan satu file aktif yang dihapus lewat Delete Asset Data: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar), Jumlah file `1 (aktif)` (9 kar) · sumber turunan penulis
- **DU-069-5** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Active tanpa file yang berubah menjadi Unmanaged: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Jumlah file `0` (1 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-069-6** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Active dengan Photo yang diganti serta dua dokumen Attachment: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-069-13` (15 kar), Transaksi `tersedia untuk Assignment baru` (30 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-069-7** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Draft dengan foto registrasi yang diganti lalu dihapus: Name `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Status `Draft` (5 kar), Foto registrasi `milik DU-069-15` (15 kar) · sumber turunan penulis
- **DU-069-8** File (awal), File Disposal Document aktif aset Disposed yang tidak diubah: File Name `dsp-receipt-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `3.2 MB` (6 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-069-9** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File aktif yang di-Delete (soft) untuk memindahkan byte ke Recycle Bin: File Name `maint-after-{runId}.jpg` (23 kar), File Format `JPG` (3 kar), Source `Maintenance After Photo` (23 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `1.9 MB` (6 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-069-10** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File di Recycle Bin yang dihapus permanen: File Name `maint-before-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `750.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-069-11** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File di Recycle Bin yang dihapus auto-purge: File Name `maint-old-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Source `Maintenance Before Photo` (24 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `600.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `29 days` (7 kar) · sumber turunan penulis
- **DU-069-12** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File aktif aset Disposed yang dihapus oleh cascade purge: File Name `scanner-doc-{runId}.pdf` (23 kar), File Format `PDF` (3 kar), Source `Disposal Document` (17 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `2.0 MB` (6 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-069-13** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File lama pada penggantian Photo (auto-transition): File Name `foto-laptop-lama-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-069-14** File (dibuat), File baru pengganti Photo aset Laptop: File Name `foto-laptop-baru-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-069-15** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File foto registrasi pertama aset Draft yang menjadi file Recycle Bin saat diganti: File Name `foto-draft-lama-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `—` (1 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-069-16** File (dibuat; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File foto registrasi pengganti aset Draft yang dihapus cascade purge: File Name `foto-draft-baru-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `—` (1 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-069-17** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File aktif yang di-Delete saat Storage penuh: File Name `penuh-satu-{runId}.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-069-18** File (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), File di Recycle Bin yang dihapus permanen saat Storage penuh: File Name `penuh-dua-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-069-19** File (dicoba), Berkas yang diunggah ke form yang dibatalkan: File Name `batal-{runId}.jpg` (17 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Size `500.0 KB` (8 kar), Status File `tidak pernah menjadi record` (27 kar) · sumber turunan penulis
- **DU-069-20** File (dicoba), Foto wajib transaksi yang upload-nya ditolak saat Storage penuh: File Name `handover-{runId}.jpg` (20 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Reference `—` (1 kar), Size `450.2 KB` (8 kar), Status File `tidak pernah menjadi record` (27 kar), Titik upload `Photo at start Assignment atas aset DU-069-6` (44 kar) · sumber turunan penulis
- **DU-069-21** Aset (awal; dimutasi TC-FA-FAFM-BE-069-perhitungan-storage-fams), Aset Active dengan satu file yang berganti Status ke Unmanaged lalu kembali Active: Name `Router Cisco ISR 4331 {runId}` (29 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Jumlah file `1 (aktif)` (9 kar) · sumber turunan penulis
- **DU-069-22** File (awal), File aktif aset yang berganti Status: File Name `router-manual-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Size `1.5 MB` (6 kar), Status File `aktif` (5 kar), Asset `Router Cisco ISR 4331 {runId}` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-069-23** Aset (awal), Aset Active dalam Assignment yang siap pada langkah Photo at end: Name `Tablet Samsung Galaxy Tab S8 {runId}` (36 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Transaksi `Assignment belum dikembalikan` (29 kar) · sumber turunan penulis
- **DU-069-24** Aset (awal), Aset Active dalam Transfer yang siap pada langkah Send: Name `Proyektor Epson EB-X49 {runId}` (30 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Transaksi `Transfer siap Send` (18 kar) · sumber turunan penulis
- **DU-069-25** Aset (awal), Aset Active dalam Transfer yang sudah dikirim dan siap pada langkah Receive: Name `Kamera Sony ZV-E10 {runId}` (26 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Transaksi `Transfer siap Receive` (21 kar) · sumber turunan penulis
- **DU-069-26** File (dicoba), Foto wajib pengembalian yang upload-nya ditolak saat Storage penuh: File Name `return-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Return Photo` (12 kar), Reference `—` (1 kar), Size `410.6 KB` (8 kar), Status File `tidak pernah menjadi record` (27 kar), Asset `Tablet Samsung Galaxy Tab S8 {runId}` (36 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-069-27** File (dicoba), Foto wajib langkah Send yang upload-nya ditolak saat Storage penuh: File Name `send-{runId}.jpg` (16 kar), File Format `JPG` (3 kar), Source `Send Photo` (10 kar), Reference `—` (1 kar), Size `380.4 KB` (8 kar), Status File `tidak pernah menjadi record` (27 kar), Asset `Proyektor Epson EB-X49 {runId}` (30 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-069-28** File (dicoba), Foto wajib langkah Receive yang upload-nya ditolak saat Storage penuh: File Name `receive-{runId}.jpg` (19 kar), File Format `JPG` (3 kar), Source `Receive Photo` (13 kar), Reference `—` (1 kar), Size `395.8 KB` (8 kar), Status File `tidak pernah menjadi record` (27 kar), Asset `Kamera Sony ZV-E10 {runId}` (26 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-070-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-070-2** User (awal), Aktor Custom dengan Manage files Read pada Branch Bandung beserta descendant: Name `Wulan Anggraini {runId}` (23 kar), Role `Custom` (6 kar), Manage files `Read pada Branch Bandung beserta descendant` (43 kar), Cakupan `Branch Bandung beserta descendant` (33 kar) · sumber matriks role PRD
- **DU-070-3** User (awal), Pengunggah dengan last name dua kata: Name `Siti Nur Rahmawati {runId}` (26 kar), Nama tampil `Siti N` (6 kar), Role `Total Control` (13 kar) · sumber turunan penulis
- **DU-070-4** Group (awal), Group anak Head Office dengan leaf yang sama dengan group anak Branch Bandung: Name `Warehouse {runId}` (17 kar), Parent `Head Office` (11 kar), Hierarki penuh `Head Office > Warehouse {runId}` (31 kar) · sumber turunan penulis
- **DU-070-5** Group (awal), Group anak Branch Bandung dengan leaf yang sama dengan group anak Head Office: Name `Warehouse {runId}` (17 kar), Parent `Branch Bandung` (14 kar), Hierarki penuh `Branch Bandung > Warehouse {runId}` (34 kar) · sumber turunan penulis
- **DU-070-6** Aset (awal), Aset di Head Office > Warehouse pemilik dua file: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office > Warehouse {runId}` (31 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-070-7** Aset (awal), Aset dengan tanda kutip pada nama di Branch Bandung > Warehouse: Name `Printer "HP" M404 {runId}` (25 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Status `Active` (6 kar), Tulisan Asset pada sel CSV `sel dibungkus kutip ganda dan kutip dalam nama digandakan` (57 kar), Tulisan kutip pada sel CSV `""HP""` (6 kar) · sumber turunan penulis
- **DU-070-8** Aset (awal), Aset kedua di Branch Bandung > Warehouse pemilik file bernama kembar: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-070-9** File (awal), File dengan koma pada nama dan ukuran bulat dalam MB: File Name `kontrak, final {runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office > Warehouse {runId}` (31 kar), Size `2.0 MB` (6 kar), Size (byte) `2097152` (7 kar), Dasar tampil Size `dari 2097152 byte` (17 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-070-10** File (awal), File Custom Field Document dengan huruf beraksen pada nama: File Name `café-élan-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office > Warehouse {runId}` (31 kar), Size `310.0 KB` (8 kar), Size (byte) `317440` (6 kar), Dasar tampil Size `dari 317440 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-070-11** File (awal), File Attachment pada aset dengan tanda kutip di nama: File Name `manual-printer-{runId}.pdf` (26 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer "HP" M404 {runId}` (25 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `450.0 KB` (8 kar), Size (byte) `460800` (6 kar), Dasar tampil Size `dari 460800 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-070-12** File (awal), File bernama kembar yang diunggah lebih dulu: File Name `scan-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer "HP" M404 {runId}` (25 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `300.0 KB` (8 kar), Size (byte) `307200` (6 kar), Dasar tampil Size `dari 307200 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar), Nama entri ZIP `scan-{runId}.pdf` (16 kar) · sumber turunan penulis
- **DU-070-13** File (awal), File bernama kembar yang diunggah sesudahnya: File Name `scan-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `640.0 KB` (8 kar), Size (byte) `655360` (6 kar), Dasar tampil Size `dari 655360 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar), Nama entri ZIP `scan-{runId} (2).pdf` (20 kar), Dasar nama entri ZIP `dari nama kembar DU-070-12, diunggah sesudahnya` (47 kar) · sumber turunan penulis
- **DU-070-14** File (awal), File di Recycle Bin yang tidak tersedia untuk ZIP: File Name `lama-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer "HP" M404 {runId}` (25 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `820.4 KB` (8 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-070-15** File (awal), File bernama kembar ketiga yang diunggah paling akhir: File Name `scan-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer "HP" M404 {runId}` (25 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `120.0 KB` (8 kar), Size (byte) `122880` (6 kar), Dasar tampil Size `dari 122880 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `aktif` (5 kar), Nama entri ZIP `scan-{runId} (3).pdf` (20 kar), Dasar nama entri ZIP `dari nama kembar DU-070-12 dan DU-070-13, diunggah paling akhir` (63 kar) · sumber turunan penulis
- **DU-070-16** File (awal), File foto registrasi aset Draft di Recycle Bin dengan Asset kosong: File Name `foto-registrasi-draft-{runId}.jpg` (33 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `—` (1 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Size `500.0 KB` (8 kar), Size (byte) `512000` (6 kar), Dasar tampil Size `dari 512000 byte` (16 kar), Uploaded By `Siti Nur Rahmawati {runId}` (26 kar), Status File `di Recycle Bin` (14 kar), Tulisan Asset pada sel CSV `-` (1 kar) · sumber PRD §4.1 Recycle Bin Setup Column (Asset: Tampil — untuk file Draft, F-FAFM-01h)
- **DU-070-17** Aset (awal), Aset Unmanaged tanpa file di Head Office > Warehouse: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office > Warehouse {runId}` (31 kar), Status `Unmanaged` (9 kar), Files Size `0.0 KB` (6 kar), Files Size (byte) `0` (1 kar), Tulisan Status pada sel CSV `Unmanaged` (9 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-070-18** Aset (awal), Aset Disposed tanpa file di Branch Bandung > Warehouse: Name `Scanner Canon LiDE 400 {runId}` (30 kar), Group `Branch Bandung > Warehouse {runId}` (34 kar), Status `Disposed` (8 kar), Tulisan Status pada sel CSV `Disposed` (8 kar) · sumber turunan penulis
- **DU-071-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-071-2** User (awal), Pelaku soft-delete dengan nama depan sama dengan pelaku lain: Name `Budi Santoso {runId}` (20 kar), Nama tampil `Budi S` (6 kar), Role `Total Control` (13 kar) · sumber turunan penulis
- **DU-071-3** User (awal), Pelaku soft-delete dengan nama depan sama dengan pelaku lain: Name `Budi Hartono {runId}` (20 kar), Nama tampil `Budi H` (6 kar), Role `Total Control` (13 kar) · sumber turunan penulis
- **DU-071-4** Aset (awal), Aset Head Office pemilik dua file di Recycle Bin: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-071-5** Aset (awal), Aset Branch Bandung pemilik dua file di Recycle Bin: Name `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-071-6** Aset (awal), Aset Branch Bandung pemilik satu file di Recycle Bin: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-071-7** Aset (awal), Aset Draft yang file-nya di Recycle Bin tampil dengan Asset kosong: Name `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Status `Draft` (5 kar) · sumber turunan penulis
- **DU-071-8** File (awal), File Recycle Bin dengan nama diawali huruf kapital dan Size sama dengan file lain: File Name `Anggur-lama-{runId}.png` (23 kar), File Format `PNG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Size (byte) `921600` (6 kar), Dasar tampil Size `dari 921600 byte` (16 kar), Deleted By `Budi Santoso {runId}` (20 kar), Urutan soft-delete `ketiga dari enam` (16 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-071-9** File (awal), File Recycle Bin dengan nama diawali huruf kecil dan Size dalam MB: File Name `apel-lama-{runId}.jpg` (21 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `1.0 MB` (6 kar), Size (byte) `1048576` (7 kar), Dasar tampil Size `dari 1048576 byte` (17 kar), Deleted By `Budi Hartono {runId}` (20 kar), Urutan soft-delete `pertama dari enam` (17 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-071-10** File (awal), File Recycle Bin kategori Asset Documents di-soft-delete oleh System: File Name `Dokumen-garansi-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Size (byte) `307200` (6 kar), Dasar tampil Size `dari 307200 byte` (16 kar), Deleted By `System` (6 kar), Urutan soft-delete `keenam dari enam` (16 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-071-11** File (awal), File Recycle Bin milik aset Draft dengan Asset kosong: File Name `draft-foto-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `—` (1 kar), Group `Head Office` (11 kar), Size `450.0 KB` (8 kar), Size (byte) `460800` (6 kar), Dasar tampil Size `dari 460800 byte` (16 kar), Deleted By `Budi Santoso {runId}` (20 kar), Urutan soft-delete `kelima dari enam` (16 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-071-12** File (awal), File Recycle Bin Repair Photo dengan Size sama dengan file lain: File Name `repair-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Category `Damaged` (7 kar), Source `Repair Photo` (12 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Branch Bandung` (14 kar), Size `900.0 KB` (8 kar), Size (byte) `921600` (6 kar), Dasar tampil Size `dari 921600 byte` (16 kar), Deleted By `Budi Hartono {runId}` (20 kar), Urutan soft-delete `kedua dari enam` (15 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-071-13** File (awal), File Recycle Bin Disposal Document di-soft-delete oleh System: File Name `Zebra-{runId}.pdf` (17 kar), File Format `PDF` (3 kar), Category `Disposal` (8 kar), Source `Disposal Document` (17 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Branch Bandung` (14 kar), Size `3.0 MB` (6 kar), Size (byte) `3145728` (7 kar), Dasar tampil Size `dari 3145728 byte` (17 kar), Deleted By `System` (6 kar), Urutan soft-delete `keempat dari enam` (17 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-072-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-072-2** User (awal), Aktor Group Manager group Head Office: Name `Hendra Gunawan {runId}` (22 kar), Role `Group Manager` (13 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-072-3** Aset (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), Aset pemilik file yang di-Delete serentak oleh dua aktor: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-072-8` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-072-4** Aset (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), Aset pemilik file yang di-Delete serentak dengan penggantian foto: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-072-9` (14 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-072-5** Aset (awal), Aset pemilik file di Recycle Bin pada skenario Permanently Delete serentak: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `kosong` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-072-6** Aset (awal), Aset dengan Photo yang sudah dikosongkan proses lain padahal file masih aktif: Name `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `kosong` (6 kar) · sumber turunan penulis
- **DU-072-7** Aset (awal), Aset pemilik file auto-purge dan file yang sudah di Recycle Bin: Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `kosong` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-072-8** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File aktif yang di-Delete oleh dua aktor serentak: File Name `balap-delete-{runId}.jpg` (24 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-072-9** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File aktif yang di-Delete serentak dengan auto-transition: File Name `balap-transisi-lama-{runId}.jpg` (31 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-072-10** File (dibuat), File baru pengganti pada skenario Delete serentak dengan auto-transition: File Name `balap-transisi-baru-{runId}.jpg` (31 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `600.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-072-11** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File di Recycle Bin yang dihapus permanen oleh dua aktor serentak: File Name `balap-permanen-{runId}.png` (26 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-072-12** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File di Recycle Bin dengan batas purge terlampaui yang dihapus permanen serentak dengan auto-purge: File Name `balap-purge-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `0 days` (6 kar) · sumber turunan penulis
- **DU-072-13** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File di Recycle Bin yang sudah dihapus permanen pihak lain sebelum aksi aktor kedua: File Name `sudah-hilang-{runId}.png` (24 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `510.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-072-14** File (awal), File yang sudah di Recycle Bin dan di-Delete lagi: File Name `sudah-selesai-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `520.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-072-15** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File aktif yang rujukannya sudah dikosongkan proses lain: File Name `rujukan-kosong-{runId}.jpg` (26 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-072-16** Aset (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), Aset yang recordnya disimpan dari keadaan lama setelah file-nya dihapus: Name `Webcam Logitech C920 {runId}` (28 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-072-17` (15 kar) · sumber turunan penulis
- **DU-072-17** File (awal; dimutasi TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file), File aktif yang di-Delete lalu dihapus permanen sebelum record disimpan dari keadaan lama: File Name `balap-kalah-lama-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Webcam Logitech C920 {runId}` (28 kar), Group `Head Office` (11 kar), Size `700.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-072-18** File (dicoba), File pengganti yang penyimpanannya ditolak: File Name `balap-kalah-baru-{runId}.jpg` (28 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Webcam Logitech C920 {runId}` (28 kar), Group `Head Office` (11 kar), Size `650.0 KB` (8 kar), Status File `tidak pernah tersimpan` (22 kar) · sumber turunan penulis
- **DU-073-1** User (awal), Aktor Total Control: Name `Bagas Pratama {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-073-2** User (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aktor Group Manager yang diubah namanya sesudah entri dicatat: Name `Hendra Gunawan {runId}` (22 kar), Nama baru `Hendra Setiawan {runId}` (23 kar), Role `Group Manager` (13 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-073-3** User (awal), Aktor Custom dengan Manage files Read dan Delete serta akses Attachments kelompok Purchase: Name `Indra Wijaya {runId}` (20 kar), Role `Custom` (6 kar), Manage files `Read dan Delete pada Head Office` (32 kar), Attachments Purchase `ada` (3 kar), Cakupan `Head Office` (11 kar) · sumber matriks role PRD
- **DU-073-4** User (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aktor Custom dengan Manage files Read tanpa akses Attachments kelompok Purchase, yang aksesnya ditambah kemudian: Name `Wulan Anggraini {runId}` (23 kar), Role `Custom` (6 kar), Manage files `Read pada Head Office` (21 kar), Attachments Purchase `tidak ada, lalu ditambah` (24 kar), Cakupan `Head Office` (11 kar) · sumber matriks role PRD
- **DU-073-5** Aset (awal), Aset pemilik file Delete manual dan Attachment Purchase: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-073-6** Aset (awal), Aset pemilik file pada skenario bulk dan auto-purge: Name `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-073-7** Aset (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aset yang fotonya diganti (auto-transition): Name `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-073-16` (15 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-073-8** Aset (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aset yang fotonya dikosongkan tanpa pengganti: Name `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Photo `milik DU-073-18` (15 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-073-9** Aset (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aset yang di-Delete Asset Data sehingga file-nya dihapus cascade purge: Name `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-073-10** Aset (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), Aset yang ditransfer dan diubah Status tanpa log File Manager: Name `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Status `Active` (6 kar), Group tujuan `Branch Bandung` (14 kar), Status tujuan `Disposed` (8 kar) · sumber turunan penulis
- **DU-073-11** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File yang di-Delete manual lalu di-Permanently Delete oleh aktor lain: File Name `manual-delete-{runId}.jpg` (25 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-073-12** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File pertama pada Delete bulk dan Permanently Delete bulk: File Name `bulk-satu-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-073-13** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File kedua pada Delete bulk dan Permanently Delete bulk: File Name `bulk-dua-{runId}.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-073-14** File (awal), File di Recycle Bin yang dilewati Delete bulk: File Name `bulk-lama-{runId}.pdf` (21 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `300.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-073-15** File (awal), File aktif aset yang sama yang tidak ikut permintaan bulk: File Name `bulk-tidak-ikut-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-16** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File lama yang diganti sehingga di-soft-delete auto-transition oleh System: File Name `ganti-lama-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-17** File (dibuat), File baru pengganti pada auto-transition: File Name `ganti-baru-{runId}.jpg` (22 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Scanner Epson DS-530 {runId}` (28 kar), Group `Head Office` (11 kar), Size `600.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-18** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File yang dikosongkan tanpa pengganti sehingga aktor pengguna pelaku: File Name `kosong-{runId}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Monitor LG 24 {runId}` (21 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-19** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File di Recycle Bin dengan batas purge terlampaui yang dihapus auto-purge oleh System: File Name `purge-{runId}.png` (17 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Printer HP M404 {runId}` (23 kar), Group `Head Office` (11 kar), Size `1.0 MB` (6 kar), Status File `di Recycle Bin` (14 kar), Auto-Purge In `0 days` (6 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-073-20** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File aktif aset yang dihapus lewat Delete Asset Data (cascade purge): File Name `cascade-aktif-{runId}.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Head Office` (11 kar), Size `520.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-21** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File di Recycle Bin aset yang dihapus lewat Delete Asset Data yang tidak punya entri Changelog File Manager: File Name `cascade-bin-{runId}.png` (23 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Head Office` (11 kar), Size `510.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber turunan penulis
- **DU-073-22** File (awal), File aktif yang terkena Download, ZIP, pembacaan Storage, transfer, perubahan Status, kuota, dan retensi tanpa log: File Name `aman-{runId}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Camera Canon EOS 90D {runId}` (28 kar), Group `Head Office` (11 kar), Size `430.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber turunan penulis
- **DU-073-23** File (awal; dimutasi TC-FA-FAFM-BE-073-pencatatan-log-file-manager), File Attachment kelompok Purchase yang di-Delete oleh pemegang akses Purchase: File Name `invoice-{runId}.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-074-1** User (awal), Aktor Read Only tanpa capability Delete: Name `Sari Wulandari {runId}` (22 kar), Role `Read Only` (9 kar), Cakupan `seluruh group` (13 kar) · sumber matriks role PRD
- **DU-074-2** User (awal), Aktor Custom dengan Manage files Read saja: Name `Wulan Anggraini {runId}` (23 kar), Role `Custom` (6 kar), Manage files `Read pada Head Office` (21 kar), Cakupan `Head Office` (11 kar) · sumber matriks role PRD
- **DU-074-3** Aset (awal), Aset pemilik file yang menjadi sasaran request langsung: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Active` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-074-4** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File aktif sasaran Delete single tanpa capability: File Name `delete-langsung-{runId}.jpg` (27 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-074-5** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File aktif pertama sasaran Delete bulk tanpa capability: File Name `delete-bulk-satu-{runId}.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-074-6** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File aktif kedua sasaran Delete bulk tanpa capability: File Name `delete-bulk-dua-{runId}.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Status File `aktif` (5 kar) · sumber PRD §4.1 Files Example Data
- **DU-074-7** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File di Recycle Bin sasaran Permanently Delete single tanpa capability: File Name `permanen-langsung-{runId}.png` (29 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `900.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-074-8** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File di Recycle Bin pertama sasaran Permanently Delete bulk tanpa capability: File Name `permanen-bulk-satu-{runId}.png` (30 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-074-9** File (awal; dimutasi TC-FA-FAFM-BE-074-request-langsung-tanpa-capability), File di Recycle Bin kedua sasaran Permanently Delete bulk tanpa capability: File Name `permanen-bulk-dua-{runId}.png` (29 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Size `750.0 KB` (8 kar), Status File `di Recycle Bin` (14 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-075-1** Storage Usage (awal), Kartu Storage Usage di bawah kuota: Total Used `4.8 GB` (6 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `3.2 GB` (6 kar) · sumber PRD §4.2c Example Data
- **DU-075-2** File (awal), File aktif tab Asset Photo: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-075-3** Asset Data (awal), Aset Disposed dengan dokumen Disposal: Name `Printer HP M404 - 1` (19 kar), Asset ID `PRN-2026-0001` (13 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar), Data & Log Size `1.2 MB` (6 kar), Files Size `5.8 MB` (6 kar), Total Size `7.0 MB` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-075-4** Asset Data (awal), Aset Unmanaged tanpa file: Name `Monitor LG 24 - 7` (17 kar), Asset ID `MON-2026-0007` (13 kar), Group `Head Office` (11 kar), Status `Unmanaged` (9 kar), Data & Log Size `412.0 KB` (8 kar), Files Size `0.0 KB` (6 kar), Total Size `412.0 KB` (8 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-075-5** Storage Usage (awal), Kartu Storage Usage penuh: Total Used `50.4 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `48.8 GB` (7 kar) · sumber PRD §4.2c Example Data
- **DU-076-1** Storage Usage (awal), Kartu di bawah kuota: Total Used `4.8 GB` (6 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `3.2 GB` (6 kar) · sumber PRD §4.2c Example Data
- **DU-076-2** Storage Usage (awal), Kartu melewati kuota: Total Used `50.4 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `48.8 GB` (7 kar) · sumber PRD §4.2c Example Data
- **DU-076-3** Storage Usage (awal), Kuota belum dialokasikan: Total Used `3.2 GB` (6 kar), Storage Quota `—` (1 kar), Fixed Asset `3.2 GB` (6 kar) · sumber PRD §4.2c Example Data
- **DU-076-4** Storage Usage (awal), Kuota 0.0 GB: Total Used `1.0 GB` (6 kar), Storage Quota `0.0 GB` (6 kar), Fixed Asset `1.0 GB` (6 kar) · sumber SUC-04f
- **DU-076-5** Storage Usage (awal), Total Used belum tersedia, kuota terisi: Total Used `—` (1 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `3.2 GB` (6 kar) · sumber SUC-04f
- **DU-076-6** Storage Usage (awal), Pemakaian 120% dari kuota: Total Used `60.0 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `58.0 GB` (7 kar) · sumber SUC-05b
- **DU-076-7** Storage Usage (awal), Satu langkah di bawah kuota: Total Used `49.9 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `40.0 GB` (7 kar) · sumber turunan penulis
- **DU-076-8** Storage Usage (awal), Tepat di kuota: Total Used `50.0 GB` (7 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `40.0 GB` (7 kar) · sumber turunan penulis
- **DU-076-9** Storage Usage (awal), Angka GB di atas 1,000.0 dengan pemisah ribuan: Total Used `1,536.0 GB` (10 kar), Storage Quota `2,000.0 GB` (10 kar), Fixed Asset `1,200.0 GB` (10 kar) · sumber turunan penulis
- **DU-077-1** Storage Usage (awal), Kartu terisi (setelah Try Again, dan saat tabel Files gagal dimuat): Total Used `4.8 GB` (6 kar), Storage Quota `50.0 GB` (7 kar), Fixed Asset `3.2 GB` (6 kar) · sumber PRD §4.2c Example Data
- **DU-077-2** File (awal), File aktif di tabel Files: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-078-1** File (awal), File Asset Photo: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi Santoso` (12 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-078-2** File (awal), File Attachment General: File Name `warranty-card-lpt0004.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `28/10/26 09:00` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-078-3** File (awal), Attachment tanpa Reference (null): File Name `lease-agreement-lpt0004.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `None` (4 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `120.0 KB` (8 kar), Uploaded By `Budi` (4 kar), Upload Date `29/10/26 10:05` (14 kar) · sumber turunan penulis
- **DU-078-4** File (awal), Attachment dengan Reference string kosong: File Name `serial-label-lpt0004.pdf` (24 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `` (0 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `88.0 KB` (7 kar), Uploaded By `Dewi Anggraini` (14 kar), Upload Date `30/10/26 11:10` (14 kar) · sumber turunan penulis
- **DU-078-5** File (awal), Custom Field Document dengan custom field sumber terhapus: File Name `serial-label-lpt0005.pdf` (24 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `None` (4 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `76.0 KB` (7 kar), Uploaded By `Dewi Anggreni` (13 kar), Upload Date `31/10/26 08:20` (14 kar) · sumber turunan penulis
- **DU-078-6** File (awal), Nama file, Asset, dan nama user panjang: File Name `regional-procurement-and-vendor-management-office-jakarta-agreement.pdf` (71 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Regional Procurement and Vendor Management Office Jakarta` (57 kar), Asset ID `OFC-2026-0001` (13 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Uploaded By `Buzzlightyear Sumardi` (21 kar), Upload Date `06/11/26 10:00` (14 kar) · sumber turunan penulis
- **DU-078-7** File (awal), Group tepat 25 karakter: File Name `rack-layout-svr0002.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Server Dell R740 - 2` (20 kar), Asset ID `SVR-2026-0002` (13 kar), Group `Jakarta Barat Warehouse 1` (25 kar), Size `1.4 MB` (6 kar), Uploaded By `Alexander Graham Bell` (21 kar), Upload Date `07/11/26 13:20` (14 kar), Hierarki Group `Head Office > Jakarta Barat Warehouse 1` (39 kar) · sumber turunan penulis
- **DU-078-8** File (awal), Group lebih dari 25 karakter: File Name `rack-layout-svr0003.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Server Dell R740 - 3` (20 kar), Asset ID `SVR-2026-0003` (13 kar), Group `Jakarta Barat Warehouse 12` (26 kar), Size `1.2 MB` (6 kar), Uploaded By `Siti Nurbaya` (12 kar), Upload Date `07/11/26 13:45` (14 kar), Hierarki Group `Head Office > Jakarta Barat Warehouse 12` (40 kar), Group tampil di badge `Jakarta Bara..Warehouse 12` (26 kar) · sumber turunan penulis
- **DU-078-9** File (awal), Group berhierarki tiga level: File Name `floor-plan-srv-room.pdf` (23 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Rack Cabinet 42U - 1` (20 kar), Asset ID `RCK-2026-0001` (13 kar), Group `Server Room` (11 kar), Size `2.1 MB` (6 kar), Uploaded By `John Lennon` (11 kar), Upload Date `08/11/26 09:10` (14 kar), Hierarki Group `Jakarta Office > Floor 2 > Server Room` (38 kar) · sumber turunan penulis
- **DU-078-10** File (awal), File diunggah aktor System: File Name `handbook-lpt0009.pdf` (20 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Size `95.0 KB` (7 kar), Uploaded By `System` (6 kar), Upload Date `09/11/26 02:00` (14 kar) · sumber turunan penulis
- **DU-078-11** File (awal), Size di atas 1,000.0 GB: File Name `site-survey-scans.pdf` (21 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `1,536.0 GB` (10 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `10/11/26 15:00` (14 kar) · sumber turunan penulis
- **DU-078-12** File (awal), Size yang dibulatkan menjadi 1,000.0 GB: File Name `site-survey-photos.pdf` (22 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `1,000.0 GB (mentah sedikit di bawah 1,000.0 GB)` (47 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `10/11/26 15:10` (14 kar) · sumber turunan penulis
- **DU-078-13** File (awal), File JPEG di tab Asset Photo: File Name `loading-dock.jpeg` (17 kar), File Format `JPEG` (4 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `1.1 MB` (6 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `04/11/26 08:15` (14 kar) · sumber turunan penulis
- **DU-078-14** File (awal), Reference memuat markup: File Name `card-markup-lpt0004.pdf` (23 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `<b>Warranty Card</b>` (20 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `64.0 KB` (7 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `11/11/26 09:30` (14 kar) · sumber turunan penulis
- **DU-078-15** File (awal), Size dalam MB: File Name `insurance-policy-lpt0004.pdf` (28 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `3.2 MB` (6 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `12/11/26 14:00` (14 kar) · sumber turunan penulis
- **DU-078-16** File (awal), File Name dan Asset memuat markup: File Name `<b>handover</b>-lpt0004.pdf` (27 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `<i>Laptop Dell</i> - 4` (22 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `45.0 KB` (7 kar), Uploaded By `Rina Anggraini` (14 kar), Upload Date `13/11/26 10:15` (14 kar) · sumber turunan penulis
- **DU-079-1** File (awal), File Asset Photo untuk daftar yang menjadi kosong: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Reference `—` (1 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-079-2** File (awal), File Attachment General: File Name `warranty-card-lpt0004.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `28/10/26 09:00` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-079-3** File (awal), File Handover Photo berformat JPG: File Name `handover-brw0148.jpg` (20 kar), File Format `JPG` (3 kar), Source `Handover Photo` (14 kar), Reference `BRW-2026-0148` (13 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Size `640.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `03/11/26 09:00` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-079-4** Akun (awal), Akun tanpa satu pun file aktif: Jumlah file aktif `0` (1 kar) · sumber turunan penulis
- **DU-079-5** File (awal), File di group lain di luar scope aktor: File Name `warranty-card-scn0003.pdf` (25 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Scanner Epson DS-530 - 3` (24 kar), Asset ID `SCN-2026-0003` (13 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `20/10/26 08:45` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-080-1** File (awal), File Attachment General: File Name `warranty-card-lpt0004.pdf` (25 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `General` (7 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `310.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `28/10/26 09:00` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-080-2** File (awal), File Attachment Purchase: File Name `invoice-lpt0004.pdf` (19 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Reference `Purchase` (8 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `450.2 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `05/11/26 10:15` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-080-3** File (awal), File Custom Field Document: File Name `warranty-card-scn0003.pdf` (25 kar), File Format `PDF` (3 kar), Source `Custom Field Document` (21 kar), Reference `Warranty Card` (13 kar), Asset `Scanner Epson DS-530 - 3` (24 kar), Asset ID `SCN-2026-0003` (13 kar), Group `Branch Bandung` (14 kar), Size `300.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `20/10/26 08:45` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-081-1** File (awal), File JPG di group Head Office: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-081-2** File (awal), File JPEG di group Head Office: File Name `loading-dock.jpeg` (17 kar), File Format `JPEG` (4 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Size `1.1 MB` (6 kar), Uploaded By `Rina A` (6 kar), Upload Date `04/11/26 08:15` (14 kar) · sumber turunan penulis
- **DU-081-3** File (awal), File PNG di group Branch Bandung: File Name `monitor-lg-front.png` (20 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Asset `Monitor LG 24 - 7` (17 kar), Asset ID `MON-2026-0007` (13 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `05/11/26 09:00` (14 kar) · sumber turunan penulis
- **DU-081-4** File (awal), File JPG di group Branch Bandung: File Name `printer-hp-side.jpg` (19 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Printer HP M404 - 1` (19 kar), Asset ID `PRN-2026-0001` (13 kar), Group `Branch Bandung` (14 kar), Size `700.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `06/11/26 10:30` (14 kar) · sumber turunan penulis
- **DU-081-5** File (awal), File PNG di group Branch Surabaya: File Name `scanner-epson-top.png` (21 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Asset `Scanner Epson DS-530 - 3` (24 kar), Asset ID `SCN-2026-0003` (13 kar), Group `Branch Surabaya` (15 kar), Size `512.0 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `07/11/26 11:00` (14 kar) · sumber turunan penulis
- **DU-081-6** File (awal), File JPEG di group Branch Surabaya: File Name `router-cisco-front.jpeg` (23 kar), File Format `JPEG` (4 kar), Source `Asset Photo` (11 kar), Asset `Router Cisco ISR 4331 - 2` (25 kar), Asset ID `RTR-2026-0002` (13 kar), Group `Branch Surabaya` (15 kar), Size `905.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `08/11/26 13:45` (14 kar) · sumber turunan penulis
- **DU-081-7** Akun (awal), Akun tanpa satu pun file aktif: Jumlah file aktif `0` (1 kar) · sumber turunan penulis
- **DU-082-1** File (awal), File JPG di group Head Office: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-082-2** File (awal), File PNG di group Branch Bandung: File Name `monitor-lg-front.png` (20 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Asset `Monitor LG 24 - 7` (17 kar), Asset ID `MON-2026-0007` (13 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `05/11/26 09:00` (14 kar) · sumber turunan penulis
- **DU-082-3** File (awal), File JPG di group Branch Bandung: File Name `printer-hp-side.jpg` (19 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Printer HP M404 - 1` (19 kar), Asset ID `PRN-2026-0001` (13 kar), Group `Branch Bandung` (14 kar), Size `700.0 KB` (8 kar), Uploaded By `Rina A` (6 kar), Upload Date `06/11/26 10:30` (14 kar) · sumber turunan penulis
- **DU-083-1** File (awal), File JPG di group Head Office: File Name `laptop-front.jpg` (16 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Size `820.4 KB` (8 kar), Uploaded By `Budi S` (6 kar), Upload Date `02/11/26 14:30` (14 kar) · sumber PRD §4.1 Files Example Data
- **DU-083-2** File (awal), File PNG di group Branch Bandung: File Name `monitor-lg-front.png` (20 kar), File Format `PNG` (3 kar), Source `Asset Photo` (11 kar), Asset `Monitor LG 24 - 7` (17 kar), Asset ID `MON-2026-0007` (13 kar), Group `Branch Bandung` (14 kar), Size `640.0 KB` (8 kar), Uploaded By `Dodi P` (6 kar), Upload Date `05/11/26 09:00` (14 kar) · sumber turunan penulis
- **DU-083-3** Asset Data (awal), Aset Disposed dengan dokumen Disposal: Name `Printer HP M404 - 1` (19 kar), Asset ID `PRN-2026-0001` (13 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar), Data & Log Size `1.2 MB` (6 kar), Files Size `5.8 MB` (6 kar), Total Size `7.0 MB` (6 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-084-1** File (awal; 23 record), 23 file Asset Photo (tiga halaman): File Name `site-photo-{n}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 1 `Showing 1 to 10 of 23` (21 kar), Laporan halaman 2 `Showing 11 to 20 of 23` (22 kar), Laporan halaman 3 `Showing 21 to 23 of 23` (22 kar) · sumber turunan penulis
- **DU-084-2** File (awal; 11 record), 11 file Asset Photo (satu baris di halaman terakhir): File Name `site-photo-{n}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 2 `Showing 11 to 11 of 11` (22 kar) · sumber turunan penulis
- **DU-084-3** File (awal; 10 record), 10 file Asset Photo (tepat ukuran halaman): File Name `site-photo-{n}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 1 `Showing 1 to 10 of 10` (21 kar) · sumber turunan penulis
- **DU-084-4** File (awal; 26 record), 26 file Asset Photo (melebihi ukuran terpilih 25): File Name `site-photo-{n}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 2 ukuran 10 `Showing 11 to 20 of 26` (22 kar), Laporan halaman 1 ukuran 25 `Showing 1 to 25 of 26` (21 kar), Laporan halaman 2 ukuran 25 `Showing 26 to 26 of 26` (22 kar) · sumber turunan penulis
- **DU-084-5** File (awal; 101 record), 101 file Asset Photo (melebihi ukuran maksimum 100): File Name `site-photo-{n}.jpg` (18 kar), File Format `JPG` (3 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 1 ukuran 100 `Showing 1 to 100 of 101` (23 kar), Laporan halaman 2 ukuran 100 `Showing 101 to 101 of 101` (25 kar) · sumber turunan penulis
- **DU-084-6** File (awal; 12 record), 12 file Attachment cocok dengan kata kunci contract: File Name `contract-{n}.pdf` (16 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Laporan halaman 1 `Showing 1 to 10 of 12` (21 kar), Laporan halaman 2 `Showing 11 to 12 of 12` (22 kar) · sumber turunan penulis
- **DU-084-8** Input nomor halaman (awal), Nomor halaman tidak valid untuk kolom Jump to page: Nol `0` (1 kar), Negatif `-1` (2 kar), Melebihi halaman terakhir `4` (1 kar), Non-angka `abc` (3 kar) · sumber PRD §9.18 (foundation prd-conventions.md)
- **DU-084-7** File (awal; 18 record), 18 file Attachment tidak cocok dengan kata kunci contract: File Name `survey-{n}.pdf` (14 kar), File Format `PDF` (3 kar), Source `Attachment` (10 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-085-1** File (awal; 12 record), 12 file Asset Photo untuk seleksi: File Name `site-photo-{n}.jpg` (18 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar) · sumber turunan penulis
- **DU-085-2** File (awal; 999 record), 999 file Asset Photo (di bawah Selection Limit): File Name `site-photo-{n}.jpg` (18 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar), Tombol Select All `Select All (999 records)` (24 kar) · sumber turunan penulis
- **DU-085-3** File (awal; 1000 record), 1000 file Asset Photo (tepat Selection Limit): File Name `site-photo-{n}.jpg` (18 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar), Tombol Select All `Select All (1000 records)` (25 kar) · sumber turunan penulis
- **DU-085-4** File (awal; 1001 record), 1001 file Asset Photo (melebihi Selection Limit): File Name `site-photo-{n}.jpg` (18 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar), Tombol Select All `Select All (1001 records)` (25 kar), Toast batas `Error, only the first 1000 of 1001 rows were selected. Narrow your filter to include the rest.` (94 kar) · sumber turunan penulis
- **DU-085-5** File (awal; 1200 record), 1200 file Asset Photo cocok dengan kata kunci survey: File Name `survey-{n}.jpg` (14 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar), Tombol Select All `Select All (1200 records)` (25 kar), Toast batas `Error, only the first 1000 of 1200 rows were selected. Narrow your filter to include the rest.` (94 kar) · sumber turunan penulis
- **DU-085-7** Kata kunci Search (awal), Kata kunci Search untuk menyempitkan atau menyembunyikan baris terpilih: Cocok 1200 file `survey` (6 kar), Hanya cocok file ke-12 `site-photo-12` (13 kar) · sumber turunan penulis
- **DU-085-6** File (awal; 300 record), 300 file Asset Photo tidak cocok dengan kata kunci survey: File Name `site-photo-{n}.jpg` (18 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Source `Asset Photo` (11 kar), File Format `JPG` (3 kar), Upload Date `menurun menurut n (file ke-1 paling baru)` (41 kar) · sumber turunan penulis
- **DU-086-1** Asset Data (awal), Aset Disposed dengan ukuran yang dibulatkan: Name `Printer HP M404 - 1` (19 kar), Asset ID `PRN-2026-0001` (13 kar), Group `Branch Bandung` (14 kar), Status `Disposed` (8 kar), Alias Name `Printer Lantai 2` (16 kar), Brand `HP` (2 kar), Model / Type `LaserJet M404n` (14 kar), Category `Printer` (7 kar), Division `Operasional` (11 kar), Register Date `2026-03-15` (10 kar), Last Scanned `2026-10-30` (10 kar), Data & Log Size (byte) `1258291` (7 kar), Files Size (byte) `6081741` (7 kar), Total Size (byte) `7340032` (7 kar), Photo `foto-printer-hp-m404.jpg` (24 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-086-2** Asset Data (awal), Aset Unmanaged tanpa foto dengan kolom Curated kosong: Name `Scanner Epson DS-530 - 3` (24 kar), Asset ID `SCN-2026-0003` (13 kar), Group `Branch Bandung` (14 kar), Status `Unmanaged` (9 kar), Alias Name `None` (4 kar), TAG `None` (4 kar), Brand `Epson` (5 kar), Model / Type `DS-530` (6 kar), Category `Scanner` (7 kar), Division `None` (4 kar), Register Date `2026-02-10` (10 kar), Last Scanned `None` (4 kar), Data & Log Size (byte) `215040` (6 kar), Files Size (byte) `307200` (6 kar), Total Size (byte) `522240` (6 kar), Photo `None` (4 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-086-3** Asset Data (awal), Aset Unmanaged tanpa file, ukuran file nol: Name `Monitor LG 24 - 7` (17 kar), Asset ID `MON-2026-0007` (13 kar), Group `Head Office` (11 kar), Status `Unmanaged` (9 kar), Alias Name `Monitor Meja Resepsionis` (24 kar), TAG `None` (4 kar), Brand `None` (4 kar), Model / Type `None` (4 kar), Category `Monitor` (7 kar), Division `Umum` (4 kar), Register Date `2026-01-20` (10 kar), Last Scanned `2026-09-12` (10 kar), Data & Log Size (byte) `421888` (6 kar), Files Size (byte) `0` (1 kar), Total Size (byte) `421888` (6 kar), Photo `foto-monitor-lg-24.jpg` (22 kar) · sumber PRD §4.1 Asset Data Example Data
- **DU-086-4** Asset Data (awal), Aset Disposed dengan nama Group dan Category panjang serta ukuran di atas 1.000 GB: Name `Server Rack Dell PowerEdge R740 - 2` (35 kar), Asset ID `SRV-2026-0002` (13 kar), Group `Jakarta Selatan Distribution Center` (35 kar), Status `Disposed` (8 kar), Alias Name `Server Pusat Data` (17 kar), TAG `None` (4 kar), Brand `Dell` (4 kar), Model / Type `PowerEdge R740` (14 kar), Category `Environmental Monitoring Equipment` (34 kar), Division `Infrastruktur` (13 kar), Register Date `2025-06-01` (10 kar), Last Scanned `2026-08-05` (10 kar), Data & Log Size (byte) `858993459200` (12 kar), Files Size (byte) `790273982464` (12 kar), Total Size (byte) `1649267441664` (13 kar), Photo `foto-server-r740.jpg` (20 kar), Category Hierarchy `Sensors > Environmental Monitoring Equipment` (44 kar) · sumber turunan penulis
- **DU-086-5** Asset Data (awal), Aset Disposed dengan Group berhierarki: Name `Access Point Cisco 9120 - 4` (27 kar), Asset ID `APT-2026-0004` (13 kar), Group `Server Room` (11 kar), Group Hierarchy `Jakarta Office > Floor 2 > Server Room` (38 kar), Status `Disposed` (8 kar), Alias Name `AP Ruang Server` (15 kar), TAG `None` (4 kar), Brand `Cisco` (5 kar), Model / Type `Catalyst 9120` (13 kar), Category `Network Device` (14 kar), Division `Infrastruktur` (13 kar), Register Date `2025-11-03` (10 kar), Last Scanned `2026-07-18` (10 kar), Data & Log Size (byte) `524288` (6 kar), Files Size (byte) `1048576` (7 kar), Total Size (byte) `1572864` (7 kar), Photo `foto-ap-cisco-9120.jpg` (22 kar) · sumber turunan penulis
- **DU-086-6** Asset Data (awal), Aset Unmanaged di luar scope group aktor: Name `Router Mikrotik RB4011 - 1` (26 kar), Asset ID `RTR-2026-0001` (13 kar), Group `Branch Surabaya` (15 kar), Status `Unmanaged` (9 kar), Scope Group Aktor `Head Office, Branch Bandung, Jakarta Selatan Distribution Center, Server Room` (77 kar) · sumber turunan penulis
- **DU-086-7** Asset Data (awal), Entitas tanpa aset Disposed maupun Unmanaged: Aset Disposed `tidak ada` (9 kar), Aset Unmanaged `tidak ada` (9 kar) · sumber S-27a
- **DU-086-8** Search Keyword (dicoba), Kata kunci Search yang tidak cocok dengan baris mana pun: Search `Rak Gudang Timur` (16 kar) · sumber S-27b
- **DU-086-9** Asset Data (awal), Aset Disposed dengan TAG terpasang serta Brand dan Model / Type panjang: Name `Server HPE ProLiant DL380 - 5` (29 kar), Asset ID `SRV-2026-0005` (13 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar), Alias Name `Server Cadangan` (15 kar), TAG `RFID` (4 kar), Brand `Hewlett Packard Enterprise Company` (34 kar), Model / Type `ProLiant DL380 Gen10 Plus Rackmount` (35 kar), Category `Network Device` (14 kar), Division `Infrastruktur` (13 kar), Register Date `2026-04-02` (10 kar), Last Scanned `2026-10-30` (10 kar), Data & Log Size (byte) `1048576` (7 kar), Files Size (byte) `2097152` (7 kar), Total Size (byte) `3145728` (7 kar), Photo `foto-server-hpe-dl380.jpg` (25 kar) · sumber turunan penulis
- **DU-087-1** File Recycle Bin (awal), File aktif dihapus otomatis oleh System: File Name `laptop-old.png` (14 kar), File Format `PNG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Size (byte) `1048576` (7 kar), Deleted Date `2026-11-02 14:30` (16 kar), Deleted By `System` (6 kar), Batas Purge `T0 + 28 hari 12 jam` (19 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-087-2** File Recycle Bin (awal), File dihapus manual di group yang aktor hanya Read, pelaku dua kata: File Name `damage-01.jpg` (13 kar), File Format `JPG` (3 kar), Category `Damaged` (7 kar), Source `Damaged Photo` (13 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Branch Bandung` (14 kar), Size (byte) `921600` (6 kar), Deleted Date `2026-11-01 10:00` (16 kar), Deleted By `Rina Anggraini` (14 kar), Batas Purge `T0 + 27 hari 6 jam` (18 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-087-3** File Recycle Bin (awal), File dengan batas purge dalam 24 jam: File Name `maint-before-0031.jpg` (21 kar), File Format `JPG` (3 kar), Category `Maintenance` (11 kar), Source `Maintenance Before Photo` (24 kar), Asset `Printer HP M404 - 1` (19 kar), Group `Branch Bandung` (14 kar), Size (byte) `768000` (6 kar), Deleted Date `2026-10-05 09:00` (16 kar), Deleted By `Rina Anggraini` (14 kar), Batas Purge `T0 + 18 jam` (11 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-087-4** File Recycle Bin (awal), File dengan batas purge sudah lewat: File Name `repair-02.jpg` (13 kar), File Format `JPG` (3 kar), Category `Damaged` (7 kar), Source `Repair Photo` (12 kar), Asset `Toyota Avanza - 2` (17 kar), Group `Branch Bandung` (14 kar), Size (byte) `901120` (6 kar), Deleted Date `2026-10-04 16:00` (16 kar), Deleted By `Dodi Pratama` (12 kar), Batas Purge `T0 - 2 jam` (10 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-087-5** File Recycle Bin (awal; dimutasi TC-FA-FAFM-UI-087-dialog-recycle-bin-tampilan-dan-state), File Draft tanpa aset, pelaku satu kata, satu-satunya file di bin: File Name `draft-photo-01.jpg` (18 kar), File Format `JPG` (3 kar), Category `Asset Photo` (11 kar), Source `Asset Photo` (11 kar), Asset `None` (4 kar), Group `Head Office` (11 kar), Size (byte) `655360` (6 kar), Deleted Date `2026-11-10 08:15` (16 kar), Deleted By `Budi` (4 kar), Batas Purge `T0 + 29 hari 20 jam` (19 kar) · sumber turunan penulis
- **DU-087-6** File Recycle Bin (awal), File dihapus oleh pengguna bernama tiga kata: File Name `calibration-cert.pdf` (20 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Attachment` (10 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar), Group `Fleet` (5 kar), Size (byte) `317440` (6 kar), Deleted Date `2026-10-20 13:45` (16 kar), Deleted By `Alexander Graham Bell` (21 kar), Batas Purge `T0 + 10 hari 3 jam` (18 kar), Group Hierarchy `Head Office > Fleet` (19 kar) · sumber turunan penulis
- **DU-087-7** File Recycle Bin (awal), File dihapus oleh pengguna dengan nama depan panjang: File Name `warranty-card-mon0007.pdf` (25 kar), File Format `PDF` (3 kar), Category `Asset Documents` (15 kar), Source `Custom Field Document` (21 kar), Asset `Monitor LG 24 - 7` (17 kar), Group `Head Office` (11 kar), Size (byte) `307200` (6 kar), Deleted Date `2026-10-18 09:10` (16 kar), Deleted By `Buzzlightyear Sumardi` (21 kar), Batas Purge `T0 + 8 hari 1 jam` (17 kar) · sumber turunan penulis
- **DU-087-8** File Recycle Bin (awal), File dihapus oleh pengguna bernama mirip (Dewi Anggraini): File Name `handover-brw0150.jpg` (20 kar), File Format `JPG` (3 kar), Category `Borrow` (6 kar), Source `Handover Photo` (14 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar), Group `Head Office` (11 kar), Size (byte) `655360` (6 kar), Deleted Date `2026-10-22 11:20` (16 kar), Deleted By `Dewi Anggraini` (14 kar), Batas Purge `T0 + 12 hari 5 jam` (18 kar) · sumber turunan penulis
- **DU-087-9** File Recycle Bin (awal), File dihapus oleh pengguna bernama mirip (Dewi Anggreni): File Name `handover-brw0151.jpg` (20 kar), File Format `JPG` (3 kar), Category `Borrow` (6 kar), Source `Handover Photo` (14 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar), Group `Head Office` (11 kar), Size (byte) `675840` (6 kar), Deleted Date `2026-10-22 11:40` (16 kar), Deleted By `Dewi Anggreni` (13 kar), Batas Purge `T0 + 12 hari 5 jam` (18 kar) · sumber turunan penulis
- **DU-087-10** Daftar Recycle Bin (awal), Entitas tanpa file terhapus: File di Recycle Bin `tidak ada` (9 kar) · sumber S-28a
- **DU-087-11** File Recycle Bin (awal), File di group luar cakupan Read aktor: File Name `old-label.png` (13 kar), Group `Branch Surabaya` (15 kar), Scope Read Aktor `Branch Bandung, Head Office beserta descendant` (46 kar) · sumber turunan penulis
- **DU-087-12** Search Keyword (dicoba), Kata kunci Search yang tidak cocok dengan baris mana pun: Search `foto-tidak-ada.png` (18 kar) · sumber S-28b
- **DU-088-1** Entri Changelog (awal), Entri auto-purge oleh System: Date `2026-11-14 02:00` (16 kar), Action `Permanently Delete` (18 kar), File Name `old-label.png` (13 kar), Field `File Name` (9 kar), Old Value `old-label.png` (13 kar), New Value `None` (4 kar), Modified By `System` (6 kar) · sumber PRD §4.1 Changelog Example Data
- **DU-088-2** Entri Changelog (awal), Entri soft-delete manual, pelaku dua kata: Date `2026-11-01 10:00` (16 kar), Action `Delete` (6 kar), File Name `damage-01.jpg` (13 kar), Field `File Name` (9 kar), Old Value `damage-01.jpg` (13 kar), New Value `None` (4 kar), Modified By `Rina Anggraini` (14 kar) · sumber PRD §4.1 Changelog Example Data
- **DU-088-3** Entri Changelog (awal), Entri dengan pelaku bernama tiga kata: Date `2026-10-20 13:45` (16 kar), Action `Delete` (6 kar), File Name `calibration-cert.pdf` (20 kar), Field `File Name` (9 kar), Old Value `calibration-cert.pdf` (20 kar), New Value `None` (4 kar), Modified By `Alexander Graham Bell` (21 kar) · sumber turunan penulis
- **DU-088-4** Entri Changelog (awal), Entri dengan pelaku bernama depan panjang: Date `2026-10-18 09:10` (16 kar), Action `Delete` (6 kar), File Name `warranty-card-mon0007.pdf` (25 kar), Field `File Name` (9 kar), Old Value `warranty-card-mon0007.pdf` (25 kar), New Value `None` (4 kar), Modified By `Buzzlightyear Sumardi` (21 kar) · sumber turunan penulis
- **DU-088-5** Entri Changelog (awal), Entri dengan pelaku satu kata: Date `2026-11-10 08:15` (16 kar), Action `Delete` (6 kar), File Name `draft-photo-01.jpg` (18 kar), Field `File Name` (9 kar), Old Value `draft-photo-01.jpg` (18 kar), New Value `None` (4 kar), Modified By `Budi` (4 kar) · sumber turunan penulis
- **DU-088-6** Entri Changelog (awal), Entri dengan pelaku bernama mirip (Dewi Anggraini): Date `2026-10-22 11:20` (16 kar), Action `Delete` (6 kar), File Name `handover-brw0150.jpg` (20 kar), Field `File Name` (9 kar), Old Value `handover-brw0150.jpg` (20 kar), New Value `None` (4 kar), Modified By `Dewi Anggraini` (14 kar) · sumber turunan penulis
- **DU-088-7** Entri Changelog (awal), Entri dengan pelaku bernama mirip (Dewi Anggreni): Date `2026-10-22 11:40` (16 kar), Action `Delete` (6 kar), File Name `handover-brw0151.jpg` (20 kar), Field `File Name` (9 kar), Old Value `handover-brw0151.jpg` (20 kar), New Value `None` (4 kar), Modified By `Dewi Anggreni` (13 kar) · sumber turunan penulis
- **DU-088-8** Daftar Changelog (awal), Entitas tanpa file sama sekali: File di entitas `tidak ada` (9 kar), Entri Changelog `tidak ada` (9 kar) · sumber S-29a
- **DU-088-9** Daftar Changelog (awal), Entitas punya file tetapi belum ada Delete atau Permanently Delete tercatat: File di entitas `laptop-front.jpg` (16 kar), Entri Changelog `tidak ada` (9 kar) · sumber S-29a
- **DU-088-10** Entri Changelog (awal), Entri atas file kelompok Purchase yang tidak terlihat oleh role aktor: Date `2026-11-05 10:15` (16 kar), Action `Delete` (6 kar), File Name `invoice-lpt0004.pdf` (19 kar), Field `File Name` (9 kar), Old Value `invoice-lpt0004.pdf` (19 kar), New Value `None` (4 kar), Modified By `Budi Santoso` (12 kar) · sumber turunan penulis
- **DU-088-11** Search Keyword (dicoba), Kata kunci Search yang tidak cocok dengan baris mana pun: Search `log-tidak-ada.png` (17 kar) · sumber S-29b
- **DU-089-1** File (awal), File Asset Photo yang dihapus single: File Name `laptop-front.jpg` (16 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar) · sumber PRD §4.1 Files Example Data
- **DU-089-2** File (awal), File Asset Photo kedua: File Name `monitor-lg-24.jpg` (17 kar), Source `Asset Photo` (11 kar), Asset `Monitor LG 24 - 7` (17 kar) · sumber turunan penulis
- **DU-089-3** File (awal), File Asset Photo ketiga: File Name `printer-hp-m404.jpg` (19 kar), Source `Asset Photo` (11 kar), Asset `Printer HP M404 - 1` (19 kar) · sumber turunan penulis
- **DU-089-4** File (awal; 7 record), Tujuh file Asset Photo untuk memenuhi 10 baris dan daftar bulk yang digulir: File Name `inventaris-{n}.jpg` (18 kar), Source `Asset Photo` (11 kar), Asset `Toyota Avanza - {n}` (19 kar) · sumber turunan penulis
- **DU-090-1** File di Recycle Bin (awal), File di Recycle Bin yang dihapus permanen single: File Name `laptop-old.png` (14 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar) · sumber PRD §4.1 Recycle Bin Example Data
- **DU-090-2** File di Recycle Bin (awal), File di Recycle Bin kedua: File Name `damage-01.jpg` (13 kar), Source `Damaged Photo` (13 kar), Asset `Toyota Avanza - 2` (17 kar) · sumber turunan penulis
- **DU-090-3** File di Recycle Bin (awal), File di Recycle Bin ketiga: File Name `calibration-cert.pdf` (20 kar), Source `Attachment` (10 kar), Asset `Laptop Dell Latitude 5420 - 9` (29 kar) · sumber turunan penulis
- **DU-090-4** File di Recycle Bin (awal; 7 record), Tujuh file di Recycle Bin untuk memenuhi 10 baris dan daftar bulk yang digulir: File Name `arsip-{n}.jpg` (13 kar), Source `Asset Photo` (11 kar), Asset `Toyota Avanza - {n}` (19 kar) · sumber turunan penulis
- **DU-091-1** File (awal), File Asset Photo yang diunduh single: File Name `laptop-front.jpg` (16 kar), Source `Asset Photo` (11 kar), Asset `Laptop Dell Latitude 5420 - 4` (29 kar) · sumber PRD §4.1 Files Example Data
- **DU-091-2** File (awal), File Asset Photo kedua: File Name `monitor-lg-24.jpg` (17 kar), Source `Asset Photo` (11 kar), Asset `Monitor LG 24 - 7` (17 kar) · sumber turunan penulis
- **DU-091-3** File (awal), File Asset Photo ketiga: File Name `printer-hp-m404.jpg` (19 kar), Source `Asset Photo` (11 kar), Asset `Printer HP M404 - 1` (19 kar) · sumber turunan penulis
- **DU-091-4** Volume Download (awal), Jumlah baris hasil tepat di bawah ambang Download: Jumlah baris `4999` (4 kar) · sumber turunan penulis
- **DU-091-5** Volume Download (awal), Jumlah baris hasil tepat di ambang Download: Jumlah baris `5000` (4 kar) · sumber turunan penulis
- **DU-091-6** Volume Download (awal), Jumlah baris hasil tepat di atas ambang Download: Jumlah baris `5001` (4 kar) · sumber turunan penulis
- **DU-092-1** Akun (awal), Akun yang belum pernah membuka halaman File Manager: Flag `belum diset` (11 kar) · sumber turunan penulis
- **DU-092-2** Akun (awal), Akun yang sudah pernah menyelesaikan atau melewati tur: Flag `true` (4 kar) · sumber turunan penulis
- **DU-092-3** Ukuran Jendela (dicoba), Lebar jendela browser setelah diubah: Lebar jendela (piksel) `800` (3 kar) · sumber turunan penulis
