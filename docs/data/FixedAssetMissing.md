<!-- Ditulis stage spec-from-prd saat close. Jangan diubah tangan: run berikutnya menimpanya. -->

Suite: `specs/FixedAsset/Missing`. Sumber: PRD `fixed-asset@ea04860` (sha `db4637b30cc75d5d`), foundation@757d6be, kontrak komponen wangs-ui@1.0.0. Stage: `prd-harness@963b2f8`, ditutup 2026-11-23T11:54:41Z.

# Matriks data Missing (e27e3e782b16dacd)

- Entri: 1004 (awal 789, dibuat 141, dicoba 74)
- Checker: ERROR 0, REVIEW 114

## Target × varian

✓ entri yang memenuhi, ✗ belum ada entri, — tidak berlaku beserta alasannya.

### What happened@report-missing · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-054-13, DU-073-18 |
| `spasi-saja` | ✓ DU-054-14, DU-073-19 |
| `pilihan-kosong` | — §9.9 FLD-01: Textarea, bukan pilihan |
| `berkas-kosong` | — §9.9 FLD-01: Textarea, bukan berkas |

### What happened@report-missing · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-054-16, DU-073-20 |
| `lebih-maks` | ✓ DU-054-17, DU-073-21 |
| `batas-min` | ✓ DU-054-15 |
| `batas-maks-spasi-tepi` | ✓ DU-054-18 |
| `batas-maks-spasi-tengah` | ✓ DU-054-19 |
| `batas-maks-unicode` | ✓ DU-054-20 |
| `kurang-min` | — §9.9 FLD-01: min 1 karakter, kurang dari min sama dengan kosong (VD-F1) |
| `addon-tidak-dihitung` | — §9.9 FLD-01: tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9 FLD-01: field wajib |

### What happened@report-missing · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-054-21, DU-054-22 |
| `batch-stay-on-form` | — §4.2.3: dialog tanpa checkbox Stay on this form |
| `semua-tipe-kontrol-terisi` | — §4.2.3: hanya satu isian Textarea |

### Reason@reject-report · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-056-2, DU-073-22 |
| `spasi-saja` | ✓ DU-056-3, DU-073-23 |
| `pilihan-kosong` | — §9.9 FLD-07: Textarea |
| `berkas-kosong` | — §9.9 FLD-07: Textarea |

### Reason@reject-report · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-056-5, DU-073-24 |
| `lebih-maks` | ✓ DU-056-6, DU-073-25 |
| `batas-min` | ✓ DU-056-4 |
| `batas-maks-spasi-tepi` | ✓ DU-056-7 |
| `batas-maks-spasi-tengah` | ✓ DU-056-8 |
| `batas-maks-unicode` | ✓ DU-056-9 |
| `kurang-min` | — §9.9 FLD-07: min 1 sama dengan kosong |
| `addon-tidak-dihitung` | — §9.9 FLD-07: tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9 FLD-07: field wajib |

### Update@add-update · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-057-3, DU-073-26 |
| `spasi-saja` | ✓ DU-057-4, DU-073-27 |
| `pilihan-kosong` | — §9.9 FLD-08: Textarea |
| `berkas-kosong` | — §9.9 FLD-08: Textarea |

### Update@add-update · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-057-6, DU-073-28 |
| `lebih-maks` | ✓ DU-057-7, DU-073-29 |
| `batas-min` | ✓ DU-057-5 |
| `batas-maks-spasi-tepi` | ✓ DU-057-8 |
| `batas-maks-spasi-tengah` | ✓ DU-057-9 |
| `batas-maks-unicode` | ✓ DU-057-10 |
| `kurang-min` | — §9.9 FLD-08: min 1 sama dengan kosong |
| `addon-tidak-dihitung` | — §9.9 FLD-08: tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9 FLD-08: field wajib |

### Note@mark-as-found · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-055-13, DU-073-32 |
| `lebih-maks` | ✓ DU-055-14, DU-073-33 |
| `batas-min` | ✓ DU-055-12 |
| `batas-maks-spasi-tepi` | ✓ DU-055-15 |
| `batas-maks-spasi-tengah` | ✓ DU-055-16 |
| `batas-maks-unicode` | ✓ DU-055-17 |
| `opsional-kosong-tanpa-min` | ✓ DU-055-18 |
| `kurang-min` | — §9.9 FLD-05: min 1 saat Damaged sama dengan kosong (VD-F1) |
| `addon-tidak-dihitung` | — §9.9 FLD-05: tanpa addon |

### Note@mark-as-found · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-055-10, DU-073-30 |
| `spasi-saja` | ✓ DU-055-11, DU-073-31 |
| `pilihan-kosong` | — §9.9 FLD-05: Textarea |
| `berkas-kosong` | — §9.9 FLD-05: Textarea |

### Damaged Photo@mark-as-found · VD-F1

| Varian | Entri |
|---|---|
| `berkas-kosong` | ✓ DU-055-19 |
| `kosong` | — §9.9 FLD-06: berkas, bukan teks |
| `spasi-saja` | — §9.9 FLD-06: berkas |
| `pilihan-kosong` | — §9.9 FLD-06: berkas |

### Damaged Photo@mark-as-found · VD-F12

| Varian | Entri |
|---|---|
| `per-format-izin:PNG` | ✓ DU-055-20 |
| `per-format-izin:JPG` | ✓ DU-055-21 |
| `per-format-izin:JPEG` | ✓ DU-055-22 |
| `ukuran-di-bawah` | ✓ DU-055-21 |
| `berkas-valid-field-lain-invalid` | ✓ DU-055-21 |
| `unggah-lalu-batal` | ✓ DU-055-20 |
| `format-tolak` | — §9.9#p4: picker hanya menerima PNG / JPG / JPEG sehingga tidak ada pesan format salah |
| `ukuran-tepat-batas` | — §9.9#p4: file lebih dari 1 MB di-resize otomatis tanpa pesan; batas bukan penolakan |
| `ukuran-lebih-batas` | — §9.9#p4: di-resize otomatis tanpa pesan error, hasil resize tidak teramati |
| `satu-foto-auto-default` | — §9.9 FLD-06: satu foto tanpa slot default |
| `default-di-slot-dua` | — §9.9 FLD-06: satu foto |
| `ganti-berkas-edit` | — §9.6#p2: tidak ada form edit |
| `hapus-record-berberkas` | — §10#r5: record tidak dapat dihapus |

### Found at@mark-as-found · VD-F14

| Varian | Entri |
|---|---|
| `pilih-satu` | ✓ DU-055-6 |
| `default-terpilih` | ✓ DU-055-1 |
| `item-default-wajib-ada` | ✓ DU-055-2 |
| `dalam-scope` | ✓ DU-055-4 |
| `luar-scope` | ✓ DU-055-4 |
| `opsi-belum-dipakai` | — §9.9 FLD-03: Found at hanya data, bukan relasi pemakaian |
| `opsi-banyak` | — §9.9 FLD-03: tree, bukan daftar datar; cakupan diuji lewat dalam-scope/luar-scope |
| `pilih-banyak` | — §4.2.4#p7: single-select |
| `sumber-kosong` | — §9.9 FLD-03: Group aset itu sendiri selalu tampil |
| `opsi-nonaktif` | — §9.9 FLD-03: PRD tidak menyebut Group nonaktif |
| `opsi-tidak-boleh-ada` | — §9.9 FLD-03: node induk tampil tetapi tidak dapat dipilih (dicakup pilih-satu pada node induk) |
| `per-tipe-entitas` | — §9.9 FLD-03: satu tipe (Group) |
| `nama-sama-beda-tipe` | — §9.9 FLD-03: satu tipe |
| `aktor-scope-satu-tipe` | — §9.9 FLD-03: satu tipe |
| `opsi-dari-master` | — §9.9 FLD-03: opsi adalah Group dalam cakupan aktor (dicakup dalam-scope) |

### Asset Status@mark-as-found · VD-F6

| Varian | Entri |
|---|---|
| `default-tak-disentuh` | ✓ DU-055-7 |
| `per-opsi:Normal` | ✓ DU-055-7 |
| `per-opsi:Damaged` | ✓ DU-055-8 |
| `pasangan-berinteraksi` | ✓ DU-055-8 |
| `terisi` | — §9.9 FLD-04: Select tanpa nilai kosong (dicakup per-opsi) |
| `kosong` | — §9.9 FLD-04: selalu terisi (default Normal) |

### Note dan Photo@mark-as-found · VD-F15

| Varian | Entri |
|---|---|
| `pemicu-tampil` | ✓ DU-055-8 |
| `pemicu-sembunyi` | ✓ DU-055-7 |
| `per-cabang-pemicu:Normal` | ✓ DU-055-7 |
| `per-cabang-pemicu:Damaged` | ✓ DU-055-8 |
| `ganti-pemicu-setelah-isi` | ✓ DU-055-9 |

### Scan TAG@mark-as-found · VD-F13

| Varian | Entri |
|---|---|
| `tag-paired-aset` | ✓ DU-073-11 |
| `tag-tidak-terdaftar` | ✓ DU-073-13 |
| `tag-bukan-tagsamurai` | ✓ DU-073-14 |
| `tag-missing` | ✓ DU-073-12 |
| `aset-missing` | ✓ DU-073-6 |
| `tag-belum-paired` | — §9.9#p3: TAG yang belum dipasang tidak dihitung; hasil tidak dinyatakan selain `tag-tidak-terdaftar` |
| `tag-paired-user-lain` | — §9.9 FLD-02: tidak ada TAG milik user |
| `object-tag` | — §9.9: PRD tidak menyebut object TAG |
| `tag-company-lain` | — §6#p3: diperlakukan sebagai tidak terdaftar di client (dicakup tag-tidak-terdaftar) |
| `tag-belum-diaktivasi` | — §9.9: PRD tidak menyebut aktivasi TAG |
| `tag-damaged` | — §9.9: PRD tidak membedakan TAG rusak saat scan |
| `group-found-sama` | — §9.9 FLD-02: Found at bukan hasil scan |
| `group-found-beda` | — §9.9 FLD-02: Found at bukan hasil scan |
| `aset-on-tracking` | — §9.9: PRD tidak menyebut aset on tracking |
| `per-jenis-tag` | — §9.10: tipe TAG hanya memengaruhi kunci plan, bukan hasil scan |

### kolom-searchable@tabel-active · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:teks` | ✓ DU-002-2 |
| `per-kelas-kolom:badge` | ✓ DU-002-2 |
| `per-kelas-kolom:kode` | ✓ DU-002-2 |
| `per-kelas-kolom:ikon` | ✓ DU-002-2 |
| `substring-tengah` | ✓ DU-002-9 |
| `beda-kapital` | ✓ DU-002-10 |
| `tanpa-hasil` | ✓ DU-002-15 |
| `kolom-non-searchable` | ✓ DU-002-2 |
| `kolom-tersembunyi` | ✓ DU-002-2 |
| `lintas-kolom` | ✓ DU-002-3 |
| `kolom-icon-label` | ✓ DU-002-2 |
| `karakter-pola` | ✓ DU-002-5, DU-002-6, DU-002-16 |
| `query-spasi-tepi` | ✓ DU-002-11 |
| `query-spasi-saja` | ✓ DU-002-12 |
| `query-spasi-tengah` | ✓ DU-002-7, DU-002-13 |
| `query-kata-tidak-bersebelahan` | ✓ DU-002-8, DU-002-14 |
| `nilai-substring-nilai-lain` | — §4.1a Status T-MIS-01: tidak ada nilai badge yang menjadi substring nilai lain |
| `record-tab-non-default` | — §4.4#r1: Search terisolasi per tab, tanpa Search global |
| `cocok-di-anak-saja` | — §4.1a: tidak ada tree di tabel |
| `kolom-homogen` | — §4.1a: PRD tidak menetapkan kolom bernilai seragam |

### kolom-searchable@tabel-history · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:teks` | ✓ DU-008-3 |
| `per-kelas-kolom:badge` | ✓ DU-008-3 |
| `substring-tengah` | ✓ DU-008-6 |
| `beda-kapital` | ✓ DU-008-7 |
| `tanpa-hasil` | ✓ DU-008-8 |
| `kolom-non-searchable` | ✓ DU-008-3 |
| `nilai-substring-nilai-lain` | — §4.1b Status: Found, Disposed, Rejected, Canceled saling bukan substring |
| `record-tab-non-default` | — §4.4#r1: Search per tab |
| `cocok-di-anak-saja` | — §4.1b: tanpa tree |
| `kolom-homogen` | — §4.1b: tidak ditetapkan |
| `kolom-icon-label` | — VD-2: mekanik tabel diuji di tabel pertama; kolom TAG sama dengan T-MIS-01 |
| `karakter-pola` | — VD-2: diuji di T-MIS-01 |
| `query-spasi-tepi` | — VD-2: diuji di T-MIS-01 |
| `query-spasi-saja` | — VD-2: diuji di T-MIS-01 |
| `query-spasi-tengah` | — VD-2: diuji di T-MIS-01 |
| `query-kata-tidak-bersebelahan` | — VD-2: diuji di T-MIS-01 |
| `kolom-tersembunyi` | — EB-SRC-5 berlaku hanya di tabel-active (EB-6) |
| `lintas-kolom` | — VD-2: diuji di T-MIS-01 |

### sort@tabel-active · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-003-6 |
| `sama-tiebreak` | ✓ DU-003-10, DU-003-13 |
| `kosong` | ✓ DU-003-9, DU-003-11 |
| `beda-kapital` | ✓ DU-003-6, DU-003-7 |
| `natural` | ✓ DU-003-14 |
| `per-tipe-kolom:tanggal` | ✓ DU-003-12 |
| `per-tipe-kolom:badge` | ✓ DU-003-10 |
| `per-tipe-kolom:icon-only` | ✓ DU-003-12 |
| `per-tipe-kolom:currency` | ✓ DU-003-6 |
| `aksen` | ✓ DU-003-8, DU-003-9 |
| `diawali-angka-simbol` | ✓ DU-003-11, DU-003-12 |
| `default-beda` | ✓ DU-003-10, DU-003-13 |
| `sisip-beda-default` | ✓ DU-003-14 |
| `lintas-halaman` | ✓ DU-003-14 |
| `sama-melintasi-halaman` | ✓ DU-003-14 |
| `sama-di-kolom-dan-default` | ✓ DU-003-8, DU-003-9 |
| `jumlah-chip-sama` | ✓ DU-003-12 |
| `format-komposit` | ✓ DU-003-14 |
| `urutan-beda-antar-kolom` | ✓ DU-003-7 |
| `urutan-custom` | — §4.1a Status: Alphabetical by label, bukan urutan lifecycle |
| `jumlah-aktif-sama` | — §4.1a: tidak ada kolom multi-boolean |
| `campuran-tipe` | — §4.1a: tidak ada kolom Old/New Value |
| `nama-tampil-beda-nama-penuh` | — §4.1a Last Holder: sort Alphabetical atas nama tampil; tie dipecah default sort (dicakup sama-tiebreak) |

### sort@tabel-history · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-009-6, DU-009-10 |
| `sama-tiebreak` | ✓ DU-009-8, DU-009-9 |
| `kosong` | ✓ DU-009-7 |
| `per-tipe-kolom:tanggal` | ✓ DU-009-6 |
| `default-beda` | ✓ DU-009-7 |
| `beda-kapital` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `natural` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `aksen` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `diawali-angka-simbol` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `lintas-halaman` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `sama-melintasi-halaman` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `jumlah-chip-sama` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `jumlah-aktif-sama` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `campuran-tipe` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `format-komposit` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `nama-tampil-beda-nama-penuh` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `urutan-custom` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `urutan-beda-antar-kolom` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `sama-di-kolom-dan-default` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |
| `sisip-beda-default` | — VD-2: mekanik sort diuji di T-MIS-01; T-MIS-02 hanya kolom yang lahir dari tabelnya (Duration, Resolved Date) |

### filter@tabel-active · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-004-8 |
| `tidak-cocok` | ✓ DU-004-11 |
| `and-a-saja` | ✓ DU-004-10 |
| `and-b-saja` | ✓ DU-004-11 |
| `and-keduanya` | ✓ DU-004-8, DU-004-9 |
| `and-tidak-keduanya` | ✓ DU-004-7 |
| `or-dalam-field` | ✓ DU-004-8 |
| `search-saja` | ✓ DU-004-11 |
| `filter-saja` | ✓ DU-004-9 |
| `search-dan-filter` | ✓ DU-004-8 |
| `irisan-kosong` | ✓ DU-004-12 |
| `kolom-tersembunyi` | ✓ DU-004-8 |
| `filter-only` | ✓ DU-004-10 |
| `rentang-dalam` | ✓ DU-004-22, DU-004-32 |
| `rentang-luar` | ✓ DU-004-25 |
| `rentang-tepat-awal` | ✓ DU-004-23 |
| `rentang-tepat-akhir` | ✓ DU-004-23 |
| `rentang-sehari` | ✓ DU-004-24 |
| `range-tepat-min` | ✓ DU-004-28 |
| `range-tepat-max` | ✓ DU-004-28 |
| `range-hanya-min` | ✓ DU-004-29 |
| `range-hanya-max` | ✓ DU-004-30 |
| `range-min-lebih-max` | ✓ DU-004-31 |
| `per-kelas-kontrol:multi-select` | ✓ DU-004-8 |
| `per-kelas-kontrol:tree picker` | ✓ DU-004-12 |
| `per-kelas-kontrol:date range` | ✓ DU-004-22 |
| `per-kelas-kontrol:numeric range` | ✓ DU-004-28 |
| `per-kelas-kontrol:checkbox` | ✓ DU-004-10 |
| `mutasi-keluar-saringan` | ✓ DU-004-13 |
| `mutasi-masuk-saringan` | ✓ DU-004-14 |
| `custom-field-per-tipe` | — §4.1a: tidak ada custom field |
| `status-dikecualikan` | — §4.1a#p1: semua status berjalan tersaring lewat filter Status |
| `default-filter-lolos` | — §9.5#r9: tidak ada default filter |
| `default-filter-tersaring` | — §9.5#r9: tidak ada default filter |
| `boolean-kedua-nilai` | — §4.1a Days Missing: filter Long missing satu checkbox, hanya nilai dicentang (dicakup per-kelas-kontrol:checkbox) |
| `create-tidak-cocok` | — §4.2.1#b1: tidak ada Create di halaman ini; dicakup mutasi-masuk-saringan |

### filter@tabel-history · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-010-2 |
| `tidak-cocok` | ✓ DU-010-3 |
| `or-dalam-field` | ✓ DU-010-4 |
| `range-tepat-min` | ✓ DU-010-7 |
| `range-tepat-max` | ✓ DU-010-7 |
| `per-kelas-kontrol:multi-select` | ✓ DU-010-2 |
| `per-kelas-kontrol:numeric range` | ✓ DU-010-7 |
| `per-kelas-kontrol:date range` | ✓ DU-010-6 |
| `and-a-saja` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `and-b-saja` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `and-keduanya` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `and-tidak-keduanya` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `search-saja` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `filter-saja` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `search-dan-filter` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `irisan-kosong` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `kolom-tersembunyi` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `filter-only` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `boolean-kedua-nilai` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `custom-field-per-tipe` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `mutasi-keluar-saringan` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `mutasi-masuk-saringan` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `create-tidak-cocok` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `status-dikecualikan` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `default-filter-lolos` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `default-filter-tersaring` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `rentang-dalam` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `rentang-luar` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `rentang-tepat-awal` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `rentang-tepat-akhir` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `rentang-sehari` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `range-min-lebih-max` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `range-hanya-min` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |
| `range-hanya-max` | — VD-2: kombinasi Search/Filter dan mekanik diuji di T-MIS-01 |

### opsi-filter@tabel-active · VD-T4

| Varian | Entri |
|---|---|
| `nilai-berulang` | ✓ DU-004-8 |
| `kosong` | ✓ DU-004-7 |
| `kolom-tanpa-null` | ✓ DU-004-8 |
| `master-tak-terpakai` | ✓ DU-004-6 |
| `enum-sebagian-terisi` | ✓ DU-004-12 |
| `per-anggota-enum:Waiting for Confirmation` | ✓ DU-004-7 |
| `per-anggota-enum:Missing` | ✓ DU-004-8 |
| `per-anggota-enum:Reported Disposal` | ✓ DU-004-11 |
| `per-anggota-enum:In Disposal Process` | ✓ DU-004-15 |
| `opsi-tidak-dipersempit-search` | ✓ DU-004-12 |
| `nilai-baru-saat-uji` | ✓ DU-004-14 |
| `opsi-banyak-overflow` | ✓ DU-004-10 |
| `cari-opsi-substring` | ✓ DU-004-18 |
| `cari-opsi-beda-kapital` | ✓ DU-004-19 |
| `cari-opsi-tanpa-hasil` | ✓ DU-004-20 |
| `sumber-kosong` | ✓ DU-004-21 |
| `nilai-di-cakupan-lain` | — §4.4#r1: opsi dari sub-tab aktif saja (dicakup nilai-berulang per tab) |
| `opsi-tetap-worm` | — §4.1a: tabel bukan log WORM |
| `entitas-terhapus-berhistori` | — §4.1b#p1: nama historis hanya di T-MIS-02 (target history) |
| `entitas-rename-berhistori` | — §4.1b#p1: hanya T-MIS-02 |
| `nilai-kondisional` | — §4.1a: tidak ada opsi bersyarat |
| `satu-nilai-distinct` | — §9.8 foundation Single-Value Guard tidak dirujuk PRD |
| `dua-nilai-distinct` | — §4.1a kolom Filterable: Single-Value Guard foundation tidak dirujuk PRD |
| `opsi-hilang` | — EB-FLT-7 ditahan (temuan 3) |

### paginasi@tabel-active · VD-T5

| Varian | Entri |
|---|---|
| `lebih-satu-halaman` | ✓ DU-051-1 |
| `satu-baris-halaman-terakhir` | ✓ DU-051-1 |
| `tepat-ukuran-halaman` | ✓ DU-051-2 |
| `lebih-ukuran-terpilih:10` | ✓ DU-051-1 |
| `lebih-ukuran-terpilih:25` | ✓ DU-051-3 |
| `tersaring-lebih-satu-halaman` | ✓ DU-051-4 |
| `nomor-halaman-invalid` | ✓ DU-051-5 |
| `lebih-ukuran-maks` | — §5#r2: ukuran maks 100; 101 record tidak dibentuk di component test (LY-4) dan tidak di ui-e2e (RC-4 volume) |

### empty-state@tabel · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-050-19 |
| `relasi-kosong` | — §7.1: tidak ada sub-tabel relasi |
| `node-tanpa-anak` | — §7.1: tidak ada tree |
| `kosong-untuk-aktor-ini` | — §7.1: empty state per cakupan tidak dibedakan copy-nya |
| `jadi-kosong-setelah-hapus` | — §10#r5: tidak ada hapus |
| `log-kosong` | — §7.1 S-12: Missing log tidak pernah kosong |

### tampilan-sel@tabel-active · VD-T7

| Varian | Entri |
|---|---|
| `null` | ✓ DU-050-3, DU-050-9 |
| `tanggal-null` | ✓ DU-050-9 |
| `kosong-tidak-pernah-diisi` | ✓ DU-050-9 |
| `teks-panjang` | ✓ DU-050-13 |
| `per-nilai-badge:Waiting for Confirmation` | ✓ DU-050-2 |
| `per-nilai-badge:Missing` | ✓ DU-050-1 |
| `per-nilai-badge:Reported Disposal` | ✓ DU-050-3 |
| `per-nilai-badge:In Disposal Process` | ✓ DU-050-5 |
| `tanpa-foto` | ✓ DU-050-6 |
| `nilai-beda-antar-kolom` | ✓ DU-050-4, DU-050-8 |
| `aktor-system` | ✓ DU-050-9 |
| `string-kosong` | — §4.1a Nilai Kosong: kosong tampil `—` tanpa membedakan string kosong dari null |
| `array-kosong` | — §4.1a Labels/TAG kosong tampil `—` (dicakup null) |
| `boolean-null` | — §4.1a: tidak ada kolom boolean |
| `nol-numerik` | — §4.1a Days Missing: copy untuk 0 hari tidak dinyatakan (temuan 4) |
| `angka-ribuan` | — §4.1a: kolom currency memakai format mata uang Company (dicakup nilai-beda-antar-kolom) |
| `angka-pembulatan` | — §4.1a: tidak dinyatakan |
| `nilai-turunan` | — §4.1a: tidak ada path hirarki di sel; hierarki Group di hover (dicakup per-nilai-badge) |
| `asal-jalur` | — LY-3: asal data tidak tampil berbeda di ui-client; Source diuji lewat per-nilai-badge |
| `referensi-diarsipkan` | — §4.1a: tidak dinyatakan |
| `referensi-terhapus` | — §4.1b#p1: hanya History (target tabel-history) |
| `kosong-setelah-dihapus` | — §4.1a: tidak ada field yang dikosongkan pengguna |
| `teks-panjang-multibaris` | — §9.9: What happened tidak tampil di tabel |

### tampilan-sel@tabel-history · VD-T7

| Varian | Entri |
|---|---|
| `per-nilai-badge:Found` | ✓ DU-053-1 |
| `per-nilai-badge:Disposed` | ✓ DU-053-2 |
| `per-nilai-badge:Rejected` | ✓ DU-053-3 |
| `per-nilai-badge:Canceled` | ✓ DU-053-4 |
| `aktor-system` | ✓ DU-053-2 |
| `referensi-terhapus` | ✓ DU-053-5 |
| `string-kosong` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `array-kosong` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `boolean-null` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `nol-numerik` | — §4.1a Days Missing: copy untuk 0 hari tidak dinyatakan (temuan 4) |
| `tanggal-null` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `kosong-tidak-pernah-diisi` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `kosong-setelah-dihapus` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `teks-panjang` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `teks-panjang-multibaris` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `tanpa-foto` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `angka-ribuan` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `angka-pembulatan` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `nilai-turunan` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `nilai-beda-antar-kolom` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `asal-jalur` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `referensi-diarsipkan` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |
| `null` | — VD-2: tampilan nilai diuji di T-MIS-01; T-MIS-02 hanya kolom dan keadaan yang lahir dari tabelnya (Duration, Resolved By System, referensi terhapus/dinonaktifkan) |

### nama-user@tabel-active · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-050-10 |
| `dua-kata` | ✓ DU-050-1, DU-050-10 |
| `tiga-kata-lebih` | ✓ DU-050-11 |
| `nama-panjang` | ✓ DU-050-11 |
| `tanpa-last-name` | ✓ DU-050-10 |
| `nama-mirip` | ✓ DU-050-12 |

### Days Missing@tabel-active · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-050-2 |
| `jumlah-banyak` | ✓ DU-050-1, DU-050-4 |
| `jumlah-nol` | — §4.1a Days Missing dan §4.1b Duration: copy 0 hari tidak dinyatakan (temuan 4) |
| `per-jumlah-independen` | — §4.1a: satu jumlah |

### Duration@tabel-history · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-053-3 |
| `jumlah-banyak` | ✓ DU-053-1 |
| `jumlah-nol` | — §4.1a Days Missing dan §4.1b Duration: copy 0 hari tidak dinyatakan (temuan 4) |
| `per-jumlah-independen` | — §4.1b: satu jumlah |

### tanggal@tabel-active · VD-T13

| Varian | Entri |
|---|---|
| `hari-lebih-12` | ✓ DU-050-10 |
| `dekat-tengah-malam` | ✓ DU-050-11 |

### seleksi@tabel-active · VD-T14

| Varian | Entri |
|---|---|
| `satu-baris` | ✓ DU-052-1 |
| `banyak-baris` | ✓ DU-052-1 |
| `halaman-penuh` | ✓ DU-052-1 |
| `lintas-halaman` | ✓ DU-052-1 |
| `tersembunyi-filter` | ✓ DU-052-2 |
| `homogen:Missing` | ✓ DU-052-1 |
| `checkbox-disabled` | — §4.1a#p2: PRD tidak menetapkan baris dengan checkbox disabled |
| `single-select-ganti` | — §4.1a: tidak ada single-select |
| `campuran-state` | — §4.1a#p9: seleksi lintas status diuji sebagai record dilewati di spec -dep- (VD-A1 campuran) |

### download@tabel-active · VD-D1

| Varian | Entri |
|---|---|
| `tanpa-saringan-lebih-satu-halaman` | ✓ DU-006-4 |
| `hasil-tersaring` | ✓ DU-006-5, DU-006-7 |
| `nol-baris` | ✓ DU-006-6 |
| `urutan-sort-aktif` | ✓ DU-006-4 |
| `kolom-tersembunyi` | ✓ DU-006-4 |
| `per-tab` | — §5#r6: nama berkas per sub-tab diuji di spec Download History (target sendiri) |

### isi-berkas@download · VD-D2

| Varian | Entri |
|---|---|
| `kolom-foto` | ✓ DU-079-7 |
| `kolom-ikon` | ✓ DU-079-7 |
| `per-nilai-badge:Missing` | ✓ DU-079-7 |
| `per-nilai-badge:Waiting for Confirmation` | ✓ DU-079-8 |
| `multi-badge` | ✓ DU-079-7, DU-079-18 |
| `item-flat` | ✓ DU-079-7 |
| `nama-user-lengkap` | ✓ DU-079-3 |
| `numerik-terformat` | ✓ DU-079-7 |
| `mata-uang` | ✓ DU-079-7 |
| `nilai-kosong` | ✓ DU-079-8 |
| `switch-kedua-nilai` | — §4.1a: tidak ada kolom switch |
| `boolean-kedua-nilai` | — §4.1a: tidak ada kolom boolean |
| `hierarki-penuh` | — §4.1a Group: hierarki hanya di hover; isi export mengikuti §9.9 foundation (dicakup item-flat) |
| `leaf-sama-parent-beda` | — §4.1a: tidak dinyatakan |
| `lebih-dua-badge` | — §4.1a Labels: satu badge per label tanpa +N more |

### csv@download · VD-D3

| Varian | Entri |
|---|---|
| `nilai-koma` | ✓ DU-079-8 |
| `nilai-kutip` | ✓ DU-079-9 |
| `non-ascii` | ✓ DU-079-10 |
| `nilai-baris-baru` | — §5#r6, §4.1a, §4.1b: kolom unduhan adalah kolom tabel bertipe Text/Date/Number/Currency/Badge dari field single-line; field Textarea (What happened, Note, Reason, Update, §9.9) tidak menjadi kolom tabel. prd-conventions §4: newline tidak bisa ter-input di field single-line, jadi data ber-newline tidak bisa dibuat lewat produk (DT-4). |

### bulk-report-disposal@tabel-active · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-037-4 |
| `n-banyak` | ✓ DU-037-1, DU-037-2, DU-037-3 |
| `campuran` | ✓ DU-037-5, DU-037-6, DU-037-7, DU-037-8 |
| `semua-ditolak` | ✓ DU-037-7, DU-037-8 |
| `semua-ditolak-alasan-single` | ✓ DU-037-8 |
| `gagal-banyak` | — §6 V-12: record dilewati memakai satu toast skipped, tanpa penggabungan per item |
| `daftar-melebihi-tampil` | — §4.2.4#p15: D-DISP-13 milik modul Disposal |
| `item-beranotasi` | — §4.1a#p9: record dilewati tanpa anotasi di dialog |
| `sisa-satu-relevan` | — §4.1a#p8: satu Reason untuk semua; bentuk dialog milik Disposal |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada baris Default/Self |
| `jadi-tidak-eligible-saat-submit` | — §4.2.4#p14: aksi bulk tidak memakai D-MIS-06 dan PRD tidak menyatakan hasilnya |
| `nol-item` | — §4.1a#p9: tombol aktif selama ada seleksi; nol seleksi tidak punya aksi |

### status-record@tabel-active · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Waiting for Confirmation` | ✓ DU-001-7 |
| `per-status:Missing` | ✓ DU-001-6 |
| `per-status:Reported Disposal` | ✓ DU-001-8 |
| `per-status:In Disposal Process` | ✓ DU-001-9 |
| `per-kondisi-disabled:Last holder` | ✓ DU-001-12 |
| `transisi-valid` | — §9.2 9.2.0: transisi diuji di be-e2e lewat target status-record@server |
| `transisi-mundur` | — §9.2 9.2.0: diuji di be-e2e (status-record@server) |
| `transisi-ilegal` | — §9.2 9.2.0: diuji di be-e2e (status-record@server) |
| `state-final` | — §4.1b: status final ada di tab History (target tabel-history) |
| `sudah-di-state-tujuan` | — §9.6 kolom Idempotent: diuji di be-e2e (status-record@server) |
| `state-transien` | — §9.2: tidak ada state committing |
| `flag-terkunci` | — §9.2: tidak ada flag terkunci |
| `koheren-rantai-gate` | — §9.2: tidak ada rantai gate |

### status-record@tabel-history · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Found` | ✓ DU-007-6 |
| `per-status:Disposed` | ✓ DU-007-7 |
| `per-status:Rejected` | ✓ DU-007-8 |
| `per-status:Canceled` | ✓ DU-007-9 |
| `state-final` | ✓ DU-007-7 |
| `transisi-valid` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `transisi-mundur` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `transisi-ilegal` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `sudah-di-state-tujuan` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `state-transien` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `flag-terkunci` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `per-kondisi-disabled` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |
| `koheren-rantai-gate` | — §4.1b: tab History hanya menampilkan status final; transisi di be-e2e |

### status-record@server · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Waiting for Confirmation` | ✓ DU-071-3 |
| `per-status:Missing` | ✓ DU-071-7 |
| `per-status:Reported Disposal` | ✓ DU-071-10 |
| `per-status:In Disposal Process` | ✓ DU-071-11 |
| `per-status:Found` | ✓ DU-071-21 |
| `per-status:Disposed` | ✓ DU-071-22 |
| `per-status:Rejected` | ✓ DU-071-23 |
| `per-status:Canceled` | ✓ DU-071-24 |
| `transisi-valid` | ✓ DU-071-3, DU-071-4, DU-071-5 |
| `transisi-mundur` | ✓ DU-071-12, DU-071-13, DU-071-14, DU-071-15, DU-071-16 |
| `transisi-ilegal` | ✓ DU-071-21 |
| `state-final` | ✓ DU-071-21 |
| `sudah-di-state-tujuan` | ✓ DU-071-3 |
| `state-transien` | — §9.2: tidak ada state committing |
| `flag-terkunci` | — §9.2: tidak ada flag |
| `per-kondisi-disabled` | — §6 V-01 Last holder diuji di target authz |
| `koheren-rantai-gate` | — §9.2: tidak ada rantai gate |

### matriks-role@missing · VD-P1

| Varian | Entri |
|---|---|
| `per-baris-matriks:Total Control` | ✓ DU-072-1 |
| `per-baris-matriks:Group Manager` | ✓ DU-072-2 |
| `per-baris-matriks:Manage asset & TAG (Update)` | ✓ DU-072-3 |
| `per-baris-matriks:Accounting` | ✓ DU-072-4 |
| `per-baris-matriks:Read Only` | ✓ DU-072-5 |
| `per-baris-matriks:Manage asset & TAG (Read)` | ✓ DU-072-6 |
| `per-baris-matriks:View asset value` | ✓ DU-072-7 |
| `per-baris-matriks:Pemegang` | ✓ DU-072-8 |
| `tanpa-akses` | ✓ DU-072-9 |
| `read-only-saja` | ✓ DU-072-5 |
| `capability-tunggal:Update` | ✓ DU-072-3 |
| `tanpa-capability-aksi:Update` | ✓ DU-072-6 |
| `tanpa-sesi` | ✓ DU-072-20 |
| `kombinasi-permission` | — §2#b1: Create dan Delete pada Manage asset & TAG tidak berlaku |
| `per-kombinasi-crud` | — §2#b1: hanya Read dan Update |
| `tanpa-bulk` | — §4.1a#p8: bulk mengikuti hak Report Disposal, bukan capability tersendiri |
| `tanpa-single-action` | — §2.1: tidak ada capability per aksi tunggal |
| `access-level-null-plus-individual` | — §2: tidak dinyatakan |
| `zero-assignment` | — §2: tidak dinyatakan |
| `can-read-false` | — §2: tidak dinyatakan |
| `assignment-retained` | — §2: tidak dinyatakan |
| `entitas-diblok-punya-role` | — §9.4.1 D1 diuji lewat VD-A4 |
| `per-jenis-entitas` | — §9.11: hanya Client |
| `per-peran-alur` | — §2#b2 Pelapor admin jenis 2 dan 3 diuji di spec -dep-borrow dan -dep-audit (dicakup per-baris-matriks tidak; tidakBerlaku karena hak datang dari modul lain) |

### scope@server · VD-P2

| Varian | Entri |
|---|---|
| `luar-group` | ✓ DU-072-6, DU-072-24 |
| `multi-group` | ✓ DU-072-3 |
| `field-terbatas-per-role` | ✓ DU-072-7, DU-072-21 |
| `scope-sub-tree` | ✓ DU-072-2 |
| `dua-aktor-scope-beda` | ✓ DU-072-3 |
| `luar-entitas` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `client-multi-partner` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `client-transitif` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `target-write-transitif` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `target-write-langsung` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `field-termask` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `scope-exact-match` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |
| `assignment-node-descendant` | — §2.1 Scope: cakupan Group binaan/penugasan + descendant saja; tidak ada entitas lain, Partner, mask field, atau exact match |

### akses-langsung@missing-log · VD-P4

| Varian | Entri |
|---|---|
| `aktor-tanpa-read` | ✓ DU-072-9 |
| `id-tidak-ada` | ✓ DU-072-40 |
| `id-sudah-dihapus` | ✓ DU-072-39 |
| `id-milik-entitas-lain` | ✓ DU-072-38 |

### state-entitas@missing · VD-A4

| Varian | Entri |
|---|---|
| `active` | ✓ DU-080-1 |
| `suspended` | ✓ DU-080-2 |
| `expired` | ✓ DU-080-3 |
| `job-sistem` | ✓ DU-080-3 |
| `deleted` | — §9.4.1 D1: hanya Suspended / Expired |
| `per-jenis-entitas-pemilik` | — §9.11: Client |
| `per-peran-entitas` | — §9.11: Client |
| `aksi-reaktivasi` | — §18.8 foundation: aksi modul Client Subscription, di luar modul ini |
| `per-interval` | — §9.4.1 D1: tidak ada interval |

### plan@missing · VD-P5

| Varian | Entri |
|---|---|
| `per-tier:Starter` | ✓ DU-080-4 |
| `basic-dalam-scope` | — §9.10: level Basic tersedia penuh |
| `basic-luar-scope` | — §9.10: tidak dinyatakan |
| `addon-dibeli` | — §1#b1: fitur inti tanpa add-on |
| `addon-tidak-dibeli` | — §1#b1: tanpa add-on |
| `cap-plan-lama-beda-baru` | — §9.10: tidak ada cap |
| `per-level` | — plans.md §3.4a: Feature Suite Disposal hanya punya level None dan Full; level Basic tidak ada (PRD §9.10 menyebutnya, temuan 11) |

### kelayakan@report-missing · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-MISS-01.k1a` | ✓ DU-070-8, DU-070-9, DU-070-10, DU-070-11, DU-070-13, DU-070-14 |
| `per-kondisi:F-MISS-01.k1b` | ✓ DU-070-12 |
| `per-kondisi:F-MISS-01.k3` | ✓ DU-070-16 |
| `lolos-semua-cabang` | ✓ DU-070-1, DU-070-7 |
| `per-langkah-logic` | — §9.6#p1: API contract milik backend |
| `per-baris-error-handling` | — §9.6#p1: milik backend |
| `efek-samping-per-cabang` | — §9.4.4#r1: penolakan tanpa event; dicakup lolos-semua-cabang |

### konkurensi@report-missing · VD-A7

| Varian | Entri |
|---|---|
| `create-nilai-sama-serentak` | ✓ DU-070-16 |
| `diubah-pihak-lain` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `dihapus-pihak-lain` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `target-sama-nilai-beda` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `target-beda` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `per-pasangan-aksi` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `create-bersamaan` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `status-diubah-pihak-lain` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `jadi-dipakai-saat-confirm` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `bulk-semua-jadi-dipakai` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `bulk-sebagian-jadi-dipakai` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `nilai-guard-berubah` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `dibuat-pihak-lain` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `pihak-lain-cocok-saringan` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `pihak-lain-tidak-cocok-saringan` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `pihak-lain-halaman-lain` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `pihak-lain-ubah-baris-terseleksi` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |
| `permintaan-basi` | — §9.4.2 EC-MIS-02 hanya menyatakan dua laporan bersamaan; pasangan lain ditangani D-MIS-06 (target konkurensi@aksi) |

### konkurensi@aksi · VD-A7

| Varian | Entri |
|---|---|
| `per-pasangan-aksi:Add Update-Mark as Found` | ✓ DU-071-7 |
| `per-pasangan-aksi:Confirm-Mark as Found` | ✓ DU-071-6 |
| `per-pasangan-aksi:Review-Reject` | ✓ DU-071-8 |
| `per-pasangan-aksi:Cancel Report-Confirm` | ✓ DU-071-9 |
| `per-pasangan-aksi:Cancel Disposal Report-Dispose` | ✓ DU-071-10 |
| `status-diubah-pihak-lain` | ✓ DU-071-11 |
| `dihapus-pihak-lain` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `target-sama-nilai-beda` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `target-beda` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `create-nilai-sama-serentak` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `create-bersamaan` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `jadi-dipakai-saat-confirm` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `bulk-semua-jadi-dipakai` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `bulk-sebagian-jadi-dipakai` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `nilai-guard-berubah` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `dibuat-pihak-lain` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `pihak-lain-cocok-saringan` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `pihak-lain-tidak-cocok-saringan` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `pihak-lain-halaman-lain` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `pihak-lain-ubah-baris-terseleksi` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `permintaan-basi` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |
| `diubah-pihak-lain` | — §6 V-10: hanya «status record sudah berubah»; tidak ada hapus, saringan live, atau guard nilai |

### jalur-non-form@missing-log · VD-A8

| Varian | Entri |
|---|---|
| `per-jalur:Deteksi scan` | ✓ DU-077-19 |
| `per-jalur:Job Long missing` | ✓ DU-077-20 |
| `per-jalur:I found it` | ✓ DU-077-21 |
| `per-jalur:Event Disposal` | ✓ DU-077-14 |
| `dengan-aktor` | ✓ DU-077-21 |
| `tanpa-aktor` | ✓ DU-077-14 |
| `butuh-normalisasi` | — §8: tidak ada Import |
| `pasangan-manual-setara` | — §8: tidak ada Import |
| `duplikat-dalam-batch` | — §8: tidak ada Import |
| `duplikat-dengan-data-ada` | — §8: tidak ada Import |
| `import-semua-valid` | — §8: tidak ada Import |
| `import-sebagian-error` | — §8: tidak ada Import |

### log@missing · VD-L1

| Varian | Entri |
|---|---|
| `bulk` | ✓ DU-077-4, DU-077-18 |
| `per-aksi-non-crud:Report Missing` | ✓ DU-077-4 |
| `per-aksi-non-crud:Confirm` | ✓ DU-077-8 |
| `per-aksi-non-crud:Reject` | ✓ DU-077-9 |
| `per-aksi-non-crud:Cancel Report` | ✓ DU-077-10 |
| `per-aksi-non-crud:Add Update` | ✓ DU-077-11 |
| `per-aksi-non-crud:Mark as Found` | ✓ DU-077-12 |
| `per-aksi-non-crud:Report Disposal` | ✓ DU-077-13 |
| `per-aksi-non-crud:Cancel Disposal Report` | ✓ DU-077-13 |
| `create` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `edit-per-field` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `delete` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `field-sub-item` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `field-permission` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `field-badge-enum` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `field-tanpa-teks` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `nilai-awal` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `assign` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `remove` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `update-setelah-assign` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `approve-dari-approvals` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `reject-dari-approvals` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `settings-tanpa-nama` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `reset-ke-default` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `reset-sudah-default` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `per-event` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `event-sesi` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `nilai-kosong` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `edit-multi-field` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `per-baris-pencatatan` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `per-varian-jalur` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |
| `per-sub-konteks` | — §8: Missing Log mencatat peristiwa aksi, bukan Create/Edit/Delete field; tidak ada assign, settings, approval, atau sesi |

### log-tidak-tercatat@missing · VD-L2

| Varian | Entri |
|---|---|
| `efek-samping-tanpa-log` | ✓ DU-077-16 |
| `record-lain-tak-terlibat` | ✓ DU-077-7 |
| `bulk-dengan-skip` | ✓ DU-077-6 |
| `tanpa-perubahan` | — §9.6#p2: tidak ada edit no-op |
| `entri-entitas-lain` | — §9.11: log per record, tidak ter-scope lintas entitas |

### aktor-log@missing · VD-L4

| Varian | Entri |
|---|---|
| `aktor-system` | ✓ DU-077-14 |
| `aktor-beda-target` | ✓ DU-077-8 |
| `asal-modul-lain` | ✓ DU-077-14 |
| `log-entitas-terkait` | — §8.2: tampilan lain adalah milik modul lain (spec -dep-) |

### jendela-deteksi@server · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-074-7 |
| `per-nilai-setting:1 jam` | ✓ DU-074-7 |
| `nilai-diubah` | — §9.5#r6: jendela tetap 1 jam, bukan setting |
| `record-sebelum-perubahan` | — §9.5#r6: jendela tetap 1 jam, bukan setting |
| `record-sesudah-perubahan` | — §9.5#r6: jendela tetap 1 jam, bukan setting |
| `per-opsi-format-tanggal` | — §9.5#r6: jendela tetap 1 jam, bukan setting |
| `zona-waktu-non-default` | — §9.5#r6: jendela tetap 1 jam, bukan setting |
| `format-regional-beda-entitas` | — §9.5#r6: jendela tetap 1 jam, bukan setting |

### Long missing after@server · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-075-2 |
| `nilai-diubah` | ✓ DU-075-12, DU-075-13, DU-075-14 |
| `per-nilai-setting:0` | ✓ DU-075-13 |
| `per-nilai-setting:30` | ✓ DU-075-2 |
| `record-sebelum-perubahan` | ✓ DU-075-4 |
| `record-sesudah-perubahan` | ✓ DU-075-15 |
| `per-opsi-format-tanggal` | — §9.5#r5: setting hari, bukan format |
| `zona-waktu-non-default` | — §9.2 F-MISS-08.k1d: zona waktu Company tetap (Kondisi) |
| `format-regional-beda-entitas` | — §9.5: satu entitas |

### lokalisasi@tabel-active · VD-S2

| Varian | Entri |
|---|---|
| `bahasa-non-default` | ✓ DU-050-7, DU-050-14 |
| `verbatim-mirip-kamus` | ✓ DU-050-14 |
| `kode-berkata-inggris` | ✓ DU-050-14 |
| `enum-diterjemahkan` | — §4.1#p4: label sistem translatable diuji lewat bahasa-non-default |
| `ganti-bahasa-format-tetap` | — §4.1#p4: tidak dinyatakan |

### guided-tooltip@missing · VD-S3

| Varian | Entri |
|---|---|
| `flag-belum` | ✓ DU-019-1, DU-019-3, DU-019-4, DU-019-5 |
| `flag-sudah` | ✓ DU-019-2 |
| `aktor-lain` | ✓ DU-019-3 |
| `flag-sudah-device-lain` | — §4.7: foundation guided-tooltip menyimpan flag per aktor hanya bila dinyatakan; PRD diam |

### asersi-negatif@missing-log · VD-A14

| Varian | Entri |
|---|---|
| `terlibat` | ✓ DU-077-4 |
| `kontrol` | ✓ DU-077-7 |

### nasib-dependen@group · VD-A11

| Varian | Entri |
|---|---|
| `punya-anak` | ✓ DU-040-1 |
| `tanpa-anak` | ✓ DU-040-2 |
| `log-menunjuk` | ✓ DU-040-3 |
| `pending-in-flight` | — §10#r6: tidak dinyatakan |
| `assignment-luar-constraint` | — §10#r6: tidak dinyatakan |
| `linked-item` | — §10#r6: tidak dinyatakan |

## Entri

- **DU-001-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Tampil `Rina W` (6 kar) · sumber matriks role PRD
- **DU-001-2** User (awal), Group Manager, Last holder dan pelapor: Name `Andi Pratama {runId}` (20 kar), Role `Group Manager` (13 kar), Group `Head Office {runId}` (19 kar), Tampil `Andi P` (6 kar) · sumber matriks role PRD
- **DU-001-3** User (awal), Pemegang aset tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Role `Borrower` (8 kar), Tampil `Joko S` (6 kar) · sumber matriks role PRD
- **DU-001-4** User (awal), Manage asset & TAG Update pada Branch Surabaya: Name `Agus Prasetyo {runId}` (21 kar), Role `Manage asset & TAG (Update)` (27 kar), Group `Branch Surabaya {runId}` (23 kar), Tampil `Agus P` (6 kar) · sumber matriks role PRD
- **DU-001-5** User (awal), Last holder yang dinonaktifkan: Name `Dewi Anggraini {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Group `Head Office {runId}` (19 kar), Status `dinonaktifkan sesudah menjadi Last holder DU-001-11` (51 kar), Tampil `Dewi A` (6 kar) · sumber PRD §4.1a Example Data
- **DU-001-6** Missing record (awal; dimutasi TC-FA-MISS-E2E-001-tab-active-tampilan-tabel), Record Missing Source Borrow dengan Last holder dan Last Seen dari reader: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room {runId}` (20 kar), TAG `RFID` (4 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Andi Pratama {runId}` (20 kar), Last Seen `T0 − 9 hari, pukul 10:12` (24 kar), Pemindai `Lobby reader {runId}` (20 kar), Reported By `Andi Pratama {runId}` (20 kar), Reported Date `T0 − 8 hari, pukul 09:30` (24 kar), Days Missing `8 days` (6 kar), Last Updated `sama dengan Reported Date` (25 kar) · sumber PRD §4.1a Example Data
- **DU-001-7** Missing record (awal), Record Waiting for Confirmation laporan pemegang, belum pernah terpindai: Asset Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse {runId}` (17 kar), TAG `NFC` (3 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susilo {runId}` (19 kar), Last Seen `Unknown` (7 kar), Reported By `Joko Susilo {runId}` (19 kar), Reported Date `T0 − 1 hari, pukul 07:15` (24 kar), Days Missing `1 day` (5 kar), Last Updated `sama dengan Reported Date` (25 kar) · sumber PRD §4.1a Example Data
- **DU-001-8** Missing record (awal), Record Reported Disposal tanpa Last holder, melewati Long missing after: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Surabaya {runId}` (23 kar), TAG `QR` (2 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), Last Seen `T0 − 45 hari, pukul 14:05` (25 kar), Pemindai `Agus Prasetyo {runId}` (21 kar), Reported By `Agus Prasetyo {runId}` (21 kar), Reported Date `T0 − 41 hari, pukul 08:00` (25 kar), Days Missing `41 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-001-9** Missing record (awal), Record In Disposal Process tanpa Last holder: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), TAG `BLE` (3 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Last Seen `T0 − 80 hari, pukul 16:40` (25 kar), Pemindai `Lobby reader {runId}` (20 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 78 hari, pukul 10:00` (25 kar), Days Missing `78 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-001-10** Missing record (awal), Record Missing Source Transfer tanpa Last holder: Asset Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), TAG `GPS` (3 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `—` (1 kar), Last Seen `T0 − 11 hari, pukul 16:20` (25 kar), Pemindai `Gate B reader {runId}` (21 kar), Reported By `Agus Prasetyo {runId}` (21 kar), Reported Date `T0 − 10 hari, pukul 09:00` (25 kar), Days Missing `10 days` (7 kar), Last Updated `sama dengan Reported Date` (25 kar) · sumber PRD §4.1a Example Data
- **DU-001-11** Missing record (awal), Record Missing yang melewati Long missing after, Last holder dinonaktifkan: Asset Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), TAG `NFC, QR` (7 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi Anggraini {runId}` (22 kar), Last Seen `T0 − 37 hari, pukul 11:10` (25 kar), Pemindai `Gate A reader {runId}` (21 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 34 hari, pukul 09:00` (25 kar), Days Missing `34 days` (7 kar), Penanda `Long missing` (12 kar), Garansi 1 nama `Garansi Unit {runId}` (20 kar), Garansi 1 sampai `T0 + 120 hari` (13 kar), Garansi 2 nama `Garansi Baterai {runId}` (23 kar), Garansi 2 sampai `T0 + 365 hari` (13 kar), Warranty Expiry `T0 + 120 hari, dari Warranty until terdekat` (43 kar) · sumber PRD §4.1a Example Data
- **DU-001-12** Missing record (awal), Record Missing yang Last holder-nya aktor, aset tanpa TAG: Asset Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office {runId}` (19 kar), TAG `—` (1 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Rina Wijaya {runId}` (19 kar), Last Seen `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 3 hari, pukul 08:00` (24 kar), Days Missing `3 days` (6 kar), Last Updated `sama dengan Reported Date` (25 kar) · sumber PRD §4.1a Example Data
- **DU-001-13** Missing record (awal), Record Found yang hanya ada di tab History: Asset Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office {runId}` (19 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-001-14** Kata kunci Search (dicoba), Kata kunci tanpa hasil: Kata kunci `{runId} tidakada` (16 kar) · sumber EB-TBL-1@tabel-active
- **DU-001-15** Isian dialog (dibuat), Isian Report Disposal untuk DU-001-6: Reason `Aset tidak ditemukan setelah penelusuran tiga minggu` (52 kar) · sumber turunan penulis
- **DU-001-16** Garansi aset (awal), Daftar garansi tambahan untuk sort Warranty Expiry: Aset 1 `Monitor LG 27UL500 {runId}` (26 kar), Garansi 1 nama `Garansi Monitor {runId}` (23 kar), Garansi 1 sampai `T0 + 30 hari` (12 kar), Warranty Expiry aset 1 `T0 + 30 hari, dari Warranty until terdekat` (42 kar), Aset 2 `Printer HP LaserJet M404 {runId}` (32 kar), Garansi 2 nama `Garansi Printer {runId}` (23 kar), Garansi 2 sampai `T0 + 200 hari` (13 kar), Warranty Expiry aset 2 `T0 + 200 hari, dari Warranty until terdekat` (43 kar) · sumber turunan penulis
- **DU-001-17** Kata kunci Search (dicoba), Nama garansi yang tidak boleh ikut dicari: Kata kunci `Garansi Unit {runId}` (20 kar) · sumber turunan penulis
- **DU-001-18** Filter Warranty Expiry (dicoba), Rentang yang memuat satu Warranty until terdekat: Dari `T0 + 100 hari` (13 kar), Sampai `T0 + 150 hari` (13 kar) · sumber turunan penulis
- **DU-002-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-002-2** Missing record (awal), Record Missing dengan nama, Group, Asset ID, TAG, Brand, dan Purchase Cost yang dicari: Asset Name `Plotter Delta {runId}` (21 kar), Group `Finance Room {runId}` (20 kar), TAG `RFID` (4 kar), Brand `Zephyrion {runId}` (17 kar), Purchase Cost `18250075` (8 kar), Last Seen `T0 − 7 hari` (11 kar), Pemindai `Lobby reader {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 6 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-002-3** Missing record (awal), Record Missing yang Group-nya cocok dengan kata kunci lintas kolom: Asset Name `Router Aksara {runId}` (21 kar), Group `Delta {runId}` (13 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 5 hari, pukul 10:00` (24 kar) · sumber turunan penulis
- **DU-002-4** Missing record (awal), Record Waiting for Confirmation laporan PIC atas nama karyawan tanpa akun: Asset Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse {runId}` (17 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susilo {runId}` (19 kar), Reported By `Rudi Hartono {runId}` (20 kar), Atas nama `Joko Susilo {runId}` (19 kar), Reported Date `T0 − 2 hari, pukul 07:15` (24 kar) · sumber PRD §4.1a Example Data
- **DU-002-5** Missing record (awal), Record Missing dengan karakter % dan _ pada nama: Asset Name `Cooler 50%_A {runId}` (20 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 4 hari, pukul 08:00` (24 kar) · sumber turunan penulis
- **DU-002-6** Missing record (awal), Pengecoh yang cocok bila % dan _ diperlakukan wildcard: Asset Name `Cooler 500XA {runId}` (20 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 4 hari, pukul 08:30` (24 kar) · sumber turunan penulis
- **DU-002-7** Missing record (awal), Record Missing dengan satu spasi di tengah nama: Asset Name `Printer Kantor {runId}` (22 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 3 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-002-8** Missing record (awal), Record Missing dengan nama berkata banyak: Asset Name `Server Room Utama {runId}` (25 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 3 hari, pukul 09:30` (24 kar) · sumber turunan penulis
- **DU-002-9** Kata kunci Search (dicoba), Potongan dari tengah nama: Kata kunci `lotter Delta {runId}` (20 kar) · sumber turunan penulis
- **DU-002-10** Kata kunci Search (dicoba), Nama dengan huruf kapital berbeda: Kata kunci `plotter delta {runId}` (21 kar) · sumber turunan penulis
- **DU-002-11** Kata kunci Search (dicoba), Nama dengan spasi di awal dan di akhir: Kata kunci `  Plotter Delta {runId}  ` (25 kar) · sumber turunan penulis
- **DU-002-12** Kata kunci Search (dicoba), Kata kunci hanya spasi: Kata kunci `   ` (3 kar) · sumber turunan penulis
- **DU-002-13** Kata kunci Search (dicoba), Kata kunci dengan dua spasi di tengah: Kata kunci `Printer  Kantor {runId}` (23 kar) · sumber turunan penulis
- **DU-002-14** Kata kunci Search (dicoba), Kata tidak bersebelahan: Kata kunci `Server Utama {runId}` (20 kar) · sumber turunan penulis
- **DU-002-15** Kata kunci Search (dicoba), Kata kunci tanpa hasil: Kata kunci `{runId} tidakada` (16 kar) · sumber turunan penulis
- **DU-002-16** Kata kunci Search (dicoba), Kata kunci berkarakter pola: Kata kunci `50%_A {runId}` (13 kar) · sumber turunan penulis
- **DU-003-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-003-2** User (awal), Pemegang Citra: Name `Citra Lestari {runId}` (21 kar), Role `Borrower` (8 kar), Tampil `Citra L` (7 kar) · sumber matriks role PRD
- **DU-003-3** User (awal), Pemegang Dodi: Name `Dodi Wibowo {runId}` (19 kar), Role `Borrower` (8 kar), Tampil `Dodi W` (6 kar) · sumber matriks role PRD
- **DU-003-4** User (awal), Pemegang Eka: Name `Eka Saputra {runId}` (19 kar), Role `Borrower` (8 kar), Tampil `Eka S` (5 kar) · sumber matriks role PRD
- **DU-003-5** User (awal), Pemegang Fajar: Name `Fajar Nugroho {runId}` (21 kar), Role `Borrower` (8 kar), Tampil `Fajar N` (7 kar) · sumber matriks role PRD
- **DU-003-6** Missing record (awal), Nama berawalan huruf kecil dengan Days Missing 12: Asset Name `anggur Press {runId}` (20 kar), Group `Gudang Uji {runId}` (18 kar), TAG `RFID` (4 kar), Purchase Cost `4500000` (7 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported Date `T0 − 12 hari, pukul 09:00` (25 kar), Days Missing `12 days` (7 kar) · sumber turunan penulis
- **DU-003-7** Missing record (awal), Nama Apel dengan dua ikon TAG: Asset Name `Apel Slicer {runId}` (19 kar), Group `Gudang Uji {runId}` (18 kar), TAG `NFC, QR` (7 kar), Purchase Cost `1250000` (7 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar), Reported Date `T0 − 9 hari, pukul 09:00` (24 kar), Days Missing `9 days` (6 kar) · sumber turunan penulis
- **DU-003-8** Missing record (awal), Nama beraksen dengan Days Missing sama: Asset Name `Élan Mixer {runId}` (18 kar), Group `Gudang Uji {runId}` (18 kar), TAG `NFC` (3 kar), Purchase Cost `2750000` (7 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Citra Lestari {runId}` (21 kar), Reported Date `T0 − 20 hari, pukul 09:00` (25 kar), Days Missing `20 days` (7 kar) · sumber turunan penulis
- **DU-003-9** Missing record (awal), Nama tanpa aksen dengan status dan Days Missing sama: Asset Name `Elan Mixer {runId}` (18 kar), Group `Gudang Uji {runId}` (18 kar), TAG `QR` (2 kar), Purchase Cost `9800000` (7 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar), Reported Date `T0 − 20 hari, pukul 11:00` (25 kar), Days Missing `20 days` (7 kar) · sumber turunan penulis
- **DU-003-10** Missing record (awal), Waiting for Confirmation dengan Days Missing kecil: Asset Name `Ezra Grinder {runId}` (20 kar), Group `Gudang Uji {runId}` (18 kar), TAG `BLE` (3 kar), Purchase Cost `3100000` (7 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Dodi Wibowo {runId}` (19 kar), Reported Date `T0 − 2 hari, pukul 08:00` (24 kar), Days Missing `2 days` (6 kar) · sumber turunan penulis
- **DU-003-11** Missing record (awal), Nama berawalan angka tanpa TAG: Asset Name `3D Printer {runId}` (18 kar), Group `Gudang Uji {runId}` (18 kar), Purchase Cost `6400000` (7 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `—` (1 kar), Reported Date `T0 − 15 hari, pukul 09:00` (25 kar), Days Missing `15 days` (7 kar) · sumber turunan penulis
- **DU-003-12** Missing record (awal), Nama berawalan simbol dengan Reported Date tertua: Asset Name `#Gudang Rak {runId}` (19 kar), Group `Gudang Uji {runId}` (18 kar), TAG `GPS` (3 kar), Purchase Cost `800000` (6 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `Eka Saputra {runId}` (19 kar), Reported Date `T0 − 40 hari, pukul 09:00` (25 kar), Days Missing `40 days` (7 kar) · sumber turunan penulis
- **DU-003-13** Missing record (awal), Waiting for Confirmation dengan dua ikon TAG: Asset Name `Forklift Kecil {runId}` (22 kar), Group `Gudang Uji {runId}` (18 kar), TAG `BLE, GPS` (8 kar), Purchase Cost `12000000` (8 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Fajar Nugroho {runId}` (21 kar), Reported Date `T0 − 1 hari, pukul 08:00` (24 kar), Days Missing `1 day` (5 kar) · sumber turunan penulis
- **DU-003-14** Missing record (awal; 12 record), Dua belas aset ber-nama sama dengan Days Missing 1 sampai 12: Asset Name `Pompa Air {runId}` (17 kar), Group `Gudang Pompa {runId}` (20 kar), TAG `NFC` (3 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported Date `T0 − {n} hari, pukul 09:00` (26 kar), Days Missing `{n} days` (8 kar) · sumber turunan penulis
- **DU-003-15** Atribut aset (awal), Labels dan pemindaian terakhir untuk DU-003-6, bukan record baru: Asset Name `anggur Press {runId}` (20 kar), Label 1 `Audit {runId}` (13 kar), Label 2 `Zebra {runId}` (13 kar), Last Seen `T0 − 14 hari` (12 kar), Pemindai `Gate A reader {runId}` (21 kar) · sumber turunan penulis
- **DU-003-16** Atribut aset (awal), Labels dan pemindaian terakhir untuk DU-003-7, bukan record baru: Asset Name `Apel Slicer {runId}` (19 kar), Label 1 `Berat {runId}` (13 kar), Last Seen `T0 − 10 hari` (12 kar), Pemindai `Gate A reader {runId}` (21 kar) · sumber turunan penulis
- **DU-003-17** Atribut aset (awal), Labels dan pemindaian terakhir untuk DU-003-8, bukan record baru: Asset Name `Élan Mixer {runId}` (18 kar), Label 1 `Cadangan {runId}` (16 kar), Label 2 `Fragile {runId}` (15 kar), Label 3 `Priority {runId}` (16 kar), Last Seen `T0 − 22 hari` (12 kar), Pemindai `Gate A reader {runId}` (21 kar) · sumber turunan penulis
- **DU-004-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-004-2** Karyawan (awal), Karyawan tanpa akun yang diwakili PIC: Name `Gita Permata {runId}` (20 kar), Akun `tanpa akun` (10 kar) · sumber matriks role PRD
- **DU-004-3** User (awal), PIC pelapor atas nama karyawan: Name `Rudi Hartono {runId}` (20 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-004-4** User (awal), Pemegang aset: Name `Hari Santoso {runId}` (20 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-004-5** User (awal), Group Manager pelapor: Name `Indra Kusuma {runId}` (20 kar), Role `Group Manager` (13 kar), Group `Gedung B {runId}` (16 kar) · sumber matriks role PRD
- **DU-004-6** User (awal), Master user yang tidak terpakai di tabel: Name `Kirana Putri {runId}` (20 kar), Role `Manage asset & TAG (Read)` (25 kar) · sumber matriks role PRD
- **DU-004-7** Missing record (awal), Laporan PIC atas nama dengan Brand kosong: Asset Name `Unit Alfa {runId}` (17 kar), Group `Gedung A {runId}` (16 kar), Brand `—` (1 kar), Purchase Cost `1000000` (7 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Gita Permata {runId}` (20 kar), Reported By `Rudi Hartono {runId}` (20 kar), Atas nama `Gita Permata {runId}` (20 kar), Reported Date `T0 − 1 hari, pukul 07:15` (24 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-8** Missing record (awal), Missing Source Borrow dengan Brand Alfa: Asset Name `Unit Beta {runId}` (17 kar), Group `Gedung A {runId}` (16 kar), TAG `RFID` (4 kar), Brand `Merk Alfa {runId}` (17 kar), Purchase Cost `2000000` (7 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Hari Santoso {runId}` (20 kar), Last Seen `T0 − 13 hari` (12 kar), Pemindai `Gate B reader {runId}` (21 kar), Reported By `Hari Santoso {runId}` (20 kar), Reported Date `T0 − 10 hari, pukul 09:00` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-9** Missing record (awal), Missing Source Borrow dengan Brand Beta: Asset Name `Unit Gamma {runId}` (18 kar), Group `Gedung B {runId}` (16 kar), TAG `RFID` (4 kar), Brand `Merk Beta {runId}` (17 kar), Purchase Cost `3000000` (7 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Hari Santoso {runId}` (20 kar), Last Seen `T0 − 15 hari` (12 kar), Pemindai `Gate B reader {runId}` (21 kar), Reported By `Indra Kusuma {runId}` (20 kar), Reported Date `T0 − 12 hari, pukul 09:00` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-10** Missing record (awal), Missing yang melewati Long missing after: Asset Name `Unit Delta {runId}` (18 kar), Group `Gedung B {runId}` (16 kar), Brand `Merk Gamma {runId}` (18 kar), Purchase Cost `4000000` (7 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Indra Kusuma {runId}` (20 kar), Reported Date `T0 − 35 hari, pukul 09:00` (25 kar), Days Missing `35 days` (7 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-11** Missing record (awal), Reported Disposal Source Borrow: Asset Name `Unit Epsilon {runId}` (20 kar), Group `Gedung A {runId}` (16 kar), Brand `Merk Delta {runId}` (18 kar), Purchase Cost `5000000` (7 kar), Status `Reported Disposal` (17 kar), Source `Borrow` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 40 hari, pukul 09:00` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-12** Missing record (awal), Missing Source Transfer di Gedung C: Asset Name `Unit Zeta {runId}` (17 kar), Group `Gedung C {runId}` (16 kar), Brand `Merk Epsilon {runId}` (20 kar), Purchase Cost `6000000` (7 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 5 hari, pukul 09:00` (24 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-13** Missing record (awal; dimutasi TC-FA-MISS-E2E-004-tab-active-filter), Missing yang keluar dari saringan Last Updated lama: Asset Name `Unit Eta {runId}` (16 kar), Group `Gedung C {runId}` (16 kar), Brand `Merk Zeta {runId}` (17 kar), Purchase Cost `7000000` (7 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 7 hari, pukul 09:00` (24 kar), Last Updated `sama dengan Reported Date` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-14** Missing record (awal; dimutasi TC-FA-MISS-E2E-004-tab-active-filter), Missing yang masuk ke saringan Last Updated hari ini: Asset Name `Unit Theta {runId}` (18 kar), Group `Gedung C {runId}` (16 kar), Brand `Merk Eta {runId}` (16 kar), Purchase Cost `8000000` (7 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 2 hari, pukul 09:00` (24 kar), Last Updated `sama dengan Reported Date` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-15** Missing record (awal), In Disposal Process Source Manual: Asset Name `Unit Iota {runId}` (17 kar), Group `Gedung A {runId}` (16 kar), Brand `Merk Theta {runId}` (18 kar), Purchase Cost `9000000` (7 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 60 hari, pukul 09:00` (25 kar), Modified By `System` (6 kar) · sumber turunan penulis
- **DU-004-16** Update (dibuat), Catatan investigasi pada record yang masuk saringan: Update `Pemeriksaan ruang arsip dimulai {runId}` (39 kar) · sumber turunan penulis
- **DU-004-17** Update (dibuat), Catatan investigasi pada record yang keluar saringan: Update `Pemeriksaan gudang cadangan selesai {runId}` (43 kar) · sumber turunan penulis
- **DU-004-18** Kata kunci opsi (dicoba), Potongan tengah nama Brand: Kata kunci `psil` (4 kar) · sumber turunan penulis
- **DU-004-19** Kata kunci opsi (dicoba), Brand dengan huruf kapital berbeda: Kata kunci `merk gamma {runId}` (18 kar) · sumber turunan penulis
- **DU-004-20** Kata kunci opsi (dicoba), Kata kunci opsi tanpa hasil: Kata kunci `zzzopsi` (7 kar) · sumber turunan penulis
- **DU-004-21** Kata kunci Search (dicoba), Kata kunci tanpa hasil: Kata kunci `{runId} tidakada` (16 kar) · sumber turunan penulis
- **DU-004-22** Filter Reported Date (dicoba), Rentang di dalam: Dari `T0 − 11 hari` (12 kar), Sampai `T0 − 6 hari` (11 kar) · sumber turunan penulis
- **DU-004-23** Filter Reported Date (dicoba), Rentang tepat di batas awal dan akhir: Dari `T0 − 12 hari` (12 kar), Sampai `T0 − 10 hari` (12 kar) · sumber turunan penulis
- **DU-004-24** Filter Reported Date (dicoba), Rentang satu hari: Dari `T0 − 10 hari` (12 kar), Sampai `T0 − 10 hari` (12 kar) · sumber turunan penulis
- **DU-004-25** Filter Reported Date (dicoba), Rentang di luar semua record: Dari `T0 − 30 hari` (12 kar), Sampai `T0 − 20 hari` (12 kar) · sumber turunan penulis
- **DU-004-26** Filter Last Updated (dicoba), Rentang hari ini: Dari `T0` (2 kar), Sampai `T0` (2 kar) · sumber turunan penulis
- **DU-004-27** Filter Last Updated (dicoba), Rentang lama: Dari `T0 − 8 hari` (11 kar), Sampai `T0 − 6 hari` (11 kar) · sumber turunan penulis
- **DU-004-28** Filter Purchase Cost (dicoba), Min dan Max tepat di nilai record: Min `3000000` (7 kar), Max `5000000` (7 kar) · sumber turunan penulis
- **DU-004-29** Filter Purchase Cost (dicoba), Hanya Min: Min `8000000` (7 kar) · sumber turunan penulis
- **DU-004-30** Filter Purchase Cost (dicoba), Hanya Max: Max `2000000` (7 kar) · sumber turunan penulis
- **DU-004-31** Filter Purchase Cost (dicoba), Min lebih besar dari Max: Min `9000000` (7 kar), Max `1000000` (7 kar) · sumber turunan penulis
- **DU-004-32** Filter Last Seen (dicoba), Rentang yang memuat satu pemindaian: Dari `T0 − 14 hari` (12 kar), Sampai `T0 − 12 hari` (12 kar) · sumber turunan penulis
- **DU-005-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-005-2** Missing record (awal), Record Missing dengan Group Hideable dan Brand Curated yang dicari: Asset Name `Mesin Cuci {runId}` (18 kar), Group `Gudang Konfig {runId}` (21 kar), Brand `Zenith {runId}` (14 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 4 hari, pukul 09:00` (24 kar) · sumber turunan penulis
- **DU-006-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-006-2** Group (awal), Group anak dengan induk untuk hierarki berkas: Name `Gudang Unduh {runId}` (20 kar), Induk `Kantor Unduh {runId}` (20 kar), Hierarki penuh `Kantor Unduh {runId} > Gudang Unduh {runId}` (43 kar) · sumber turunan penulis
- **DU-006-3** User (awal), Pemegang aset: Name `Wulan Prasetyo {runId}` (22 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-006-4** Missing record (awal; 10 record), Sepuluh record Missing dengan Days Missing 1 sampai 10: Asset Name `Unduh Aset {runId}` (18 kar), Group `Gudang Unduh {runId}` (20 kar), Brand `Kenmore {runId}` (15 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − {n} hari, pukul 09:00` (26 kar), Days Missing `{n} days` (8 kar) · sumber turunan penulis
- **DU-006-5** Missing record (awal), Record Waiting for Confirmation pertama yang tersaring keluar: Asset Name `Unduh Tunggu A {runId}` (22 kar), Group `Gudang Unduh {runId}` (20 kar), Brand `Kenmore {runId}` (15 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Wulan Prasetyo {runId}` (22 kar), Reported By `Wulan Prasetyo {runId}` (22 kar), Reported Date `T0 − 20 hari, pukul 08:00` (25 kar), Days Missing `20 days` (7 kar) · sumber turunan penulis
- **DU-006-7** Missing record (awal), Record Waiting for Confirmation kedua yang tersaring keluar: Asset Name `Unduh Tunggu B {runId}` (22 kar), Group `Gudang Unduh {runId}` (20 kar), Brand `Kenmore {runId}` (15 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Wulan Prasetyo {runId}` (22 kar), Reported By `Wulan Prasetyo {runId}` (22 kar), Reported Date `T0 − 20 hari, pukul 08:30` (25 kar), Days Missing `20 days` (7 kar) · sumber turunan penulis
- **DU-006-6** Kata kunci Search (dicoba), Kata kunci tanpa hasil: Kata kunci `{runId} tidakada` (16 kar) · sumber turunan penulis
- **DU-006-8** Missing record (awal), Record Found yang hanya ada di tab History: Asset Name `Unduh Selesai {runId}` (21 kar), Group `Gudang Unduh {runId}` (20 kar), Brand `Kenmore {runId}` (15 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-007-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Tampil `Rina W` (6 kar) · sumber matriks role PRD
- **DU-007-2** User (awal), Last holder yang kemudian dinonaktifkan: Name `Sari Dewi {runId}` (17 kar), Role `Borrower` (8 kar), Status `dinonaktifkan` (13 kar), Tampil `Sari D` (6 kar) · sumber PRD §4.1b Example Data
- **DU-007-3** User (awal), Pelapor record Disposed: Name `Agus Prasetyo {runId}` (21 kar), Role `Manage asset & TAG (Update)` (27 kar), Tampil `Agus P` (6 kar) · sumber PRD §4.1b Example Data
- **DU-007-4** User (awal), Pemegang yang laporannya ditolak: Name `Budi Santoso {runId}` (20 kar), Role `Borrower` (8 kar), Tampil `Budi S` (6 kar) · sumber PRD §4.1b Example Data
- **DU-007-5** User (awal), Pemegang yang membatalkan laporannya: Name `Joko Susilo {runId}` (19 kar), Role `Borrower` (8 kar), Tampil `Joko S` (6 kar) · sumber PRD §4.1b Example Data
- **DU-007-6** Missing record (awal), Record Found dengan Group dan Purchase Cost beku serta nama aset berubah: Asset Name `Kamera Baru {runId}` (19 kar), Nama sebelumnya `Kamera Lama {runId}` (19 kar), Group saat selesai `Gudang Lama {runId}` (19 kar), Group kini `Gudang Baru {runId}` (19 kar), Purchase Cost saat selesai `5000000` (7 kar), Purchase Cost kini `5500000` (7 kar), Category saat selesai `Elektronik {runId}` (18 kar), Category kini `Peralatan Studio {runId}` (24 kar), Asset Value (Commercial) saat selesai `4200000` (7 kar), Asset Value (Commercial) kini `3900000` (7 kar), Asset Value (Fiscal) saat selesai `4000000` (7 kar), Asset Value (Fiscal) kini `3800000` (7 kar), Brand sebelum selesai `Merk Lama {runId}` (17 kar), Brand `Sonora {runId}` (14 kar), Model/Type `Alpha 7 {runId}` (15 kar), TAG `RFID` (4 kar), Labels `Studio {runId}` (14 kar), Division `Produksi {runId}` (16 kar), Measurement `Pcs` (3 kar), Asset Class `Peralatan {runId}` (17 kar), Garansi 1 nama `Garansi Unit {runId}` (20 kar), Garansi 1 sampai `T0 + 300 hari` (13 kar), Garansi 2 nama `Garansi Servis {runId}` (22 kar), Garansi 2 sampai `T0 + 540 hari` (13 kar), Register Date `T0 − 400 hari` (13 kar), Purchase Date `T0 − 410 hari` (13 kar), Warranty Expiry `T0 + 300 hari, dari Warranty until terdekat` (43 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `Sari Dewi {runId}` (17 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 24 hari, pukul 14:10` (25 kar), Duration `6 days` (6 kar) · sumber PRD §4.1b Example Data
- **DU-007-7** Missing record (awal), Record Disposed yang ditutup System tanpa Last holder: Asset Name `Bor Listrik {runId}` (19 kar), Group `Gudang Lama {runId}` (19 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus Prasetyo {runId}` (21 kar), Reported Date `T0 − 70 hari, pukul 08:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 8 hari, pukul 00:00` (24 kar), Duration `62 days` (7 kar) · sumber PRD §4.1b Example Data
- **DU-007-8** Missing record (awal), Record Rejected oleh Aktor Missing: Asset Name `Mesin Foto {runId}` (18 kar), Group `Gudang Lama {runId}` (19 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso {runId}` (20 kar), Reported By `Budi Santoso {runId}` (20 kar), Reported Date `T0 − 10 hari, pukul 08:30` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 9 hari, pukul 09:15` (24 kar), Duration `1 day` (5 kar) · sumber PRD §4.1b Example Data
- **DU-007-9** Missing record (awal), Record Canceled oleh pelapor: Asset Name `Pemindai Gudang {runId}` (23 kar), Group `Gudang Lama {runId}` (19 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susilo {runId}` (19 kar), Reported By `Joko Susilo {runId}` (19 kar), Reported Date `T0 − 12 hari, pukul 13:00` (25 kar), Resolved By `Joko Susilo {runId}` (19 kar), Resolved Date `T0 − 11 hari, pukul 08:20` (25 kar), Duration `1 day` (5 kar) · sumber PRD §4.1b Example Data
- **DU-007-10** Missing record (awal), Record Found pertama untuk aset yang hilang berulang: Asset Name `Gerinda Tangan {runId}` (22 kar), Group `Gudang Lama {runId}` (19 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus Prasetyo {runId}` (21 kar), Reported Date `T0 − 55 hari` (12 kar), Resolved By `Wulan Pertiwi {runId}` (21 kar), Resolved Date `T0 − 50 hari` (12 kar), Duration `5 days` (6 kar) · sumber turunan penulis
- **DU-007-11** Missing record (awal), Record Canceled kedua untuk aset yang sama: Asset Name `Gerinda Tangan {runId}` (22 kar), Group `Gudang Lama {runId}` (19 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso {runId}` (20 kar), Reported By `Budi Santoso {runId}` (20 kar), Reported Date `T0 − 45 hari` (12 kar), Resolved By `Budi Santoso {runId}` (20 kar), Resolved Date `T0 − 44 hari` (12 kar), Duration `1 day` (5 kar) · sumber turunan penulis
- **DU-007-12** User (awal), Penyelesai record Found yang kemudian dinonaktifkan: Name `Wulan Pertiwi {runId}` (21 kar), Role `Manage asset & TAG (Update)` (27 kar), Status `dinonaktifkan sesudah menyelesaikan record DU-007-10` (52 kar), Tampil `Wulan P` (7 kar) · sumber turunan penulis
- **DU-007-13** Garansi aset (awal), Daftar garansi tambahan untuk sort Warranty Expiry: Aset 1 `Bor Listrik {runId}` (19 kar), Garansi 1 nama `Garansi Bor {runId}` (19 kar), Garansi 1 sampai `T0 + 100 hari` (13 kar), Warranty Expiry aset 1 `T0 + 100 hari, dari Warranty until terdekat` (43 kar), Aset 2 `Pemindai Gudang {runId}` (23 kar), Garansi 2 nama `Garansi Pemindai {runId}` (24 kar), Garansi 2 sampai `T0 + 200 hari` (13 kar), Warranty Expiry aset 2 `T0 + 200 hari, dari Warranty until terdekat` (43 kar), Aset 3 `Mesin Foto {runId}` (18 kar), Garansi 3 nama `Garansi Mesin Foto {runId}` (26 kar), Garansi 3 sampai `T0 + 450 hari` (13 kar), Warranty Expiry aset 3 `T0 + 450 hari, dari Warranty until terdekat` (43 kar) · sumber turunan penulis
- **DU-007-14** Kata kunci Search (dicoba), Nama garansi yang tidak boleh ikut dicari: Kata kunci `Garansi Unit {runId}` (20 kar) · sumber turunan penulis
- **DU-007-15** Filter Warranty Expiry (dicoba), Rentang yang memuat dua Warranty until terdekat: Dari `T0 + 150 hari` (13 kar), Sampai `T0 + 350 hari` (13 kar) · sumber turunan penulis
- **DU-008-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-008-2** User (awal), Penyelesai record Rejected: Name `Dian Pertiwi {runId}` (20 kar), Role `Manage asset & TAG (Update)` (27 kar) · sumber matriks role PRD
- **DU-008-3** Missing record (awal), Record Found yang dicari lewat nama, Group, dan tanggal: Asset Name `Papan Tulis Digital {runId}` (27 kar), Group `Gudang Cari {runId}` (19 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 20 hari, pukul 09:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 14 hari, pukul 14:10` (25 kar) · sumber turunan penulis
- **DU-008-4** Missing record (awal), Record Disposed yang ditutup System: Asset Name `Layar Proyektor {runId}` (23 kar), Group `Gudang Lain {runId}` (19 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 50 hari, pukul 09:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 5 hari, pukul 00:00` (24 kar) · sumber turunan penulis
- **DU-008-5** Missing record (awal), Record Rejected yang diselesaikan Dian: Asset Name `Meja Rapat Besar {runId}` (24 kar), Group `Gudang Lain {runId}` (19 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 9 hari, pukul 10:00` (24 kar), Resolved By `Dian Pertiwi {runId}` (20 kar), Resolved Date `T0 − 8 hari, pukul 09:15` (24 kar) · sumber turunan penulis
- **DU-008-6** Kata kunci Search (dicoba), Potongan dari tengah nama: Kata kunci `apan Tulis {runId}` (18 kar) · sumber turunan penulis
- **DU-008-7** Kata kunci Search (dicoba), Nama dengan huruf kapital berbeda: Kata kunci `papan tulis digital {runId}` (27 kar) · sumber turunan penulis
- **DU-008-8** Kata kunci Search (dicoba), Kata kunci tanpa hasil: Kata kunci `{runId} tidakada` (16 kar) · sumber turunan penulis
- **DU-009-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-009-2** User (awal), Pemegang Citra: Name `Citra Lestari {runId}` (21 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-009-3** User (awal), Pemegang Dodi: Name `Dodi Wibowo {runId}` (19 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-009-4** User (awal), Pemegang Eka: Name `Eka Saputra {runId}` (19 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-009-5** User (awal), Pemegang Fajar: Name `Fajar Nugroho {runId}` (21 kar), Role `Borrower` (8 kar) · sumber matriks role PRD
- **DU-009-6** Missing record (awal), Record Found dengan Duration 6: Asset Name `Server Rak Lama {runId}` (23 kar), Label 1 `Audit {runId}` (13 kar), Label 2 `Zebra {runId}` (13 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `Citra Lestari {runId}` (21 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved Date `T0 − 24 hari, pukul 14:10` (25 kar), Duration `6 days` (6 kar) · sumber turunan penulis
- **DU-009-7** Missing record (awal), Record Disposed tanpa Last holder dan Resolved Date terbaru: Asset Name `Genset Portabel {runId}` (23 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 70 hari, pukul 08:00` (25 kar), Resolved Date `T0 − 8 hari, pukul 00:00` (24 kar), Duration `62 days` (7 kar) · sumber turunan penulis
- **DU-009-8** Missing record (awal), Record Rejected dengan Duration sama dengan record Canceled: Asset Name `Printer Label {runId}` (21 kar), Label 1 `Berat {runId}` (13 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Dodi Wibowo {runId}` (19 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 10 hari, pukul 08:30` (25 kar), Resolved Date `T0 − 9 hari, pukul 09:15` (24 kar), Duration `1 day` (5 kar) · sumber turunan penulis
- **DU-009-9** Missing record (awal), Record Canceled dengan Duration sama dengan record Rejected: Asset Name `Scanner Gudang {runId}` (22 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Eka Saputra {runId}` (19 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 12 hari, pukul 13:00` (25 kar), Resolved Date `T0 − 11 hari, pukul 08:20` (25 kar), Duration `1 day` (5 kar) · sumber turunan penulis
- **DU-009-10** Missing record (awal), Record Found dengan Resolved Date tertua: Asset Name `Kompresor Mini {runId}` (22 kar), Label 1 `Cadangan {runId}` (16 kar), Label 2 `Fragile {runId}` (15 kar), Label 3 `Priority {runId}` (16 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Last Holder `Fajar Nugroho {runId}` (21 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 45 hari, pukul 10:00` (25 kar), Resolved Date `T0 − 25 hari, pukul 14:10` (25 kar), Duration `20 days` (7 kar) · sumber turunan penulis
- **DU-010-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-010-2** Missing record (awal), Record Found dengan Group yang sudah dihapus: Asset Name `Kursi Kantor {runId}` (20 kar), Group saat selesai `Gudang Arsip {runId}` (20 kar), Category saat selesai `Elektronik {runId}` (18 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 24 hari, pukul 14:10` (25 kar), Duration `6 days` (6 kar) · sumber turunan penulis
- **DU-010-3** Missing record (awal), Record Disposed dengan Duration terbesar: Asset Name `Lemari Besi {runId}` (19 kar), Group saat selesai `Gudang Arsip {runId}` (20 kar), Category saat selesai `Kendaraan {runId}` (17 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 70 hari, pukul 08:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 8 hari, pukul 00:00` (24 kar), Duration `62 days` (7 kar) · sumber turunan penulis
- **DU-010-4** Missing record (awal), Record Rejected dengan Duration terkecil: Asset Name `Proyektor Kecil {runId}` (23 kar), Group saat selesai `Gudang Aktif {runId}` (20 kar), Category saat selesai `Elektronik {runId}` (18 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 10 hari, pukul 08:30` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 9 hari, pukul 09:15` (24 kar), Duration `1 day` (5 kar) · sumber turunan penulis
- **DU-010-5** Missing record (awal), Record Canceled di antara rentang Resolved Date: Asset Name `Meja Lipat {runId}` (18 kar), Group saat selesai `Gudang Aktif {runId}` (20 kar), Category saat selesai `Furnitur {runId}` (16 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 14 hari, pukul 13:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 11 hari, pukul 08:20` (25 kar), Duration `3 days` (6 kar) · sumber turunan penulis
- **DU-010-6** Filter Resolved Date (dicoba), Rentang tepat di hari awal dan akhir: Dari `T0 − 24 hari` (12 kar), Sampai `T0 − 9 hari` (11 kar) · sumber turunan penulis
- **DU-010-7** Filter Duration (dicoba), Min dan Max tepat di nilai record: Min `6` (1 kar), Max `62` (2 kar) · sumber turunan penulis
- **DU-010-8** Filter Duration (dicoba), Rentang kecil: Min `1` (1 kar), Max `3` (1 kar) · sumber turunan penulis
- **DU-011-1** User (awal), Aktor Total Control spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-011-2** User (awal), Last holder yang kemudian dinonaktifkan: Name `Sari Dewi {runId}` (17 kar), Role `Borrower` (8 kar), Status `dinonaktifkan` (13 kar), Tampil `Sari D` (6 kar) · sumber PRD §4.1b Example Data
- **DU-011-3** Missing record (awal), Record Found dengan Last holder nonaktif: Asset Name `Rak Arsip {runId}` (17 kar), Group `Gudang Berkas {runId}` (21 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `Sari Dewi {runId}` (17 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved By `Rina Wijaya {runId}` (19 kar), Resolved Date `T0 − 24 hari, pukul 14:10` (25 kar) · sumber turunan penulis
- **DU-011-4** Missing record (awal), Record Disposed tanpa Last holder: Asset Name `Troli Dokumen {runId}` (21 kar), Group `Gudang Berkas {runId}` (21 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina Wijaya {runId}` (19 kar), Reported Date `T0 − 70 hari, pukul 08:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 8 hari, pukul 00:00` (24 kar) · sumber turunan penulis
- **DU-011-5** Missing record (awal), Record Canceled oleh pelapor: Asset Name `Lemari Berkas {runId}` (21 kar), Group `Gudang Berkas {runId}` (21 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar), Reported By `Sari Dewi {runId}` (17 kar), Reported Date `T0 − 12 hari, pukul 13:00` (25 kar), Resolved By `Sari Dewi {runId}` (17 kar), Resolved Date `T0 − 11 hari, pukul 08:20` (25 kar) · sumber turunan penulis
- **DU-012-1** Missing record (awal), Record Missing berpenanda Long missing dengan node laporan, Update, deteksi reader dan pengguna, laporan penemu, dan Long missing: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `milik entri ini (dibentuk server)` (33 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi A` (6 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Days Missing `30 days` (7 kar), Node laporan `Reported missing by Rina W` (26 kar), What happened `Laptop tidak ada di meja kerja setelah rapat bulanan` (52 kar), Node Update `Update added by Rina W` (22 kar), Update `Sudah dicek ke ruang arsip lantai 2, belum ditemukan` (52 kar), Last seen reader `T0 − 6 hari, pukul 11:10` (24 kar), Pemindai reader `Gate A reader` (13 kar), Count reader `3` (1 kar), Last seen pengguna `T0 − 2 hari, pukul 15:25` (24 kar), Pemindai pengguna `Agus P` (6 kar), Count pengguna `1` (1 kar), Node penemu `Reported found by Agus P` (24 kar), Location `—` (1 kar), Photo `satu foto terlampir` (19 kar), Days missing node Long missing `30` (2 kar) · sumber PRD §4.1a Example Data
- **DU-012-2** Missing record (awal), Record Waiting for Confirmation dari laporan PIC atas nama pemegang tanpa akun: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `HPT-012-0002` (12 kar), Group `Warehouse` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko S` (6 kar), Reported By `Rudi H (on behalf of Joko S)` (28 kar), Reported Date `T0 − 1 hari, pukul 07:15` (24 kar), Days Missing `1 day` (5 kar), Node laporan `Reported missing by Rudi H on behalf of Joko S` (46 kar), What happened `Hand pallet truck tidak kembali dari area bongkar muat` (54 kar), Status global aset `Missing` (7 kar), Transaction log `entri Reported missing berstatus Waiting for Confirmation` (57 kar) · sumber PRD §4.1a Example Data
- **DU-012-3** Missing record (awal), Record Missing 10 hari dengan dua laporan Disposal: pertama di-Decline, kedua di-Cancel: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `PRJ-012-0003` (12 kar), Group `Branch Surabaya` (15 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 10 hari, pukul 08:00` (25 kar), Days Missing `10 days` (7 kar), Node laporan Disposal `Disposal reported by Agus P` (27 kar), Reason laporan pertama `Aset belum ditemukan sesudah pencarian di seluruh kantor` (56 kar), Node Decline `Disposal report declined by Rina W` (34 kar), Reason Decline `Pencarian di gudang cabang masih berlangsung` (44 kar), Back to Missing Decline `Yes` (3 kar), Reason laporan kedua `Pencarian selesai tanpa hasil` (29 kar), Node Cancel `Disposal report canceled by Agus P` (34 kar), Reason Cancel `Laporan diajukan sebelum pencarian selesai` (42 kar), Back to Missing Cancel `Yes` (3 kar) · sumber PRD §4.1a Example Data
- **DU-012-4** Missing record (awal), Record Disposed di History dengan node laporan Disposal dan Disposed oleh System: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `DRL-012-0004` (12 kar), Group `Warehouse` (9 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Node laporan Disposal `Disposal reported by Agus P` (27 kar), Reason laporan Disposal `Bor hilang lebih dari 60 hari` (29 kar), Node Disposed `Disposed` (8 kar), Disposed oleh `System` (6 kar), Resolved Date `T0 − 8 hari, pukul 13:20` (24 kar) · sumber PRD §4.1b Example Data
- **DU-012-5** Missing record (awal), Record Rejected di History dari laporan pemegang: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `CAM-012-0005` (12 kar), Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Node Reject `Report rejected by Rina W` (25 kar), Reason Reject `Aset terlihat di ruang studio lantai 3` (38 kar), Resolved Date `T0 − 3 hari, pukul 09:30` (24 kar) · sumber PRD §4.1b Example Data
- **DU-012-6** Missing record (awal), Record Canceled di History dari laporan pemegang yang dibatalkan pelapornya: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `SCN-012-0006` (12 kar), Group `Warehouse` (9 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Joko S` (6 kar), Reported By `Joko S` (6 kar), Node Cancel Report `Report canceled by Joko S` (25 kar), Resolved Date `T0 − 5 hari, pukul 16:00` (24 kar) · sumber PRD §4.1b Example Data
- **DU-012-7** Missing record (awal), Record Found di History dengan node Report confirmed by (Closed lines) dan Marked as found by (Manual identification): Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `LPT-012-0007` (12 kar), Group `Finance Room` (12 kar), Status `Found` (5 kar), Source `Reported by holder` (18 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar), Node Confirm `Report confirmed by Rina W` (26 kar), Closed lines `nomor transaksi dan jenis transaksi milik satu baris transaksi berjalan atas Sari D yang ditutup saat Confirm (nomor dibentuk server, milik entri ini)` (150 kar), Node Found `Marked as found by Rina W` (25 kar), Found at `Server Room` (11 kar), Asset Status `Normal` (6 kar), Manual identification `Yes` (3 kar), Note `Ditemukan di laci ruang rapat lantai 2` (38 kar), Photo `satu foto terlampir` (19 kar), Resolved Date `T0 − 1 hari, pukul 10:00` (24 kar) · sumber PRD §4.1b Example Data
- **DU-012-8** User (awal), Pengguna Total Control yang melapor Missing, melapor dan membatalkan laporan Disposal, dan memindai TAG: Name `Agus Prasetyo {runId}` (21 kar), Display `Agus P` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-012-9** Notification (awal), Notifikasi in-app bagi Rina W atas record DU-012-2, belum dibaca: Event `missing_holder_reported` (23 kar), Penerima `Rina W` (6 kar), Record `Hand Pallet Truck {runId}` (25 kar), Status baca `belum dibaca` (12 kar) · sumber PRD §9.8; notification.md §5.1d
- **DU-012-10** Notification (awal), Notifikasi in-app bagi Rina W atas record DU-012-7, belum dibaca: Event `missing_resolved` (16 kar), Penerima `Rina W` (6 kar), Record `Laptop Dell Latitude 5420 {runId}` (33 kar), Status baca `belum dibaca` (12 kar) · sumber PRD §9.8; notification.md §5.1d
- **DU-013-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-013-add-update-tersimpan), Record Missing dengan satu Update awal dari Dewi A sebagai perubahan terakhir: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `PRN-013-0001` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 5 hari, pukul 10:00` (24 kar), Days Missing `5 days` (6 kar), What happened `Printer tidak ada di meja layanan setelah jam kerja` (51 kar), Node Update awal `Update added by Dewi A` (22 kar), Update awal `Printer sudah dicek di ruang server, tidak ada` (46 kar), Waktu Update awal `T0 − 3 hari, pukul 10:00` (24 kar), Modified By `Dewi A` (6 kar), Last Updated `T0 − 3 hari, pukul 10:00` (24 kar), Node laporan `Reported missing by Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-013-2** Update (dibuat), Update pertama yang ditambahkan Rina W: Update `Pemeriksaan lapangan: printer terakhir terlihat di gudang cabang Bekasi` (71 kar), Node `Update added by Rina W` (22 kar) · sumber turunan penulis
- **DU-013-3** Update (dibuat), Update kedua yang ditambahkan Rina W pada record yang sama: Update `Update kedua: pengelola gudang Bekasi mengonfirmasi printer tidak ada di lokasi` (79 kar), Node `Update added by Rina W` (22 kar) · sumber turunan penulis
- **DU-013-4** Missing record (awal), Record Found di History sebagai pembanding aksi yang tidak tersedia pada record selesai: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `MON-013-0004` (12 kar), Group `Head Office` (11 kar), Status `Found` (5 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar) · sumber PRD §4.1b Example Data
- **DU-013-5** Missing record (awal), Record berstatus Waiting for Confirmation sebagai pembanding ketersediaan Add Update menurut status: Name `Forklift Toyota 8FG25 {runId}` (29 kar), Asset ID `FKL-013-0005` (12 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar), Reported Date `T0 − 1 hari, pukul 08:30` (24 kar) · sumber PRD §4.1a Matriks Aksi (status berjalan)
- **DU-013-6** Missing record (awal), Record berstatus Reported Disposal sebagai pembanding ketersediaan Add Update menurut status: Name `Compressor Atlas Copco GA30 {runId}` (35 kar), Asset ID `CMP-013-0006` (12 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 8 hari, pukul 09:10` (24 kar) · sumber PRD §4.1a Matriks Aksi (status berjalan)
- **DU-013-7** Missing record (awal), Record berstatus In Disposal Process sebagai pembanding ketersediaan Add Update menurut status: Name `Genset Perkins 40kVA {runId}` (28 kar), Asset ID `GEN-013-0007` (12 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 12 hari, pukul 14:00` (25 kar) · sumber PRD §4.1a Matriks Aksi (status berjalan)
- **DU-013-8** Missing record (awal), Record berstatus Rejected sebagai pembanding ketersediaan Add Update menurut status: Name `Tablet Samsung Galaxy Tab A8 {runId}` (36 kar), Asset ID `TAB-013-0008` (12 kar), Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar), Reported Date `T0 − 9 hari, pukul 11:15` (24 kar) · sumber PRD §4.1a Matriks Aksi (status selesai)
- **DU-013-9** Missing record (awal), Record berstatus Canceled sebagai pembanding ketersediaan Add Update menurut status: Name `Scanner Honeywell Voyager 1450g {runId}` (39 kar), Asset ID `SCN-013-0009` (12 kar), Group `Head Office` (11 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar), Reported Date `T0 − 7 hari, pukul 10:45` (24 kar) · sumber PRD §4.1a Matriks Aksi (status selesai)
- **DU-013-10** Missing record (awal), Record berstatus Disposed sebagai pembanding ketersediaan Add Update menurut status: Name `Mesin Fotokopi Ricoh MP 2555 {runId}` (36 kar), Asset ID `FTK-013-0010` (12 kar), Group `Head Office` (11 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 20 hari, pukul 15:30` (25 kar) · sumber PRD §4.1a Matriks Aksi (status selesai)
- **DU-014-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-014-review-confirm), Record Waiting for Confirmation dari laporan PIC atas nama pemegang tanpa akun, di-Confirm oleh Rina W: Name `Hydraulic Pallet Jack {runId}` (29 kar), Asset ID `HPJ-014-0001` (12 kar), Group `Warehouse` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko S` (6 kar), Reported By `Rudi H (on behalf of Joko S)` (28 kar), Reported Date `T0 − 2 hari, pukul 07:15` (24 kar), Node laporan `Reported missing by Rudi H on behalf of Joko S` (46 kar), What happened `Hydraulic pallet jack tidak kembali dari area bongkar muat` (58 kar), Node Confirm yang diharapkan `Report confirmed by Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-015-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-015-review-reject), Record Waiting for Confirmation dari laporan pemegang yang di-Reject Rina W: Name `Barcode Scanner Honeywell {runId}` (33 kar), Asset ID `BCS-015-0001` (12 kar), Group `Warehouse` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Reported Date `T0 − 1 hari, pukul 08:30` (24 kar), Node laporan `Reported missing by Budi S` (26 kar), What happened `Barcode scanner tidak ada di meja kasir gudang` (46 kar) · sumber PRD §4.1b Example Data
- **DU-015-2** Missing record (awal), Record Missing pembanding yang tetap di tab Active sebagai sibling: Name `Fire Extinguisher Amerex {runId}` (32 kar), Asset ID `FEX-015-0002` (12 kar), Group `Warehouse` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 4 hari, pukul 09:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-015-3** Reason (dibuat), Reason Reject tepat di batas 360 karakter: Reason `Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegang tidak perlu dilanjutkan sebagai kehilangan resmi dan catatan ini ditulis lengkap supaya admin berikutnya memahami alasan penolakan laporan Aset terlihat kembali di ruang gudang lantai 2 saat pengecekan rutin sehingga laporan kehilangan dari pemegan.` (360 kar), Node `Report rejected by Rina W` (25 kar) · sumber §9.9#r7
- **DU-016-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-016-mark-as-found-normal), Record Missing aset tanpa TAG yang di-Mark as Found dengan Found at di Group lain: Name `Camera DSLR Canon R6 {runId}` (28 kar), Asset ID `CAM-016-0001` (12 kar), Group `Finance Room` (12 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 6 hari, pukul 09:00` (24 kar), TAG `tanpa TAG` (9 kar) · sumber PRD §4.1a Example Data
- **DU-016-2** Missing record (awal; dimutasi TC-FA-MISS-E2E-016-mark-as-found-normal), Record Waiting for Confirmation aset tanpa TAG dari laporan pemegang, dengan baris transaksi pemegang yang masih terbuka: Name `Hand Held Radio Motorola {runId}` (32 kar), Asset ID `HHR-016-0002` (12 kar), Group `Finance Room` (12 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar), Reported Date `T0 − 1 hari, pukul 08:00` (24 kar), TAG `tanpa TAG` (9 kar), Baris transaksi pemegang `masih terbuka` (13 kar) · sumber PRD §4.1a Example Data
- **DU-016-3** Mark as Found (dibuat), Isian dialog Mark as Found untuk DU-016-1: Found at `Server Room` (11 kar), Asset Status `Normal` (6 kar), Note `Ditemukan di rak server lantai 2 saat pemeriksaan rutin` (55 kar), Node `Marked as found by Rina W` (25 kar) · sumber §9.9#r3
- **DU-017-1** Missing record (awal), Record Missing yang dilaporkan Andi P sendiri sebagai Pelapor admin, Last Holder Andi P: Name `Laptop Dell Latitude 7440 {runId}` (33 kar), Asset ID `LPT-017-0001` (12 kar), Group `Finance Room` (12 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Andi P` (6 kar), Reported By `Andi P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar) · sumber matriks role PRD
- **DU-017-2** Missing record (awal), Record Waiting for Confirmation atas karyawan tanpa akun dengan PIC Andi P yang melapor atas nama, hak Aktor Missing Andi P diperoleh sesudah laporan dibuat: Name `Pallet Stacker Electric {runId}` (31 kar), Asset ID `PST-017-0002` (12 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko S` (6 kar), Reported By `Andi P (on behalf of Joko S)` (28 kar), PIC tercatat `Andi P` (6 kar), Reported Date `T0 − 1 hari, pukul 09:20` (24 kar), Hak Aktor Missing Andi P `diperoleh sesudah laporan dibuat` (32 kar) · sumber matriks role PRD
- **DU-017-3** Missing record (awal), Record Waiting for Confirmation yang dilaporkan Rina W (Total Control) sebagai pemegang, hak diperoleh sesudah laporan: Name `Mesin Label Printer {runId}` (27 kar), Asset ID `MLP-017-0003` (12 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Rina W` (6 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 2 hari, pukul 13:40` (24 kar), Hak Aktor Missing Rina W `Total Control diperoleh sesudah laporan dibuat` (46 kar) · sumber matriks role PRD
- **DU-017-4** Missing record (awal), Record Waiting for Confirmation yang dilaporkan Bimo T (Manage asset & TAG Update) sebagai pemegang, hak diperoleh sesudah laporan: Name `Scanner Barcode Zebra {runId}` (29 kar), Asset ID `SBZ-017-0004` (12 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Bimo T` (6 kar), Reported By `Bimo T` (6 kar), Reported Date `T0 − 2 hari, pukul 08:15` (24 kar), Hak Aktor Missing Bimo T `Manage asset & TAG (Update) diperoleh sesudah laporan dibuat` (60 kar) · sumber matriks role PRD
- **DU-017-5** User (awal), Pengguna Manage asset & TAG (Update) yang menjadi Last Holder DU-017-4: Name `Bimo Tirta {runId}` (18 kar), Display `Bimo T` (6 kar), Role `Manage asset & TAG (Update)` (27 kar), Group `Head Office` (11 kar) · sumber matriks role PRD
- **DU-018-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-018-konflik-status-d-mis-06), Record Missing yang diubah Andi P menjadi Found saat Rina W menyiapkan Add Update: Name `Welder Machine Lincoln {runId}` (30 kar), Asset ID `WLD-018-0001` (12 kar), Group `Finance Room` (12 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 4 hari, pukul 09:30` (24 kar) · sumber PRD §4.1a Example Data
- **DU-018-2** Missing record (awal), Record Missing pembanding yang tetap di sub-tab Active: Name `Air Compressor Puma {runId}` (27 kar), Asset ID `CMP-018-0002` (12 kar), Group `Finance Room` (12 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 5 hari, pukul 09:45` (24 kar) · sumber PRD §4.1a Example Data
- **DU-018-3** Update (dicoba), Update yang diajukan Rina W lalu ditolak karena status record sudah berubah: Update `Pemeriksaan bengkel selesai, mesin las tidak ditemukan di lokasi servis` (71 kar), Node `Update added by Rina W` (22 kar) · sumber §6#r10
- **DU-018-4** Mark as Found (dibuat), Isian Mark as Found oleh Andi P atas DU-018-1: Found at `Finance Room` (12 kar), Asset Status `Normal` (6 kar), Node `Marked as found by Andi P` (25 kar) · sumber §6#r10
- **DU-019-1** User (awal; dimutasi TC-FA-MISS-E2E-019-guided-tooltip), Pengguna Total Control dengan flag Guided Tooltip halaman Missing belum terset: Name `Maya Tanjung {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag Guided Tooltip halaman Missing `belum terset` (12 kar) · sumber foundation guided-tooltip.md §16.4
- **DU-019-2** User (awal), Pengguna Total Control dengan flag Guided Tooltip halaman Missing sudah terset: Name `Bayu Ramadhan {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag Guided Tooltip halaman Missing `sudah terset` (12 kar) · sumber foundation guided-tooltip.md §16.4
- **DU-019-3** User (awal; dimutasi TC-FA-MISS-E2E-019-guided-tooltip), Pengguna Total Control dengan flag Guided Tooltip halaman Missing belum terset: Name `Sari Wulandari {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag Guided Tooltip halaman Missing `belum terset` (12 kar) · sumber foundation guided-tooltip.md §16.4
- **DU-019-4** User (awal; dimutasi TC-FA-MISS-E2E-019-guided-tooltip), Pengguna Total Control dengan flag Guided Tooltip halaman Missing belum terset: Name `Dewi Anggraini {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag Guided Tooltip halaman Missing `belum terset` (12 kar) · sumber foundation guided-tooltip.md §16.4
- **DU-019-5** User (awal; dimutasi TC-FA-MISS-E2E-019-guided-tooltip), Pengguna Total Control dengan flag Guided Tooltip halaman Missing belum terset: Name `Hendra Pratama {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag Guided Tooltip halaman Missing `belum terset` (12 kar) · sumber foundation guided-tooltip.md §16.4
- **DU-020-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-020-gating-total-control), record Missing di Group Finance Room, aksi tulis tersedia: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-020-2** Missing record (awal), record Missing di Group Warehouse untuk cakupan seluruh client: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-020-3** Missing record (awal), laporan pemegang menunggu konfirmasi di Group Head Office: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-020-4** Missing record (awal), record Reported Disposal di Group Branch Surabaya: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-020-5** Missing record (awal), record selesai Found di tab History: Name `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `CAM-0001 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1b Example Data
- **DU-020-6** Asset (awal), aset tersedia tanpa record Missing berjalan: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-020-7** Update (dibuat), catatan Update yang ditambahkan Total Control: Update `Terakhir terlihat di lobi kantor pusat {runId}` (46 kar) · sumber turunan penulis
- **DU-021-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-021-gating-group-manager), record Missing di sub-group Finance Room, aksi tulis tersedia: Name `Laptop Lenovo ThinkPad T14 {runId} - 4` (38 kar), Asset ID `LPT-0004 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-021-2** Missing record (awal), record Missing di Group Warehouse di luar binaan: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-021-3** Missing record (awal), laporan pemegang menunggu konfirmasi di sub-group Server Room: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Server Room {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-021-4** Missing record (awal), record Reported Disposal di Group binaan Head Office: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-021-5** Missing record (awal), record selesai Found di tab History: Name `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `CAM-0001 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1b Example Data
- **DU-021-6** Asset (awal), aset tersedia tanpa record Missing berjalan di Group binaan: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-021-7** Update (dibuat), catatan Update yang ditambahkan Group Manager: Update `Dicari di ruang keuangan lantai tiga {runId}` (44 kar) · sumber turunan penulis
- **DU-022-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-022-gating-manage-asset-tag-update), record Missing di Finance Room (hak Update), tempat Add Update: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-022-2** Missing record (awal), record Missing di Warehouse (hanya hak Read): Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-022-3** Missing record (awal; dimutasi TC-FA-MISS-E2E-022-gating-manage-asset-tag-update), record Missing aset tanpa TAG di Server Room, tempat Mark as Found: Name `Laptop Lenovo ThinkPad T14 {runId} - 4` (38 kar), Asset Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `LPT-0004 {runId}` (16 kar), Group `Server Room {runId}` (19 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-022-4** Missing record (awal; dimutasi TC-FA-MISS-E2E-022-gating-manage-asset-tag-update), laporan pemegang menunggu konfirmasi di Server Room, tempat Confirm: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Server Room {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-022-5** Missing record (awal; dimutasi TC-FA-MISS-E2E-022-gating-manage-asset-tag-update), laporan pemegang menunggu konfirmasi di Finance Room, tempat Reject: Name `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `CAM-0001 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso {runId}` (20 kar) · sumber PRD §4.1b Example Data
- **DU-022-6** Missing record (awal), record Reported Disposal di Head Office, dilaporkan pengguna lain: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-022-7** Missing record (awal), record Missing di Group tanpa hak Read aktor: Name `Printer HP LaserJet M404 {runId} - 5` (36 kar), Asset ID `PRN-0005 {runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-022-8** Asset (awal), aset tersedia tanpa record Missing berjalan di Group hak Update: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-022-9** Update (dibuat), catatan Update yang ditambahkan pemegang Update: Update `Terakhir terlihat di ruang rapat lantai dua {runId}` (51 kar) · sumber turunan penulis
- **DU-022-10** Reason (dibuat), alasan penolakan laporan pemegang: Reason `Barang ternyata masih dipakai di gudang cabang {runId}` (54 kar) · sumber turunan penulis
- **DU-022-11** Missing record (awal), record Reported Disposal di Finance Room, dilaporkan aktor ini: Name `Printer Canon imageCLASS {runId}` (32 kar), Group `Finance Room {runId}` (20 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber matriks role PRD
- **DU-023-1** Missing record (awal), record Missing di Finance Room, Report Disposal tersedia: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-023-2** Missing record (awal), record Missing di Warehouse untuk cakupan seluruh client: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-023-3** Missing record (awal), laporan pemegang menunggu konfirmasi, Review tidak tersedia bagi Accounting: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-023-4** Missing record (awal), record Reported Disposal yang dilaporkan oleh aktor Accounting sendiri: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-023-5** Missing record (awal), record Reported Disposal yang dilaporkan pengguna lain: Name `Printer HP LaserJet M404 {runId} - 5` (36 kar), Asset ID `PRN-0005 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-023-6** Missing record (awal), record selesai Found di tab History: Name `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `CAM-0001 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1b Example Data
- **DU-023-7** Asset (awal), aset tersedia tanpa record Missing berjalan: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-024-1** Missing record (awal), record Missing di Finance Room: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-024-2** Missing record (awal), record Missing di Warehouse, Group Read pemegang Manage asset & TAG: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-024-3** Missing record (awal), laporan pemegang menunggu konfirmasi, tempat uji filter Status: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-024-4** Missing record (awal), record Reported Disposal di Branch Surabaya: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-024-5** Missing record (awal), record selesai Found di tab History: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office {runId}` (19 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1b Example Data
- **DU-024-6** Asset (awal), aset tersedia tanpa record Missing berjalan: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-024-7** Missing record (awal), laporan pemegang menunggu konfirmasi di Warehouse, terlihat oleh pemegang Manage asset & TAG (Read): Name `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Warehouse {runId}` (17 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber turunan penulis
- **DU-024-8** Asset (awal), aset tersedia di Group Read tanpa record Missing berjalan: Name `Pallet Jack Crown PE {runId}` (28 kar), Group `Warehouse {runId}` (17 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-025-1** Missing record (awal), record Missing di sub-group Finance Room pada Group di-assign: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-025-2** Missing record (awal), record Missing di Group Warehouse di luar Group di-assign: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-025-3** Missing record (awal), laporan pemegang menunggu konfirmasi di Group di-assign: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-025-4** Missing record (awal), record Reported Disposal di Group di-assign: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-025-5** Missing record (awal), record selesai Found di tab History: Name `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `CAM-0001 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1b Example Data
- **DU-025-6** Asset (awal), aset tersedia tanpa record Missing berjalan di Group di-assign: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar) · sumber turunan penulis
- **DU-026-1** Missing record (awal), record Missing yang tidak boleh terlihat oleh aktor tanpa capability: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-027-1** Missing record (awal), laporan pemegang menunggu konfirmasi, aksi Confirm ditolak setelah capability dicabut: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-027-2** Missing record (awal), record Missing tempat aksi tulis disembunyikan setelah pencabutan: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-028-1** Client (awal), entitas khusus berstatus Suspended: Name `Klien Suspended {runId}` (23 kar), Status `Suspended` (9 kar) · sumber foundation functions/entity-isolation.md §18.8
- **DU-028-2** Missing record (awal), record Missing yang tetap terbaca pada Client Suspended: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-028-3** Missing record (awal), laporan pemegang menunggu konfirmasi, Confirm ditolak karena Client Suspended: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar) · sumber PRD §4.1a Example Data
- **DU-029-1** Client (awal), entitas khusus berplan Starter: Name `Klien Starter {runId}` (21 kar), Plan `Starter` (7 kar) · sumber foundation product/licensing/plans.md §2.2
- **DU-029-2** Missing record (awal; dimutasi TC-FA-MISS-E2E-029-plan-starter), record Missing dengan TAG QR, tempat Report Disposal terkunci dan Add Update: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-029-3** Missing record (awal), record Missing dengan pairing lama RFID, NFC, BLE, GPS, dan QR: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `RFID, NFC, BLE, GPS, QR` (23 kar) · sumber turunan penulis
- **DU-029-4** Missing record (awal), record Reported Disposal dengan pairing lama RFID saja: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), TAG `RFID` (4 kar) · sumber turunan penulis
- **DU-029-5** Update (dibuat), catatan Update pada plan Starter: Update `Terakhir terlihat di lobi cabang {runId}` (40 kar) · sumber turunan penulis
- **DU-030-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-030-scan-found-asset), record Missing ber-TAG dalam cakupan, selesai lewat Scan Found Asset: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `LPT-0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-030-2** Missing record (awal), record Missing ber-TAG di Group di luar cakupan aktor: Name `Hand Pallet Truck {runId} - 3` (29 kar), Asset ID `HPT-0003 {runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-030-3** Asset (awal), aset ber-TAG tanpa record Missing berjalan: Name `Scanner Zebra DS2208 {runId} - 2` (32 kar), Asset Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `SCN-0002 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar), TAG `QR` (2 kar) · sumber turunan penulis
- **DU-030-4** Missing record (awal), record Reported Disposal ber-TAG dalam cakupan: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `PRJ-0007 {runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-030-5** Missing record (awal), record Missing ber-TAG dengan aktor sebagai Last holder: Name `Monitor LG 27UL500 {runId} - 11` (31 kar), Asset ID `MON-0011 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `aktor spec ini` (14 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-030-6** Missing record (awal), record Missing ber-TAG, tempat uji TAG bukan milik aset: Name `Printer HP LaserJet M404 {runId} - 5` (36 kar), Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `PRN-0005 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber PRD §4.1a Example Data
- **DU-030-7** Missing record (awal), record Waiting for Confirmation ber-TAG dalam cakupan, discan lewat Scan Found Asset: Asset Name `Tablet Samsung Galaxy Tab {runId}` (33 kar), Group `Finance Room {runId}` (20 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewi {runId}` (17 kar), TAG `QR` (2 kar) · sumber §4.1#r3
- **DU-030-8** Missing record (awal), record Reported Disposal ber-TAG di Group di luar cakupan aktor: Asset Name `Genset Honda EU22 {runId}` (25 kar), Group `Warehouse {runId}` (17 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber §6#p2
- **DU-030-9** Missing record (awal), record Reported Disposal ber-TAG dalam cakupan dengan aktor sebagai Last holder: Asset Name `Compressor Atlas Copco {runId}` (30 kar), Group `Finance Room {runId}` (20 kar), Status `Reported Disposal` (17 kar), Source `Borrow` (6 kar), Last Holder `aktor spec ini` (14 kar), TAG `QR` (2 kar) · sumber §6#p2
- **DU-030-10** Missing record (awal), record In Disposal Process ber-TAG dalam cakupan: Asset Name `Printer Brother HL-L2350 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), TAG `QR` (2 kar) · sumber §6#r7
- **DU-030-11** Asset (awal), aset ber-TAG dengan record sebelumnya Found, tanpa record Missing berjalan: Asset Name `Camera Canon EOS {runId}` (24 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar), TAG `QR` (2 kar) · sumber §6#r5
- **DU-030-12** Asset (awal), aset ber-TAG dengan record sebelumnya Disposed, tanpa record Missing berjalan: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Finance Room {runId}` (20 kar), Status `Disposed` (8 kar), TAG `QR` (2 kar) · sumber §6#r5
- **DU-030-13** Asset (awal), aset ber-TAG dengan record sebelumnya Rejected, tanpa record Missing berjalan: Asset Name `Speaker JBL PartyBox {runId}` (28 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar), TAG `QR` (2 kar) · sumber §6#r5
- **DU-030-14** Asset (awal), aset ber-TAG dengan record sebelumnya Canceled, tanpa record Missing berjalan: Asset Name `Webcam Logitech C920 {runId}` (28 kar), Group `Finance Room {runId}` (20 kar), Status `Available` (9 kar), TAG `QR` (2 kar) · sumber §6#r5
- **DU-030-15** Asset (awal), aset ber-TAG di Group di luar cakupan aktor, tanpa record Missing berjalan: Asset Name `Welding Machine Lincoln {runId}` (31 kar), Group `Warehouse {runId}` (17 kar), Status `Available` (9 kar), TAG `QR` (2 kar) · sumber §6#p2
- **DU-031-1** Asset (awal; dimutasi TC-FA-MISS-E2E-031-report-missing-dep-asset), Aset ber-TAG QR belum pernah terpindai dengan Activity Lock Under Maintenance, tanpa pemegang, dilaporkan hilang dari Asset List: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), TAG `QR` (2 kar), Activity Lock `Under Maintenance` (17 kar), Pemegang `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-031-2** Asset (awal; dimutasi TC-FA-MISS-E2E-031-report-missing-dep-asset), Aset yang dipegang Total Control pelapor, dilaporkan hilang dari Asset Detail: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Pemegang `Rina W` (6 kar) · sumber PRD §4.1a Example Data
- **DU-031-3** Asset (awal; dimutasi TC-FA-MISS-E2E-031-report-missing-dep-asset), Aset tanpa pemegang yang ikut laporan banyak aset dan menjadi pembanding menu aksi: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Pemegang `—` (1 kar) · sumber PRD §4.1a Example Data
- **DU-031-4** Asset (awal; dimutasi TC-FA-MISS-E2E-031-report-missing-dep-asset), Aset yang dipegang pengguna lain dan ikut laporan banyak aset: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Pemegang `Sari Dewanti {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-031-5** Asset (awal), Aset yang sudah punya record Missing berjalan, dipakai sebagai aset yang dilewati: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Branch Surabaya` (15 kar), Record `Missing berjalan, pelapor Rina W` (32 kar) · sumber PRD §4.1a Example Data
- **DU-031-6** Asset (awal), Aset dengan record Missing berjalan yang Last holder-nya sudah dinonaktifkan; Last holder sudah dinonaktifkan: Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya` (15 kar), Record `Missing berjalan` (16 kar), Last holder `Budi Santoso {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-031-7** Asset (awal; dimutasi TC-FA-MISS-E2E-031-report-missing-dep-asset), Aset tanpa record yang dilaporkan bersamaan oleh dua pelapor: Name `Server Dell PowerEdge {runId}` (29 kar), Group `Head Office` (11 kar), Pemegang `—` (1 kar) · sumber turunan penulis
- **DU-031-8** Asset (awal), Aset Unmanaged tanpa record yang boleh dihapus, dipakai membuktikan penolakan bulk Delete Asset Data seluruhnya: Name `Meja Rapat Kayu {runId}` (23 kar), Group `Head Office` (11 kar), Asset Status `Unmanaged` (9 kar) · sumber turunan penulis
- **DU-031-9** Asset (awal), Aset dengan satu record Missing yang sudah selesai Found: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Record `Found` (5 kar) · sumber PRD §4.1b Example Data
- **DU-031-10** User (awal), Total Control kedua yang memicu laporan bersamaan: Name `Dewi Anggraini {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-031-11** Missing (dibuat), Isian What happened laporan satu aset dari Asset List: What happened `Laptop tidak ditemukan saat pengecekan pagi di ruang Finance` (60 kar) · sumber turunan penulis
- **DU-031-12** Missing (dibuat), Isian What happened laporan dari Asset Detail: What happened `Hand pallet truck tidak kembali ke gudang setelah dipakai` (57 kar) · sumber turunan penulis
- **DU-031-13** Missing (dibuat), Isian What happened laporan banyak aset: What happened `Printer dan monitor tidak ada di ruang kerja setelah renovasi` (61 kar) · sumber turunan penulis
- **DU-031-14** Missing (dicoba), Isian What happened laporan yang seluruh asetnya sudah dilaporkan: What happened `Pengecekan ulang aset yang sudah dilaporkan hilang` (50 kar) · sumber turunan penulis
- **DU-031-15** Missing (dibuat), Isian What happened laporan pertama dari pelapor lain pada race: What happened `Server tidak ditemukan di rak setelah pemindahan ruang server` (61 kar) · sumber turunan penulis
- **DU-031-16** Missing (dicoba), Isian What happened laporan kedua yang kalah pada race: What happened `Server tidak ada di ruang server saat inventarisasi` (51 kar) · sumber turunan penulis
- **DU-031-17** Asset (awal), Aset yang dipegang Total Control pelapor, dibuka dialog Report Missing tanpa dikirim: Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Warehouse` (9 kar), Pemegang `Rina W` (6 kar) · sumber turunan penulis
- **DU-032-1** Asset (awal; dimutasi TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset), Aset ditugaskan ke pemegang berakun, dilaporkan lalu dibatalkan: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Pemegang `Joko Santoso {runId}` (20 kar) · sumber PRD §4.1b Example Data
- **DU-032-2** Asset (awal; dimutasi TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset), Aset dipinjam pemegang berakun, dilaporkan dari tab Borrowed lalu dikonfirmasi Total Control: Name `Handheld Honeywell CT60 {runId}` (31 kar), Group `Warehouse` (9 kar), Pemegang `Joko Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-032-3** Asset (awal; dimutasi TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset), Aset ditugaskan ke karyawan tanpa akun, dilaporkan PIC atas nama: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Pemegang `Dedi Kurniawan {runId}` (22 kar), PIC `Rudi Hartono {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-032-4** Asset (awal; dimutasi TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset), Aset dipegang pengguna dengan hak Manage asset & TAG (Update): Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office` (11 kar), Pemegang `Andi Pratama {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-032-5** Asset (awal), Aset dengan record Waiting for Confirmation lama dari pelapor yang sudah dinonaktifkan: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Pemegang `Tono Wibowo {runId}` (19 kar), Record `Waiting for Confirmation` (24 kar), Waktu laporan `T0 − 40 hari` (12 kar) · sumber PRD §4.1a Example Data
- **DU-032-6** Asset (awal), Aset dengan laporan pemegang yang sudah Rejected beserta reason: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Pemegang `Joko Santoso {runId}` (20 kar), Record `Rejected` (8 kar), Reason `Aset terlihat di gudang cabang` (30 kar) · sumber PRD §4.1b Example Data
- **DU-032-7** Asset (awal; dimutasi TC-FA-MISS-E2E-032-laporan-pemegang-dep-my-asset), Aset karyawan tanpa akun dengan record Waiting for Confirmation dari PIC lama dan PIC pengganti: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Pemegang `Gita Permata {runId}` (20 kar), PIC pengganti `Wulan Sari {runId}` (18 kar), Record `Waiting for Confirmation, pelapor Rudi Hartono {runId}` (54 kar) · sumber PRD §4.1a Example Data
- **DU-032-8** Missing (dibuat), Isian What happened laporan: What happened `Scanner tidak ada di loker setelah shift malam` (46 kar) · sumber turunan penulis
- **DU-032-9** Missing (dibuat), Isian What happened laporan: What happened `Handheld tertinggal di kendaraan operasional` (44 kar) · sumber turunan penulis
- **DU-032-10** Missing (dibuat), Isian What happened laporan: What happened `Projector hilang dari ruang rapat setelah acara` (47 kar) · sumber turunan penulis
- **DU-032-11** Missing (dibuat), Isian What happened laporan: What happened `Laptop tidak ada di meja setelah perjalanan dinas` (49 kar) · sumber turunan penulis
- **DU-032-12** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-032-13** User (awal), Pengguna PIC: Name `Rudi Hartono {runId}` (20 kar), Role `PIC` (3 kar), Cakupan `aset karyawan tanpa akun yang ia wakili` (39 kar) · sumber matriks role PRD
- **DU-032-14** User (awal), Pengguna PIC pengganti: Name `Wulan Sari {runId}` (18 kar), Role `PIC pengganti` (13 kar), Cakupan `aset karyawan tanpa akun yang ia wakili` (39 kar) · sumber matriks role PRD
- **DU-032-15** User (awal), Pengguna Manage asset & TAG (Update): Name `Andi Pratama {runId}` (20 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group aset yang dipegangnya` (27 kar) · sumber matriks role PRD
- **DU-032-16** User (awal), Pengguna pemegang, sudah dinonaktifkan: Name `Tono Wibowo {runId}` (19 kar), Role `pemegang, sudah dinonaktifkan` (29 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-033-1** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dengan baris Borrow Borrowed yang dilaporkan Aktor Borrow: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Borrow `Borrowed` (8 kar), Peminjam `Joko Santoso {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-033-2** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dengan baris Borrow Waiting for handover yang dilaporkan Aktor Borrow: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Borrow `Waiting for handover` (20 kar), Peminjam `Joko Santoso {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-033-3** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dengan baris Borrow Overdue dan laporan pemegang Waiting for Confirmation untuk di-Confirm: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Borrow `Overdue` (7 kar), Peminjam `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1b Example Data
- **DU-033-4** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dengan baris Borrow Borrowed dan laporan pemegang Waiting for Confirmation untuk di-Reject: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Borrow `Borrowed` (8 kar), Peminjam `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-033-5** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset tanpa TAG dengan baris Borrow Borrowed dan laporan pemegang Waiting for Confirmation untuk Mark as Found: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), TAG `—` (1 kar), Borrow `Borrowed` (8 kar), Peminjam `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-033-6** Asset (awal), Aset dengan laporan pemegang Waiting for Confirmation atas pemegang yang sudah dinonaktifkan: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Borrow `Borrowed` (8 kar), Peminjam `Tono Wibowo {runId}` (19 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-033-7** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dengan laporan pemegang Waiting for Confirmation yang dibatalkan pelapor: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Borrow `Borrowed` (8 kar), Peminjam `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1b Example Data
- **DU-033-8** User (awal), Aktor Borrow tanpa Manage asset & TAG (Update): Name `Maya Putri {runId}` (18 kar), Role `Aktor Borrow` (12 kar), Cakupan `aset dalam cakupan transaksi Borrow` (35 kar) · sumber matriks role PRD
- **DU-033-9** User (awal), Pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-033-10** User (awal), Pemegang yang sudah dinonaktifkan: Name `Tono Wibowo {runId}` (19 kar), Role `pemegang, sudah dinonaktifkan` (29 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-033-11** Missing (dibuat), Isian What happened laporan Aktor Borrow: What happened `Laptop tidak dikembalikan dan tidak ditemukan di lokasi peminjam` (64 kar) · sumber turunan penulis
- **DU-033-12** Missing (dibuat), Isian What happened laporan baris Waiting for handover: What happened `Hand pallet truck tidak diserahkan dan hilang dari gudang` (57 kar) · sumber turunan penulis
- **DU-033-13** Missing (dibuat), Alasan Reject laporan pemegang: Reason `Aset masih dipakai di lapangan` (30 kar) · sumber turunan penulis
- **DU-033-14** Missing (dibuat), Catatan Mark as Found: Note `Ditemukan di mobil operasional` (30 kar) · sumber turunan penulis
- **DU-033-15** Asset (awal; dimutasi TC-FA-MISS-E2E-033-efek-transaksi-dep-borrow), Aset dalam Draft Borrow yang dilaporkan hilang: Name `Tablet Samsung Galaxy Tab S8 {runId}` (36 kar), Group `Head Office` (11 kar), Draft `Draft Peminjaman Tablet {runId}` (31 kar) · sumber turunan penulis
- **DU-033-16** Missing (dibuat), Isian What happened laporan atas aset dalam Draft Borrow: What happened `Tablet tidak ada di ruang rapat setelah sesi pelatihan` (54 kar) · sumber turunan penulis
- **DU-033-17** Asset (awal), Aset pembanding milik pemegang yang dinonaktifkan tanpa record Missing, tetap masuk Return list offboarding: Name `Keyboard Logitech MX Keys {runId}` (33 kar), Group `Head Office` (11 kar), Borrow `Borrowed` (8 kar), Peminjam `Tono Wibowo {runId}` (19 kar) · sumber turunan penulis
- **DU-033-18** User (awal), Pengguna tanpa hak Aktor Borrow dan tanpa hak Aktor Missing yang bisa melihat halaman Borrow: Name `Hendra Gunawan {runId}` (22 kar), Role `lihat Borrow tanpa Aktor Borrow dan tanpa Aktor Missing` (55 kar), Cakupan `halaman Borrow` (14 kar) · sumber matriks role PRD
- **DU-034-1** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset dengan baris Assignment Assigned yang dilaporkan Aktor Assignment: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Assignment `Assigned` (8 kar), Penerima `Joko Santoso {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-034-2** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset dengan satu permintaan Assignment menunggu yang dibatalkan oleh laporan: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Assignment `Waiting for Handover` (20 kar) · sumber PRD §4.1a Example Data
- **DU-034-3** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset dalam Draft Assignment yang dilaporkan Total Control: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Draft `Draft Penugasan Printer {runId}` (31 kar) · sumber PRD §4.1a Example Data
- **DU-034-4** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset dengan baris Assigned dan laporan pemegang Waiting for Confirmation: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Assignment `Assigned` (8 kar), Penerima `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-034-5** User (awal), Pengguna Aktor Assignment tanpa Manage asset & TAG (Update): Name `Nina Aulia {runId}` (18 kar), Role `Aktor Assignment tanpa Manage asset & TAG (Update)` (50 kar), Cakupan `aset dalam cakupan transaksi Assignment` (39 kar) · sumber matriks role PRD
- **DU-034-6** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-034-7** Missing (dibuat), Isian What happened laporan baris Assigned: What happened `Laptop tidak ada di meja penerima setelah pindah ruangan` (56 kar) · sumber turunan penulis
- **DU-034-8** Missing (dibuat), Isian What happened laporan aset dengan permintaan menunggu: What happened `Hand pallet truck hilang dari gudang sebelum diserahkan` (55 kar) · sumber turunan penulis
- **DU-034-9** Missing (dibuat), Isian What happened laporan Total Control atas aset dalam Draft: What happened `Printer tidak ada di ruang cetak setelah renovasi` (49 kar) · sumber turunan penulis
- **DU-034-10** Asset (awal), Aset Assigned yang dibuka dialog Report Missing-nya tanpa dikirim: Name `Tablet Samsung Galaxy Tab S8 {runId}` (36 kar), Group `Head Office` (11 kar), Assignment `Assigned` (8 kar), Penerima `Joko Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-034-11** Asset (awal), Aset dalam Draft Assignment yang dibuka dialog Report Missing-nya tanpa dikirim: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Draft `Draft Penugasan Scanner {runId}` (31 kar) · sumber turunan penulis
- **DU-034-12** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset dengan baris Assignment Waiting for Approval yang dilaporkan hilang: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Assignment `Waiting for Approval` (20 kar) · sumber turunan penulis
- **DU-034-13** Asset (awal; dimutasi TC-FA-MISS-E2E-034-efek-transaksi-dep-transactions-assignment), Aset pendamping dalam Draft Assignment yang tidak dilaporkan hilang: Name `Mouse Logitech MX Master 3 {runId}` (34 kar), Group `Head Office` (11 kar), Draft `Draft Penugasan Printer {runId}` (31 kar) · sumber turunan penulis
- **DU-034-14** Missing (dibuat), Isian What happened laporan atas aset dengan permintaan Waiting for Approval: What happened `Kamera tidak ada di ruang arsip sebelum permintaan disetujui` (60 kar) · sumber turunan penulis
- **DU-035-1** Asset (awal; dimutasi TC-FA-MISS-E2E-035-efek-transaksi-dep-transactions-transfer), Aset tanpa pemegang dengan baris Transfer In transit yang dilaporkan Aktor Transfer: Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya` (15 kar), Transfer `In transit` (10 kar) · sumber PRD §4.1a Example Data
- **DU-035-2** User (awal), Pengguna Aktor Transfer tanpa Manage asset & TAG (Update): Name `Rudi Hartono {runId}` (20 kar), Role `Aktor Transfer tanpa Manage asset & TAG (Update)` (48 kar), Cakupan `aset dalam cakupan transaksi Transfer` (37 kar) · sumber matriks role PRD
- **DU-035-3** Missing (dibuat), Isian What happened laporan baris In transit: What happened `Kendaraan tidak sampai di cabang tujuan setelah pengiriman` (58 kar) · sumber turunan penulis
- **DU-036-1** Asset (awal; dimutasi TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal), Aset dengan record Missing yang di-Report Disposal lalu Cancel Disposal Report: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-036-2** Asset (awal; dimutasi TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal), Aset dengan record Missing yang di-Report Disposal lalu di-Decline: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-036-3** Asset (awal; dimutasi TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal), Aset dengan record Missing yang di-Dispose sampai In Disposal Process: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar) · sumber PRD §4.1b Example Data
- **DU-036-4** Asset (awal), Aset dengan record Disposed di History: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Record `Disposed` (8 kar), Resolved By `System` (6 kar), Disposal No `dibentuk server milik entri ini` (31 kar) · sumber PRD §4.1b Example Data
- **DU-036-5** Asset (awal), Aset dengan record Missing melewati Long missing after: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar), Dilaporkan `T0 − 34 hari` (12 kar) · sumber PRD §4.1a Example Data
- **DU-036-6** Asset (awal; dimutasi TC-FA-MISS-E2E-036-report-disposal-dep-transactions-disposal), Aset tanpa record Missing dengan Disposal Report Reported: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Disposal Report `Reported` (8 kar) · sumber turunan penulis
- **DU-036-7** Disposal (dibuat), Reason Report Disposal untuk Cancel Disposal Report: Reason `Aset tidak ditemukan setelah penelusuran tiga minggu` (52 kar) · sumber turunan penulis
- **DU-036-8** Disposal (dibuat), Reason Report Disposal untuk Decline: Reason `Aset hilang saat pemindahan gudang` (34 kar) · sumber turunan penulis
- **DU-036-9** Disposal (dibuat), Reason Report Disposal untuk Dispose: Reason `Aset tidak ada di lokasi terakhir` (33 kar) · sumber turunan penulis
- **DU-036-10** Disposal (dibuat), Reason Decline Report: Reason Decline `Aset masih dalam penelusuran` (28 kar) · sumber turunan penulis
- **DU-036-11** Missing (dibuat), Isian What happened laporan atas aset dengan Disposal Report: What happened `Kamera hilang dari ruang studio setelah sesi foto` (49 kar) · sumber turunan penulis
- **DU-037-1** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset Missing satu Group yang diproses bulk: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-037-2** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset Missing satu Group yang diproses bulk: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-037-3** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset Missing satu Group yang diproses bulk: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-037-4** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Satu aset Missing yang diproses bulk bentuk tunggal: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-037-5** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset Missing yang diproses dalam seleksi campuran: Name `Hand Pallet Truck {runId}` (25 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-037-6** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset Missing yang diproses dalam seleksi campuran: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber PRD §4.1b Example Data
- **DU-037-7** Asset (awal), Aset yang dilewati karena record bukan Missing: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Record `Reported Disposal` (17 kar) · sumber PRD §4.1b Example Data
- **DU-037-8** Asset (awal), Aset yang dilewati karena pemakai adalah Last holder: Name `Toyota Innova {runId}` (21 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar), Last holder `Rina W` (6 kar) · sumber PRD §4.1a Example Data
- **DU-037-9** Asset (awal), Aset Missing di Group Warehouse untuk seleksi lintas Group: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar) · sumber PRD §4.1b Example Data
- **DU-037-10** Asset (awal), Aset Missing di Group Head Office untuk seleksi lintas Group: Name `Server Dell PowerEdge {runId}` (29 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber turunan penulis
- **DU-037-11** User (awal), Total Control yang juga Aktor Disposal dan Last holder aset Toyota: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-037-12** Disposal (dibuat), Reason bulk banyak record: Reason `Aset dilaporkan hilang bersamaan dari satu lokasi` (49 kar) · sumber turunan penulis
- **DU-037-13** Disposal (dibuat), Reason bulk satu item: Reason `Proyektor tidak ditemukan setelah acara kantor` (46 kar) · sumber turunan penulis
- **DU-037-14** Disposal (dibuat), Reason bulk campuran: Reason `Aset dari beberapa lokasi dilaporkan untuk disposal` (51 kar) · sumber turunan penulis
- **DU-037-15** Asset (awal; 2 record), Aset tambahan supaya jumlah Asset Active ber-runId melebihi satu halaman berukuran 10: Name `Kursi Kantor {n} {runId}` (24 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber turunan penulis
- **DU-037-16** Asset (awal; dimutasi TC-FA-MISS-E2E-037-bulk-report-disposal-dep-transactions-disposal), Aset yang di-Report Disposal dengan klik ganda konfirmasi: Name `Bor Listrik Makita {runId}` (26 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar) · sumber turunan penulis
- **DU-037-17** Disposal (dibuat), Isian Reason Report Disposal untuk uji klik ganda: Reason `Aset tidak ditemukan setelah audit gudang` (41 kar) · sumber turunan penulis
- **DU-038-1** Asset (awal; dimutasi TC-FA-MISS-E2E-038-mark-as-found-damaged-dep-damaged), Aset tanpa TAG berkondisi Normal dengan record Missing yang ditemukan rusak: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Record `Missing` (7 kar), Condition sebelum laporan `Normal` (6 kar) · sumber PRD §4.1a Example Data
- **DU-038-2** Asset (awal; dimutasi TC-FA-MISS-E2E-038-mark-as-found-damaged-dep-damaged), Aset asal Damaged + Missing dengan Damage record yang ditahan: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `ditahan` (7 kar) · sumber PRD §4.1a Example Data
- **DU-038-3** Asset (awal; dimutasi TC-FA-MISS-E2E-038-mark-as-found-damaged-dep-damaged), Aset asal Damaged dengan laporan pemegang Waiting for Confirmation yang di-Reject: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Record `Waiting for Confirmation` (24 kar), Pelapor `Joko Santoso {runId}` (20 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `ditahan` (7 kar) · sumber PRD §4.1a Example Data
- **DU-038-4** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-038-5** Damaged (dibuat), Foto dan Note kerusakan aset Normal ditemukan rusak: Damaged Photo `foto-kerusakan-laptop.png` (25 kar), Note `Layar retak dan engsel patah saat ditemukan` (43 kar) · sumber turunan penulis
- **DU-038-6** Damaged (dibuat), Foto dan Note kerusakan aset asal Damaged + Missing: Damaged Photo `foto-kerusakan-printer.png` (26 kar), Note `Rumah printer retak sejak sebelum hilang` (40 kar) · sumber turunan penulis
- **DU-038-7** Missing (dibuat), Reason Reject laporan pemegang: Reason `Monitor masih dipakai dalam kondisi rusak` (41 kar) · sumber turunan penulis
- **DU-038-8** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-039-1** Asset (awal; dimutasi TC-FA-MISS-E2E-039-mark-as-found-tanpa-scan-dep-tag), Aset ber-TAG QR dengan record Missing yang ditemukan lewat identifikasi manual: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), TAG `QR` (2 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-039-2** Asset (awal; dimutasi TC-FA-MISS-E2E-039-mark-as-found-tanpa-scan-dep-tag), Aset ber-TAG QR dengan record Missing yang ditemukan lewat scan setelah Report TAG: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), TAG `QR` (2 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-039-3** Tag (dibuat), Reason Report TAG dan Note Mark as Found aset pertama: Reason Report TAG `TAG QR rusak terkena air` (24 kar), Note `Ditemukan di laci meja kerja` (28 kar) · sumber turunan penulis
- **DU-039-4** Tag (dibuat), Reason Report TAG dan Note Mark as Found aset kedua: Reason Report TAG `TAG QR tergores sehingga tidak terbaca` (38 kar), Note `Ditemukan di rak gudang belakang` (32 kar) · sumber turunan penulis
- **DU-039-5** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-040-1** Group (awal), Group yang dirujuk record Missing berjalan, penghapusannya ditolak: Name `Gudang Cabang Surabaya {runId}` (30 kar), Aset `Toyota Innova {runId}` (21 kar), Record `Missing berjalan` (16 kar), Missing Log `satu node Reported missing by` (29 kar) · sumber turunan penulis
- **DU-040-2** Group (awal; dimutasi TC-FA-MISS-E2E-040-hapus-group-dep-settings-groups), Group tanpa aset dan tanpa record yang dihapus: Name `Ruang Server Cadangan {runId}` (29 kar) · sumber turunan penulis
- **DU-040-3** Group (awal; dimutasi TC-FA-MISS-E2E-040-hapus-group-dep-settings-groups), Group yang hanya dirujuk record History Found yang dihapus: Name `Ruang Arsip {runId}` (19 kar), Aset `Camera Canon EOS {runId}` (24 kar), Record `Found` (5 kar) · sumber turunan penulis
- **DU-040-4** User (awal), Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-041-1** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dipegang pengguna lain, dilaporkan Pelapor admin: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Pemegang `Sari Dewanti {runId}` (20 kar) · sumber turunan penulis
- **DU-041-2** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset tanpa pemegang, dilaporkan Pelapor admin: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-041-3** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dipegang pemegang tanpa hak, dilaporkan pemegang lalu di-Confirm: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Pemegang `Joko Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-041-4** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dipegang pemegang dengan hak Aktor Missing, dilaporkan sebagai Pelapor admin: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office` (11 kar), Pemegang `Andi Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-041-5** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dengan laporan pemegang Waiting for Confirmation yang di-Reject: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Pemegang `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-041-6** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset tanpa TAG dengan record Missing dan notifikasi missing_reported belum terbaca, ditemukan: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar), Notifikasi `missing_reported belum terbaca` (30 kar) · sumber turunan penulis
- **DU-041-7** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dengan record In Disposal Process yang Disposal-nya dieksekusi: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Record `In Disposal Process` (19 kar) · sumber turunan penulis
- **DU-041-8** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset dengan record Missing yang di-Report Disposal: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar), Notifikasi `tanpa notifikasi event missing_*` (32 kar) · sumber turunan penulis
- **DU-041-9** Asset (awal), Aset dengan record Missing dan node Detected by scan yang notifikasinya sudah terkirim: Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya` (15 kar), Record `Missing` (7 kar), Node `Detected by scan` (16 kar), Notifikasi `missing_detected terkirim` (25 kar) · sumber turunan penulis
- **DU-041-10** Asset (awal), Aset dengan record Long missing dan satu notifikasi missing_long terkirim: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Record `Missing` (7 kar), Dilaporkan `T0 − 34 hari` (12 kar), Penanda `Long missing` (12 kar), Notifikasi `missing_long terkirim satu` (26 kar) · sumber turunan penulis
- **DU-041-11** Asset (awal), Aset dengan record Missing dan node Reported found by yang notifikasinya sudah terkirim: Name `Handheld Honeywell CT60 {runId}` (31 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar), Node `Reported found by` (17 kar), Notifikasi `missing_found_reported terkirim` (31 kar) · sumber turunan penulis
- **DU-041-12** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset tanpa pemegang yang dilaporkan bersamaan oleh dua pelapor: Name `Server Dell PowerEdge {runId}` (29 kar), Group `Head Office` (11 kar) · sumber turunan penulis
- **DU-041-13** Asset (awal), Aset dengan laporan pemegang Waiting for Confirmation yang menunggu lama: Name `Meja Rapat Kayu {runId}` (23 kar), Group `Head Office` (11 kar), Record `Waiting for Confirmation` (24 kar), Dilaporkan `T0 − 40 hari` (12 kar), Notifikasi `missing_holder_reported satu` (28 kar) · sumber turunan penulis
- **DU-041-14** User (awal), Pengguna Total Control: Name `Dewi Anggraini {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-041-15** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-041-16** User (awal), Pengguna Manage asset & TAG (Update): Name `Andi Pratama {runId}` (20 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group aset yang dipegangnya` (27 kar) · sumber matriks role PRD
- **DU-041-17** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Sari Dewanti {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-041-18** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-041-19** Missing (dibuat), Isian What happened laporan Pelapor admin atas aset dipegang: What happened `Monitor tidak ada di meja kerja setelah pindah lantai` (53 kar) · sumber turunan penulis
- **DU-041-20** Missing (dibuat), Isian What happened laporan Pelapor admin atas aset tanpa pemegang: What happened `Printer tidak ada di ruang cetak saat pengecekan` (48 kar) · sumber turunan penulis
- **DU-041-21** Missing (dibuat), Isian What happened laporan pemegang tanpa hak: What happened `Scanner tidak ada di loker setelah shift malam` (46 kar) · sumber turunan penulis
- **DU-041-22** Missing (dibuat), Isian What happened laporan pemegang dengan hak: What happened `Laptop tidak ada di meja setelah perjalanan dinas` (49 kar) · sumber turunan penulis
- **DU-041-23** Missing (dibuat), Reason Reject laporan pemegang: Reason `Kamera masih dipakai di lapangan` (32 kar) · sumber turunan penulis
- **DU-041-24** Missing (dibuat), Note Mark as Found: Note `Ditemukan di mobil operasional` (30 kar) · sumber turunan penulis
- **DU-041-25** Disposal (dibuat), Reason Report Disposal: Reason `Aset tidak ditemukan setelah penelusuran` (40 kar) · sumber turunan penulis
- **DU-041-26** Missing (dibuat), Isian What happened laporan pertama pada race: What happened `Server tidak ditemukan di rak setelah pemindahan ruang server` (61 kar) · sumber turunan penulis
- **DU-041-27** Missing (dicoba), Isian What happened laporan kedua yang kalah pada race: What happened `Server tidak ada di ruang server saat inventarisasi` (51 kar) · sumber turunan penulis
- **DU-041-28** Audit (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Task Audit dengan item Not found yang dilaporkan pelapor Audit: Name `Audit Gudang Utama {runId}` (26 kar), Item `Rak Server APC {runId}` (22 kar) · sumber turunan penulis
- **DU-041-29** Asset (awal; dimutasi TC-FA-MISS-E2E-041-notifikasi-dep-notification), Aset Not found yang dilaporkan pelapor Audit tanpa hak Aktor Missing: Name `Rak Server APC {runId}` (22 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-041-30** User (awal), Pengguna Asset Admin sub-tab Audit tanpa hak Aktor Missing: Name `Lia Kartika {runId}` (19 kar), Role `Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group Warehouse` (70 kar), Cakupan `aset dalam cakupan Task Audit` (29 kar) · sumber matriks role PRD
- **DU-041-31** Missing (dibuat), Isian What happened laporan pelapor Audit: What happened `Rak server tidak ada di ruang server saat penghitungan fisik` (60 kar) · sumber turunan penulis
- **DU-042-1** Audit (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Task Audit dengan tiga item Not found untuk Report Missing: Name `Audit Gudang Utama {runId}` (26 kar), Item `Laptop Dell Latitude 5420 {runId}; Printer HP LaserJet M404 {runId}; Projector Epson EB-X06 {runId}` (99 kar) · sumber turunan penulis
- **DU-042-2** Asset (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Aset Not found yang dilaporkan satu per satu: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber PRD §4.1a Example Data
- **DU-042-3** Asset (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Aset Not found yang ikut Bulk Report Missing: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber PRD §4.1a Example Data
- **DU-042-4** Asset (awal), Aset Not found yang sudah punya record berjalan sehingga dilewati: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Warehouse` (9 kar), Record `Missing berjalan` (16 kar) · sumber PRD §4.1a Example Data
- **DU-042-5** Audit (awal), Sesi Audit dengan item Audited berbadge Reported Missing: Name `Audit Gudang Cabang {runId}` (27 kar), Item `Toyota Innova {runId}` (21 kar), Badge `Reported Missing` (16 kar) · sumber turunan penulis
- **DU-042-6** Asset (awal), Aset dengan record Missing yang terbaca di sesi Audit: Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya` (15 kar), Record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-042-7** User (awal), Pengguna Group Manager pemegang hak Aktor Missing: Name `Dewi Lestari {runId}` (20 kar), Role `Group Manager` (13 kar), Cakupan `Group Warehouse` (15 kar) · sumber matriks role PRD
- **DU-042-8** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-042-9** Missing (dibuat), Isian What happened laporan satu item: What happened `Laptop tidak ada di rak saat penghitungan fisik` (47 kar) · sumber turunan penulis
- **DU-042-10** Missing (dibuat), Isian What happened Bulk Report Missing: What happened `Printer dan proyektor tidak ada di rak saat penghitungan fisik` (62 kar) · sumber turunan penulis
- **DU-042-11** Audit (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Sesi Audit dengan satu item dalam cakupan dan satu item di luar cakupan pelapor: Name `Audit Gudang Pusat {runId}` (26 kar), Item `Kursi Rapat Lipat {runId}; Lemari Arsip Besi {runId}` (52 kar) · sumber turunan penulis
- **DU-042-12** Asset (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Aset Not found dalam cakupan Group pelapor: Name `Kursi Rapat Lipat {runId}` (25 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-042-13** Asset (awal; dimutasi TC-FA-MISS-E2E-042-stock-opname-dep-audit), Aset Not found di luar cakupan Group pelapor: Name `Lemari Arsip Besi {runId}` (25 kar), Group `Branch Medan` (12 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-042-14** Missing (dibuat), Isian What happened Bulk Report Missing dengan aset di luar cakupan: What happened `Kursi dan lemari tidak ada di ruang penyimpanan saat penghitungan fisik` (71 kar) · sumber turunan penulis
- **DU-043-1** Rekonsiliasi (awal; dimutasi TC-FA-MISS-E2E-043-reconciliation-dep-wizard-reconciliation), Rekonsiliasi dengan aset tidak ditemukan: Name `Rekonsiliasi Gudang {runId}` (27 kar), Pemilik `Maya Putri {runId}` (18 kar), Aset tidak ditemukan `Hand Pallet Truck {runId}; Forklift Mini {runId}` (48 kar) · sumber turunan penulis
- **DU-043-2** Asset (awal; dimutasi TC-FA-MISS-E2E-043-reconciliation-dep-wizard-reconciliation), Aset tidak ditemukan saat rekonsiliasi yang dilaporkan hilang: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber PRD §4.1a Example Data
- **DU-043-3** User (awal), Pengguna pemilik Wizard Reconciliation: Name `Maya Putri {runId}` (18 kar), Role `pemilik Wizard Reconciliation` (29 kar), Cakupan `aset dalam cakupan rekonsiliasinya` (34 kar) · sumber matriks role PRD
- **DU-043-4** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-043-5** Missing (dibuat), Isian What happened laporan dari rekonsiliasi: What happened `Hand pallet truck tidak ditemukan saat rekonsiliasi gudang` (58 kar) · sumber turunan penulis
- **DU-043-6** Asset (awal; dimutasi TC-FA-MISS-E2E-043-reconciliation-dep-wizard-reconciliation), Aset tidak ditemukan kedua yang belum punya record Missing: Name `Forklift Mini {runId}` (21 kar), Group `Warehouse` (9 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-043-7** Missing (dibuat), Isian What happened laporan kedua dari rekonsiliasi: What happened `Forklift mini tidak ditemukan saat rekonsiliasi gudang` (54 kar) · sumber turunan penulis
- **DU-044-1** User (awal), Pengguna Total Control: Name `Dewi Anggraini {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-044-2** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-044-3** Asset (awal), Aset dengan entri Report Missing di Transaction admin log: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Log `Report Missing` (14 kar), Name di log `Laptop Dell Latitude 5420 {runId} - 1` (37 kar) · sumber PRD §4.1a Example Data
- **DU-044-4** Asset (awal), Aset dengan entri Confirm di Transaction admin log: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Log `Confirm` (7 kar), Name di log `Scanner Zebra DS2208 {runId} - 1` (32 kar) · sumber PRD §4.1b Example Data
- **DU-044-5** Asset (awal), Aset dengan entri Reject di Transaction admin log: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Log `Reject` (6 kar), Name di log `Camera Canon EOS {runId} - 1` (28 kar) · sumber PRD §4.1b Example Data
- **DU-044-6** Asset (awal), Aset dengan entri Mark as Found di Transaction admin log: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Log `Mark as Found` (13 kar), Name di log `Projector Epson EB-X06 {runId} - 1` (34 kar) · sumber PRD §4.1a Example Data
- **DU-044-7** Asset (awal), Aset yang diproses laporan banyak aset dengan satu entri log: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Log `Report Missing satu entri` (25 kar), Name di log `Printer HP LaserJet M404 {runId} - 1` (36 kar) · sumber PRD §4.1a Example Data
- **DU-044-8** Asset (awal), Aset yang diproses laporan banyak aset dengan satu entri log: Name `Monitor LG 27UL500 {runId}` (26 kar), Group `Head Office` (11 kar), Log `Report Missing satu entri` (25 kar), Name di log `Monitor LG 27UL500 {runId} - 1` (30 kar) · sumber PRD §4.1a Example Data
- **DU-044-9** Asset (awal), Aset yang dilewati laporan banyak aset tanpa entri log: Name `Server Dell PowerEdge {runId}` (29 kar), Group `Head Office` (11 kar), Record `Missing berjalan` (16 kar), Log `tanpa entri` (11 kar) · sumber turunan penulis
- **DU-044-10** Asset (awal), Aset dengan laporan pemegang yang dibatalkan lewat Cancel Report: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office` (11 kar), Record `Canceled` (8 kar) · sumber PRD §4.1a Example Data
- **DU-044-11** Asset (awal; dimutasi TC-FA-MISS-E2E-044-log-admin-dep-settings-user), Aset dengan record Missing yang diberi Add Update: Name `Hand Pallet Truck {runId}` (25 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar), Log `Add Update satu entri` (21 kar), Name di log `Hand Pallet Truck {runId} - 1` (29 kar) · sumber PRD §4.1a Example Data
- **DU-044-12** Asset (awal), Aset dengan record Reported Disposal yang dicatat di sub-tab Disposal: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Record `Reported Disposal` (17 kar) · sumber PRD §4.1b Example Data
- **DU-044-13** Asset (awal), Aset dengan node Reported found by dari jalur I found it: Name `Handheld Honeywell CT60 {runId}` (31 kar), Group `Warehouse` (9 kar), Record `Missing` (7 kar), Node `Reported found by` (17 kar) · sumber turunan penulis
- **DU-044-14** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-044-15** Missing (dibuat), Isian Update untuk Add Update: Update `Catatan penelusuran hari ini` (28 kar) · sumber turunan penulis
- **DU-044-16** User (awal), Pengguna Aktor Borrow tanpa Manage asset & TAG (Update) sebagai Pelapor admin: Name `Budi Hartono {runId}` (20 kar), Role `Aktor Borrow tanpa Manage asset & TAG (Update)` (46 kar), Cakupan `aset dalam cakupan transaksi Borrow` (35 kar) · sumber §8.2#b2
- **DU-044-17** Asset (awal), Aset dengan entri Report Missing dari halaman transaksi Borrow di Transaction admin log: Name `Proyektor BenQ MW535 {runId}` (28 kar), Group `Head Office` (11 kar), Log `Report Missing` (14 kar), Titik masuk `halaman transaksi Borrow` (24 kar), Name di log `Proyektor BenQ MW535 {runId} - 1` (32 kar) · sumber §8.2#b2
- **DU-044-18** User (awal), Pengguna Group Manager pemegang hak Aktor Missing yang melapor dari Task Detail Audit: Name `Sari Wulandari {runId}` (22 kar), Role `Group Manager atas Group Warehouse, pemegang hak Aktor Missing` (62 kar), Cakupan `aset Group Warehouse` (20 kar) · sumber §8.2#b2
- **DU-044-19** Asset (awal), Aset dengan entri Report Missing dari Task Detail Audit di Transaction admin log: Name `Barcode Scanner Honeywell 1900 {runId}` (38 kar), Group `Warehouse` (9 kar), Log `Report Missing` (14 kar), Titik masuk `Task Detail Audit` (17 kar), Name di log `Barcode Scanner Honeywell 1900 {runId} - 1` (42 kar) · sumber §8.2#b2
- **DU-044-20** User (awal), Pengguna Asset Admin sub-tab Audit tanpa hak Aktor Missing sebagai pelapor umum dari Task Detail Audit: Name `Lia Kartika {runId}` (19 kar), Role `Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group Warehouse` (70 kar), Cakupan `aset dalam cakupan Task Audit` (29 kar) · sumber §8.2#b2
- **DU-044-21** Asset (awal), Aset dengan record Missing Source Audit yang dibatalkan pelapor dari Task Detail Audit: Name `Rak Server APC {runId}` (22 kar), Group `Warehouse` (9 kar), Record `Canceled` (8 kar), Source `Audit` (5 kar), Name di log `Rak Server APC {runId} - 1` (26 kar) · sumber §8.2#b2
- **DU-044-22** User (awal), Pengguna pemegang aset dengan hak Aktor Missing yang melapor dari My Asset: Name `Hadi Pratama {runId}` (20 kar), Role `pemegang aset dengan hak Aktor Missing (Pelapor admin)` (54 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber §8.2#b2
- **DU-044-23** Asset (awal), Aset yang dipegang dengan record Missing dari laporan lewat My Asset: Name `Kamera Nikon D850 {runId}` (25 kar), Group `Head Office` (11 kar), Record `Missing dari laporan pemegang` (29 kar) · sumber §8.2#b2
- **DU-045-1** Asset (awal), Aset dengan record Missing melewati nilai bawaan Long missing after: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Group `Head Office` (11 kar), Record `Missing` (7 kar), Dilaporkan `T0 − 34 hari` (12 kar) · sumber PRD §4.1a Example Data
- **DU-045-2** Asset (awal), Aset dengan record Missing di bawah nilai bawaan Long missing after: Name `Toyota Innova {runId}` (21 kar), Group `Branch Surabaya` (15 kar), Record `Missing` (7 kar), Dilaporkan `T0 − 10 hari` (12 kar) · sumber PRD §4.1a Example Data
- **DU-045-3** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-049-1** Audit (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Task Audit dengan dua item Not found yang dilaporkan pelapor Audit: Name `Audit Gudang Barat {runId}` (26 kar), Item `Rak Server APC {runId}; Meja Kerja Lipat {runId}` (48 kar) · sumber turunan penulis
- **DU-049-2** Asset (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Aset Not found yang dilaporkan Asset Admin lalu dibatalkan: Name `Rak Server APC {runId}` (22 kar), Group `Warehouse` (9 kar), Asset Status `Normal` (6 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-049-3** Asset (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Aset Not found yang dilaporkan Staff Auditor: Name `Meja Kerja Lipat {runId}` (24 kar), Group `Warehouse` (9 kar), Asset Status `Normal` (6 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-049-4** User (awal), Pengguna Asset Admin sub-tab Audit tanpa hak Aktor Missing: Name `Lia Kartika {runId}` (19 kar), Role `Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group Warehouse` (70 kar), Cakupan `aset dalam cakupan Task Audit` (29 kar) · sumber matriks role PRD
- **DU-049-5** User (awal), Pengguna Staff Auditor tanpa hak Aktor Missing: Name `Bayu Saputra {runId}` (20 kar), Role `Staff Auditor tanpa hak Aktor Missing pada Group Warehouse` (58 kar), Cakupan `aset dalam cakupan Task Audit` (29 kar) · sumber matriks role PRD
- **DU-049-6** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-049-7** Missing (dibuat), Isian What happened laporan Asset Admin: What happened `Rak server tidak ada di ruang server saat penghitungan fisik` (60 kar) · sumber turunan penulis
- **DU-049-8** Missing (dibuat), Isian What happened laporan Staff Auditor: What happened `Meja kerja lipat tidak ada di area gudang barat saat penghitungan fisik` (71 kar) · sumber turunan penulis
- **DU-049-9** Audit (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Task Audit dengan dua item Not found yang dilaporkan Staff Auditor lewat Bulk Report Missing: Name `Audit Gudang Timur {runId}` (26 kar), Item `Kabinet Arsip Besi {runId}; Lemari Display Kaca {runId}` (55 kar) · sumber turunan penulis
- **DU-049-10** Asset (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Aset Not found bertagging Tag Reported yang laporannya dibatalkan: Name `Kabinet Arsip Besi {runId}` (26 kar), Group `Warehouse` (9 kar), Asset Status `Normal` (6 kar), Tagging `Tag Reported` (12 kar), Pemegang `tidak dipegang siapa pun` (24 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-049-11** Asset (awal; dimutasi TC-FA-MISS-E2E-049-pelapor-task-detail-audit-dep-audit), Aset Not found yang dilaporkan Staff Auditor lewat Bulk Report Missing: Name `Lemari Display Kaca {runId}` (27 kar), Group `Warehouse` (9 kar), Asset Status `Normal` (6 kar), Pemegang `tidak dipegang siapa pun` (24 kar), Record `tanpa record Missing` (20 kar) · sumber turunan penulis
- **DU-049-12** Missing (dibuat), Isian What happened Bulk Report Missing Staff Auditor: What happened `Kabinet dan lemari display tidak ada di area gudang timur saat penghitungan fisik` (81 kar) · sumber turunan penulis
- **DU-060-1** Maintenance (awal), Task Maintenance atas aset yang belum dimulai: Name `Servis Printer {runId}` (22 kar), Asset `Printer HP LaserJet M404 {runId}` (32 kar) · sumber turunan penulis
- **DU-060-2** Asset (awal; dimutasi TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine), Aset dengan task Maintenance yang dilaporkan Missing lalu ditemukan: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Warehouse` (9 kar), Asset Status `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record `tanpa record Missing` (20 kar) · sumber PRD §4.1a Example Data
- **DU-060-3** User (awal), Pengguna Total Control: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-060-4** Missing (dibuat), Isian What happened laporan aset ber-task Maintenance: What happened `Printer tidak ada di ruang cetak saat pengecekan` (48 kar) · sumber turunan penulis
- **DU-060-5** Maintenance (awal; dimutasi TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine), Task Maintenance atas aset pemegang yang belum dimulai, laporan pemegang ditolak: Name `Servis Scanner {runId}` (22 kar), Asset `Scanner Zebra DS2208 {runId}` (28 kar) · sumber turunan penulis
- **DU-060-6** Asset (awal; dimutasi TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine), Aset ditugaskan ke pemegang dengan record Waiting for Confirmation dari laporan pemegang, laporannya ditolak: Name `Scanner Zebra DS2208 {runId}` (28 kar), Group `Warehouse` (9 kar), Pemegang `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation, dilaporkan Joko Santoso {runId}` (57 kar) · sumber turunan penulis
- **DU-060-7** User (awal), Pemegang tanpa hak Aktor Missing: Name `Joko Santoso {runId}` (20 kar), Role `pemegang tanpa hak Aktor Missing` (32 kar) · sumber turunan penulis
- **DU-060-8** Missing (dibuat), Reason Reject laporan pemegang: Reason `Aset terlihat kembali di gudang` (31 kar) · sumber turunan penulis
- **DU-060-9** Maintenance (awal; dimutasi TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine), Task Maintenance atas aset pemegang yang belum dimulai, laporan pemegang dibatalkan: Name `Servis Proyektor {runId}` (24 kar), Asset `Proyektor Epson EB-X06 {runId}` (30 kar) · sumber turunan penulis
- **DU-060-10** Asset (awal; dimutasi TC-FA-MISS-E2E-060-penanda-asset-missing-dep-maintenance-routine), Aset ditugaskan ke pemegang dengan record Waiting for Confirmation dari laporan pemegang, laporannya dibatalkan pemegang: Name `Proyektor Epson EB-X06 {runId}` (30 kar), Group `Warehouse` (9 kar), Pemegang `Joko Santoso {runId}` (20 kar), Record `Waiting for Confirmation, dilaporkan Joko Santoso {runId}` (57 kar) · sumber turunan penulis
- **DU-046-1** Missing record (awal), record Missing di Group Finance Room, dipegang Andi saat dilaporkan, ber-TAG QR: Name `Laptop Dell Latitude 5420 {runId} - 22` (38 kar), Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `LPT 0022 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Andi Pratama {runId}` (20 kar), TAG `TAG QR 0022 {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-046-2** Missing record (awal), record Reported Disposal di Group Finance Room, ber-TAG QR: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `PRJ 0007 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), TAG `TAG QR 0007 {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-046-3** User (awal), pengguna Total Control: Name `Rina Wulandari {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-046-4** User (awal), pengguna Group Manager: Name `Andi Pratama {runId}` (20 kar), Role `Group Manager` (13 kar), Cakupan `Finance Room {runId}` (20 kar) · sumber matriks role PRD
- **DU-046-5** User (awal), pengguna Manage asset & TAG (Update): Name `Dewi Anggraini {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Warehouse {runId}` (17 kar) · sumber matriks role PRD
- **DU-046-6** User (awal), pengguna Accounting: Name `Maya Rahmawati {runId}` (22 kar), Role `Accounting` (10 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-046-7** User (awal), pengguna Read Only: Name `Sari Dewanti {runId}` (20 kar), Role `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-046-8** User (awal), pengguna View asset value: Name `Bima Santoso {runId}` (20 kar), Role `View asset value` (16 kar), Cakupan `Finance Room {runId}` (20 kar) · sumber matriks role PRD
- **DU-046-9** User (awal), pengguna tanpa Group Role (pemegang): Name `Joko Susilo {runId}` (19 kar), Role `tanpa Group Role (pemegang)` (27 kar), Aset dipegang `Hand Pallet Truck {runId} - 3` (29 kar) · sumber matriks role PRD
- **DU-046-10** Photo (dibuat), foto penemuan lebih dari 1 MB untuk I found it: File `foto-laptop-ditemukan {runId}.jpg` (33 kar), Format `JPG` (3 kar), Ukuran `2 MB` (4 kar) · sumber §4.6#b2
- **DU-046-11** Missing record (awal), record In Disposal Process di Group Finance Room, ber-TAG QR: Name `Printer HP LaserJet Pro {runId} - 12` (36 kar), Asset Name `Printer HP LaserJet Pro {runId}` (31 kar), Asset ID `PRN 0012 {runId}` (16 kar), Group `Finance Room {runId}` (20 kar), Status `In Disposal Process` (19 kar), Source `Audit` (5 kar), Last Holder `—` (1 kar), TAG `TAG QR 0012 {runId}` (19 kar) · sumber §4.6#b4
- **DU-046-12** Client (awal), entitas khusus dengan Storage yang menjadi penuh (usage ledger melebihi kuota) pada langkah 123: Name `Klien I Found It {runId}` (24 kar), Kuota Storage `50.0 GB` (7 kar), Usage ledger Storage awal `10.0 GB` (7 kar), Usage ledger Storage sesudah langkah 123 `51.2 GB` (7 kar) · sumber §1.2#r126
- **DU-047-1** Client (awal), entitas khusus dengan Storage penuh (usage ledger melebihi kuota): Name `Klien Storage Penuh {runId}` (27 kar), Kuota Storage `50.0 GB` (7 kar), Usage ledger Storage `51.2 GB` (7 kar) · sumber §1.2#r126
- **DU-047-2** Missing record (awal; dimutasi TC-FA-MISS-E2E-047-mark-as-found-storage-penuh-dep-file-manager), record Missing aset tanpa TAG, Condition Normal, dipakai untuk Photo baru dan tanpa Photo: Name `Camera DSLR Canon R6 {runId}` (28 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Condition `Normal` (6 kar), Node `Reported missing by Rina Wulandari {runId}` (42 kar) · sumber §9.4.2#r34
- **DU-047-3** Missing record (awal), record Missing aset tanpa TAG untuk Mark as Found Damaged yang ditolak: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Dian Kusuma {runId}` (19 kar), Condition `Normal` (6 kar), Baris transaksi `satu baris transaksi Borrow, tertutup` (37 kar) · sumber §1.2#r127
- **DU-047-4** Missing record (awal), record Missing asal Damaged + Missing dengan Damage record yang ditahan: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Finance Room {runId}` (20 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `satu, ditahan` (13 kar) · sumber §1.2#r128
- **DU-047-5** Photo (dicoba), foto penemuan PNG di bawah 1 MB yang ditolak karena Storage penuh: File `foto-ditemukan {runId}.png` (26 kar), Format `PNG` (3 kar), Ukuran `di bawah 1 MB` (13 kar) · sumber §9.9#p4
- **DU-047-6** Damaged Photo (dicoba), Damaged Photo dan Note untuk laptop yang ditolak karena Storage penuh: File `foto-kerusakan-laptop {runId}.png` (33 kar), Note `Layar retak dan engsel patah saat ditemukan` (43 kar) · sumber §1.2#r127
- **DU-047-7** Damaged Photo (dicoba), Damaged Photo dan Note untuk printer asal Damaged + Missing yang ditolak karena Storage penuh: File `foto-kerusakan-printer {runId}.png` (34 kar), Note `Rumah printer retak sejak sebelum hilang` (40 kar) · sumber §1.2#r128
- **DU-047-8** User (awal), pengguna Total Control pada entitas khusus: Name `Rina Wulandari {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-047-9** User (awal), pemegang terakhir aset laptop, tanpa Group Role: Name `Dian Kusuma {runId}` (19 kar), Role `tanpa Group Role (pemegang)` (27 kar) · sumber matriks role PRD
- **DU-048-1** Missing record (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), record Found aset tanpa TAG dengan node Reported found by dan Marked as found by yang memuat Photo: Name `Camera DSLR Canon R6 {runId}` (28 kar), Group `Finance Room` (12 kar), Source `Manual` (6 kar), Status `Found` (5 kar), Node 1 `Reported found by Sari Dewanti {runId}` (38 kar), Node 1 Photo `foto-laporan-ditemukan {runId}.png` (34 kar), Node 2 `Marked as found by Rina W` (25 kar), Node 2 Found at `Finance Room` (12 kar), Node 2 Asset Status `Normal` (6 kar), Node 2 Note `Ditemukan di rak server lantai 2` (32 kar), Node 2 Photo `foto-ditemukan {runId}.png` (26 kar) · sumber §1.2#r129
- **DU-048-2** Missing record (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), record Found aset Damaged dengan Damaged Photo dan satu Damage Report Source Missing Asset: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Finance Room` (12 kar), Source `Manual` (6 kar), Status `Found` (5 kar), Node `Marked as found by Rina W` (25 kar), Node Asset Status `Damaged` (7 kar), Node Note `Layar retak dan engsel patah saat ditemukan` (43 kar), Node Damaged Photo `foto-kerusakan-laptop {runId}.png` (33 kar), Damage Report `satu, Source Missing Asset` (26 kar) · sumber §9.4.2#r36
- **DU-048-3** User (awal), pengguna Total Control pelaku Mark as Found dan Delete File Manager: Name `Rina W` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-048-4** User (awal), pengguna Read Only pengirim I found it: Name `Sari Dewanti {runId}` (20 kar), Role `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-048-5** Berkas File Manager (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), berkas Found Photo yang dihapus lewat Delete File Manager: File `foto-ditemukan {runId}.png` (26 kar), Source `Found Photo` (11 kar), Asset `Camera DSLR Canon R6 {runId}` (28 kar), Toast hapus `Success, foto-ditemukan {runId}.png has been deleted.` (53 kar) · sumber §1.2#r129
- **DU-048-6** Berkas File Manager (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), berkas Found Photo yang dihapus lewat Delete File Manager: File `foto-laporan-ditemukan {runId}.png` (34 kar), Source `Found Photo` (11 kar), Asset `Camera DSLR Canon R6 {runId}` (28 kar), Toast hapus `Success, foto-laporan-ditemukan {runId}.png has been deleted.` (61 kar) · sumber §1.2#r129
- **DU-048-7** Berkas File Manager (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), berkas Damaged Photo yang dihapus lewat Delete File Manager: File `foto-kerusakan-laptop {runId}.png` (33 kar), Source `Damaged Photo` (13 kar), Asset `Laptop Dell Latitude 5420 {runId}` (33 kar), Toast hapus `Success, foto-kerusakan-laptop {runId}.png has been deleted.` (60 kar) · sumber §1.2#r129
- **DU-048-8** Missing record (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), record Found aset asal Damaged + Missing dengan Damaged Photo pada node Marked as found by: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Finance Room` (12 kar), Source `Manual` (6 kar), Status `Found` (5 kar), Node `Marked as found by Rina W` (25 kar), Node Asset Status `Damaged` (7 kar), Node Note `Rumah printer retak sejak sebelum hilang` (40 kar), Node Damaged Photo `foto-kerusakan-printer {runId}.png` (34 kar), Asal `Damaged + Missing` (17 kar) · sumber §1.2#r124
- **DU-048-9** Berkas File Manager (awal; dimutasi TC-FA-MISS-E2E-048-hapus-foto-file-manager-dep-file-manager), berkas Damaged Photo asal Damaged + Missing yang dihapus lewat Delete File Manager: File `foto-kerusakan-printer {runId}.png` (34 kar), Source `Damaged Photo` (13 kar), Asset `Printer HP LaserJet M404 {runId}` (32 kar), Toast hapus `Success, foto-kerusakan-printer {runId}.png has been deleted.` (61 kar) · sumber §1.2#r124
- **DU-050-1** Missing Record (awal), Record Missing dari Borrow, dipegang Andi Pratama: Name `Laptop Dell Latitude 5420 - 22` (30 kar), Asset ID `LPT-2026-0022` (13 kar), Group `Finance Room` (12 kar), Hierarki Group `Head Office > Finance Room` (26 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Andi Pratama` (12 kar), Last Holder tampil `Andi P` (6 kar), Last Holder Division `Finance` (7 kar), Last Holder Employee ID `EMP-0142` (8 kar), Last Seen waktu `2026-11-02T10:12:00Z` (20 kar), Last Seen pemindai `Lobby reader (reader tetap)` (27 kar), Last Seen tampil `02/11/26, 10:12 · Lobby reader` (30 kar), Deteksi terakhir (5) `02/11/26, 10:12 · Lobby reader | 01/11/26, 17:45 · Lobby reader | 31/10/26, 08:20 · Agus P | 30/10/26, 16:05 · Gate A reader | 29/10/26, 09:10 · Dedi K` (151 kar), Deteksi lebih lama (2, tidak tampil) `28/10/26, 14:30 · Gate A reader | 27/10/26, 08:00 · Lobby reader` (64 kar), Reported By `Andi Pratama` (12 kar), Reported By tampil `Andi P` (6 kar), Reported Date `2026-11-03T09:30:00Z` (20 kar), Reported Date tampil `03/11/26, 09:30` (15 kar), Days Missing `8` (1 kar), Days Missing tampil `8 days` (6 kar), Last Updated `2026-11-03T09:30:00Z` (20 kar), Last Updated tampil `03/11/26, 09:30` (15 kar), Photo `laptop-dell-22.jpg` (18 kar), Penanda Long missing `tidak` (5 kar) · sumber PRD §4.1a Example Data
- **DU-050-2** Missing Record (awal), Record Waiting for Confirmation, dilaporkan PIC Rudi Hartono atas nama Joko Susanto: Name `Hand Pallet Truck - 3` (21 kar), Asset ID `HPT-2026-0003` (13 kar), Group `Warehouse` (9 kar), Hierarki Group `Warehouse` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susanto` (12 kar), Last Holder tampil `Joko S` (6 kar), Last Holder Division `Warehouse Operations` (20 kar), Last Holder Employee ID `EMP-0388` (8 kar), Last Holder hover PIC `PIC: Rudi Hartono` (17 kar), Last Seen waktu `2026-11-09T22:40:00Z` (20 kar), Last Seen pemindai `Dedi Kurniawan (pengguna)` (25 kar), Last Seen tampil `09/11/26, 22:40 · Dedi K` (24 kar), Reported By `Rudi Hartono (PIC) atas nama Joko Susanto` (41 kar), Reported By tampil `Rudi H (on behalf of Joko S)` (28 kar), Reported Date `2026-11-10T07:15:00Z` (20 kar), Reported Date tampil `10/11/26, 07:15` (15 kar), Days Missing `1` (1 kar), Days Missing tampil `1 day` (5 kar), Last Updated `2026-11-10T07:15:00Z` (20 kar), Last Updated tampil `10/11/26, 07:15` (15 kar), Photo `hand-pallet-truck-3.jpg` (23 kar), Penanda Long missing `tidak` (5 kar) · sumber PRD §4.1a Example Data
- **DU-050-3** Missing Record (awal), Record Reported Disposal tanpa Last Holder: Name `Projector Epson EB-X06 - 7` (26 kar), Asset ID `PRJ-2026-0007` (13 kar), Group `Branch Surabaya` (15 kar), Hierarki Group `Branch Surabaya` (15 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Last Seen waktu `2026-09-15T14:05:00Z` (20 kar), Last Seen pemindai `Agus Prasetyo (pengguna)` (24 kar), Last Seen tampil `15/09/26, 14:05 · Agus P` (24 kar), Reported By `Agus Prasetyo` (13 kar), Reported By tampil `Agus P` (6 kar), Reported Date `2026-10-01T08:00:00Z` (20 kar), Reported Date tampil `01/10/26, 08:00` (15 kar), Days Missing `41` (2 kar), Days Missing tampil `41 days` (7 kar), Last Updated `2026-11-05T15:30:00Z` (20 kar), Last Updated tampil `05/11/26, 15:30` (15 kar), Photo `projector-epson-7.jpg` (21 kar) · sumber PRD §4.1a Example Data
- **DU-050-4** Missing Record (awal), Record Missing dari Transfer, Reported Date dan Last Updated berbeda: Name `Toyota Innova - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Branch Surabaya` (15 kar), Hierarki Group `Branch Surabaya` (15 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Last Seen waktu `2026-10-31T16:20:00Z` (20 kar), Last Seen pemindai `Gate B reader (reader tetap)` (28 kar), Last Seen tampil `31/10/26, 16:20 · Gate B reader` (31 kar), Reported By `Agus Prasetyo` (13 kar), Reported By tampil `Agus P` (6 kar), Reported Date `2026-11-01T09:00:00Z` (20 kar), Reported Date tampil `01/11/26, 09:00` (15 kar), Days Missing `10` (2 kar), Days Missing tampil `10 days` (7 kar), Last Updated `2026-11-04T16:10:00Z` (20 kar), Last Updated tampil `04/11/26, 16:10` (15 kar), Photo `toyota-innova-2.jpg` (19 kar), Penanda Long missing `tidak` (5 kar) · sumber PRD §4.1a Example Data
- **DU-050-5** Missing Record (awal), Record In Disposal Process: Name `Printer HP LaserJet M404 - 5` (28 kar), Asset ID `PRN-2026-0005` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Last Seen waktu `2026-08-20T16:40:00Z` (20 kar), Last Seen pemindai `Lobby reader (reader tetap)` (27 kar), Last Seen tampil `20/08/26, 16:40 · Lobby reader` (30 kar), Reported By `Rina Wulandari` (14 kar), Reported By tampil `Rina W` (6 kar), Reported Date `2026-08-25T10:00:00Z` (20 kar), Reported Date tampil `25/08/26, 10:00` (15 kar), Days Missing `78` (2 kar), Days Missing tampil `78 days` (7 kar), Last Updated `2026-11-02T11:20:00Z` (20 kar), Last Updated tampil `02/11/26, 11:20` (15 kar), Photo `printer-hp-5.jpg` (16 kar) · sumber PRD §4.1a Example Data
- **DU-050-6** Missing Record (awal), Record Waiting for Confirmation, belum pernah terpindai, tanpa foto: Name `Monitor LG 27UL500 - 11` (23 kar), Asset ID `MON-2026-0011` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewanti` (12 kar), Last Holder tampil `Sari D` (6 kar), Last Seen waktu `null` (4 kar), Last Seen pemindai `null` (4 kar), Last Seen tampil `Unknown` (7 kar), Reported By `Sari Dewanti` (12 kar), Reported By tampil `Sari D` (6 kar), Reported Date `2026-11-08T11:00:00Z` (20 kar), Reported Date tampil `08/11/26, 11:00` (15 kar), Days Missing `3` (1 kar), Days Missing tampil `3 days` (6 kar), Last Updated `2026-11-08T11:00:00Z` (20 kar), Last Updated tampil `08/11/26, 11:00` (15 kar), Photo `tanpa foto (avatar inisial)` (27 kar) · sumber PRD §4.1a Example Data
- **DU-050-7** Missing Record (awal), Record Missing melewati Long missing after: Name `Laptop Lenovo ThinkPad T14 - 4` (30 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi Anggraini` (14 kar), Last Holder tampil `Dewi A` (6 kar), Last Seen waktu `2026-10-05T11:10:00Z` (20 kar), Last Seen pemindai `Gate A reader (reader tetap)` (28 kar), Last Seen tampil `05/10/26, 11:10 · Gate A reader` (31 kar), Reported By `Rina Wulandari` (14 kar), Reported By tampil `Rina W` (6 kar), Reported Date `2026-10-08T09:00:00Z` (20 kar), Reported Date tampil `08/10/26, 09:00` (15 kar), Days Missing `34` (2 kar), Days Missing tampil `34 days` (7 kar), Last Updated `2026-11-07T00:00:00Z` (20 kar), Last Updated tampil `07/11/26, 00:00` (15 kar), Photo `laptop-lenovo-4.jpg` (19 kar), Penanda Long missing `ya (34 hari, melewati Long missing after 30)` (44 kar) · sumber PRD §4.1a Example Data
- **DU-050-8** Missing Record (awal), Record Missing dengan seluruh kolom Curated terisi: Name `Handheld Reader Zebra TC21 - 3` (30 kar), Asset ID `HRD-2026-0003` (13 kar), Group `East Distribution Center` (24 kar), Hierarki Group `Region Java > East Distribution Center` (38 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Seen waktu `2026-11-08T10:00:00Z` (20 kar), Last Seen pemindai `Dedi Kurniawan (pengguna)` (25 kar), Last Seen tampil `08/11/26, 10:00 · Dedi K` (24 kar), Brand `Zebra Technologies` (18 kar), Model/Type `Handheld Reader Pro` (19 kar), TAG `RFID, NFC` (9 kar), Category `Handheld Reader` (15 kar), Hierarki Category `Hardware > Scanner > Handheld Reader` (36 kar), Alias Name `<b>Reader Gudang Timur</b>` (26 kar), Measurement `Unit` (4 kar), Division `Logistics` (9 kar), Labels `Fragile, Priority` (17 kar), Asset Class `Electronic Equipment` (20 kar), Register Date `2025-01-15` (10 kar), Register Date tampil `15/01/25` (8 kar), Purchase Date `2024-12-20` (10 kar), Purchase Date tampil `20/12/24` (8 kar), Daftar garansi `Garansi Pabrik — 2026-12-20 | Garansi Baterai — 2027-03-15 | Garansi Layar — 2027-06-30` (87 kar), Warranty Expiry (Warranty until terdekat) `2026-12-20` (10 kar), Warranty Expiry tampil `20/12/26` (8 kar), Hover daftar garansi `Garansi Pabrik — 20/12/26 | Garansi Baterai — 15/03/27 | Garansi Layar — 30/06/27` (81 kar), Purchase Cost `15000000` (8 kar), Asset Value (Commercial) `12500000` (8 kar), Asset Value (Fiscal) `9000000` (7 kar), Modified By `Siti Nurbaya` (12 kar), Modified By tampil `Siti N` (6 kar) · sumber turunan penulis
- **DU-050-9** Missing Record (awal), Record Missing tanpa TAG dengan kolom Curated kosong: Name `Kursi Lipat Aluminium - 8` (25 kar), Asset ID `FRN-2026-0008` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Seen waktu `null` (4 kar), Last Seen tampil `—` (1 kar), Brand `null` (4 kar), Model/Type `null` (4 kar), TAG `null` (4 kar), Category `Furniture` (9 kar), Hierarki Category `Furniture` (9 kar), Alias Name `null` (4 kar), Measurement `null` (4 kar), Division `null` (4 kar), Labels `null` (4 kar), Asset Class `null` (4 kar), Register Date `2025-03-10` (10 kar), Register Date tampil `10/03/25` (8 kar), Purchase Date `null` (4 kar), Warranty Expiry `null` (4 kar), Purchase Cost `null` (4 kar), Asset Value (Commercial) `null` (4 kar), Asset Value (Fiscal) `null` (4 kar), Modified By `System` (6 kar), Modified By tampil `System` (6 kar) · sumber turunan penulis
- **DU-050-10** Missing Record (awal), Record dengan pemegang satu kata dan Reported Date hari ke-25: Name `Router Cisco ISR 4331 - 2` (25 kar), Asset ID `NET-2026-0002` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Budi` (4 kar), Last Holder tampil `Budi` (4 kar), Last Seen waktu `2026-10-24T10:00:00Z` (20 kar), Last Seen pemindai `Siti Nurbaya (pengguna)` (23 kar), Last Seen tampil `24/10/26, 10:00 · Siti N` (24 kar), Reported By `Siti Nurbaya` (12 kar), Reported By tampil `Siti N` (6 kar), Reported Date `2026-10-25T14:05:00Z` (20 kar), Reported Date tampil `25/10/26, 14:05` (15 kar), Days Missing `17` (2 kar), Days Missing tampil `17 days` (7 kar), Last Updated `2026-10-25T14:05:00Z` (20 kar), Last Updated tampil `25/10/26, 14:05` (15 kar) · sumber turunan penulis
- **DU-050-11** Missing Record (awal), Record dengan nama tiga kata, nama panjang, dan Reported Date dekat tengah malam: Name `Switch Aruba 2930F - 6` (22 kar), Asset ID `NET-2026-0006` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `Alexander Graham Bell` (21 kar), Last Holder tampil `Alexander G` (11 kar), Last Seen waktu `2026-10-30T09:00:00Z` (20 kar), Last Seen pemindai `Gate B reader (reader tetap)` (28 kar), Last Seen tampil `30/10/26, 09:00 · Gate B reader` (31 kar), Reported By `Buzzlightyear Sumardi` (21 kar), Reported By tampil `Buzzlightyear S` (15 kar), Reported Date `2026-10-24T23:30:00Z` (20 kar), Reported Date tampil `24/10/26, 23:30` (15 kar), Days Missing `18` (2 kar), Days Missing tampil `18 days` (7 kar), Last Updated `2026-10-24T23:30:00Z` (20 kar), Last Updated tampil `24/10/26, 23:30` (15 kar) · sumber turunan penulis
- **DU-050-12** Missing Record (awal), Record dengan dua nama mirip: Name `Printer Epson L3250 - 9` (23 kar), Asset ID `PRN-2026-0009` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi Anggraini` (14 kar), Last Holder tampil `Dewi A` (6 kar), Last Seen waktu `null` (4 kar), Last Seen pemindai `null` (4 kar), Last Seen tampil `Unknown` (7 kar), Reported By `Dewi Anggreni` (13 kar), Reported By tampil `Dewi A` (6 kar), Reported Date `2026-11-06T10:30:00Z` (20 kar), Reported Date tampil `06/11/26, 10:30` (15 kar), Days Missing `5` (1 kar), Days Missing tampil `5 days` (6 kar), Last Updated `2026-11-06T10:30:00Z` (20 kar), Last Updated tampil `06/11/26, 10:30` (15 kar) · sumber turunan penulis
- **DU-050-13** Missing Record (awal), Record dengan nama aset dan nama Group panjang: Name `Regional Procurement and Vendor Management Office Jakarta - 1` (61 kar), Asset ID `OFC-2026-0001` (13 kar), Group `Jakarta Selatan Distribution Center` (35 kar), Hierarki Group `Region Jawa > Jakarta Selatan Distribution Center` (49 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `Siti Nurbaya` (12 kar), Last Holder tampil `Siti N` (6 kar), Last Seen waktu `2026-11-05T13:00:00Z` (20 kar), Last Seen pemindai `Gate A reader (reader tetap)` (28 kar), Last Seen tampil `05/11/26, 13:00 · Gate A reader` (31 kar), Reported By `Siti Nurbaya` (12 kar), Reported By tampil `Siti N` (6 kar), Reported Date `2026-11-06T08:00:00Z` (20 kar), Reported Date tampil `06/11/26, 08:00` (15 kar), Days Missing `5` (1 kar), Days Missing tampil `5 days` (6 kar), Last Updated `2026-11-06T08:00:00Z` (20 kar), Last Updated tampil `06/11/26, 08:00` (15 kar), Group tampil `Jakarta Sela..ution Center` (26 kar) · sumber turunan penulis
- **DU-050-14** Missing Record (awal), Record dengan nama dan kode mirip kata kamus: Name `Available Room - 1` (18 kar), Asset ID `SKU-DESK-01` (11 kar), Group `Meja Rapat` (10 kar), Hierarki Group `Head Office > Meja Rapat` (24 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Last Seen waktu `null` (4 kar), Last Seen pemindai `null` (4 kar), Last Seen tampil `Unknown` (7 kar), Reported By `Budi` (4 kar), Reported By tampil `Budi` (4 kar), Reported Date `2026-11-09T09:00:00Z` (20 kar), Reported Date tampil `09/11/26, 09:00` (15 kar), Days Missing `2` (1 kar), Days Missing tampil `2 days` (6 kar), Last Updated `2026-11-09T09:00:00Z` (20 kar), Last Updated tampil `09/11/26, 09:00` (15 kar) · sumber turunan penulis
- **DU-050-15** Missing History Record (awal), Record History Found: Name `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `Sari Dewanti` (12 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-10-12T09:00:00Z` (20 kar), Reported Date tampil `12/10/26, 09:00` (15 kar), Duration `6` (1 kar), Resolved By `Rina Wulandari` (14 kar), Resolved Date `2026-10-18T14:10:00Z` (20 kar), Resolved Date tampil `18/10/26, 14:10` (15 kar) · sumber PRD §4.1b Example Data
- **DU-050-16** Missing History Record (awal), Record History Disposed: Name `Drill Bosch GSB - 4` (19 kar), Asset ID `DRL-2026-0004` (13 kar), Group `Warehouse` (9 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-08-01T08:00:00Z` (20 kar), Reported Date tampil `01/08/26, 08:00` (15 kar), Duration `62` (2 kar), Resolved By `System` (6 kar), Resolved Date `2026-10-02T00:00:00Z` (20 kar), Resolved Date tampil `02/10/26, 00:00` (15 kar) · sumber PRD §4.1b Example Data
- **DU-050-17** Missing History Record (awal), Record History Rejected: Name `Camera Canon EOS - 1` (20 kar), Asset ID `CAM-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso` (12 kar), Reported By `Budi Santoso` (12 kar), Reported Date `2026-11-05T08:30:00Z` (20 kar), Reported Date tampil `05/11/26, 08:30` (15 kar), Duration `1` (1 kar), Resolved By `Rina Wulandari` (14 kar), Resolved Date `2026-11-06T09:15:00Z` (20 kar), Resolved Date tampil `06/11/26, 09:15` (15 kar) · sumber PRD §4.1b Example Data
- **DU-050-18** Missing History Record (awal), Record History Canceled: Name `Scanner Zebra DS2208 - 2` (24 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Warehouse` (9 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susanto` (12 kar), Reported By `Joko Susanto` (12 kar), Reported Date `2026-11-03T13:00:00Z` (20 kar), Reported Date tampil `03/11/26, 13:00` (15 kar), Duration `1` (1 kar), Resolved By `Joko Susanto` (12 kar), Resolved Date `2026-11-04T08:20:00Z` (20 kar), Resolved Date tampil `04/11/26, 08:20` (15 kar) · sumber PRD §4.1b Example Data
- **DU-050-19** Missing Record (awal), Daftar Active tanpa record: Respons daftar Active `0 record` (8 kar) · sumber turunan penulis
- **DU-050-20** Kata Kunci Search (dicoba), Kata kunci Search tanpa hasil: Kata kunci `ZZZ-TIDAK-ADA` (13 kar) · sumber turunan penulis
- **DU-050-21** Missing Record (awal), Record Missing untuk setting tanggal, jam 12 jam, dan zona waktu lain: Name `Tablet Lenovo Tab M10 - 12` (26 kar), Asset ID `TAB-2026-0012` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Last Seen waktu `2026-11-09T16:05:00Z` (20 kar), Last Seen pemindai `Gate A reader (reader tetap)` (28 kar), Last Seen tampil tanggal `11/9/26` (7 kar), Last Seen tampil jam `11:05` (5 kar), Last Seen tampil pemindai `Gate A reader` (13 kar), Reported By `Siti Nurbaya` (12 kar), Reported By tampil `Siti N` (6 kar), Reported Date `2026-11-09T16:40:00Z` (20 kar), Reported Date tampil tanggal `11/9/26` (7 kar), Reported Date tampil jam `11:40` (5 kar), Days Missing `2` (1 kar), Days Missing tampil `2 days` (6 kar), Last Updated `2026-11-09T16:40:00Z` (20 kar), Last Updated tampil tanggal `11/9/26` (7 kar), Last Updated tampil jam `11:40` (5 kar), Photo `tablet-lenovo-12.jpg` (20 kar) · sumber turunan penulis
- **DU-050-22** Setting Tampilan (awal), Setting tampilan tanggal dan waktu selain bawaan: Date Format `M/d/yy` (6 kar), Time Format `12 jam` (6 kar), Time Zone `UTC+7` (5 kar) · sumber turunan penulis
- **DU-050-23** Missing Log Node (awal; 19 record), Sembilan belas node riwayat Update added by untuk DU-050-1: Node `Update added by Rina W` (22 kar), Detail `Pencarian lantai {n}` (20 kar) · sumber turunan penulis
- **DU-050-24** Missing Log Node (awal), Node laporan awal untuk DU-050-1: Node `Reported missing by Andi P` (26 kar), Detail `Laptop hilang saat dipinjam` (27 kar) · sumber turunan penulis
- **DU-050-25** Missing Record (awal), Record Missing dengan tiga garansi yang urutan daftarnya tidak dimulai dari garansi terdekat: Name `Server Dell PowerEdge R440 - 6` (30 kar), Asset ID `SRV-2026-0006` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Register Date `2025-02-03` (10 kar), Register Date tampil `03/02/25` (8 kar), Purchase Date `2025-01-20` (10 kar), Purchase Date tampil `20/01/25` (8 kar), Daftar garansi `Garansi Server — 2028-01-20 | Garansi Penyimpanan — 2027-08-05 | Garansi Catu Daya — 2026-11-30` (95 kar), Warranty Expiry (Warranty until terdekat) `2026-11-30` (10 kar), Warranty Expiry tampil `30/11/26` (8 kar), Hover daftar garansi `Garansi Server — 20/01/28 | Garansi Penyimpanan — 05/08/27 | Garansi Catu Daya — 30/11/26` (89 kar), Purchase Cost `28000000` (8 kar), Asset Value (Commercial) `24500000` (8 kar), Asset Value (Fiscal) `21000000` (8 kar), Modified By `Rina Wulandari` (14 kar), Modified By tampil `Rina W` (6 kar) · sumber turunan penulis
- **DU-051-1** Missing Record (awal; 11 record), Sebelas record Missing untuk dua halaman: Name `Aset Paginasi {n}` (17 kar), Asset ID `PGN-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-051-2** Missing Record (awal; 10 record), Sepuluh record Missing tepat satu halaman: Name `Aset Tepat Sepuluh {n}` (22 kar), Asset ID `TPT-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-051-3** Missing Record (awal; 26 record), Dua puluh enam record Missing untuk ukuran halaman 25: Name `Aset Dua Puluh Enam {n}` (23 kar), Asset ID `DPE-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-051-4** Missing Record (awal; 12 record), Dua belas record Missing hasil pencarian tersaring: Name `Aset Tersaring {n}` (18 kar), Asset ID `TSR-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-051-5** Input Halaman (dicoba), Input nomor halaman tidak valid: Input nomor halaman `0 | -1 | 2 | abc` (16 kar) · sumber turunan penulis
- **DU-051-6** Missing Record (awal), Record Waiting for Confirmation dengan TAG RFID: Name `Laptop Asus Vivobook - 1` (24 kar), Asset ID `LPT-2026-0101` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Sari Dewanti` (12 kar), Last Seen `Unknown` (7 kar), Reported By `Sari Dewanti` (12 kar), Reported Date `2026-11-08T11:00:00Z` (20 kar), Days Missing `3` (1 kar), Last Updated `2026-11-08T11:00:00Z` (20 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a Example Data
- **DU-051-7** Missing Record (awal), Record Missing dengan TAG NFC dan QR: Name `Printer Canon Pixma - 2` (23 kar), Asset ID `PRN-2026-0102` (13 kar), Group `Branch Surabaya` (15 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `2026-11-05T10:00:00Z · Lobby reader` (35 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-11-06T09:00:00Z` (20 kar), Days Missing `5` (1 kar), Last Updated `2026-11-06T09:00:00Z` (20 kar), TAG `NFC, QR` (7 kar) · sumber turunan penulis
- **DU-051-8** Missing Record (awal), Record Missing dengan TAG QR: Name `Scanner Honeywell - 3` (21 kar), Asset ID `SCN-2026-0103` (13 kar), Group `Warehouse` (9 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), Last Holder `Andi Pratama` (12 kar), Last Seen `2026-10-05T09:00:00Z · Gate A reader` (36 kar), Reported By `Andi Pratama` (12 kar), Reported Date `2026-10-05T09:00:00Z` (20 kar), Days Missing `37` (2 kar), Last Updated `2026-11-07T00:00:00Z` (20 kar), TAG `QR` (2 kar) · sumber turunan penulis
- **DU-051-9** Missing History Record (awal), Record History Rejected: Name `Camera Canon EOS - 1` (20 kar), Asset ID `CAM-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso` (12 kar), Reported By `Budi Santoso` (12 kar), Reported Date `2026-11-05T08:30:00Z` (20 kar), Duration `1` (1 kar), Resolved By `Rina Wulandari` (14 kar), Resolved Date `2026-11-06T09:15:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-051-10** Opsi Filter (awal), Opsi filter Source: nilai DISTINCT dari baris DU-051-6 sampai DU-051-8 dan DU-051-12 sampai DU-051-15: Source `Borrow, Reported by holder, Audit, Transfer, Manual, Work order, Reconciliation` (79 kar) · sumber turunan penulis
- **DU-051-11** Kata Kunci (dicoba), Kata kunci Search dan kata kunci opsi filter: Kata kunci Search `Canon` (5 kar), Kata kunci Search tersaring `Aset Tersaring` (14 kar), Kata kunci opsi filter tanpa hasil `ZZZ-TIDAK-ADA` (13 kar) · sumber turunan penulis
- **DU-051-12** Missing Record (awal), Record Reported Disposal dengan Source Audit: Name `Projector Epson EB-X06 - 7` (26 kar), Asset ID `PRJ-2026-0007` (13 kar), Group `Branch Surabaya` (15 kar), Status `Reported Disposal` (17 kar), Source `Audit` (5 kar), Last Holder `null` (4 kar), Last Seen `2026-09-15T14:05:00Z · Agus P` (29 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-10-01T08:00:00Z` (20 kar), Days Missing `41` (2 kar), Last Updated `2026-11-05T15:30:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-051-13** Missing Record (awal), Record In Disposal Process dengan Source Work order: Name `Printer HP LaserJet M404 - 5` (28 kar), Asset ID `PRN-2026-0005` (13 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Work order` (10 kar), Last Holder `null` (4 kar), Last Seen `2026-08-20T16:40:00Z · Lobby reader` (35 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-08-25T10:00:00Z` (20 kar), Days Missing `78` (2 kar), Last Updated `2026-11-02T11:20:00Z` (20 kar) · sumber turunan penulis
- **DU-051-14** Missing Record (awal), Record Missing dengan Source Transfer: Name `Toyota Innova - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Branch Surabaya` (15 kar), Status `Missing` (7 kar), Source `Transfer` (8 kar), Last Holder `null` (4 kar), Last Seen `2026-10-31T16:20:00Z · Gate B reader` (36 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-11-01T09:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-04T16:10:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-051-15** Missing Record (awal), Record Missing dengan Source Reconciliation: Name `Tablet Samsung Galaxy Tab - 6` (29 kar), Asset ID `TAB-2026-0106` (13 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Reconciliation` (14 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-1** Missing Record (awal; 12 record), Dua belas record Missing satu Group: Name `Aset Bulk {n}` (13 kar), Asset ID `BLK-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-2** Missing Record (awal), Record Missing di Group Warehouse hasil filter: Name `Aset Gudang Hilang - 1` (22 kar), Asset ID `WHS-2026-0001` (13 kar), Group `Warehouse` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-3** Missing Record (awal), Record Missing di Group Head Office: Name `Aset Head Office - 1` (20 kar), Asset ID `HOF-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-4** Missing Record (awal; 2 record), Dua record Missing yang seluruhnya dilewati: Name `Aset Semua Dilewati {n}` (23 kar), Asset ID `SDL-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-5** Missing Record (awal; 3 record), Tiga record Missing yang sebagian dilewati: Name `Aset Sebagian Dilewati {n}` (26 kar), Asset ID `SBD-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-6** Missing Record (awal; 2 record), Dua record Missing untuk kegagalan server: Name `Aset Gagal Bulk {n}` (19 kar), Asset ID `GGL-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-7** Missing Record (awal), Record Waiting for Confirmation: Name `Aset Menunggu Konfirmasi - 1` (28 kar), Asset ID `WFC-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-052-8** Disposal Reason (dibuat), Reason yang diisi pada dialog Report Disposal: Reason `Aset tidak ditemukan setelah inventarisasi gudang` (49 kar) · sumber turunan penulis
- **DU-052-9** Missing Record (awal), Record Missing yang muncul pada pembacaan ulang daftar sesudah kegagalan: Name `Aset Muncul Sesudah Gagal - 1` (29 kar), Asset ID `MSG-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Seen `Unknown` (7 kar), Reported By `Rina Wulandari` (14 kar), Reported Date `2026-11-01T08:00:00Z` (20 kar), Days Missing `10` (2 kar), Last Updated `2026-11-01T08:00:00Z` (20 kar) · sumber turunan penulis
- **DU-053-1** Missing History Record (awal), Record History Found, diselesaikan Rina Wulandari: Name `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), Last Holder `Sari Dewanti` (12 kar), Last Holder tampil `Sari D` (6 kar), Last Holder Division `Finance` (7 kar), Last Holder Employee ID `EMP-0207` (8 kar), Reported By `Rina Wulandari` (14 kar), Reported By tampil `Rina W` (6 kar), Reported Date `2026-10-12T09:00:00Z` (20 kar), Reported Date tampil `12/10/26, 09:00` (15 kar), Duration `6` (1 kar), Duration tampil `6 days` (6 kar), Resolved By `Rina Wulandari` (14 kar), Resolved By tampil `Rina W` (6 kar), Resolved Date `2026-10-18T14:10:00Z` (20 kar), Resolved Date tampil `18/10/26, 14:10` (15 kar), Photo `laptop-dell-9.jpg` (17 kar) · sumber PRD §4.1b Example Data
- **DU-053-2** Missing History Record (awal), Record History Disposed, diselesaikan System, tanpa Last Holder: Name `Drill Bosch GSB - 4` (19 kar), Asset ID `DRL-2026-0004` (13 kar), Group `Warehouse` (9 kar), Hierarki Group `Warehouse` (9 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), Last Holder `null` (4 kar), Last Holder tampil `—` (1 kar), Reported By `Agus Prasetyo` (13 kar), Reported By tampil `Agus P` (6 kar), Reported Date `2026-08-01T08:00:00Z` (20 kar), Reported Date tampil `01/08/26, 08:00` (15 kar), Duration `62` (2 kar), Duration tampil `62 days` (7 kar), Resolved By `System` (6 kar), Resolved By tampil `System` (6 kar), Resolved Date `2026-10-02T00:00:00Z` (20 kar), Resolved Date tampil `02/10/26, 00:00` (15 kar), Photo `drill-bosch-4.jpg` (17 kar) · sumber PRD §4.1b Example Data
- **DU-053-3** Missing History Record (awal), Record History Rejected dengan Duration satu hari: Name `Camera Canon EOS - 1` (20 kar), Asset ID `CAM-2026-0001` (13 kar), Group `Head Office` (11 kar), Hierarki Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi Santoso` (12 kar), Last Holder tampil `Budi S` (6 kar), Reported By `Budi Santoso` (12 kar), Reported By tampil `Budi S` (6 kar), Reported Date `2026-11-05T08:30:00Z` (20 kar), Reported Date tampil `05/11/26, 08:30` (15 kar), Duration `1` (1 kar), Duration tampil `1 day` (5 kar), Resolved By `Rina Wulandari` (14 kar), Resolved By tampil `Rina W` (6 kar), Resolved Date `2026-11-06T09:15:00Z` (20 kar), Resolved Date tampil `06/11/26, 09:15` (15 kar), Photo `camera-canon-1.jpg` (18 kar) · sumber PRD §4.1b Example Data
- **DU-053-4** Missing History Record (awal), Record History Canceled oleh pelapor: Name `Scanner Zebra DS2208 - 2` (24 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Warehouse` (9 kar), Hierarki Group `Warehouse` (9 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susanto` (12 kar), Last Holder tampil `Joko S` (6 kar), Reported By `Joko Susanto` (12 kar), Reported By tampil `Joko S` (6 kar), Reported Date `2026-11-03T13:00:00Z` (20 kar), Reported Date tampil `03/11/26, 13:00` (15 kar), Duration `1` (1 kar), Duration tampil `1 day` (5 kar), Resolved By `Joko Susanto` (12 kar), Resolved By tampil `Joko S` (6 kar), Resolved Date `2026-11-04T08:20:00Z` (20 kar), Resolved Date tampil `04/11/26, 08:20` (15 kar), Photo `scanner-zebra-2.jpg` (19 kar) · sumber PRD §4.1b Example Data
- **DU-053-5** Missing History Record (awal), Record History Found dengan pengguna yang kemudian dihapus: Name `Tablet Samsung Galaxy Tab A8 - 3` (32 kar), Asset ID `TAB-2026-0003` (13 kar), Group `Finance Room` (12 kar), Hierarki Group `Head Office > Finance Room` (26 kar), Status `Found` (5 kar), Source `Transfer` (8 kar), Last Holder `Maya Kusuma` (11 kar), Last Holder tampil `Maya K` (6 kar), Status akun Maya Kusuma `dihapus sesudah record selesai` (30 kar), Reported By `Maya Kusuma` (11 kar), Reported By tampil `Maya K` (6 kar), Reported Date `2026-10-20T10:00:00Z` (20 kar), Reported Date tampil `20/10/26, 10:00` (15 kar), Duration `3` (1 kar), Duration tampil `3 days` (6 kar), Resolved By `Rina Wulandari` (14 kar), Resolved By tampil `Rina W` (6 kar), Resolved Date `2026-10-23T15:45:00Z` (20 kar), Resolved Date tampil `23/10/26, 15:45` (15 kar), Photo `tablet-samsung-3.jpg` (20 kar) · sumber turunan penulis
- **DU-053-6** Missing History Record (awal), Record History dengan seluruh kolom Curated terisi: Name `Mobile Printer Zebra ZQ320 - 5` (30 kar), Asset ID `PRN-2026-0205` (13 kar), Group `Head Office` (11 kar), Status `Found` (5 kar), Brand `Zebra Technologies` (18 kar), Model/Type `Mobile Printer ZQ320` (20 kar), TAG `BLE, QR` (7 kar), Category `Mobile Printer` (14 kar), Hierarki Category `Hardware > Printer > Mobile Printer` (35 kar), Alias Name `Printer Lapangan` (16 kar), Measurement `Unit` (4 kar), Division `Operations` (10 kar), Labels `Portable, Priority` (18 kar), Asset Class `Electronic Equipment` (20 kar), Register Date `2024-06-01` (10 kar), Register Date tampil `01/06/24` (8 kar), Purchase Date `2024-05-20` (10 kar), Purchase Date tampil `20/05/24` (8 kar), Daftar garansi `Garansi Pabrik — 2026-12-05 | Garansi Layanan Purna Jual — 2027-04-18 | Garansi Baterai — 2027-09-30` (100 kar), Warranty Expiry (Warranty until terdekat) `2026-12-05` (10 kar), Warranty Expiry tampil `05/12/26` (8 kar), Hover daftar garansi `Garansi Pabrik — 05/12/26 | Garansi Layanan Purna Jual — 18/04/27 | Garansi Baterai — 30/09/27` (94 kar), Purchase Cost `4500000` (7 kar), Asset Value (Commercial) `3200000` (7 kar), Asset Value (Fiscal) `2800000` (7 kar) · sumber turunan penulis
- **DU-053-7** Missing History Record (awal), Record History dengan kolom Curated kosong: Name `Lemari Arsip Besi - 2` (21 kar), Asset ID `FRN-2026-0302` (13 kar), Group `Head Office` (11 kar), Status `Found` (5 kar), Brand `null` (4 kar), Model/Type `null` (4 kar), TAG `null` (4 kar), Category `Furniture` (9 kar), Hierarki Category `Furniture` (9 kar), Alias Name `null` (4 kar), Measurement `null` (4 kar), Division `null` (4 kar), Labels `null` (4 kar), Asset Class `null` (4 kar), Register Date `2025-02-14` (10 kar), Register Date tampil `14/02/25` (8 kar), Purchase Date `null` (4 kar), Warranty Expiry `null` (4 kar), Purchase Cost `null` (4 kar), Asset Value (Commercial) `null` (4 kar), Asset Value (Fiscal) `null` (4 kar) · sumber turunan penulis
- **DU-053-8** Kata Kunci (dicoba), Kata kunci Search tanpa hasil: Kata kunci Search `ZZZ-TIDAK-ADA` (13 kar) · sumber turunan penulis
- **DU-053-9** Missing History Record (awal), Record History Found tanpa foto, dilaporkan PIC atas nama pemegang tanpa akun: Name `Forklift Toyota 8FD - 6` (23 kar), Asset ID `FLK-2026-0006` (13 kar), Group `Warehouse` (9 kar), Hierarki Group `Warehouse` (9 kar), Status `Found` (5 kar), Source `Reported by holder` (18 kar), Last Holder `Joko Susanto` (12 kar), Last Holder tampil `Joko S` (6 kar), Last Holder hover PIC `PIC: Rudi Hartono` (17 kar), Reported By `Rudi Hartono (PIC) atas nama Joko Susanto` (41 kar), Reported By tampil `Rudi H (on behalf of Joko S)` (28 kar), Reported Date `2026-10-25T07:15:00Z` (20 kar), Reported Date tampil `25/10/26, 07:15` (15 kar), Duration `2` (1 kar), Duration tampil `2 days` (6 kar), Resolved By `Rina Wulandari` (14 kar), Resolved By tampil `Rina W` (6 kar), Resolved Date `2026-10-27T10:30:00Z` (20 kar), Resolved Date tampil `27/10/26, 10:30` (15 kar), Photo `tanpa foto (avatar inisial)` (27 kar) · sumber turunan penulis
- **DU-053-10** Missing History Record (awal), Record History dengan tiga garansi yang urutan daftarnya tidak dimulai dari garansi terdekat: Name `Generator Honda EU22i - 4` (25 kar), Asset ID `GEN-2026-0104` (13 kar), Group `Warehouse` (9 kar), Status `Found` (5 kar), Register Date `2025-04-11` (10 kar), Register Date tampil `11/04/25` (8 kar), Purchase Date `2025-04-01` (10 kar), Purchase Date tampil `01/04/25` (8 kar), Daftar garansi `Garansi Mesin — 2028-04-01 | Garansi Aki — 2027-01-15 | Garansi Servis — 2026-12-12` (83 kar), Warranty Expiry (Warranty until terdekat) `2026-12-12` (10 kar), Warranty Expiry tampil `12/12/26` (8 kar), Hover daftar garansi `Garansi Mesin — 01/04/28 | Garansi Aki — 15/01/27 | Garansi Servis — 12/12/26` (77 kar), Purchase Cost `18500000` (8 kar), Asset Value (Commercial) `16200000` (8 kar), Asset Value (Fiscal) `14800000` (8 kar) · sumber turunan penulis
- **DU-054-1** Asset (awal), Aset yang dipegang Joko S, dilaporkan Pelapor admin: Name `Hand Pallet Truck` (17 kar), Increment `3` (1 kar), Asset ID `HPT-2026-0003` (13 kar), TAG `RFID` (4 kar), Brand `Jungheinrich` (12 kar), Group `Warehouse` (9 kar), Model/Type `JH-HPT25` (8 kar), Asset Status `Assigned` (8 kar), Photo `hpt-2026-0003.jpg` (17 kar), Pemegang `Joko S` (6 kar) · sumber PRD §4.1a Example Data
- **DU-054-2** Asset (awal), Aset yang dipegang Andi P: Name `Laptop Dell Latitude 5420` (25 kar), Increment `22` (2 kar), Asset ID `LPT-2026-0022` (13 kar), TAG `NFC` (3 kar), Brand `Dell` (4 kar), Group `Finance Room` (12 kar), Model/Type `Latitude 5420` (13 kar), Asset Status `Assigned` (8 kar), Photo `lpt-2026-0022.jpg` (17 kar), Pemegang `Andi P` (6 kar) · sumber PRD §4.1a Example Data
- **DU-054-3** Asset (awal), Aset yang dipegang Sari D: Name `Monitor LG 27UL500` (18 kar), Increment `11` (2 kar), Asset ID `MON-2026-0011` (13 kar), TAG `QR` (2 kar), Brand `LG` (2 kar), Group `Head Office` (11 kar), Model/Type `27UL500` (7 kar), Asset Status `Assigned` (8 kar), Photo `mon-2026-0011.jpg` (17 kar), Pemegang `Sari D` (6 kar) · sumber PRD §4.1a Example Data
- **DU-054-4** Asset (awal), Aset tanpa pemegang: Name `Toyota Innova` (13 kar), Increment `2` (1 kar), Asset ID `VEH-2026-0002` (13 kar), TAG `GPS` (3 kar), Brand `Toyota` (6 kar), Group `Branch Surabaya` (15 kar), Model/Type `Innova` (6 kar), Asset Status `Available` (9 kar), Photo `veh-2026-0002.jpg` (17 kar) · sumber PRD §4.1a Example Data
- **DU-054-5** Asset (awal), Aset yang dipegang Joko S, dilaporkan pemegangnya sendiri: Name `Scanner Zebra DS2208` (20 kar), Increment `2` (1 kar), Asset ID `SCN-2026-0002` (13 kar), TAG `BLE` (3 kar), Brand `Zebra` (5 kar), Group `Warehouse` (9 kar), Model/Type `DS2208` (6 kar), Asset Status `Assigned` (8 kar), Photo `scn-2026-0002.jpg` (17 kar), Pemegang `Joko S` (6 kar) · sumber PRD §4.1b Example Data
- **DU-054-6** Asset (awal), Aset kedua yang dipegang Joko S: Name `Camera Canon EOS` (16 kar), Increment `1` (1 kar), Asset ID `CAM-2026-0001` (13 kar), TAG `RFID` (4 kar), Brand `Canon` (5 kar), Group `Head Office` (11 kar), Model/Type `EOS 90D` (7 kar), Asset Status `Assigned` (8 kar), Photo `cam-2026-0001.jpg` (17 kar), Pemegang `Joko S` (6 kar) · sumber PRD §4.1b Example Data
- **DU-054-7** Asset (awal), Aset yang dipegang Andi P dengan efek modul pemilik gagal: Name `Printer HP LaserJet M404` (24 kar), Increment `5` (1 kar), Asset ID `PRN-2026-0005` (13 kar), TAG `QR` (2 kar), Brand `HP` (2 kar), Group `Head Office` (11 kar), Model/Type `LaserJet M404` (13 kar), Asset Status `Assigned` (8 kar), Photo `prn-2026-0005.jpg` (17 kar), Pemegang `Andi P` (6 kar) · sumber PRD §4.1a Example Data
- **DU-054-8** Kotak Dampak (awal), Kotak dampak satu transaksi Borrow pada satu aset: Borrow `BRW-2026-0141` (13 kar) · sumber §4.2.3#p2
- **DU-054-9** Kotak Dampak (awal), Kotak dampak dua aset, masing-masing dengan transaksi Borrow: Borrow aset Laptop Dell Latitude 5420 `BRW-2026-0152` (13 kar), Borrow aset Monitor LG 27UL500 `BRW-2026-0153` (13 kar) · sumber §4.2.3#p2
- **DU-054-10** Isian Awal (awal), Isian awal What happened dari titik masuk: What happened `Aset tidak ditemukan saat pengecekan rak` (40 kar) · sumber turunan penulis
- **DU-054-11** Tab Missing (awal), Jumlah record yang perlu ditindaklanjuti nol: Jumlah `0` (1 kar) · sumber §4.3#r1
- **DU-054-12** Tab Missing (awal), Jumlah record yang perlu ditindaklanjuti dua: Jumlah `2` (1 kar) · sumber §4.3#r1
- **DU-054-13** Report Missing (dicoba), What happened dikosongkan: What happened `` (0 kar) · sumber §9.9#r1
- **DU-054-14** Report Missing (dicoba), What happened hanya tiga spasi: What happened `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-054-15** Report Missing (dibuat), What happened tepat di batas minimum satu karakter: What happened `H` (1 kar) · sumber §9.9#r1
- **DU-054-16** Report Missing (dibuat), What happened tepat di batas maksimum 360 karakter: What happened `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 kar) · sumber §9.9#r1
- **DU-054-17** Report Missing (dicoba), What happened satu karakter di atas batas maksimum: What happened `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 kar) · sumber §9.9#r1
- **DU-054-18** Report Missing (dibuat), What happened 360 karakter diapit spasi di awal dan di akhir: What happened `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  ` (364 kar) · sumber foundation prd-conventions.md §4
- **DU-054-19** Report Missing (dibuat), What happened 360 karakter dengan spasi ganda di tengah: What happened `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-054-20** Report Missing (dibuat), What happened 360 code point dengan huruf beraksen dan karakter non-BMP: What happened `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-054-21** Report Missing (dibuat), What happened valid lengkap: What happened `Aset tidak ditemukan di rak gudang setelah inventarisasi akhir bulan` (68 kar) · sumber turunan penulis
- **DU-054-22** Report Missing (dibuat), What happened hasil penyuntingan isian awal: What happened `Aset tidak ditemukan saat pengecekan rak, terakhir terlihat di ruang arsip` (74 kar) · sumber turunan penulis
- **DU-054-23** Kotak Dampak (awal), Kotak dampak aset campuran: satu aset tidak layak dengan Borrow, satu aset layak dengan Borrow: Borrow aset tidak layak `BRW-2026-0150` (13 kar), Borrow aset layak `BRW-2026-0155` (13 kar) · sumber §4.2.3#b1
- **DU-054-24** Kotak Dampak (awal), Kotak dampak satu transaksi Assignment pada satu aset: Assignment `ASG-2026-0071` (13 kar) · sumber §4.2.3#p2
- **DU-055-1** Asset (awal), Aset ber-TAG dengan record Missing, Group Finance Room: Name `Laptop Dell Latitude 5420` (25 kar), Increment `22` (2 kar), Asset ID `LPT-2026-0022` (13 kar), Brand `Dell` (4 kar), Group `Finance Room` (12 kar), Model/Type `Latitude 5420` (13 kar), Status record `Missing` (7 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a Example Data
- **DU-055-2** Asset (awal), Aset tanpa TAG dengan record Missing, Group Head Office (induk): Name `Laptop Lenovo ThinkPad T14` (26 kar), Increment `4` (1 kar), Asset ID `LPT-2026-0004` (13 kar), Brand `Lenovo` (6 kar), Group `Head Office` (11 kar), Model/Type `ThinkPad T14` (12 kar), Status record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-055-3** Asset (awal), Aset asal Damaged + Missing tanpa TAG, Group Server Room: Name `Monitor LG 27UL500` (18 kar), Increment `11` (2 kar), Asset ID `MON-2026-0011` (13 kar), Brand `LG` (2 kar), Group `Server Room` (11 kar), Model/Type `27UL500` (7 kar), Status record `Missing` (7 kar) · sumber turunan penulis
- **DU-055-4** Group (awal), Pohon Group dalam cakupan Group Manager Head Office: Induk `Head Office` (11 kar), Node terbawah `Finance Room` (12 kar), Node terbawah 2 `Server Room` (11 kar), Di luar cakupan `Warehouse` (9 kar) · sumber §4.2.4#p6
- **DU-055-5** Group (awal), Pohon Group untuk Total Control: Induk `Head Office` (11 kar), Node terbawah `Finance Room` (12 kar), Node terbawah 2 `Server Room` (11 kar), Group lain `Warehouse` (9 kar) · sumber §4.2.4#p6
- **DU-055-6** Mark as Found (dibuat), Found at dipilih ke Group lain: Found at `Server Room` (11 kar) · sumber §4.2.4#p6
- **DU-055-7** Mark as Found (dibuat), Asset Status dibiarkan Normal: Asset Status `Normal` (6 kar) · sumber §9.9#r4
- **DU-055-8** Mark as Found (dibuat), Asset Status dipilih Damaged: Asset Status `Damaged` (7 kar) · sumber §9.9#r4
- **DU-055-9** Mark as Found (dibuat), Note valid yang diisi lalu Asset Status diganti: Note `Layar retak di sudut kiri atas` (30 kar) · sumber turunan penulis
- **DU-055-10** Mark as Found (dicoba), Note Damaged dikosongkan: Note `` (0 kar) · sumber §9.9#r5
- **DU-055-11** Mark as Found (dicoba), Note Damaged hanya tiga spasi: Note `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-055-12** Mark as Found (dibuat), Note Damaged tepat di batas minimum satu karakter: Note `H` (1 kar) · sumber §9.9#r5
- **DU-055-13** Mark as Found (dibuat), Note tepat di batas maksimum 360 karakter: Note `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 kar) · sumber §9.9#r5
- **DU-055-14** Mark as Found (dicoba), Note satu karakter di atas batas maksimum: Note `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 kar) · sumber §9.9#r5
- **DU-055-15** Mark as Found (dibuat), Note 360 karakter diapit spasi di awal dan di akhir: Note `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  ` (364 kar) · sumber foundation prd-conventions.md §4
- **DU-055-16** Mark as Found (dibuat), Note 360 karakter dengan spasi ganda di tengah: Note `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-055-17** Mark as Found (dibuat), Note 360 code point dengan huruf beraksen dan karakter non-BMP: Note `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-055-18** Mark as Found (dibuat), Note dikosongkan pada Asset Status Normal: Note `` (0 kar) · sumber §9.9#r5
- **DU-055-19** Mark as Found (dicoba), Damaged Photo tidak diunggah: Damaged Photo `` (0 kar) · sumber §9.9#r6
- **DU-055-20** Mark as Found (dibuat), Damaged Photo berformat PNG: Damaged Photo `kerusakan-unit.png` (18 kar) · sumber §9.9#p4
- **DU-055-21** Mark as Found (dibuat), Damaged Photo berformat JPG di bawah 1 MB: Damaged Photo `kerusakan-unit.jpg` (18 kar), Ukuran `300 KB` (6 kar) · sumber §9.9#p4
- **DU-055-22** Mark as Found (dibuat), Damaged Photo berformat JPEG: Damaged Photo `kerusakan-unit.jpeg` (19 kar) · sumber §9.9#p4
- **DU-055-23** Mark as Found (dibuat), Damaged Photo berukuran di atas 1 MB: Damaged Photo `kerusakan-besar.jpg` (19 kar), Ukuran `3 MB` (4 kar) · sumber §9.9#p4
- **DU-055-24** Mark as Found (dicoba), Damaged Photo berformat PDF yang tidak diterima picker: Damaged Photo `dokumen-kerusakan.pdf` (21 kar) · sumber §9.9#p4
- **DU-055-25** Mark as Found (dicoba), Damaged Photo berformat GIF yang tidak diterima picker: Damaged Photo `kerusakan-unit.gif` (18 kar) · sumber §9.9#p4
- **DU-055-26** Asset (awal), Aset tanpa TAG dengan record Missing berpenanda Long missing, Group Head Office: Name `Printer Epson L3250` (19 kar), Increment `7` (1 kar), Asset ID `PRN-2026-0007` (13 kar), Brand `Epson` (5 kar), Group `Head Office` (11 kar), Model/Type `L3250` (5 kar), Status record `Missing` (7 kar), Penanda `Long missing` (12 kar), Days Missing `34` (2 kar), Long missing after `30` (2 kar) · sumber §4.2.4#p2
- **DU-056-1** Asset (awal), Aset dengan laporan pemegang yang ditolak: Name `Hand Pallet Truck` (17 kar), Increment `3` (1 kar), Asset ID `HPT-2026-0003` (13 kar), Group `Warehouse` (9 kar), Status record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-056-2** Reject Report (dicoba), Reason dikosongkan: Reason `` (0 kar) · sumber §9.9#r7
- **DU-056-3** Reject Report (dicoba), Reason hanya tiga spasi: Reason `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-056-4** Reject Report (dibuat), Reason tepat di batas minimum satu karakter: Reason `H` (1 kar) · sumber §9.9#r7
- **DU-056-5** Reject Report (dibuat), Reason tepat di batas maksimum 360 karakter: Reason `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 kar) · sumber §9.9#r7
- **DU-056-6** Reject Report (dicoba), Reason satu karakter di atas batas maksimum: Reason `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 kar) · sumber §9.9#r7
- **DU-056-7** Reject Report (dibuat), Reason 360 karakter diapit spasi di awal dan di akhir: Reason `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  ` (364 kar) · sumber foundation prd-conventions.md §4
- **DU-056-8** Reject Report (dibuat), Reason 360 karakter dengan spasi ganda di tengah: Reason `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-056-9** Reject Report (dibuat), Reason 360 code point dengan huruf beraksen dan karakter non-BMP: Reason `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-056-10** Reject Report (dibuat), Reason valid: Reason `Aset sudah ditemukan di gudang oleh petugas lapangan` (52 kar) · sumber turunan penulis
- **DU-057-1** Missing Record (awal), Record Missing dengan penanda Long missing: Name `Laptop Lenovo ThinkPad T14` (26 kar), Increment `4` (1 kar), Asset ID `LPT-2026-0004` (13 kar), Status record `Missing` (7 kar), Penanda `Long missing` (12 kar) · sumber PRD §4.1a Example Data
- **DU-057-2** Missing Record (awal), Record Missing tanpa penanda Long missing: Name `Toyota Innova` (13 kar), Increment `2` (1 kar), Asset ID `VEH-2026-0002` (13 kar), Status record `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-057-3** Add Update (dicoba), Update dikosongkan: Update `` (0 kar) · sumber §9.9#r8
- **DU-057-4** Add Update (dicoba), Update hanya tiga spasi: Update `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-057-5** Add Update (dibuat), Update tepat di batas minimum satu karakter: Update `H` (1 kar) · sumber §9.9#r8
- **DU-057-6** Add Update (dibuat), Update tepat di batas maksimum 360 karakter: Update `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra` (360 kar) · sumber §9.9#r8
- **DU-057-7** Add Update (dicoba), Update satu karakter di atas batas maksimum: Update `Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke raZ` (361 kar) · sumber §9.9#r8
- **DU-057-8** Add Update (dibuat), Update 360 karakter diapit spasi di awal dan di akhir: Update `  Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke rak penyimpanan sejak inventarisasi akhir bulan dan tidak ada catatan peminjaman terbaru. Aset belum kembali ke ra  ` (364 kar) · sumber foundation prd-conventions.md §4
- **DU-057-9** Add Update (dibuat), Update 360 karakter dengan spasi ganda di tengah: Update `Aset belum kembali ke rak  penyimpanan sejak inventarisasi akhir bulan  dan tidak ada catatan peminjaman  terbaru.  Aset belum kembali  ke rak penyimpanan sejak inventarisasi  akhir bulan dan tidak ada  catatan peminjaman terbaru.  Aset  belum kembali ke rak penyimpanan  sejak inventarisasi akhir bulan dan  tidak ada catatan peminjaman terbaru.   Aset belum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-057-10** Add Update (dibuat), Update 360 code point dengan huruf beraksen dan karakter non-BMP: Update `Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum dipindahkan ke lantai tiga bangunan baru. Kantor Cabang Medan Élan 𝒜 menyimpan aset di ruang arsip Éléonore dan gudang Müller sebelum.` (360 kar) · sumber foundation prd-conventions.md §4
- **DU-057-11** Add Update (dibuat), Update valid: Update `Petugas sudah memeriksa rekaman CCTV lobi dan belum menemukan aset` (66 kar) · sumber turunan penulis
- **DU-058-1** Missing Record (awal), Record Waiting for Confirmation, Last holder Sari D: Name `Monitor LG 27UL500` (18 kar), Increment `11` (2 kar), Asset ID `MON-2026-0011` (13 kar), Group `Head Office` (11 kar), Status record `Waiting for Confirmation` (24 kar), Last Holder `Sari D` (6 kar), Reported By `Sari D` (6 kar) · sumber PRD §4.1a Example Data
- **DU-058-2** Missing Record (awal), Record Missing tanpa penanda: Name `Laptop Dell Latitude 5420` (25 kar), Increment `22` (2 kar), Asset ID `LPT-2026-0022` (13 kar), Group `Finance Room` (12 kar), Status record `Missing` (7 kar), Last Holder `Andi P` (6 kar), Reported By `Andi P` (6 kar) · sumber PRD §4.1a Example Data
- **DU-058-3** Missing Record (awal), Record Missing dengan penanda Long missing: Name `Laptop Lenovo ThinkPad T14` (26 kar), Increment `4` (1 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Status record `Missing` (7 kar), Last Holder `Dewi A` (6 kar), Reported By `Rina W` (6 kar), Penanda `Long missing` (12 kar) · sumber PRD §4.1a Example Data
- **DU-058-4** Reject Report (dibuat), Reason penolakan laporan: Reason `Aset masih tercatat dipegang oleh pelapor` (41 kar) · sumber turunan penulis
- **DU-058-5** Missing Record (awal), Record Waiting for Confirmation yang sudah punya node Detected by scan: Name `Printer HP LaserJet M404` (24 kar), Increment `5` (1 kar), Asset ID `PRN-2026-0005` (13 kar), Group `Head Office` (11 kar), Status record `Waiting for Confirmation` (24 kar), Last Holder `Andi P` (6 kar), Reported By `Andi P` (6 kar), Detected by scan `08/11/26` (8 kar) · sumber §1.2#r113
- **DU-059-1** Missing Record (awal), Record Waiting for Confirmation yang dilaporkan pemegang: Name `Scanner Zebra DS2208` (20 kar), Increment `2` (1 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Warehouse` (9 kar), Status record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1b Example Data
- **DU-059-2** Asset (awal), Aset yang tidak dilaporkan hilang: Name `Camera Canon EOS` (16 kar), Increment `1` (1 kar), Asset ID `CAM-2026-0001` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1b Example Data
- **DU-059-3** Asset (awal), Aset yang sedang dalam proses disposal: Name `Printer HP LaserJet M404` (24 kar), Increment `5` (1 kar), Asset ID `PRN-2026-0005` (13 kar), Group `Head Office` (11 kar), Status record `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-059-4** Missing Record (awal), Record yang statusnya sudah diubah pengguna lain: Name `Hand Pallet Truck` (17 kar), Increment `3` (1 kar), Asset ID `HPT-2026-0003` (13 kar), Group `Warehouse` (9 kar), Status record `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-070-1** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor, dipegang pemegang, punya scan terakhir: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA070-001` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `Joko Susilo {runId}` (19 kar), Scan terakhir `Lobby reader pada T0 − 2 hari, pukul 09:00` (42 kar) · sumber PRD §4.1a Example Data
- **DU-070-2** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor, tanpa pemegang, belum pernah terpindai, punya Work Order, jadwal maintenance, dan item sesi pemeriksaan aset berjalan: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA070-002` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Scan terakhir `belum pernah terpindai` (22 kar), Transaksi lain berjalan `Work Order berjalan, jadwal maintenance, dan item sesi pemeriksaan aset berjalan` (80 kar), Activity Lock `In Audit` (8 kar) · sumber PRD §4.1a Example Data
- **DU-070-3** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor dengan Condition Damaged: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA070-003` (9 kar), Group `Server Room` (11 kar), Condition `Damaged` (7 kar), Pemegang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-070-4** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor dengan Activity Lock Under Maintenance: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA070-004` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Activity Lock `Under Maintenance` (17 kar) · sumber PRD §4.1a Example Data
- **DU-070-5** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor yang dipegang Andi P: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `FA070-005` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `Andi P` (6 kar) · sumber PRD §4.1a Example Data
- **DU-070-6** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor yang dipegang pemegang tanpa hak Aktor Missing: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA070-006` (9 kar), Group `Warehouse` (9 kar), Condition `Normal` (6 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-070-7** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor di antara aset tidak layak dalam satu laporan: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA070-007` (9 kar), Group `Warehouse` (9 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-070-8** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang sudah punya record berjalan Missing: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA070-008` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Missing` (7 kar), What happened record `Kamera tidak ada di lemari penyimpanan` (38 kar), Pelapor record `Rina W` (6 kar) · sumber PRD §4.1a Example Data
- **DU-070-9** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang sudah punya record berjalan Waiting for Confirmation: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA070-009` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-070-10** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang sudah punya record berjalan Reported Disposal: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA070-010` (9 kar), Group `Server Room` (11 kar), Condition `Normal` (6 kar), Record berjalan `Reported Disposal` (17 kar) · sumber PRD §4.1a Example Data
- **DU-070-11** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang sudah punya record berjalan In Disposal Process: Name `Mesin Fotokopi Ricoh {runId}` (28 kar), Asset ID `FA070-011` (9 kar), Group `Server Room` (11 kar), Condition `Normal` (6 kar), Record berjalan `In Disposal Process` (19 kar) · sumber turunan penulis
- **DU-070-12** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset Disposed dengan record History Disposed: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA070-012` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Lifecycle `Disposed` (8 kar), Record History `Disposed` (8 kar), Riwayat transaksi `satu riwayat transaksi aset` (27 kar) · sumber turunan penulis
- **DU-070-13** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset layak lapor di Group di luar cakupan Andi P: Name `Hand Truck Gudang {runId}` (25 kar), Asset ID `FA070-013` (9 kar), Group `Warehouse` (9 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar) · sumber turunan penulis
- **DU-070-14** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang dipegang Andi P, dilaporkan oleh bukan pemegangnya: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA070-014` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `Andi P` (6 kar) · sumber turunan penulis
- **DU-070-15** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang dipegang pemegang yang kemudian dinonaktifkan: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA070-015` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `Sari Dewi {runId}` (17 kar) · sumber turunan penulis
- **DU-070-16** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset yang dilaporkan dua aktor pada saat yang sama: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA070-016` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar) · sumber turunan penulis
- **DU-070-17** User (awal), Pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar) · sumber matriks role PRD
- **DU-070-18** User (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Pemegang yang dinonaktifkan sesudah aset dilaporkan: Name `Sari Dewi {runId}` (17 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Status `Active` (6 kar) · sumber matriks role PRD
- **DU-070-19** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset Unmanaged tanpa record berjalan, dengan record History dan riwayat transaksi, boleh dihapus: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA070-019` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Lifecycle `Unmanaged` (9 kar), Record History `Found` (5 kar), Riwayat transaksi `satu riwayat transaksi aset` (27 kar) · sumber turunan penulis
- **DU-070-20** Group (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Group yang dirujuk record berjalan: Name `Ruang Arsip {runId}` (19 kar) · sumber turunan penulis
- **DU-070-21** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset di Group Ruang Arsip dengan record berjalan Missing: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA070-021` (9 kar), Group `Ruang Arsip {runId}` (19 kar), Condition `Normal` (6 kar), Record berjalan `Missing` (7 kar) · sumber turunan penulis
- **DU-070-22** Group (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Group yang hanya dirujuk record History sebagai Found at: Name `Lantai Dua {runId}` (18 kar) · sumber turunan penulis
- **DU-070-23** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dengan record History Found yang Found at-nya Group Lantai Dua: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA070-023` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Record History `Found, Found at Lantai Dua {runId}` (34 kar) · sumber turunan penulis
- **DU-070-24** Laporan Missing (dibuat), What happened laporan Pelapor admin: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
- **DU-070-25** Laporan Missing (dibuat), What happened laporan pemegang: What happened `Terakhir terlihat di pantry lantai dua` (38 kar) · sumber turunan penulis
- **DU-070-26** Category (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Category yang dirujuk aset dengan record berjalan: Name `Perabot Arsip {runId}` (21 kar) · sumber turunan penulis
- **DU-070-27** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset ber-Category Perabot Arsip dengan record berjalan Missing: Name `Lemari Arsip Baja {runId}` (25 kar), Asset ID `FA070-027` (9 kar), Group `Finance Room` (12 kar), Category `Perabot Arsip {runId}` (21 kar), Condition `Normal` (6 kar), Record berjalan `Missing` (7 kar) · sumber turunan penulis
- **DU-070-28** Category (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Category yang hanya dirujuk record History: Name `Peralatan Gudang {runId}` (24 kar) · sumber turunan penulis
- **DU-070-29** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dengan record History Found yang Category tersimpannya Peralatan Gudang: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA070-029` (9 kar), Group `Finance Room` (12 kar), Category `Perabot Arsip {runId}` (21 kar), Condition `Normal` (6 kar), Record History `Found, Category Peralatan Gudang {runId}` (40 kar) · sumber turunan penulis
- **DU-070-30** User (awal), Staff Auditor tanpa hak Aktor Missing: Name `Hendra Kusuma {runId}` (21 kar), Peran `Staff Auditor tanpa hak Aktor Missing` (37 kar) · sumber matriks role PRD
- **DU-070-31** Sesi Audit (awal), Sesi Audit milik Hendra yang memuat tiga aset: Name `Audit Ruang Server {runId}` (26 kar), Pemilik `Hendra Kusuma {runId}` (21 kar), Aset `Rak Server Dell {runId}, Switch Cisco Catalyst {runId}, UPS APC Smart {runId}` (77 kar) · sumber §1.2#r71
- **DU-070-32** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dalam sesi Audit, dilapor Staff Auditor: Name `Rak Server Dell {runId}` (23 kar), Asset ID `FA070-032` (9 kar), Group `Server Room` (11 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Sesi Audit `Audit Ruang Server {runId}` (26 kar) · sumber §1.2#r71
- **DU-070-33** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dalam sesi Audit, dilapor Total Control: Name `Switch Cisco Catalyst {runId}` (29 kar), Asset ID `FA070-033` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Sesi Audit `Audit Ruang Server {runId}` (26 kar) · sumber §1.2#r71
- **DU-070-34** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dalam sesi Audit, dilapor Group Manager: Name `UPS APC Smart {runId}` (21 kar), Asset ID `FA070-034` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Sesi Audit `Audit Ruang Server {runId}` (26 kar) · sumber §1.2#r71
- **DU-070-35** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset di luar cakupan sesi Audit: Name `Proyektor BenQ MW550 {runId}` (28 kar), Asset ID `FA070-035` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Sesi Audit `tidak termasuk dalam sesi Audit Audit Ruang Server {runId}` (58 kar) · sumber §1.2#r71
- **DU-070-36** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset dengan record Missing berjalan, Activity Lock In Audit, dan baris sesi pemeriksaan aset yang sudah final: Name `Kabinet Besi Arsip {runId}` (26 kar), Asset ID `FA070-036` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Record berjalan `Missing` (7 kar), Activity Lock `In Audit` (8 kar), Baris sesi pemeriksaan aset `sudah final` (11 kar) · sumber PRD §1.2 MISS-LOGIC-04j
- **DU-070-37** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset tanpa record Missing berjalan dengan baris Disposal Waiting for Approval berjenis Sell: Name `Generator Perkins 20kVA {runId}` (31 kar), Asset ID `FA070-037` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Baris Disposal `Waiting for Approval, jenis Sell` (32 kar) · sumber PRD §9.2 F-MISS-05.k4
- **DU-070-38** Asset (awal; dimutasi TC-FA-MISS-BE-070-kelayakan-report-missing), Aset tanpa record Missing berjalan yang tercantum dalam Draft Disposal berjenis Scrap: Name `Kompresor Udara Swan {runId}` (28 kar), Asset ID `FA070-038` (9 kar), Group `Finance Room` (12 kar), Condition `Normal` (6 kar), Pemegang `tidak ada` (9 kar), Draft Disposal `Scrap` (5 kar) · sumber PRD §9.2 F-MISS-05.k4
- **DU-071-1** User (awal), Admin kedua dengan hak Aktor Missing dan Aktor Disposal: Name `Bambang Wijaya {runId}` (22 kar), Peran `Total Control` (13 kar) · sumber matriks role PRD
- **DU-071-2** User (awal), Pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar) · sumber matriks role PRD
- **DU-071-3** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan laporan pemegang yang menunggu konfirmasi, dilalui sampai Found: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA071-001` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-4** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan laporan pemegang yang akan ditolak: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA071-002` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-5** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan laporan pemegang yang akan dibatalkan pelapor: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA071-003` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-6** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation untuk pasangan Confirm dan Mark as Found: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA071-004` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-7** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Missing untuk pasangan Add Update dan Mark as Found: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA071-005` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-071-8** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation untuk pasangan Review dan Reject: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA071-006` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-9** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation untuk pasangan Cancel Report dan Confirm: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA071-007` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-10** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Reported Disposal untuk pasangan Cancel Disposal Report dan Dispose: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA071-008` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Reported Disposal` (17 kar) · sumber PRD §4.1a Example Data
- **DU-071-11** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset In Disposal Process yang berubah oleh System: Name `Mesin Fotokopi Ricoh {runId}` (28 kar), Asset ID `FA071-009` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-12** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset In Disposal Process dengan baris Disposal yang akan Rejected: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA071-010` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-13** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset In Disposal Process dengan baris Disposal yang akan Canceled: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA071-011` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-14** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset In Disposal Process dengan baris Disposal yang akan Removed: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA071-012` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-15** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset In Disposal Process dengan baris Disposal yang akan timeout: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA071-013` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-16** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Reported Disposal yang akan di-Decline: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `FA071-014` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Reported Disposal` (17 kar) · sumber PRD §4.1a Example Data
- **DU-071-17** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation yang dilaporkan T0 − 90 hari: Name `Hand Truck Gudang {runId}` (25 kar), Asset ID `FA071-015` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation, dilaporkan T0 − 90 hari` (49 kar) · sumber PRD §4.1a Example Data
- **DU-071-18** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Missing yang dilaporkan T0 − 45 hari: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA071-016` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Missing, dilaporkan T0 − 45 hari` (32 kar) · sumber PRD §4.1a Example Data
- **DU-071-19** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation yang Condition tersimpannya tidak lagi dapat dipulihkan untuk Reject: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA071-017` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Condition tersimpan `Damaged, tidak lagi dapat dipulihkan` (36 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-20** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset Waiting for Confirmation yang Condition tersimpannya tidak lagi dapat dipulihkan untuk Cancel Report: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA071-018` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Condition tersimpan `Damaged, tidak lagi dapat dipulihkan` (36 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-071-21** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan record selesai Found: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA071-019` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Found` (5 kar) · sumber PRD §4.1a Example Data
- **DU-071-22** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan record selesai Disposed lalu aset dihapus: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA071-020` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Disposed` (8 kar) · sumber PRD §4.1a Example Data
- **DU-071-23** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan record selesai Rejected: Name `Lemari Arsip Besi {runId}` (25 kar), Asset ID `FA071-021` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Rejected` (8 kar) · sumber PRD §4.1a Example Data
- **DU-071-24** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan record selesai Canceled: Name `Kipas Angin Standing {runId}` (28 kar), Asset ID `FA071-022` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Canceled` (8 kar) · sumber PRD §4.1a Example Data
- **DU-071-25** Input aksi (dibuat), Update pertama: Update `Pencarian di gudang lantai satu belum membuahkan hasil` (54 kar) · sumber turunan penulis
- **DU-071-26** Input aksi (dibuat), Update kedua: Update `Pencarian di gudang lantai dua belum membuahkan hasil` (53 kar) · sumber turunan penulis
- **DU-071-27** Input aksi (dibuat), Reason Reject: Reason `Aset masih dipakai di meja pemegang` (35 kar) · sumber turunan penulis
- **DU-071-28** Input aksi (dibuat), Reason Report Disposal: Reason `Aset tidak ditemukan setelah pencarian dua pekan` (48 kar) · sumber turunan penulis
- **DU-071-29** Input aksi (dibuat), What happened laporan ulang: What happened `Aset hilang lagi sesudah pemeriksaan bulanan` (44 kar) · sumber turunan penulis
- **DU-071-30** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset dengan record Waiting for Confirmation untuk Confirm yang atomik: Name `Kulkas Pendingin {runId}` (24 kar), Asset ID `FA071-023` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Record berjalan `Waiting for Confirmation` (24 kar), Pelapor `Joko Susilo {runId}` (19 kar) · sumber turunan penulis
- **DU-071-31** User (awal), Staff Auditor tanpa hak Aktor Missing: Name `Sabrina Putri {runId}` (21 kar), Peran `Staff Auditor tanpa hak Aktor Missing` (37 kar) · sumber matriks role PRD
- **DU-071-32** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset laporan Source Audit yang dibatalkan pelapor: Name `Kabinet Server {runId}` (22 kar), Asset ID `FA071-024` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Waiting for Confirmation` (24 kar), Source `Audit` (5 kar), Pelapor `Sabrina Putri {runId}` (21 kar), Baris sesi Audit `Pending` (7 kar) · sumber §9.4.2#r38
- **DU-071-33** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset laporan Source Audit yang lebih dulu dikonfirmasi Aktor Missing: Name `Meja Resepsionis {runId}` (24 kar), Asset ID `FA071-025` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Waiting for Confirmation` (24 kar), Source `Audit` (5 kar), Pelapor `Sabrina Putri {runId}` (21 kar) · sumber §9.4.2#r38
- **DU-071-34** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset yang dilaporkan langsung Missing oleh Total Control dari Task Detail Audit: Name `Lemari Berkas Jati {runId}` (26 kar), Asset ID `FA071-026` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Record berjalan `Missing` (7 kar), Source `Audit` (5 kar) · sumber §9.4.2#r38
- **DU-071-35** Sesi Audit (awal), Sesi Audit milik Sabrina yang memuat aset laporan: Name `Audit Gudang {runId}` (20 kar), Pemilik `Sabrina Putri {runId}` (21 kar) · sumber §9.4.2#r38
- **DU-071-36** Asset (awal; dimutasi TC-FA-MISS-BE-071-transisi-status-dan-konflik), Aset laporan Source Audit yang dipegang dengan baris Borrow terbuka, untuk Confirm yang menutup baris: Name `Server Rack Gudang {runId}` (26 kar), Asset ID `FA071-027` (9 kar), Condition `Normal` (6 kar), TAG `tanpa TAG` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar), Baris transaksi `berjalan berstatus Borrowed untuk Joko Susilo {runId}` (53 kar), Record berjalan `Waiting for Confirmation` (24 kar), Source `Audit` (5 kar), Pelapor `Sabrina Putri {runId}` (21 kar) · sumber §9.4.2#r37
- **DU-072-1** User (awal), Pengguna Total Control: Name `Hendra Pratama {runId}` (22 kar), Peran `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-072-2** User (awal), Pengguna Group Manager: Name `Maya Anggraini {runId}` (22 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-072-3** User (awal), Pengguna Manage asset & TAG dengan Update pada Head Office dan Read pada Warehouse: Name `Dewi Anindita {runId}` (21 kar), Peran `Manage asset & TAG dengan Update pada Head Office dan Read pada Warehouse` (73 kar), Cakupan `Head Office beserta descendant untuk Update, Warehouse untuk Read` (65 kar) · sumber matriks role PRD
- **DU-072-4** User (awal), Pengguna Accounting dengan Manage accounting Read dan Update: Name `Eko Wibowo {runId}` (18 kar), Peran `Accounting dengan Manage accounting Read dan Update` (51 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-072-5** User (awal), Pengguna Read Only: Name `Fajar Nugroho {runId}` (21 kar), Peran `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-072-6** User (awal), Pengguna Manage asset & TAG dengan Read: Name `Gita Lestari {runId}` (20 kar), Peran `Manage asset & TAG dengan Read` (30 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-072-7** User (awal), Pengguna View asset value: Name `Hari Susanto {runId}` (20 kar), Peran `View asset value` (16 kar), Cakupan `Group Head Office beserta descendant` (36 kar) · sumber matriks role PRD
- **DU-072-8** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-072-9** User (awal), Pengguna tanpa capability apa pun di modul Missing: Name `Indra Kusuma {runId}` (20 kar), Peran `tanpa capability apa pun di modul Missing` (41 kar), Cakupan `tanpa cakupan` (13 kar) · sumber matriks role PRD
- **DU-072-10** User (awal), Pengguna Group Manager yang memperoleh hak itu sesudah laporan pemegang atas Camera Canon EOS dan Lemari Arsip Besi dibuat: Name `Andi Prasetyo {runId}` (21 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-072-11** User (awal), Pengguna Manage asset & TAG dengan Create dan Delete tanpa Update: Name `Kartika Sari {runId}` (20 kar), Peran `Manage asset & TAG dengan Create dan Delete tanpa Update` (56 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-072-12** User (awal), Pengguna Aktor transaksi tanpa Manage asset & TAG dengan Update: Name `Wulan Sari {runId}` (18 kar), Peran `Aktor transaksi tanpa Manage asset & TAG dengan Update` (54 kar), Cakupan `aset dalam transaksinya sendiri` (31 kar) · sumber matriks role PRD
- **DU-072-13** User (awal), Pengguna Staff Auditor pemilik sesi Audit tanpa Manage asset & TAG dengan Update: Name `Yoga Pratama {runId}` (20 kar), Peran `Staff Auditor pemilik sesi Audit tanpa Manage asset & TAG dengan Update` (71 kar), Cakupan `aset dalam sesinya sendiri` (26 kar) · sumber matriks role PRD
- **DU-072-14** User (awal), Pengguna Manage asset & TAG dengan Update: Name `Nanda Putri {runId}` (19 kar), Peran `Manage asset & TAG dengan Update` (32 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-072-15** User (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Pengguna PIC tanpa hak Aktor Missing: Name `Rudi Hartono {runId}` (20 kar), Peran `PIC tanpa hak Aktor Missing` (27 kar), Cakupan `aset karyawan tanpa akun yang ia wakili` (39 kar) · sumber matriks role PRD
- **DU-072-16** User (awal), Pengguna PIC pengganti tanpa hak Aktor Missing: Name `Taufik Ramadhan {runId}` (23 kar), Peran `PIC pengganti tanpa hak Aktor Missing` (37 kar), Cakupan `aset karyawan tanpa akun yang ia wakili` (39 kar) · sumber matriks role PRD
- **DU-072-17** User (awal), Pengguna karyawan tanpa akun: Name `Budi Santoso {runId}` (20 kar), Peran `karyawan tanpa akun` (19 kar), Cakupan `tanpa akses` (11 kar) · sumber matriks role PRD
- **DU-072-18** User (awal), Pengguna pemegang tanpa hak Aktor Missing yang dinonaktifkan: Name `Lina Marlina {runId}` (20 kar), Peran `pemegang tanpa hak Aktor Missing yang dinonaktifkan` (51 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-072-19** User (awal), Pengguna Group Manager yang juga PIC: Name `Sinta Maharani {runId}` (22 kar), Peran `Group Manager yang juga PIC` (27 kar), Cakupan `Group Head Office beserta sub-group dan aset karyawan tanpa akun yang ia wakili` (79 kar) · sumber matriks role PRD
- **DU-072-20** Sesi (awal), Permintaan tanpa token login: Sesi `tanpa token` (11 kar) · sumber matriks role PRD
- **DU-072-21** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan record Missing dan nilai finansial terisi: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA072-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Hendra Pratama {runId}` (42 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `9800000` (7 kar), Asset Value (Fiscal) `9100000` (7 kar) · sumber PRD §4.1a Example Data
- **DU-072-22** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset layak lapor tanpa record berjalan: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA072-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-072-23** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan laporan pemegang yang menunggu konfirmasi: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA072-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-072-24** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset di Warehouse dengan record Missing dan TAG QR: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA072-004` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Missing, dilaporkan Hendra Pratama {runId}` (42 kar), TAG `QR-072-0001` (11 kar) · sumber PRD §4.1a Example Data
- **DU-072-25** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset di sub-group Server Room dengan record Missing: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA072-005` (9 kar), Group aset `Server Room` (11 kar), Record berjalan `Missing, dilaporkan Hendra Pratama {runId}` (42 kar) · sumber PRD §4.1a Example Data
- **DU-072-26** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan Disposal Report milik Hendra Pratama: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA072-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Hendra Pratama {runId}` (52 kar) · sumber PRD §4.1a Example Data
- **DU-072-27** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset di Warehouse dengan Disposal Report milik Hendra Pratama: Name `Mesin Fotokopi Ricoh {runId}` (28 kar), Asset ID `FA072-007` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Reported Disposal, dilaporkan Hendra Pratama {runId}` (52 kar) · sumber PRD §4.1a Example Data
- **DU-072-28** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset Missing yang akan dilaporkan untuk disposal oleh Accounting: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA072-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Hendra Pratama {runId}` (42 kar) · sumber PRD §4.1a Example Data
- **DU-072-29** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan laporan yang Last holder-nya Andi Prasetyo: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA072-009` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Andi Prasetyo {runId} sebelum ia memperoleh hak Aktor Missing` (98 kar), Pemegang `Andi Prasetyo {runId}` (21 kar) · sumber PRD §4.1a Example Data
- **DU-072-30** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset yang Last holder-nya Andi Prasetyo dan ia laporkan sendiri sebagai Pelapor admin: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA072-010` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Andi Prasetyo {runId}` (41 kar), Pemegang `Andi Prasetyo {runId}` (21 kar) · sumber PRD §4.1a Example Data
- **DU-072-31** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dalam transaksi Wulan Sari: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA072-011` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Transaksi `milik Wulan Sari {runId}` (24 kar) · sumber PRD §4.1a Example Data
- **DU-072-32** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset di luar transaksi Wulan Sari dan tidak dipegang Joko Susilo: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA072-012` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-072-33** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dalam sesi Audit milik Yoga Pratama: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA072-013` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Sesi Audit `milik Yoga Pratama {runId}` (26 kar) · sumber PRD §4.1a Example Data
- **DU-072-34** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset Missing untuk pengujian pencabutan capability: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA072-014` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Hendra Pratama {runId}` (42 kar) · sumber PRD §4.1a Example Data
- **DU-072-35** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset karyawan tanpa akun dengan PIC Rudi Hartono: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `FA072-015` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Pemegang `Budi Santoso {runId}` (20 kar), PIC `Rudi Hartono {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-072-36** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset karyawan tanpa akun dengan PIC Sinta Maharani: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA072-016` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Pemegang `Budi Santoso {runId}` (20 kar), PIC `Sinta Maharani {runId}` (22 kar) · sumber PRD §4.1a Example Data
- **DU-072-37** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan laporan pemegang yang sudah dinonaktifkan: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA072-017` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Lina Marlina {runId}` (57 kar), Pemegang `Lina Marlina {runId}` (20 kar) · sumber PRD §4.1a Example Data
- **DU-072-38** Record entitas lain (awal), Record milik client lain: Name `Meja Kerja Kayu {runId}` (23 kar), Client `client lain` (11 kar), Record berjalan `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-072-39** Record terhapus (awal), Record milik aset yang sudah dihapus: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA072-019` (9 kar), Record `ikut terhapus bersama aset` (26 kar) · sumber PRD §4.1a Example Data
- **DU-072-40** Record (awal), ID record yang tidak pernah dibuat: ID record `00000000-0000-0000-0000-000000000000` (36 kar) · sumber turunan penulis
- **DU-072-41** Input aksi (dibuat), Update input aksi: Update `Pencarian di gudang lantai satu belum membuahkan hasil` (54 kar) · sumber turunan penulis
- **DU-072-42** Input aksi (dibuat), Reason input aksi: Reason `Aset masih dipakai di meja pemegang` (35 kar) · sumber turunan penulis
- **DU-072-43** Input aksi (dibuat), Reason input aksi: Reason `Aset tidak ditemukan setelah pencarian dua pekan` (48 kar) · sumber turunan penulis
- **DU-072-44** Input aksi (dibuat), What happened input aksi: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
- **DU-072-45** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dengan laporan pemegang Waiting for Confirmation yang Last holder-nya Andi Prasetyo, untuk penolakan tanpa efek: Name `Lemari Arsip Besi {runId}` (25 kar), Asset ID `FA072-018` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Andi Prasetyo {runId} sebelum ia memperoleh hak Aktor Missing` (98 kar), Pemegang `Andi Prasetyo {runId}` (21 kar) · sumber turunan penulis
- **DU-072-46** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset karyawan tanpa akun dengan laporan PIC yang akan dinonaktifkan: Name `Mesin Cuci Industri {runId}` (27 kar), Asset ID `FA072-020` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Rudi Hartono {runId} atas nama Budi Santoso {runId}` (88 kar), Pemegang `Budi Santoso {runId}` (20 kar), PIC `Rudi Hartono {runId}` (20 kar) · sumber turunan penulis
- **DU-072-47** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset karyawan tanpa akun dengan laporan PIC yang akan dihapus: Name `Rak Display {runId}` (19 kar), Asset ID `FA072-021` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Citra Dewi {runId} atas nama Budi Santoso {runId}` (86 kar), Pemegang `Budi Santoso {runId}` (20 kar), PIC `Citra Dewi {runId}` (18 kar) · sumber turunan penulis
- **DU-072-48** User (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), PIC tanpa hak Aktor Missing yang akan dihapus: Name `Citra Dewi {runId}` (18 kar), Peran `PIC tanpa hak Aktor Missing` (27 kar), Cakupan `aset karyawan tanpa akun yang ia wakili` (39 kar) · sumber matriks role PRD
- **DU-072-49** User (awal), Pengguna terautentikasi di client lain: Name `Bagus Setiawan {runId}` (22 kar), Peran `pengguna terautentikasi tanpa hubungan dengan client suite` (58 kar), Cakupan `client lain` (11 kar) · sumber matriks role PRD
- **DU-072-50** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset dalam sesi Audit milik Yoga, dilapor Total Control: Name `Meja Rapat Kayu {runId}` (23 kar), Asset ID `FA072-022` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Sesi Audit `milik Yoga Pratama {runId}` (26 kar) · sumber §2#b2
- **DU-072-51** Asset (awal; dimutasi TC-FA-MISS-BE-072-authz-scope-dan-pemisahan-tugas), Aset pemegang tanpa akun dengan laporan menunggu konfirmasi yang dilaporkan PIC: Name `Vacuum Cleaner Industri {runId}` (31 kar), Asset ID `FA072-023` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Sinta Maharani {runId} atas nama Budi Santoso {runId}` (90 kar), Pemegang `Budi Santoso {runId}` (20 kar), PIC `Sinta Maharani {runId}` (22 kar) · sumber §1.2#r121
- **DU-073-1** User (awal), Group Manager dengan Group binaan Head Office: Name `Maya Anggraini {runId}` (22 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-073-2** User (awal), Pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-073-3** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset layak lapor untuk uji What happened: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA073-001` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-073-4** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset dengan laporan pemegang untuk uji Reason: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA073-002` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-073-5** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset Missing untuk uji Update: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA073-003` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-073-6** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset Missing ber-TAG untuk uji Scan TAG dan Note: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA073-004` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-073-0001` (11 kar), TAG yang sudah diganti `QR-073-0003` (11 kar) · sumber PRD §4.1a Example Data
- **DU-073-7** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset Missing tanpa TAG untuk uji Found at: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA073-005` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-073-8** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset Missing yang Group-nya bukan node terbawah: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA073-006` (9 kar), Group aset `Head Office` (11 kar), Condition `Normal` (6 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-073-9** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset Missing untuk uji Asset Status Damaged: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA073-007` (9 kar), Group aset `Finance Room` (12 kar), Condition `Normal` (6 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-073-10** Asset (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Aset dengan asal Damaged + Missing: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA073-008` (9 kar), Group aset `Finance Room` (12 kar), Condition `Damaged` (7 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar), Damage record `ditahan` (7 kar) · sumber PRD §4.1a Example Data
- **DU-073-11** TAG (awal), TAG milik aset lain: TAG `QR-073-0002` (11 kar), Terpasang pada `Mesin Fotokopi Ricoh {runId}` (28 kar) · sumber turunan penulis
- **DU-073-12** TAG (awal), TAG sah milik aset Missing: TAG `QR-073-0001` (11 kar), Terpasang pada `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber turunan penulis
- **DU-073-13** TAG (awal), TAG yang tidak terdaftar pada aset mana pun: TAG `QR-073-9999` (11 kar), Terpasang pada `tidak ada` (9 kar) · sumber turunan penulis
- **DU-073-14** TAG (awal), Kode batang yang bukan TAG Tag Samurai: TAG `8991234567890` (13 kar), Terpasang pada `bukan TAG Tag Samurai` (21 kar) · sumber turunan penulis
- **DU-073-15** TAG (awal), TAG yang sudah diganti pada aset Missing: TAG `QR-073-0003` (11 kar), Terpasang pada `sudah diganti pada Laptop Dell Latitude 5420 {runId}` (52 kar) · sumber turunan penulis
- **DU-073-16** Group (awal; dimutasi TC-FA-MISS-BE-073-validasi-field), Group yang akan dihapus aktor lain sebelum Submit: Name `Lantai Tiga {runId}` (19 kar) · sumber turunan penulis
- **DU-073-17** Berkas (awal), Foto kerusakan PNG di atas 1 MB: Berkas `foto-kerusakan-073.png` (22 kar), Format `PNG` (3 kar), Ukuran `2 MB` (4 kar) · sumber turunan penulis
- **DU-073-18** Input aksi (dicoba), What happened dikosongkan: What happened `` (0 kar) · sumber turunan penulis
- **DU-073-19** Input aksi (dicoba), What happened hanya berisi spasi: What happened `   ` (3 kar) · sumber turunan penulis
- **DU-073-20** Input aksi (dibuat), What happened tepat 360 karakter: What happened `Laporan kehilangan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, guda` (360 kar) · sumber turunan penulis
- **DU-073-21** Input aksi (dicoba), What happened 361 karakter: What happened `Laporan kehilangan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (361 kar) · sumber turunan penulis
- **DU-073-22** Input aksi (dicoba), Reason dikosongkan: Reason `` (0 kar) · sumber turunan penulis
- **DU-073-23** Input aksi (dicoba), Reason hanya berisi spasi: Reason `   ` (3 kar) · sumber turunan penulis
- **DU-073-24** Input aksi (dibuat), Reason tepat 360 karakter: Reason `Alasan penolakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (360 kar) · sumber turunan penulis
- **DU-073-25** Input aksi (dicoba), Reason 361 karakter: Reason `Alasan penolakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang,` (361 kar) · sumber turunan penulis
- **DU-073-26** Input aksi (dicoba), Update dikosongkan: Update `` (0 kar) · sumber turunan penulis
- **DU-073-27** Input aksi (dicoba), Update hanya berisi spasi: Update `   ` (3 kar) · sumber turunan penulis
- **DU-073-28** Input aksi (dibuat), Update tepat 360 karakter: Update `Catatan pencarian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (360 kar) · sumber turunan penulis
- **DU-073-29** Input aksi (dicoba), Update 361 karakter: Update `Catatan pencarian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (361 kar) · sumber turunan penulis
- **DU-073-30** Input aksi (dicoba), Note dikosongkan: Note `` (0 kar) · sumber turunan penulis
- **DU-073-31** Input aksi (dicoba), Note hanya berisi spasi: Note `   ` (3 kar) · sumber turunan penulis
- **DU-073-32** Input aksi (dibuat), Note tepat 360 karakter: Note `Catatan kerusakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudan` (360 kar) · sumber turunan penulis
- **DU-073-33** Input aksi (dicoba), Note 361 karakter: Note `Catatan kerusakan. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang, dan area parkir berdasarkan catatan pemeriksaan harian. Pencarian dilakukan di ruang kerja, gudang` (361 kar) · sumber turunan penulis
- **DU-073-34** Input aksi (dibuat), Note kerusakan pendek: Note `Layar retak dan bodi penyok pada sisi kiri` (42 kar) · sumber turunan penulis
- **DU-074-1** User (awal), Pengguna Group Manager, pemindai Aktor Missing dalam cakupan Group aset: Name `Maya Anggraini {runId}` (22 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-074-2** User (awal), Pengguna Read Only: Name `Fajar Nugroho {runId}` (21 kar), Peran `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-074-3** User (awal), Pengguna pengguna terautentikasi tanpa hak Aktor Missing: Name `Agus Pratama {runId}` (20 kar), Peran `pengguna terautentikasi tanpa hak Aktor Missing dengan akses ke layar pemindai Handover, Return, Send Transfer, Receive Transfer, Disposal, Damage, Work Order, Report TAG, dan Audit` (181 kar), Cakupan `tanpa cakupan Group Missing` (27 kar) · sumber matriks role PRD
- **DU-074-4** User (awal), Pengguna Group Manager: Name `Dedi Kurnia {runId}` (19 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-074-5** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-074-6** Reader (awal), Reader tetap tanpa pengguna: Name `Gate A reader` (13 kar), Jenis `reader tetap tanpa pengguna` (27 kar) · sumber PRD §4.1a Example Data
- **DU-074-7** Setting (awal), Jendela penggabungan deteksi scan: Jendela penggabungan `1 jam per sumber pemindai` (25 kar) · sumber PRD §9.5
- **DU-074-8** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing dengan dua TAG terpasang dan belum pernah terpindai: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA074-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-074-0001 dan RFID-074-0001` (29 kar), Scan terakhir `belum pernah terpindai` (22 kar) · sumber PRD §4.1a Example Data
- **DU-074-9** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing untuk deteksi dari berbagai layar pemindai: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA074-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-074-0002` (11 kar), Scan terakhir `Gate B reader pada T0 − 3 hari, pukul 08:00` (43 kar) · sumber PRD §4.1a Example Data
- **DU-074-10** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset dengan record Reported Disposal: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA074-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Rina W` (36 kar), TAG terpasang `QR-074-0003` (11 kar) · sumber PRD §4.1a Example Data
- **DU-074-11** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing yang Last holder-nya Dedi Kurnia: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA074-004` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Dedi Kurnia {runId}` (39 kar), TAG terpasang `QR-074-0004` (11 kar), Last holder `Dedi Kurnia {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-074-12** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing di Group di luar cakupan Maya Anggraini: Name `Hand Truck Gudang {runId}` (25 kar), Asset ID `FA074-005` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-074-0005` (11 kar) · sumber PRD §4.1a Example Data
- **DU-074-13** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing yang tidak ditemukan di Audit sebelumnya: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA074-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-074-0006` (11 kar) · sumber PRD §4.1a Example Data
- **DU-074-14** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing untuk scan di layar transaksi: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA074-007` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-074-0007` (11 kar) · sumber PRD §4.1a Example Data
- **DU-074-15** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset Missing tanpa TAG: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA074-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-074-16** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset dengan laporan pemegang, Tagging Tag Reported, dan Activity Lock In Audit untuk Reject: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA074-009` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Tagging `Tag Reported` (12 kar), Activity Lock `In Audit` (8 kar), Custody `dipegang Joko Susilo {runId}` (28 kar) · sumber PRD §4.1a Example Data
- **DU-074-17** Asset (awal; dimutasi TC-FA-MISS-BE-074-deteksi-scan), Aset dengan laporan pemegang, Tagging Tag Reported, dan Activity Lock In Audit untuk Cancel Report: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA074-010` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Tagging `Tag Reported` (12 kar), Activity Lock `In Audit` (8 kar), Custody `dipegang Joko Susilo {runId}` (28 kar) · sumber PRD §4.1a Example Data
- **DU-074-18** Input aksi (dibuat), Reason Reject: Reason `Aset masih tercatat di ruang rapat` (34 kar) · sumber turunan penulis
- **DU-074-19** Sesi Audit (awal), Sesi Audit berikutnya setelah aset ditandai Not found pada sesi sebelumnya: Sesi sebelumnya `Monitor LG 27UL500 {runId} berstatus Not found` (46 kar), Sesi berikutnya `berjalan dengan pemindai Agus Pratama {runId}` (45 kar) · sumber turunan penulis
- **DU-075-1** User (awal), Pemegang yang sudah dinonaktifkan: Name `Sari Dewi {runId}` (17 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Status `dinonaktifkan` (13 kar) · sumber matriks role PRD
- **DU-075-2** Client (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Entitas khusus dengan setting Long missing after pada nilai bawaan: Name `Klien Long Missing {runId}` (26 kar), Long missing after `30 hari` (7 kar) · sumber PRD §4.1a Example Data
- **DU-075-3** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Missing satu hari sebelum mencapai batas: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA075-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing` (7 kar), Reported Date `T0 − 29 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-075-4** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Missing tepat di batas: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA075-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing` (7 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Days Missing pada evaluasi T0 + 3 `33 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-075-5** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Missing yang sudah punya node Long missing dan sudah menerima missing_long: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA075-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing` (7 kar), Reported Date `T0 − 45 hari, pukul 09:00` (25 kar), Node Long missing `sudah ada dengan Days missing 31` (32 kar), missing_long `sudah terkirim satu kali` (24 kar) · sumber PRD §4.1a Example Data
- **DU-075-6** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Reported Disposal yang sudah punya node Long missing dan sudah menerima missing_long: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA075-004` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal` (17 kar), Reported Date `T0 − 40 hari, pukul 09:00` (25 kar), Node Long missing `sudah ada dengan Days missing 35` (32 kar), missing_long `sudah terkirim satu kali` (24 kar) · sumber PRD §4.1a Example Data
- **DU-075-7** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Missing yang dilaporkan sepuluh menit sebelum pergantian tanggal: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA075-005` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing` (7 kar), Reported Date `T0 − 1 hari, pukul 23:50` (24 kar) · sumber PRD §4.1a Example Data
- **DU-075-8** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset dengan record History Found yang selesai tujuh hari setelah dilaporkan: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA075-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Found` (5 kar), Reported Date `T0 − 10 hari, pukul 09:00` (25 kar), Resolved Date `T0 − 3 hari, pukul 14:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-075-9** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset dengan record History Found yang selesai sepuluh menit setelah dilaporkan melewati pergantian tanggal: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA075-007` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Found` (5 kar), Reported Date `T0 − 5 hari, pukul 23:50` (24 kar), Resolved Date `T0 − 4 hari, pukul 00:10` (24 kar) · sumber PRD §4.1a Example Data
- **DU-075-10** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset Missing yang Last holder-nya sudah dinonaktifkan: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA075-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing` (7 kar), Reported Date `T0 − 31 hari, pukul 09:00` (25 kar), Last holder `Sari Dewi {runId}` (17 kar), Days Missing pada evaluasi T0 + 4 `35 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-075-11** Input aksi (dibuat), Reason Report Disposal: Reason `Aset tidak ditemukan setelah pencarian lebih dari 30 hari` (57 kar) · sumber turunan penulis
- **DU-075-12** Setting (dibuat), Setting Long missing after dinaikkan di atas selisih record yang sudah bertanda: Long missing after `60` (2 kar) · sumber §9.2#b55
- **DU-075-13** Setting (dibuat), Setting Long missing after diset 0 untuk menonaktifkan penanda: Long missing after `0` (1 kar) · sumber §9.2#b55
- **DU-075-14** Setting (dibuat), Setting Long missing after diturunkan sehingga record yang dilaporkan sesudah perubahan mencapai batas: Long missing after `2` (1 kar) · sumber turunan penulis
- **DU-075-15** Asset (awal; dimutasi TC-FA-MISS-BE-075-long-missing-job), Aset layak lapor yang record Missing-nya dibuat sesudah nilai setting diubah: Name `Dispenser Air Galon {runId}` (27 kar), Asset ID `FA075-009` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar) · sumber turunan penulis
- **DU-075-16** Input aksi (dibuat), What happened input aksi: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
- **DU-076-1** User (awal), Pengguna Group Manager: Name `Maya Anggraini {runId}` (22 kar), Peran `Group Manager` (13 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-076-2** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-076-3** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Sari Dewi {runId}` (17 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar), Status `dinonaktifkan` (13 kar) · sumber matriks role PRD
- **DU-076-4** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing ber-TAG dengan Condition sebelum laporan Normal: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA076-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `QR-076-0001` (11 kar), Work Order `berjalan` (8 kar) · sumber PRD §4.1a Example Data
- **DU-076-5** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset dengan laporan pemegang yang dinonaktifkan dan baris transaksi terbuka: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA076-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Sari Dewi {runId}` (54 kar), Pemegang `Sari Dewi {runId}` (17 kar), Baris transaksi `terbuka dengan badge `Reported Missing`` (39 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-076-6** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing ber-TAG yang ditemukan lewat I Can't Scan the TAG dengan Asset Status Normal: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA076-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `QR-076-0002` (11 kar) · sumber PRD §4.1a Example Data
- **DU-076-7** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing ber-TAG yang ditemukan lewat I Can't Scan the TAG dengan Asset Status Damaged: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA076-004` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `QR-076-0003` (11 kar) · sumber PRD §4.1a Example Data
- **DU-076-8** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing ber-TAG yang Report TAG-nya dibatalkan oleh scan berhasil: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA076-005` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `QR-076-0004` (11 kar) · sumber PRD §4.1a Example Data
- **DU-076-9** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing tanpa TAG yang ditemukan rusak: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA076-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-076-10** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing dengan asal Damaged + Missing dan Damage record yang ditahan: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA076-007` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Damaged` (7 kar), TAG terpasang `tidak ada` (9 kar), Damage record `berjalan dan ditahan` (20 kar), Work Order `berjalan` (8 kar) · sumber PRD §4.1a Example Data
- **DU-076-11** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset dengan laporan pemegang yang Condition sebelum laporannya Damaged untuk Reject: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA076-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Transaksi pemegang `Borrow` (6 kar), Baris transaksi `terbuka dengan badge `Reported Missing`` (39 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `berjalan dan ditahan` (20 kar), Tagging `Tag Reported` (12 kar), Activity Lock `In Audit` (8 kar) · sumber PRD §4.1a Example Data
- **DU-076-12** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset dengan laporan pemegang yang Condition sebelum laporannya Damaged untuk Cancel Report: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA076-009` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Transaksi pemegang `Borrow` (6 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `berjalan dan ditahan` (20 kar) · sumber PRD §4.1a Example Data
- **DU-076-13** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset dengan laporan pemegang yang Condition tersimpannya tidak lagi dapat dipulihkan: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA076-010` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Condition sebelum laporan `Damaged, tidak lagi dapat dipulihkan` (36 kar) · sumber PRD §4.1a Example Data
- **DU-076-14** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset dengan laporan pemegang yang akan di-Confirm: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA076-011` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Condition sebelum laporan `Normal` (6 kar) · sumber PRD §4.1a Example Data
- **DU-076-15** Asset (awal; dimutasi TC-FA-MISS-BE-076-mark-as-found-efek), Aset Missing untuk uji kelayakan transaksi baru dan opsi Found at: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA076-012` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Condition sebelum laporan `Normal` (6 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-076-16** Berkas (awal), Foto kerusakan PNG: Berkas `foto-kerusakan-076.png` (22 kar), Format `PNG` (3 kar), Ukuran `800 KB` (6 kar) · sumber turunan penulis
- **DU-076-17** Input aksi (dibuat), Note kerusakan: Note `Layar retak dan bodi penyok pada sisi kiri` (42 kar) · sumber turunan penulis
- **DU-076-18** Input aksi (dibuat), Reason Reject: Reason `Aset terlihat di ruang kerja pemegang` (37 kar) · sumber turunan penulis
- **DU-076-19** Input aksi (dibuat), Reason Reject kedua: Reason `Aset masih tercatat di gudang cabang` (36 kar) · sumber turunan penulis
- **DU-077-1** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-077-2** User (awal), Pengguna pengguna terautentikasi tanpa hak Aktor Missing: Name `Agus Pratama {runId}` (20 kar), Peran `pengguna terautentikasi tanpa hak Aktor Missing` (47 kar), Cakupan `tanpa cakupan Group` (19 kar) · sumber matriks role PRD
- **DU-077-3** User (awal), Pengguna pengguna terautentikasi tanpa hak Aktor Missing: Name `Budi Hartono {runId}` (20 kar), Peran `pengguna terautentikasi tanpa hak Aktor Missing` (47 kar), Cakupan `tanpa cakupan Group` (19 kar) · sumber matriks role PRD
- **DU-077-4** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset layak lapor pertama dalam laporan banyak aset: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA077-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-077-5** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset layak lapor kedua dalam laporan banyak aset: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA077-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-077-6** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset yang sudah punya record berjalan dan dilewati: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA077-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-077-7** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Record pembanding yang tidak terlibat dalam aksi mana pun: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA077-004` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-077-8** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset yang dipegang Joko Susilo untuk laporan pemegang lalu Confirm: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA077-005` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-077-9** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan laporan pemegang untuk Reject: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA077-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Transaksi pemegang `Borrow` (6 kar) · sumber PRD §4.1a Example Data
- **DU-077-10** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan laporan pemegang untuk Cancel Report: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA077-007` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar), Transaksi pemegang `Borrow` (6 kar) · sumber PRD §4.1a Example Data
- **DU-077-11** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing untuk Add Update: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA077-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-077-12** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing untuk Mark as Found: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA077-009` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-077-13** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing untuk Report Disposal, Decline, dan Cancel Disposal Report: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA077-010` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-077-14** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset In Disposal Process yang akan Disposal Executed: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA077-011` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `In Disposal Process, dilaporkan Rina W` (38 kar) · sumber PRD §4.1a Example Data
- **DU-077-15** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset In Disposal Process yang baris Disposalnya akan Rejected: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA077-012` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `In Disposal Process, dilaporkan Rina W` (38 kar) · sumber PRD §4.1a Example Data
- **DU-077-16** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan Disposal Report Reported tanpa record Missing: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA077-013` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Disposal Report `Reported` (8 kar) · sumber PRD §4.1a Example Data
- **DU-077-17** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan baris Disposal Sell berstatus Waiting for Approval tanpa record Missing: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA077-014` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Baris Disposal `Sell, Waiting for Approval` (26 kar) · sumber PRD §4.1a Example Data
- **DU-077-18** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan laporan pemegang yang dilewati Bulk Report Disposal: Name `Meja Rapat Kayu {runId}` (23 kar), Asset ID `FA077-018` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-077-19** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing ber-TAG untuk deteksi scan: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA077-015` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-077-0001` (11 kar) · sumber PRD §4.1a Example Data
- **DU-077-20** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing yang dilaporkan T0 − 30 hari untuk job Long missing: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA077-016` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-077-21** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset Missing untuk I found it: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA077-017` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar), TAG terpasang `QR-077-0002` (11 kar) · sumber PRD §4.1a Example Data
- **DU-077-22** Berkas (awal), Foto penemuan JPG: Berkas `foto-penemuan-077.jpg` (21 kar), Format `JPG` (3 kar), Ukuran `600 KB` (6 kar) · sumber turunan penulis
- **DU-077-23** Lokasi (awal), Lokasi GPS perangkat penemu: Latitude `-6.200000` (9 kar), Longitude `106.816667` (10 kar) · sumber turunan penulis
- **DU-077-24** Input aksi (dibuat), What happened input aksi: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
- **DU-077-25** Input aksi (dibuat), Update input aksi: Update `Pencarian di gudang lantai satu belum membuahkan hasil` (54 kar) · sumber turunan penulis
- **DU-077-26** Input aksi (dibuat), Reason input aksi: Reason `Aset terlihat di ruang kerja pemegang` (37 kar) · sumber turunan penulis
- **DU-077-27** Input aksi (dibuat), Reason Disposal input aksi: Reason Disposal `Aset tidak ditemukan setelah pencarian dua pekan` (48 kar) · sumber turunan penulis
- **DU-077-28** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan Report Disposal yang akan di-Submit Request: Name `Lemari Arsip Besi {runId}` (25 kar), Asset ID `FA077-019` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Rina W` (36 kar) · sumber turunan penulis
- **DU-077-29** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan baris Disposal yang akan dibatalkan pembuatnya: Name `Kipas Angin Standing {runId}` (28 kar), Asset ID `FA077-020` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `In Disposal Process, dilaporkan Rina W` (38 kar) · sumber turunan penulis
- **DU-077-30** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan baris Disposal yang akan dihapus dari daftar Disposal: Name `Mesin Fotokopi Ricoh {runId}` (28 kar), Asset ID `FA077-021` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `In Disposal Process, dilaporkan Rina W` (38 kar) · sumber turunan penulis
- **DU-077-31** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dengan baris Disposal yang akan melewati Transaction timeout: Name `Mesin Cuci Industri {runId}` (27 kar), Asset ID `FA077-022` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `In Disposal Process, dilaporkan Rina W` (38 kar) · sumber turunan penulis
- **DU-077-32** Laporan Disposal (dibuat), Jenis disposal Write-off: Jenis `Write-off` (9 kar) · sumber turunan penulis
- **DU-077-36** User (awal), Staff Auditor tanpa hak Aktor Missing: Name `Sabrina Putri {runId}` (21 kar), Peran `Staff Auditor tanpa hak Aktor Missing` (37 kar), Cakupan `aset dalam sesinya sendiri` (26 kar) · sumber matriks role PRD
- **DU-077-37** Sesi Audit (awal), Sesi Audit milik Sabrina: Name `Audit Gudang {runId}` (20 kar), Pemilik `Sabrina Putri {runId}` (21 kar), Aset `Kabinet Server {runId}, Meja Resepsionis {runId}` (48 kar) · sumber §1.2#r72
- **DU-077-38** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dalam sesi Audit, dilapor lalu dibatalkan Staff Auditor: Name `Kabinet Server {runId}` (22 kar), Asset ID `FA077-023` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Sesi Audit `Audit Gudang {runId}` (20 kar) · sumber §1.2#r72
- **DU-077-39** Asset (awal; dimutasi TC-FA-MISS-BE-077-log-dan-notifikasi), Aset dalam sesi Audit, dilapor Total Control: Name `Meja Resepsionis {runId}` (24 kar), Asset ID `FA077-024` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Sesi Audit `Audit Gudang {runId}` (20 kar) · sumber §8.2#p21
- **DU-078-1** User (awal), Pengguna View asset value: Name `Hari Susanto {runId}` (20 kar), Peran `View asset value` (16 kar), Cakupan `Group Head Office beserta descendant` (36 kar) · sumber matriks role PRD
- **DU-078-2** User (awal), Pengguna PIC yang melapor atas nama karyawan tanpa akun: Name `Rudi Hartono {runId}` (20 kar), Peran `PIC yang melapor atas nama karyawan tanpa akun` (46 kar), Cakupan `aset karyawan yang ia wakili` (28 kar) · sumber matriks role PRD
- **DU-078-3** User (awal), Pengguna karyawan tanpa akun: Name `Joko Susilo {runId}` (19 kar), Peran `karyawan tanpa akun` (19 kar), Cakupan `tanpa akses` (11 kar) · sumber matriks role PRD
- **DU-078-4** User (awal), Pengguna karyawan tanpa akun: Name `Budi Santoso {runId}` (20 kar), Peran `karyawan tanpa akun` (19 kar), Cakupan `tanpa akses` (11 kar) · sumber matriks role PRD
- **DU-078-5** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Sari Dewi {runId}` (17 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-078-6** User (awal), Pengguna pengguna terautentikasi tanpa hak Aktor Missing: Name `Agus Pratama {runId}` (20 kar), Peran `pengguna terautentikasi tanpa hak Aktor Missing` (47 kar), Cakupan `tanpa cakupan Group` (19 kar) · sumber matriks role PRD
- **DU-078-7** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Missing dengan TAG NFC dan nilai finansial terisi: Name `Camera Canon EOS {runId}` (24 kar), Increment `1` (1 kar), Name tampil `Camera Canon EOS {runId} - 1` (28 kar), Asset ID `FA078-001` (9 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), TAG `NFC` (3 kar), Last Holder `Budi Santoso {runId}` (20 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 5 hari, pukul 09:00` (24 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `9800000` (7 kar) · sumber PRD §4.1a Example Data
- **DU-078-8** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Missing dengan dua ikon TAG NFC dan QR: Name `Drill Bosch GSB {runId}` (23 kar), Increment `1` (1 kar), Name tampil `Drill Bosch GSB {runId} - 1` (27 kar), Asset ID `FA078-002` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `NFC, QR` (7 kar), Last Holder `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 12 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-078-9** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Reported Disposal dengan TAG QR: Name `Hand Pallet Truck {runId}` (25 kar), Increment `1` (1 kar), Name tampil `Hand Pallet Truck {runId} - 1` (29 kar), Asset ID `FA078-003` (9 kar), Status `Reported Disposal` (17 kar), Source `Transfer` (8 kar), TAG `QR` (2 kar), Last Holder `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 40 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-078-10** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record In Disposal Process tanpa TAG: Name `Hand Pallet Truck {runId}` (25 kar), Increment `2` (1 kar), Name tampil `Hand Pallet Truck {runId} - 2` (29 kar), Asset ID `FA078-004` (9 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Last Holder `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 20 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-078-11** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Missing laporan PIC atas nama karyawan tanpa akun dengan penanda Long missing: Name `Hand Pallet Truck {runId}` (25 kar), Increment `10` (2 kar), Name tampil `Hand Pallet Truck {runId} - 10` (30 kar), Asset ID `FA078-005` (9 kar), Status `Missing` (7 kar), Source `Borrow` (6 kar), TAG `RFID` (4 kar), Last Holder `Joko Susilo {runId}` (19 kar), Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})` (55 kar), Reported Date `T0 − 45 hari, pukul 09:00` (25 kar), Penanda `Long missing` (12 kar) · sumber PRD §4.1a Example Data
- **DU-078-12** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Waiting for Confirmation dengan TAG BLE: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Increment `1` (1 kar), Name tampil `Laptop Dell Latitude 5420 {runId} - 1` (37 kar), Asset ID `FA078-006` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), TAG `BLE` (3 kar), Last Holder `Sari Dewi {runId}` (17 kar), Reported By `Sari Dewi {runId}` (17 kar), Reported Date `T0 − 2 hari, pukul 09:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-078-13** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record Missing dengan TAG GPS: Name `Monitor LG 27UL500 {runId}` (26 kar), Increment `1` (1 kar), Name tampil `Monitor LG 27UL500 {runId} - 1` (30 kar), Asset ID `FA078-007` (9 kar), Status `Missing` (7 kar), Source `Audit` (5 kar), TAG `GPS` (3 kar), Last Holder `tidak ada` (9 kar), Reported By `Agus Pratama {runId}` (20 kar), Reported Date `T0 − 8 hari, pukul 09:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-078-14** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record dengan tanda persen literal pada nama: Name `Rak Gudang Timur 50% {runId}` (28 kar), Increment `1` (1 kar), Name tampil `Rak Gudang Timur 50% {runId} - 1` (32 kar), Asset ID `FA078-008` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Last Holder `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 6 hari, pukul 09:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-078-15** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record pengecoh yang cocok bila tanda persen dianggap wildcard: Name `Rak Gudang Timur 5001 {runId}` (29 kar), Increment `1` (1 kar), Name tampil `Rak Gudang Timur 5001 {runId} - 1` (33 kar), Asset ID `FA078-009` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Last Holder `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 7 hari, pukul 09:00` (24 kar) · sumber PRD §4.1a Example Data
- **DU-078-16** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record History Found dengan Duration 10 hari: Name `Projector Epson EB-X06 {runId}` (30 kar), Increment `1` (1 kar), Name tampil `Projector Epson EB-X06 {runId} - 1` (34 kar), Asset ID `FA078-011` (9 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), TAG `NFC` (3 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 20 hari, pukul 09:00` (25 kar), Duration `10 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-078-17** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record History Disposed dengan Source yang hanya ada di History: Name `Printer HP LaserJet M404 {runId}` (32 kar), Increment `1` (1 kar), Name tampil `Printer HP LaserJet M404 {runId} - 1` (36 kar), Asset ID `FA078-012` (9 kar), Status `Disposed` (8 kar), Source `Reconciliation` (14 kar), TAG `NFC, QR` (7 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 90 hari, pukul 09:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 10 hari, pukul 09:00` (25 kar), Duration `80 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-078-18** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record History Rejected dengan Duration 1 hari: Name `Toyota Innova {runId}` (21 kar), Increment `1` (1 kar), Name tampil `Toyota Innova {runId} - 1` (25 kar), Asset ID `FA078-013` (9 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), TAG `QR` (2 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 7 hari, pukul 09:00` (24 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 6 hari, pukul 09:00` (24 kar), Duration `1 day` (5 kar) · sumber PRD §4.1a Example Data
- **DU-078-19** Asset (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record History Canceled dengan Duration 3 hari: Name `Kamera Sony A7 {runId}` (22 kar), Increment `1` (1 kar), Name tampil `Kamera Sony A7 {runId} - 1` (26 kar), Asset ID `FA078-014` (9 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), TAG `tidak ada` (9 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 10 hari, pukul 09:00` (25 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 7 hari, pukul 09:00` (24 kar), Duration `3 days` (6 kar) · sumber PRD §4.1a Example Data
- **DU-078-20** Missing record (awal; dimutasi TC-FA-MISS-BE-078-search-sort-filter), Record History Canceled yang diselesaikan PIC atas nama karyawan tanpa akun: Name `Vacuum Cleaner Industri {runId}` (31 kar), Increment `1` (1 kar), Name tampil `Vacuum Cleaner Industri {runId} - 1` (35 kar), Asset ID `FA078-015` (9 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), TAG `RFID` (4 kar), Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})` (55 kar), Reported Date `T0 − 200 hari, pukul 09:00` (26 kar), Resolved By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})` (55 kar), Resolved Date `T0 − 100 hari, pukul 09:00` (26 kar), Duration `100 days` (8 kar) · sumber turunan penulis
- **DU-079-1** User (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Aktor Missing dengan Setup Column sendiri: Name `Hendra Pratama {runId}` (22 kar), Peran `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-079-2** User (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Pemegang View asset value: Name `Hari Susanto {runId}` (20 kar), Peran `View asset value` (16 kar), Cakupan `Group Head Office beserta descendant` (36 kar) · sumber matriks role PRD
- **DU-079-3** User (awal), Karyawan tanpa akun sebagai Last holder: Name `Budi Santoso {runId}` (20 kar), Peran `karyawan tanpa akun` (19 kar) · sumber matriks role PRD
- **DU-079-4** User (awal), Pemegang yang melapor sendiri: Name `Sari Dewi {runId}` (17 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar) · sumber matriks role PRD
- **DU-079-5** User (awal), PIC yang melapor atas nama karyawan: Name `Rudi Hartono {runId}` (20 kar), Peran `PIC` (3 kar) · sumber matriks role PRD
- **DU-079-6** User (awal), Karyawan tanpa akun yang diwakili PIC: Name `Joko Susilo {runId}` (19 kar), Peran `karyawan tanpa akun` (19 kar) · sumber matriks role PRD
- **DU-079-7** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing dengan dua ikon TAG, Brand dan Model flat, serta hierarki Group dan Category: Name `Camera Canon EOS Berkas {runId}` (31 kar), Asset ID `FA079-001` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `NFC, QR` (7 kar), Brand `Canon` (5 kar), Model/Type `EOS R6` (6 kar), Group `Head Office > Finance Room` (26 kar), Category `Elektronik > Kamera` (19 kar), Last Holder `Budi Santoso {runId}` (20 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 5 hari, pukul 09:00` (24 kar), Purchase Cost `12500000` (8 kar), Last Seen `Gate A reader pada T0 − 3 hari, pukul 09:00` (43 kar) · sumber PRD §4.1a Example Data
- **DU-079-8** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Waiting for Confirmation dengan nama ber-koma dan nilai kosong: Name `Printer, Laser HP M404 Berkas {runId}` (37 kar), Asset ID `FA079-002` (9 kar), Status `Waiting for Confirmation` (24 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Brand `tidak ada` (9 kar), Model/Type `tidak ada` (9 kar), Group `Head Office > Finance Room` (26 kar), Category `Elektronik > Printer` (20 kar), Last Holder `Sari Dewi {runId}` (17 kar), Reported By `Sari Dewi {runId}` (17 kar), Reported Date `T0 − 3 hari, pukul 09:00` (24 kar), Purchase Cost `tidak ada` (9 kar), Last Seen `tidak ada TAG` (13 kar) · sumber PRD §4.1a Example Data
- **DU-079-9** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing dengan nama ber-kutip ganda: Name `Monitor 27" LG Berkas {runId}` (29 kar), Asset ID `FA079-003` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `QR` (2 kar), Brand `LG` (2 kar), Model/Type `27UL500` (7 kar), Group `Head Office > Finance Room` (26 kar), Category `Elektronik > Monitor` (20 kar), Last Holder `tidak ada` (9 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 9 hari, pukul 09:00` (24 kar), Purchase Cost `4500000` (7 kar) · sumber PRD §4.1a Example Data
- **DU-079-10** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing dengan karakter non-ASCII pada nama: Name `Café Élan Rak Berkas {runId}` (28 kar), Asset ID `FA079-004` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `RFID` (4 kar), Brand `tidak ada` (9 kar), Model/Type `tidak ada` (9 kar), Group `Head Office > Server Room` (25 kar), Category `Furnitur > Rak` (14 kar), Last Holder `tidak ada` (9 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 14 hari, pukul 09:00` (25 kar), Purchase Cost `1750000` (7 kar) · sumber PRD §4.1a Example Data
- **DU-079-11** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing laporan PIC atas nama karyawan tanpa akun: Name `Hand Pallet Truck Berkas {runId}` (32 kar), Asset ID `FA079-005` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `BLE` (3 kar), Brand `tidak ada` (9 kar), Model/Type `tidak ada` (9 kar), Group `Warehouse` (9 kar), Category `Alat Angkut > Troli` (19 kar), Last Holder `Joko Susilo {runId}` (19 kar), Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})` (55 kar), Reported Date `T0 − 31 hari, pukul 09:00` (25 kar), Purchase Cost `2300000` (7 kar) · sumber PRD §4.1a Example Data
- **DU-079-12** Asset (awal; 5001 record; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing volume di atas ambang unduhan: Name `Gudang Cabang {n} Volume {runId}` (32 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), Group `Head Office > Finance Room` (26 kar) · sumber PRD §4.1a Example Data
- **DU-079-13** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record History Found: Name `Projector Epson EB-X06 Berkas {runId}` (37 kar), Asset ID `FA079-011` (9 kar), Status `Found` (5 kar), Source `Borrow` (6 kar), TAG `NFC` (3 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar), Resolved By `Hendra Pratama {runId}` (22 kar), Resolved Date `T0 − 20 hari, pukul 09:00` (25 kar), Duration `10 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-079-14** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record History Disposed oleh System: Name `Toyota Innova Berkas {runId}` (28 kar), Asset ID `FA079-012` (9 kar), Status `Disposed` (8 kar), Source `Manual` (6 kar), TAG `NFC` (3 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 90 hari, pukul 09:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 10 hari, pukul 09:00` (25 kar), Duration `80 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-079-15** Input aksi (dibuat), Kata kunci Search aktif: Search `Berkas {runId}` (14 kar) · sumber turunan penulis
- **DU-079-16** Input aksi (dibuat), Kata kunci Search volume: Search `Volume {runId}` (14 kar) · sumber turunan penulis
- **DU-079-17** Input aksi (dicoba), Kata kunci tanpa hasil: Search `zzq-079-tidak-ada` (17 kar) · sumber turunan penulis
- **DU-079-18** Asset (awal; dimutasi TC-FA-MISS-BE-079-download-isi-berkas), Record Missing dengan tiga label pada kolom badge ber-item banyak: Name `Genset Honda EU22 Multilabel {runId}` (36 kar), Asset ID `FA079-018` (9 kar), Status `Missing` (7 kar), Source `Manual` (6 kar), TAG `NFC` (3 kar), Labels `Aset Kritis, Garansi Aktif, Pinjaman Cabang` (43 kar), Brand `Honda` (5 kar), Model/Type `EU22i` (5 kar), Group `Head Office > Server Room` (25 kar), Category `Elektronik > Genset` (19 kar), Last Holder `tidak ada` (9 kar), Reported By `Hendra Pratama {runId}` (22 kar), Reported Date `T0 − 2 hari, pukul 09:00` (24 kar), Purchase Cost `18500000` (8 kar) · sumber PRD §9.17 / prd-conventions §9.9 (multi-badge dipisah ", ")
- **DU-080-1** Client (awal), Client aktif pada plan Professional dengan level Disposal Full: Name `Klien Aktif Uji {runId}` (23 kar), Plan `Professional` (12 kar), Status `Active` (6 kar) · sumber PRD §9.10
- **DU-080-2** Client (awal), Client Suspended: Name `Klien Suspended Uji {runId}` (27 kar), Plan `Professional` (12 kar), Status `Suspended` (9 kar) · sumber PRD §9.10
- **DU-080-3** Client (awal), Client Expired dengan record pemicu job sistem: Name `Klien Expired Uji {runId}` (25 kar), Plan `Professional` (12 kar), Status `Expired` (7 kar) · sumber PRD §9.10
- **DU-080-4** Client (awal), Client aktif pada plan Starter dengan level Disposal None: Name `Klien Starter Uji {runId}` (25 kar), Plan `Starter` (7 kar), Status `Active` (6 kar) · sumber PRD §9.10
- **DU-080-5** Client (awal), Client aktif pada plan Growth dengan level Disposal Full: Name `Klien Growth Uji {runId}` (24 kar), Plan `Growth` (6 kar), Status `Active` (6 kar) · sumber PRD §9.10
- **DU-080-6** User (awal), Pengguna Total Control di Klien Aktif Uji: Name `Gunawan Setiadi {runId}` (23 kar), Peran `Total Control` (13 kar), Client `Klien Aktif Uji {runId}` (23 kar) · sumber matriks role PRD
- **DU-080-7** User (awal), Pengguna Total Control di Klien Suspended Uji: Name `Maria Kusuma {runId}` (20 kar), Peran `Total Control` (13 kar), Client `Klien Suspended Uji {runId}` (27 kar) · sumber matriks role PRD
- **DU-080-8** User (awal), Pengguna Total Control di Klien Expired Uji: Name `Nugroho Aditya {runId}` (22 kar), Peran `Total Control` (13 kar), Client `Klien Expired Uji {runId}` (25 kar) · sumber matriks role PRD
- **DU-080-9** User (awal), Pengguna Total Control di Klien Starter Uji: Name `Putri Handayani {runId}` (23 kar), Peran `Total Control` (13 kar), Client `Klien Starter Uji {runId}` (25 kar) · sumber matriks role PRD
- **DU-080-10** User (awal), Pengguna Total Control di Klien Growth Uji: Name `Rahmat Hidayat {runId}` (22 kar), Peran `Total Control` (13 kar), Client `Klien Growth Uji {runId}` (24 kar) · sumber matriks role PRD
- **DU-080-11** User (awal), Pengguna pemegang tanpa hak Aktor Missing di Klien Suspended Uji: Name `Slamet Riyadi {runId}` (21 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Client `Klien Suspended Uji {runId}` (27 kar) · sumber matriks role PRD
- **DU-080-12** User (awal), Pengguna pemegang tanpa hak Aktor Missing di Klien Expired Uji: Name `Tono Wijaya {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Client `Klien Expired Uji {runId}` (25 kar) · sumber matriks role PRD
- **DU-080-13** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset layak lapor di Klien Suspended Uji: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA080-101` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-14** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset dengan laporan pemegang di Klien Suspended Uji: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA080-102` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Waiting for Confirmation, dilaporkan Slamet Riyadi {runId}` (58 kar), Pemegang `Slamet Riyadi {runId}` (21 kar) · sumber PRD §4.1a Example Data
- **DU-080-15** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing untuk Add Update, Mark as Found, dan Report Disposal di Klien Suspended Uji: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA080-103` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-16** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Reported Disposal di Klien Suspended Uji: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA080-104` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Reported Disposal, dilaporkan admin client` (42 kar) · sumber PRD §4.1a Example Data
- **DU-080-17** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing kedua untuk Bulk Report Disposal di Klien Suspended Uji: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA080-105` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-18** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing yang dilaporkan T0 − 30 hari untuk job Long missing di Klien Suspended Uji: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA080-106` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-080-19** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing ber-TAG untuk deteksi scan di Klien Suspended Uji: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA080-107` (9 kar), Client `Klien Suspended Uji {runId}` (27 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `QR-080-107` (10 kar) · sumber PRD §4.1a Example Data
- **DU-080-20** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset layak lapor di Klien Expired Uji: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA080-201` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-21** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset dengan laporan pemegang di Klien Expired Uji: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA080-202` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Waiting for Confirmation, dilaporkan Tono Wijaya {runId}` (56 kar), Pemegang `Tono Wijaya {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-080-22** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing untuk Add Update, Mark as Found, dan Report Disposal di Klien Expired Uji: Name `Mesin Fotokopi Ricoh {runId}` (28 kar), Asset ID `FA080-203` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-23** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Reported Disposal di Klien Expired Uji: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA080-204` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Reported Disposal, dilaporkan admin client` (42 kar) · sumber PRD §4.1a Example Data
- **DU-080-24** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing kedua untuk Bulk Report Disposal di Klien Expired Uji: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA080-205` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-25** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing yang dilaporkan T0 − 30 hari untuk job Long missing di Klien Expired Uji: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA080-206` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Reported Date `T0 − 30 hari, pukul 09:00` (25 kar) · sumber PRD §4.1a Example Data
- **DU-080-26** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing ber-TAG untuk deteksi scan di Klien Expired Uji: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA080-207` (9 kar), Client `Klien Expired Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `QR-080-207` (10 kar) · sumber PRD §4.1a Example Data
- **DU-080-27** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di client aktif untuk Add Update dan Report Disposal: Name `Laptop Lenovo ThinkPad T14 {runId}` (34 kar), Asset ID `FA080-301` (9 kar), Client `Klien Aktif Uji {runId}` (23 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-28** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing kedua di client aktif untuk Report Disposal: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA080-302` (9 kar), Client `Klien Aktif Uji {runId}` (23 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-29** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset layak lapor di Starter: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA080-401` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-30** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset dengan laporan pemegang di Starter: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA080-402` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Waiting for Confirmation, dilaporkan admin client` (49 kar) · sumber PRD §4.1a Example Data
- **DU-080-31** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Starter untuk Add Update: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA080-403` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-32** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Starter untuk Mark as Found: Name `Lemari Arsip Besi {runId}` (25 kar), Asset ID `FA080-404` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `tidak ada` (9 kar) · sumber PRD §4.1a Example Data
- **DU-080-33** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Starter untuk Report Disposal: Name `Kipas Angin Standing {runId}` (28 kar), Asset ID `FA080-405` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-34** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing kedua di Starter untuk Bulk Report Disposal: Name `Dispenser Air Galon {runId}` (27 kar), Asset ID `FA080-406` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-35** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Reported Disposal sisa dari plan sebelumnya di Starter: Name `Genset Mini Yamaha {runId}` (26 kar), Asset ID `FA080-407` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Reported Disposal, dilaporkan admin client` (42 kar) · sumber PRD §4.1a Example Data
- **DU-080-36** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Starter dengan TAG QR dan RFID: Name `Router Mikrotik RB750 {runId}` (29 kar), Asset ID `FA080-408` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `QR-080-0408 dan RFID-080-0408` (29 kar) · sumber PRD §4.1a Example Data
- **DU-080-37** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Starter dengan TAG RFID saja: Name `Switch Cisco SG350 {runId}` (26 kar), Asset ID `FA080-409` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), TAG terpasang `RFID-080-0409` (13 kar) · sumber PRD §4.1a Example Data
- **DU-080-38** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Growth untuk Report Disposal: Name `Stabilizer Lampu Studio {runId}` (31 kar), Asset ID `FA080-501` (9 kar), Client `Klien Growth Uji {runId}` (24 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-39** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di Growth untuk Bulk Report Disposal: Name `Lampu Sorot Panggung {runId}` (28 kar), Asset ID `FA080-502` (9 kar), Client `Klien Growth Uji {runId}` (24 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-40** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing kedua di Growth untuk Bulk Report Disposal: Name `Speaker Aktif Yamaha {runId}` (28 kar), Asset ID `FA080-503` (9 kar), Client `Klien Growth Uji {runId}` (24 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar) · sumber PRD §4.1a Example Data
- **DU-080-41** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Reported Disposal di Growth untuk Cancel Disposal Report: Name `Mixer Audio Behringer {runId}` (29 kar), Asset ID `FA080-504` (9 kar), Client `Klien Growth Uji {runId}` (24 kar), Record berjalan `Reported Disposal, dilaporkan admin client` (42 kar) · sumber PRD §4.1a Example Data
- **DU-080-42** Input aksi (dibuat), What happened input aksi: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
- **DU-080-43** Input aksi (dibuat), Reason input aksi: Reason `Aset masih dipakai di meja pemegang` (35 kar) · sumber turunan penulis
- **DU-080-44** Input aksi (dibuat), Update input aksi: Update `Pencarian di gudang lantai satu belum membuahkan hasil` (54 kar) · sumber turunan penulis
- **DU-080-45** Input aksi (dibuat), Reason Disposal input aksi: Reason Disposal `Aset tidak ditemukan setelah pencarian dua pekan` (48 kar) · sumber turunan penulis
- **DU-080-46** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset di client Starter dengan laporan pemegang yang akan di-Reject: Name `Meja Lipat Aluminium {runId}` (28 kar), Asset ID `FA080-410` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Waiting for Confirmation, dilaporkan Wawan Setiawan {runId}` (59 kar), Pemegang `Wawan Setiawan {runId}` (22 kar) · sumber turunan penulis
- **DU-080-47** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset di client Starter dengan laporan pemegang yang akan dibatalkan pemegangnya: Name `Kursi Lipat Besi {runId}` (24 kar), Asset ID `FA080-411` (9 kar), Client `Klien Starter Uji {runId}` (25 kar), Record berjalan `Waiting for Confirmation, dilaporkan Wawan Setiawan {runId}` (59 kar), Pemegang `Wawan Setiawan {runId}` (22 kar) · sumber turunan penulis
- **DU-080-48** User (awal), Pemegang tanpa hak Aktor Missing di client Starter: Name `Wawan Setiawan {runId}` (22 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Client `Klien Starter Uji {runId}` (25 kar) · sumber matriks role PRD
- **DU-080-49** Client (awal), Client dengan Storage penuh (tanpa baris ledger Storage, berkuota 0): Name `Klien Storage Penuh Uji {runId}` (31 kar), Plan `Professional` (12 kar), Status `Active` (6 kar), Storage `client tanpa baris ledger Storage, dianggap berkuota 0` (54 kar) · sumber §1.2#r126
- **DU-080-50** User (awal), Total Control di client Storage penuh: Name `Dian Pratiwi {runId}` (20 kar), Peran `Total Control` (13 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar) · sumber matriks role PRD
- **DU-080-51** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing, Mark as Found Normal dengan Photo baru: Name `Meja Arsip Jati {runId}` (23 kar), Asset ID `FA080-601` (9 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Condition `Normal` (6 kar), TAG terpasang `tidak ada` (9 kar) · sumber §9.10#p1
- **DU-080-52** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing, Mark as Found Normal tanpa Photo: Name `Lemari Besi Arsip {runId}` (25 kar), Asset ID `FA080-602` (9 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Condition `Normal` (6 kar), TAG terpasang `tidak ada` (9 kar) · sumber §9.10#p1
- **DU-080-53** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing, Mark as Found Damaged dengan Damaged Photo baru: Name `Rak Buku Jati {runId}` (21 kar), Asset ID `FA080-603` (9 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Condition `Normal` (6 kar), TAG terpasang `tidak ada` (9 kar) · sumber §9.10#p1
- **DU-080-54** Berkas (dibuat), Foto penemuan baru yang diunggah: Berkas `foto-penemuan-080.jpg` (21 kar), Format `JPG` (3 kar), Ukuran `600 KB` (6 kar) · sumber turunan penulis
- **DU-080-55** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset Missing di client Storage penuh untuk I found it dengan Photo baru: Name `Kursi Tamu Jati {runId}` (23 kar), Asset ID `FA080-604` (9 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Condition `Normal` (6 kar), TAG `tidak ada` (9 kar) · sumber §9.4.4#r27
- **DU-080-56** Berkas (dibuat), Berkas berformat tidak diterima untuk Photo / Damaged Photo: Berkas `dokumen-080.pdf` (15 kar), Format `PDF (tidak diterima)` (20 kar), Ukuran `200 KB` (6 kar) · sumber §9.4.2#r34
- **DU-080-57** Asset (awal; dimutasi TC-FA-MISS-BE-080-state-tenant-dan-plan), Aset asal Damaged + Missing di client Storage penuh: Name `Panel Surya Mini {runId}` (24 kar), Asset ID `FA080-605` (9 kar), Client `Klien Storage Penuh Uji {runId}` (31 kar), Record berjalan `Missing, dilaporkan admin client` (32 kar), Condition sebelum laporan `Damaged` (7 kar), Damage record `berjalan dan ditahan` (20 kar), TAG terpasang `tidak ada` (9 kar) · sumber §9.4.2#r34
- **DU-081-1** User (awal), Pengguna Group Manager dan Aktor Disposal: Name `Maya Anggraini {runId}` (22 kar), Peran `Group Manager dan Aktor Disposal` (32 kar), Cakupan `Group Head Office beserta sub-group` (35 kar) · sumber matriks role PRD
- **DU-081-2** User (awal), Pengguna Manage asset & TAG dengan Update pada Head Office: Name `Dewi Anindita {runId}` (21 kar), Peran `Manage asset & TAG dengan Update pada Head Office` (49 kar), Cakupan `Head Office beserta descendant` (30 kar) · sumber matriks role PRD
- **DU-081-3** User (awal), Pengguna Accounting dengan Manage accounting Read dan Update: Name `Eko Wibowo {runId}` (18 kar), Peran `Accounting dengan Manage accounting Read dan Update` (51 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-081-4** User (awal), Pengguna Read Only: Name `Fajar Nugroho {runId}` (21 kar), Peran `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-081-5** User (awal), Pengguna pemegang tanpa hak Aktor Missing: Name `Joko Susilo {runId}` (19 kar), Peran `pemegang tanpa hak Aktor Missing` (32 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-081-6** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing pertama untuk Bulk Report Disposal penuh: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Asset ID `FA081-001` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-7** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing kedua untuk Bulk Report Disposal penuh: Name `Hand Pallet Truck {runId}` (25 kar), Asset ID `FA081-002` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-8** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing ketiga untuk Bulk Report Disposal penuh: Name `Projector Epson EB-X06 {runId}` (30 kar), Asset ID `FA081-003` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-9** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing yang layak diproses dalam seleksi campuran: Name `Camera Canon EOS {runId}` (24 kar), Asset ID `FA081-004` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-10** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan laporan pemegang yang dilewati karena bukan Missing: Name `Printer HP LaserJet M404 {runId}` (32 kar), Asset ID `FA081-005` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-081-11** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing yang Last holder-nya Maya Anggraini: Name `Monitor LG 27UL500 {runId}` (26 kar), Asset ID `FA081-006` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Maya Anggraini {runId}` (42 kar), Last holder `Maya Anggraini {runId}` (22 kar) · sumber PRD §4.1a Example Data
- **DU-081-12** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing di Warehouse di luar hak Report Disposal Maya Anggraini: Name `Toyota Innova {runId}` (21 kar), Asset ID `FA081-007` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-13** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing di Finance Room untuk seleksi lintas Group: Name `Drill Bosch GSB {runId}` (23 kar), Asset ID `FA081-008` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-14** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing di Warehouse untuk seleksi lintas Group: Name `Genset Honda EU22 {runId}` (25 kar), Asset ID `FA081-009` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-15** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing untuk percobaan Bulk Report Disposal tanpa hak: Name `Kursi Ergonomis {runId}` (23 kar), Asset ID `FA081-010` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-16** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset Missing untuk Bulk Report Disposal oleh Accounting: Name `Meja Kerja Kayu {runId}` (23 kar), Asset ID `FA081-011` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Missing, dilaporkan Rina W` (26 kar) · sumber PRD §4.1a Example Data
- **DU-081-17** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan laporan pemegang yang dilewati Accounting: Name `Papan Tulis {runId}` (19 kar), Asset ID `FA081-012` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Waiting for Confirmation, dilaporkan Joko Susilo {runId}` (56 kar), Pemegang `Joko Susilo {runId}` (19 kar) · sumber PRD §4.1a Example Data
- **DU-081-18** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan Disposal Report milik Eko Wibowo: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Asset ID `FA081-013` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Eko Wibowo {runId}` (48 kar) · sumber PRD §4.1a Example Data
- **DU-081-19** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan Disposal Report milik Rina W: Name `Kamera Sony A7 {runId}` (22 kar), Asset ID `FA081-014` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Rina W` (36 kar) · sumber PRD §4.1a Example Data
- **DU-081-20** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan Disposal Report di Group binaan Maya Anggraini: Name `Scanner Zebra DS2208 {runId}` (28 kar), Asset ID `FA081-015` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `Reported Disposal, dilaporkan Rina W` (36 kar) · sumber PRD §4.1a Example Data
- **DU-081-21** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan Disposal Report di Group di luar binaan Maya Anggraini: Name `Rak Besi Gudang {runId}` (23 kar), Asset ID `FA081-016` (9 kar), Group aset `Warehouse` (9 kar), Record berjalan `Reported Disposal, dilaporkan Rina W` (36 kar) · sumber PRD §4.1a Example Data
- **DU-081-22** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan Disposal Report Reported tanpa record Missing: Name `Brankas Besi {runId}` (20 kar), Asset ID `FA081-017` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Disposal Report `Reported` (8 kar) · sumber PRD §4.1a Example Data
- **DU-081-23** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan baris Disposal Sell berstatus Waiting for Execution: Name `Dispenser Air Galon {runId}` (27 kar), Asset ID `FA081-019` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Baris Disposal `Sell, Waiting for Execution` (27 kar) · sumber PRD §4.1a Example Data
- **DU-081-24** Asset (awal; dimutasi TC-FA-MISS-BE-081-bulk-report-disposal-dep-transactions-disposal), Aset dengan baris Disposal Sell berstatus Waiting for Approval dan Draft Disposal: Name `Lemari Arsip Besi {runId}` (25 kar), Asset ID `FA081-018` (9 kar), Group aset `Finance Room` (12 kar), Record berjalan `tidak ada` (9 kar), Baris Disposal `Sell, Waiting for Approval` (26 kar), Draft Disposal `ada` (3 kar) · sumber PRD §4.1a Example Data
- **DU-081-25** Input aksi (dibuat), Reason input aksi: Reason `Aset tidak ditemukan setelah pencarian dua pekan` (48 kar) · sumber turunan penulis
- **DU-081-26** Input aksi (dibuat), What happened input aksi: What happened `Aset tidak ditemukan saat pengecekan rutin di ruang arsip` (57 kar) · sumber turunan penulis
