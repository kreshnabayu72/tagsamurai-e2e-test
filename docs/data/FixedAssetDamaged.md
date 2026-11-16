<!-- Ditulis stage spec-from-prd saat close. Jangan diubah tangan: run berikutnya menimpanya. -->

Suite: `specs/FixedAsset/Damaged`. Sumber: PRD `fixed-asset@625d932` (sha `cbd9b7ca9320daee`), foundation@8ec9ed8-dirty, kontrak komponen wangs-ui@1.0.0. Stage: `prd-harness@1271d35`, ditutup 2026-11-16T04:02:58Z.

# Matriks data Damaged (a2e6f06bcadf191c)

- Entri: 1034 (awal 843, dibuat 132, dicoba 59)
- Checker: ERROR 0, REVIEW 26

## Target × varian

✓ entri yang memenuhi, ✗ belum ada entri, — tidak berlaku beserta alasannya.

### What happened@report-damaged · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-111-4, DU-201-40 |
| `spasi-saja` | ✓ DU-111-5 |
| `pilihan-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |
| `berkas-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |

### What happened@report-damaged · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-111-6 |
| `lebih-maks` | ✓ DU-111-7 |
| `batas-maks-spasi-tengah` | ✓ DU-111-8 |
| `batas-maks-unicode` | ✓ DU-111-9 |
| `batas-min` | — §9.9: minimum 1 karakter sama dengan aturan wajib (pesan must not be empty) |
| `kurang-min` | — §9.9: minimum 1 = wajib; kosong sudah varian VD-F1 |
| `batas-maks-spasi-tepi` | — §9.9: PRD tidak menyatakan trim (ekspektasi baku: auto-trim tidak diasersi) |
| `addon-tidak-dihitung` | — §9.9: Textarea tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9: field wajib |

### Damaged Photo@report-damaged · VD-F1

| Varian | Entri |
|---|---|
| `berkas-kosong` | ✓ DU-111-4 |
| `kosong` | — FLD-DMG-02 (§9.9): field Image, bukan teks |
| `spasi-saja` | — FLD-DMG-02 (§9.9): field Image, bukan teks |
| `pilihan-kosong` | — FLD-DMG-02 (§9.9): field Image, bukan pilihan |

### Damaged Photo@report-damaged · VD-F12

| Varian | Entri |
|---|---|
| `per-format-izin:JPEG` | ✓ DU-111-10 |
| `per-format-izin:PNG` | ✓ DU-111-11 |
| `format-tolak` | ✓ DU-111-12 |
| `ukuran-di-bawah` | ✓ DU-111-10 |
| `ukuran-tepat-batas` | ✓ DU-111-11 |
| `ukuran-lebih-batas` | ✓ DU-111-13 |
| `satu-foto-auto-default` | — FLD-DMG-02 (§9.9): satu foto per aset, tanpa slot default |
| `default-di-slot-dua` | — FLD-DMG-02 (§9.9): satu foto, tanpa slot kedua |
| `berkas-valid-field-lain-invalid` | — §9.9#p4: nasib berkas staging tidak teramati (orphan file cleanup tidak diasersi); yang diasersi caption field lain saja lewat VD-F1 |
| `unggah-lalu-batal` | — §9.9#p4: pembersihan staging tidak teramati dari luar |
| `ganti-berkas-edit` | — §9.6#p3: tidak ada form edit |
| `hapus-record-berberkas` | — §2#b3: Delete tidak berlaku |

### Repair note@mark-as-repaired · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-114-7, DU-204-20 |
| `spasi-saja` | ✓ DU-114-8 |
| `pilihan-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |
| `berkas-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |

### Repair note@mark-as-repaired · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-114-9 |
| `lebih-maks` | ✓ DU-114-10 |
| `batas-maks-spasi-tengah` | ✓ DU-114-11 |
| `batas-maks-unicode` | ✓ DU-114-12 |
| `batas-min` | — §9.9: minimum 1 karakter sama dengan aturan wajib (pesan must not be empty) |
| `kurang-min` | — §9.9: minimum 1 = wajib; kosong sudah varian VD-F1 |
| `batas-maks-spasi-tepi` | — §9.9: PRD tidak menyatakan trim (ekspektasi baku: auto-trim tidak diasersi) |
| `addon-tidak-dihitung` | — §9.9: Textarea tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9: field wajib |

### After photo@mark-as-repaired · VD-F1

| Varian | Entri |
|---|---|
| `berkas-kosong` | ✓ DU-114-18 |
| `kosong` | — FLD-DMG-04 (§9.9): field Image |
| `spasi-saja` | — FLD-DMG-04 (§9.9): field Image |
| `pilihan-kosong` | — FLD-DMG-04 (§9.9): field Image |

### After photo@mark-as-repaired · VD-F6

| Varian | Entri |
|---|---|
| `terisi` | ✓ DU-114-13 |
| `kosong` | ✓ DU-114-17 |
| `default-tak-disentuh` | — FLD-DMG-04 (§9.9): default kosong, bukan nilai ber-default |
| `per-opsi` | — FLD-DMG-04 (§9.9): bukan field pilihan |
| `pasangan-berinteraksi` | — §4.2.4: tidak ada pasangan field yang berinteraksi |

### After photo@mark-as-repaired · VD-F12

| Varian | Entri |
|---|---|
| `per-format-izin:JPEG` | ✓ DU-114-13 |
| `per-format-izin:PNG` | ✓ DU-114-14 |
| `format-tolak` | ✓ DU-114-15 |
| `ukuran-di-bawah` | ✓ DU-114-13 |
| `ukuran-tepat-batas` | ✓ DU-114-14 |
| `ukuran-lebih-batas` | ✓ DU-114-16 |
| `satu-foto-auto-default` | — FLD-DMG-04 (§9.9): satu foto |
| `default-di-slot-dua` | — FLD-DMG-04 (§9.9): satu foto |
| `berkas-valid-field-lain-invalid` | — §9.9#p4: nasib berkas staging tidak teramati |
| `unggah-lalu-batal` | — §9.9#p4: pembersihan staging tidak teramati |
| `ganti-berkas-edit` | — §9.6#p3: tidak ada form edit |
| `hapus-record-berberkas` | — §2#b3: Delete tidak berlaku |

### Scan TAG@mark-as-repaired · VD-F13

| Varian | Entri |
|---|---|
| `tag-paired-aset` | ✓ DU-012-4 |
| `tag-paired-user-lain` | ✓ DU-012-7 |
| `per-jenis-tag:RFID` | ✓ DU-012-4 |
| `per-jenis-tag:QR` | ✓ DU-012-5 |
| `per-jenis-tag:NFC` | ✓ DU-012-6 |
| `tag-belum-paired` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-tidak-terdaftar` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-bukan-tagsamurai` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `object-tag` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-company-lain` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-belum-diaktivasi` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-damaged` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `tag-missing` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `aset-on-tracking` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `aset-missing` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `group-found-sama` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |
| `group-found-beda` | — FLD-DMG-03 (§9.9): hasil selain TAG milik aset / bukan milik aset dimiliki tag.md §9.12.3 (bukan sumber) |

### Scan TAG@mark-as-repaired · VD-F15

| Varian | Entri |
|---|---|
| `pemicu-tampil` | ✓ DU-113-1 |
| `pemicu-sembunyi` | ✓ DU-113-2 |
| `per-cabang-pemicu:aset ber-TAG` | ✓ DU-113-1 |
| `per-cabang-pemicu:aset tanpa TAG` | ✓ DU-113-2 |
| `ganti-pemicu-setelah-isi` | — §4.2.4#p2: aset dialog tetap satu dan tidak diganti |

### After photo label@mark-as-repaired · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-113-3 |
| `nilai-diubah` | ✓ DU-113-4 |
| `per-nilai-setting:ON` | ✓ DU-113-4 |
| `per-nilai-setting:OFF` | ✓ DU-113-3 |
| `record-sebelum-perubahan` | — §4.3 S-DMG-07: setting dibaca saat dialog dibuka, tanpa efek retroaktif |
| `record-sesudah-perubahan` | — §4.3 S-DMG-07: setting dibaca saat dialog dibuka |
| `per-opsi-format-tanggal` | — FATR-LOGIC-13: setting boolean, bukan format tanggal |
| `zona-waktu-non-default` | — FATR-LOGIC-13: setting boolean |
| `format-regional-beda-entitas` | — §4.3 S-DMG-07: satu setting per entitas suite |

### Reason@reject-report · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-115-2, DU-203-42 |
| `spasi-saja` | ✓ DU-115-3 |
| `pilihan-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |
| `berkas-kosong` | — §9.9: field Textarea, bukan pilihan atau berkas |

### Reason@reject-report · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-115-4 |
| `lebih-maks` | ✓ DU-115-5 |
| `batas-maks-spasi-tengah` | ✓ DU-115-6 |
| `batas-maks-unicode` | ✓ DU-115-7 |
| `batas-min` | — §9.9: minimum 1 karakter sama dengan aturan wajib (pesan must not be empty) |
| `kurang-min` | — §9.9: minimum 1 = wajib; kosong sudah varian VD-F1 |
| `batas-maks-spasi-tepi` | — §9.9: PRD tidak menyatakan trim (ekspektasi baku: auto-trim tidak diasersi) |
| `addon-tidak-dihitung` | — §9.9: Textarea tanpa addon |
| `opsional-kosong-tanpa-min` | — §9.9: field wajib |

### form@report-damaged · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-112-4 |
| `batch-stay-on-form` | — §4.2.3: tanpa checkbox Stay on this form |
| `semua-tipe-kontrol-terisi` | — §4.2.3: tanpa [Clear Field]; kontrol hanya Textarea dan ImagePicker |

### form@mark-as-repaired · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-114-19 |
| `batch-stay-on-form` | — §4.2.4: tanpa checkbox Stay on this form |
| `semua-tipe-kontrol-terisi` | — §4.2.4: tanpa [Clear Field] |

### form@reject-report · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-115-8 |
| `batch-stay-on-form` | — §4.2.4: tanpa checkbox Stay on this form |
| `semua-tipe-kontrol-terisi` | — §4.2.4: tanpa [Clear Field] |

### payload@what-happened · VD-F17

| Varian | Entri |
|---|---|
| `payload-xss` | ✓ DU-008-1 |
| `payload-sqli` | ✓ DU-008-2 |
| `payload-nosqli` | ✓ DU-008-3 |
| `markup-tersimpan` | ✓ DU-008-4 |

### payload@search-active · VD-F17

| Varian | Entri |
|---|---|
| `payload-xss` | ✓ DU-002-16 |
| `payload-sqli` | ✓ DU-002-17 |
| `payload-nosqli` | ✓ DU-002-18 |
| `markup-tersimpan` | ✓ DU-002-7 |

### judul-dan-kotak-dampak@report-damaged · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-110-1 |
| `jumlah-banyak` | ✓ DU-110-3 |
| `jumlah-nol` | — §4.2.3#b5: tanpa aset layak dialog tidak dibuka (D-DMG-12) |
| `per-jumlah-independen` | — §4.2.3#p2: satu jumlah (aset terpilih) |

### keterangan-aset@report-damaged · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-031-1 |
| `n-banyak` | ✓ DU-031-3, DU-031-4 |
| `campuran` | ✓ DU-031-3 |
| `semua-ditolak` | ✓ DU-031-10 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-031-14, DU-031-15 |
| `daftar-melebihi-tampil` | ✓ DU-031-2 |
| `item-beranotasi` | ✓ DU-031-5 |
| `semua-ditolak-alasan-single` | — §4.2.3#b1: titik masuk satu aset tidak menampilkan aksi, tanpa dialog blok |
| `nol-item` | — §4.2.3#b5: semua tidak layak = semua-ditolak (D-DMG-12) |
| `gagal-banyak` | — §7.3 TS-DMG-10: satu toast berapa pun aset yang dilewati |
| `sisa-satu-relevan` | — §4.2.3#b5: Title mengikuti jumlah aset terpilih saat klik tanpa berubah |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada baris Default/Self |

### search@tabel-active · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:teks` | ✓ DU-002-2 |
| `per-kelas-kolom:badge` | ✓ DU-002-3 |
| `per-kelas-kolom:kode` | ✓ DU-002-1 |
| `substring-tengah` | ✓ DU-002-9 |
| `beda-kapital` | ✓ DU-002-10 |
| `tanpa-hasil` | ✓ DU-002-20 |
| `kolom-non-searchable` | ✓ DU-002-21 |
| `kolom-tersembunyi` | ✓ DU-002-1 |
| `lintas-kolom` | ✓ DU-002-1 |
| `kolom-icon-label` | ✓ DU-002-1 |
| `kolom-homogen` | ✓ DU-002-3 |
| `karakter-pola` | ✓ DU-002-15 |
| `query-spasi-tepi` | ✓ DU-002-12 |
| `query-spasi-saja` | ✓ DU-002-25 |
| `query-spasi-tengah` | ✓ DU-002-8 |
| `query-kata-tidak-bersebelahan` | ✓ DU-002-14 |
| `nilai-substring-nilai-lain` | ✓ DU-002-13 |
| `record-tab-non-default` | — §4.4#r1, §9.19: tiap sub-tab punya Search sendiri; tidak ada Search Global lintas sub-tab |
| `cocok-di-anak-saja` | — §4.1a: Search tabel tanpa tree |
| `per-kelas-kolom:numerik` | — §4.1a: kolom numerik searchable hanya Purchase Cost / Asset Value (Commercial / Fiscal), Hidden Curated, nilai dari `asset-registration/` dan nilai buku (modul lain, TV-5) berformat «Mata uang Company» tanpa format tampilan yang ditetapkan PRD, sehingga literal sel tidak bisa ditulis (TL-2); Days Damaged tidak searchable (§4.1a Searchable —); kelas numerik kode diwakili `kode` (Asset ID) |

### sort@tabel-active · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-003-4 |
| `sama-tiebreak` | ✓ DU-003-6 |
| `kosong` | ✓ DU-003-1 |
| `beda-kapital` | ✓ DU-003-1, DU-003-2 |
| `natural` | ✓ DU-003-3, DU-003-4, DU-003-5 |
| `per-tipe-kolom:tanggal` | ✓ DU-003-5 |
| `per-tipe-kolom:badge` | ✓ DU-003-3 |
| `aksen` | ✓ DU-003-6, DU-003-7, DU-003-8 |
| `diawali-angka-simbol` | ✓ DU-003-9, DU-003-10 |
| `default-beda` | ✓ DU-003-5 |
| `sisip-beda-default` | ✓ DU-003-1 |
| `lintas-halaman` | ✓ DU-003-11, DU-003-12 |
| `sama-melintasi-halaman` | ✓ DU-003-11, DU-003-12 |
| `sama-di-kolom-dan-default` | ✓ DU-003-11, DU-003-12 |
| `nama-tampil-beda-nama-penuh` | ✓ DU-003-6, DU-003-11 |
| `per-tipe-kolom:currency` | — §4.1a: kolom currency hanya Purchase Cost / Asset Value (Commercial / Fiscal), Hidden Curated, nilai dari `asset-registration/` dan nilai buku (modul lain, TV-5) berformat «Mata uang Company» tanpa format tampilan yang ditetapkan PRD, sehingga urutan sel tidak bisa diasersi dengan literal (TL-2); sort numerik kolom itu milik be-e2e (target sort@server) |
| `jumlah-chip-sama` | — §4.1a Labels: kolom Hidden Curated berisi label aset milik modul Asset (§9.7#b1 Reflected, ikut berubah saat pemilik berubah); baris berlabel adalah data modul lain yang tidak dibentuk spec inti (TV-5, IS-2), dan sort «+N more» mengikuti pola bersama prd-conventions §9.7 |
| `jumlah-aktif-sama` | — §4.1a: tidak ada kolom ikon aktif atau boolean |
| `campuran-tipe` | — §4.1a: tidak ada kolom Old/New Value bertipe campuran |
| `format-komposit` | — §4.1a: tidak ada kolom ukuran berkas atau IP |
| `urutan-custom` | — §4.1a Status: «Alphabetical by label», bukan urutan lifecycle |
| `urutan-beda-antar-kolom` | — §4.1a: semua kolom teks Alphabetical (A–Z); tidak ada urutan berbeda antar kolom sejenis |

### filter@tabel-active · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-004-1 |
| `tidak-cocok` | ✓ DU-004-3 |
| `and-a-saja` | ✓ DU-004-2 |
| `and-b-saja` | ✓ DU-004-5 |
| `and-keduanya` | ✓ DU-004-1 |
| `and-tidak-keduanya` | ✓ DU-004-3 |
| `or-dalam-field` | ✓ DU-004-4 |
| `search-saja` | ✓ DU-004-5 |
| `filter-saja` | ✓ DU-004-2 |
| `search-dan-filter` | ✓ DU-004-1 |
| `irisan-kosong` | ✓ DU-004-5 |
| `kolom-tersembunyi` | ✓ DU-004-8 |
| `rentang-dalam` | ✓ DU-004-7 |
| `rentang-luar` | ✓ DU-004-15 |
| `rentang-tepat-awal` | ✓ DU-004-7 |
| `rentang-tepat-akhir` | ✓ DU-004-6 |
| `rentang-sehari` | ✓ DU-004-2 |
| `range-tepat-min` | ✓ DU-004-4 |
| `range-tepat-max` | ✓ DU-004-6 |
| `range-hanya-min` | ✓ DU-004-3 |
| `range-hanya-max` | ✓ DU-004-8 |
| `per-kelas-kontrol:Multi-select searchable` | ✓ DU-004-1 |
| `per-kelas-kontrol:Tree picker multi-select` | ✓ DU-004-2 |
| `per-kelas-kontrol:Date range picker` | ✓ DU-004-14 |
| `per-kelas-kontrol:Range Min–Max` | ✓ DU-004-16 |
| `mutasi-keluar-saringan` | ✓ DU-004-8 |
| `mutasi-masuk-saringan` | ✓ DU-004-1, DU-004-10 |
| `filter-only` | — §4.1a: setiap field filter memiliki kolom tabel |
| `boolean-kedua-nilai` | — §4.1a: tidak ada field boolean |
| `custom-field-per-tipe` | — §4.1a: tidak ada custom field |
| `create-tidak-cocok` | — §4.2.1#b1: record baru dibuat di modul lain; tidak dibentuk di spec inti (EB-FLT-1 alasan) |
| `status-dikecualikan` | — §9.5#r7: semua status record berjalan menjadi opsi |
| `default-filter-lolos` | — §9.5#r5: tidak ada default filter |
| `default-filter-tersaring` | — §9.5#r5: tidak ada default filter |
| `range-min-lebih-max` | — §4.1a Range Min–Max: PRD tidak menetapkan hasil Min > Max; prd-conventions §9.8 «Penanganan Min > Max mengikuti perilaku bawaan komponen FilterContainer» tanpa copy, dan kontrak FilterContainer#13 hanya menetapkan rentang inklusif dan batas kosong; hasilnya tidak ditetapkan sumber mana pun (VD-9) |

### filter-opsi@tabel-active · VD-T4

| Varian | Entri |
|---|---|
| `nilai-berulang` | ✓ DU-004-2 |
| `kosong` | ✓ DU-004-5 |
| `kolom-tanpa-null` | ✓ DU-004-1 |
| `master-tak-terpakai` | ✓ DU-004-18 |
| `enum-sebagian-terisi` | ✓ DU-004-9 |
| `per-anggota-enum:Waiting for Confirmation` | ✓ DU-004-3 |
| `per-anggota-enum:Damaged` | ✓ DU-004-6 |
| `per-anggota-enum:Reported Disposal` | ✓ DU-004-4 |
| `per-anggota-enum:In Disposal Process` | ✓ DU-004-5 |
| `per-anggota-enum:Reported Missing` | ✓ DU-004-6 |
| `per-anggota-enum:Missing` | ✓ DU-004-7 |
| `nilai-di-cakupan-lain` | ✓ DU-004-9 |
| `opsi-tidak-dipersempit-search` | ✓ DU-004-1 |
| `opsi-hilang` | ✓ DU-004-8 |
| `cari-opsi-substring` | ✓ DU-004-2, DU-004-17 |
| `cari-opsi-beda-kapital` | ✓ DU-004-5, DU-004-17 |
| `cari-opsi-tanpa-hasil` | ✓ DU-004-17 |
| `nilai-baru-saat-uji` | — §4.2.1#b1: record baru dibuat di modul lain, tidak dibentuk di spec inti |
| `opsi-tetap-worm` | — §4.1a: bukan log WORM |
| `entitas-terhapus-berhistori` | — §9.7#b1: Group/Category di Active Reflected, bukan snapshot (varian History) |
| `entitas-rename-berhistori` | — §9.7#b1: Reflected di Active (varian History) |
| `sumber-kosong` | — §9.5#r7: sumber opsi data tabel; tabel kosong adalah S-DMG-11 yang diasersi ui-client sebagai Kondisi |
| `nilai-kondisional` | — §4.1a: tidak ada opsi bersyarat |
| `satu-nilai-distinct` | — §9.5#r7 / prd-conventions §9.8: opsi = DISTINCT seluruh baris tabel pada cakupan Group pengguna; tepat satu nilai distinct adalah keadaan seluruh daftar entitas (IN-2) yang memuat baris spec lain dan tidak dibentuk pada entitas suite (spec 004 tanpa entitasKhusus) |
| `dua-nilai-distinct` | — §9.5#r7 / prd-conventions §9.8: opsi = DISTINCT seluruh baris tabel pada cakupan Group pengguna; tepat dua nilai distinct adalah keadaan seluruh daftar entitas (IN-2) yang memuat baris spec lain dan tidak dibentuk pada entitas suite (spec 004 tanpa entitasKhusus) |
| `opsi-banyak-overflow` | — §9.5#r7 / prd-conventions §9.8: tidak ada ambang jumlah opsi; kontrak FilterContainer#12 meringkas chip «when there is no room», bergantung lebar panel dan bukan jumlah data, sehingga jumlah yang muat tidak diasersi (LR-5, VD-9) |

### filter-status@tabel-history · VD-T4

| Varian | Entri |
|---|---|
| `per-anggota-enum:Repaired` | ✓ DU-007-1 |
| `per-anggota-enum:Disposed` | ✓ DU-007-2 |
| `per-anggota-enum:Rejected` | ✓ DU-007-3 |
| `per-anggota-enum:Canceled` | ✓ DU-007-4 |
| `entitas-terhapus-berhistori` | ✓ DU-007-3, DU-007-6 |
| `entitas-rename-berhistori` | ✓ DU-007-4, DU-007-6 |
| `nilai-berulang` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `kosong` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `kolom-tanpa-null` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `master-tak-terpakai` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `enum-sebagian-terisi` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `nilai-di-cakupan-lain` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `nilai-kondisional` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `opsi-tidak-dipersempit-search` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `nilai-baru-saat-uji` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `opsi-hilang` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `opsi-tetap-worm` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `opsi-banyak-overflow` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `cari-opsi-substring` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `cari-opsi-beda-kapital` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `cari-opsi-tanpa-hasil` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `sumber-kosong` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `satu-nilai-distinct` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |
| `dua-nilai-distinct` | — §4.1b: tabel kedua sejenis, mekanik opsi diuji di T-DMG-01 (EB-6 pertama-per-jenis) |

### paginasi@tabel-active · VD-T5

| Varian | Entri |
|---|---|
| `lebih-satu-halaman` | ✓ DU-005-1 |
| `satu-baris-halaman-terakhir` | ✓ DU-005-2 |
| `tepat-ukuran-halaman` | ✓ DU-005-1 |
| `lebih-ukuran-terpilih:10` | ✓ DU-005-1 |
| `lebih-ukuran-terpilih:25` | ✓ DU-005-2 |
| `tersaring-lebih-satu-halaman` | ✓ DU-005-2 |
| `lebih-ukuran-maks` | — §9.5#r4: paginasi tanpa delta; 101 record ber-{runId} melebihi volume yang dibentuk spec fungsional (RC-4 volume) |
| `nomor-halaman-invalid` | — §9.5#r4 → prd-conventions §9.18 dan Paginator#9: input nomor halaman `0`, `-1`, `abc`, dan melebihi halaman terakhir bukan record dan tidak bergantung isi data (VD-6 bukan data: mekanik Paginator); diasersi sebagai langkah kelompok «Nomor halaman tidak valid» di TC-FA-DAMAGED-UI-102-tabel-active-mekanik-toolbar (EB-TBL-7@tabel-active), bukan entri data |

### tampilan-sel@tabel-active · VD-T7

| Varian | Entri |
|---|---|
| `null` | ✓ DU-101-3 |
| `array-kosong` | ✓ DU-101-11 |
| `nol-numerik` | ✓ DU-101-13 |
| `tanggal-null` | ✓ DU-101-11 |
| `kosong-tidak-pernah-diisi` | ✓ DU-101-11 |
| `teks-panjang` | ✓ DU-101-12 |
| `per-nilai-badge:Waiting for Confirmation` | ✓ DU-101-2 |
| `per-nilai-badge:Damaged` | ✓ DU-101-1 |
| `per-nilai-badge:Reported Disposal` | ✓ DU-101-4 |
| `per-nilai-badge:In Disposal Process` | ✓ DU-101-5 |
| `tanpa-foto` | ✓ DU-101-3 |
| `angka-ribuan` | ✓ DU-101-10 |
| `nilai-turunan` | ✓ DU-101-10 |
| `nilai-beda-antar-kolom` | ✓ DU-101-1 |
| `string-kosong` | — §4.1a: nilai kosong adalah null (aset tanpa pemegang / tanpa Alias), bukan string kosong |
| `boolean-null` | — §4.1a: tidak ada kolom boolean |
| `kosong-setelah-dihapus` | — §9.7#b3: kolom Reflected ikut pemilik; riwayat penghapusan nilai tidak teramati di modul ini |
| `teks-panjang-multibaris` | — §4.1a: tidak ada kolom multi-baris |
| `angka-pembulatan` | — §4.1a: Days Damaged bilangan bulat hari; mata uang mengikuti format Company |
| `asal-jalur` | — VD-9/TV-5: hanya beda asal data; dimiliki target data-baris@tabel-active (ui-e2e) |
| `referensi-terhapus` | — §9.7#b1: Group/Category/Brand Reflected; hapus referensi dimiliki modul asal (temuan 1) |
| `referensi-diarsipkan` | — §4.1a: tidak ada referensi terarsip |
| `aktor-system` | — §4.1a Modified By `System`: asal nilai dari server, dimiliki target data-baris@tabel-active (ui-e2e) |

### data-baris@tabel-active · VD-T7

| Varian | Entri |
|---|---|
| `aktor-system` | ✓ DU-001-5 |
| `asal-jalur:Manual` | ✓ DU-001-2 |
| `asal-jalur:Reported by scan` | ✓ DU-001-7 |
| `asal-jalur:Reported by holder` | ✓ DU-001-1 |
| `asal-jalur:Borrow return` | ✓ DU-001-6 |
| `asal-jalur:Stock opname` | ✓ DU-001-3 |
| `asal-jalur:Missing asset` | ✓ DU-001-8 |
| `asal-jalur:Registration` | ✓ DU-001-9 |
| `asal-jalur:Transfer receive` | ✓ DU-001-10 |
| `null` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `string-kosong` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `array-kosong` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `nol-numerik` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `boolean-null` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `tanggal-null` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `kosong-tidak-pernah-diisi` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `kosong-setelah-dihapus` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `teks-panjang` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `teks-panjang-multibaris` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `per-nilai-badge` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `tanpa-foto` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `angka-ribuan` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `angka-pembulatan` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `nilai-turunan` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `nilai-beda-antar-kolom` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `referensi-terhapus` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |
| `referensi-diarsipkan` | — §4.1a: transformasi tampilan klien atas nilai ini dimiliki target tampilan-sel@tabel-active (ui-client) |

### kolom-labels@tabel-active · VD-T8

| Varian | Entri |
|---|---|
| `nol` | ✓ DU-101-11 |
| `satu` | ✓ DU-101-13 |
| `dua` | ✓ DU-101-12 |
| `lebih-dua` | ✓ DU-101-10 |
| `urutan-input-acak` | ✓ DU-101-10, DU-101-12 |
| `semua-master` | — §4.1a Labels: «Satu badge per label», tanpa bentuk All |
| `total-kurang-satu` | — §4.1a Labels: tanpa bentuk All |
| `switch-off-relasi-tersimpan` | — §4.1a: tidak ada switch |
| `konsolidasi-multi-group` | — §4.1a: Labels bukan role per group |

### nama-user@tabel-active · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-101-2 |
| `dua-kata` | ✓ DU-101-1 |
| `tiga-kata-lebih` | ✓ DU-101-4 |
| `nama-panjang` | ✓ DU-101-4 |
| `tanpa-last-name` | ✓ DU-101-2 |
| `nama-mirip` | ✓ DU-101-5 |

### days-damaged@tabel-active · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-101-2 |
| `jumlah-banyak` | ✓ DU-101-1 |
| `jumlah-nol` | ✓ DU-101-8 |
| `per-jumlah-independen` | — §4.1a Days Damaged: satu angka |

### kolom-tanggal@tabel-active · VD-T13

| Varian | Entri |
|---|---|
| `hari-lebih-12` | ✓ DU-101-9 |
| `dekat-tengah-malam` | ✓ DU-101-9 |

### seleksi@tabel-active · VD-T14

| Varian | Entri |
|---|---|
| `satu-baris` | ✓ DU-013-1 |
| `banyak-baris` | ✓ DU-013-1 |
| `halaman-penuh` | ✓ DU-013-1 |
| `checkbox-disabled` | ✓ DU-013-2, DU-013-3, DU-013-4, DU-013-5, DU-013-6 |
| `lintas-halaman` | ✓ DU-013-1 |
| `tersembunyi-filter` | ✓ DU-013-1 |
| `homogen:Damaged` | ✓ DU-013-1 |
| `campuran-state` | — §4.1a: checkbox baris bukan Damaged Disabled, seleksi selalu Damaged |
| `single-select-ganti` | — §4.1a: multi-select, bukan single-select |

### selection-limit@tabel-active · VD-A6

| Varian | Entri |
|---|---|
| `per-jenis-limit:Selection Limit` | ✓ DU-103-11 |
| `di-bawah` | ✓ DU-103-10 |
| `tepat-batas` | ✓ DU-103-11 |
| `lebih-batas` | ✓ DU-103-12 |
| `limit-diturunkan` | ✓ DU-103-14 |
| `tersaring-lebih-limit` | ✓ DU-103-13 |
| `sisa-satu` | — prd-conventions.md §8: Selection Limit dicek per checkbox, tanpa race antar aktor |
| `over-cap-downgrade` | — §4.1a: bukan kuota data tersimpan |
| `tersimpan-melebihi-batas-baru` | — §4.1a: bukan kuota data tersimpan |
| `tanpa-cap-mobile` | — §4.6#p1: tidak ada tabel Damaged di mobile |
| `berurutan-stay-on-form` | — §4.2.3: tanpa Stay on this form |
| `saldo-cukup` | — §4.1a: bukan saldo |
| `saldo-kurang` | — §4.1a: bukan saldo |
| `kuota-status-akun` | — §4.1a: bukan kuota akun |

### empty-state@tab-damaged · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-101-15, DU-106-5 |
| `kosong-untuk-aktor-ini` | ✓ DU-101-16 |
| `log-kosong` | — S-DMG-15 (§7.1): Damage Log tidak pernah kosong |
| `relasi-kosong` | — §4.1a: tidak ada induk-anggota |
| `node-tanpa-anak` | — §4.1a: tidak ada tree data |
| `jadi-kosong-setelah-hapus` | — dimiliki target empty-state-setelah-selesai@tabel-active (ui-e2e, EB-EDG-2) |

### empty-state-setelah-selesai@tabel-active · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-021-1 |
| `jadi-kosong-setelah-hapus` | ✓ DU-021-1 |
| `log-kosong` | — S-DMG-15 (§7.1): Damage Log tidak pernah kosong |
| `relasi-kosong` | — §4.1a: tidak ada induk-anggota |
| `node-tanpa-anak` | — §4.1a: tidak ada tree data |
| `kosong-untuk-aktor-ini` | — §2.1#r11: cakupan per aktor dimiliki target empty-state@tab-damaged (ui-client) |

### badge-tab@tab-damaged · VD-T11

| Varian | Entri |
|---|---|
| `mutasi-penggeser` | ✓ DU-011-1, DU-041-1 |
| `detail-dikecualikan` | ✓ DU-011-3 |
| `angka-unik-per-metric` | — §4.3 S-DMG-01: satu metric |
| `nol` | — §4.3 S-DMG-01: badge tanpa record = daftar kosong (spec 021, entitas khusus) |
| `detail-lintas-halaman` | — §4.3 S-DMG-01: badge tanpa daftar detail |

### status-record@tabel-active · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Waiting for Confirmation` | ✓ DU-001-1 |
| `per-status:Damaged` | ✓ DU-001-6 |
| `per-status:Reported Disposal` | ✓ DU-001-3 |
| `per-status:In Disposal Process` | ✓ DU-001-2 |
| `flag-terkunci:Reported Missing` | ✓ DU-001-4 |
| `flag-terkunci:Missing` | ✓ DU-001-5 |
| `per-kondisi-disabled:penanda Missing` | ✓ DU-001-4 |
| `per-kondisi-disabled:Reported Disposal / In Disposal Process` | ✓ DU-001-2 |
| `transisi-valid` | — §9.2 "9.2.0": transisi diuji be-e2e (target status-record@server) |
| `transisi-mundur` | — §9.2 "9.2.0": transisi dimiliki target status-record@server |
| `transisi-ilegal` | — §9.2 "9.2.0": transisi dimiliki target status-record@server |
| `state-final` | — §4.1a: status selesai ada di History (target status-record@tabel-history) |
| `sudah-di-state-tujuan` | — §9.6: idempotensi dimiliki target status-record@server |
| `state-transien` | — §9.2 "9.2.0": tidak ada status transien |
| `koheren-rantai-gate` | — §4.1a: tiap baris satu status, tanpa rantai gate |
| `per-kondisi-disabled:level Feature Suite Disposal None` | — §9.10#p1 / EC-DMG-36: kondisi tingkat entitas (level Feature Suite Disposal), bukan state record tabel; lingkungan suite memakai level Basic (plans.md §3.4a) dan keadaan None dibentuk spec TC-FA-DAMAGED-E2E-025-plan-disposal-none ber-entitasKhusus status-entitas (IN-2), bukan entri data record di entitas suite |

### status-record@tabel-history · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Repaired` | ✓ DU-007-1 |
| `per-status:Disposed` | ✓ DU-007-2 |
| `per-status:Rejected` | ✓ DU-007-3 |
| `per-status:Canceled` | ✓ DU-007-4 |
| `state-final` | ✓ DU-007-1 |
| `transisi-valid` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `transisi-mundur` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `transisi-ilegal` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `sudah-di-state-tujuan` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `state-transien` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `flag-terkunci` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `per-kondisi-disabled` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |
| `koheren-rantai-gate` | — §4.1b: record selesai, tanpa transisi, penanda, atau kondisi aksi (hanya Damage Log) |

### status-record@server · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Waiting for Confirmation` | ✓ DU-207-7 |
| `per-status:Damaged` | ✓ DU-207-8 |
| `per-status:Reported Disposal` | ✓ DU-207-8 |
| `per-status:In Disposal Process` | ✓ DU-207-8 |
| `per-status:Repaired` | ✓ DU-207-18 |
| `per-status:Disposed` | ✓ DU-207-8, DU-207-19 |
| `per-status:Rejected` | ✓ DU-207-20 |
| `per-status:Canceled` | ✓ DU-207-21 |
| `transisi-valid` | ✓ DU-207-8 |
| `transisi-mundur` | ✓ DU-207-9, DU-207-10, DU-207-13, DU-207-14, DU-207-15, DU-207-16 |
| `transisi-ilegal` | ✓ DU-207-7, DU-207-17, DU-207-18, DU-207-20, DU-207-21 |
| `state-final` | ✓ DU-207-19 |
| `sudah-di-state-tujuan` | ✓ DU-207-12 |
| `flag-terkunci:Reported Missing` | ✓ DU-207-23 |
| `flag-terkunci:Missing` | ✓ DU-207-24 |
| `state-transien` | — §9.2 "9.2.0": tidak ada status transien |
| `per-kondisi-disabled` | — §4.3: kondisi Disabled UI dimiliki target status-record@tabel-active |
| `koheren-rantai-gate` | — §9.2 "9.2.0": satu status per record tanpa rantai gate |

### konkurensi@server · VD-A7

| Varian | Entri |
|---|---|
| `diubah-pihak-lain` | ✓ DU-203-26 |
| `per-pasangan-aksi:Confirm-Cancel Report` | ✓ DU-203-25 |
| `per-pasangan-aksi:Mark as Repaired-Report Disposal` | ✓ DU-203-28 |
| `per-pasangan-aksi:Cancel Disposal Report-Dispose` | ✓ DU-203-30 |
| `per-pasangan-aksi:Bulk Report Disposal-Mark as Repaired` | ✓ DU-203-31 |
| `per-pasangan-aksi:Report Damaged-Report Damaged` | ✓ DU-203-35 |
| `create-bersamaan` | ✓ DU-203-35 |
| `status-diubah-pihak-lain` | ✓ DU-203-27 |
| `bulk-semua-jadi-dipakai` | ✓ DU-203-33, DU-203-34 |
| `bulk-sebagian-jadi-dipakai` | ✓ DU-203-31, DU-203-32 |
| `permintaan-basi` | ✓ DU-203-29, DU-203-36 |
| `dihapus-pihak-lain` | — §2#b3: Delete tidak berlaku |
| `target-sama-nilai-beda` | — §9.6#p3: tidak ada form edit |
| `target-beda` | — §9.6#p3: tidak ada form edit |
| `create-nilai-sama-serentak` | — §9.9: tidak ada field unik |
| `jadi-dipakai-saat-confirm` | — §6: tidak ada guard in-use |
| `nilai-guard-berubah` | — §6: tidak ada guard bernilai |
| `dibuat-pihak-lain` | — §9.6: PRD tidak menetapkan live update (SSE) |
| `pihak-lain-cocok-saringan` | — §9.6: PRD tidak menetapkan live update |
| `pihak-lain-tidak-cocok-saringan` | — §9.6: PRD tidak menetapkan live update |
| `pihak-lain-halaman-lain` | — §9.6: PRD tidak menetapkan live update |
| `pihak-lain-ubah-baris-terseleksi` | — §9.6: PRD tidak menetapkan live update; perubahan baris terseleksi dicek saat submit (EC-DMG-35) |

### record-berjalan@aset · VD-A3

| Varian | Entri |
|---|---|
| `tepat-maksimal` | ✓ DU-201-18 |
| `mutually-exclusive` | ✓ DU-201-18, DU-201-19, DU-201-20, DU-201-21 |
| `per-operasi:Report Damaged` | ✓ DU-201-19 |
| `per-operasi:Unassigned bermarker Damaged` | ✓ DU-201-30 |
| `per-operasi:Mark as Found Damaged` | ✓ DU-201-31 |
| `per-operasi:Registrasi` | ✓ DU-201-32 |
| `per-operasi:Transfer receive` | ✓ DU-201-33 |
| `per-operasi:Stock opname` | ✓ DU-201-34 |
| `item-terakhir` | — §9.2#b3 (DAMAGED-LOGIC-01b): invarian maksimum satu record, bukan item terakhir |
| `terakhir-tidak-dipakai` | — §9.2#b3: bukan guard item terakhir |
| `dipakai-bukan-terakhir` | — §9.2#b3: bukan guard item terakhir |
| `item-terakhir-via-cascade` | — §2#b3: Delete tidak berlaku |
| `pembeda-interpretasi` | — §9.2#b3 (DAMAGED-LOGIC-01b/01d): satu tafsiran, laporan kedua ditolak |

### custody@report-disposal · VD-A2

| Varian | Entri |
|---|---|
| `dipakai` | ✓ DU-041-2, DU-041-3 |
| `tidak-dipakai` | ✓ DU-041-1 |
| `per-jenis-pemakai:Borrowed` | ✓ DU-041-2 |
| `per-jenis-pemakai:Assigned` | ✓ DU-041-3 |
| `pemakai-status-lain` | — §4.1a: Custody Available atau dipegang; tidak ada status pemakai lain |
| `pemakai-di-recycle-bin` | — §4.1a: tidak ada Recycle Bin |
| `pemakai-snapshot` | — §4.1a: tidak ada pemakai snapshot |
| `dipakai-multi-konsumen` | — §4.1a: satu pemegang per aset |

### bulk-report-disposal@tabel-active · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-042-1 |
| `n-banyak` | ✓ DU-042-2 |
| `campuran` | ✓ DU-042-3 |
| `semua-ditolak` | ✓ DU-042-4 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-042-3 |
| `gagal-banyak` | ✓ DU-042-3 |
| `daftar-melebihi-tampil` | ✓ DU-042-4 |
| `item-beranotasi` | ✓ DU-042-4 |
| `semua-ditolak-alasan-single` | — §4.2.4#p10: D-DMG-13 hanya untuk bulk; aksi tunggal memakai D-DMG-06 |
| `nol-item` | — §4.1a: bar hanya tampil saat ≥ 1 baris terpilih; semua dilewati = semua-ditolak |
| `sisa-satu-relevan` | — D-DISP-13 (§4.2.4, baris Bulk Report Disposal): satu Reason untuk semua; PRD tidak menyatakan bentuk tunggal |
| `termasuk-baris-terlindungi` | — §4.1a: tidak ada baris Default/Self |

### kondisi-bulk@tabel-active · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-02.k1` | ✓ DU-042-5, DU-042-6 |
| `per-kondisi:F-DMG-02.k2` | ✓ DU-042-3 |
| `lolos-semua-cabang` | ✓ DU-042-2 |
| `efek-samping-per-cabang` | ✓ DU-042-3 |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API (M-2 milik backend) |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### kondisi@report-damaged · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-01.k1` | ✓ DU-201-18 |
| `per-kondisi:F-DMG-01.k2` | ✓ DU-201-22, DU-201-23 |
| `per-kondisi:F-DMG-01.k3` | ✓ DU-201-14 |
| `per-kondisi:F-DMG-01.k5` | ✓ DU-201-27 |
| `per-kondisi:F-DMG-01.k7` | ✓ DU-201-13 |
| `per-kondisi:F-DMG-01.k8` | ✓ DU-201-19 |
| `per-kondisi:F-DMG-01.k9` | ✓ DU-201-29, DU-201-41 |
| `lolos-semua-cabang` | ✓ DU-201-12 |
| `efek-samping-per-cabang` | ✓ DU-201-18 |
| `per-kondisi:F-DMG-01.k4` | — §9.2#b7: jalur Return/Unassign; data dibuat form modul asal (spec -dep-borrow) |
| `per-kondisi:F-DMG-01.k6` | — §9.2#b5: record dibuat transaksi aktivasi registrasi (spec -dep-asset-registration) |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### kondisi@review · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-04.k2` | ✓ DU-203-25 |
| `per-kondisi:F-DMG-04.k4` | ✓ DU-203-9, DU-203-38 |
| `lolos-semua-cabang` | ✓ DU-203-15 |
| `efek-samping-per-cabang` | ✓ DU-203-15, DU-203-20 |
| `per-kondisi:F-DMG-04.k3` | — EC-DMG-23: menunggu lama adalah waktu berlalu (Kondisi, bukan data) |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### kondisi@mark-as-repaired · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-05.k1` | ✓ DU-204-7 |
| `per-kondisi:F-DMG-05.k2` | ✓ DU-204-8 |
| `per-kondisi:F-DMG-05.k4` | ✓ DU-204-9 |
| `per-kondisi:F-DMG-05.k5` | ✓ DU-204-6 |
| `per-kondisi:F-DMG-05.k6` | ✓ DU-204-10, DU-204-11 |
| `lolos-semua-cabang` | ✓ DU-204-5 |
| `efek-samping-per-cabang` | ✓ DU-204-5 |
| `per-kondisi:F-DMG-05.k3` | — §9.4.1#r12: TAG rusak adalah dependensi eksternal (Kondisi) |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### kondisi@report-disposal · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-06.k1` | ✓ DU-207-9, DU-207-13 |
| `per-kondisi:F-DMG-06.k2` | ✓ DU-207-11, DU-207-12 |
| `per-kondisi:F-DMG-06.k3` | ✓ DU-207-8 |
| `per-kondisi:F-DMG-06.k4` | ✓ DU-207-35 |
| `lolos-semua-cabang` | ✓ DU-207-8 |
| `efek-samping-per-cabang` | ✓ DU-207-8 |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### kondisi@missing-bersamaan · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-DMG-10.k1` | ✓ DU-206-6 |
| `per-kondisi:F-DMG-10.k2` | ✓ DU-206-11 |
| `per-kondisi:F-DMG-10.k3` | ✓ DU-206-9, DU-206-10 |
| `per-kondisi:F-DMG-10.k4` | ✓ DU-206-13 |
| `lolos-semua-cabang` | ✓ DU-206-6 |
| `efek-samping-per-cabang` | ✓ DU-206-6 |
| `per-langkah-logic` | — §9.6#p2: tidak ada dokumen API |
| `per-baris-error-handling` | — §9.6#p2: tidak ada dokumen API |

### akses@tab-damaged · VD-P1

| Varian | Entri |
|---|---|
| `per-baris-matriks:Total Control` | ✓ DU-205-1 |
| `per-baris-matriks:Group Manager` | ✓ DU-205-2 |
| `per-baris-matriks:Manage asset & TAG (Update)` | ✓ DU-205-3 |
| `per-baris-matriks:Read Only` | ✓ DU-205-4 |
| `per-baris-matriks:Manage asset & TAG (Read)` | ✓ DU-205-5 |
| `per-baris-matriks:View asset value` | ✓ DU-205-6 |
| `per-baris-matriks:Pelapor umum` | ✓ DU-205-7 |
| `tanpa-akses` | ✓ DU-205-8 |
| `read-only-saja` | ✓ DU-205-4 |
| `capability-tunggal:Update` | ✓ DU-205-3 |
| `tanpa-capability-aksi:Update` | ✓ DU-205-5, DU-205-10 |
| `tanpa-bulk` | ✓ DU-205-4 |
| `tanpa-sesi` | ✓ DU-205-49 |
| `entitas-diblok-punya-role` | ✓ DU-205-14 |
| `per-peran-alur:Pelapor admin` | ✓ DU-205-1 |
| `per-peran-alur:pelapor umum` | ✓ DU-205-7 |
| `per-peran-alur:Aktor transaksi` | ✓ DU-205-11 |
| `per-peran-alur:pemilik sesi Stock Opname` | ✓ DU-205-12 |
| `kombinasi-permission` | — §2#b3: hanya Read dan Update; Create dan Delete tidak berlaku |
| `per-kombinasi-crud` | — §2#b3: hanya Read dan Update |
| `tanpa-single-action` | — §2.1: aksi baris dan bulk mengikuti hak yang sama (Update / hak Report Disposal) |
| `access-level-null-plus-individual` | — §2#b1: modul tidak digate Global Role / access level |
| `zero-assignment` | — §2#b2: Group Role memakai Group penugasan; tanpa assignment = tanpa akses (varian tanpa-akses) |
| `can-read-false` | — §2#b2: CRUD per-group dimiliki settings-role-permission; Read false = tanpa-akses |
| `assignment-retained` | — §2#b2: tidak ada switch modul |
| `per-jenis-entitas` | — §2.1#r11: scope seluruh client; tidak ada jenis entitas lain |

### cakupan@tab-damaged · VD-P2

| Varian | Entri |
|---|---|
| `luar-entitas` | ✓ DU-205-41 |
| `luar-group` | ✓ DU-205-2 |
| `multi-group` | ✓ DU-205-3 |
| `field-termask` | ✓ DU-205-25 |
| `field-terbatas-per-role` | ✓ DU-205-4, DU-205-25 |
| `scope-sub-tree` | ✓ DU-205-2 |
| `assignment-node-descendant` | ✓ DU-205-3 |
| `dua-aktor-scope-beda` | ✓ DU-205-2, DU-205-6 |
| `client-multi-partner` | — §2.1#r11: scope di dalam satu client |
| `client-transitif` | — §2.1#r11: scope di dalam satu client |
| `target-write-transitif` | — §2.1#r11: scope Group, bukan jaringan entitas |
| `target-write-langsung` | — §2.1#r11: scope Group, bukan jaringan entitas |
| `scope-exact-match` | — §2.1#r11: semua scope Group + descendant |

### akses-langsung@damage-log · VD-P4

| Varian | Entri |
|---|---|
| `aktor-tanpa-read` | ✓ DU-205-8 |
| `id-tidak-ada` | ✓ DU-205-48 |
| `id-milik-entitas-lain` | ✓ DU-205-41 |
| `id-sudah-dihapus` | — §2#b3: Delete tidak berlaku; record tidak dihapus |

### plan-disposal@tab-damaged · VD-P5

| Varian | Entri |
|---|---|
| `per-level:None` | ✓ DU-025-1 |
| `per-level:Basic` | ✓ DU-025-2 |
| `per-level:Full` | ✓ DU-025-3 |
| `per-tier` | — §9.10#p1: yang menentukan level Feature Suite Disposal, bukan tier |
| `basic-dalam-scope` | — plans.md §3.4a: Report Disposal berlaku di semua level selain None |
| `basic-luar-scope` | — plans.md §3.4a: Report Disposal berlaku di semua level selain None |
| `addon-dibeli` | — §9.10#p1: bukan add-on |
| `addon-tidak-dibeli` | — §9.10#p1: bukan add-on |
| `cap-plan-lama-beda-baru` | — §9.10#p1: tidak ada cap |

### entitas@tab-damaged · VD-A4

| Varian | Entri |
|---|---|
| `active` | ✓ DU-024-1 |
| `suspended` | ✓ DU-024-2 |
| `expired` | ✓ DU-024-3 |
| `deleted` | — entity-isolation.md §18.8: state Suspended/Expired; entitas terhapus tidak punya sesi |
| `per-jenis-entitas-pemilik` | — §2.1#r11: client |
| `per-peran-entitas` | — §2.1#r11: client tunggal |
| `job-sistem` | — §9.4.1#r1: modul tidak menjalankan job sendiri; event tanpa aktor dari modul lain |
| `aksi-reaktivasi` | — entity-isolation.md §18.8: pengecualian milik Client Subscription, bukan modul ini |
| `per-interval` | — §9.4.1#r1: tanpa interval |

### damage-log@record · VD-L1

| Varian | Entri |
|---|---|
| `create` | ✓ DU-208-13 |
| `bulk` | ✓ DU-208-14, DU-208-15 |
| `per-aksi-non-crud:Report Damaged` | ✓ DU-208-13 |
| `per-aksi-non-crud:Confirm` | ✓ DU-208-19 |
| `per-aksi-non-crud:Reject` | ✓ DU-208-20 |
| `per-aksi-non-crud:Cancel Report` | ✓ DU-208-21 |
| `per-aksi-non-crud:Mark as Repaired` | ✓ DU-208-22, DU-208-23 |
| `per-aksi-non-crud:Report Disposal` | ✓ DU-208-24 |
| `per-aksi-non-crud:Decline Report` | ✓ DU-208-25 |
| `per-aksi-non-crud:Cancel Disposal Report` | ✓ DU-208-26 |
| `per-varian-jalur:Registrasi aset ber-Condition Damaged` | ✓ DU-208-32 |
| `per-varian-jalur:Report Damaged di halaman Return Borrow` | ✓ DU-208-35 |
| `per-varian-jalur:Unassigned bermarker Damaged` | ✓ DU-208-36 |
| `per-varian-jalur:Report Condition (Stock Opname)` | ✓ DU-208-39 |
| `per-varian-jalur:Report Damaged saat Receive (Transfer)` | ✓ DU-208-40 |
| `per-varian-jalur:Mark as Found Damaged` | ✓ DU-208-42 |
| `per-varian-jalur:Event missing/` | ✓ DU-208-44 |
| `per-varian-jalur:Event Disposal` | ✓ DU-208-27 |
| `per-varian-jalur:Reject / Cancel / Remove / timeout baris Disposal` | ✓ DU-208-28 |
| `field-tanpa-teks` | ✓ DU-208-32 |
| `per-event:Reported damaged by` | ✓ DU-208-13 |
| `per-event:Report confirmed by` | ✓ DU-208-19 |
| `per-event:Report rejected by` | ✓ DU-208-20 |
| `per-event:Report canceled by` | ✓ DU-208-21 |
| `per-event:Asset reported missing` | ✓ DU-208-44 |
| `per-event:Asset found` | ✓ DU-208-42 |
| `per-event:Missing report closed` | ✓ DU-208-45 |
| `per-event:Marked as repaired by` | ✓ DU-208-22 |
| `per-event:Disposal reported by` | ✓ DU-208-24 |
| `per-event:Disposal report declined by` | ✓ DU-208-25 |
| `per-event:Disposal report canceled by` | ✓ DU-208-26 |
| `per-event:Disposed` | ✓ DU-208-27 |
| `edit-per-field` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `delete` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `per-baris-pencatatan` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `per-sub-konteks` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `field-sub-item` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `field-permission` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `field-badge-enum` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `nilai-awal` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `assign` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `remove` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `update-setelah-assign` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `approve-dari-approvals` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `reject-dari-approvals` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `settings-tanpa-nama` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `reset-ke-default` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `reset-sudah-default` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `event-sesi` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `nilai-kosong` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |
| `edit-multi-field` | — §8: Damage Log per peristiwa tanpa Old/New Value field; §9.6#p3 tidak ada form edit |

### tidak-dicatat@record · VD-L2

| Varian | Entri |
|---|---|
| `efek-samping-tanpa-log` | ✓ DU-208-41 |
| `record-lain-tak-terlibat` | ✓ DU-208-18 |
| `entri-entitas-lain` | ✓ DU-208-12 |
| `bulk-dengan-skip` | ✓ DU-208-16, DU-208-17 |
| `tanpa-perubahan` | — §9.6#p3: submit tanpa perubahan tidak terjadi |

### urutan-log@record · VD-L3

| Varian | Entri |
|---|---|
| `snapshot-setelah-rename` | ✓ DU-208-1 |
| `timestamp-sama` | ✓ DU-208-14 |
| `multi-entri-aktor-beda` | ✓ DU-208-2 |
| `edit-beruntun` | — §9.6#p3: tidak ada form edit |
| `edit-nama-sendiri` | — §9.6#p3: tidak ada form edit |
| `edit-beruntun-dua-aktor` | — §9.6#p3: tidak ada form edit |
| `record-tanpa-entri` | — S-DMG-15 (§7.1): Damage Log tidak pernah kosong |

### aktor-log@record · VD-L4

| Varian | Entri |
|---|---|
| `aktor-system` | ✓ DU-208-28, DU-208-44 |
| `aktor-beda-target` | ✓ DU-208-9 |
| `asal-modul-lain` | ✓ DU-208-3, DU-208-35 |
| `log-entitas-terkait` | ✓ DU-208-12 |

### jalur-non-form@record · VD-A8

| Varian | Entri |
|---|---|
| `per-jalur:Registrasi` | ✓ DU-208-32 |
| `per-jalur:Report Damaged di halaman Return Borrow` | ✓ DU-208-35 |
| `per-jalur:Unassigned bermarker Damaged` | ✓ DU-208-36 |
| `per-jalur:Report Condition (Stock Opname)` | ✓ DU-208-39 |
| `per-jalur:Report Damaged saat Receive` | ✓ DU-208-40 |
| `per-jalur:Mark as Found Damaged` | ✓ DU-208-42, DU-208-43 |
| `per-jalur:Event missing/` | ✓ DU-208-44 |
| `per-jalur:Event Disposal` | ✓ DU-208-27 |
| `dengan-aktor` | ✓ DU-208-27, DU-208-36 |
| `tanpa-aktor` | ✓ DU-208-28 |
| `pasangan-manual-setara` | ✓ DU-208-32 |
| `duplikat-dengan-data-ada` | ✓ DU-208-37 |
| `butuh-normalisasi` | — §9.2#b6: What happened dari registrasi dipakai apa adanya, tanpa normalisasi |
| `duplikat-dalam-batch` | — §8.3: tidak ada import batch |
| `import-semua-valid` | — §8.3: tidak ada Import |
| `import-sebagian-error` | — §8.3: tidak ada Import |

### asersi-negatif@record · VD-A14

| Varian | Entri |
|---|---|
| `terlibat` | ✓ DU-208-13 |
| `kontrol` | ✓ DU-208-18 |

### sync@record · VD-X1

| Varian | Entri |
|---|---|
| `konsumen-relasi` | ✓ DU-210-12 |
| `konsumen-snapshot` | ✓ DU-210-13 |
| `arah-a-ke-b` | ✓ DU-210-1 |
| `arah-b-ke-a` | ✓ DU-210-1 |
| `state-reflected` | ✓ DU-210-12 |
| `per-konsumen:asset-list/` | ✓ DU-210-49 |
| `per-konsumen:asset-detail/` | ✓ DU-210-24 |
| `per-konsumen:my-asset/` | ✓ DU-210-25 |
| `per-konsumen:borrow/` | ✓ DU-210-26 |
| `per-konsumen:assignment/` | ✓ DU-210-27 |
| `per-konsumen:missing/` | ✓ DU-210-28 |
| `per-konsumen:asset-registration/` | ✓ DU-210-29 |
| `per-konsumen:audit/` | ✓ DU-210-30 |
| `per-konsumen:disposal/` | ✓ DU-210-31 |
| `per-konsumen:transfer/` | ✓ DU-210-32 |
| `per-konsumen:settings-groups/` | ✓ DU-210-33 |
| `state-dari-modul-trigger` | ✓ DU-210-23 |
| `turunan` | ✓ DU-210-22 |
| `fk-create` | — Dependencies: modul ini bukan master data opsi dropdown (EB-XM-2 tidak berlaku) |
| `fk-edit` | — §11: modul bukan master data opsi dropdown |
| `fk-delete` | — §11: modul bukan master data opsi dropdown |
| `konsumen-sudah-ada` | — §11: modul bukan master data opsi dropdown |
| `per-konsekuensi-lifecycle` | — §9.2 "9.2.0": lifecycle record diuji target status-record@server |
| `propagasi-event` | — §9.7: Timing Sync, tanpa event eventual |

### nasib-dependen@group · VD-A11

| Varian | Entri |
|---|---|
| `punya-anak` | ✓ DU-210-11 |
| `tanpa-anak` | ✓ DU-210-10 |
| `linked-item` | — §6 V-DMG-11: penghapusan ditolak, tidak ada item tertaut yang bertahan |
| `pending-in-flight` | — §6 V-DMG-11: guard hanya record berjalan |
| `log-menunjuk` | — §6 V-DMG-11: guard hanya record berjalan |
| `assignment-luar-constraint` | — §6 V-DMG-11: bukan assignment |

### identitas@record · VD-P7

| Varian | Entri |
|---|---|
| `capability-dicabut-halaman-terbuka` | ✓ DU-210-2 |
| `email-diganti-token-lama` | — §9.4.1#r13: identitas yang berubah hanya pelapor dinonaktifkan |
| `password-diganti-sesi-aktif` | — §9.4.1#r13: hanya pelapor dinonaktifkan |
| `role-dicabut-sesi-aktif` | — EB-AKS-6: dimiliki varian capability-dicabut-halaman-terbuka |

### download@tabel-active · VD-D1

| Varian | Entri |
|---|---|
| `tanpa-saringan-lebih-satu-halaman` | ✓ DU-006-2, DU-006-3 |
| `hasil-tersaring` | ✓ DU-006-2 |
| `per-tab` | ✓ DU-006-4 |
| `nol-baris` | ✓ DU-006-7 |
| `urutan-sort-aktif` | ✓ DU-006-3 |
| `kolom-tersembunyi` | ✓ DU-006-3 |

### isi-berkas@download · VD-D2

| Varian | Entri |
|---|---|
| `kolom-foto` | ✓ DU-211-8 |
| `kolom-ikon` | ✓ DU-211-8 |
| `per-nilai-badge:Waiting for Confirmation` | ✓ DU-211-9 |
| `per-nilai-badge:Damaged` | ✓ DU-211-8 |
| `per-nilai-badge:Reported Disposal` | ✓ DU-211-10 |
| `per-nilai-badge:In Disposal Process` | ✓ DU-211-11 |
| `per-nilai-badge:Repaired` | ✓ DU-211-16 |
| `per-nilai-badge:Disposed` | ✓ DU-211-17 |
| `per-nilai-badge:Rejected` | ✓ DU-211-18 |
| `per-nilai-badge:Canceled` | ✓ DU-211-19 |
| `multi-badge` | ✓ DU-211-8 |
| `lebih-dua-badge` | ✓ DU-211-8 |
| `hierarki-penuh` | ✓ DU-211-8 |
| `leaf-sama-parent-beda` | ✓ DU-211-7 |
| `item-flat` | ✓ DU-211-8 |
| `nama-user-lengkap` | ✓ DU-211-8 |
| `numerik-terformat` | ✓ DU-211-8 |
| `mata-uang` | ✓ DU-211-8 |
| `nilai-kosong` | ✓ DU-211-8 |
| `switch-kedua-nilai` | — §4.1a: tidak ada kolom switch |
| `boolean-kedua-nilai` | — §4.1a: tidak ada kolom boolean |

### csv@download · VD-D3

| Varian | Entri |
|---|---|
| `nilai-koma` | ✓ DU-211-12 |
| `nilai-kutip` | ✓ DU-211-13 |
| `nilai-baris-baru` | ✓ DU-211-14 |
| `non-ascii` | ✓ DU-211-15 |

### ambang-download@tabel-active · VD-A13

| Varian | Entri |
|---|---|
| `di-bawah-ambang` | ✓ DU-211-8 |
| `tepat-ambang` | ✓ DU-211-20 |
| `lebih-ambang` | ✓ DU-211-21 |

### guided-tooltip@tab-damaged · VD-S3

| Varian | Entri |
|---|---|
| `flag-belum` | ✓ DU-023-1 |
| `flag-sudah` | ✓ DU-023-2 |
| `flag-sudah-device-lain` | ✓ DU-023-2 |

### setting-tanggal@tab-damaged · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-060-1 |
| `nilai-diubah` | ✓ DU-060-4 |
| `record-sebelum-perubahan` | ✓ DU-060-1 |
| `record-sesudah-perubahan` | ✓ DU-060-3 |
| `per-opsi-format-tanggal:dd/MM/yy` | ✓ DU-060-10 |
| `per-opsi-format-tanggal:M/d/yy` | ✓ DU-060-4 |
| `per-opsi-format-tanggal:dd MMM yy` | ✓ DU-060-5 |
| `per-opsi-format-tanggal:DDD, MMM dd, yy` | ✓ DU-060-6 |
| `per-opsi-format-tanggal:DDD, MMM dd, yyyy` | ✓ DU-060-7 |
| `zona-waktu-non-default` | ✓ DU-060-9 |
| `per-nilai-setting` | — prd-conventions.md §32: opsi format tanggal dimiliki varian per-opsi-format-tanggal |
| `format-regional-beda-entitas` | — §4.1#p4: format mengikuti General Settings satu entitas suite (IN-2) |

### search-by-scan@tabel-active · VD-F13

| Varian | Entri |
|---|---|
| `tag-belum-paired` | ✓ DU-026-7 |
| `tag-paired-aset` | ✓ DU-026-4 |
| `tag-tidak-terdaftar` | ✓ DU-026-11 |
| `per-jenis-tag:RFID` | ✓ DU-026-4 |
| `per-jenis-tag:QR` | ✓ DU-026-5 |
| `tag-paired-user-lain` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `tag-bukan-tagsamurai` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `object-tag` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `tag-company-lain` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `tag-belum-diaktivasi` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `tag-damaged` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `tag-missing` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `aset-on-tracking` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `aset-missing` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `group-found-sama` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |
| `group-found-beda` | — §4.1#p2: hasil pindai hanya mengisi Search dengan Asset ID; keadaan TAG lain mengikuti prd-conventions.md §9.6 dan dimiliki tag/ (bukan sumber) |

## Entri

- **DU-001-1** Damage record (awal), Record berjalan Waiting for Confirmation, Source Reported by holder: Name `Laptop Dell Latitude {runId} - 4` (32 kar), Asset ID `LPT-0004-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Reported Date `T0 − 1 hari, pukul 08:15` (24 kar), Days Damaged `1 day` (5 kar), Modified By `Budi S` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-2** Damage record (awal), Record berjalan In Disposal Process, Source Manual: Name `Monitor Dell P2422H {runId} - 6` (31 kar), Asset ID `MON-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 52 hari, pukul 14:20` (25 kar), Days Damaged `52 days` (7 kar), Modified By `Rina W` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-3** Damage record (awal), Record berjalan Reported Disposal, Source Stock opname: Name `Printer HP LaserJet M404 {runId} - 8` (36 kar), Asset ID `PRN-0008-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 27 hari, pukul 10:00` (25 kar), Days Damaged `27 days` (7 kar), Modified By `Agus P` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-4** Damage record (awal), Record berjalan Damaged dengan penanda Reported Missing, Source Manual: Name `Drill Bosch GSB {runId} - 6` (27 kar), Asset ID `DRL-0006-{runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 14 hari, pukul 10:00` (25 kar), Days Damaged `14 days` (7 kar), Modified By `System` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-5** Damage record (awal), Record berjalan Damaged dengan penanda Missing, Source Manual: Name `Camera Canon EOS {runId} - 3` (28 kar), Asset ID `CAM-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 8 hari, pukul 11:00` (24 kar), Days Damaged `8 days` (6 kar), Modified By `System` (6 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-6** Damage record (awal), Record berjalan Damaged, Source Borrow return: Name `Projector Epson EB-X06 {runId} - 2` (34 kar), Asset ID `PRJ-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Borrow return` (13 kar), Last Holder `Sari D` (6 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 7 hari, pukul 17:10` (24 kar), Days Damaged `7 days` (6 kar), Modified By `Rina W` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-7** Damage record (awal), Record berjalan Damaged, Source Reported by scan: Name `Office Chair Ergo {runId} - 31` (30 kar), Asset ID `CHR-0031-{runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Reported by scan` (16 kar), Last Holder `—` (1 kar), Reported By `Dedi K` (6 kar), Reported Date `T0 − 5 hari, pukul 13:00` (24 kar), Days Damaged `5 days` (6 kar), Modified By `Dedi K` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-8** Damage record (awal), Record berjalan Damaged, Source Missing asset: Name `Laptop Dell Latitude {runId} - 6` (32 kar), Asset ID `LPT-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Missing asset` (13 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 2 hari, pukul 15:20` (24 kar), Days Damaged `2 days` (6 kar), Modified By `Rina W` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-9** Damage record (awal), Record berjalan Damaged, Source Registration: Name `Projector Epson EB-X06 {runId} - 7` (34 kar), Asset ID `PRJ-0007-{runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Registration` (12 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 3 hari, pukul 09:00` (24 kar), Days Damaged `3 days` (6 kar), Modified By `Rina W` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-10** Damage record (awal), Record berjalan Damaged, Source Transfer receive: Name `Forklift Toyota 8FD {runId} - 1` (31 kar), Asset ID `FLT-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Transfer receive` (16 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 6 hari, pukul 14:00` (24 kar), Days Damaged `6 days` (6 kar), Modified By `Agus P` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-001-11** Damage record (awal), Record selesai Repaired yang tidak boleh tampil di sub-tab Active: Name `Projector Epson EB-X06 {runId} - 5` (34 kar), Asset ID `PRJ-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Registration` (12 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 3 hari, pukul 09:00` (24 kar), Resolved Date `T0 − 1 hari, pukul 13:45` (24 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-001-12** Damage record (awal), Record Waiting for Confirmation yang dilaporkan aktor sendiri: Name `Scanner Fujitsu fi-7160 {runId} - 2` (35 kar), Asset ID `SCN-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Admin T` (7 kar), Reported By `Admin T` (7 kar), Reported Date `T0 − 2 hari, pukul 10:30` (24 kar), Days Damaged `2 days` (6 kar), Modified By `Admin T` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-1** Damage record (awal), Record berjalan Damaged: Name `Delta {runId} Genset - 1` (24 kar), Asset ID `GEN-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), TAG `RFID` (4 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-2** Damage record (awal), Record berjalan Waiting for Confirmation: Name `Valve Aura {runId} - 2` (22 kar), Asset ID `VLV-0002-{runId}` (16 kar), Group `Delta {runId}` (13 kar), Status `Waiting for Confirmation` (24 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-3** Damage record (awal), Record berjalan Reported Disposal: Name `Valve A {runId} - 1` (19 kar), Asset ID `VLV-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-4** Damage record (awal), Record berjalan In Disposal Process: Name `Valve A {runId} - 12` (20 kar), Asset ID `VLV-0012-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-5** Damage record (awal), Record berjalan Damaged: Name `Panel 100% {runId} - 3` (22 kar), Asset ID `PNL-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-6** Damage record (awal), Record berjalan Damaged: Name `Panel 1005 {runId} - 4` (22 kar), Asset ID `PNL-0004-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-7** Damage record (awal), Record berjalan Damaged: Name `<b>Finance</b> {runId} - 5` (26 kar), Asset ID `FIN-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), TAG `—` (1 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-002-8** Search query (dicoba), Kata kunci Search 'Valve Aura {runId}': Search `Valve Aura {runId}` (18 kar) · sumber EB-SRC-1
- **DU-002-9** Search query (dicoba), Kata kunci Search 'ura {runId}': Search `ura {runId}` (11 kar) · sumber EB-SRC-1
- **DU-002-10** Search query (dicoba), Kata kunci Search 'VALVE AURA {runId}': Search `VALVE AURA {runId}` (18 kar) · sumber EB-SRC-1
- **DU-002-11** Search query (dicoba), Kata kunci Search 'Reported Disposal': Search `Reported Disposal` (17 kar) · sumber EB-SRC-1
- **DU-002-12** Search query (dicoba), Kata kunci Search ' Valve Aura {runId} ': Search ` Valve Aura {runId} ` (20 kar) · sumber EB-SRC-1
- **DU-002-13** Search query (dicoba), Kata kunci Search 'Valve A {runId} - 1': Search `Valve A {runId} - 1` (19 kar) · sumber EB-SRC-1
- **DU-002-14** Search query (dicoba), Kata kunci Search 'Delta Genset': Search `Delta Genset` (12 kar) · sumber EB-SRC-1
- **DU-002-15** Search query (dicoba), Kata kunci Search '100%': Search `100%` (4 kar) · sumber EB-SRC-1
- **DU-002-16** Search query (dicoba), Kata kunci Search '<script>alert(1)</script>': Search `<script>alert(1)</script>` (25 kar) · sumber EB-SRC-1
- **DU-002-17** Search query (dicoba), Kata kunci Search "' OR '1'='1": Search `' OR '1'='1` (11 kar) · sumber EB-SRC-1
- **DU-002-18** Search query (dicoba), Kata kunci Search '{"$ne": null}': Search `{"$ne": null}` (13 kar) · sumber EB-SRC-1
- **DU-002-19** Search query (dicoba), Kata kunci Search '<b>Finance</b>': Search `<b>Finance</b>` (14 kar) · sumber EB-SRC-1
- **DU-002-20** Search query (dicoba), Kata kunci Search 'Tidak Ada Hasil {runId}': Search `Tidak Ada Hasil {runId}` (23 kar) · sumber EB-SRC-1
- **DU-002-21** Search query (dicoba), Kata kunci Search '10:00', jam pada kolom tanggal Reported Date: Search `10:00` (5 kar) · sumber EB-SRC-1
- **DU-002-22** Search query (dicoba), Kata kunci Search 'RFID': Search `RFID` (4 kar) · sumber EB-SRC-1
- **DU-002-23** Search query (dicoba), Kata kunci Search 'Head Office {runId}': Search `Head Office {runId}` (19 kar) · sumber EB-SRC-1
- **DU-002-24** Search query (dicoba), Kata kunci Search 'Delta {runId}': Search `Delta {runId}` (13 kar) · sumber EB-SRC-1
- **DU-002-25** Search query (dicoba), Kata kunci Search '   ': Search `   ` (3 kar) · sumber EB-SRC-1
- **DU-003-1** Damage record (awal), Record berjalan Damaged: Name `anggur {runId} - 1` (18 kar), Asset ID `SRT-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 4 hari, pukul 10:00` (24 kar), Days Damaged `4 days` (6 kar), TAG `RFID` (4 kar), Asset Value (Commercial) `800000` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-2** Damage record (awal), Record berjalan Damaged: Name `Apel {runId} - 1` (16 kar), Asset ID `SRT-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 6 hari, pukul 10:00` (24 kar), Days Damaged `6 days` (6 kar), Last Holder (nama lengkap) `Sari Dewanti` (12 kar), TAG `QR` (2 kar), Asset Value (Commercial) `2500000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-3** Damage record (awal), Record berjalan Waiting for Confirmation: Name `Crate {runId} - 1` (17 kar), Asset ID `SRT-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 9 hari, pukul 10:00` (24 kar), Days Damaged `9 days` (6 kar), TAG `NFC` (3 kar), Asset Value (Commercial) `12000000` (8 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-4** Damage record (awal), Record berjalan Reported Disposal: Name `Crate {runId} - 2` (17 kar), Asset ID `SRT-0004-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Last Holder `Dewi A` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 12 hari, pukul 10:00` (25 kar), Days Damaged `12 days` (7 kar), Last Holder (nama lengkap) `Dewi Anggraini` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-5** Damage record (awal), Record berjalan In Disposal Process: Name `Crate {runId} - 10` (18 kar), Asset ID `SRT-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 15 hari, pukul 10:00` (25 kar), Days Damaged `15 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-6** Damage record (awal), Record berjalan Damaged: Name `Elan {runId} - 1` (16 kar), Asset ID `SRT-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Budi S` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 5 hari, pukul 10:00` (24 kar), Days Damaged `5 days` (6 kar), Last Holder (nama lengkap) `Budi Santoso` (12 kar), Labels `Aset Kritis {runId}` (19 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-7** Damage record (awal), Record berjalan Damaged: Name `Élan {runId} - 1` (16 kar), Asset ID `SRT-0007-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 7 hari, pukul 10:00` (24 kar), Days Damaged `7 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-8** Damage record (awal), Record berjalan Damaged: Name `Ezra {runId} - 1` (16 kar), Asset ID `SRT-0008-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 8 hari, pukul 10:00` (24 kar), Days Damaged `8 days` (6 kar), Last Holder (nama lengkap) `Sari Dewanti` (12 kar), Labels `Operasional {runId}` (19 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-9** Damage record (awal), Record berjalan Damaged: Name `3D Printer {runId} - 1` (22 kar), Asset ID `SRT-0009-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 10 hari, pukul 10:00` (25 kar), Days Damaged `10 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-10** Damage record (awal), Record berjalan Damaged: Name `#Gudang {runId} - 1` (19 kar), Asset ID `SRT-0010-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi A` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 11 hari, pukul 10:00` (25 kar), Days Damaged `11 days` (7 kar), Last Holder (nama lengkap) `Dewi Anggraini` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-11** Damage record (awal), Record berjalan Damaged: Name `Zulu {runId} - 1` (16 kar), Asset ID `SRT-0011-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Budi H` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 13 hari, pukul 09:00` (25 kar), Days Damaged `13 days` (7 kar), Last Holder (nama lengkap) `Budi Hartono` (12 kar), Labels `Aset Kritis {runId}` (19 kar), Last Updated `sama dengan Reported Date` (25 kar), Labels (kedua) `Gudang {runId}` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-12** Damage record (awal), Record berjalan Damaged: Name `Zulu {runId} - 2` (16 kar), Asset ID `SRT-0012-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 13 hari, pukul 09:30` (25 kar), Days Damaged `13 days` (7 kar), Last Holder (nama lengkap) `Sari Dewanti` (12 kar), Labels `Aset Kritis {runId}` (19 kar), Last Updated `sama dengan Reported Date` (25 kar), Labels (kedua) `Gudang {runId}` (14 kar), Labels (ketiga) `Operasional {runId}` (19 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-003-13** Search query (dicoba), Kata kunci Search 'Zulu {runId}' untuk menyempitkan ke dua record Last Updated sama dengan Reported Date: Search `Zulu {runId}` (12 kar) · sumber turunan penulis
- **DU-004-1** Damage record (awal), Record berjalan Damaged, Source Manual: Name `Filter Aset {runId} - 1` (23 kar), Asset ID `FLT-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 11:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-2** Damage record (awal), Record berjalan Damaged, Source Reported by scan: Name `Filter Aset {runId} - 2` (23 kar), Asset ID `FLT-0002-{runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Reported by scan` (16 kar), Last Holder `—` (1 kar), Reported By `Dedi K` (6 kar), Reported Date `T0 − 6 hari, pukul 11:00` (24 kar), Days Damaged `6 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-3** Damage record (awal), Record berjalan Waiting for Confirmation, Source Reported by holder: Name `Filter Aset {runId} - 3` (23 kar), Asset ID `FLT-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `—` (1 kar), Reported By `Budi S` (6 kar), Reported Date `T0 − 10 hari, pukul 11:00` (25 kar), Days Damaged `10 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-4** Damage record (awal), Record berjalan Reported Disposal, Source Stock opname: Name `Filter Aset {runId} - 4` (23 kar), Asset ID `FLT-0004-{runId}` (16 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 14 hari, pukul 11:00` (25 kar), Days Damaged `14 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-5** Damage record (awal), Record berjalan In Disposal Process, Source Manual: Name `Filter Aset {runId} - 5` (23 kar), Asset ID `FLT-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 20 hari, pukul 11:00` (25 kar), Days Damaged `20 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-6** Damage record (awal), Record berjalan Damaged berpenanda Reported Missing, Source Manual: Name `Filter Aset {runId} - 6` (23 kar), Asset ID `FLT-0006-{runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 5 hari, pukul 11:00` (24 kar), Days Damaged `5 days` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-7** Damage record (awal), Record berjalan Damaged berpenanda Missing, Source Borrow return: Name `Filter Aset {runId} - 7` (23 kar), Asset ID `FLT-0007-{runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Borrow return` (13 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 8 hari, pukul 11:00` (24 kar), Days Damaged `8 days` (6 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-8** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-004-tabel-active-filter), Record berjalan Damaged, Source Assign return: Name `Filter Aset {runId} - 8` (23 kar), Asset ID `FLT-0008-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Assign return` (13 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 10 hari, pukul 11:00` (25 kar), Days Damaged `10 days` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-9** Damage record (awal), Record selesai Repaired yang hanya ada di sub-tab History: Name `Filter Aset {runId} - 9` (23 kar), Asset ID `FLT-0009-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 12 hari, pukul 11:00` (25 kar), Resolved Date `T0 − 11 hari, pukul 11:00` (25 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-10** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-004-tabel-active-filter), Aset Normal tanpa record berjalan yang akan dilaporkan rusak oleh Admin B: Name `Filter Aset {runId} - 10` (24 kar), Asset ID `FLT-0010-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status asset `Normal` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-004-11** Damage record (dibuat), Isian laporan Report Damaged oleh Admin B atas aset DU-004-10: What happened `Layar retak terbentur` (21 kar), Damaged Photo `foto-layar-retak.jpg` (20 kar), Reported By `Bima A` (6 kar) · sumber turunan penulis
- **DU-004-12** Damage record (dibuat), Isian Mark as Repaired oleh Admin B atas aset DU-004-8: Repair note `Unit sudah diganti` (18 kar), Aset `Filter Aset {runId} - 8` (23 kar) · sumber turunan penulis
- **DU-004-14** Filter input (dicoba), Rentang Reported Date di dalam data, tepat pada batas awal dan akhir: Dari `T0 − 8 hari` (11 kar), Sampai `T0 − 5 hari` (11 kar) · sumber PRD §4.1a T-DMG-01
- **DU-004-15** Filter input (dicoba), Rentang Reported Date di luar semua data: Dari `T0 − 30 hari` (12 kar), Sampai `T0 − 25 hari` (12 kar) · sumber PRD §4.1a T-DMG-01
- **DU-004-16** Filter input (dicoba), Rentang Days Damaged dengan Min tepat pada nilai terkecil: Min `14` (2 kar), Max `5` (1 kar) · sumber PRD §4.1a T-DMG-01
- **DU-004-17** Filter input (dicoba), Kata kunci pencarian di dalam dropdown Source: huruf kecil, huruf besar, tanpa hasil: cari1 `scan` (4 kar), cari2 `STOCK` (5 kar), cari3 `Tidak Ada` (9 kar) · sumber PRD §4.1a T-DMG-01
- **DU-004-18** User (awal), User master yang tidak pernah melapor: Name tampil `Gita P` (6 kar) · sumber PRD §4.1a T-DMG-01
- **DU-004-13** User (awal), Aktor kedua Admin B, Total Control: Name tampil `Bima A` (6 kar), Role `Total Control` (13 kar) · sumber matriks role PRD
- **DU-005-1** Damage record (awal; 10 record), Sepuluh record berstatus Reported Disposal di Group Head Office: Name `Paginasi Aset {runId} - {n}` (27 kar), Asset ID `PGN-1{n}-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 5 hari, pukul 10:00` (24 kar), Days Damaged `5 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-005-2** Damage record (awal; 16 record), Enam belas record berstatus Damaged di Group Warehouse: Name `Paginasi Aset {runId} - {n}` (27 kar), Asset ID `PGN-2{n}-{runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 6 hari, pukul 10:00` (24 kar), Days Damaged `6 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-005-3** Konfigurasi kolom (dicoba), Kolom yang diubah lewat Setup Column dan Column Visibility: Disembunyikan `Source` (6 kar), Ditambahkan `Brand` (5 kar), Disembunyikan lewat panel cepat `Last Holder` (11 kar) · sumber PRD §4.1a T-DMG-01
- **DU-005-4** Search query (dicoba), Kata kunci Search 'Paginasi Aset {runId}' yang dijalankan dari halaman 2: Search `Paginasi Aset {runId}` (21 kar) · sumber PRD §9.5 Pagination (prd-conventions.md §9.11)
- **DU-006-1** Entitas (awal), Entitas khusus yang hanya dipakai spec ini: Name `Entitas Download {runId}` (24 kar) · sumber PRD §5 Global Table Rules
- **DU-006-2** Damage record (awal; 4 record), Empat record Waiting for Confirmation di entitas khusus: Name `Unduh Waiting {runId} - {n}` (27 kar), Asset ID `UNW-{n}-{runId}` (15 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 2 hari, pukul 10:00` (24 kar), Days Damaged `2 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-006-3** Damage record (awal; 8 record), Delapan record Damaged di entitas khusus: Name `Unduh Damaged {runId} - {n}` (27 kar), Asset ID `UND-{n}-{runId}` (15 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 4 hari, pukul 10:00` (24 kar), Days Damaged `4 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-006-4** Damage record (awal), Record selesai Repaired di sub-tab History: Name `Unduh Selesai {runId} - 1` (25 kar), Asset ID `UNS-1-{runId}` (13 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 9 hari, pukul 10:00` (24 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 7 hari, pukul 10:00` (24 kar), Duration `2 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-006-5** Damage record (awal), Record selesai Rejected di sub-tab History: Name `Unduh Selesai {runId} - 2` (25 kar), Asset ID `UNS-2-{runId}` (13 kar), Group `Head Office {runId}` (19 kar), Status `Rejected` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 9 hari, pukul 10:00` (24 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 7 hari, pukul 10:00` (24 kar), Duration `2 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-006-6** Damage record (awal), Record selesai Canceled di sub-tab History: Name `Unduh Selesai {runId} - 3` (25 kar), Asset ID `UNS-3-{runId}` (13 kar), Group `Head Office {runId}` (19 kar), Status `Canceled` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 9 hari, pukul 10:00` (24 kar), Resolved By `Dewi A` (6 kar), Resolved Date `T0 − 7 hari, pukul 10:00` (24 kar), Duration `2 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-006-7** Download (dicoba), Kata kunci Search tanpa hasil untuk berkas nol baris: Search `Tidak Ada Hasil {runId}` (23 kar) · sumber PRD §5 Global Table Rules
- **DU-007-1** Damage record (awal), Record selesai Repaired di sub-tab History: Name `Riwayat Aset {runId} - 1` (24 kar), Asset ID `RWY-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Borrow return` (13 kar), Last Holder `Sari D` (6 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 20 hari, pukul 09:00` (25 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 14 hari, pukul 14:10` (25 kar), Duration `6 days` (6 kar), Category `Elektronik {runId}` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-007-2** Damage record (awal), Record selesai Disposed di sub-tab History: Name `Riwayat Aset {runId} - 2` (24 kar), Asset ID `RWY-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Disposed` (8 kar), Source `Stock opname` (12 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 30 hari, pukul 08:00` (25 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 10 hari, pukul 00:30` (25 kar), Duration `20 days` (7 kar), Category `Elektronik {runId}` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-007-3** Damage record (awal), Record selesai Rejected di sub-tab History: Name `Riwayat Aset {runId} - 3` (24 kar), Asset ID `RWY-0003-{runId}` (16 kar), Group `Cabang Lama {runId}` (19 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Reported Date `T0 − 8 hari, pukul 08:30` (24 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 7 hari, pukul 09:15` (24 kar), Duration `1 day` (5 kar), Category `Peralatan Lama {runId}` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-007-4** Damage record (awal), Record selesai Canceled di sub-tab History: Name `Riwayat Aset {runId} - 4` (24 kar), Asset ID `RWY-0004-{runId}` (16 kar), Group `Gudang Lama {runId}` (19 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Dewi A` (6 kar), Reported By `Dewi A` (6 kar), Reported Date `T0 − 5 hari, pukul 10:00` (24 kar), Resolved By `Dewi A` (6 kar), Resolved Date `T0 − 4 hari, pukul 08:00` (24 kar), Duration `1 day` (5 kar), Category `Mebel Lama {runId}` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-007-5** Damage record (awal), Record berjalan Damaged yang tidak boleh tampil di sub-tab History: Name `Riwayat Aset {runId} - 5` (24 kar), Asset ID `RWY-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar), Days Damaged `3 days` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-007-6** Group (awal), Group yang sudah dihapus dan diganti nama sebelum spec mulai: Group dihapus `Cabang Lama {runId}` (19 kar), Group diganti nama `Gudang Lama {runId}` (19 kar), Nama Group sekarang `Gudang Baru {runId}` (19 kar) · sumber PRD §4.1b T-DMG-02 Setup Column
- **DU-007-7** Search query (dicoba), Kata kunci Search tanpa hasil: Search `Tidak Ada Hasil {runId}` (23 kar) · sumber PRD §7.1
- **DU-007-8** Damage record (awal), Record selesai Repaired untuk aset yang punya dua record selesai: Name `Riwayat Aset {runId} - 6` (24 kar), Asset ID `RWY-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Category `Elektronik {runId}` (18 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 41 hari, pukul 08:00` (25 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 38 hari, pukul 16:20` (25 kar), Duration `3 days` (6 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-007-9** Damage record (awal), Record selesai Canceled untuk aset yang sama dengan DU-007-8: Name `Riwayat Aset {runId} - 6` (24 kar), Asset ID `RWY-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Category `Elektronik {runId}` (18 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Dewi A` (6 kar), Reported By `Dewi A` (6 kar), Reported Date `T0 − 36 hari, pukul 09:00` (25 kar), Resolved By `Dewi A` (6 kar), Resolved Date `T0 − 35 hari, pukul 11:30` (25 kar), Duration `1 day` (5 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-007-10** Category (awal), Category yang sudah dihapus dan diganti nama sebelum spec mulai: Category dihapus `Peralatan Lama {runId}` (22 kar), Category diganti nama `Mebel Lama {runId}` (18 kar), Nama Category sekarang `Mebel Baru {runId}` (18 kar) · sumber PRD §4.1b T-DMG-02 Setup Column
- **DU-007-11** Filter input (dicoba), Rentang Resolved Date dan rentang Duration Min dan Max pada sub-tab History: Dari `T0 − 14 hari` (12 kar), Sampai `T0 − 10 hari` (12 kar), Min `2` (1 kar), Max `1` (1 kar) · sumber PRD §4.1b T-DMG-02
- **DU-008-1** Damage record (awal), Record Damaged dengan 6 node Damage Log: Name `Log Aset {runId} - 1` (20 kar), Asset ID `LOG-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 10 hari, pukul 09:00` (25 kar), What happened `<script>alert(1)</script>` (25 kar), Node 1 `Reported damaged by Rina W` (26 kar), Node 2 `Disposal reported by Rina W` (27 kar), Node 3 `Disposal report declined by Agus P` (34 kar), Node 4 `Disposal reported by Rina W` (27 kar), Node 5 `Disposal report canceled by Rina W` (34 kar), Node 6 `Asset reported missing` (22 kar), Penanda `Missing` (7 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-2** Damage record (awal), Record Damaged dengan 2 node Damage Log: Name `Log Aset {runId} - 2` (20 kar), Asset ID `LOG-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Reported Date `T0 − 5 hari, pukul 09:00` (24 kar), What happened `' OR '1'='1` (11 kar), Node 1 `Reported damaged by Budi S` (26 kar), Node 2 `Report confirmed by Rina W` (26 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-3** Damage record (awal), Record Rejected dengan 2 node Damage Log: Name `Log Aset {runId} - 3` (20 kar), Asset ID `LOG-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Tono R` (6 kar), Reported By `Sinta M on behalf of Tono R` (27 kar), Reported Date `T0 − 12 hari, pukul 09:00` (25 kar), What happened `{"$ne": null}` (13 kar), Node 1 `Reported damaged by Sinta M on behalf of Tono R` (47 kar), Node 2 `Report rejected by Rina W` (25 kar), Resolved Date `T0 − 2 hari, pukul 16:00` (24 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-4** Damage record (awal), Record Canceled dengan 2 node Damage Log: Name `Log Aset {runId} - 4` (20 kar), Asset ID `LOG-0004-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Dewi A` (6 kar), Reported By `Dewi A` (6 kar), Reported Date `T0 − 9 hari, pukul 09:00` (24 kar), What happened `<b>Finance</b>` (14 kar), Node 1 `Reported damaged by Dewi A` (26 kar), Node 2 `Report canceled by Dewi A` (25 kar), Resolved Date `T0 − 4 hari, pukul 16:00` (24 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-5** Damage record (awal), Record Repaired dengan 2 node Damage Log: Name `Log Aset {runId} - 5` (20 kar), Asset ID `LOG-0005-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 14 hari, pukul 09:00` (25 kar), What happened `Layar tidak menyala` (19 kar), Node 1 `Reported damaged by Agus P` (26 kar), Node 2 `Marked as repaired by Rina W` (28 kar), Resolved Date `T0 − 6 hari, pukul 16:00` (24 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-6** Damage record (awal), Record Disposed dengan 3 node Damage Log: Name `Log Aset {runId} - 6` (20 kar), Asset ID `LOG-0006-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Disposed` (8 kar), Source `Registration` (12 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 20 hari, pukul 09:00` (25 kar), What happened `Casing retak saat registrasi` (28 kar), Node 1 `Reported damaged by Rina W` (26 kar), Node 2 `Disposal reported by Rina W` (27 kar), Node 3 `Disposed` (8 kar), Resolved Date `T0 − 9 hari, pukul 16:00` (24 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-7** Damage record (awal), Record Damaged dengan 5 node Damage Log: Name `Log Aset {runId} - 7` (20 kar), Asset ID `LOG-0007-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 8 hari, pukul 09:00` (24 kar), What happened `Kipas mati total` (16 kar), Node 1 `Reported damaged by Agus P` (26 kar), Node 2 `Asset reported missing` (22 kar), Node 3 `Missing report closed` (21 kar), Node 4 `Asset reported missing` (22 kar), Node 5 `Asset found` (11 kar), Damaged Photo `foto-kerusakan.jpg` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-008-8** Damage log node (awal), Detail node disposal, penolakan, dan perbaikan pada record DU-008: Reason Disposal `Sudah tidak ekonomis` (20 kar), Reason Decline `Masih bisa diperbaiki` (21 kar), Reason Reject `Foto tidak menunjukkan kerusakan` (32 kar), Repair note `Layar diganti` (13 kar), Report ID `milik laporan disposal DU-008-1 dan DU-008-6` (44 kar), Disposal No. `milik DU-008-6` (14 kar) · sumber PRD §8.1
- **DU-009-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-009-review-confirm), Laporan pemegang Waiting for Confirmation yang akan di-Confirm: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar), What happened `Layar laptop retak setelah terjatuh dari meja kerja` (51 kar) · sumber turunan penulis
- **DU-009-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-009-review-confirm), Laporan Waiting for Confirmation yang pelapornya kini Aktor Damaged (aktor spec ini): Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar), What happened `Cartridge printer bocor dan hasil cetak bergaris` (48 kar) · sumber turunan penulis
- **DU-009-3** User (awal), Pemegang aset yang melapor sebagai pelapor umum: Name `Budi Santoso {runId}` (20 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-009-4** User (awal), Aktor spec ini, Total Control yang pernah melapor sebagai pelapor umum: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-010-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-010-review-reject), Laporan pemegang Waiting for Confirmation yang akan di-Reject: Asset Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar), What happened `Lensa kamera berembun dan gambar tidak fokus` (44 kar) · sumber turunan penulis
- **DU-010-2** Reason Reject Report (dibuat), Alasan penolakan laporan yang diketik di dialog Reject Report: Reason `Foto kerusakan berbeda dari aset yang dilaporkan` (48 kar) · sumber turunan penulis
- **DU-010-3** User (awal), Pemegang aset yang melapor sebagai pelapor umum: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-010-4** User (awal), Aktor spec ini, Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-011-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-011-mark-as-repaired), Record Damaged aset tanpa TAG yang di-Mark as Repaired: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Reported By `Agus Pratama {runId}` (20 kar), What happened `Lampu proyektor mati dan gambar tidak muncul` (44 kar) · sumber turunan penulis
- **DU-011-2** Input Mark as Repaired (dibuat), Isian dialog Mark as Repaired: Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal` (59 kar), After photo `proyektor-setelah-diperbaiki.jpg` (32 kar) · sumber turunan penulis
- **DU-011-3** Damage record (awal), Record Damaged berpenanda Missing, tidak ikut jumlah badge: Asset Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-011-4** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-011-5** Damage record (awal), Record In Disposal Process: Asset Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-011-6** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-012-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-012-mark-as-repaired-scan-tag), Record Damaged aset ber-TAG RFID yang di-Mark as Repaired: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `RFID` (4 kar), Reported By `Agus Pratama {runId}` (20 kar), What happened `Layar laptop retak dan menampilkan garis` (40 kar) · sumber turunan penulis
- **DU-012-2** Damage record (awal), Record Damaged aset ber-TAG QR, hanya dipindai: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `QR` (2 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-012-3** Damage record (awal), Record Damaged aset ber-TAG NFC, hanya dipindai: Asset Name `Handheld Scanner Zebra TC21 {runId}` (35 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `NFC` (3 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-012-4** TAG (awal), TAG fisik yang dipindai: Kode TAG `RFID-{runId}-A` (14 kar), Tipe `RFID` (4 kar), Terpasang pada `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber turunan penulis
- **DU-012-5** TAG (awal), TAG fisik yang dipindai: Kode TAG `QR-{runId}-B` (12 kar), Tipe `QR` (2 kar), Terpasang pada `Tablet Samsung Tab A8 {runId}` (29 kar) · sumber turunan penulis
- **DU-012-6** TAG (awal), TAG fisik yang dipindai: Kode TAG `NFC-{runId}-C` (13 kar), Tipe `NFC` (3 kar), Terpasang pada `Handheld Scanner Zebra TC21 {runId}` (35 kar) · sumber turunan penulis
- **DU-012-7** TAG (awal), TAG fisik yang dipindai: Kode TAG `RFID-{runId}-U` (14 kar), Tipe `RFID` (4 kar), Terpasang pada `User Sinta Maharani {runId}` (27 kar) · sumber turunan penulis
- **DU-012-8** User (awal), Pemegang TAG yang bukan aset: Name `Sinta Maharani {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-012-9** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-012-10** Input Mark as Repaired (dibuat), Repair note yang diketik: Repair note `Layar laptop diganti baru dan unit sudah diuji menyala normal` (61 kar) · sumber turunan penulis
- **DU-013-1** Damage record (awal; 12 record), 12 record Damaged satu Group untuk seleksi lintas halaman: Asset Name `Monitor Dell P2422H {n} {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-2** Damage record (awal), Record Waiting for Confirmation, checkbox Disabled: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Warehouse {runId}` (17 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-013-3** Damage record (awal), Record Reported Disposal, checkbox Disabled: Asset Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Warehouse {runId}` (17 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-4** Damage record (awal), Record In Disposal Process, checkbox Disabled: Asset Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Warehouse {runId}` (17 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-5** Damage record (awal), Record Damaged berpenanda Missing, checkbox Disabled: Asset Name `Camera Canon EOS {runId}` (24 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-6** Damage record (awal), Record Damaged berpenanda Reported Missing, checkbox Disabled: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Penanda `Reported Missing` (16 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-7** Damage record (awal), Record Damaged di Group kedua untuk seleksi lintas Group: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-8** Group (awal), Group pertama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-013-9** Group (awal), Group kedua: Name `Warehouse {runId}` (17 kar) · sumber turunan penulis
- **DU-013-10** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-013-11** User (awal), Pelapor record Waiting for Confirmation: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-013-12** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-013-bulk-seleksi-lintas-group), Record Damaged di Warehouse yang dipilih lalu berubah menjadi Reported Disposal oleh Admin B sebelum klik bulk: Asset Name `Generator Honda EU20i {runId}` (29 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-013-13** User (awal), Admin B, aktor lain yang hanya memicu perubahan state: Name `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-013-14** Reason Report Disposal (dibuat), Alasan Report Disposal yang diketik Admin B atas record DU-013-12: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain` (48 kar) · sumber turunan penulis
- **DU-014-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-014-gating-total-control), Laporan Waiting yang di-Confirm: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-014-2** Damage record (awal), Record Damaged di Group lain: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-014-3** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-014-4** Damage record (awal), Record Damaged: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-014-5** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-014-6** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-014-7** Group (awal), Group pertama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-014-8** Group (awal), Group kedua: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-014-9** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-014-10** User (awal), Pelapor record Waiting for Confirmation: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-014-11** Damage record (awal), Record Reported Disposal yang dilaporkan aktor lain: Asset Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Reported By `Hendra Kusuma {runId}` (21 kar) · sumber turunan penulis
- **DU-014-12** User (awal), Aktor lain pelapor Reported Disposal: Name `Hendra Kusuma {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-015-1** Damage record (awal), Laporan Waiting di Group binaan: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-015-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-015-gating-group-manager), Record Damaged di sub-group yang di-Mark as Repaired: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Sub Head Office {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-015-3** Damage record (awal), Record Reported Disposal di Group binaan: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-015-4** Damage record (awal), Record Damaged di luar Group binaan: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-015-5** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-015-6** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-015-7** Group (awal), Group binaan: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-015-8** Group (awal), Sub-group dari Group binaan: Name `Sub Head Office {runId}` (23 kar), Induk `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-015-9** Group (awal), Group di luar binaan: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-015-10** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Group Manager (Group binaan Head Office {runId}, tanpa Manage accounting)` (73 kar), Cakupan `Group binaan beserta sub-group` (30 kar) · sumber matriks role PRD
- **DU-015-11** User (awal), Pelapor record Waiting for Confirmation: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-015-12** Input Mark as Repaired (dibuat), Repair note yang diketik: Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal` (59 kar) · sumber turunan penulis
- **DU-015-13** Damage record (awal), Record Reported Disposal di luar Group binaan: Asset Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-016-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-016-gating-manage-asset-tag-update), Laporan Waiting yang di-Confirm: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-016-2** Damage record (awal), Record Damaged di descendant: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Sub Head Office {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-016-3** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-016-4** Damage record (awal), Record Damaged di Group Read: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-016-5** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-016-6** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-016-7** Damage record (awal), Laporan Waiting untuk uji pencabutan capability: Asset Name `Handheld Scanner Zebra TC21 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-016-8** Group (awal), Group Update: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-016-9** Group (awal), Descendant Group Update: Name `Sub Head Office {runId}` (23 kar), Induk `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-016-10** Group (awal), Group Read: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-016-11** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Manage asset & TAG (Update pada Head Office {runId}, Read pada Branch Surabaya {runId}; tanpa Manage accounting dan tanpa Asset Admin sub-tab Disposal; pencabutan di akhir spec hanya mencabut Update, Read pada Head Office {runId} tetap dimiliki)` (245 kar), Cakupan `Group Update beserta descendant, ditambah Group Read` (52 kar) · sumber matriks role PRD
- **DU-016-12** User (awal), Pelapor record dan admin yang mencabut capability aktor: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-016-13** User (awal), Pelapor record Waiting for Confirmation: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-016-14** Group (awal), Group tanpa Update maupun Read bagi aktor: Name `Gudang Bandung {runId}` (22 kar) · sumber turunan penulis
- **DU-016-15** Damage record (awal), Record Damaged di Group di luar cakupan aktor: Asset Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Gudang Bandung {runId}` (22 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-016-16** User (awal), Aktor akhir spec: pemegang Update yang juga Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Manage asset & TAG (Update pada Head Office {runId}) dan Asset Admin sub-tab Disposal` (85 kar), Cakupan `Group Update beserta descendant` (31 kar) · sumber matriks role PRD
- **DU-016-17** Damage record (awal), Record Reported Disposal milik Asset Admin sub-tab Disposal: Asset Name `Scanner Brother ADS-2200 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar), Reported By `Maya Puspita {runId}` (20 kar) · sumber turunan penulis
- **DU-017-1** Damage record (awal), Laporan Waiting di Group pertama: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-017-2** Damage record (awal), Record Damaged di Group lain: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-017-3** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-017-4** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-017-5** Damage record (awal), Laporan aktor sendiri sebagai pelapor umum: Asset Name `Handheld Scanner Zebra TC21 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-017-6** Group (awal), Group pertama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-017-7** Group (awal), Group kedua: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-017-8** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Read Only (tanpa Manage accounting)` (35 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-017-9** User (awal), Pelapor record: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-017-10** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-018-1** Damage record (awal), Laporan Waiting di Group penugasan: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-018-2** Damage record (awal), Record Damaged di descendant, tautan Damage Log dalam cakupan: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Sub Head Office {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-018-3** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-018-4** Damage record (awal), Record Damaged di luar Group penugasan, tautan Damage Log ditolak: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-018-5** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-018-6** Damage record (awal), Laporan aktor sendiri sebagai pelapor umum: Asset Name `Handheld Scanner Zebra TC21 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-018-7** Group (awal), Group penugasan: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-018-8** Group (awal), Descendant Group penugasan: Name `Sub Head Office {runId}` (23 kar), Induk `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-018-9** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Manage asset & TAG (Read pada Head Office {runId}, tanpa Manage accounting)` (75 kar), Cakupan `Group penugasan beserta descendant` (34 kar) · sumber matriks role PRD
- **DU-018-10** User (awal), Pelapor record: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-018-11** Group (awal), Group di luar penugasan: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-018-12** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-019-1** Damage record (awal), Laporan Waiting di Group assign: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-019-2** Damage record (awal), Record Damaged di descendant, tautan Damage Log dalam cakupan: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Sub Head Office {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-019-3** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-019-4** Damage record (awal), Record Damaged di luar Group assign, tautan Damage Log ditolak: Asset Name `Toyota Avanza {runId}` (21 kar), Group `Branch Surabaya {runId}` (23 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-019-5** Damage record (awal), Record Repaired di History: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-019-6** Damage record (awal), Laporan aktor sendiri sebagai pelapor umum: Asset Name `Handheld Scanner Zebra TC21 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-019-7** Group (awal), Group assign: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-019-8** Group (awal), Descendant Group assign: Name `Sub Head Office {runId}` (23 kar), Induk `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-019-9** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `View asset value (Group assign Head Office {runId})` (51 kar), Cakupan `Aset di Group assign beserta descendant` (39 kar) · sumber matriks role PRD
- **DU-019-10** User (awal), Pelapor record: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-019-11** Group (awal), Group di luar penugasan: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-019-12** Asset (awal), Aset tanpa record Damaged berjalan: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Normal` (6 kar) · sumber turunan penulis
- **DU-020-1** Damage record (awal), Laporan pelapor yang tidak punya akses tab Damaged: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-020-2** User (awal), Aktor spec ini: Name `Budi Santoso {runId}` (20 kar), Role `Pelapor umum (tanpa role Damaged)` (33 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-021-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-021-record-terakhir-selesai-empty-state), Satu-satunya record berjalan di entitas khusus, tanpa TAG: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-021-2** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client pada entitas khusus` (34 kar) · sumber matriks role PRD
- **DU-021-3** Input Mark as Repaired (dibuat), Repair note yang diketik: Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal` (59 kar) · sumber turunan penulis
- **DU-022-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-022-already-changed-konflik-status), Laporan Waiting yang lebih dulu di-Confirm admin kedua: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-022-2** Damage record (awal), Record Reported Disposal: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-022-3** Damage record (awal), Record In Disposal Process: Asset Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-022-4** User (awal), Pelapor record: Name `Dewi Anggraeni {runId}` (22 kar), Role `Pelapor umum (tanpa hak Aktor Damaged)` (38 kar), Cakupan `Aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-022-5** User (awal), Aktor spec ini: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-022-6** User (awal), Aktor kedua yang mengonfirmasi lebih dulu: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-022-7** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-022-already-changed-konflik-status), Record Damaged tanpa TAG yang dipindah ke Reported Disposal oleh admin lain saat dialog Mark as Repaired terbuka: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `tidak ada` (9 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-022-8** Repair note Mark as Repaired (dicoba), Repair note yang diketik lalu ditolak karena status sudah berubah: Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal` (59 kar) · sumber turunan penulis
- **DU-022-9** Reason Report Disposal (dibuat), Alasan Report Disposal oleh admin lain yang lebih dulu memindahkan status: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain` (48 kar) · sumber turunan penulis
- **DU-022-10** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-022-already-changed-konflik-status), Laporan Waiting yang lebih dulu dibatalkan pelapor saat admin membuka Confirm: Asset Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraeni {runId}` (22 kar) · sumber turunan penulis
- **DU-023-1** User (awal), Aktor kunjungan pertama: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control (flag Guided Tooltip tab Damaged belum diset)` (59 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-023-2** User (awal), Aktor yang flag-nya sudah diset di perangkat lain: Name `Agus Pratama {runId}` (20 kar), Role `Total Control (flag Guided Tooltip tab Damaged sudah diset dari perangkat lain)` (79 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-023-3** User (awal), Aktor ketiga dengan flag Guided Tooltip belum diset, memakai jalur Skip: Name `Budi Santoso {runId}` (20 kar), Role `Total Control (flag Guided Tooltip tab Damaged belum diset)` (59 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-024-1** Entitas (awal), Entitas Active sebagai pembanding: Name `Client Aktif {runId}` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-024-2** Entitas (awal), Entitas Suspended: Name `Client Suspended {runId}` (24 kar), Status `Suspended` (9 kar) · sumber turunan penulis
- **DU-024-3** Entitas (awal), Entitas Expired: Name `Client Expired {runId}` (22 kar), Status `Expired` (7 kar) · sumber turunan penulis
- **DU-024-4** User (awal), Aktor entitas Active: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control pada entitas Client Aktif {runId}` (47 kar), Cakupan `Seluruh entitas Active` (22 kar) · sumber matriks role PRD
- **DU-024-5** User (awal), Aktor entitas Suspended: Name `Agus Pratama {runId}` (20 kar), Role `Total Control pada entitas Client Suspended {runId}` (51 kar), Cakupan `Seluruh entitas Suspended` (25 kar) · sumber matriks role PRD
- **DU-024-6** User (awal), Aktor entitas Expired: Name `Dewi Anggraeni {runId}` (22 kar), Role `Total Control pada entitas Client Expired {runId}` (49 kar), Cakupan `Seluruh entitas Expired` (23 kar) · sumber matriks role PRD
- **DU-024-7** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-024-entitas-suspended-expired), Laporan Waiting di entitas Active, di-Confirm: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Entitas `Client Aktif {runId}` (20 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-024-8** Damage record (awal), Laporan Waiting di entitas Suspended: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Entitas `Client Suspended {runId}` (24 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-024-9** Damage record (awal), Laporan Waiting di entitas Expired: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Entitas `Client Expired {runId}` (22 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar) · sumber turunan penulis
- **DU-025-1** Entitas (awal), Entitas level Disposal None: Name `Client None {runId}` (19 kar), Level Feature Suite Disposal `None` (4 kar) · sumber turunan penulis
- **DU-025-2** Entitas (awal), Entitas level Disposal Basic: Name `Client Basic {runId}` (20 kar), Level Feature Suite Disposal `Basic` (5 kar) · sumber turunan penulis
- **DU-025-3** Entitas (awal), Entitas level Disposal Full: Name `Client Full {runId}` (19 kar), Level Feature Suite Disposal `Full` (4 kar) · sumber turunan penulis
- **DU-025-4** User (awal), Aktor entitas level None: Name `Rina Wijaya {runId}` (19 kar), Role `Total Control pada entitas Client None {runId}` (46 kar), Cakupan `Seluruh entitas level None` (26 kar) · sumber matriks role PRD
- **DU-025-5** User (awal), Aktor entitas level Basic: Name `Agus Pratama {runId}` (20 kar), Role `Total Control pada entitas Client Basic {runId}` (47 kar), Cakupan `Seluruh entitas level Basic` (27 kar) · sumber matriks role PRD
- **DU-025-6** User (awal), Aktor entitas level Full: Name `Dewi Anggraeni {runId}` (22 kar), Role `Total Control pada entitas Client Full {runId}` (46 kar), Cakupan `Seluruh entitas level Full` (26 kar) · sumber matriks role PRD
- **DU-025-7** Damage record (awal), Record Damaged di tiap entitas: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-025-8** Damage record (awal), Record Reported Disposal di tiap entitas: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Rina Wijaya {runId}` (19 kar) · sumber turunan penulis
- **DU-025-9** Entitas (awal), Entitas dengan plan Starter untuk tipe TAG yang terkunci: Name `Client Starter {runId}` (22 kar), Plan `Starter` (7 kar) · sumber turunan penulis
- **DU-025-10** User (awal), Aktor Total Control pada entitas plan Starter: Name `Budi Santoso {runId}` (20 kar), Role `Total Control pada entitas Client Starter {runId}` (49 kar), Cakupan `Seluruh entitas plan Starter` (28 kar) · sumber matriks role PRD
- **DU-026-1** Damage record (awal), Record Damaged aset ber-TAG RFID: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `RFID` (4 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-026-2** Damage record (awal), Record Damaged aset ber-TAG QR: Asset Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `QR` (2 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-026-3** Damage record (awal), Record Damaged aset di Group di luar saringan: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), TAG `RFID` (4 kar), Reported By `Agus Pratama {runId}` (20 kar) · sumber turunan penulis
- **DU-026-4** TAG (awal), TAG RFID terpasang pada aset: Kode TAG `RFID-{runId}-A` (14 kar), Tipe `RFID` (4 kar), Terpasang pada `Laptop Dell Latitude 5420 {runId}` (33 kar) · sumber turunan penulis
- **DU-026-5** TAG (awal), TAG QR terpasang pada aset: Kode TAG `QR-{runId}-B` (12 kar), Tipe `QR` (2 kar), Terpasang pada `Tablet Samsung Tab A8 {runId}` (29 kar) · sumber turunan penulis
- **DU-026-6** TAG (awal), TAG RFID aset di luar saringan: Kode TAG `RFID-{runId}-C` (14 kar), Tipe `RFID` (4 kar), Terpasang pada `Projector Epson EB-X06 {runId}` (30 kar) · sumber turunan penulis
- **DU-026-7** TAG (awal), TAG terdaftar yang belum terpasang pada aset: Kode TAG `RFID-{runId}-N` (14 kar), Tipe `RFID` (4 kar), Terpasang pada `belum terpasang` (15 kar) · sumber turunan penulis
- **DU-026-8** Group (awal), Group pertama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-026-9** Group (awal), Group kedua: Name `Warehouse {runId}` (17 kar) · sumber turunan penulis
- **DU-026-10** User (awal), Aktor spec ini: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-026-11** TAG (awal), TAG yang tidak terdaftar di perusahaan: Kode TAG `RFID-{runId}-X` (14 kar), Tipe `RFID` (4 kar), Terdaftar `tidak` (5 kar) · sumber turunan penulis
- **DU-030-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-030-report-damaged-satu-aset-dep-asset), Aset Normal tanpa record Damage, dilaporkan dari Asset List: Asset Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-030-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-030-report-damaged-satu-aset-dep-asset), Aset Normal tanpa record Damage, dilaporkan dari Asset Detail: Asset Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-030-3** Damage Report (dibuat), Isian laporan aset dari Asset List: What happened `Layar proyektor retak dan tidak menampilkan gambar` (50 kar), Damaged Photo `proyektor-retak.jpg` (19 kar) · sumber turunan penulis
- **DU-030-4** Damage Report (dibuat), Isian laporan aset dari Asset Detail: What happened `Kertas macet dan roller printer patah` (37 kar), Damaged Photo `printer-roller-patah.jpg` (24 kar) · sumber turunan penulis
- **DU-030-5** Asset (awal), Aset dengan record Damage berjalan berstatus Damaged yang dilaporkan, di-Confirm, dan node terakhirnya di hari berbeda: Asset Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Damaged` (7 kar), Reported Date `T0 − 5 hari, pukul 09:10` (24 kar), Tanggal Confirm `T0 − 2 hari, pukul 10:30` (24 kar), Node terbaru `T0 − 1 hari, pukul 16:40` (24 kar) · sumber turunan penulis
- **DU-030-6** Asset (awal), Aset Disposed: Asset Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Head Office` (11 kar), Status global `Disposed` (8 kar) · sumber turunan penulis
- **DU-030-7** Asset (awal), Aset Missing tanpa record Damage: Asset Name `Drill Bosch GSB {runId}` (23 kar), Group `Head Office` (11 kar), Status global `Missing` (7 kar) · sumber turunan penulis
- **DU-030-8** Asset (awal), Aset dengan record Damage berstatus Waiting for Confirmation: Asset Name `Headset Logitech H390 {runId}` (29 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Waiting for Confirmation` (24 kar), Reported Date `T0 − 3 hari, pukul 09:15` (24 kar) · sumber turunan penulis
- **DU-030-9** Asset (awal), Aset dengan record Damage berstatus Reported Disposal: Asset Name `Laptop Lenovo ThinkPad E14 {runId}` (34 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Reported Disposal` (17 kar) · sumber turunan penulis
- **DU-030-10** Asset (awal), Aset dengan record Damage berstatus In Disposal Process: Asset Name `Keyboard Logitech K380 {runId}` (30 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `In Disposal Process` (19 kar) · sumber turunan penulis
- **DU-031-1** Asset (awal), Satu aset layak dipilih untuk dialog tunggal: Asset Name `Meja Kerja Staff {runId}` (24 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-031-2** Asset (awal; 8 record), Delapan aset bernama panjang agar daftar dialog bergulir: Asset Name `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId} {n}` (80 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar), Kata kunci Search `Kursi Rapat Eksekutif Ruang Pertemuan Utama Lantai Tiga Gedung Timur {runId}` (76 kar) · sumber turunan penulis
- **DU-031-3** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset layak pertama dalam seleksi campuran: Asset Name `Laptop Staf {runId} Layak 1` (27 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar), Kata kunci Search `Laptop Staf {runId}` (19 kar) · sumber turunan penulis
- **DU-031-4** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset layak kedua dalam seleksi campuran: Asset Name `Laptop Staf {runId} Layak 2` (27 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-031-5** Asset (awal), Aset dengan record Damage berjalan berstatus Damaged (beranotasi): Asset Name `Laptop Staf {runId} Berjalan` (28 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Damaged` (7 kar) · sumber turunan penulis
- **DU-031-6** Asset (awal), Aset dengan record Damage berstatus Waiting for Confirmation: Asset Name `Laptop Staf {runId} Waiting` (27 kar), Group `Head Office` (11 kar), Status record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-031-7** Asset (awal), Aset Disposed dalam seleksi campuran: Asset Name `Laptop Staf {runId} Disposed` (28 kar), Group `Head Office` (11 kar), Status global `Disposed` (8 kar) · sumber turunan penulis
- **DU-031-8** Asset (awal), Aset Missing dalam seleksi campuran: Asset Name `Laptop Staf {runId} Missing` (27 kar), Group `Head Office` (11 kar), Status global `Missing` (7 kar) · sumber turunan penulis
- **DU-031-9** Asset (awal), Aset di Group tempat aktor hanya memegang Read: Asset Name `Laptop Staf {runId} Luar Cakupan` (32 kar), Group `Branch Surabaya` (15 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-031-10** Asset (awal), Aset ber-record berjalan dalam seleksi yang seluruhnya tidak layak: Asset Name `Monitor Arsip {runId} Berjalan` (30 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Damaged` (7 kar), Kata kunci Search `Monitor Arsip {runId}` (21 kar) · sumber turunan penulis
- **DU-031-11** Asset (awal), Aset Disposed dalam seleksi yang seluruhnya tidak layak: Asset Name `Monitor Arsip {runId} Disposed` (30 kar), Group `Head Office` (11 kar), Status global `Disposed` (8 kar) · sumber turunan penulis
- **DU-031-12** Asset (awal), Aset Missing dalam seleksi yang seluruhnya tidak layak: Asset Name `Monitor Arsip {runId} Missing` (29 kar), Group `Head Office` (11 kar), Status global `Missing` (7 kar) · sumber turunan penulis
- **DU-031-13** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset pertama yang tetap dilaporkan saat aset kedua dilaporkan admin lain: Asset Name `Scanner Gudang {runId} Satu` (27 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar), Kata kunci Search `Scanner Gudang {runId}` (22 kar) · sumber turunan penulis
- **DU-031-14** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset yang menjadi tidak layak karena dilaporkan admin lain sebelum Submit: Asset Name `Scanner Gudang {runId} Dua` (26 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-031-15** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset pertama yang dilaporkan admin lain sebelum Submit: Asset Name `Printer Gudang {runId} Satu` (27 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar), Kata kunci Search `Printer Gudang {runId}` (22 kar) · sumber turunan penulis
- **DU-031-16** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-031-report-damaged-banyak-aset-dep-asset), Aset kedua yang dilaporkan admin lain sebelum Submit: Asset Name `Printer Gudang {runId} Dua` (26 kar), Group `Head Office` (11 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-031-17** Damage Report (dibuat), Isian laporan dua aset laptop: What happened `Genangan air merusak casing laptop` (34 kar), Damaged Photo Layak 1 `laptop-layak-1.jpg` (18 kar), Damaged Photo Layak 2 `laptop-layak-2.jpg` (18 kar) · sumber turunan penulis
- **DU-031-18** Damage Report (dibuat), Isian laporan dua aset scanner: What happened `Casing scanner retak setelah terjatuh` (37 kar), Damaged Photo Satu `scanner-satu.jpg` (16 kar), Damaged Photo Dua `scanner-dua.jpg` (15 kar) · sumber turunan penulis
- **DU-031-19** Damage Report (dibuat), Isian laporan dua aset printer: What happened `Roller printer gudang aus` (25 kar), Damaged Photo Satu `printer-satu.jpg` (16 kar), Damaged Photo Dua `printer-dua.jpg` (15 kar) · sumber turunan penulis
- **DU-031-20** Damage Report (dibuat), Laporan Admin B atas scanner kedua: What happened `Kabel daya scanner terbakar` (27 kar), Damaged Photo `scanner-kabel-terbakar.jpg` (26 kar) · sumber turunan penulis
- **DU-031-21** Damage Report (dibuat), Laporan Admin B atas printer pertama: What happened `Panel printer gudang mati total` (31 kar), Damaged Photo `printer-panel-mati.jpg` (22 kar) · sumber turunan penulis
- **DU-031-22** Damage Report (dibuat), Laporan Admin B atas printer kedua: What happened `Tray kertas printer gudang patah` (32 kar), Damaged Photo `printer-tray-patah.jpg` (22 kar) · sumber turunan penulis
- **DU-032-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-032-efek-repaired-di-asset-dep-asset), Aset tanpa TAG dengan record Damage berjalan berstatus Damaged: Asset Name `Genset Honda EU22i {runId}` (26 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status global `Damaged` (7 kar), Status record `Damaged` (7 kar) · sumber turunan penulis
- **DU-032-2** Damage Report (dibuat), Repair note untuk Mark as Repaired: Repair note `Mesin diservis dan busi diganti` (31 kar) · sumber turunan penulis
- **DU-033-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-033-report-dari-my-asset-dep-my-asset), Aset yang dipegang pelapor lewat Assignment, tanpa record Damage: Asset Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status global `Assigned` (8 kar) · sumber turunan penulis
- **DU-033-2** Damage Report (dibuat), Isian laporan pemegang dari My Asset: What happened `Keyboard laptop tidak merespons tombol` (38 kar), Damaged Photo `keyboard-rusak.jpg` (18 kar) · sumber turunan penulis
- **DU-034-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-034-pemegang-berhak-update-dep-my-asset), Aset yang dipegang aktor di Group tempat aktor memegang Update: Asset Name `Tablet Samsung Tab A8 {runId} Pusat` (35 kar), Group `Head Office` (11 kar), Status global `Assigned` (8 kar) · sumber turunan penulis
- **DU-034-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-034-pemegang-berhak-update-dep-my-asset), Aset yang dipegang aktor di Group tempat aktor hanya memegang Read: Asset Name `Tablet Samsung Tab A8 {runId} Cabang` (36 kar), Group `Branch Surabaya` (15 kar), Status global `Assigned` (8 kar) · sumber turunan penulis
- **DU-034-3** Damage Report (dibuat), Isian laporan aset Pusat: What happened `Layar tablet pecah di sudut kanan atas` (38 kar), Damaged Photo `tablet-pusat-pecah.jpg` (22 kar) · sumber turunan penulis
- **DU-034-4** Damage Report (dibuat), Isian laporan aset Cabang: What happened `Baterai tablet menggembung` (26 kar), Damaged Photo `tablet-cabang-baterai.jpg` (25 kar) · sumber turunan penulis
- **DU-035-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-035-cancel-report-dep-my-asset), Aset dengan laporan pemegang berstatus Waiting for Confirmation yang akan dibatalkan: Asset Name `Kamera Canon EOS R10 {runId} A` (30 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-035-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-035-cancel-report-dep-my-asset), Aset dengan laporan pemegang Waiting for Confirmation yang di-Confirm Admin B lebih dulu: Asset Name `Kamera Canon EOS R10 {runId} B` (30 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-035-3** Asset (awal), Aset dipegang aktor dengan laporan yang ditolak admin: Asset Name `Proyektor BenQ MH733 {runId} Ditolak` (36 kar), Group `Head Office` (11 kar), Status global `Assigned` (8 kar), Status record `Rejected` (8 kar) · sumber turunan penulis
- **DU-035-4** Asset (awal), Aset dipegang aktor dengan laporan yang sudah diperbaiki: Asset Name `Speaker JBL Eon {runId} Selesai` (31 kar), Group `Head Office` (11 kar), Status global `Assigned` (8 kar), Status record `Repaired` (8 kar) · sumber turunan penulis
- **DU-035-5** Asset (awal), Aset yang tidak lagi dipegang aktor dengan laporan Waiting for Confirmation milik aktor: Asset Name `Mikrofon Shure SM58 {runId} Dilepas` (35 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Waiting for Confirmation` (24 kar), Pemegang `bukan aktor` (11 kar) · sumber turunan penulis
- **DU-036-1** Asset (awal), Aset dipegang aktor dengan laporan Waiting for Confirmation: Asset Name `Mesin Fotokopi {runId} Waiting` (30 kar), Group `Head Office` (11 kar), Status record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-036-2** Asset (awal), Aset dipegang aktor dengan laporan Damaged: Asset Name `Mesin Fotokopi {runId} Damaged` (30 kar), Group `Head Office` (11 kar), Status record `Damaged` (7 kar) · sumber turunan penulis
- **DU-036-3** Asset (awal), Aset dengan laporan aktor yang sudah Repaired: Asset Name `Mesin Fotokopi {runId} Repaired` (31 kar), Group `Head Office` (11 kar), Status record `Repaired` (8 kar) · sumber turunan penulis
- **DU-036-4** Asset (awal), Aset tidak dipegang aktor dengan laporan Disposed: Asset Name `Mesin Fotokopi {runId} Disposed` (31 kar), Group `Head Office` (11 kar), Status record `Disposed` (8 kar) · sumber turunan penulis
- **DU-036-5** Asset (awal), Aset tidak dipegang aktor dengan laporan Rejected beserta Reason: Asset Name `Mesin Fotokopi {runId} Rejected` (31 kar), Group `Head Office` (11 kar), Status record `Rejected` (8 kar), Damaged Photo `fotokopi-rusak.jpg` (18 kar), Reason `Kerusakan akibat kelalaian pengguna` (35 kar), Diputuskan oleh `Admin B` (7 kar) · sumber turunan penulis
- **DU-036-6** Asset (awal), Aset tidak dipegang aktor dengan laporan Canceled: Asset Name `Mesin Fotokopi {runId} Canceled` (31 kar), Group `Head Office` (11 kar), Status record `Canceled` (8 kar) · sumber turunan penulis
- **DU-036-7** Asset (awal), Aset dengan record Damage milik pelapor lain: Asset Name `Mesin Fotokopi {runId} Milik Lain` (33 kar), Group `Head Office` (11 kar), Status record `Damaged` (7 kar) · sumber turunan penulis
- **DU-057-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-057-laporan-scan-mobile-dep-tag), Aset ber-TAG layak dilaporkan, dipindai pengguna aktif: Asset Name `Proyektor BenQ MW535 {runId}` (28 kar), Group `Head Office` (11 kar), TAG `QR` (2 kar), Status global `Normal` (6 kar) · sumber turunan penulis
- **DU-057-2** Asset (awal), Aset ber-TAG berstatus Disposed: Asset Name `Printer Brother HL-L2375DW {runId}` (34 kar), Group `Head Office` (11 kar), TAG `QR` (2 kar), Status global `Disposed` (8 kar) · sumber turunan penulis
- **DU-057-3** Asset (awal), Aset ber-TAG berstatus Missing tanpa record Damage: Asset Name `Mesin Cuci Industri {runId}` (27 kar), Group `Head Office` (11 kar), TAG `QR` (2 kar), Status global `Missing` (7 kar) · sumber turunan penulis
- **DU-057-4** Damage Report (dibuat), Isian laporan lewat scan: What happened `Lensa proyektor berembun dan gambar buram` (41 kar), Damaged Photo `lensa-berembun.jpg` (18 kar) · sumber turunan penulis
- **DU-058-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-058-my-asset-mobile-dep-my-asset), Aset yang dipegang aktor, dilaporkan dari kartu My Asset lalu dibatalkan: Asset Name `Handphone Samsung Galaxy A54 {runId}` (36 kar), Group `Head Office` (11 kar), Status global `Assigned` (8 kar) · sumber turunan penulis
- **DU-058-2** Damage Report (dibuat), Isian laporan lewat bottom sheet dengan foto kamera: What happened `Layar ponsel retak setelah terjatuh` (35 kar), Damaged Photo `foto-layar-retak` (16 kar) · sumber turunan penulis
- **DU-058-3** Asset (awal), Aset tidak dipegang aktor dengan laporan lewat scan Waiting for Confirmation: Asset Name `Tablet Lenovo Tab M10 {runId}` (29 kar), Group `Head Office` (11 kar), Status record `Waiting for Confirmation` (24 kar), Source `Reported by scan` (16 kar) · sumber turunan penulis
- **DU-058-4** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-058-my-asset-mobile-dep-my-asset), Aset dengan laporan Waiting for Confirmation yang di-Confirm Admin B lebih dulu: Asset Name `Speaker Bluetooth JBL {runId}` (29 kar), Group `Head Office` (11 kar), Status global `Damaged` (7 kar), Status record `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-059-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-059-report-tag-saat-mark-as-repaired-dep-tag), Aset ber-TAG yang TAG-nya tidak dapat dipindai, record Damaged berjalan: Asset Name `Kamera Sony ZV-E10 {runId}` (26 kar), Group `Head Office` (11 kar), TAG `RFID` (4 kar), Status global `Damaged` (7 kar), Status record `Damaged` (7 kar) · sumber turunan penulis
- **DU-059-2** Damage Report (dibuat), Repair note untuk Mark as Repaired dengan identifikasi manual: Repair note `Antena RFID diganti dan diuji ulang` (35 kar) · sumber turunan penulis
- **DU-037-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-037-report-missing-dep-missing), Record Damaged tanpa penanda yang dilaporkan Missing: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Lensa retak setelah jatuh dari rak penyimpanan` (46 kar), Damaged Photo `kamera-lensa-retak.jpg` (22 kar) · sumber PRD §4.1a Example Data
- **DU-037-2** Damage record (awal), Record Damaged berpenanda Reported Missing: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a Example Data
- **DU-037-3** Damage record (awal), Record Damaged pembanding tanpa penanda: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-038-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-038-aset-ditemukan-damaged-dep-missing), Record Damaged ditahan penanda Missing atas aset Missing: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Layar laptop retak dan tidak menyala` (36 kar), Damaged Photo `laptop-layar-retak.jpg` (22 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-038-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-038-aset-ditemukan-damaged-dep-missing), Aset Missing tanpa Damage record: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), Status `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-038-3** Mark as Found Damaged (dibuat), Input Mark as Found atas aset berrecord ditahan: Kondisi `Damaged` (7 kar), Note `Ditemukan di gudang dengan bodi penyok` (38 kar), Damaged Photo `laptop-ditemukan-penyok.jpg` (27 kar) · sumber turunan penulis
- **DU-038-4** Mark as Found Damaged (dibuat), Input Mark as Found atas aset tanpa Damage record: Kondisi `Damaged` (7 kar), Note `Ditemukan di ruang rapat dengan layar pecah` (43 kar), Damaged Photo `tablet-ditemukan-pecah.jpg` (26 kar) · sumber turunan penulis
- **DU-039-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-039-laporan-missing-ditutup-dep-missing), Record Damaged berpenanda Reported Missing yang laporannya ditolak: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a Example Data
- **DU-039-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-039-laporan-missing-ditutup-dep-missing), Record Damaged berpenanda Reported Missing yang laporannya dibatalkan pemegang: Name `Drill Bosch GSB {runId}` (23 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a Example Data
- **DU-039-3** Reject laporan Missing (dibuat), Input Reject laporan Missing atas record Camera Canon EOS: Reason `Aset masih berada di gudang pusat` (33 kar) · sumber turunan penulis
- **DU-040-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-040-missing-disposed-dep-missing), Record Damaged berpenanda Missing atas aset Missing yang di-Dispose: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-041-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-041-report-disposal-dep-disposal), Record Damaged atas aset tanpa pemakai yang dilaporkan untuk disposal: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Custody `Available` (9 kar) · sumber PRD §4.1a Example Data
- **DU-041-2** Damage record (awal), Record Damaged atas aset yang sedang Borrowed: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Custody `Borrowed` (8 kar), Transaction ID `milik transaksi Borrow aset ini` (31 kar) · sumber PRD §4.1a Example Data
- **DU-041-3** Damage record (awal), Record Damaged atas aset yang sedang Assigned: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Custody `Assigned` (8 kar), Transaction ID `milik transaksi Assignment aset ini` (35 kar) · sumber PRD §4.1a Example Data
- **DU-041-4** Report Disposal (dibuat), Input Reason Report Disposal atas record Printer HP LaserJet: Reason `Unit rusak berat dan biaya perbaikan melebihi nilai buku` (56 kar) · sumber turunan penulis
- **DU-042-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal), Satu record Damaged yang dibulk Report Disposal: Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-2** Damage record (awal; 2 record; dimutasi TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal), Dua record Damaged satu Group yang lolos semua cabang bulk: Asset Name `Printer HP LaserJet {runId}` (27 kar), Name `Printer HP LaserJet {runId} - {n}` (33 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-3** Damage record (awal; 6 record; dimutasi TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal), Enam record Damaged, empat di antaranya sudah dilaporkan lebih dulu oleh admin lain saat Submit: Asset Name `Proyektor Epson EB-X06 {runId}` (30 kar), Name `Proyektor Epson EB-X06 {runId} - {n}` (36 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-4** Damage record (awal; 8 record; dimutasi TC-FA-DAMAGED-E2E-042-bulk-report-disposal-dep-disposal), Delapan record Damaged bernama panjang yang seluruhnya sudah dilaporkan lebih dulu oleh admin lain saat Submit: Asset Name `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara` (70 kar), Name `Panel Listrik {runId} Distribusi Utama Gedung Operasional Cabang Utara - {n}` (76 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-5** Damage record (awal), Record Damaged di Group Warehouse untuk seleksi lintas Group: Name `Forklift Toyota 8FD {runId}` (27 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-6** Damage record (awal), Record Damaged di Group Head Office untuk seleksi lintas Group: Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-042-7** User (awal), Admin lain yang memicu perubahan status record: Name `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-042-8** Report Disposal (dibuat), Reason bulk satu record: Reason `Monitor tidak menyala dan tidak layak diperbaiki` (48 kar) · sumber turunan penulis
- **DU-042-9** Report Disposal (dibuat), Reason bulk dua record satu Group: Reason `Printer satu Group sudah tidak layak pakai` (42 kar) · sumber turunan penulis
- **DU-042-10** Report Disposal (dibuat), Reason bulk enam record dengan sebagian dilewati: Reason `Proyektor satu Group sudah tidak layak pakai` (44 kar) · sumber turunan penulis
- **DU-042-11** Report Disposal (dibuat), Reason bulk delapan record yang seluruhnya dilewati: Reason `Panel listrik sudah tidak layak pakai` (37 kar) · sumber turunan penulis
- **DU-042-12** Report Disposal (dibuat), Reason Report Disposal oleh admin lain: Reason `Unit sudah dilaporkan lebih dulu oleh admin lain` (48 kar) · sumber turunan penulis
- **DU-043-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-043-cancel-disposal-report-dep-disposal), Record Reported Disposal yang di-Cancel Disposal Report: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-043-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-043-cancel-disposal-report-dep-disposal), Record Reported Disposal yang di-Decline admin lain sebelum Submit: Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-043-3** Damage record (awal), Record Damaged pembanding aksi Hidden: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-043-4** Damage record (awal), Record In Disposal Process pembanding aksi Hidden: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-043-5** User (awal), Admin lain yang memicu perubahan status record: Name `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-043-6** Cancel Disposal Report (dibuat), Input Reason Cancel Disposal Report: Reason `Aset masih dapat diperbaiki` (27 kar) · sumber turunan penulis
- **DU-043-7** Decline Report (dibuat), Input Reason Decline Report oleh admin lain: Reason `Laporan ditolak karena aset masih dapat dipakai` (47 kar) · sumber turunan penulis
- **DU-044-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-044-record-kembali-damaged-dari-tab-reported-dep-disposal), Record Reported Disposal yang di-Decline: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-044-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-044-record-kembali-damaged-dari-tab-reported-dep-disposal), Record Reported Disposal yang di-Cancel Report: Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-044-3** Decline Report (dibuat), Input Reason Decline Report: Reason `Aset masih dapat diperbaiki oleh teknisi internal` (49 kar) · sumber turunan penulis
- **DU-044-4** Cancel Report (dibuat), Input Reason Cancel Report: Reason `Pelaporan dibatalkan karena monitor sudah diperbaiki` (52 kar) · sumber turunan penulis
- **DU-045-1** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal), Record Reported Disposal yang berakhir Disposed: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-045-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal), Record Reported Disposal yang barisnya di-Reject: Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-045-3** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal), Record Reported Disposal yang barisnya di-Cancel: Name `Printer HP LaserJet M404 {runId}` (32 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-045-4** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-045-record-mengikuti-baris-disposal-dep-disposal), Record Reported Disposal yang asetnya di-Remove dari baris: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a Example Data
- **DU-046-1** Asset Registration (awal; dimutasi TC-FA-DAMAGED-E2E-046-registrasi-condition-damaged-dep-asset-registration), draft registrasi aset ber-Condition Damaged yang siap Activate: Name `Laptop Lenovo ThinkPad E14 {runId}` (34 kar), Condition `Damaged` (7 kar), Damage note `Layar retak dan engsel patah setelah terjatuh saat pemindahan unit` (66 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar) · sumber turunan penulis
- **DU-046-2** Damage record (dibuat), Repair note untuk Mark as Repaired: Repair note `Layar sudah diganti dan unit berfungsi normal` (45 kar) · sumber turunan penulis
- **DU-047-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-047-mark-repaired-aset-dipinjam-dep-borrow), aset Damaged yang sedang dipinjam: Name `Tablet Samsung Tab A8 {runId}` (29 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Borrow `Borrowed` (8 kar), Borrower `Dewi Anggraini {runId}` (22 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Layar tablet tidak merespons sentuhan di sisi kanan` (51 kar) · sumber turunan penulis
- **DU-047-2** Asset (awal), aset Damaged tanpa pemegang untuk pembacaan form Borrow: Name `Camera Canon EOS {runId}` (24 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Lensa tidak bisa fokus otomatis` (31 kar) · sumber turunan penulis
- **DU-047-3** Damage record (dibuat), Repair note untuk Mark as Repaired aset dipinjam: Repair note `Sentuhan layar sudah dikalibrasi ulang dan berfungsi normal` (59 kar) · sumber turunan penulis
- **DU-048-1** Asset (awal), aset yang sedang dipinjam dan belum punya record Damage: Name `Projector Epson EB-X06 {runId}` (30 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Borrow `Borrowed` (8 kar), Borrower `Sari Dewanti {runId}` (20 kar) · sumber turunan penulis
- **DU-048-2** Damage record (dibuat), laporan kerusakan dari Detail BRW: What happened `Lensa proyektor berembun dan gambar buram` (41 kar), Damaged Photo `proyektor-lensa-buram.jpg` (25 kar) · sumber turunan penulis
- **DU-049-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-049-return-accept-with-damage-dep-borrow), aset dipinjam tanpa record Damage: Name `Printer Brother HL-L2375 {runId}` (32 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Borrow `Borrowed` (8 kar), Borrower `Hana Pratiwi {runId}` (20 kar) · sumber turunan penulis
- **DU-049-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-049-return-accept-with-damage-dep-borrow), aset dipinjam dengan record Waiting for Confirmation dari laporan pemegang, untuk Confirm: Name `Scanner Fujitsu fi-7160 {runId}` (31 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Borrow `Borrowed` (8 kar), Borrower `Rudi Hartono {runId}` (20 kar), Status record `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), What happened `Roller pemindai macet dan kertas sering tersangkut` (50 kar) · sumber turunan penulis
- **DU-049-3** Return (dibuat), catatan dan foto Return atas aset tanpa record: Description `Casing printer retak setelah terjatuh saat dikembalikan` (55 kar), Foto Return `printer-casing-retak.jpg` (24 kar) · sumber turunan penulis
- **DU-050-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-050-mark-repaired-aset-ditugaskan-dep-assignment), aset Damaged yang sedang ditugaskan: Name `Laptop Dell Latitude 5420 {runId}` (33 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Assignment `Assigned` (8 kar), Assignee `Bima Prakoso {runId}` (20 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Engsel laptop longgar dan layar tidak bisa berdiri tegak` (56 kar) · sumber turunan penulis
- **DU-050-2** Asset (awal), aset Damaged tanpa pemegang untuk pembacaan form Assign: Name `Monitor Dell P2422H {runId}` (27 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Layar monitor berkedip dan garis vertikal muncul` (48 kar) · sumber turunan penulis
- **DU-050-3** Damage record (dibuat), Repair note untuk Mark as Repaired aset ditugaskan: Repair note `Engsel laptop sudah diganti dan layar bisa berdiri tegak` (56 kar) · sumber turunan penulis
- **DU-051-1** Asset (awal), aset yang sedang ditugaskan dan belum punya record Damage: Name `Headset Jabra Evolve2 {runId}` (29 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Assignment `Assigned` (8 kar), Assignee `Maya Lestari {runId}` (20 kar) · sumber turunan penulis
- **DU-051-2** Damage record (dibuat), laporan kerusakan dari Detail Assignment: What happened `Earcup kiri retak dan bantalan terlepas` (39 kar), Damaged Photo `headset-earcup-retak.jpg` (24 kar) · sumber turunan penulis
- **DU-052-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-052-unassign-accept-with-damage-dep-assignment), aset ditugaskan tanpa record Damage: Name `Webcam Logitech C920 {runId}` (28 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Assignment `Assigned` (8 kar), Assignee `Citra Maharani {runId}` (22 kar) · sumber turunan penulis
- **DU-052-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-052-unassign-accept-with-damage-dep-assignment), aset ditugaskan dengan record Waiting for Confirmation dari laporan pemegang: Name `Tablet Lenovo Tab M10 {runId}` (29 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status Assignment `Assigned` (8 kar), Assignee `Dani Ramadhan {runId}` (21 kar), Status record `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), What happened `Layar tablet muncul bintik hitam dan sentuhan lambat` (52 kar) · sumber turunan penulis
- **DU-052-3** Unassign (dibuat), catatan dan foto Unassign atas aset tanpa record: Description `Lensa webcam tergores dan gambar buram` (38 kar), Foto Unassign `webcam-lensa-tergores.jpg` (25 kar) · sumber turunan penulis
- **DU-052-4** Unassign (dibuat), catatan dan foto Unassign atas aset yang sudah punya record Waiting for Confirmation: Description `Layar tablet bintik hitam seperti yang dilaporkan pemegang` (58 kar), Foto Unassign `tablet-layar-bintik.jpg` (23 kar) · sumber turunan penulis
- **DU-053-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-053-transfer-dep-transfer), aset ber-record Damaged yang akan di-Transfer: Name `Printer Epson L3250 {runId}` (27 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Tinta merembes dan head printer macet` (37 kar) · sumber turunan penulis
- **DU-053-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-053-transfer-dep-transfer), aset normal yang dilaporkan rusak saat Receive: Name `Scanner Canon DR-C225 {runId}` (29 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar) · sumber turunan penulis
- **DU-053-3** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-053-transfer-dep-transfer), aset ber-laporan scan Waiting for Confirmation yang di-Transfer: Name `Router Cisco RV340 {runId}` (26 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Waiting for Confirmation` (24 kar), Source `Reported by scan` (16 kar), What happened `Port LAN tiga mati sejak kemarin` (32 kar) · sumber turunan penulis
- **DU-053-4** Transfer (dibuat), Group tujuan Transfer: Group tujuan `Branch Surabaya` (15 kar) · sumber PRD §4.1a Example Data
- **DU-053-5** Damage record (dibuat), laporan rusak saat Receive: What happened `Casing scanner retak selama pengiriman` (38 kar), Damaged Photo `scanner-casing-retak.jpg` (24 kar) · sumber turunan penulis
- **DU-054-1** Stock Opname (awal), sesi Stock Opname berisi aset yang belum punya record Damage: Name sesi `Stock Opname Gudang Pusat {runId}` (33 kar), Group `Head Office` (11 kar), Name aset `Rak Besi Heavy Duty {runId}` (27 kar), TAG `tanpa TAG` (9 kar) · sumber turunan penulis
- **DU-054-2** Damage record (dibuat), isian dialog Report Condition untuk kondisi rusak: Condition `Damaged` (7 kar), Catatan kerusakan `Kaki rak bengkok dan tidak stabil saat diberi beban` (51 kar), Foto kerusakan `rak-kaki-bengkok.jpg` (20 kar) · sumber turunan penulis
- **DU-055-1** Group (awal; dimutasi TC-FA-DAMAGED-E2E-055-hapus-group-dep-groups), Group berisi aset dengan record Damaged berjalan: Name Group `Gudang Cabang Bekasi {runId}` (28 kar), Name aset `Genset Honda EU22i {runId}` (26 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Mesin genset sulit menyala dan mengeluarkan asap hitam` (54 kar) · sumber turunan penulis
- **DU-055-2** Asset (awal), aset ber-record Damaged di Group lain sebagai pembanding baris tersisa: Name `Kompresor Atlas Copco GX5 {runId}` (33 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), What happened `Kompresor tidak mencapai tekanan kerja dan bocor di sambungan selang` (68 kar) · sumber turunan penulis
- **DU-055-3** Damage record (dibuat), Repair note Mark as Repaired oleh aktor kedua: Repair note `Mesin genset sudah diservis dan menyala normal` (46 kar) · sumber turunan penulis
- **DU-056-1** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-056-notifikasi-dep-notification), aset dipegang pelapor dengan record Waiting for Confirmation dari laporan pemegang: Name `Laptop HP ProBook 450 {runId}` (29 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Holder `Budi Santoso {runId}` (20 kar), Status record `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar), What happened `Keyboard laptop beberapa tombol tidak berfungsi` (47 kar) · sumber turunan penulis
- **DU-056-2** Asset (awal; dimutasi TC-FA-DAMAGED-E2E-056-notifikasi-dep-notification), aset dipegang pelapor dengan record Damaged dari laporan pemegang: Name `Tablet Samsung Galaxy Tab S7 {runId}` (36 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Holder `Budi Santoso {runId}` (20 kar), Status record `Damaged` (7 kar), Source `Reported by holder` (18 kar), Reported By `Budi Santoso {runId}` (20 kar), What happened `Layar tablet retak di sudut kanan atas` (38 kar) · sumber turunan penulis
- **DU-056-3** Damage record (dibuat), Repair note untuk Mark as Repaired yang memicu notifikasi: Repair note `Layar sudah diganti dan sentuhan normal kembali` (47 kar) · sumber turunan penulis
- **DU-060-1** Damage record (awal), record Damaged yang sudah ada sebelum setting berubah: Name `Mesin Fotokopi Canon iR2625 {runId}` (35 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), Reported Date `T0 − 3 hari, pukul 17:10` (24 kar) · sumber turunan penulis
- **DU-060-2** Damage record (awal; dimutasi TC-FA-DAMAGED-E2E-060-format-tanggal-dep-general-settings), record Damaged yang diselesaikan sesudah setting berubah: Name `Mesin Laminating GBC Fusion {runId}` (35 kar), Group `Head Office` (11 kar), TAG `tanpa TAG` (9 kar), Status record `Damaged` (7 kar), Source `Manual` (6 kar), Reported Date `T0 − 2 hari, pukul 09:30` (24 kar) · sumber turunan penulis
- **DU-060-3** Damage record (dibuat), Repair note untuk record yang diselesaikan sesudah perubahan setting: Repair note `Elemen pemanas sudah diganti dan hasil laminasi rata` (52 kar) · sumber turunan penulis
- **DU-060-4** General Settings (dibuat), Date Format diubah ke M/d/yy: Date Format `M/d/yy` (6 kar) · sumber foundation prd-conventions.md §32
- **DU-060-5** General Settings (dibuat), Date Format diubah ke dd MMM yy: Date Format `dd MMM yy` (9 kar) · sumber foundation prd-conventions.md §32
- **DU-060-6** General Settings (dibuat), Date Format diubah ke DDD, MMM dd, yy: Date Format `DDD, MMM dd, yy` (15 kar) · sumber foundation prd-conventions.md §32
- **DU-060-7** General Settings (dibuat), Date Format diubah ke DDD, MMM dd, yyyy: Date Format `DDD, MMM dd, yyyy` (17 kar) · sumber foundation prd-conventions.md §32
- **DU-060-8** General Settings (dibuat), Time Format diubah ke 12h: Time Format `12h` (3 kar) · sumber foundation prd-conventions.md §32
- **DU-060-9** General Settings (dibuat), Time Zone diubah ke zona non-default: Time Zone `Asia/Jayapura` (13 kar) · sumber turunan penulis
- **DU-060-10** General Settings (dibuat), Date Format, Time Format, dan Time Zone dipilih ke nilai bawaan: Date Format `dd/MM/yy` (8 kar), Time Format `24h` (3 kar), Time Zone `Asia/Jakarta` (12 kar) · sumber foundation prd-conventions.md §32
- **DU-101-1** Damage record (awal), Record Damaged dengan nama dua kata dan tanggal berbeda antar kolom: Photo `projector-epson-eb-x06-2.jpg` (28 kar), Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Borrow return` (13 kar), Last Holder `Sari Dewi` (9 kar), Last Holder Division `Operations` (10 kar), Last Holder Employee ID `EMP-0145` (8 kar), Reported By `Rina Wijaya` (11 kar), Reported Date `2026-11-04T10:10:00Z` (20 kar), Days Damaged `7 days` (6 kar), Last Updated `2026-11-06T02:45:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-101-2** Damage record (awal), Record Waiting for Confirmation dengan nama satu kata: Photo `laptop-dell-latitude-5420-4.jpg` (31 kar), Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Budi` (4 kar), Reported By `Budi` (4 kar), Reported Date `2026-11-10T01:15:00Z` (20 kar), Days Damaged `1 day` (5 kar), Last Updated `2026-11-10T01:15:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-101-3** Damage record (awal), Record Damaged tanpa foto dan tanpa pemegang: Photo `None` (4 kar), Name `Office Chair Ergo - 31` (22 kar), Asset ID `CHR-2026-0031` (13 kar), Group `Branch Surabaya` (15 kar), Status `Damaged` (7 kar), Source `Reported by scan` (16 kar), Last Holder `None` (4 kar), Reported By `Dedi Kurniawan` (14 kar), Reported Date `2026-11-06T06:00:00Z` (20 kar), Days Damaged `5 days` (6 kar) · sumber PRD §4.1a Example Data
- **DU-101-4** Damage record (awal), Record Reported Disposal dengan nama user tiga kata dan nama depan panjang: Name `Printer HP LaserJet M404 - 8` (28 kar), Asset ID `PRN-2026-0008` (13 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Last Holder `Buzzlightyear Sumardi` (21 kar), Reported By `Alexander Graham Bell` (21 kar), Reported Date `2026-10-15T03:00:00Z` (20 kar), Days Damaged `27 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-101-5** Damage record (awal), Record In Disposal Process dengan dua nama user yang mirip: Name `Monitor Dell P2422H - 6` (23 kar), Asset ID `MON-2026-0006` (13 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Last Holder `Dewi Anggraini` (14 kar), Reported By `Dewi Anggreni` (13 kar), Reported Date `2026-09-20T07:20:00Z` (20 kar), Days Damaged `52 days` (7 kar) · sumber PRD §4.1a Example Data
- **DU-101-6** Damage record (awal), Record Damaged berpenanda Missing: Name `Camera Canon EOS - 3` (20 kar), Asset ID `CAM-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar), Source `Manual` (6 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-11-03T04:00:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-101-7** Damage record (awal), Record Damaged berpenanda Reported Missing: Name `Drill Bosch GSB - 6` (19 kar), Asset ID `DRL-2026-0006` (13 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Penanda `Reported Missing` (16 kar), Source `Manual` (6 kar), Last Holder `Sari Dewi` (9 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-10-28T03:00:00Z` (20 kar) · sumber PRD §4.1a Example Data
- **DU-101-8** Damage record (awal), Record Damaged dilaporkan pada hari ini: Name `Laptop Dell Latitude 5420 - 6` (29 kar), Asset ID `LPT-2026-0006` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Missing asset` (13 kar), Reported By `Rina Wijaya` (11 kar), Reported Date `2026-11-11T08:20:00Z` (20 kar), Days Damaged `0 days` (6 kar) · sumber PRD §4.1a Example Data
- **DU-101-9** Damage record (awal), Record Damaged dengan tanggal laporan dekat tengah malam dan hari lebih dari 12: Name `Generator Set Cummins C100 - 1` (30 kar), Asset ID `GEN-2026-0001` (13 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Source `Stock opname` (12 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-03-24T23:30:00Z` (20 kar), Days Damaged `231 days` (8 kar) · sumber turunan penulis
- **DU-101-10** Damage record (awal), Record Damaged dengan seluruh kolom terisi: Photo `tablet-samsung-tab-a8-3.jpg` (27 kar), Name `Tablet Samsung Tab A8 - 3` (25 kar), Asset ID `TAB-2026-0003` (13 kar), Brand `Samsung` (7 kar), Model/Type `Galaxy Tab A8` (13 kar), TAG `['RFID', 'QR']` (14 kar), Category `Tablet` (6 kar), Category Hierarchy `IT Equipment > Tablet` (21 kar), Group `Server Room` (11 kar), Group Hierarchy `Head Office > Floor 2 > Server Room` (35 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `Dewi Anggraini` (14 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-11-07T03:30:00Z` (20 kar), Days Damaged `4 days` (6 kar), Alias Name `Tab Gudang` (10 kar), Measurement `Unit` (4 kar), Division `Operations` (10 kar), Labels `['Warehouse', 'Fragile', 'Priority']` (36 kar), Asset Class `Electronic` (10 kar), Register Date `2026-01-15` (10 kar), Purchase Date `2026-01-10` (10 kar), Warranty Expiry `2028-01-10` (10 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `9800000` (7 kar), Asset Value (Fiscal) `10200000` (8 kar), Modified By `Rina Wijaya` (11 kar), Last Updated `2026-11-10T02:30:00Z` (20 kar) · sumber turunan penulis
- **DU-101-11** Damage record (awal), Record Damaged dengan kolom tersembunyi tidak pernah diisi: Photo `None` (4 kar), Name `Forklift Toyota 8FD - 1` (23 kar), Asset ID `FLT-2026-0001` (13 kar), Brand `None` (4 kar), Model/Type `None` (4 kar), TAG `[]` (2 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Prasetyo` (13 kar), Alias Name `None` (4 kar), Measurement `None` (4 kar), Division `None` (4 kar), Labels `[]` (2 kar), Asset Class `None` (4 kar), Purchase Date `None` (4 kar), Warranty Expiry `None` (4 kar), Purchase Cost `None` (4 kar), Asset Value (Commercial) `None` (4 kar), Asset Value (Fiscal) `None` (4 kar) · sumber turunan penulis
- **DU-101-12** Damage record (awal), Record Damaged dengan teks panjang dan badge terpotong: Name `Handheld RFID Scanner Zebra TC21 Warehouse Receiving Dock Unit - 14` (67 kar), Asset ID `HSC-2026-0014` (13 kar), Brand `Zebra Technologies International Holdings` (41 kar), Group `Jakarta Selatan Distribution Center` (35 kar), Group Hierarchy `Region Jawa > Jakarta Selatan Distribution Center` (49 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Division `Regional Procurement and Vendor Management Office Jakarta` (57 kar), Labels `['Warehouse', 'Priority']` (25 kar), Reported By `Rina Wijaya` (11 kar) · sumber turunan penulis
- **DU-101-13** Damage record (awal), Record Damaged dengan satu label dan nilai nol: Name `Folding Chair Ergo - 4` (22 kar), Asset ID `CHR-2026-0004` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Labels `['Fragile']` (11 kar), Asset Value (Fiscal) `0` (1 kar), Reported By `Rina Wijaya` (11 kar) · sumber turunan penulis
- **DU-101-14** Damage record (awal), Record Damaged dengan nama aset berisi markup: Name `<b>Meeting</b> Table - 2` (24 kar), Asset ID `TBL-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya` (11 kar) · sumber turunan penulis
- **DU-101-15** Damage record (awal), Daftar record berjalan kosong untuk entitas yang belum pernah menerima laporan: Jumlah record `0` (1 kar) · sumber turunan penulis
- **DU-101-16** Damage record (awal), Record berjalan di luar cakupan Group aktor: Name `Toyota Avanza - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Branch Surabaya` (15 kar), Status `Damaged` (7 kar), Cakupan Group aktor `Head Office` (11 kar) · sumber turunan penulis
- **DU-101-18** Damage record (awal), Record Waiting for Confirmation dilaporkan PIC atas nama pemegang tanpa akun: Name `Handheld Scanner Zebra TC21 - 2` (31 kar), Asset ID `HSC-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Tono Rahmat` (11 kar), Last Holder Division `Finance` (7 kar), Last Holder PIC `Sinta Maharani` (14 kar), Last Holder Hover PIC `PIC: Sinta Maharani` (19 kar), Last Holder Employee ID `EMP-0217` (8 kar), Reported By `Sinta M on behalf of Tono R` (27 kar) · sumber PRD §4.1a Example Data
- **DU-101-17** Damage record (dicoba), Kata kunci Search yang tidak cocok dengan record mana pun: Search `Printer Hilang` (14 kar) · sumber turunan penulis
- **DU-102-1** Damage record (awal), Record Reported Disposal untuk baris pertama tabel: Name `Printer HP LaserJet M404 - 8` (28 kar), Asset ID `PRN-2026-0008` (13 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Reported By `Agus Prasetyo` (13 kar) · sumber PRD §4.1a Example Data
- **DU-102-2** Damage record (awal), Record In Disposal Process untuk baris kedua tabel: Name `Monitor Dell P2422H - 6` (23 kar), Asset ID `MON-2026-0006` (13 kar), Group `Warehouse` (9 kar), Status `In Disposal Process` (19 kar), Source `Manual` (6 kar), Reported By `Rina Wijaya` (11 kar) · sumber PRD §4.1a Example Data
- **DU-102-3** Damage record (awal), Record Damaged untuk baris ketiga tabel: Name `Camera Canon EOS - 3` (20 kar), Asset ID `CAM-2026-0003` (13 kar), Group `Branch Surabaya` (15 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Prasetyo` (13 kar) · sumber PRD §4.1a Example Data
- **DU-102-4** Damage record (awal), Sebelas nilai Source sebagai sumber opsi filter: Source `['Manual', 'Reported by scan', 'Reported by holder', 'Borrowed asset', 'Borrow return', 'Assigned asset', 'Assign return', 'Stock opname', 'Transfer receive', 'Missing asset', 'Registration']` (191 kar) · sumber PRD §9.2 9.2.1
- **DU-102-5** Damage record (awal), Pohon Group untuk filter: Group `['Head Office', 'Warehouse', 'Branch Surabaya']` (47 kar) · sumber turunan penulis
- **DU-102-6** Damage record (awal), Pohon Category untuk filter: Category `['Electronics', 'Furniture', 'Vehicle']` (39 kar) · sumber turunan penulis
- **DU-102-7** Damage record (awal; 25 record), Dua puluh lima record untuk tiga halaman: Name `Office Desk Standard - {n}` (26 kar), Asset ID `DSK-2026-{n}` (12 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber turunan penulis
- **DU-102-8** Damage record (awal), Jumlah baris hasil unduhan di atas ambang: Jumlah baris hasil unduhan `5.001` (5 kar) · sumber turunan penulis
- **DU-102-9** Damage record (dicoba), Kata kunci Search yang dicoba: Search 1 `Camera` (6 kar), Search 2 `Monitor` (7 kar) · sumber turunan penulis
- **DU-102-10** Damage record (dicoba), Kata kunci pencarian di dalam dropdown dan tree filter: Cari opsi Status `zzz` (3 kar), Cari tree Group `Branch` (6 kar), Cari tree Category `Furn` (4 kar) · sumber turunan penulis
- **DU-102-11** Damage record (dicoba), Nomor halaman yang dicoba: Nomor halaman 1 `0` (1 kar), Nomor halaman 2 `-1` (2 kar), Nomor halaman 3 `abc` (3 kar), Nomor halaman 4 `4` (1 kar) · sumber turunan penulis
- **DU-103-1** Damage record (awal), Record Damaged Group Head Office pertama: Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber PRD §4.1a Example Data
- **DU-103-2** Damage record (awal), Record Damaged Group Head Office kedua: Name `Tablet Samsung Tab A8 - 3` (25 kar), Asset ID `TAB-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber PRD §4.1a Example Data
- **DU-103-3** Damage record (awal), Record Damaged Group Branch Surabaya: Name `Toyota Avanza - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Branch Surabaya` (15 kar), Status `Damaged` (7 kar) · sumber PRD §4.1a Example Data
- **DU-103-4** Damage record (awal), Record Waiting for Confirmation: Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-103-5** Damage record (awal), Record Reported Disposal: Name `Printer HP LaserJet M404 - 8` (28 kar), Asset ID `PRN-2026-0008` (13 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar) · sumber PRD §4.1a Example Data
- **DU-103-6** Damage record (awal), Record In Disposal Process: Name `Monitor Dell P2422H - 6` (23 kar), Asset ID `MON-2026-0006` (13 kar), Group `Warehouse` (9 kar), Status `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-103-7** Damage record (awal), Record Damaged berpenanda Missing: Name `Camera Canon EOS - 3` (20 kar), Asset ID `CAM-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-103-8** Damage record (awal), Record Damaged berpenanda Reported Missing: Name `Drill Bosch GSB - 6` (19 kar), Asset ID `DRL-2026-0006` (13 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a Example Data
- **DU-103-9** Damage record (awal; 12 record), Dua belas record Damaged untuk dua halaman: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-10** Damage record (awal; 999 record), Satu record di bawah Selection Limit: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-11** Damage record (awal; 1000 record), Record tepat sebanyak Selection Limit: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-12** Damage record (awal; 1001 record), Record satu lebih banyak dari Selection Limit: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-13** Damage record (awal; 1200 record), Hasil saringan Group di atas Selection Limit: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-14** Damage record (awal; 6 record), Enam record dengan batas diturunkan menjadi lima: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-15** Damage record (awal; 300 record), Tiga ratus record Group lain yang tidak lolos saringan: Name `Hand Truck Steel - {n}` (22 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-16** Damage record (dicoba), Reason yang dikirim pada dialog Report Disposal: Reason `Kerusakan tidak dapat diperbaiki` (32 kar) · sumber turunan penulis
- **DU-103-17** Damage record (awal; 4 record), Empat record Damaged dengan batas diturunkan menjadi lima: Name `Hydraulic Jack Steel - {n}` (26 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber turunan penulis
- **DU-103-18** Damage record (awal), Record Waiting for Confirmation yang checkbox-nya Disabled: Name `Welding Machine Lincoln - 1` (27 kar), Asset ID `WLD-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar) · sumber turunan penulis
- **DU-103-19** Damage record (awal), Record Reported Disposal yang checkbox-nya Disabled: Name `Welding Machine Lincoln - 2` (27 kar), Asset ID `WLD-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar) · sumber turunan penulis
- **DU-103-20** Damage record (awal), Record In Disposal Process yang checkbox-nya Disabled: Name `Welding Machine Lincoln - 3` (27 kar), Asset ID `WLD-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar) · sumber turunan penulis
- **DU-104-1** Damage record (awal), Record Waiting for Confirmation dilaporkan pengguna lain: Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar), Reported By `Budi Santoso` (12 kar) · sumber PRD §4.1a Example Data
- **DU-104-3** Damage record (awal), Record Damaged dari Pelapor admin: Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar) · sumber PRD §4.1a Example Data
- **DU-104-4** Damage record (awal), Record Reported Disposal: Name `Printer HP LaserJet M404 - 8` (28 kar), Asset ID `PRN-2026-0008` (13 kar), Group `Head Office` (11 kar), Status `Reported Disposal` (17 kar) · sumber PRD §4.1a Example Data
- **DU-104-5** Damage record (awal), Record In Disposal Process: Name `Monitor Dell P2422H - 6` (23 kar), Asset ID `MON-2026-0006` (13 kar), Group `Head Office` (11 kar), Status `In Disposal Process` (19 kar) · sumber PRD §4.1a Example Data
- **DU-104-6** Damage record (awal), Record Damaged berpenanda Missing: Name `Camera Canon EOS - 3` (20 kar), Asset ID `CAM-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-104-7** Damage record (awal), Record Damaged berpenanda Reported Missing: Name `Drill Bosch GSB - 6` (19 kar), Asset ID `DRL-2026-0006` (13 kar), Group `Warehouse` (9 kar), Status `Damaged` (7 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a Example Data
- **DU-104-8** Damage record (awal), Pelaku perubahan status terakhir berupa user: Pelaku perubahan terakhir `Rina Wijaya` (11 kar), Status sesudah muat ulang `Damaged` (7 kar) · sumber turunan penulis
- **DU-104-9** Damage record (awal), Pelaku perubahan status terakhir tanpa user aktor: Pelaku perubahan terakhir `System` (6 kar), Status sesudah muat ulang `Damaged` (7 kar) · sumber turunan penulis
- **DU-104-10** Damage record (dicoba), Reason yang dikirim pada dialog Report Disposal: Reason `Kerusakan tidak dapat diperbaiki` (32 kar) · sumber turunan penulis
- **DU-106-1** Damage record (awal), Record Repaired dengan Resolved By user: Name `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Status `Repaired` (8 kar), Source `Borrow return` (13 kar), Photo `laptop-dell-latitude-5420-9.jpg` (31 kar), Last Holder `Sari Dewi` (9 kar), Last Holder Division `Operations` (10 kar), Last Holder Employee ID `EMP-0145` (8 kar), Reported By `Rina Wijaya` (11 kar), Reported Date `2026-10-12T02:00:00Z` (20 kar), Duration `6 days` (6 kar), Resolved By `Rina Wijaya` (11 kar), Resolved Date `2026-10-18T07:10:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-106-2** Damage record (awal), Record Disposed dengan Resolved By System: Name `Drill Bosch GSB - 4` (19 kar), Asset ID `DRL-2026-0004` (13 kar), Group `Warehouse` (9 kar), Status `Disposed` (8 kar), Source `Stock opname` (12 kar), Reported By `Agus Prasetyo` (13 kar), Reported Date `2026-08-01T01:00:00Z` (20 kar), Duration `62 days` (7 kar), Resolved By `System` (6 kar), Resolved Date `2026-10-01T17:00:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-106-3** Damage record (awal), Record Rejected: Name `Camera Canon EOS - 1` (20 kar), Asset ID `CAM-2026-0001` (13 kar), Group `Head Office` (11 kar), Status `Rejected` (8 kar), Source `Reported by holder` (18 kar), Reported By `Budi` (4 kar), Reported Date `2026-11-05T01:30:00Z` (20 kar), Duration `1 day` (5 kar), Resolved By `Rina Wijaya` (11 kar), Resolved Date `2026-11-06T02:15:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-106-4** Damage record (awal), Record Canceled: Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Reported By `Dewi Anggraini` (14 kar), Reported Date `2026-11-08T03:00:00Z` (20 kar), Duration `1 day` (5 kar), Resolved By `Dewi Anggraini` (14 kar), Resolved Date `2026-11-09T01:00:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-106-5** Damage record (awal), Daftar record selesai kosong untuk entitas yang belum menyelesaikan record: Jumlah record `0` (1 kar) · sumber turunan penulis
- **DU-106-6** Damage record (dicoba), Kata kunci Search yang tidak cocok dengan record mana pun: Search `Printer Hilang` (14 kar) · sumber turunan penulis
- **DU-106-7** Damage record (awal), Record Repaired dengan pemegang tanpa akun dan laporan PIC: Name `Handheld Scanner Zebra TC21 - 2` (31 kar), Asset ID `HSC-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Repaired` (8 kar), Source `Reported by holder` (18 kar), Last Holder `Tono Rahmat` (11 kar), Last Holder Division `Finance` (7 kar), Last Holder PIC `Sinta Maharani` (14 kar), Last Holder Hover PIC `PIC: Sinta Maharani` (19 kar), Last Holder Employee ID `EMP-0217` (8 kar), Reported By `Sinta M on behalf of Tono R` (27 kar), Reported Date `2026-11-03T02:30:00Z` (20 kar), Duration `2 days` (6 kar), Resolved By `Rina Wijaya` (11 kar), Resolved Date `2026-11-05T04:00:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-106-8** Damage record (awal), Record Repaired Source Registration tanpa Damaged Photo: Photo `None` (4 kar), Name `Projector Epson EB-X06 - 5` (26 kar), Asset ID `PRJ-2026-0005` (13 kar), Group `Head Office` (11 kar), Status `Repaired` (8 kar), Source `Registration` (12 kar), Reported By `Rina Wijaya` (11 kar), Reported Date `2026-11-02T02:00:00Z` (20 kar), Duration `3 days` (6 kar), Resolved By `Rina Wijaya` (11 kar), Resolved Date `2026-11-05T06:45:00Z` (20 kar) · sumber PRD §4.1b Example Data
- **DU-107-1** Damage record (awal), Record Active Damaged pertama: Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Borrow return` (13 kar), Reported By `Rina Wijaya` (11 kar) · sumber PRD §4.1a Example Data
- **DU-107-2** Damage record (awal), Record Active Damaged kedua: Name `Camera Canon EOS - 3` (20 kar), Asset ID `CAM-2026-0003` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Reported By `Agus Prasetyo` (13 kar) · sumber PRD §4.1a Example Data
- **DU-107-3** Damage record (awal), Record History Repaired pertama: Name `Laptop Dell Latitude 5420 - 9` (29 kar), Asset ID `LPT-2026-0009` (13 kar), Group `Head Office` (11 kar), Status `Repaired` (8 kar), Source `Borrow return` (13 kar), Reported By `Rina Wijaya` (11 kar), Resolved By `Rina Wijaya` (11 kar) · sumber PRD §4.1b Example Data
- **DU-107-4** Damage record (awal), Record History Repaired kedua: Name `Toyota Avanza - 1` (17 kar), Asset ID `VEH-2026-0001` (13 kar), Group `Branch Surabaya` (15 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Reported By `Agus Prasetyo` (13 kar), Resolved By `Agus Prasetyo` (13 kar) · sumber PRD §4.1b Example Data
- **DU-107-5** Damage record (dicoba), Kata kunci Search per sub-tab yang dicoba: Search sub-tab Active `Camera` (6 kar), Search sub-tab History `Laptop` (6 kar), Filter Source sub-tab Active `Manual` (6 kar) · sumber turunan penulis
- **DU-107-6** Damage record (awal; 12 record), Dua belas record Active untuk dua halaman: Name `Pallet Jack Manual - {n}` (24 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar) · sumber turunan penulis
- **DU-107-7** Damage record (awal; 12 record), Dua belas record History untuk dua halaman: Name `Hand Truck Steel - {n}` (22 kar), Group `Head Office` (11 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar) · sumber turunan penulis
- **DU-110-1** Asset (awal), Aset tanpa pemegang, satu aset terpilih: Asset Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Holder `tanpa pemegang` (14 kar) · sumber PRD §4.1a Example Data
- **DU-110-2** Asset (awal), Aset sedang dipinjam, satu aset terpilih: Asset Name `Tablet Samsung Tab A8 - 3` (25 kar), Asset ID `TAB-2026-0003` (13 kar), Group `Head Office` (11 kar), Holder `Dewi A` (6 kar) · sumber PRD §4.1a Example Data
- **DU-110-3** Asset (awal), Aset dipinjam Sari D, pertama dari empat aset terpilih: Asset Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar), Holder `Sari D` (6 kar) · sumber PRD §4.1a Example Data
- **DU-110-4** Asset (awal), Aset dipinjam Sari D, kedua dari empat aset terpilih: Asset Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Head Office` (11 kar), Holder `Sari D` (6 kar) · sumber PRD §4.1a Example Data
- **DU-110-5** Asset (awal), Aset ditugaskan kepada Tono R, ketiga dari empat aset terpilih: Asset Name `Handheld Scanner Zebra TC21 - 2` (31 kar), Asset ID `HSC-2026-0002` (13 kar), Group `Head Office` (11 kar), Holder `Tono R` (6 kar) · sumber PRD §4.1a Example Data
- **DU-110-6** Asset (awal), Aset tanpa pemegang, keempat dari empat aset terpilih: Asset Name `Office Chair Ergo - 31` (22 kar), Asset ID `CHR-2026-0031` (13 kar), Group `Branch Surabaya` (15 kar), Holder `tanpa pemegang` (14 kar) · sumber PRD §4.1a Example Data
- **DU-110-7** Asset (awal), Aset layak dilaporkan di antara empat aset terpilih: Asset Name `Toyota Avanza - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Head Office` (11 kar), Holder `tanpa pemegang` (14 kar) · sumber PRD §4.1a Example Data
- **DU-110-8** Asset (awal), Aset yang sudah punya record berjalan: Asset Name `Drill Bosch GSB - 6` (19 kar), Asset ID `DRL-2026-0006` (13 kar), Group `Head Office` (11 kar), Keterangan `Already reported damaged` (24 kar) · sumber PRD §4.1a Example Data
- **DU-110-9** Asset (awal), Aset Disposed: Asset Name `Forklift Toyota 8FD - 1` (23 kar), Asset ID `FLT-2026-0001` (13 kar), Group `Head Office` (11 kar), Keterangan `Can't be reported damaged` (25 kar) · sumber PRD §4.1b Example Data
- **DU-110-10** Asset (awal), Aset di luar Group tempat pengguna memegang Update: Asset Name `Office Chair Ergo - 18` (22 kar), Asset ID `CHR-2026-0018` (13 kar), Group `Branch Surabaya` (15 kar), Keterangan `Can't be reported damaged` (25 kar) · sumber PRD §4.1b Example Data
- **DU-110-11** Report Damaged (awal), Isian awal What happened dari titik masuk: What happened `Layar retak setelah terjatuh dari meja` (38 kar) · sumber turunan penulis
- **DU-110-12** Report Damaged (dibuat), What happened yang diketik pelapor: What happened `Layar retak dan perangkat tidak menyala` (39 kar) · sumber turunan penulis
- **DU-110-13** Report Damaged (dibuat), Berkas foto kerusakan yang dipilih: Damaged Photo proyektor `kerusakan-proyektor.jpg` (23 kar), Damaged Photo handheld `kerusakan-handheld.jpg` (22 kar), Damaged Photo laptop `kerusakan-laptop.jpg` (20 kar) · sumber turunan penulis
- **DU-111-1** Asset (awal), Satu aset terpilih: Asset Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1a Example Data
- **DU-111-2** Asset (awal), Aset pertama dari dua aset terpilih: Asset Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1a Example Data
- **DU-111-3** Asset (awal), Aset kedua dari dua aset terpilih: Asset Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1b Example Data
- **DU-111-4** Report Damaged (dicoba), What happened kosong dan foto tidak dipilih: What happened `` (0 kar), Damaged Photo `` (0 kar) · sumber FLD-DMG-01
- **DU-111-5** Report Damaged (dicoba), What happened hanya spasi: What happened `   ` (3 kar) · sumber FLD-DMG-01
- **DU-111-6** Report Damaged (dibuat), What happened tepat 360 karakter: What happened `Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipakai bekerja. Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipak` (360 kar) · sumber FLD-DMG-01
- **DU-111-7** Report Damaged (dicoba), What happened 361 karakter: What happened `Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipakai bekerja. Layar laptop retak di bagian tengah setelah terjatuh dari meja rapat lantai tiga saat dipindahkan oleh staf gudang, sehingga tampilan bergaris dan perangkat tidak dapat dipaka` (361 kar) · sumber FLD-DMG-01
- **DU-111-8** Report Damaged (dibuat), What happened 360 karakter dengan spasi ganda di tengah: What happened `Layar  laptop  retak  di  bagian  tengah  setelah  terjatuh  dari  meja  rapat  lantai  tiga  saat  dipindahkan  oleh  staf  gudang,  sehingga  tampilan  bergaris  dan  perangkat  tidak  dapat  dipakai  bekerja.  Layar  laptop  retak  di  bagian  tengah  setelah  terjatuh  dari  meja  rapat  lantai  tiga  saat  dipindahkan  oleh  staf  gudang,  sehingga  tam` (360 kar) · sumber FLD-DMG-01
- **DU-111-9** Report Damaged (dibuat), What happened 360 code point dengan huruf beraksen dan karakter non-BMP: What happened `Lénsa kaméra Cañon retak sesudah terjatuh dari rak Gudang Pusat Jakarta 𝒜 dan bingkai logam melengkung hingga penutup lensa tidak dapat dipasang kembali oleh teknisi lapangan Ünit Perawatan, sehingga perangkat dinyatakan tidak layak dipakai untuk pengambilan foto aset di lokasi. Lénsa kaméra Cañon retak sesudah terjatuh dari rak Gudang Pusat Jakarta 𝒜 dan bi` (360 kar) · sumber FLD-DMG-01
- **DU-111-10** Damaged Photo (dibuat), Foto JPEG 512 KB: Damaged Photo `kerusakan-layar.jpeg` (20 kar), Format `JPEG` (4 kar), Ukuran `512 KB` (6 kar) · sumber FLD-DMG-02
- **DU-111-11** Damaged Photo (dibuat), Foto PNG tepat 1 MB: Damaged Photo `kerusakan-layar.png` (19 kar), Format `PNG` (3 kar), Ukuran `1 MB` (4 kar) · sumber FLD-DMG-02
- **DU-111-12** Damaged Photo (dicoba), Berkas PDF dipilih sebagai foto: Damaged Photo `catatan-kerusakan.pdf` (21 kar), Format `PDF` (3 kar), Ukuran `300 KB` (6 kar) · sumber FLD-DMG-02
- **DU-111-13** Damaged Photo (dibuat), Foto JPEG 2 MB: Damaged Photo `kerusakan-layar-besar.jpeg` (26 kar), Format `JPEG` (4 kar), Ukuran `2 MB` (4 kar) · sumber FLD-DMG-02
- **DU-112-1** Asset (awal), Satu aset terpilih: Asset Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1a Example Data
- **DU-112-2** Asset (awal), Aset pertama dari dua aset terpilih: Asset Name `Projector Epson EB-X06 - 2` (26 kar), Asset ID `PRJ-2026-0002` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1a Example Data
- **DU-112-3** Asset (awal), Aset kedua dari dua aset terpilih: Asset Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Asset ID `SCN-2026-0002` (13 kar), Group `Head Office` (11 kar) · sumber PRD §4.1b Example Data
- **DU-112-4** Report Damaged (dibuat), Laporan valid lengkap satu aset: What happened `Layar retak dan perangkat tidak menyala` (39 kar), Damaged Photo `kerusakan-layar.jpeg` (20 kar) · sumber turunan penulis
- **DU-112-5** Report Damaged (dibuat), Laporan valid lengkap dua aset: What happened `Bodi perangkat retak dan tidak dapat dipakai` (44 kar), Damaged Photo proyektor `kerusakan-proyektor.jpeg` (24 kar), Damaged Photo scanner `kerusakan-scanner.jpeg` (22 kar) · sumber turunan penulis
- **DU-113-1** Damage record (awal), Record Damaged aset ber-TAG: Asset Name `Laptop Dell Latitude 5420 - 6` (29 kar), Asset ID `LPT-2026-0006` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a Example Data
- **DU-113-2** Damage record (awal), Record Damaged aset tanpa TAG: Asset Name `Toyota Avanza - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), TAG `tanpa TAG` (9 kar) · sumber PRD §4.1a Example Data
- **DU-113-3** Setting (awal), After photo required nilai bawaan: After photo required `OFF` (3 kar) · sumber PRD §4.2.4 FI-DMG-12
- **DU-113-4** Setting (awal), After photo required diubah menjadi ON: After photo required `ON` (2 kar) · sumber PRD §4.2.4 FI-DMG-11
- **DU-113-5** Mark as Repaired (dibuat), Repair note yang diketik: Repair note `Layar diganti baru dan sudah diuji fungsi` (41 kar) · sumber turunan penulis
- **DU-114-1** Damage record (awal), Record Damaged aset ber-TAG: Asset Name `Laptop Dell Latitude 5420 - 6` (29 kar), Asset ID `LPT-2026-0006` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a Example Data
- **DU-114-2** Damage record (awal), Record Damaged aset tanpa TAG: Asset Name `Toyota Avanza - 2` (17 kar), Asset ID `VEH-2026-0002` (13 kar), Group `Head Office` (11 kar), Status `Damaged` (7 kar), TAG `tanpa TAG` (9 kar) · sumber PRD §4.1a Example Data
- **DU-114-3** Setting (awal), After photo required OFF: After photo required `OFF` (3 kar) · sumber PRD §4.2.4 FI-DMG-12
- **DU-114-4** Setting (awal), After photo required ON: After photo required `ON` (2 kar) · sumber PRD §4.2.4 FI-DMG-11
- **DU-114-5** TAG (awal), Hasil pindai TAG milik aset: TAG `RFID-LPT-0006` (13 kar), Asset ID `LPT-2026-0006` (13 kar) · sumber turunan penulis
- **DU-114-6** TAG (awal), Hasil pindai TAG bukan milik aset: TAG `RFID-CHR-0031` (13 kar), Asset ID `CHR-2026-0031` (13 kar) · sumber turunan penulis
- **DU-114-7** Mark as Repaired (dicoba), Repair note kosong: Repair note `` (0 kar) · sumber FLD-DMG-05
- **DU-114-8** Mark as Repaired (dicoba), Repair note hanya spasi: Repair note `   ` (3 kar) · sumber FLD-DMG-05
- **DU-114-9** Mark as Repaired (dibuat), Repair note tepat 360 karakter: Repair note `Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemegang. Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke peme` (360 kar) · sumber FLD-DMG-05
- **DU-114-10** Mark as Repaired (dicoba), Repair note 361 karakter: Repair note `Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemegang. Panel layar diganti dengan unit baru dari pemasok resmi, konektor daya dibersihkan, lalu perangkat diuji menyala selama dua jam tanpa gangguan sebelum diserahkan kembali ke pemeg` (361 kar) · sumber FLD-DMG-05
- **DU-114-11** Mark as Repaired (dibuat), Repair note 360 karakter dengan spasi ganda: Repair note `Panel  layar  diganti  dengan  unit  baru  dari  pemasok  resmi,  konektor  daya  dibersihkan,  lalu  perangkat  diuji  menyala  selama  dua  jam  tanpa  gangguan  sebelum  diserahkan  kembali  ke  pemegang.    Panel  layar  diganti  dengan  unit  baru  dari  pemasok  resmi,  konektor  daya  dibersihkan,  lalu  perangkat  diuji  menyala  selama  dua  jam  ta` (360 kar) · sumber FLD-DMG-05
- **DU-114-12** Mark as Repaired (dibuat), Repair note 360 code point beraksen dan non-BMP: Repair note `Lénsa kaméra Cañon diganti oleh teknisi Ünit Perawatan Jakarta 𝒜 dan mekanisme fokus dikalibrasi ulang, kemudian perangkat diuji mengambil foto aset di gudang pusat tanpa gangguan selama satu jam penuh sebelum dikembalikan ke rak peminjaman karyawan lapangan, dengan catatan servis dilampirkan pada berkas perawatan. Lénsa kaméra Cañon diganti oleh teknisi Üni` (360 kar) · sumber FLD-DMG-05
- **DU-114-13** After photo (dibuat), After photo JPEG 512 KB: After photo `foto-sesudah.jpeg` (17 kar), Format `JPEG` (4 kar), Ukuran `512 KB` (6 kar) · sumber FLD-DMG-04
- **DU-114-14** After photo (dibuat), After photo PNG tepat 1 MB: After photo `foto-sesudah.png` (16 kar), Format `PNG` (3 kar), Ukuran `1 MB` (4 kar) · sumber FLD-DMG-04
- **DU-114-15** After photo (dicoba), Berkas PDF dipilih sebagai foto: After photo `catatan-servis.pdf` (18 kar), Format `PDF` (3 kar), Ukuran `300 KB` (6 kar) · sumber FLD-DMG-04
- **DU-114-16** After photo (dibuat), After photo JPEG 2 MB: After photo `foto-sesudah-besar.jpeg` (23 kar), Format `JPEG` (4 kar), Ukuran `2 MB` (4 kar) · sumber FLD-DMG-04
- **DU-114-17** After photo (dibuat), After photo tidak dipilih saat opsional: After photo `` (0 kar) · sumber FLD-DMG-04
- **DU-114-18** After photo (dicoba), After photo tidak dipilih saat wajib: After photo `` (0 kar) · sumber FLD-DMG-04
- **DU-114-19** Mark as Repaired (dibuat), Pengisian valid lengkap: Repair note `Layar diganti baru dan sudah diuji fungsi` (41 kar), Scan TAG `RFID-LPT-0006` (13 kar) · sumber turunan penulis
- **DU-115-1** Damage record (awal), Laporan Waiting for Confirmation yang akan ditolak: Asset Name `Laptop Dell Latitude 5420 - 4` (29 kar), Asset ID `LPT-2026-0004` (13 kar), Group `Head Office` (11 kar), Status `Waiting for Confirmation` (24 kar) · sumber PRD §4.1a Example Data
- **DU-115-2** Reject Report (dicoba), Reason kosong: Reason `` (0 kar) · sumber FLD-DMG-06
- **DU-115-3** Reject Report (dicoba), Reason hanya spasi: Reason `   ` (3 kar) · sumber FLD-DMG-06
- **DU-115-4** Reject Report (dibuat), Reason tepat 360 karakter: Reason `Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat diverifikasi oleh admin aset pada saat peninjauan laporan. Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat d` (360 kar) · sumber FLD-DMG-06
- **DU-115-5** Reject Report (dicoba), Reason 361 karakter: Reason `Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat diverifikasi oleh admin aset pada saat peninjauan laporan. Laporan ditolak karena foto yang dilampirkan memperlihatkan perangkat lain dan bukan aset yang dimaksud, sehingga kerusakan pada aset ini tidak dapat di` (361 kar) · sumber FLD-DMG-06
- **DU-115-6** Reject Report (dibuat), Reason 360 karakter dengan spasi ganda: Reason `Laporan  ditolak  karena  foto  yang  dilampirkan  memperlihatkan  perangkat  lain  dan  bukan  aset  yang  dimaksud,  sehingga  kerusakan  pada  aset  ini  tidak  dapat  diverifikasi  oleh  admin  aset  pada  saat  peninjauan  laporan.    Laporan  ditolak  karena  foto  yang  dilampirkan  memperlihatkan  perangkat  lain  dan  bukan  aset  yang  dimaksud,  s` (360 kar) · sumber FLD-DMG-06
- **DU-115-7** Reject Report (dibuat), Reason 360 code point beraksen dan non-BMP: Reason `Laporan ditolak karena lensa kaméra Cañon pada foto bukan milik Ünit Gudang Pusat Jakarta 𝒜 dan nomor seri pada badan perangkat tidak cocok dengan data aset, sehingga laporan tidak dapat dilanjutkan sampai pelapor melampirkan foto yang benar dan keterangan kerusakan yang lebih jelas bagi admin aset di lokasi. Laporan ditolak karena lensa kaméra Cañon pada fo` (360 kar) · sumber FLD-DMG-06
- **DU-115-8** Reject Report (dibuat), Pengisian valid lengkap: Reason `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan` (58 kar) · sumber turunan penulis
- **DU-116-1** Damage record (awal), Laporan menunggu review: Asset Name `Laptop Dell Latitude 5420 - 4` (29 kar), Status `Waiting for Confirmation` (24 kar), Node `Reported damaged by Budi S` (26 kar), Holder `Budi S` (6 kar), Reported By `Budi S` (6 kar), Tanggal laporan `10/11/26, 08:15` (15 kar), What happened `Layar retak setelah terjatuh dari meja` (38 kar), Damaged Photo `kerusakan-layar.jpeg` (20 kar) · sumber PRD §4.1a Example Data
- **DU-116-2** Damage record (awal), Record Damaged pertama dalam daftar: Asset Name `Projector Epson EB-X06 - 2` (26 kar), Status `Damaged` (7 kar), Holder `Sari D` (6 kar), Reported By `Rina W` (6 kar) · sumber PRD §4.1a Example Data
- **DU-116-3** Damage record (awal), Record Damaged terakhir dalam daftar: Asset Name `Tablet Samsung Tab A8 - 3` (25 kar), Status `Damaged` (7 kar), Holder `Dewi A` (6 kar), Reported By `Agus P` (6 kar) · sumber PRD §4.1a Example Data
- **DU-116-4** User (awal), Aktor Damaged bukan pelapor: Name `Rina W` (6 kar), Hak `Aktor Damaged pada Group Head Office` (36 kar) · sumber matriks role PRD
- **DU-116-5** User (awal), Pelapor yang juga Aktor Damaged: Name `Budi S` (6 kar), Hak `Aktor Damaged pada Group Head Office` (36 kar) · sumber matriks role PRD
- **DU-116-6** Damage record (awal), Laporan menunggu review berpenanda Reported Missing: Asset Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Status `Waiting for Confirmation` (24 kar), Penanda `Reported Missing` (16 kar), Holder `Dewi A` (6 kar), Reported By `Dewi A` (6 kar) · sumber PRD §4.1a Example Data
- **DU-116-7** Damage record (awal), Record Damaged berpenanda Missing: Asset Name `Camera Canon EOS - 3` (20 kar), Status `Damaged` (7 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a Example Data
- **DU-116-8** Reject Report (dibuat), Reason yang diketik: Reason `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan` (58 kar) · sumber turunan penulis
- **DU-116-9** Damage record (awal), Node Pelapor admin: Asset Name `Toyota Avanza - 2` (17 kar), Node `Reported damaged by Agus P` (26 kar), What happened `Rem tidak berfungsi saat dipakai` (32 kar), Damaged Photo `kerusakan-rem.jpeg` (18 kar) · sumber PRD §4.1a Example Data
- **DU-116-10** Damage record (awal), Node PIC atas nama karyawan: Asset Name `Handheld Scanner Zebra TC21 - 2` (31 kar), Node `Reported damaged by Sinta M on behalf of Tono R` (47 kar) · sumber PRD §4.1a Example Data
- **DU-116-11** Damage record (awal), Node Registration tanpa foto: Asset Name `Projector Epson EB-X06 - 5` (26 kar), Source `Registration` (12 kar), Node `Reported damaged by Agus P` (26 kar), What happened `Layar bergaris sejak didaftarkan` (32 kar) · sumber PRD §4.1a Example Data
- **DU-116-12** Damage record (awal), Node Confirm dan Reject: Node 1 `Report confirmed by Yoga T` (26 kar), Node 2 `Report rejected by Rina W` (25 kar), Reason `Foto tidak menunjukkan kerusakan pada aset yang dilaporkan` (58 kar) · sumber PRD §4.1a Example Data
- **DU-116-13** Damage record (awal), Node Cancel Report: Status `Canceled` (8 kar), Node `Report canceled by Budi S` (25 kar) · sumber PRD §4.1a Example Data
- **DU-116-14** Damage record (awal), Node peristiwa Missing: Node 1 `Asset reported missing` (22 kar), Node 2 `Missing report closed` (21 kar), Node 3 `Asset found` (11 kar), Pelaku `System` (6 kar) · sumber PRD §4.1a Example Data
- **DU-116-15** Damage record (awal), Node Marked as repaired: Status `Repaired` (8 kar), Node `Marked as repaired by Rina W` (28 kar), Repair note `Panel layar diganti dan diuji` (29 kar), After photo `foto-sesudah.jpeg` (17 kar), Manual identification `Identifikasi manual dicatat` (27 kar) · sumber PRD §4.1a Example Data
- **DU-116-16** Damage record (awal), Node peristiwa Disposal: Node 1 `Disposal reported by Agus P` (27 kar), Node 2 `Disposal report declined by Dedi K` (34 kar), Node 3 `Disposal report canceled by Agus P` (34 kar), Report ID `RPT-DSP-0001` (12 kar), Reason `Aset tidak ekonomis diperbaiki` (30 kar), Back to Damaged `Back to Damaged` (15 kar) · sumber PRD §4.1a Example Data
- **DU-116-17** Damage record (awal), Node Disposal report canceled oleh System: Node `Disposal report canceled by System` (34 kar), Report ID `RPT-DSP-0002` (12 kar), Back to Damaged `Back to Damaged` (15 kar) · sumber PRD §4.1a Example Data
- **DU-116-18** Damage record (awal), Node Disposed: Status `Disposed` (8 kar), Node `Disposed` (8 kar), Pelaku `System` (6 kar), Disposal No. `DSP-2026-0007` (13 kar) · sumber PRD §4.1a Example Data
- **DU-116-19** User (awal), Pengguna Read Only tanpa hak Aktor Damaged: Name `Lia N` (5 kar), Hak `Read Only, cakupan seluruh client` (33 kar) · sumber matriks role PRD
- **DU-116-20** User (awal), Pemegang Manage asset & TAG (Read) tanpa hak Update: Name `Joko T` (6 kar), Hak `Manage asset & TAG (Read) pada Group Head Office beserta descendant` (67 kar) · sumber matriks role PRD
- **DU-117-1** Damage record (awal), Laporan menunggu review yang akan dibatalkan: Asset Name `Scanner Fujitsu fi-7160 - 2` (27 kar), Asset ID `SCN-2026-0002` (13 kar), Status `Waiting for Confirmation` (24 kar), Pelapor `Dewi A` (6 kar) · sumber PRD §4.1b Example Data
- **DU-117-2** Damage record (awal), Status diubah admin menjadi Rejected: Diubah oleh `Rina W` (6 kar), Status `Rejected` (8 kar) · sumber PRD §4.1b Example Data
- **DU-117-3** Damage record (awal), Status diubah System: Diubah oleh `System` (6 kar) · sumber PRD §4.2.4 D-DMG-06
- **DU-119-1** Asset (awal), Aset yang sudah punya record berjalan: Asset Name `Drill Bosch GSB - 6` (19 kar), Asset ID `DRL-2026-0006` (13 kar), Keterangan `Already reported damaged` (24 kar) · sumber PRD §4.1a Example Data
- **DU-119-2** Asset (awal), Aset Disposed: Asset Name `Forklift Toyota 8FD - 1` (23 kar), Asset ID `FLT-2026-0001` (13 kar), Keterangan `Can't be reported damaged` (25 kar) · sumber PRD §4.1b Example Data
- **DU-119-3** Asset (awal), Aset di luar cakupan Update: Asset Name `Office Chair Ergo - 18` (22 kar), Asset ID `CHR-2026-0018` (13 kar), Keterangan `Can't be reported damaged` (25 kar) · sumber PRD §4.1b Example Data
- **DU-119-4** Asset (awal), Delapan aset tidak layak: Asset Name 1 `Office Chair Ergo - 1` (21 kar), Asset Name 2 `Office Chair Ergo - 2` (21 kar), Asset Name 3 `Office Chair Ergo - 3` (21 kar), Asset Name 4 `Office Chair Ergo - 4` (21 kar), Asset Name 5 `Office Chair Ergo - 5` (21 kar), Asset Name 6 `Office Chair Ergo - 6` (21 kar), Asset Name 7 `Office Chair Ergo - 7` (21 kar), Asset Name 8 `Office Chair Ergo - 8` (21 kar) · sumber turunan penulis
- **DU-201-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-201-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-201-3** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-201-4** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-201-5** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-201-6** User (awal), User pelapor umum, pemindai TAG: Name `Dedi Kurniawan {runId}` (22 kar), Role `pelapor umum, pemindai TAG` (26 kar), Cakupan `aset yang ia pindai` (19 kar) · sumber matriks role PRD
- **DU-201-7** User (awal), User Aktor Missing: Name `Hendra Saputra {runId}` (22 kar), Role `Aktor Missing` (13 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-201-8** User (awal), User Aktor Transfer: Name `Tono Riyadi {runId}` (19 kar), Role `Aktor Transfer` (14 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-201-9** User (awal), User pemilik sesi Stock Opname: Name `Sinta Marlina {runId}` (21 kar), Role `pemilik sesi Stock Opname` (25 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-201-10** Group (awal), Group tempat aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-201-11** Group (awal), Group di luar cakupan Update Rina Wulandari: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-201-12** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 1 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-13** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 3 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `Assigned kepada `Rina Wulandari {runId}`, tanpa record berjalan` (63 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-14** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 2 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `Borrowed oleh `Budi Santoso {runId}`, tanpa record berjalan` (59 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-15** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 6 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `Assigned kepada `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-16** Asset (awal), Aset uji: Name `Office Chair Ergo - 31 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-17** Asset (awal), Aset uji: Name `Camera Canon EOS - 1 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `Assigned kepada `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-18** Asset (awal), Aset uji: Name `Scanner Fujitsu fi-7160 - 2 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dengan What happened `Port charger patah`` (81 kar), Record berjalan `Waiting for Confirmation` (24 kar), What happened `Port charger patah` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-19** Asset (awal), Aset uji: Name `Toyota Avanza - 2 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dengan What happened `Kaca spion pecah`` (62 kar), Record berjalan `Damaged` (7 kar), What happened `Kaca spion pecah` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-20** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 8 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal` dengan What happened `Roller macet`` (68 kar), Record berjalan `Reported Disposal` (17 kar), What happened `Roller macet` (12 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-21** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 7 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan What happened `Panel bergaris`` (72 kar), Record berjalan `In Disposal Process` (19 kar), What happened `Panel bergaris` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-22** Asset (awal), Aset uji: Name `Drill Bosch GSB - 4 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `Disposed, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-23** Asset (awal), Aset uji: Name `Forklift Toyota 8FD - 1 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `Missing (hilang), tanpa record Damaged` (38 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-24** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 2 {runId}` (39 kar), Group `Branch Surabaya {runId}` (23 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-25** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 4 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-26** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 6 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-27** Asset (awal), Aset uji: Name `Toyota Avanza - 1 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-28** Asset (awal), Aset uji: Name `Toyota Avanza - 3 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-29** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 2 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-30** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 9 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `Assigned kepada `Budi Santoso {runId}`, punya record `Damaged` Source `Manual` dengan What happened `Engsel longgar`` (116 kar), Record berjalan `Damaged` (7 kar), What happened `Engsel longgar` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-31** Asset (awal), Aset uji: Name `Camera Canon EOS - 3 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `Missing (hilang) dengan Condition sebelumnya Damaged, punya record `Damaged` ditahan dengan What happened `Lensa berjamur`` (122 kar), Record berjalan `Damaged` (7 kar), What happened `Lensa berjamur` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-32** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 5 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `draf registrasi dengan Condition `Damaged` dan Damage note `Lensa tergores saat pengiriman`, belum Active` (105 kar), Damage note `Lensa tergores saat pengiriman` (30 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-33** Asset (awal), Aset uji: Name `Forklift Toyota 8FD - 2 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `dalam Transfer menuju `Branch Surabaya {runId}`, punya record `Damaged` dengan What happened `Garpu bengkok`` (108 kar), Record berjalan `Damaged` (7 kar), What happened `Garpu bengkok` (13 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-34** Asset (awal), Aset uji: Name `Drill Bosch GSB - 6 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `termasuk sesi Stock Opname milik `Sinta Marlina {runId}`, punya record `Damaged` dengan What happened `Mata bor patah`` (118 kar), Record berjalan `Damaged` (7 kar), What happened `Mata bor patah` (14 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-35** Damage evidence (dibuat), Bukti laporan: What happened `Layar retak setelah terjatuh dari meja` (38 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber turunan penulis
- **DU-201-36** Damage evidence (dibuat), Bukti laporan: What happened `Kursi roda patah saat dipakai` (29 kar), Damaged Photo `roda-patah.jpg` (14 kar) · sumber turunan penulis
- **DU-201-37** Damage evidence (dibuat), Bukti laporan: What happened `Laporan kedua atas aset yang sama` (33 kar), Damaged Photo `laporan-kedua.jpg` (17 kar) · sumber turunan penulis
- **DU-201-38** Damage evidence (dibuat), What happened tepat 360 karakter: What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengala` (360 kar), Damaged Photo `foto-360.jpg` (12 kar) · sumber FLD-DMG-01
- **DU-201-39** Damage evidence (dicoba), What happened 361 karakter: What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalay` (361 kar), Damaged Photo `foto-361.jpg` (12 kar) · sumber FLD-DMG-01
- **DU-201-40** Damage evidence (dicoba), What happened kosong: What happened `` (0 kar), Damaged Photo `foto-kosong.jpg` (15 kar) · sumber FLD-DMG-01
- **DU-201-41** Damage evidence (dicoba), Laporan tanpa Damaged Photo: What happened `Printer macet saat mencetak` (27 kar) · sumber FLD-DMG-02
- **DU-201-42** User (awal), User Group Manager: Name `Gita Permatasari {runId}` (24 kar), Role `Group Manager` (13 kar), Cakupan `Group binaan `Head Office {runId}` beserta sub-group` (52 kar) · sumber matriks role PRD
- **DU-201-43** User (awal), User pelapor umum, PIC karyawan tanpa akun: Name `Maya Kusuma {runId}` (19 kar), Role `pelapor umum, PIC karyawan tanpa akun` (37 kar), Cakupan `aset yang dipegang karyawan `Bagus Hartono {runId}`` (51 kar) · sumber matriks role PRD
- **DU-201-44** Employee (awal), Karyawan tanpa akun: Name `Bagus Hartono {runId}` (21 kar), PIC `Maya Kusuma {runId}` (19 kar) · sumber PRD §2 pelapor umum (BORROW-LOGIC-20)
- **DU-201-45** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 11 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, punya record `Repaired` selesai dengan What happened `Baterai kembung`, tanpa record berjalan` (101 kar), Record selesai `Repaired` (8 kar), What happened `Baterai kembung` (15 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-46** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 7 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `Borrowed oleh `Budi Santoso {runId}`, tanpa record berjalan` (59 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-47** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 5 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `Assigned kepada karyawan `Bagus Hartono {runId}` dengan PIC `Maya Kusuma {runId}`, tanpa record berjalan` (104 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-48** Asset (awal), Aset uji: Name `Office Chair Ergo - 33 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-49** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 9 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-50** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 12 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-51** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 4 {runId}` (39 kar), Group `Branch Surabaya {runId}` (23 kar), Keadaan `Normal, tanpa record berjalan` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-201-52** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 6 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `dalam Transfer menuju `Branch Surabaya {runId}`, tanpa record berjalan` (70 kar) · sumber turunan penulis
- **DU-202-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-202-2** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-202-3** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-202-4** User (awal), User Aktor Transfer: Name `Tono Riyadi {runId}` (19 kar), Role `Aktor Transfer` (14 kar), Cakupan `Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`` (63 kar) · sumber matriks role PRD
- **DU-202-5** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-202-6** User (awal), User pelapor umum, pemindai TAG: Name `Dedi Kurniawan {runId}` (22 kar), Role `pelapor umum, pemindai TAG` (26 kar), Cakupan `aset yang ia pindai` (19 kar) · sumber matriks role PRD
- **DU-202-7** Group (awal), Group asal aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-202-8** Group (awal), Group tujuan pemindahan aset: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-202-9** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 2 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (77 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-10** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 5 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (75 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-11** Asset (awal), Aset uji: Name `Camera Canon EOS - 2 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (77 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-12** Asset (awal), Aset uji: Name `Office Chair Ergo - 12 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Normal`, tanpa record berjalan` (45 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-13** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 3 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (77 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-14** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 3 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (77 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-15** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 7 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (75 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-16** Asset (awal), Aset uji: Name `Scanner Fujitsu fi-7160 - 3 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Normal`, tanpa record berjalan` (45 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-17** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 3 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Normal`, tanpa record berjalan` (45 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-18** Asset (awal), Aset uji: Name `Forklift Toyota 8FD - 3 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (76 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-19** Asset (awal), Aset uji: Name `Drill Bosch GSB - 3 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`` (78 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-20** Asset (awal), Aset uji: Name `Toyota Avanza - 4 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `TAG Reported`, punya record `Damaged`` (52 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-21** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 3 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Damaged`, punya record `Damaged`, tidak dipegang` (63 kar), TAG `tanpa TAG` (9 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-22** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 9 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (76 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-23** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 5 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`` (78 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-24** Damage evidence (dibuat), Bukti laporan: What happened `Layar retak setelah terjatuh {runId}` (36 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber turunan penulis
- **DU-202-25** Reject reason (dibuat), Alasan Reject laporan: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-202-26** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-202-27** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 8 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (75 kar), TAG `QR` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-28** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 10 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `TAG Reported`, dipegang `Budi Santoso {runId}`, tanpa record berjalan` (84 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-29** Asset (awal), Aset uji: Name `Forklift Toyota 8FD - 5 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (76 kar), TAG `RFID` (4 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-202-30** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 7 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (75 kar), TAG `QR` (2 kar) · sumber turunan penulis
- **DU-202-31** Asset (awal), Aset uji: Name `Camera Canon EOS - 7 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (77 kar), TAG `RFID` (4 kar) · sumber turunan penulis
- **DU-202-32** Asset (awal), Aset uji: Name `Drill Bosch GSB - 5 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `status global `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`` (78 kar), TAG `QR` (2 kar) · sumber turunan penulis
- **DU-203-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-203-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-203-3** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-203-4** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-203-5** User (awal), User Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Asset Admin sub-tab Disposal` (28 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-203-6** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-203-7** User (awal), User pelapor umum, pemindai TAG: Name `Dedi Kurniawan {runId}` (22 kar), Role `pelapor umum, pemindai TAG` (26 kar), Cakupan `aset yang ia pindai` (19 kar) · sumber matriks role PRD
- **DU-203-8** User (awal), User pelapor umum, kemudian pemegang Manage asset & TAG (Update): Name `Sari Dewanti {runId}` (20 kar), Role `pelapor umum, kemudian pemegang Manage asset & TAG (Update)` (59 kar), Cakupan `aset yang ia pegang, lalu Group `Head Office {runId}`` (53 kar) · sumber matriks role PRD
- **DU-203-9** User (awal), User pelapor umum, pemegang aset yang kemudian dinonaktifkan: Name `Hana Lestari {runId}` (20 kar), Role `pelapor umum, pemegang aset yang kemudian dinonaktifkan` (55 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-203-10** User (awal), User PIC pelapor atas nama karyawan tanpa akun `Tono Rahmat {runId}`: Name `Sinta Maharani {runId}` (22 kar), Role `PIC pelapor atas nama karyawan tanpa akun `Tono Rahmat {runId}`` (63 kar), Cakupan `aset yang dipegang `Tono Rahmat {runId}`` (40 kar) · sumber matriks role PRD
- **DU-203-11** User (awal), Karyawan tanpa akun: Name `Tono Rahmat {runId}` (19 kar), Role `karyawan tanpa akun, pemegang aset` (34 kar), Cakupan `aset yang ia pegang, dilaporkan lewat PIC` (41 kar) · sumber turunan penulis
- **DU-203-12** Damage record (awal), Pelapor laporan PIC atas nama: Reported By `Sinta Maharani {runId} on behalf of Tono Rahmat {runId}` (55 kar) · sumber PRD §4.1a T-DMG-01 Setup Column
- **DU-203-13** Damage record (awal), Waktu laporan awal: Waktu laporan `T0 − 90 hari, pukul 08:15` (25 kar) · sumber turunan penulis
- **DU-203-14** Group (awal), Group tempat aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-203-15** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 11 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-16** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 4 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Dedi Kurniawan {runId}` lewat scan TAG` (92 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-17** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 4 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-18** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 7 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya` (97 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-19** Asset (awal), Aset uji: Name `Scanner Fujitsu fi-7160 - 5 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Sinta Maharani {runId} on behalf of Tono Rahmat {runId}`` (110 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-20** Asset (awal), Aset uji: Name `Camera Canon EOS - 4 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Sari Dewanti {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-21** Asset (awal), Aset uji: Name `Toyota Avanza - 5 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dari laporan pemegang Update `Rina Wulandari {runId}`` (76 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-24** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 4 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya` (97 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-25** Asset (awal), Aset uji: Name `Office Chair Ergo - 20 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-26** Asset (awal), Aset uji: Name `Office Chair Ergo - 21 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-27** Asset (awal), Aset uji: Name `Office Chair Ergo - 22 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-28** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 6 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang, ber-TAG `RFID`` (54 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-29** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 7 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang, ber-TAG `RFID`` (54 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-30** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 10 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-31** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 12 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang, ber-TAG `RFID`` (54 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-32** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 13 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang` (38 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-33** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 14 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang, ber-TAG `RFID`` (54 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-34** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 15 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tidak dipegang, ber-TAG `RFID`` (54 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-35** Asset (awal), Aset uji: Name `Toyota Avanza - 6 {runId}` (25 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-36** Asset (awal), Aset uji: Name `Drill Bosch GSB - 8 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang status terakhirnya diubah `System` saat baris Disposal kedaluwarsa` (94 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-37** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 11 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Repaired`` (23 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-38** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 5 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Hana Lestari {runId}` sejak `T0 − 90 hari, pukul 08:15`` (109 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-203-39** Reject reason (dibuat), Alasan Reject laporan: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-203-40** Reject reason (dibuat), Reason tepat 360 karakter: Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,x` (360 kar) · sumber FLD-DMG-06
- **DU-203-41** Reject reason (dicoba), Reason 361 karakter: Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,xy` (361 kar) · sumber FLD-DMG-06
- **DU-203-42** Reject reason (dicoba), Reason kosong: Reason `` (0 kar) · sumber FLD-DMG-06
- **DU-203-43** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-203-44** Damage evidence (dibuat), Bukti laporan baru: What happened `Casing retak setelah terbentur {runId}` (38 kar), Damaged Photo `casing-retak.jpg` (16 kar) · sumber turunan penulis
- **DU-203-47** Asset (awal), Aset uji: Name `Camera Canon EOS - 5 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Sari Dewanti {runId}`` (75 kar) · sumber turunan penulis
- **DU-203-48** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 8 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Yoga Tanuwijaya {runId}` lewat halaman peminjaman` (143 kar) · sumber turunan penulis
- **DU-203-49** Asset (awal), Aset uji: Name `Camera Canon EOS - 6 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Dewi Anggraini {runId}` lewat halaman penugasan` (143 kar) · sumber turunan penulis
- **DU-204-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-204-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-204-3** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-204-4** Group (awal), Group tempat aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-204-5** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 21 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar), TAG `RFID-L21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-6** Asset (awal), Aset uji: Name `Laptop Dell Latitude 5420 - 22 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar), TAG `RFID-L22 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-7** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 21 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (62 kar), TAG `RFID-M21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-8** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 22 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`` (64 kar), TAG `RFID-M22 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-9** Asset (awal), Aset uji: Name `Forklift Toyota 8FD - 21 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, TAG tidak terbaca oleh pemindai` (55 kar), TAG `RFID-F21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-10** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 21 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar), TAG `RFID-P21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-11** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 22 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process`` (34 kar), TAG `RFID-P22 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-12** Asset (awal), Aset uji: Name `Camera Canon EOS - 21 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan pelapor umum `Budi Santoso {runId}`` (88 kar), TAG `RFID-C21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-13** Asset (awal), Aset uji: Name `Projector Epson EB-X06 - 23 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Registration` tanpa Damaged Photo` (64 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-14** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 21 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dari laporan `Rina Wulandari {runId}`` (60 kar), TAG `RFID-H21 {runId}` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-204-15** TAG (awal), TAG milik aset lain: Kode TAG `RFID-X99 {runId}` (16 kar) · sumber turunan penulis
- **DU-204-16** Asset (awal), Aset pemilik TAG lain: Name `Handheld Scanner Zebra TC21 - 21 {runId}` (40 kar), TAG `RFID-X99 {runId}` (16 kar) · sumber turunan penulis
- **DU-204-17** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-204-18** Repair note (dibuat), Repair note tepat 360 karakter: Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenx` (360 kar) · sumber FLD-DMG-05
- **DU-204-19** Repair note (dicoba), Repair note 361 karakter: Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenxy` (361 kar) · sumber FLD-DMG-05
- **DU-204-20** Repair note (dicoba), Repair note kosong: Repair note `` (0 kar) · sumber FLD-DMG-05
- **DU-204-21** After photo (dibuat), Foto sesudah perbaikan: After photo `perbaikan-{runId}.jpg` (21 kar) · sumber turunan penulis
- **DU-205-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-205-2** User (awal), User Group Manager: Name `Gunawan Hartono {runId}` (23 kar), Role `Group Manager` (13 kar), Cakupan `Group `Head Office {runId}` beserta sub-group` (45 kar) · sumber matriks role PRD
- **DU-205-3** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Update pada Group `Head Office {runId}` beserta descendant, Read pada Group `Warehouse {runId}`` (95 kar) · sumber matriks role PRD
- **DU-205-4** User (awal), User Read Only: Name `Rosa Maharani {runId}` (21 kar), Role `Read Only` (9 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-205-5** User (awal), User Manage asset & TAG (Read): Name `Reza Pratama {runId}` (20 kar), Role `Manage asset & TAG (Read)` (25 kar), Cakupan `Read pada Group `Head Office {runId}` beserta descendant` (56 kar) · sumber matriks role PRD
- **DU-205-6** User (awal), User View asset value: Name `Vina Kusuma {runId}` (19 kar), Role `View asset value` (16 kar), Cakupan `Group `Warehouse {runId}` beserta descendant` (44 kar) · sumber matriks role PRD
- **DU-205-7** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-205-8** User (awal), User Manage accounting tanpa Manage asset & TAG maupun Read Only: Name `Nani Setiawan {runId}` (21 kar), Role `Manage accounting tanpa Manage asset & TAG maupun Read Only` (59 kar), Cakupan `tanpa akses modul` (17 kar) · sumber matriks role PRD
- **DU-205-9** User (awal), User Read Only dan Manage accounting: Name `Tari Aminah {runId}` (19 kar), Role `Read Only dan Manage accounting` (31 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-205-10** User (awal), User Manage asset & TAG dengan Create dan Delete tanpa Update: Name `Cici Rahayu {runId}` (19 kar), Role `Manage asset & TAG dengan Create dan Delete tanpa Update` (56 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-205-11** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-205-12** User (awal), User pemilik sesi opname: Name `Sinta Marlina {runId}` (21 kar), Role `pemilik sesi opname` (19 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-205-13** User (awal), User Manage asset & TAG (Update) dan Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Manage asset & TAG (Update) dan Asset Admin sub-tab Disposal` (60 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-205-14** User (awal), User Total Control di entitas `Mitra Suspended {runId}` yang berstatus Suspended: Name `Anton Wijaya {runId}` (20 kar), Role `Total Control di entitas `Mitra Suspended {runId}` yang berstatus Suspended` (75 kar), Cakupan `entitas `Mitra Suspended {runId}`` (33 kar) · sumber matriks role PRD
- **DU-205-15** User (awal), User Total Control di entitas `Mitra Expired {runId}` yang berstatus Expired: Name `Erika Hasan {runId}` (19 kar), Role `Total Control di entitas `Mitra Expired {runId}` yang berstatus Expired` (71 kar), Cakupan `entitas `Mitra Expired {runId}`` (31 kar) · sumber matriks role PRD
- **DU-205-16** User (awal), User Total Control di entitas `Mitra Tanpa Disposal {runId}` ber-level Feature Suite Disposal `None`: Name `Dian Susanto {runId}` (20 kar), Role `Total Control di entitas `Mitra Tanpa Disposal {runId}` ber-level Feature Suite Disposal `None`` (95 kar), Cakupan `entitas `Mitra Tanpa Disposal {runId}`` (38 kar) · sumber matriks role PRD
- **DU-205-17** User (awal), User pelapor umum, pemindai TAG: Name `Dedi Kurniawan {runId}` (22 kar), Role `pelapor umum, pemindai TAG` (26 kar), Cakupan `aset yang ia pindai` (19 kar) · sumber matriks role PRD
- **DU-205-18** Entitas (awal), Entitas lain di luar entitas suite: Name `Mitra Lain {runId}` (18 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-205-19** Entitas (awal), Entitas Suspended: Name `Mitra Suspended {runId}` (23 kar), Status `Suspended` (9 kar) · sumber turunan penulis
- **DU-205-20** Entitas (awal), Entitas Expired: Name `Mitra Expired {runId}` (21 kar), Status `Expired` (7 kar) · sumber turunan penulis
- **DU-205-21** Entitas (awal), Entitas ber-level Disposal None: Name `Mitra Tanpa Disposal {runId}` (28 kar), Level Feature Suite Disposal `None` (4 kar) · sumber turunan penulis
- **DU-205-22** Group (awal), Group induk: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-205-23** Group (awal), Sub-group dari Head Office: Name `Finance Division {runId}` (24 kar), Induk `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-205-24** Group (awal), Group di luar binaan Group Manager: Name `Warehouse {runId}` (17 kar) · sumber turunan penulis
- **DU-205-25** Damage record (awal), Record uji: Name `Laptop Dell Latitude 5420 - 31 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Record ``Damaged`` (9 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `10000000` (8 kar), Asset Value (Fiscal) `9000000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-26** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Printer HP LaserJet M404 - 32 {runId}` (37 kar), Group `Finance Division {runId}` (24 kar), Record ``Damaged`` (9 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-27** Damage record (awal), Record uji: Name `Drill Bosch GSB - 33 {runId}` (28 kar), Group `Warehouse {runId}` (17 kar), Record ``Damaged`` (9 kar), Purchase Cost `4500000` (7 kar), Asset Value (Commercial) `3500000` (7 kar), Asset Value (Fiscal) `3000000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-28** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Monitor Dell P2422H - 34 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Record ``Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (62 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-29** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Camera Canon EOS - 35 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Record ``Reported Disposal` yang dilaporkan `Maya Puspita {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-30** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Tablet Samsung Tab A8 - 36 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Record ``Reported Disposal` yang dilaporkan `Agus Pratama {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-31** Damage record (awal), Record uji: Name `Projector Epson EB-X06 - 37 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Record ``Damaged` dengan penanda `Missing`` (34 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-32** Damage record (awal), Record uji: Name `Scanner Fujitsu fi-7160 - 38 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Record ``Damaged` dari laporan `Yoga Tanuwijaya {runId}` yang sudah di-Confirm Aktor Damaged` (84 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-33** Damage record (awal), Record uji: Name `Forklift Toyota 8FD - 39 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Record ``Damaged` dari laporan `Sinta Marlina {runId}`` (46 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-34** Damage record (awal), Record uji: Name `Office Chair Ergo - 40 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Record ``Rejected` dari laporan `Budi Santoso {runId}` dengan Reason `Foto tidak jelas {runId}`, Damaged Photo `kursi-patah.jpg`, diputuskan `Rina Wulandari {runId}`` (157 kar), Reason `Foto tidak jelas {runId}` (24 kar), Damaged Photo `kursi-patah.jpg` (15 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-35** Damage record (awal), Record uji: Name `Handheld Scanner Zebra TC21 - 41 {runId}` (40 kar), Group `Head Office {runId}` (19 kar), Record ``Waiting for Confirmation` dari laporan `Dedi Kurniawan {runId}`` (64 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-36** Damage record (awal), Record uji: Name `Toyota Avanza - 42 {runId}` (26 kar), Group `Warehouse {runId}` (17 kar), Record ``Damaged`` (9 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-37** Damage record (awal), Record uji: Name `Laptop Dell Latitude 5420 - 43 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Record `tanpa record berjalan, dipegang `Rosa Maharani {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-38** Damage record (awal), Record uji: Name `Laptop Dell Latitude 5420 - 44 {runId}` (38 kar), Group `Warehouse {runId}` (17 kar), Record `tanpa record berjalan, dipegang `Gunawan Hartono {runId}`` (57 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-39** Damage record (awal), Record uji: Name `Laptop Dell Latitude 5420 - 52 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Record `tanpa record berjalan, `Borrowed` oleh `Budi Santoso {runId}`` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-40** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Monitor Dell P2422H - 53 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Record ``Reported Disposal` yang dilaporkan `Maya Puspita {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-41** Damage record (awal), Record uji: Name `Printer HP LaserJet M404 - 45 {runId}` (37 kar), Group `Mitra Lain {runId}` (18 kar), Record ``Damaged` milik entitas lain `Mitra Lain {runId}`` (49 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-42** Damage record (awal), Record uji: Name `Monitor Dell P2422H - 46 {runId}` (32 kar), Group `Mitra Suspended {runId}` (23 kar), Record ``Damaged` di entitas `Mitra Suspended {runId}`` (46 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-43** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-205-authz-cakupan-dan-isolasi), Record uji: Name `Camera Canon EOS - 47 {runId}` (29 kar), Group `Mitra Suspended {runId}` (23 kar), Record ``In Disposal Process` dengan baris Disposal yang kedaluwarsa oleh `System`` (74 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-44** Damage record (awal), Record uji: Name `Scanner Fujitsu fi-7160 - 48 {runId}` (36 kar), Group `Mitra Expired {runId}` (21 kar), Record ``Damaged` di entitas `Mitra Expired {runId}`` (44 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-45** Damage record (awal), Record uji: Name `Drill Bosch GSB - 49 {runId}` (28 kar), Group `Mitra Tanpa Disposal {runId}` (28 kar), Record ``Damaged` di entitas `Mitra Tanpa Disposal {runId}`` (51 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-46** Damage record (awal), Record uji: Name `Forklift Toyota 8FD - 50 {runId}` (32 kar), Group `Mitra Tanpa Disposal {runId}` (28 kar), Record ``Reported Disposal` di entitas `Mitra Tanpa Disposal {runId}`` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-47** Damage record (awal), Record uji: Name `Tablet Samsung Tab A8 - 51 {runId}` (34 kar), Group `Mitra Tanpa Disposal {runId}` (28 kar), Record ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-48** Damage record (dicoba), Id record yang tidak ada: Id record `00000000-0000-0000-0000-000000000000` (36 kar) · sumber turunan penulis
- **DU-205-49** Request (dicoba), Permintaan tanpa sesi: Sesi `tanpa token` (11 kar) · sumber turunan penulis
- **DU-205-50** Damage evidence (dibuat), Bukti laporan: What happened `Casing retak setelah terbentur {runId}` (38 kar), Damaged Photo `casing-retak.jpg` (16 kar) · sumber turunan penulis
- **DU-205-51** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-205-52** Reject reason (dibuat), Alasan Reject: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-205-53** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`, tanpa Update dan tanpa Read Only` (61 kar) · sumber matriks role PRD
- **DU-205-54** User (awal), User Aktor Transfer: Name `Tono Riyadi {runId}` (19 kar), Role `Aktor Transfer` (14 kar), Cakupan `Group `Head Office {runId}`, tanpa Update dan tanpa Read Only` (61 kar) · sumber matriks role PRD
- **DU-205-55** Damage record (awal), Record uji: Name `Monitor Dell P2422H - 54 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Record ``Reported Disposal` yang dilaporkan `Agus Pratama {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-56** Damage record (awal), Record uji: Name `Drill Bosch GSB - 55 {runId}` (28 kar), Group `Warehouse {runId}` (17 kar), Record ``Reported Disposal` yang dilaporkan `Agus Pratama {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-57** Damage record (awal), Record uji: Name `Handheld Scanner Zebra TC21 - 56 {runId}` (40 kar), Group `Head Office {runId}` (19 kar), Record ``Waiting for Confirmation` dari laporan `Dewi Anggraini {runId}`` (64 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-58** Damage record (awal), Record uji: Name `Forklift Toyota 8FD - 57 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Record ``Damaged` dari laporan `Tono Riyadi {runId}`` (44 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-59** Damage record (awal), Record uji: Name `Toyota Avanza - 59 {runId}` (26 kar), Group `Warehouse {runId}` (17 kar), Record ``Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (62 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-60** Damage record (awal), Record uji: Name `Printer HP LaserJet M404 - 58 {runId}` (37 kar), Group `Warehouse {runId}` (17 kar), Record `tanpa record berjalan` (21 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-61** Damage record (awal), Record uji: Name `Camera Canon EOS - 61 {runId}` (29 kar), Group `Mitra Suspended {runId}` (23 kar), Record `tanpa record berjalan di entitas `Mitra Suspended {runId}`` (58 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-205-62** Damage record (awal), Record uji: Name `Tablet Samsung Tab A8 - 60 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Record `tanpa record berjalan` (21 kar) · sumber turunan penulis
- **DU-206-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-206-2** User (awal), User Aktor Missing: Name `Hendra Saputra {runId}` (22 kar), Role `Aktor Missing` (13 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-206-3** User (awal), User Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Asset Admin sub-tab Disposal` (28 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-206-4** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-206-5** Group (awal), Group tempat aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-206-6** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Camera Canon EOS - 61 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tanpa transaksi berjalan` (48 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-7** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Laptop Dell Latitude 5420 - 62 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tanpa transaksi berjalan` (48 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-8** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 63 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (62 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-9** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Drill Bosch GSB - 64 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, dipegang `Budi Santoso {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-10** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Printer HP LaserJet M404 - 65 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, dipegang `Budi Santoso {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-11** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Projector Epson EB-X06 - 66 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`` (100 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-12** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Monitor Dell P2422H - 67 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`` (100 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-13** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Forklift Toyota 8FD - 68 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan Condition sebelumnya Damaged, punya record `Damaged` yang ditahan penanda `Missing`` (100 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-14** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Scanner Fujitsu fi-7160 - 69 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-15** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Office Chair Ergo - 70 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-16** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Office Chair Ergo - 71 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris jenis selain Lost dan Write-off` (79 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-17** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 72 {runId}` (40 kar), Group `Head Office {runId}` (19 kar), Keadaan `tanpa record Damaged, ada laporan hilang dari pemegang `Budi Santoso {runId}` yang masih `Waiting for Confirmation`` (115 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-18** Asset (awal), Aset uji: Name `Office Chair Ergo - 74 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-19** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Toyota Avanza - 73 {runId}` (26 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` tanpa record Damaged` (30 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-20** Missing evidence (dibuat), Bukti laporan hilang: What happened `Terakhir terlihat di gudang lantai dua {runId}` (46 kar), Damaged Photo `terakhir-terlihat.jpg` (21 kar) · sumber turunan penulis
- **DU-206-21** Found evidence (dibuat), Bukti ditemukan rusak: Note `Ditemukan rusak di ruang arsip {runId}` (38 kar), Damaged Photo `ditemukan-rusak.jpg` (19 kar) · sumber turunan penulis
- **DU-206-22** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-206-23** Damage report (dibuat), Laporan rusak baru: What happened `Casing retak setelah terbentur {runId}` (38 kar), Damaged Photo `casing-retak.jpg` (16 kar) · sumber turunan penulis
- **DU-206-24** Asset (awal; dimutasi TC-FA-DAMAGED-BE-206-missing-bersamaan-server), Aset uji: Name `Drill Bosch GSB - 75 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, dipegang `Budi Santoso {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-25** Asset (awal), Aset uji: Name `Handheld Scanner Zebra TC21 - 76 {runId}` (40 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`, dipegang `Budi Santoso {runId}`` (108 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-206-26** Reject reason (dicoba), Alasan Reject: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-207-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-207-2** User (awal), User Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Asset Admin sub-tab Disposal` (28 kar), Cakupan `Group `Head Office {runId}` dan Group `Warehouse {runId}`` (57 kar) · sumber matriks role PRD
- **DU-207-3** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-207-4** Group (awal), Group utama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-207-5** Group (awal), Group kedua: Name `Warehouse {runId}` (17 kar) · sumber turunan penulis
- **DU-207-6** Entitas (awal), Entitas ber-level Disposal None: Name `Mitra Tanpa Disposal {runId}` (28 kar), Level Feature Suite Disposal `None` (4 kar) · sumber turunan penulis
- **DU-207-7** Asset (awal), Aset uji: Name `Scanner Fujitsu fi-7160 - 81 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-8** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Laptop Dell Latitude 5420 - 82 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tanpa transaksi berjalan` (48 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-9** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Printer HP LaserJet M404 - 83 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-10** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Printer HP LaserJet M404 - 84 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal` dari laporan `Maya Puspita {runId}`` (68 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-11** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Printer HP LaserJet M404 - 85 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal` yang dilaporkan `Agus Pratama {runId}`` (71 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-12** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 86 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tanpa transaksi berjalan` (48 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-13** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Camera Canon EOS - 87 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris Disposal `Waiting for Approval`` (79 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-14** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Camera Canon EOS - 88 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris Disposal `Waiting for Execution`` (80 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-15** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Camera Canon EOS - 89 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris Disposal yang akan di-Remove` (76 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-16** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Camera Canon EOS - 90 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris Disposal yang akan kedaluwarsa` (78 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-17** Asset (awal), Aset uji: Name `Camera Canon EOS - 91 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process`` (34 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-18** Asset (awal), Aset uji: Name `Drill Bosch GSB - 92 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Repaired`` (23 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-19** Asset (awal), Aset uji: Name `Drill Bosch GSB - 93 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Disposed`, punya record `Disposed`` (35 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-20** Asset (awal), Aset uji: Name `Drill Bosch GSB - 94 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Rejected`` (23 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-21** Asset (awal), Aset uji: Name `Drill Bosch GSB - 95 {runId}` (28 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Canceled`` (23 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-22** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 96 {runId}` (34 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`` (62 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-23** Asset (awal), Aset uji: Name `Toyota Avanza - 97 {runId}` (26 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dengan penanda `Reported Missing`` (56 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-24** Asset (awal), Aset uji: Name `Toyota Avanza - 98 {runId}` (26 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dengan penanda `Missing`` (47 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-25** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Forklift Toyota 8FD - 99 {runId}` (32 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-26** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Forklift Toyota 8FD - 100 {runId}` (33 kar), Group `Warehouse {runId}` (17 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-27** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Office Chair Ergo - 101 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-28** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Office Chair Ergo - 102 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-29** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Handheld Scanner Zebra TC21 - 103 {runId}` (41 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-30** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Handheld Scanner Zebra TC21 - 104 {runId}` (41 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit` (70 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-31** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Handheld Scanner Zebra TC21 - 105 {runId}` (41 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang kemudian ditahan penanda `Missing` sebelum Submit` (77 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-32** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Projector Epson EB-X06 - 106 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit` (70 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-33** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Projector Epson EB-X06 - 107 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang kemudian ditahan penanda `Missing` sebelum Submit` (77 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-34** Asset (awal; dimutasi TC-FA-DAMAGED-BE-207-disposal-transisi-dan-bulk-server), Aset uji: Name `Monitor Dell P2422H - 108 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, tanpa transaksi berjalan, dilaporkan dari Asset List` (76 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-35** Asset (awal), Aset uji: Name `Printer HP LaserJet M404 - 109 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` di entitas `Mitra Tanpa Disposal {runId}`` (64 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-207-36** Disposal reason (dibuat), Alasan Report Disposal satu record: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}` (50 kar) · sumber turunan penulis
- **DU-207-37** Disposal reason (dibuat), Alasan Bulk Report Disposal: Reason `Seluruh unit dihentikan penggunaannya {runId}` (45 kar) · sumber turunan penulis
- **DU-207-38** Disposal reason (dibuat), Alasan Decline: Reason `Unit masih layak dipakai {runId}` (32 kar) · sumber turunan penulis
- **DU-208-1** User (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-208-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-208-3** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-208-4** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-208-5** User (awal), User Aktor Transfer: Name `Tono Riyadi {runId}` (19 kar), Role `Aktor Transfer` (14 kar), Cakupan `Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`` (63 kar) · sumber matriks role PRD
- **DU-208-6** User (awal), User pemilik sesi opname: Name `Sinta Marlina {runId}` (21 kar), Role `pemilik sesi opname` (19 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-208-7** User (awal), User Aktor Missing: Name `Hendra Saputra {runId}` (22 kar), Role `Aktor Missing` (13 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-208-8** User (awal), User Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Asset Admin sub-tab Disposal` (28 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-208-9** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-208-10** Group (awal), Group asal aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-208-11** Group (awal), Group tujuan pemindahan aset: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-208-12** Entitas (awal), Entitas lain di luar entitas suite: Name `Mitra Lain {runId}` (18 kar) · sumber turunan penulis
- **DU-208-13** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Laptop Dell Latitude 5420 - 111 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-14** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Laptop Dell Latitude 5420 - 112 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-15** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Laptop Dell Latitude 5420 - 113 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-16** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Toyota Avanza - 114 {runId}` (27 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-17** Asset (awal), Aset uji: Name `Drill Bosch GSB - 115 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Disposed`, tanpa record berjalan` (33 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-18** Asset (awal), Aset uji: Name `Camera Canon EOS - 116 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `tanpa catatan apa pun, tidak terlibat dalam aksi mana pun` (57 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-19** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Monitor Dell P2422H - 121 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-20** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Monitor Dell P2422H - 122 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-21** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Monitor Dell P2422H - 123 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-22** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Printer HP LaserJet M404 - 131 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, ber-TAG `RFID-M131 {runId}`` (51 kar), TAG `RFID-M131 {runId}` (17 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-23** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Printer HP LaserJet M404 - 132 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`, ber-TAG `RFID-M132 {runId}` yang tidak terbaca` (70 kar), TAG `RFID-M132 {runId}` (17 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-24** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 141 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-25** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 142 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-26** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 143 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-27** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 144 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process`, baris pelepasan aset dieksekusi` (67 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-28** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 145 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process`, baris pelepasan aset kedaluwarsa` (68 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-29** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Printer HP LaserJet M404 - 191 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-30** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Printer HP LaserJet M404 - 192 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-31** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Printer HP LaserJet M404 - 193 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit` (70 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-32** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Projector Epson EB-X06 - 151 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `draf registrasi ber-Condition `Damaged`, belum Active` (53 kar), Damage note `Lensa tergores dan bodi penyok akibat benturan saat pengiriman dari gudang pusat ke kantor cabang Lensa tergores dan bod` (120 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-35** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Tablet Samsung Tab A8 - 161 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-36** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Tablet Samsung Tab A8 - 162 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (63 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-37** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Tablet Samsung Tab A8 - 163 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}` dengan What happened `Engsel longgar {runId}`` (161 kar), What happened `Engsel longgar {runId}` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-38** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 164 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan, form Return belum lolos validasi` (95 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-39** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Forklift Toyota 8FD - 171 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `termasuk sesi opname milik `Sinta Marlina {runId}`, tanpa record berjalan` (73 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-40** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Forklift Toyota 8FD - 172 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `dalam pemindahan menuju `Branch Surabaya {runId}`, tanpa record berjalan` (72 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-41** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Forklift Toyota 8FD - 173 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `dalam pemindahan menuju `Branch Surabaya {runId}`, punya record `Damaged` dengan What happened `Garpu bengkok {runId}` Source `Manual`` (134 kar), What happened `Garpu bengkok {runId}` (21 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-42** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 181 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan record `Damaged` ditahan dengan What happened `Lensa berjamur {runId}`` (87 kar), What happened `Lensa berjamur {runId}` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-43** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 182 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` tanpa record Damaged` (30 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-44** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 183 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Damaged` tanpa laporan hilang sebelumnya, akan dilaporkan hilang` (65 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-45** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 184 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` ditahan dengan laporan hilang dari pemegang yang akan ditolak` (84 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-46** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 185 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan record `Damaged` ditahan yang akan menjadi `Disposed`` (70 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-47** Return report (dibuat), Catatan dan foto Return: Description `Engsel longgar saat dikembalikan {runId}` (40 kar), Foto Return `foto-return.jpg` (15 kar) · sumber turunan penulis
- **DU-208-48** Unassign report (dibuat), Catatan dan foto Unassign: Description `Layar tergores saat dikembalikan {runId}` (40 kar), Foto Unassign `foto-unassign.jpg` (17 kar) · sumber turunan penulis
- **DU-208-49** Opname report (dibuat), Bukti laporan opname: What happened `Rangka berkarat ditemukan saat opname {runId}` (45 kar), Damaged Photo `rangka-berkarat.jpg` (19 kar) · sumber turunan penulis
- **DU-208-50** Receive report (dibuat), Bukti laporan saat penerimaan: What happened `Garpu bengkok saat diterima {runId}` (35 kar), Damaged Photo `garpu-bengkok.jpg` (17 kar) · sumber turunan penulis
- **DU-208-51** Found report (dibuat), Note dan foto ditemukan rusak: Note `Ditemukan rusak di ruang arsip {runId}` (38 kar), Damaged Photo `ditemukan-rusak.jpg` (19 kar) · sumber turunan penulis
- **DU-208-52** Damage evidence (dibuat), Bukti laporan Pelapor admin: What happened `Layar retak setelah terjatuh dari meja {runId}` (46 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber turunan penulis
- **DU-208-53** Reject reason (dibuat), Alasan Reject dan Decline: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-208-54** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-208-55** Disposal reason (dibuat), Alasan Report Disposal: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}` (50 kar) · sumber turunan penulis
- **DU-208-56** User (dibuat), Nama baru pelaku: Name `Agus Pratama Putra {runId}` (26 kar) · sumber turunan penulis
- **DU-208-57** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Scanner Fujitsu fi-7160 - 146 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-58** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Camera Canon EOS - 186 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-208-59** Damage report (dibuat), Laporan hilang: What happened `Terakhir terlihat di gudang lantai dua {runId}` (46 kar), Damaged Photo `terakhir-terlihat.jpg` (21 kar) · sumber turunan penulis
- **DU-208-60** Asset (awal; dimutasi TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log), Aset uji: Name `Tablet Samsung Tab A8 - 165 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (117 kar) · sumber turunan penulis
- **DU-209-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-209-2** User (awal), User Group Manager: Name `Gunawan Hartono {runId}` (23 kar), Role `Group Manager` (13 kar), Cakupan `Group `Head Office {runId}` beserta sub-group` (45 kar) · sumber matriks role PRD
- **DU-209-3** Group (awal), Group utama: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-209-4** Group (awal), Group di luar binaan Group Manager: Name `Warehouse {runId}` (17 kar) · sumber turunan penulis
- **DU-209-5** Group (awal), Group lama yang kemudian diganti nama: Name `Gudang Lama {runId}` (19 kar) · sumber turunan penulis
- **DU-209-6** Group (dibuat; dimutasi TC-FA-DAMAGED-BE-209-search-sort-filter-server), Nama baru Group lama: Name `Gudang Baru {runId}` (19 kar) · sumber turunan penulis
- **DU-209-7** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 1 {runId}` (34 kar), Asset ID `LPT-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Waiting for Confirmation` (24 kar), Source `Reported by holder` (18 kar), Last Holder `Budi S` (6 kar), Reported By `—` (1 kar), Reported Date `T0 − 9 hari, pukul 08:15` (24 kar), Purchase Cost `12500000` (8 kar), Brand `Lenovo {runId}` (14 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-8** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 2 {runId}` (34 kar), Asset ID `LPT-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 7 hari, pukul 09:30` (24 kar), Purchase Cost `4500000` (7 kar), Brand `Lenovo {runId}` (14 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-9** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 10 {runId}` (35 kar), Asset ID `LPT-0010-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 5 hari, pukul 10:45` (24 kar), Purchase Cost `7200000` (7 kar), Brand `Lenovo {runId}` (14 kar), Tab `Active` (6 kar), Penanda `Missing` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-10** Damage record (awal), Record uji: Name `Printer Canon Pixma - 1 {runId}` (31 kar), Asset ID `PRN-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Reported Disposal` (17 kar), Source `Stock opname` (12 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 3 hari, pukul 11:00` (24 kar), Purchase Cost `2100000` (7 kar), Brand `Canon {runId}` (13 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-11** Damage record (awal), Record uji: Name `Printer Canon Pixma - 2 {runId}` (31 kar), Asset ID `PRN-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Borrowed asset` (14 kar), Last Holder `Sari D` (6 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 11 hari, pukul 14:20` (25 kar), Purchase Cost `3300000` (7 kar), Brand `Canon {runId}` (13 kar), Tab `Active` (6 kar), Penanda `Reported Missing` (16 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-12** Damage record (awal), Record uji: Name `Drill Bosch GSB - 1 {runId}` (27 kar), Asset ID `DRL-0001-{runId}` (16 kar), Group `Warehouse {runId}` (17 kar), Status `Damaged` (7 kar), Source `Transfer receive` (16 kar), Last Holder `—` (1 kar), Reported By `Rina W` (6 kar), Reported Date `T0 − 6 hari, pukul 13:05` (24 kar), Purchase Cost `1800000` (7 kar), Brand `Bosch {runId}` (13 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-13** Damage record (awal), Record selesai: Name `Laptop Lenovo ThinkPad - 3 {runId}` (34 kar), Asset ID `LPT-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Repaired` (8 kar), Source `Manual` (6 kar), Resolved By `Agus P` (6 kar), Resolved Date `T0 − 2 hari, pukul 15:00` (24 kar), Tab `History` (7 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-209-14** Damage record (awal), Record selesai: Name `Printer Canon Pixma - 3 {runId}` (31 kar), Asset ID `PRN-0003-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Rejected` (8 kar), Source `Reported by scan` (16 kar), Resolved By `Rina W` (6 kar), Resolved Date `T0 − 4 hari, pukul 12:10` (24 kar), Tab `History` (7 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-209-15** Damage record (awal), Record selesai: Name `Drill Bosch GSB - 2 {runId}` (27 kar), Asset ID `DRL-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Disposed` (8 kar), Source `Stock opname` (12 kar), Resolved By `System` (6 kar), Resolved Date `T0 − 1 hari, pukul 00:00` (24 kar), Tab `History` (7 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-209-16** Damage record (awal; dimutasi TC-FA-DAMAGED-BE-209-search-sort-filter-server), Record selesai: Name `Printer Canon Pixma - 4 {runId}` (31 kar), Asset ID `PRN-0004-{runId}` (16 kar), Group `Gudang Lama {runId}` (19 kar), Status `Canceled` (8 kar), Source `Reported by holder` (18 kar), Resolved By `Budi S` (6 kar), Resolved Date `T0 − 6 hari, pukul 08:00` (24 kar), Tab `History` (7 kar) · sumber PRD §4.1b T-DMG-02 Example Data
- **DU-209-17** Damage record (awal), Record uji: Name `Scanner Zulu - 1 {runId}` (24 kar), Asset ID `ZLU-0001-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 8 hari, pukul 09:30` (24 kar), Purchase Cost `5000000` (7 kar), Brand `Zulu {runId}` (12 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-209-18** Damage record (awal), Record uji: Name `Scanner Zulu - 2 {runId}` (24 kar), Asset ID `ZLU-0002-{runId}` (16 kar), Group `Head Office {runId}` (19 kar), Status `Damaged` (7 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Reported Date `T0 − 8 hari, pukul 09:30` (24 kar), Purchase Cost `5000000` (7 kar), Brand `Zulu {runId}` (12 kar), Tab `Active` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-210-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant, yang kemudian dicabut` (69 kar) · sumber matriks role PRD
- **DU-210-3** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-210-4** User (awal), User Aktor Transfer: Name `Tono Riyadi {runId}` (19 kar), Role `Aktor Transfer` (14 kar), Cakupan `Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`` (63 kar) · sumber matriks role PRD
- **DU-210-5** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-210-6** User (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), User pelapor umum, pemegang aset yang kemudian dinonaktifkan: Name `Hana Lestari {runId}` (20 kar), Role `pelapor umum, pemegang aset yang kemudian dinonaktifkan` (55 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-210-7** Setting company (awal), Zona waktu company: Time Zone `Asia/Jakarta` (12 kar) · sumber turunan penulis
- **DU-210-8** Group (awal), Group asal aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-210-9** Group (awal), Group tujuan pemindahan aset: Name `Branch Surabaya {runId}` (23 kar) · sumber turunan penulis
- **DU-210-10** Group (awal), Group tanpa anak yang punya record berjalan: Name `Divisi Gudang {runId}` (21 kar), Anak `tidak ada` (9 kar) · sumber turunan penulis
- **DU-210-11** Group (awal), Group induk yang punya anak ber-record berjalan: Name `Divisi Pusat {runId}` (20 kar), Anak `Sub Pusat {runId}` (17 kar) · sumber turunan penulis
- **DU-210-12** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Laptop Lenovo ThinkPad - 201 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Manual` dilaporkan `Agus P`, Last Holder `Budi S`, Asset ID `LPT-0201-{runId}`, Brand `Lenovo {runId}`, Model/Type `ThinkPad X1 {runId}`, Division `Keuangan {runId}`, Purchase Cost `12500000`, Asset Value (Commercial) `10000000`` (259 kar), Asset ID `LPT-0201-{runId}` (16 kar), Brand `Lenovo {runId}` (14 kar), Model/Type `ThinkPad X1 {runId}` (19 kar), Division `Keuangan {runId}` (16 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `10000000` (8 kar), Last Holder `Budi S` (6 kar), Reported By `Agus P` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-13** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Printer HP LaserJet M404 - 202 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Repaired` dengan Resolved Date `T0 − 2 hari, pukul 00:30`, Group saat selesai `Head Office {runId}`, Asset Value (Commercial) saat selesai `8000000`, Purchase Cost `3000000`, Alias Name `Printer Lobi {runId}`` (222 kar), Asset Value (Commercial) `8000000` (7 kar), Purchase Cost `3000000` (7 kar), Alias Name `Printer Lobi {runId}` (20 kar), Resolved Date `T0 − 2 hari, pukul 00:30` (24 kar), Reported Date `T0 − 3 hari, pukul 23:30` (24 kar), Asset Value (Fiscal) saat selesai `6500000` (7 kar), Category saat selesai `Elektronik {runId}` (18 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-14** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 203 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` dengan Reported Date `T0, pukul 01:00` zona waktu `Asia/Jakarta`` (87 kar), Reported Date `T0, pukul 01:00` (15 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-15** Asset (awal), Aset uji: Name `Camera Canon EOS - 204 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dengan Reported Date `T0 − 2 hari, pukul 10:00`` (87 kar), Reported Date `T0 − 2 hari, pukul 10:00` (24 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-16** Asset (awal), Aset uji: Name `Camera Canon EOS - 205 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` ditahan penanda `Missing` dengan Reported Date `T0 − 3 hari, pukul 10:00`` (96 kar), Reported Date `T0 − 3 hari, pukul 10:00` (24 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-17** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Forklift Toyota 8FD - 206 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Manual`, dalam pemindahan menuju `Branch Surabaya {runId}`` (89 kar), Source `Manual` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-18** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Drill Bosch GSB - 207 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Hana Lestari {runId}`` (75 kar), Reported By `Hana L` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-19** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 208 {runId}` (33 kar), Group `Divisi Gudang {runId}` (21 kar), Keadaan `punya record `Damaged` di Group `Divisi Gudang {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-20** Asset (awal), Aset uji: Name `Monitor Dell P2422H - 209 {runId}` (33 kar), Group `Sub Pusat {runId}` (17 kar), Keadaan `punya record `Damaged` di sub-group `Sub Pusat {runId}`` (55 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-21** Asset (awal), Aset uji: Name `Scanner Fujitsu fi-7160 - 210 {runId}` (37 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-22** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Office Chair Ergo - 211 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-23** Asset (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Aset uji: Name `Projector Epson EB-X06 - 212 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal` yang mencerminkan laporan pelepasan aset` (73 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-24** Konsumen (awal), Konsumen record asset-detail/: Konsumen `asset-detail/` (13 kar), Surface `halaman detail aset` (19 kar) · sumber turunan penulis
- **DU-210-25** Konsumen (awal), Konsumen record my-asset/: Konsumen `my-asset/` (9 kar), Surface `halaman aset yang dipegang pemegang` (35 kar) · sumber turunan penulis
- **DU-210-26** Konsumen (awal), Konsumen record borrow/: Konsumen `borrow/` (7 kar), Surface `baris peminjaman` (16 kar) · sumber turunan penulis
- **DU-210-27** Konsumen (awal), Konsumen record assignment/: Konsumen `assignment/` (11 kar), Surface `baris penugasan` (15 kar) · sumber turunan penulis
- **DU-210-28** Konsumen (awal), Konsumen record missing/: Konsumen `missing/` (8 kar), Surface `modul aset hilang` (17 kar) · sumber turunan penulis
- **DU-210-29** Konsumen (awal), Konsumen record asset-registration/: Konsumen `asset-registration/` (19 kar), Surface `registrasi aset` (15 kar) · sumber turunan penulis
- **DU-210-30** Konsumen (awal), Konsumen record audit/: Konsumen `audit/` (6 kar), Surface `sesi opname` (11 kar) · sumber turunan penulis
- **DU-210-31** Konsumen (awal), Konsumen record disposal/: Konsumen `disposal/` (9 kar), Surface `laporan pelepasan aset` (22 kar) · sumber turunan penulis
- **DU-210-32** Konsumen (awal), Konsumen record transfer/: Konsumen `transfer/` (9 kar), Surface `pemindahan aset` (15 kar) · sumber turunan penulis
- **DU-210-33** Konsumen (awal), Konsumen record settings-groups/: Konsumen `settings-groups/` (16 kar), Surface `pengelolaan Group` (17 kar) · sumber turunan penulis
- **DU-210-34** Damage evidence (dibuat), Bukti laporan: What happened `Layar retak setelah terjatuh dari meja {runId}` (46 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber turunan penulis
- **DU-210-35** Asset edit (dibuat; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), Perubahan data aset oleh pemiliknya: Brand `Lenovo Baru {runId}` (19 kar), Purchase Cost `13000000` (8 kar), Asset Value (Commercial) `9500000` (7 kar) · sumber turunan penulis
- **DU-210-36** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-210-37** Asset (awal), Aset uji: Name `Laptop Lenovo ThinkPad - 213 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Manual`` (38 kar), Asset ID `LPT-0213-{runId}` (16 kar), Model/Type `ThinkPad T14 {runId}` (20 kar), Division `Operasional {runId}` (19 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-38** Perubahan aset (dibuat), Nilai baru dari pemilik aset: Name `Laptop Lenovo ThinkPad - 213 Baru {runId}` (41 kar), Asset ID `LPT-0213B-{runId}` (17 kar), Model/Type `ThinkPad T14s {runId}` (21 kar), Division `Teknologi {runId}` (17 kar) · sumber turunan penulis
- **DU-210-39** Asset (awal), Aset uji: Name `Laptop Lenovo ThinkPad - 214 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Manual`` (38 kar), TAG `RFID-L214 {runId}` (17 kar), Labels `Prioritas {runId}` (17 kar), Asset Class `Laptop {runId}` (14 kar), Category `Elektronik {runId}` (18 kar), Alias Name `Laptop Staf {runId}` (19 kar), Measurement `14 inci` (7 kar), Register Date `T0 − 400 hari` (13 kar), Purchase Date `T0 − 420 hari` (13 kar), Warranty Expiry `T0 + 300 hari` (13 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-40** Perubahan aset (dibuat), Nilai baru dari pemilik aset: TAG `QR-L214 {runId}` (15 kar), Labels `Garansi {runId}` (15 kar), Asset Class `Perangkat Kerja {runId}` (23 kar), Category `Peralatan Kantor {runId}` (24 kar) · sumber turunan penulis
- **DU-210-41** Perubahan aset (dibuat), Nilai baru dari pemilik aset: Alias Name `Laptop Direksi {runId}` (22 kar), Measurement `15 inci` (7 kar), Register Date `T0 − 380 hari` (13 kar), Purchase Date `T0 − 400 hari` (13 kar), Warranty Expiry `T0 + 320 hari` (13 kar) · sumber turunan penulis
- **DU-210-42** Perubahan aset (dibuat), Nilai baru dari pemilik aset: Purchase Cost `14000000` (8 kar) · sumber turunan penulis
- **DU-210-43** Perubahan aset (dibuat), Nilai baru dari pemilik aset: Alias Name `Printer Lantai Dua {runId}` (26 kar), Purchase Cost `3500000` (7 kar) · sumber turunan penulis
- **DU-210-44** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 215 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-45** Asset (awal), Aset uji: Name `Tablet Samsung Tab A8 - 216 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (63 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-210-46** User (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), User pelapor yang kemudian diganti namanya: Name `Wawan Setiadi {runId}` (21 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Nama baru `Wawan Hidayat {runId}` (21 kar) · sumber matriks role PRD
- **DU-210-47** User (awal; dimutasi TC-FA-DAMAGED-BE-210-sync-reflected-snapshot-dan-dependen), User pemegang aset yang kemudian diganti namanya: Name `Dimas Prakoso {runId}` (21 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar), Nama baru `Dimas Kusuma {runId}` (20 kar) · sumber matriks role PRD
- **DU-210-48** Asset (awal), Aset uji: Name `Laptop Lenovo ThinkPad - 217 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged` Source `Manual` dilaporkan `Wawan S`, Last Holder `Dimas P`` (82 kar), Last Holder `Dimas P` (7 kar), Reported By `Wawan S` (7 kar) · sumber turunan penulis
- **DU-210-49** Konsumen (awal), Konsumen record asset-list/: Konsumen `asset-list/` (11 kar), Surface `daftar aset` (11 kar) · sumber turunan penulis
- **DU-211-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-211-2** User (awal), User Group Manager: Name `Gunawan Hartono {runId}` (23 kar), Role `Group Manager` (13 kar), Cakupan `Group `Head Office {runId}` beserta sub-group` (45 kar) · sumber matriks role PRD
- **DU-211-3** User (awal), User Read Only: Name `Rosa Maharani {runId}` (21 kar), Role `Read Only` (9 kar), Cakupan `seluruh client tanpa hak lihat nilai finansial` (46 kar) · sumber matriks role PRD
- **DU-211-4** User (awal), User pelapor umum: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum` (12 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-211-5** User (awal), User Total Control, pelaku node terbaru record `Laptop Lenovo ThinkPad - 301 {runId}`, nama belakang dua kata: Name `Siti Nur Rahmawati {runId}` (26 kar), Role `Total Control, pelaku node terbaru record `Laptop Lenovo ThinkPad - 301 {runId}`, nama belakang dua kata` (104 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-211-6** Group (awal), Group hierarkis tiga tingkat: Name `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar) · sumber foundation prd-conventions.md §9.9
- **DU-211-7** Group (awal), Group dengan leaf sama dan parent beda: Name `Bandung Office {runId} > Floor 2 {runId}` (40 kar) · sumber foundation prd-conventions.md §9.9
- **DU-211-8** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 301 {runId}` (36 kar), Asset ID `LPT-0301-{runId}` (16 kar), Status `Damaged` (7 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID, NFC` (9 kar), Tab `Active` (6 kar), Brand `Lenovo {runId}` (14 kar), Model/Type `ThinkPad X1 {runId}` (19 kar), Category `Elektronik {runId} > Laptop {runId}` (35 kar), Source `Manual` (6 kar), Last Holder `—` (1 kar), Reported By `Agus P` (6 kar), Modified By `Siti Nur Rahmawati {runId}` (26 kar), Labels `Prioritas {runId}, Aset Kantor {runId}, Aset Lantai Dua {runId}` (63 kar), Purchase Cost `12500000` (8 kar), Asset Value (Commercial) `10000000` (8 kar), Days Damaged `7` (1 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-9** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 302 {runId}` (36 kar), Asset ID `LPT-0302-{runId}` (16 kar), Status `Waiting for Confirmation` (24 kar), Group `Bandung Office {runId} > Floor 2 {runId}` (40 kar), TAG `QR` (2 kar), Tab `Active` (6 kar), Brand `Lenovo {runId}` (14 kar), Source `Reported by holder` (18 kar), Purchase Cost `4500000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-10** Damage record (awal), Record uji: Name `Printer Canon Pixma - 303 {runId}` (33 kar), Asset ID `PRN-0303-{runId}` (16 kar), Status `Reported Disposal` (17 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `Active` (6 kar), Brand `Canon {runId}` (13 kar), Source `Stock opname` (12 kar), Purchase Cost `2100000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-11** Damage record (awal), Record uji: Name `Printer Canon Pixma - 304 {runId}` (33 kar), Asset ID `PRN-0304-{runId}` (16 kar), Status `In Disposal Process` (19 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `Active` (6 kar), Brand `Canon {runId}` (13 kar), Source `Manual` (6 kar), Purchase Cost `3300000` (7 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-12** Damage record (awal), Record uji: Name `Monitor, Curved Dell - 305 {runId}` (34 kar), Asset ID `MON-0305-{runId}` (16 kar), Status `Damaged` (7 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `QR` (2 kar), Tab `Active` (6 kar), Brand `Dell {runId}` (12 kar), Source `Manual` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-13** Damage record (awal), Record uji: Name `Monitor "Curved" 27 inci - 306 {runId}` (38 kar), Asset ID `MON-0306-{runId}` (16 kar), Status `Damaged` (7 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `QR` (2 kar), Tab `Active` (6 kar), Brand `Dell {runId}` (12 kar), Source `Manual` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-14** Damage record (awal), Record uji: Name `Printer Epson L3150 - 307 {runId}` (33 kar), Asset ID `PRN-0307-{runId}` (16 kar), Status `Damaged` (7 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `QR` (2 kar), Tab `Active` (6 kar), Brand `Epson {runId}` (13 kar), Source `Manual` (6 kar), Alias Name `Printer Lobi
Lantai 2 {runId}` (29 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-15** Damage record (awal), Record uji: Name `Kamera Café Élan - 308 {runId}` (30 kar), Asset ID `CAM-0308-{runId}` (16 kar), Status `Damaged` (7 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `Active` (6 kar), Brand `Café Élan {runId}` (17 kar), Source `Manual` (6 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-16** Damage record (awal), Record uji: Name `Laptop Lenovo ThinkPad - 311 {runId}` (36 kar), Asset ID `HST-h1-{runId}` (14 kar), Status `Repaired` (8 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `History` (7 kar), Brand `Lenovo {runId}` (14 kar), Source `Manual` (6 kar), Resolved By `Agus P` (6 kar), Duration `6` (1 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-17** Damage record (awal), Record uji: Name `Drill Bosch GSB - 312 {runId}` (29 kar), Asset ID `HST-h2-{runId}` (14 kar), Status `Disposed` (8 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `History` (7 kar), Brand `Lenovo {runId}` (14 kar), Source `Manual` (6 kar), Resolved By `System` (6 kar), Duration `62` (2 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-18** Damage record (awal), Record uji: Name `Camera Canon EOS - 313 {runId}` (30 kar), Asset ID `HST-h3-{runId}` (14 kar), Status `Rejected` (8 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `History` (7 kar), Brand `Lenovo {runId}` (14 kar), Source `Manual` (6 kar), Resolved By `Rina W` (6 kar), Duration `1` (1 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-19** Damage record (awal), Record uji: Name `Scanner Fujitsu fi-7160 - 314 {runId}` (37 kar), Asset ID `HST-h4-{runId}` (14 kar), Status `Canceled` (8 kar), Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` (59 kar), TAG `RFID` (4 kar), Tab `History` (7 kar), Brand `Lenovo {runId}` (14 kar), Source `Manual` (6 kar), Resolved By `Dewi A` (6 kar), Duration `1` (1 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-211-20** Damage record (awal; 5000 record), Volume tepat 5.000 baris: Name `Aset Volume A {n} {runId}` (25 kar), Status `Damaged` (7 kar), Group `Head Office {runId}` (19 kar) · sumber PRD §9.9 prd-conventions.md
- **DU-211-21** Damage record (awal; 5001 record), Volume 5.001 baris: Name `Aset Volume B {n} {runId}` (25 kar), Status `Damaged` (7 kar), Group `Head Office {runId}` (19 kar) · sumber PRD §9.9 prd-conventions.md
- **DU-211-22** Group (awal), Group tempat volume: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-212-1** User (awal), User Total Control: Name `Agus Pratama {runId}` (20 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-212-2** User (awal), User Manage asset & TAG (Update): Name `Rina Wulandari {runId}` (22 kar), Role `Manage asset & TAG (Update)` (27 kar), Cakupan `Group `Head Office {runId}` beserta descendant` (46 kar) · sumber matriks role PRD
- **DU-212-3** User (awal), User Aktor Borrow: Name `Yoga Tanuwijaya {runId}` (23 kar), Role `Aktor Borrow` (12 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-212-4** User (awal), User Aktor Assignment: Name `Dewi Anggraini {runId}` (22 kar), Role `Aktor Assignment` (16 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-212-5** User (awal), User Aktor Missing: Name `Hendra Saputra {runId}` (22 kar), Role `Aktor Missing` (13 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-212-6** User (awal), User Asset Admin sub-tab Disposal: Name `Maya Puspita {runId}` (20 kar), Role `Asset Admin sub-tab Disposal` (28 kar), Cakupan `Group `Head Office {runId}`` (27 kar) · sumber matriks role PRD
- **DU-212-7** User (awal), User pelapor umum, pemegang aset: Name `Budi Santoso {runId}` (20 kar), Role `pelapor umum, pemegang aset` (27 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-212-8** User (awal), User pelapor umum, pemindai TAG: Name `Dedi Kurniawan {runId}` (22 kar), Role `pelapor umum, pemindai TAG` (26 kar), Cakupan `aset yang ia pindai` (19 kar) · sumber matriks role PRD
- **DU-212-9** User (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), User pelapor umum, pemegang aset yang kemudian dinonaktifkan: Name `Hana Lestari {runId}` (20 kar), Role `pelapor umum, pemegang aset yang kemudian dinonaktifkan` (55 kar), Cakupan `aset yang ia pegang` (19 kar) · sumber matriks role PRD
- **DU-212-10** Group (awal), Group tempat aset uji: Name `Head Office {runId}` (19 kar) · sumber turunan penulis
- **DU-212-11** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Laptop Dell Latitude 5420 - 301 {runId}` (39 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-12** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 302 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Rina Wulandari {runId}`, tanpa record berjalan` (65 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-13** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Projector Epson EB-X06 - 303 {runId}` (36 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-14** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Monitor Dell P2422H - 304 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (63 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-15** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Office Chair Ergo - 305 {runId}` (31 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Normal`, tanpa record berjalan` (31 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-16** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Camera Canon EOS - 311 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-17** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Camera Canon EOS - 312 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-18** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Camera Canon EOS - 313 {runId}` (30 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-19** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Printer HP LaserJet M404 - 321 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), TAG `RFID-C321 {runId}` (17 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-20** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Printer HP LaserJet M404 - 322 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris pelepasan aset yang akan dieksekusi` (83 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-21** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Printer HP LaserJet M404 - 323 {runId}` (38 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan record `Damaged` ditahan yang akan menjadi `Disposed`` (70 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-22** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 331 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan` (61 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-23** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 332 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan` (63 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-24** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 333 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan ``Missing` dengan record `Damaged` ditahan` (41 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-25** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 334 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `draf registrasi ber-Condition `Damaged`, belum Active` (53 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-26** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Tablet Samsung Tab A8 - 335 {runId}` (35 kar), Group `Head Office {runId}` (19 kar), Keadaan `termasuk sesi opname milik `Agus Pratama {runId}`, tanpa record berjalan` (72 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-27** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 341 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Damaged`` (22 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-28** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 342 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-29** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 344 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris pelepasan aset yang akan kedaluwarsa` (84 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-30** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Drill Bosch GSB - 351 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), TAG `RFID-H351 {runId}` (17 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-31** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Drill Bosch GSB - 352 {runId}` (29 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`` (75 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-32** Damage evidence (dibuat), Bukti laporan: What happened `Layar retak setelah terjatuh dari meja {runId}` (46 kar), Damaged Photo `layar-retak.jpg` (15 kar) · sumber turunan penulis
- **DU-212-33** Reject reason (dibuat), Alasan Reject: Reason `Foto yang dikirim bukan foto aset ini {runId}` (45 kar) · sumber turunan penulis
- **DU-212-34** Repair note (dibuat), Catatan perbaikan: Repair note `Komponen rusak sudah diganti {runId}` (36 kar) · sumber turunan penulis
- **DU-212-35** Return note (dibuat), Catatan dan foto Report Damaged dari halaman Return Borrow: Description `Engsel longgar saat dikembalikan {runId}` (40 kar), Foto Return `foto-return.jpg` (15 kar) · sumber turunan penulis
- **DU-212-36** Unassign note (dibuat), Catatan dan foto Unassign bermarker Damaged: Description `Layar tergores saat dikembalikan {runId}` (40 kar), Foto Unassign `foto-unassign.jpg` (17 kar) · sumber turunan penulis
- **DU-212-37** Found note (dibuat), Catatan Mark as Found Damaged: Note `Ditemukan rusak di ruang arsip {runId}` (38 kar), Damaged Photo `ditemukan-rusak.jpg` (19 kar) · sumber turunan penulis
- **DU-212-38** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 345 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal` dari laporan `Maya Puspita {runId}`` (68 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-39** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 346 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `Reported Disposal`` (32 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-40** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 347 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris pelepasan aset yang akan ditolak` (80 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-41** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 348 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris pelepasan aset yang akan dibatalkan` (83 kar) · sumber PRD §4.1a T-DMG-01 Example Data
- **DU-212-42** Asset (awal; dimutasi TC-FA-DAMAGED-BE-212-event-notifikasi), Aset uji: Name `Forklift Toyota 8FD - 349 {runId}` (33 kar), Group `Head Office {runId}` (19 kar), Keadaan `punya record `In Disposal Process` dengan baris pelepasan aset yang akan dihapus` (80 kar) · sumber PRD §4.1a T-DMG-01 Example Data
