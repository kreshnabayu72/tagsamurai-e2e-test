<!-- Ditulis stage spec-from-prd saat close. Jangan diubah tangan: run berikutnya menimpanya. -->

Suite: `specs/FixedAsset/SettingsChartOfAccounts`. Sumber: PRD `fixed-asset@9e5ae60` (sha `851502c28b0ddee7`), foundation@8ec9ed8-dirty, kontrak komponen wangs-ui@1.0.0. Stage: `prd-harness@1271d35`, ditutup 2026-11-15T19:55:20Z.

# Matriks data Chart of Accounts (8dab67140994cc6a)

- Entri: 896 (awal 613, dibuat 152, dicoba 131)
- Checker: ERROR 0, REVIEW 22

## Target × varian

✓ entri yang memenuhi, ✗ belum ada entri, — tidak berlaku beserta alasannya.

### Account Code@form-add-account · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-101-2 |
| `spasi-saja` | ✓ DU-101-3 |
| `pilihan-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |
| `berkas-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |

### Account Code@form-add-account · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-101-4 |
| `lebih-maks` | ✓ DU-101-5 |
| `batas-maks-spasi-tepi` | ✓ DU-101-6 |
| `batas-min` | — §9.9: Min 1 sama dengan aturan wajib V-01; tidak ada panjang minimum lain |
| `kurang-min` | — §9.9: Min 1 sama dengan aturan wajib V-01; tidak ada panjang minimum lain |
| `addon-tidak-dihitung` | — §4.1.2: Text input tanpa addon |
| `opsional-kosong-tanpa-min` | — §4.1.2: Account Code Required |
| `batas-maks-spasi-tengah` | — §6 V-03: whitelist huruf Latin, angka, `-`, `_`, `.` menolak spasi dan karakter non-Latin |
| `batas-maks-unicode` | — §6 V-03: whitelist huruf Latin, angka, `-`, `_`, `.` menolak spasi dan karakter non-Latin |

### Account Code@form-add-account · VD-F4

| Varian | Entri |
|---|---|
| `per-kelas-izin:-` | ✓ DU-101-7 |
| `per-kelas-izin:_` | ✓ DU-101-8 |
| `per-kelas-izin:.` | ✓ DU-101-9 |
| `per-kelas-tolak:spasi` | ✓ DU-101-10 |
| `per-kelas-tolak:emoji` | ✓ DU-101-11 |
| `emoji-paste` | ✓ DU-101-12 |
| `emoji-jalur-fallback` | — §6 V-03: Account Code tidak memblok ketikan; pesan tampil «Langsung saat mengetik» |
| `bebas-karakter` | — §4.1.2: Text input ber-whitelist, bukan Text Area |
| `karakter-kontrol-non-ui` | — §6 V-03: PRD tidak menetapkan hasil khusus karakter kontrol dari jalur non-UI; kelas di luar whitelist diwakili per-kelas-tolak |

### Account Name@form-add-account · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-102-2 |
| `spasi-saja` | ✓ DU-102-3 |
| `pilihan-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |
| `berkas-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |

### Account Name@form-add-account · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-102-4 |
| `lebih-maks` | ✓ DU-102-5 |
| `batas-maks-spasi-tepi` | ✓ DU-102-6 |
| `batas-maks-spasi-tengah` | ✓ DU-102-7 |
| `batas-maks-unicode` | ✓ DU-102-8 |
| `addon-tidak-dihitung` | — §4.1.2: Text input tanpa addon |
| `opsional-kosong-tanpa-min` | — §4.1.2: Account Name Required |
| `batas-min` | — §9.9: Min 1 sama dengan aturan wajib V-05; tidak ada panjang minimum lain |
| `kurang-min` | — §9.9: Min 1 sama dengan aturan wajib V-05; tidak ada panjang minimum lain |

### Account Name@form-add-account · VD-F4

| Varian | Entri |
|---|---|
| `per-kelas-tolak:emoji` | ✓ DU-102-9 |
| `emoji-paste` | ✓ DU-102-10 |
| `emoji-jalur-fallback` | ✓ DU-102-11 |
| `per-kelas-izin` | — §9.9: Account Name memakai «Blocklist emoji» tanpa daftar kelas izin |
| `bebas-karakter` | — §4.1.2: Text input satu baris, bukan Text Area |
| `karakter-kontrol-non-ui` | — §6 V-07: PRD hanya menetapkan emoji; hasil karakter kontrol dari jalur non-UI tidak dinyatakan |

### Account Function@form-add-account · VD-F1

| Varian | Entri |
|---|---|
| `pilihan-kosong` | ✓ DU-102-12 |
| `kosong` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |
| `spasi-saja` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |
| `berkas-kosong` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |

### Account Function@form-add-account · VD-F14

| Varian | Entri |
|---|---|
| `opsi-banyak` | ✓ DU-100-1 |
| `pilih-satu` | ✓ DU-100-2 |
| `default-terpilih` | — §9.5: «Account Function belum terpilih (placeholder) pada Create dari toolbar» |
| `opsi-dari-master` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `opsi-belum-dipakai` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `pilih-banyak` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `item-default-wajib-ada` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `sumber-kosong` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `dalam-scope` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `luar-scope` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `opsi-nonaktif` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `opsi-tidak-boleh-ada` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `per-tipe-entitas` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `nama-sama-beda-tipe` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |
| `aktor-scope-satu-tipe` | — §9.5: opsi adalah tujuh nilai tetap `FACO-LOGIC-01a` «tanpa opsi kosong», bukan master data ber-scope atau ber-status |

### form-add-account · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-103-1 |
| `batch-stay-on-form` | ✓ DU-103-2, DU-103-3 |
| `semua-tipe-kontrol-terisi` | ✓ DU-103-4 |

### create-account@tabel-account-list · VD-F9

| Varian | Entri |
|---|---|
| `valid-lengkap` | ✓ DU-020-2 |
| `batch-stay-on-form` | — §3.1: Stay on this form dan Clear Field adalah perilaku form (target form-add-account) |
| `semua-tipe-kontrol-terisi` | — §3.1: Stay on this form dan Clear Field adalah perilaku form (target form-add-account) |

### Account Code@form-edit-account · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-111-3 |
| `spasi-saja` | ✓ DU-111-4 |
| `pilihan-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |
| `berkas-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |

### Account Code@form-edit-account · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-111-5 |
| `lebih-maks` | ✓ DU-111-6 |
| `batas-maks-spasi-tepi` | ✓ DU-111-7 |
| `batas-min` | — §9.9: Min 1 sama dengan aturan wajib V-01; tidak ada panjang minimum lain |
| `kurang-min` | — §9.9: Min 1 sama dengan aturan wajib V-01; tidak ada panjang minimum lain |
| `addon-tidak-dihitung` | — §4.1.2: Text input tanpa addon |
| `opsional-kosong-tanpa-min` | — §4.1.2: Account Code Required |
| `batas-maks-spasi-tengah` | — §6 V-03: whitelist huruf Latin, angka, `-`, `_`, `.` menolak spasi dan karakter non-Latin |
| `batas-maks-unicode` | — §6 V-03: whitelist huruf Latin, angka, `-`, `_`, `.` menolak spasi dan karakter non-Latin |

### Account Code@form-edit-account · VD-F4

| Varian | Entri |
|---|---|
| `per-kelas-izin:-` | ✓ DU-111-8 |
| `per-kelas-izin:_` | ✓ DU-111-9 |
| `per-kelas-izin:.` | ✓ DU-111-10 |
| `per-kelas-tolak:spasi` | ✓ DU-111-11 |
| `per-kelas-tolak:emoji` | ✓ DU-111-12 |
| `emoji-paste` | ✓ DU-111-13 |
| `emoji-jalur-fallback` | — §6 V-03: Account Code tidak memblok ketikan; pesan tampil «Langsung saat mengetik» |
| `bebas-karakter` | — §4.1.2: Text input ber-whitelist, bukan Text Area |
| `karakter-kontrol-non-ui` | — §6 V-03: PRD tidak menetapkan hasil khusus karakter kontrol dari jalur non-UI; kelas di luar whitelist diwakili per-kelas-tolak |

### Account Name@form-edit-account · VD-F1

| Varian | Entri |
|---|---|
| `kosong` | ✓ DU-111-14 |
| `spasi-saja` | ✓ DU-111-15 |
| `pilihan-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |
| `berkas-kosong` | — §4.1.2: field ini Text input, bukan pilihan atau berkas |

### Account Name@form-edit-account · VD-F2

| Varian | Entri |
|---|---|
| `batas-maks` | ✓ DU-111-16 |
| `lebih-maks` | ✓ DU-111-17 |
| `batas-maks-spasi-tepi` | ✓ DU-111-18 |
| `batas-maks-spasi-tengah` | ✓ DU-111-19 |
| `batas-maks-unicode` | ✓ DU-111-20 |
| `addon-tidak-dihitung` | — §4.1.2: Text input tanpa addon |
| `opsional-kosong-tanpa-min` | — §4.1.2: Account Name Required |
| `batas-min` | — §9.9: Min 1 sama dengan aturan wajib V-05; tidak ada panjang minimum lain |
| `kurang-min` | — §9.9: Min 1 sama dengan aturan wajib V-05; tidak ada panjang minimum lain |

### Account Name@form-edit-account · VD-F4

| Varian | Entri |
|---|---|
| `per-kelas-tolak:emoji` | ✓ DU-111-21 |
| `emoji-paste` | ✓ DU-111-22 |
| `emoji-jalur-fallback` | ✓ DU-111-23 |
| `per-kelas-izin` | — §9.9: Account Name memakai «Blocklist emoji» tanpa daftar kelas izin |
| `bebas-karakter` | — §4.1.2: Text input satu baris, bukan Text Area |
| `karakter-kontrol-non-ui` | — §6 V-07: PRD hanya menetapkan emoji; hasil karakter kontrol dari jalur non-UI tidak dinyatakan |

### Account Function@form-edit-account · VD-F1

| Varian | Entri |
|---|---|
| `pilihan-kosong` | ✓ DU-111-24 |
| `kosong` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |
| `spasi-saja` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |
| `berkas-kosong` | — §4.1.2: Account Function adalah Select, bukan teks atau berkas |

### form-edit-account · VD-F8

| Varian | Entri |
|---|---|
| `nilai-baru` | ✓ DU-112-3 |
| `tanpa-perubahan` | ✓ DU-112-1 |
| `diubah-lalu-dikembalikan` | ✓ DU-112-7 |
| `prefill-semua-terisi` | ✓ DU-112-1 |
| `dikosongkan` | ✓ DU-112-10 |
| `tanpa-perubahan-per-tipe` | — §[F-FACO-02] k3: No-Op dinyatakan untuk seluruh submit, tidak per tipe field |
| `prefill-opsional-kosong` | — §4.1.2: ketiga field Required |
| `beda-kapital-saja` | — §[F-FACO-02] langkah 3: pembandingan dengan nilai tersimpan dilakukan server; varian ini ada di target edit-account@be |
| `spasi-tepi-saja` | — §[F-FACO-02] langkah 3: pembandingan dengan nilai tersimpan dilakukan server; varian ini ada di target edit-account@be |
| `nyata-plus-beda-kapital` | — §[F-FACO-02] langkah 3: pembandingan dengan nilai tersimpan dilakukan server; varian ini ada di target edit-account@be |

### edit-account@be · VD-F8

| Varian | Entri |
|---|---|
| `nilai-baru` | ✓ DU-151-2 |
| `tanpa-perubahan` | ✓ DU-151-3 |
| `beda-kapital-saja` | ✓ DU-151-5 |
| `spasi-tepi-saja` | ✓ DU-151-7 |
| `nyata-plus-beda-kapital` | ✓ DU-151-9 |
| `tanpa-perubahan-per-tipe` | — §[F-FACO-02] k3: No-Op dinyatakan untuk seluruh submit, tidak per tipe field |
| `diubah-lalu-dikembalikan` | — §4.1.2: mengetik ulang nilai adalah aksi form (target form-edit-account) |
| `dikosongkan` | — §4.1.2: `[Clear Field]` adalah tombol form (target form-edit-account) |
| `prefill-semua-terisi` | — §9.5: Pre-fill form Edit adalah perilaku form (target form-edit-account) |
| `prefill-opsional-kosong` | — §9.5: Pre-fill form Edit adalah perilaku form (target form-edit-account) |

### Account Code@create-be · VD-F5

| Varian | Entri |
|---|---|
| `duplikat-sama` | ✓ DU-150-2 |
| `duplikat-beda-kapital` | ✓ DU-150-3 |
| `duplikat-spasi-tepi` | ✓ DU-150-4 |
| `duplikat-luar-scope` | ✓ DU-150-6 |
| `beda-kapital-bukan-duplikat` | — §6 V-04: «tanpa membedakan huruf besar-kecil» |
| `duplikat-kombinasi` | — §6 V-04: keunikan hanya pada satu field |
| `duplikat-identifier-fisik` | — §4.1.2: Account Code bukan identifier fisik |
| `sama-dengan-diri` | — §[F-FACO-02] langkah 2: pengecualian akun sendiri hanya berlaku pada Edit |

### Account Code@edit-be · VD-F5

| Varian | Entri |
|---|---|
| `duplikat-sama` | ✓ DU-151-12, DU-151-46 |
| `duplikat-beda-kapital` | ✓ DU-151-13 |
| `duplikat-spasi-tepi` | ✓ DU-151-14 |
| `duplikat-luar-scope` | ✓ DU-151-26 |
| `sama-dengan-diri` | ✓ DU-151-3 |
| `beda-kapital-bukan-duplikat` | — §6 V-04: «tanpa membedakan huruf besar-kecil» |
| `duplikat-kombinasi` | — §6 V-04: keunikan hanya pada satu field |
| `duplikat-identifier-fisik` | — §4.1.2: Account Code bukan identifier fisik |

### Account Code@create-be · VD-F3

| Varian | Entri |
|---|---|
| `spasi-tepi` | ✓ DU-150-7 |
| `pengecualian-tanpa-trim` | — §[F-FACO-01] langkah 1: Account Code dan Account Name di-trim tanpa pengecualian |
| `lookup-spasi-tepi` | — §[F-FACO-01] langkah 1: trim dinyatakan untuk nilai form, bukan nilai lookup |
| `spasi-tengah-ganda` | — §6 V-03: spasi berada di luar whitelist, jadi nilai berspasi tengah ditolak dan tidak sampai ke trim |
| `spasi-tengah-tunggal` | — §6 V-03: spasi berada di luar whitelist, jadi nilai berspasi tengah ditolak dan tidak sampai ke trim |

### Account Name@create-be · VD-F3

| Varian | Entri |
|---|---|
| `spasi-tepi` | ✓ DU-150-8 |
| `spasi-tengah-tunggal` | ✓ DU-150-8 |
| `pengecualian-tanpa-trim` | — §[F-FACO-01] langkah 1: Account Code dan Account Name di-trim tanpa pengecualian |
| `lookup-spasi-tepi` | — §[F-FACO-01] langkah 1: trim dinyatakan untuk nilai form, bukan nilai lookup |
| `spasi-tengah-ganda` | — §[F-FACO-01] langkah 1: PRD hanya menyatakan trim; hasil spasi tengah ganda tidak dinyatakan |

### create-account@be · VD-F18

| Varian | Entri |
|---|---|
| `invalid-ui-via-api` | ✓ DU-150-11, DU-150-13, DU-150-14, DU-150-15, DU-150-16, DU-150-17, DU-150-18, DU-150-19 |
| `tipe-salah` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |
| `format-salah` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |
| `rentang-kurang-min` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |
| `rentang-lebih-maks` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |
| `payload-oversized` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |
| `payload-malformed` | — §9.9: PRD hanya menetapkan aturan per field; hasil untuk varian ini tidak dinyatakan |

### Account Name@create-be · VD-F17

| Varian | Entri |
|---|---|
| `payload-xss` | ✓ DU-150-24 |
| `payload-sqli` | ✓ DU-150-25 |
| `payload-nosqli` | ✓ DU-150-26 |
| `markup-tersimpan` | ✓ DU-150-27 |

### sel@tabel-account-list · VD-F17

| Varian | Entri |
|---|---|
| `markup-tersimpan` | ✓ DU-120-9 |
| `payload-xss` | — §5: payload pada kotak Search ada di target search@tabel-account-list |
| `payload-sqli` | — §5: payload pada kotak Search ada di target search@tabel-account-list |
| `payload-nosqli` | — §5: payload pada kotak Search ada di target search@tabel-account-list |

### nilai-tersimpan@tabel-account-list · VD-F17

| Varian | Entri |
|---|---|
| `markup-tersimpan` | ✓ DU-001-4 |
| `payload-xss` | — §5: payload pada kotak Search ada di target search@tabel-account-list |
| `payload-sqli` | — §5: payload pada kotak Search ada di target search@tabel-account-list |
| `payload-nosqli` | — §5: payload pada kotak Search ada di target search@tabel-account-list |

### search@tabel-account-list · VD-F17

| Varian | Entri |
|---|---|
| `payload-xss` | ✓ DU-002-14 |
| `payload-sqli` | ✓ DU-002-15 |
| `payload-nosqli` | ✓ DU-002-16 |
| `markup-tersimpan` | — §4.1.1: tampilan nilai ber-markup ada di target nilai-tersimpan@tabel-account-list |

### matriks-capability@be · VD-P1

| Varian | Entri |
|---|---|
| `per-baris-matriks:Total Control` | ✓ DU-152-1 |
| `per-baris-matriks:Read Only` | ✓ DU-152-2 |
| `per-baris-matriks:Manage accounting` | ✓ DU-152-3 |
| `tanpa-akses` | ✓ DU-152-10 |
| `read-only-saja` | ✓ DU-152-2 |
| `capability-tunggal:Create` | ✓ DU-152-4 |
| `capability-tunggal:Update` | ✓ DU-152-5 |
| `capability-tunggal:Delete` | ✓ DU-152-6 |
| `tanpa-capability-aksi:Create` | ✓ DU-152-8 |
| `tanpa-capability-aksi:Update` | ✓ DU-152-7 |
| `tanpa-capability-aksi:Delete` | ✓ DU-152-9 |
| `kombinasi-permission` | ✓ DU-152-7 |
| `per-kombinasi-crud` | — §4.8: kolom dibaca per huruf; gabungan huruf diwakili varian kombinasi-permission |
| `tanpa-bulk` | — §2.1: single dan bulk digerbang huruf yang sama |
| `tanpa-single-action` | — §2.1: single dan bulk digerbang huruf yang sama |
| `tanpa-sesi` | — §9.3: PRD tidak menetapkan hasil permintaan tanpa sesi |
| `access-level-null-plus-individual` | — §2.1: aktor ini sama dengan baris «Manage accounting (C/R/U/D per user)»; tidak ada varian terpisah |
| `zero-assignment` | — §2: modul tidak memakai Group Role |
| `can-read-false` | — §2: modul tidak memakai Group Role |
| `assignment-retained` | — §2: modul tidak memakai Group Role |
| `entitas-diblok-punya-role` | — §9.4.2 E-FACO-53: entitas Suspended/Expired ada di target entitas@aksi-tulis |
| `per-jenis-entitas` | — §9.11: Chart of Accounts client-wide, tanpa pembedaan jenis entitas |
| `per-peran-alur` | — §9.4.4: modul tidak memakai approval |

### matriks-role@tab-chart-of-accounts · VD-P1

| Varian | Entri |
|---|---|
| `per-baris-matriks:Total Control` | ✓ DU-040-1 |
| `per-baris-matriks:Read Only` | ✓ DU-041-1 |
| `per-baris-matriks:Manage accounting` | ✓ DU-042-1 |
| `tanpa-akses` | ✓ DU-046-1, DU-046-2 |
| `read-only-saja` | ✓ DU-041-1 |
| `capability-tunggal:Create` | ✓ DU-043-1 |
| `capability-tunggal:Update` | ✓ DU-044-1 |
| `capability-tunggal:Delete` | ✓ DU-045-1 |
| `tanpa-capability-aksi:Create` | ✓ DU-042-1 |
| `tanpa-capability-aksi:Update` | ✓ DU-042-1 |
| `tanpa-capability-aksi:Delete` | ✓ DU-042-1 |
| `kombinasi-permission` | ✓ DU-038-1 |
| `per-kombinasi-crud` | — §4.8: kolom dibaca per huruf; gabungan huruf diwakili varian kombinasi-permission |
| `tanpa-bulk` | — §2.1: single dan bulk digerbang huruf yang sama |
| `tanpa-single-action` | — §2.1: single dan bulk digerbang huruf yang sama |
| `tanpa-sesi` | — §9.3: PRD tidak menetapkan hasil permintaan tanpa sesi |
| `access-level-null-plus-individual` | — §2.1: aktor ini sama dengan baris «Manage accounting (C/R/U/D per user)»; tidak ada varian terpisah |
| `zero-assignment` | — §2: modul tidak memakai Group Role |
| `can-read-false` | — §2: modul tidak memakai Group Role |
| `assignment-retained` | — §2: modul tidak memakai Group Role |
| `entitas-diblok-punya-role` | — §9.4.2 E-FACO-53: entitas Suspended/Expired ada di target entitas@aksi-tulis |
| `per-jenis-entitas` | — §9.11: Chart of Accounts client-wide, tanpa pembedaan jenis entitas |
| `per-peran-alur` | — §9.4.4: modul tidak memakai approval |

### alamat-langsung@tab-chart-of-accounts · VD-P4

| Varian | Entri |
|---|---|
| `aktor-tanpa-read` | ✓ DU-046-1, DU-046-2 |
| `id-tidak-ada` | — §4.1.1: «modul tanpa halaman Detail», jadi tidak ada alamat ber-ID record |
| `id-sudah-dihapus` | — §4.1.1: «modul tanpa halaman Detail», jadi tidak ada alamat ber-ID record |
| `id-milik-entitas-lain` | — §4.1.1: «modul tanpa halaman Detail», jadi tidak ada alamat ber-ID record |

### entitas@aksi-tulis · VD-A4

| Varian | Entri |
|---|---|
| `active` | ✓ DU-048-1 |
| `suspended` | ✓ DU-048-2 |
| `expired` | ✓ DU-048-3 |
| `deleted` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |
| `per-jenis-entitas-pemilik` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |
| `per-peran-entitas` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |
| `job-sistem` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |
| `aksi-reaktivasi` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |
| `per-interval` | — §9.4.1 D1: PRD hanya menyatakan Suspended dan Expired; varian ini tidak punya hasil di PRD |

### plan@halaman-accounting · VD-P5

| Varian | Entri |
|---|---|
| `per-tier:starter` | ✓ DU-050-1 |
| `per-tier:growth` | ✓ DU-051-1 |
| `per-tier:professional` | ✓ DU-051-2 |
| `per-tier:enterprise` | ✓ DU-051-3 |
| `per-level:None` | ✓ DU-050-1 |
| `per-level:Full` | ✓ DU-051-1, DU-051-2, DU-051-3 |
| `basic-dalam-scope` | — §9.10: level hanya `None` dan `Full`; tidak ada Basic, add-on, atau cap per plan |
| `basic-luar-scope` | — §9.10: level hanya `None` dan `Full`; tidak ada Basic, add-on, atau cap per plan |
| `addon-dibeli` | — §9.10: level hanya `None` dan `Full`; tidak ada Basic, add-on, atau cap per plan |
| `addon-tidak-dibeli` | — §9.10: level hanya `None` dan `Full`; tidak ada Basic, add-on, atau cap per plan |
| `cap-plan-lama-beda-baru` | — §9.10: level hanya `None` dan `Full`; tidak ada Basic, add-on, atau cap per plan |

### kolom-searchable@tabel-account-list · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:Text` | ✓ DU-002-1 |
| `per-kelas-kolom:Badge` | ✓ DU-002-1 |
| `substring-tengah` | ✓ DU-002-1 |
| `beda-kapital` | ✓ DU-002-1 |
| `tanpa-hasil` | ✓ DU-002-17 |
| `kolom-non-searchable` | ✓ DU-002-2 |
| `kolom-tersembunyi` | ✓ DU-002-1 |
| `lintas-kolom` | ✓ DU-002-3, DU-002-4 |
| `karakter-pola` | ✓ DU-002-8 |
| `query-spasi-tepi` | ✓ DU-002-1 |
| `query-spasi-saja` | ✓ DU-002-18 |
| `query-spasi-tengah` | ✓ DU-002-1 |
| `query-kata-tidak-bersebelahan` | ✓ DU-002-5 |
| `nilai-substring-nilai-lain` | ✓ DU-002-6, DU-002-7 |
| `per-kelas-kolom:Number` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; kelas Number diasersi di spec `-dep-` Used By |
| `kolom-icon-label` | — §4.1.1: tidak ada kolom ikon |
| `kolom-homogen` | — §5: PRD tidak menetapkan hasil khusus untuk kolom bernilai seragam |
| `record-tab-non-default` | — §4.2a: satu panel tabel tanpa tab data |
| `cocok-di-anak-saja` | — §4.1.1: tabel datar, bukan tree |

### kolom-sortable@tabel-account-list · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-003-4 |
| `sama-tiebreak` | ✓ DU-003-4, DU-003-10 |
| `beda-kapital` | ✓ DU-003-2 |
| `per-tipe-kolom:Toggle` | ✓ DU-003-6 |
| `per-tipe-kolom:Text` | ✓ DU-003-4 |
| `per-tipe-kolom:Badge` | ✓ DU-003-8 |
| `per-tipe-kolom:Date` | ✓ DU-003-1 |
| `aksen` | ✓ DU-003-1, DU-003-5, DU-003-9 |
| `diawali-angka-simbol` | ✓ DU-003-3, DU-003-7 |
| `default-beda` | ✓ DU-003-4 |
| `sisip-beda-default` | ✓ DU-003-1 |
| `lintas-halaman` | ✓ DU-003-11 |
| `sama-melintasi-halaman` | ✓ DU-003-11 |
| `urutan-beda-antar-kolom` | ✓ DU-003-4 |
| `per-tipe-kolom:Number` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; sort Numeric diasersi di spec `-dep-` Used By |
| `kosong` | — §4.1.1: kolom Account List «Tidak pernah kosong» kecuali Last Used in Journal, yang hanya terisi lewat Export Journal (spec `-dep-`) |
| `natural` | — §4.1.1: Account Code «Alphabetical (A-Z)»; urutan numerik hanya pada Used By (spec `-dep-`) |
| `sama-di-kolom-dan-default` | — §4.1.1: kolom default Account Code unik per company |
| `jumlah-chip-sama` | — §4.1.1: tidak ada kolom multi-nilai |
| `jumlah-aktif-sama` | — §4.1.1: tidak ada kolom multi-nilai |
| `campuran-tipe` | — §4.1.1: kolom campuran tipe hanya ada di Changelog |
| `format-komposit` | — §4.1.1: tidak ada kolom ukuran atau alamat |
| `nama-tampil-beda-nama-penuh` | — §4.1.1: basis nama penuh dinyatakan untuk Modified By Changelog, bukan Account List |
| `urutan-custom` | — §4.1.1: Function «Alphabetical (A-Z) by label» |

### field-filter@tabel-account-list · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-004-1 |
| `tidak-cocok` | ✓ DU-004-3 |
| `and-a-saja` | ✓ DU-004-2 |
| `and-b-saja` | ✓ DU-004-3 |
| `and-keduanya` | ✓ DU-004-1 |
| `and-tidak-keduanya` | ✓ DU-004-4 |
| `or-dalam-field` | ✓ DU-004-5 |
| `search-saja` | ✓ DU-004-3 |
| `filter-saja` | ✓ DU-004-2 |
| `search-dan-filter` | ✓ DU-004-1 |
| `irisan-kosong` | ✓ DU-004-5 |
| `kolom-tersembunyi` | ✓ DU-004-1 |
| `boolean-kedua-nilai` | ✓ DU-004-2 |
| `rentang-dalam` | ✓ DU-004-1 |
| `rentang-luar` | ✓ DU-004-1 |
| `rentang-tepat-awal` | ✓ DU-004-1 |
| `rentang-tepat-akhir` | ✓ DU-004-1 |
| `rentang-sehari` | ✓ DU-004-1 |
| `per-kelas-kontrol:Multi-select` | ✓ DU-004-1 |
| `per-kelas-kontrol:Date range` | ✓ DU-004-1 |
| `mutasi-keluar-saringan` | ✓ DU-004-6 |
| `mutasi-masuk-saringan` | ✓ DU-004-7 |
| `filter-only` | — §5: setiap field Filter Panel punya kolom tabel |
| `custom-field-per-tipe` | — §5: tidak ada custom field |
| `create-tidak-cocok` | — §[F-FACO-01] langkah 5: Create mengosongkan Search dan Filter Panel |
| `status-dikecualikan` | — §4.1.1: tidak ada status internal |
| `default-filter-lolos` | — §9.5: «Default filter tabel | Tidak ada» |
| `default-filter-tersaring` | — §9.5: «Default filter tabel | Tidak ada» |
| `range-tepat-min` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; rentang Min / Max ada di target filter-used-by |
| `range-tepat-max` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; rentang Min / Max ada di target filter-used-by |
| `range-hanya-min` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; rentang Min / Max ada di target filter-used-by |
| `range-hanya-max` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; rentang Min / Max ada di target filter-used-by |
| `range-min-lebih-max` | — §9.7: Used By adalah Derived view dari pemakaian akun oleh Asset Class, jadi nilai > 0 hanya terbentuk lewat Asset Class; rentang Min / Max ada di target filter-used-by |

### filter-used-by@tabel-account-list · VD-T3

| Varian | Entri |
|---|---|
| `rentang-luar` | ✓ DU-060-1 |
| `range-tepat-min` | ✓ DU-060-2 |
| `range-tepat-max` | ✓ DU-060-1 |
| `range-hanya-min` | ✓ DU-060-1 |
| `range-hanya-max` | ✓ DU-060-5 |
| `range-min-lebih-max` | — §4.1.1: PRD tidak menetapkan hasil Min yang lebih besar dari Max |
| `cocok` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `tidak-cocok` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `and-a-saja` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `and-b-saja` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `and-keduanya` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `and-tidak-keduanya` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `or-dalam-field` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `search-saja` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `filter-saja` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `search-dan-filter` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `irisan-kosong` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `kolom-tersembunyi` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `filter-only` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `boolean-kedua-nilai` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `rentang-dalam` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `rentang-tepat-awal` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `rentang-tepat-akhir` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `rentang-sehari` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `custom-field-per-tipe` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `per-kelas-kontrol` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `mutasi-keluar-saringan` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `mutasi-masuk-saringan` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `create-tidak-cocok` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `status-dikecualikan` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `default-filter-lolos` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |
| `default-filter-tersaring` | — §4.1.1: field Used By hanya «Min / Max numerik»; varian ini milik target field-filter |

### filter-last-used@tabel-account-list · VD-T3

| Varian | Entri |
|---|---|
| `rentang-dalam` | ✓ DU-076-3 |
| `rentang-luar` | ✓ DU-076-1, DU-076-5 |
| `rentang-tepat-awal` | ✓ DU-076-4 |
| `rentang-tepat-akhir` | ✓ DU-076-2 |
| `rentang-sehari` | ✓ DU-076-3 |
| `cocok` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `tidak-cocok` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `and-a-saja` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `and-b-saja` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `and-keduanya` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `and-tidak-keduanya` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `or-dalam-field` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `search-saja` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `filter-saja` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `search-dan-filter` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `irisan-kosong` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `kolom-tersembunyi` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `filter-only` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `boolean-kedua-nilai` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `range-tepat-min` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `range-tepat-max` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `range-hanya-min` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `range-hanya-max` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `range-min-lebih-max` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `custom-field-per-tipe` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `per-kelas-kontrol` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `mutasi-keluar-saringan` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `mutasi-masuk-saringan` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `create-tidak-cocok` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `status-dikecualikan` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `default-filter-lolos` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |
| `default-filter-tersaring` | — §4.1.1: field Last Used in Journal hanya date range granularitas bulan; varian ini milik target field-filter |

### opsi-filter@tabel-account-list · VD-T4

| Varian | Entri |
|---|---|
| `nilai-berulang` | ✓ DU-005-2 |
| `kolom-tanpa-null` | ✓ DU-005-2 |
| `master-tak-terpakai` | ✓ DU-005-1 |
| `enum-sebagian-terisi` | ✓ DU-005-1 |
| `nilai-baru-saat-uji` | ✓ DU-005-6 |
| `opsi-hilang` | ✓ DU-005-5 |
| `kosong` | — §4.1.1: kolom ber-filter multi-select «Tidak pernah kosong» |
| `per-anggota-enum` | — §9.5: opsi hanya nilai yang ada di data tabel; kelengkapan tujuh nilai bukan keadaan yang dinyatakan |
| `nilai-di-cakupan-lain` | — §4.2a: satu panel tabel tanpa tab data |
| `nilai-kondisional` | — §4.1.1: tidak ada opsi bersyarat |
| `opsi-tidak-dipersempit-search` | — §9.5: PRD tidak menyatakan hubungan opsi dengan Search aktif |
| `opsi-tetap-worm` | — §4.1.1: tabel akun bukan log |
| `entitas-terhapus-berhistori` | — §4.1.1: opsi berasal dari nilai baris akun, bukan entitas berhistori |
| `entitas-rename-berhistori` | — §4.1.1: opsi berasal dari nilai baris akun, bukan entitas berhistori |
| `satu-nilai-distinct` | — §4.1.1: kolom Active dan Function «Filterable ✅» tanpa pengecualian jumlah nilai |
| `dua-nilai-distinct` | — §4.1.1: kolom Active dan Function «Filterable ✅» tanpa pengecualian jumlah nilai |
| `opsi-banyak-overflow` | — §4.1.1: mekanik dropdown filter ada di target dropdown-filter (ui-client) |
| `cari-opsi-substring` | — §4.1.1: mekanik dropdown filter ada di target dropdown-filter (ui-client) |
| `cari-opsi-beda-kapital` | — §4.1.1: mekanik dropdown filter ada di target dropdown-filter (ui-client) |
| `cari-opsi-tanpa-hasil` | — §4.1.1: mekanik dropdown filter ada di target dropdown-filter (ui-client) |
| `sumber-kosong` | — §4.1.1: mekanik dropdown filter ada di target dropdown-filter (ui-client) |

### dropdown-filter@tabel-account-list · VD-T4

| Varian | Entri |
|---|---|
| `opsi-banyak-overflow` | ✓ DU-123-1 |
| `cari-opsi-substring` | ✓ DU-123-9 |
| `cari-opsi-beda-kapital` | ✓ DU-123-9 |
| `cari-opsi-tanpa-hasil` | ✓ DU-123-9 |
| `sumber-kosong` | ✓ DU-123-8 |
| `nilai-berulang` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `kosong` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `kolom-tanpa-null` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `master-tak-terpakai` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `enum-sebagian-terisi` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `per-anggota-enum` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `nilai-di-cakupan-lain` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `nilai-kondisional` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `opsi-tidak-dipersempit-search` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `nilai-baru-saat-uji` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `opsi-hilang` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `opsi-tetap-worm` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `entitas-terhapus-berhistori` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `entitas-rename-berhistori` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `satu-nilai-distinct` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |
| `dua-nilai-distinct` | — §9.5: isi opsi ditentukan data tabel (target opsi-filter); spec ini hanya mekanik dropdown |

### paginasi@tabel-account-list · VD-T5

| Varian | Entri |
|---|---|
| `lebih-satu-halaman` | ✓ DU-122-1 |
| `satu-baris-halaman-terakhir` | ✓ DU-122-3 |
| `tepat-ukuran-halaman` | ✓ DU-122-2 |
| `lebih-ukuran-terpilih:10` | ✓ DU-122-3 |
| `lebih-ukuran-terpilih:25` | ✓ DU-122-1 |
| `lebih-ukuran-terpilih:50` | ✓ DU-122-1 |
| `lebih-ukuran-terpilih:100` | ✓ DU-122-1 |
| `lebih-ukuran-maks` | ✓ DU-122-1 |
| `tersaring-lebih-satu-halaman` | ✓ DU-122-4 |
| `nomor-halaman-invalid` | ✓ DU-122-6 |

### seleksi@tabel-account-list · VD-T14

| Varian | Entri |
|---|---|
| `satu-baris` | ✓ DU-125-1 |
| `banyak-baris` | ✓ DU-125-1 |
| `halaman-penuh` | ✓ DU-125-1 |
| `checkbox-disabled` | ✓ DU-125-5 |
| `lintas-halaman` | ✓ DU-125-1 |
| `tersembunyi-filter` | ✓ DU-125-1 |
| `homogen:Active` | ✓ DU-125-1 |
| `homogen:Inactive` | ✓ DU-125-2 |
| `campuran-state` | ✓ DU-125-2 |
| `single-select-ganti` | — §4.2a: DataTable varian Multiple Selection |

### counter-seleksi@tabel-account-list · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-125-1 |
| `jumlah-banyak` | ✓ DU-125-1 |
| `jumlah-nol` | — §5: Bulk Action Bar muncul saat ≥1 baris terpilih |
| `per-jumlah-independen` | — §5: counter hanya memuat satu jumlah |

### selection-limit@tabel-account-list · VD-A6

| Varian | Entri |
|---|---|
| `per-jenis-limit:Selection Limit` | ✓ DU-125-3 |
| `di-bawah` | ✓ DU-125-3 |
| `tepat-batas` | ✓ DU-125-4 |
| `lebih-batas` | ✓ DU-125-5 |
| `tersaring-lebih-limit` | ✓ DU-125-6 |
| `sisa-satu` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `limit-diturunkan` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `over-cap-downgrade` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `tersimpan-melebihi-batas-baru` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `tanpa-cap-mobile` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `berurutan-stay-on-form` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `saldo-cukup` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `saldo-kurang` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |
| `kuota-status-akun` | — §9.4.2 E-FACO-62: hanya Selection Limit pada seleksi bulk yang dinyatakan; varian ini tidak punya hasil di PRD |

### batas-jumlah-akun@create-account · VD-A6

| Varian | Entri |
|---|---|
| `per-jenis-limit:Master Data Count Limit` | ✓ DU-159-1 |
| `di-bawah` | ✓ DU-159-6 |
| `tepat-batas` | ✓ DU-159-6, DU-159-11 |
| `lebih-batas` | ✓ DU-159-7 |
| `sisa-satu` | ✓ DU-159-9, DU-159-10 |
| `kuota-status-akun` | ✓ DU-159-3, DU-159-4, DU-159-5 |
| `berurutan-stay-on-form` | — §4.1.2: Stay on this form adalah perilaku form; reaksi UI saat batas tercapai ada di spec ui-client |
| `limit-diturunkan` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `over-cap-downgrade` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tersimpan-melebihi-batas-baru` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tersaring-lebih-limit` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tanpa-cap-mobile` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `saldo-cukup` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `saldo-kurang` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |

### batas-jumlah-akun@tab-chart-of-accounts · VD-A6

| Varian | Entri |
|---|---|
| `per-jenis-limit:Master Data Count Limit` | ✓ DU-129-1 |
| `di-bawah` | ✓ DU-129-1 |
| `tepat-batas` | ✓ DU-129-2 |
| `lebih-batas` | ✓ DU-129-3 |
| `sisa-satu` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `limit-diturunkan` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `over-cap-downgrade` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tersimpan-melebihi-batas-baru` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tersaring-lebih-limit` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `tanpa-cap-mobile` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `berurutan-stay-on-form` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `saldo-cukup` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `saldo-kurang` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |
| `kuota-status-akun` | — §3.1: batas jumlah akun (`FACO-LOGIC-10`) hanya dicek pada Create Account; PRD tidak menetapkan hasil varian ini |

### sel@tabel-account-list · VD-T7

| Varian | Entri |
|---|---|
| `null` | ✓ DU-120-4 |
| `string-kosong` | ✓ DU-120-7 |
| `nol-numerik` | ✓ DU-120-3 |
| `kosong-tidak-pernah-diisi` | ✓ DU-120-3 |
| `teks-panjang` | ✓ DU-120-8 |
| `per-nilai-badge:Asset Cost` | ✓ DU-120-1 |
| `per-nilai-badge:Accumulated Depreciation` | ✓ DU-120-2 |
| `per-nilai-badge:Depreciation Expense` | ✓ DU-120-3 |
| `per-nilai-badge:Gain on Disposal` | ✓ DU-120-4 |
| `per-nilai-badge:Loss on Disposal` | ✓ DU-120-5 |
| `per-nilai-badge:Capitalization Offset` | ✓ DU-120-6 |
| `per-nilai-badge:Disposal Proceeds` | ✓ DU-120-7 |
| `nilai-beda-antar-kolom` | ✓ DU-120-8 |
| `aktor-system` | ✓ DU-120-6 |
| `kosong-setelah-dihapus` | — §9.4.3 N-07: Last Used in Journal tidak pernah dikosongkan |
| `nilai-turunan` | — §9.7: Used By adalah Derived view dari Asset Class; nilainya diasersi di spec `-dep-` |
| `asal-jalur` | — §9.7: di ui-client asal data tidak mengubah tampilan |
| `array-kosong` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `boolean-null` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `tanggal-null` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `teks-panjang-multibaris` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `tanpa-foto` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `angka-ribuan` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `angka-pembulatan` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `referensi-terhapus` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |
| `referensi-diarsipkan` | — §4.1.1: kolom lain «Tidak pernah kosong» dan tidak ada tipe kolom untuk varian ini |

### kolom-modified-by@tabel-account-list · VD-T10

| Varian | Entri |
|---|---|
| `satu-kata` | ✓ DU-120-2 |
| `dua-kata` | ✓ DU-120-1 |
| `tiga-kata-lebih` | ✓ DU-120-3 |
| `nama-panjang` | ✓ DU-120-7 |
| `tanpa-last-name` | ✓ DU-120-2 |
| `nama-mirip` | ✓ DU-120-4, DU-120-5 |

### kolom-last-updated@tabel-account-list · VD-T13

| Varian | Entri |
|---|---|
| `hari-lebih-12` | ✓ DU-120-1 |
| `dekat-tengah-malam` | ✓ DU-120-2 |

### empty-state@tabel-account-list · VD-T6

| Varian | Entri |
|---|---|
| `entitas-kosong` | ✓ DU-121-2 |
| `jadi-kosong-setelah-hapus` | ✓ DU-121-1 |
| `kosong-untuk-aktor-ini` | — §9.11: semua aktor ber-akses melihat himpunan akun yang sama |
| `log-kosong` | — §7.1 ST-20: empty state Changelog diasersi di spec modal Changelog |
| `relasi-kosong` | — §7.1: empty state hanya untuk tabel Account List dan modal Changelog; varian ini tidak punya padanan |
| `node-tanpa-anak` | — §7.1: empty state hanya untuk tabel Account List dan modal Changelog; varian ini tidak punya padanan |

### bulk-deactivate@tabel-account-list · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-026-1 |
| `n-banyak` | ✓ DU-026-2, DU-026-3, DU-026-4 |
| `daftar-melebihi-tampil` | ✓ DU-026-6 |
| `nol-item` | — §5: Bulk Action Bar muncul saat ≥1 baris terpilih |
| `termasuk-baris-terlindungi` | — §2.2: tabel akun tidak punya baris terlindungi (Default User hanya tingkat akses aktor) |
| `campuran` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `semua-ditolak` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `semua-ditolak-alasan-single` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `jadi-tidak-eligible-saat-submit` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `gagal-banyak` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `item-beranotasi` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |
| `sisa-satu-relevan` | — §3.3: Deactivate hanya diblokir bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); varian ini ada di target bulk-deactivate-diblokir |

### bulk-deactivate-diblokir@tabel-account-list · VD-A1

| Varian | Entri |
|---|---|
| `campuran` | ✓ DU-062-1 |
| `semua-ditolak` | ✓ DU-061-1 |
| `semua-ditolak-alasan-single` | ✓ DU-061-1 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-067-1 |
| `item-beranotasi` | ✓ DU-062-3 |
| `sisa-satu-relevan` | ✓ DU-062-5 |
| `nol-item` | — §5: Bulk Action Bar muncul saat ≥1 baris terpilih |
| `termasuk-baris-terlindungi` | — §2.2: tabel akun tidak punya baris terlindungi (Default User hanya tingkat akses aktor) |
| `gagal-banyak` | — §7.2 T-05: toast parsial satu kalimat tanpa rincian per item |
| `n-1` | — §3.3: bulk yang seluruhnya lolos guard ada di target bulk-deactivate |
| `n-banyak` | — §3.3: bulk yang seluruhnya lolos guard ada di target bulk-deactivate |
| `daftar-melebihi-tampil` | — §3.3: bulk yang seluruhnya lolos guard ada di target bulk-deactivate |

### bulk-delete@tabel-account-list · VD-A1

| Varian | Entri |
|---|---|
| `n-1` | ✓ DU-029-1 |
| `n-banyak` | ✓ DU-029-2, DU-029-3, DU-029-4 |
| `daftar-melebihi-tampil` | ✓ DU-029-5 |
| `nol-item` | — §5: Bulk Action Bar muncul saat ≥1 baris terpilih |
| `termasuk-baris-terlindungi` | — §2.2: tabel akun tidak punya baris terlindungi (Default User hanya tingkat akses aktor) |
| `campuran` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `semua-ditolak` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `semua-ditolak-alasan-single` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `jadi-tidak-eligible-saat-submit` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `gagal-banyak` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `item-beranotasi` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |
| `sisa-satu-relevan` | — §3.4: penolakan Delete butuh akun terekspor, dipakai Asset Class, atau default company (data modul lain); varian ini ada di target bulk-delete-diblokir |

### bulk-delete-diblokir@tabel-account-list · VD-A1

| Varian | Entri |
|---|---|
| `campuran` | ✓ DU-064-1 |
| `semua-ditolak` | ✓ DU-063-1 |
| `semua-ditolak-alasan-single` | ✓ DU-063-1 |
| `jadi-tidak-eligible-saat-submit` | ✓ DU-068-1 |
| `item-beranotasi` | ✓ DU-064-3 |
| `sisa-satu-relevan` | ✓ DU-064-5 |
| `nol-item` | — §5: Bulk Action Bar muncul saat ≥1 baris terpilih |
| `termasuk-baris-terlindungi` | — §2.2: tabel akun tidak punya baris terlindungi (Default User hanya tingkat akses aktor) |
| `gagal-banyak` | — §7.2 T-06: toast parsial satu kalimat tanpa rincian per item |
| `n-1` | — §3.4: bulk yang seluruhnya lolos guard ada di target bulk-delete |
| `n-banyak` | — §3.4: bulk yang seluruhnya lolos guard ada di target bulk-delete |
| `daftar-melebihi-tampil` | — §3.4: bulk yang seluruhnya lolos guard ada di target bulk-delete |

### status-akun@tabel-account-list · VD-A5

| Varian | Entri |
|---|---|
| `per-status:Active` | ✓ DU-027-3 |
| `per-status:Inactive` | ✓ DU-027-1, DU-027-2 |
| `transisi-valid` | ✓ DU-027-1, DU-027-2 |
| `sudah-di-state-tujuan` | ✓ DU-027-3 |
| `transisi-mundur` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `transisi-ilegal` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `state-final` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `state-transien` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `flag-terkunci` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `per-kondisi-disabled` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |
| `koheren-rantai-gate` | — §9.4.1 D3: state akun hanya Active dan Inactive; varian ini tidak punya padanan |

### guard-deactivate@account · VD-A2

| Varian | Entri |
|---|---|
| `dipakai` | ✓ DU-165-4 |
| `tidak-dipakai` | ✓ DU-165-7, DU-165-8 |
| `per-jenis-pemakai:Asset Class` | ✓ DU-165-4 |
| `pemakai-status-lain` | ✓ DU-165-6 |
| `dipakai-multi-konsumen` | ✓ DU-165-5 |
| `pemakai-di-recycle-bin` | — §9.2: PRD tidak menyebut Recycle Bin untuk Asset Class pemakai |
| `pemakai-snapshot` | — §9.2: `snapshot_consumers[]` (berkas export dan entri log) tidak dibaca guard Deactivate |

### guard-delete@account · VD-A2

| Varian | Entri |
|---|---|
| `dipakai` | ✓ DU-166-4 |
| `tidak-dipakai` | ✓ DU-166-7, DU-166-8 |
| `per-jenis-pemakai:Asset Class` | ✓ DU-166-4 |
| `pemakai-status-lain` | ✓ DU-166-6 |
| `dipakai-multi-konsumen` | ✓ DU-166-5 |
| `pemakai-di-recycle-bin` | — §9.2: PRD tidak menyebut Recycle Bin untuk Asset Class pemakai |
| `pemakai-snapshot` | — §9.2: akun dengan riwayat export diatur Guard 1 (spec akun terekspor) |

### konkurensi@account · VD-A7

| Varian | Entri |
|---|---|
| `diubah-pihak-lain` | ✓ DU-151-33, DU-151-34 |
| `dihapus-pihak-lain` | ✓ DU-151-36 |
| `target-sama-nilai-beda` | ✓ DU-151-30, DU-151-31, DU-151-47, DU-151-55, DU-151-56 |
| `per-pasangan-aksi:Edit-Activate` | ✓ DU-151-48, DU-151-49 |
| `per-pasangan-aksi:Edit-Deactivate` | ✓ DU-151-50, DU-151-51 |
| `per-pasangan-aksi:Delete-Edit` | ✓ DU-151-52, DU-151-53 |
| `create-nilai-sama-serentak` | ✓ DU-151-41 |
| `status-diubah-pihak-lain` | ✓ DU-151-38 |
| `jadi-dipakai-saat-confirm` | — §9.7: pemakaian akun (Used By) berasal dari Asset Class; varian ini ada di target cek-ulang spec `-dep-` |
| `bulk-semua-jadi-dipakai` | — §9.7: pemakaian akun (Used By) berasal dari Asset Class; varian ini ada di target cek-ulang spec `-dep-` |
| `bulk-sebagian-jadi-dipakai` | — §9.7: pemakaian akun (Used By) berasal dari Asset Class; varian ini ada di target cek-ulang spec `-dep-` |
| `target-beda` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `create-bersamaan` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `nilai-guard-berubah` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `dibuat-pihak-lain` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `pihak-lain-cocok-saringan` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `pihak-lain-tidak-cocok-saringan` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `pihak-lain-halaman-lain` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `pihak-lain-ubah-baris-terseleksi` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |
| `permintaan-basi` | — §9.4.1 D6: PRD hanya menyatakan Edit bersamaan, kunci berubah, akun menjadi dipakai, dan double-submit; varian ini tidak punya hasil di PRD |

### cek-ulang-deactivate@account · VD-A7

| Varian | Entri |
|---|---|
| `jadi-dipakai-saat-confirm` | ✓ DU-067-1 |
| `bulk-semua-jadi-dipakai` | ✓ DU-067-4 |
| `bulk-sebagian-jadi-dipakai` | ✓ DU-067-3 |
| `diubah-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `dihapus-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `target-sama-nilai-beda` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `target-beda` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `per-pasangan-aksi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `create-nilai-sama-serentak` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `create-bersamaan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `status-diubah-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `nilai-guard-berubah` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `dibuat-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-cocok-saringan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-tidak-cocok-saringan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-halaman-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-ubah-baris-terseleksi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `permintaan-basi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |

### cek-ulang-delete@account · VD-A7

| Varian | Entri |
|---|---|
| `jadi-dipakai-saat-confirm` | ✓ DU-068-1 |
| `bulk-semua-jadi-dipakai` | ✓ DU-068-4 |
| `bulk-sebagian-jadi-dipakai` | ✓ DU-068-3 |
| `diubah-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `dihapus-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `target-sama-nilai-beda` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `target-beda` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `per-pasangan-aksi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `create-nilai-sama-serentak` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `create-bersamaan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `status-diubah-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `nilai-guard-berubah` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `dibuat-pihak-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-cocok-saringan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-tidak-cocok-saringan` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-halaman-lain` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `pihak-lain-ubah-baris-terseleksi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |
| `permintaan-basi` | — §7.3: cek ulang saat Confirm hanya menyangkut akun yang menjadi dipakai; varian lain ada di target konkurensi@account |

### changelog@account · VD-L1

| Varian | Entri |
|---|---|
| `create` | ✓ DU-155-3 |
| `edit-per-field:Account Code` | ✓ DU-155-9 |
| `edit-per-field:Account Name` | ✓ DU-155-5 |
| `edit-per-field:Account Function` | ✓ DU-155-7 |
| `edit-per-field:Status` | ✓ DU-155-12 |
| `delete` | ✓ DU-155-14 |
| `bulk` | ✓ DU-155-15, DU-155-16, DU-156-9, DU-156-10 |
| `per-aksi-non-crud:Activate` | ✓ DU-155-12 |
| `per-aksi-non-crud:Deactivate` | ✓ DU-155-13 |
| `per-baris-pencatatan:L-01` | ✓ DU-155-3 |
| `per-baris-pencatatan:L-02` | ✓ DU-155-5 |
| `per-baris-pencatatan:L-03` | ✓ DU-155-12 |
| `per-baris-pencatatan:L-04` | ✓ DU-155-14 |
| `per-varian-jalur:Request API langsung` | ✓ DU-155-17 |
| `field-badge-enum` | ✓ DU-155-7 |
| `nilai-kosong` | ✓ DU-155-3, DU-155-14 |
| `edit-multi-field` | ✓ DU-155-11 |
| `per-sub-konteks` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `field-sub-item` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `field-permission` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `field-tanpa-teks` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `nilai-awal` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `assign` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `remove` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `update-setelah-assign` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `approve-dari-approvals` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `reject-dari-approvals` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `settings-tanpa-nama` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `reset-ke-default` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `reset-sudah-default` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `per-event` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |
| `event-sesi` | — §8.1: kejadian yang dicatat hanya `L-01` sampai `L-04` dan `L-10`; varian ini tidak punya padanan |

### changelog-tanpa-entri@account · VD-L2

| Varian | Entri |
|---|---|
| `tanpa-perubahan` | ✓ DU-156-6 |
| `record-lain-tak-terlibat` | ✓ DU-156-5 |
| `efek-samping-tanpa-log` | — §8.1: PRD tidak menyebut efek otomatis tanpa entri |
| `entri-entitas-lain` | — §9.11: PRD tidak menyatakan isolasi entri antar-entitas untuk Changelog |
| `bulk-dengan-skip` | — §3.3: item hanya dilewati bila Used By > 0 (`FACO-LOGIC-02c`, data Asset Class); diasersi di spec `-dep-` |

### changelog-snapshot@account · VD-L3

| Varian | Entri |
|---|---|
| `edit-beruntun` | ✓ DU-011-1 |
| `snapshot-setelah-rename` | ✓ DU-011-1 |
| `edit-nama-sendiri` | — §8.1: entri mencatat akun, bukan pengguna |
| `edit-beruntun-dua-aktor` | — §[F-FACO-02] k5: Edit dua admin diasersi di be-e2e |
| `multi-entri-aktor-beda` | — §[F-FACO-02] k5: Edit dua admin diasersi di be-e2e |
| `timestamp-sama` | — §8.1: PRD tidak menetapkan urutan entri ber-timestamp sama |
| `record-tanpa-entri` | — §8.4: setiap jalur pembuatan akun menulis `L-01`, jadi akun tanpa entri tidak terbentuk lewat jalur yang dinyatakan |

### jalur-api@account · VD-A8

| Varian | Entri |
|---|---|
| `per-jalur:Request API langsung` | ✓ DU-155-2 |
| `dengan-aktor` | ✓ DU-155-2 |
| `tanpa-aktor` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `butuh-normalisasi` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `pasangan-manual-setara` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `duplikat-dalam-batch` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `duplikat-dengan-data-ada` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `import-semua-valid` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `import-sebagian-error` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |

### jalur-export@account · VD-A8

| Varian | Entri |
|---|---|
| `per-jalur:Export Journal berhasil` | ✓ DU-167-4 |
| `dengan-aktor` | ✓ DU-167-1 |
| `tanpa-aktor` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `butuh-normalisasi` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `pasangan-manual-setara` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `duplikat-dalam-batch` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `duplikat-dengan-data-ada` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `import-semua-valid` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |
| `import-sebagian-error` | — §8.4: jalur non-form hanya `J-04` dan `J-06`; Import dimiliki `import/` |

### update-last-used@account · VD-R1

| Varian | Entri |
|---|---|
| `per-kondisi:F-FACO-08.k1` | ✓ DU-167-4 |
| `per-kondisi:F-FACO-08.k2` | ✓ DU-167-5 |
| `per-kondisi:F-FACO-08.k3` | ✓ DU-167-7 |
| `efek-samping-per-cabang` | ✓ DU-167-4 |
| `lolos-semua-cabang` | — §9.2 F-FACO-08: tiga kondisi saling eksklusif; tidak ada cabang penolakan untuk diloloskan |
| `per-langkah-logic` | — §9.9: PRD tidak memuat dokumen API; cabang dinyatakan lewat ID kondisi |
| `per-baris-error-handling` | — §9.9: PRD tidak memuat dokumen API; cabang dinyatakan lewat ID kondisi |

### download@tabel-account-list · VD-D1

| Varian | Entri |
|---|---|
| `tanpa-saringan-lebih-satu-halaman` | ✓ DU-008-1 |
| `hasil-tersaring` | ✓ DU-008-2 |
| `nol-baris` | ✓ DU-008-6 |
| `urutan-sort-aktif` | ✓ DU-008-1 |
| `kolom-tersembunyi` | ✓ DU-008-1 |
| `per-tab` | — §4.2a: tabel tanpa tab data |

### isi-berkas@download-account-list · VD-D2

| Varian | Entri |
|---|---|
| `switch-kedua-nilai` | ✓ DU-157-3, DU-157-4 |
| `per-nilai-badge:Asset Cost` | ✓ DU-157-3 |
| `per-nilai-badge:Accumulated Depreciation` | ✓ DU-157-4 |
| `per-nilai-badge:Depreciation Expense` | ✓ DU-157-5 |
| `per-nilai-badge:Gain on Disposal` | ✓ DU-157-6 |
| `per-nilai-badge:Loss on Disposal` | ✓ DU-157-7 |
| `per-nilai-badge:Capitalization Offset` | ✓ DU-157-8 |
| `per-nilai-badge:Disposal Proceeds` | ✓ DU-157-10 |
| `nama-user-lengkap` | ✓ DU-157-2 |
| `nilai-kosong` | ✓ DU-157-4 |
| `kolom-foto` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `kolom-ikon` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `multi-badge` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `lebih-dua-badge` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `hierarki-penuh` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `leaf-sama-parent-beda` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `item-flat` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `boolean-kedua-nilai` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `numerik-terformat` | — §4.1.1: tidak ada kolom bertipe ini di Account List |
| `mata-uang` | — §4.1.1: tidak ada kolom bertipe ini di Account List |

### csv@download-account-list · VD-D3

| Varian | Entri |
|---|---|
| `nilai-koma` | ✓ DU-157-5 |
| `nilai-kutip` | ✓ DU-157-6 |
| `non-ascii` | ✓ DU-157-7 |
| `nilai-baris-baru` | — §4.1.2: Account Name Text input satu baris |

### ambang-download@tabel-account-list · VD-A13

| Varian | Entri |
|---|---|
| `di-bawah-ambang` | ✓ DU-128-2 |
| `tepat-ambang` | ✓ DU-128-3 |
| `lebih-ambang` | ✓ DU-128-4 |

### asset-name-count@popup-used-by · VD-T12

| Varian | Entri |
|---|---|
| `jumlah-satu` | ✓ DU-140-3 |
| `jumlah-banyak` | ✓ DU-140-2 |
| `jumlah-nol` | ✓ DU-140-4 |
| `per-jumlah-independen` | — §4.1.4: tiap bullet hanya memuat satu jumlah |

### konsumen@asset-class · VD-X1

| Varian | Entri |
|---|---|
| `konsumen-relasi` | ✓ DU-069-1 |
| `fk-create` | ✓ DU-069-9 |
| `fk-edit` | ✓ DU-069-1 |
| `fk-delete` | ✓ DU-069-5 |
| `konsumen-sudah-ada` | ✓ DU-069-1 |
| `per-konsekuensi-lifecycle:Activate` | ✓ DU-069-4 |
| `per-konsekuensi-lifecycle:Deactivate` | ✓ DU-069-2 |
| `per-konsekuensi-lifecycle:Delete` | ✓ DU-069-5 |
| `arah-a-ke-b` | ✓ DU-069-9 |
| `arah-b-ke-a` | ✓ DU-069-8 |
| `turunan` | ✓ DU-069-7 |
| `konsumen-snapshot` | — §9.7: konsumen Snapshot adalah entri log dan berkas export lama, bukan Asset Class |
| `state-reflected` | — §9.7: state Reflected dari Asset Class hanya tampil di popup Used By (spec Used By) |
| `propagasi-event` | — §9.7: propagasi «dalam transaksi yang sama», bukan event |
| `per-konsumen` | — §11.1: konsumen lain punya spec `-dep-` sendiri |
| `state-dari-modul-trigger` | — §9.7: state yang dipicu Asset Class hanya Used By (varian arah-b-ke-a) |

### flag-tur@tab-chart-of-accounts · VD-S3

| Varian | Entri |
|---|---|
| `flag-belum` | ✓ DU-016-1, DU-016-2 |
| `flag-sudah` | ✓ DU-016-1 |
| `flag-sudah-device-lain` | ✓ DU-016-1 |

### format-tanggal@tabel-account-list · VD-S1

| Varian | Entri |
|---|---|
| `nilai-default` | ✓ DU-095-1 |
| `nilai-diubah` | ✓ DU-095-3, DU-095-7 |
| `per-opsi-format-tanggal:dd/MM/yy` | ✓ DU-095-1 |
| `per-opsi-format-tanggal:M/d/yy` | ✓ DU-095-3 |
| `per-opsi-format-tanggal:dd MMM yy` | ✓ DU-095-4 |
| `per-opsi-format-tanggal:DDD, MMM dd, yy` | ✓ DU-095-5 |
| `per-opsi-format-tanggal:DDD, MMM dd, yyyy` | ✓ DU-095-6 |
| `zona-waktu-non-default` | ✓ DU-095-8 |
| `per-nilai-setting` | — §4.1.1: hanya Date Format, Time Format, dan Time Zone General Settings yang dibaca modul |
| `record-sebelum-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `record-sesudah-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `format-regional-beda-entitas` | — §9.11: PRD tidak menyatakan perbandingan format antar-entitas |

### kolom-searchable@tabel-changelog · VD-T1

| Varian | Entri |
|---|---|
| `per-kelas-kolom:Text` | ✓ DU-012-1 |
| `substring-tengah` | ✓ DU-012-1 |
| `beda-kapital` | ✓ DU-012-1 |
| `tanpa-hasil` | ✓ DU-012-16 |
| `kolom-non-searchable` | ✓ DU-012-1 |
| `kolom-tersembunyi` | ✓ DU-012-1 |
| `lintas-kolom` | ✓ DU-012-5, DU-012-6 |
| `karakter-pola` | ✓ DU-012-3 |
| `query-spasi-tepi` | ✓ DU-012-1 |
| `query-spasi-tengah` | ✓ DU-012-1 |
| `kolom-icon-label` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `kolom-homogen` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `query-spasi-saja` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `query-kata-tidak-bersebelahan` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `nilai-substring-nilai-lain` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `record-tab-non-default` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `cocok-di-anak-saja` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |

### kolom-sortable@tabel-changelog · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-013-2 |
| `sama-tiebreak` | ✓ DU-013-1 |
| `kosong` | ✓ DU-013-5, DU-013-6 |
| `per-tipe-kolom:Date` | ✓ DU-013-2 |
| `per-tipe-kolom:Text` | ✓ DU-013-1 |
| `default-beda` | ✓ DU-013-3 |
| `campuran-tipe` | ✓ DU-013-4 |
| `nama-tampil-beda-nama-penuh` | ✓ DU-013-11, DU-013-12 |
| `beda-kapital` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `natural` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `aksen` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `diawali-angka-simbol` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `sisip-beda-default` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `lintas-halaman` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `sama-melintasi-halaman` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `sama-di-kolom-dan-default` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `jumlah-chip-sama` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `jumlah-aktif-sama` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `format-komposit` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `urutan-custom` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `urutan-beda-antar-kolom` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |

### field-filter@tabel-changelog · VD-T3

| Varian | Entri |
|---|---|
| `cocok` | ✓ DU-014-6 |
| `tidak-cocok` | ✓ DU-014-3 |
| `and-a-saja` | ✓ DU-014-1 |
| `and-b-saja` | ✓ DU-014-7 |
| `and-keduanya` | ✓ DU-014-6 |
| `and-tidak-keduanya` | ✓ DU-014-3 |
| `or-dalam-field` | ✓ DU-014-4, DU-014-5 |
| `search-saja` | ✓ DU-014-1 |
| `filter-saja` | ✓ DU-014-5 |
| `search-dan-filter` | ✓ DU-014-6 |
| `irisan-kosong` | ✓ DU-014-11 |
| `rentang-dalam` | ✓ DU-014-12 |
| `rentang-luar` | ✓ DU-014-13 |
| `per-kelas-kontrol:Multi-select` | ✓ DU-014-1 |
| `per-kelas-kontrol:Date range` | ✓ DU-014-12 |
| `kolom-tersembunyi` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `filter-only` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `boolean-kedua-nilai` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `rentang-tepat-awal` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `rentang-tepat-akhir` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `rentang-sehari` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `range-tepat-min` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `range-tepat-max` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `range-hanya-min` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `range-hanya-max` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `range-min-lebih-max` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `custom-field-per-tipe` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `mutasi-keluar-saringan` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `mutasi-masuk-saringan` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `create-tidak-cocok` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `status-dikecualikan` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `default-filter-lolos` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `default-filter-tersaring` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |

### opsi-filter@tabel-changelog · VD-T4

| Varian | Entri |
|---|---|
| `nilai-berulang` | ✓ DU-014-6 |
| `per-anggota-enum:Create` | ✓ DU-014-4 |
| `per-anggota-enum:Edit` | ✓ DU-014-1 |
| `per-anggota-enum:Delete` | ✓ DU-014-5 |
| `nilai-baru-saat-uji` | ✓ DU-014-8 |
| `opsi-tetap-worm` | ✓ DU-014-5 |
| `kosong` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `kolom-tanpa-null` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `master-tak-terpakai` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `enum-sebagian-terisi` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `nilai-di-cakupan-lain` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `nilai-kondisional` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `opsi-tidak-dipersempit-search` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `opsi-hilang` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `entitas-terhapus-berhistori` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `entitas-rename-berhistori` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `opsi-banyak-overflow` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `cari-opsi-substring` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `cari-opsi-beda-kapital` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `cari-opsi-tanpa-hasil` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `sumber-kosong` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `satu-nilai-distinct` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |
| `dua-nilai-distinct` | — §4.1.1 Modal Changelog: tidak ada kolom atau kontrol untuk varian ini |

### nilai-stale@filter-account-list · VD-A12

| Varian | Entri |
|---|---|
| `opsi-filter-aktif-dihapus` | ✓ DU-004-12 |
| `dep-dihapus` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `dep-diarsip` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `dep-dinonaktifkan` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `dep-non-selectable` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `dep-rename` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `single-stale` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `multi-satu-dari-n` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `multi-dua-stale` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `multi-tiga-lebih-stale` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `stale-user` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |
| `field-lain-terisi` | — §4.1.2: form tidak punya field referensi ke record lain (Account Function adalah enum tetap), jadi stale hanya terjadi pada opsi filter |

### kolom-turunan@tabel-account-list · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-170-3 |
| `kosong` | ✓ DU-170-2, DU-170-6 |
| `natural` | ✓ DU-170-5 |
| `per-tipe-kolom:Number` | ✓ DU-170-5 |
| `per-tipe-kolom:Text` | ✓ DU-170-4 |
| `sama-tiebreak` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `beda-kapital` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `aksen` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `diawali-angka-simbol` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `default-beda` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `sisip-beda-default` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `lintas-halaman` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `sama-melintasi-halaman` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `sama-di-kolom-dan-default` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `jumlah-chip-sama` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `jumlah-aktif-sama` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `campuran-tipe` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `format-komposit` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `nama-tampil-beda-nama-penuh` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `urutan-custom` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |
| `urutan-beda-antar-kolom` | — §4.1.1: varian ini milik target kolom-sortable@tabel-account-list (kolom tanpa data modul lain) |

### format-tanggal@download-account-list · VD-S1

| Varian | Entri |
|---|---|
| `nilai-diubah` | ✓ DU-157-13 |
| `per-opsi-format-tanggal:dd MMM yy` | ✓ DU-157-13 |
| `nilai-default` | — §4.1.1: nilai bawaan `dd/MM/yy` dan `24h` sudah dicakup target format-tanggal@tabel-account-list; target ini mengasersi format non-bawaan |
| `per-nilai-setting` | — §4.1.1: hanya Date Format, Time Format, dan Time Zone General Settings yang dibaca modul |
| `record-sebelum-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `record-sesudah-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `zona-waktu-non-default` | — §4.1.1: zona waktu sudah dicakup target format-tanggal@tabel-account-list; target ini mengasersi Date Format dan Time Format |
| `format-regional-beda-entitas` | — §9.11: PRD tidak menyatakan perbandingan format antar-entitas |

### format-tanggal@hover-last-used-in-journal · VD-S1

| Varian | Entri |
|---|---|
| `nilai-diubah` | ✓ DU-075-4 |
| `per-opsi-format-tanggal:dd MMM yy` | ✓ DU-075-4 |
| `nilai-default` | — §4.1.1: nilai bawaan `dd/MM/yy` dan `24h` sudah dicakup target format-tanggal@tabel-account-list; target ini mengasersi format non-bawaan |
| `per-nilai-setting` | — §4.1.1: hanya Date Format, Time Format, dan Time Zone General Settings yang dibaca modul |
| `record-sebelum-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `record-sesudah-perubahan` | — §4.1.1: format berlaku pada tampilan, tanpa pembedaan record lama dan baru |
| `zona-waktu-non-default` | — §4.1.1: zona waktu sudah dicakup target format-tanggal@tabel-account-list; target ini mengasersi Date Format dan Time Format |
| `format-regional-beda-entitas` | — §9.11: PRD tidak menyatakan perbandingan format antar-entitas |

### kolom-used-by@tabel-account-list · VD-T2

| Varian | Entri |
|---|---|
| `berbeda` | ✓ DU-071-1, DU-071-3, DU-071-4 |
| `natural` | ✓ DU-071-2 |
| `per-tipe-kolom:Number` | ✓ DU-071-2 |
| `default-beda` | ✓ DU-071-1 |
| `sama-tiebreak` | — §4.1.1#r5: spec ini mengasersi nilai Used By berbeda; urutan nilai sama dimiliki be-e2e (§5#b5, §9.5#r1) |
| `kosong` | — §4.1.1#r5: kolom Used By «Tidak pernah kosong» |
| `beda-kapital` | — §4.1.1#r5: Used By adalah kolom Number, tanpa huruf |
| `aksen` | — §4.1.1#r5: Used By adalah kolom Number, tanpa huruf |
| `diawali-angka-simbol` | — §4.1.1#r5: Used By adalah kolom Number, tanpa teks |
| `sisip-beda-default` | — §4.1.1#r5: Used By bukan kolom default sort; varian milik target kolom-sortable@tabel-account-list |
| `lintas-halaman` | — §4.1.1#r5: varian ini milik target kolom-sortable@tabel-account-list |
| `sama-melintasi-halaman` | — §4.1.1#r5: varian ini milik target kolom-sortable@tabel-account-list |
| `sama-di-kolom-dan-default` | — §4.1.1#r5: kolom default Account Code unik per company |
| `jumlah-chip-sama` | — §4.1.1: tidak ada kolom multi-nilai |
| `jumlah-aktif-sama` | — §4.1.1: tidak ada kolom multi-nilai |
| `campuran-tipe` | — §4.1.1: kolom campuran tipe hanya ada di Changelog |
| `format-komposit` | — §4.1.1: tidak ada kolom ukuran atau alamat |
| `nama-tampil-beda-nama-penuh` | — §4.1.1: basis nama penuh dinyatakan untuk Modified By Changelog, bukan Account List |
| `urutan-custom` | — §4.1.1#r5: Used By «Numeric», tanpa urutan lifecycle |
| `urutan-beda-antar-kolom` | — §4.1.1#r5: varian ini milik target kolom-sortable@tabel-account-list |

## Entri

- **DU-001-1** Account (awal), Akun Active ber-function Asset Cost tanpa entri Changelog: Account Code `A1-{runId}` (10 kar), Account Name `Fixed Assets – Equipment {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber PRD §4.1.1 Example Data
- **DU-001-2** Account (awal), Akun Inactive dengan Account Name sama seperti DU-001-1: Account Code `A2-{runId}` (10 kar), Account Name `Fixed Assets – Equipment {runId}` (32 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar) · sumber §4.1.1#r3
- **DU-001-3** Account (awal; dimutasi TC-FA-FACO-E2E-001-tabel-account-list-tampilan), Akun Active yang Account Name-nya diubah lalu diedit tanpa perubahan: Account Code `A3-{runId}` (10 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Account Name sesudah Edit `Depreciation Expense – Admin Pusat {runId}` (42 kar) · sumber PRD §4.1.1 Example Data
- **DU-001-4** Account (awal), Akun dengan Account Name tersimpan ber-markup: Account Code `A4-{runId}` (10 kar), Account Name `<b>Finance</b> {runId}` (22 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber EB-FRM-6@form-add-account
- **DU-001-5** User (awal), Admin B, aktor lain pemicu Save tanpa perubahan: Nama `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-002-1** Account (awal), Akun ber-nama Procurement tanpa entri Changelog, untuk substring, kapital, spasi, kolom hide, dan Modified By System: Account Code `S1-{runId}` (10 kar), Account Name `Procurement Cabang {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-002-2** Account (awal), Akun yang nilai tanggalnya dicari lewat Search: Account Code `S2-{runId}` (10 kar), Account Name `Biaya Pemeliharaan {runId}` (26 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber §5#b3
- **DU-002-3** Account (awal), Akun yang cocok di Account Code: Account Code `LK9-{runId}` (11 kar), Account Name `Akun Utama {runId}` (18 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar) · sumber EB-SRC-2@tabel-account-list
- **DU-002-4** Account (awal), Akun yang cocok di Account Name: Account Code `S4-{runId}` (10 kar), Account Name `Akun LK9-{runId}` (16 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar) · sumber EB-SRC-2@tabel-account-list
- **DU-002-5** Account (awal), Akun untuk query kata tidak bersebelahan: Account Code `S5-{runId}` (10 kar), Account Name `Head Office Room {runId}` (24 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-6** Account (awal), Akun bernilai Active Reserve: Account Code `S6-{runId}` (10 kar), Account Name `Active Reserve {runId}` (22 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-002-7** Account (awal), Akun bernilai Inactive Reserve: Account Code `S7-{runId}` (10 kar), Account Name `Inactive Reserve {runId}` (24 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-002-8** Account (awal), Akun ber-karakter persen: Account Code `S8-{runId}` (10 kar), Account Name `Biaya 10% {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-9** Account (awal), Pengecoh karakter persen: Account Code `S9-{runId}` (10 kar), Account Name `Biaya 100 {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-10** Account (awal), Akun ber-karakter garis bawah: Account Code `S10-{runId}` (11 kar), Account Name `Kas_Kecil {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-11** Account (awal), Pengecoh karakter garis bawah: Account Code `S11-{runId}` (11 kar), Account Name `KasXKecil {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-12** Account (awal), Akun ber-karakter titik bintang: Account Code `S12-{runId}` (11 kar), Account Name `Akun.*Lain {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-13** Account (awal), Pengecoh karakter titik bintang: Account Code `S13-{runId}` (11 kar), Account Name `Akun Lain {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-14** Search (dicoba), Payload skrip di kotak Search: Kata kunci Search `<script>alert(1)</script> {runId}` (33 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-15** Search (dicoba), Payload SQL di kotak Search: Kata kunci Search `' OR '1'='1 {runId}` (19 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-16** Search (dicoba), Payload NoSQL di kotak Search: Kata kunci Search `{"$ne": null} {runId}` (21 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-17** Search (dicoba), Kata kunci tanpa kecocokan: Kata kunci Search `tidakada-{runId}` (16 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-18** Search (dicoba), Query hanya berisi spasi: Kata kunci Search `   ` (3 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-19** Search (dicoba), Kata kunci huruf besar untuk nama Procurement: Kata kunci Search `PROCUREMENT Cabang {runId}` (26 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-20** Search (dicoba), Kata kunci kata tidak bersebelahan: Kata kunci Search `Head Room {runId}` (17 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-21** Search (dicoba), Kata kunci substring di tengah nama: Kata kunci Search `curement Cabang {runId}` (23 kar) · sumber EB-SRC-3@tabel-account-list
- **DU-002-22** Account (awal), Akun Inactive yang teks kolomnya tidak memuat inactive: Account Code `S14-{runId}` (11 kar), Account Name `Biaya Perawatan Mesin {runId}` (29 kar), Account Function `Depreciation Expense` (20 kar), Status `Inactive` (8 kar) · sumber §5#b3
- **DU-002-23** Entitas (awal), Entitas khusus untuk hasil Search atas seluruh daftar akun: Nama `Entitas Uji Search {runId}` (26 kar) · sumber turunan penulis
- **DU-002-24** Search (dicoba), Kata kunci nilai switch Status Inactive: Kata kunci Search `Inactive` (8 kar) · sumber §5#b3
- **DU-002-25** Search (dicoba), Kata kunci System untuk kolom Modified By akun tanpa entri Changelog: Kata kunci Search `System` (6 kar) · sumber §4.1.1#r7
- **DU-003-1** Account (awal), Akun Élan untuk uji sort: Account Code `K5-{runId}` (10 kar), Account Name `Élan SRT {runId}` (16 kar), Account Function `Loss on Disposal` (16 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-003-2** Account (awal), Akun anggur untuk uji sort: Account Code `K3-{runId}` (10 kar), Account Name `anggur SRT {runId}` (18 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-3** Account (awal), Akun 3D Printer untuk uji sort: Account Code `K9-{runId}` (10 kar), Account Name `3D Printer SRT {runId}` (22 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-4** Account (awal), Akun Melati untuk uji sort: Account Code `K1-{runId}` (10 kar), Account Name `Melati SRT {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-5** Account (awal; dimutasi TC-FA-FACO-E2E-003-sort-account-list), Akun Ezra untuk uji sort: Account Code `K7-{runId}` (10 kar), Account Name `Ezra SRT {runId}` (16 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar), Account Name sesudah diubah Sinta Wiratna `Ezra Baru SRT {runId}` (21 kar) · sumber turunan penulis
- **DU-003-6** Account (awal; dimutasi TC-FA-FACO-E2E-003-sort-account-list), Akun Zaitun untuk uji sort: Account Code `K2-{runId}` (10 kar), Account Name `Zaitun SRT {runId}` (18 kar), Account Function `Depreciation Expense` (20 kar), Status `Inactive` (8 kar), Account Name sesudah diubah Sinta Wirawan `Zaitun Baru SRT {runId}` (23 kar) · sumber turunan penulis
- **DU-003-7** Account (awal), Akun #Gudang untuk uji sort: Account Code `K8-{runId}` (10 kar), Account Name `#Gudang SRT {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-003-8** Account (awal; dimutasi TC-FA-FACO-E2E-003-sort-account-list), Akun Apel untuk uji sort: Account Code `K4-{runId}` (10 kar), Account Name `Apel SRT {runId}` (16 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Account Name sesudah diubah Admin B `Apel Baru SRT {runId}` (21 kar) · sumber turunan penulis
- **DU-003-9** Account (awal), Akun Elan untuk uji sort: Account Code `K6-{runId}` (10 kar), Account Name `Elan SRT {runId}` (16 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-10** Account (awal), Akun Melati untuk uji sort: Account Code `KA-{runId}` (10 kar), Account Name `Melati SRT {runId}` (18 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-11** Account (awal; 12 record), 12 akun volume untuk uji sort lintas halaman: Account Code `V{n}-{runId}` (12 kar), Account Name `Kas {n} Volume {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-003-12** Search (dicoba), Kata kunci penyempit baris uji sort: Kata kunci Search `SRT {runId}` (11 kar) · sumber turunan penulis
- **DU-003-13** Search (dicoba), Kata kunci penyempit 12 baris volume: Kata kunci Search `Volume {runId}` (14 kar) · sumber turunan penulis
- **DU-003-14** User (awal), Admin B yang mengubah satu akun sehingga Modified By berbeda dari System: Nama `Rani Pratama` (12 kar), Nama tampil di kolom Modified By `Rani P` (6 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-003-15** User (awal), Sinta Wiratna, aktor lain pemicu dengan nama tampil sama: Nama `Sinta Wiratna` (13 kar), Nama tampil di kolom Modified By `Sinta W` (7 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-003-16** User (awal), Sinta Wirawan, aktor lain pemicu dengan nama tampil sama: Nama `Sinta Wirawan` (13 kar), Nama tampil di kolom Modified By `Sinta W` (7 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-004-1** Account (awal), Akun yang cocok dengan Search dan Filter: Account Code `F1-{runId}` (10 kar), Account Name `Alfa Mitra FLT {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-004-2** Account (awal), Akun yang hanya cocok dengan Function dan Filter: Account Code `F2-{runId}` (10 kar), Account Name `Beta FLT {runId}` (16 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-004-3** Account (awal), Akun yang hanya cocok dengan Status dan Search: Account Code `F3-{runId}` (10 kar), Account Name `Gamma Mitra FLT {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-004-4** Account (awal), Akun yang tidak cocok dengan Function maupun Status: Account Code `F4-{runId}` (10 kar), Account Name `Delta FLT {runId}` (17 kar), Account Function `Depreciation Expense` (20 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-004-5** Account (awal), Akun untuk OR dalam satu field dan irisan kosong: Account Code `F5-{runId}` (10 kar), Account Name `Epsilon FLT {runId}` (19 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-004-6** Account (awal; dimutasi TC-FA-FACO-E2E-004-filter-account-list), Akun yang diubah sehingga keluar dari Filter: Account Code `F6-{runId}` (10 kar), Account Name `Zeta FLT {runId}` (16 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Function sesudah Edit `Gain on Disposal` (16 kar) · sumber turunan penulis
- **DU-004-7** Account (awal; dimutasi TC-FA-FACO-E2E-004-filter-account-list), Akun yang diubah Admin B sehingga masuk ke Filter: Account Code `F7-{runId}` (10 kar), Account Name `Eta FLT {runId}` (15 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Account Function sesudah diubah Admin B `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-004-8** User (awal), Admin B, aktor lain pemicu perubahan: Nama `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-004-9** Search (dicoba), Kata kunci penyempit seluruh akun uji: Kata kunci Search `FLT {runId}` (11 kar) · sumber turunan penulis
- **DU-004-10** Search (dicoba), Kata kunci untuk akun bernama Mitra: Kata kunci Search `Mitra FLT {runId}` (17 kar) · sumber turunan penulis
- **DU-004-11** Entitas (awal), Entitas khusus untuk opsi filter dan nilai stale atas seluruh daftar akun: Nama `Entitas Uji Filter {runId}` (26 kar) · sumber turunan penulis
- **DU-004-12** Account (awal; dimutasi TC-FA-FACO-E2E-004-filter-account-list), Akun terakhir pembawa Function Disposal Proceeds, dihapus Admin B sesudah menjadi kriteria filter aktif: Account Code `F8-{runId}` (10 kar), Account Name `Hasil Pelepasan {runId}` (23 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar) · sumber EB-FLT-7
- **DU-005-1** Entitas (awal), Entitas khusus untuk keadaan seluruh daftar: Nama `Entitas Uji Daftar {runId}` (26 kar) · sumber turunan penulis
- **DU-005-2** Account (awal; 18 record), 18 akun volume ber-Function sama: Account Code `P{n}-{runId}` (12 kar), Account Name `Kas Pusat {n} {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-005-3** Account (awal; dimutasi TC-FA-FACO-E2E-005-seluruh-daftar-paginasi-select-all), Akun Inactive ber-Function Accumulated Depreciation: Account Code `PA-{runId}` (10 kar), Account Name `Penyusutan Gedung {runId}` (25 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar) · sumber §9.5#r11
- **DU-005-4** Account (awal), Akun ber-Function Depreciation Expense: Account Code `PB-{runId}` (10 kar), Account Name `Beban Penyusutan Kantor {runId}` (31 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-005-5** Account (awal; dimutasi TC-FA-FACO-E2E-005-seluruh-daftar-paginasi-select-all), Satu-satunya akun ber-Function Disposal Proceeds: Account Code `PC-{runId}` (10 kar), Account Name `Hasil Pelepasan Aset {runId}` (28 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-005-6** Account (dibuat; dimutasi TC-FA-FACO-E2E-005-seluruh-daftar-paginasi-select-all), Akun baru yang membawa Function belum ada di tabel: Account Code `PZ-{runId}` (10 kar), Account Name `Laba Pelepasan Aset {runId}` (27 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-006-1** Entitas (awal), Entitas khusus tanpa akun bawaan: Nama `Entitas Uji Kosong {runId}` (26 kar) · sumber turunan penulis
- **DU-006-2** Account (awal; dimutasi TC-FA-FACO-E2E-006-daftar-kosong-hapus-akun-terakhir), Satu-satunya akun di entitas khusus: Account Code `E1-{runId}` (10 kar), Account Name `Akun Terakhir {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-007-1** Account (awal; dimutasi TC-FA-FACO-E2E-007-setup-column-tersimpan), Akun untuk uji kolom di-hide dan entri Changelog-nya: Account Code `X1-{runId}` (10 kar), Account Name `Kolom Uji {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Kolom Uji B {runId}` (19 kar) · sumber turunan penulis
- **DU-007-2** User (awal), Admin B, aktor lain untuk memeriksa konfigurasi kolom per pengguna: Nama `Admin B {runId}` (15 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-008-1** Account (awal; 9 record; dimutasi TC-FA-FACO-E2E-008-download-berkas), 9 akun Asset Cost untuk cakupan berkas Download: Account Code `DL{n}-{runId}` (13 kar), Account Name `0{n} Unduh {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `01 Unduh {runId} Ubah` (21 kar) · sumber turunan penulis
- **DU-008-2** Account (awal; dimutasi TC-FA-FACO-E2E-008-download-berkas), Akun Depreciation Expense untuk Filter dan urutan berkas: Account Code `DL10-{runId}` (12 kar), Account Name `10 Unduh {runId}` (16 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-008-3** Account (awal; dimutasi TC-FA-FACO-E2E-008-download-berkas), Akun Depreciation Expense untuk Filter dan urutan berkas: Account Code `DL11-{runId}` (12 kar), Account Name `11 Unduh {runId}` (16 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-008-4** Account (awal; dimutasi TC-FA-FACO-E2E-008-download-berkas), Akun Depreciation Expense untuk Filter dan urutan berkas: Account Code `DL12-{runId}` (12 kar), Account Name `12 Unduh {runId}` (16 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-008-5** Search (dicoba), Kata kunci Search yang hanya mencocokkan baris milik spec ini: Kata kunci Search `Unduh {runId}` (13 kar) · sumber turunan penulis
- **DU-008-6** Search (dicoba), Kata kunci Search yang hanya mencocokkan akun Asset Cost DL1, sehingga bersama Filter Function Depreciation Expense menghasilkan nol baris: Kata kunci Search `01 Unduh {runId}` (16 kar) · sumber turunan penulis
- **DU-009-1** Account (awal), Akun Active yang belum pernah diekspor: Account Code `IB1-{runId}` (11 kar), Account Name `Satu Isi {runId}` (16 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Last Used in Journal `kosong` (6 kar) · sumber turunan penulis
- **DU-009-2** Account (awal), Akun Inactive dengan Last Used in Journal kosong: Account Code `IB2-{runId}` (11 kar), Account Name `Dua Isi {runId}` (15 kar), Account Function `Depreciation Expense` (20 kar), Status `Inactive` (8 kar), Last Used in Journal `kosong` (6 kar) · sumber turunan penulis
- **DU-009-3** Search (dicoba), Kata kunci Search yang hanya mencocokkan baris milik spec ini: Kata kunci Search `Isi {runId}` (11 kar) · sumber turunan penulis
- **DU-009-4** Search (dicoba), Kata kunci Search tanpa kecocokan: Kata kunci Search `tidakada-{runId}` (16 kar) · sumber turunan penulis
- **DU-010-1** Account (dibuat; dimutasi TC-FA-FACO-E2E-010-changelog-tampilan), Akun dibuat lewat form lalu di-Edit dua field dan dinonaktifkan untuk menghasilkan entri Changelog: Account Code `CL1-{runId}` (11 kar), Account Name `Entri Awal {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Entri Ubah {runId}` (18 kar), Account Function sesudah Edit `Gain on Disposal` (16 kar), Status sesudah Deactivate `Inactive` (8 kar) · sumber turunan penulis
- **DU-010-2** Account (awal; dimutasi TC-FA-FACO-E2E-010-changelog-tampilan), Akun yang dihapus untuk menghasilkan entri Delete: Account Code `CL2-{runId}` (11 kar), Account Name `Entri Hapus {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-011-1** Account (awal; dimutasi TC-FA-FACO-E2E-011-changelog-entri-edit), Akun yang di-Edit dua kali beruntun: Account Code `LG1-{runId}` (11 kar), Account Name `Nama Satu {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Code sesudah Edit pertama `LG1B-{runId}` (12 kar), Account Name sesudah Edit pertama `Nama Dua {runId}` (16 kar), Account Function sesudah Edit pertama `Gain on Disposal` (16 kar), Account Name sesudah Edit kedua `Nama Tiga {runId}` (17 kar) · sumber turunan penulis
- **DU-011-2** Account (awal; dimutasi TC-FA-FACO-E2E-011-changelog-entri-edit), Akun pembanding yang tidak diubah sampai kelompok langkah terakhir, lalu entri Account Name ditulis sebelum Account Code berubah: Account Code `LG2-{runId}` (11 kar), Account Name `Akun Pembanding {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit pertama `Pembanding Satu {runId}` (23 kar), Account Code sesudah Edit kedua `LG2B-{runId}` (12 kar) · sumber §8.1#p3
- **DU-012-1** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun yang entri Changelog-nya dicari di kolom teks: Account Code `CS1-{runId}` (11 kar), Account Name `Procurement Cabang {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Procurement Cabang Baru {runId}` (31 kar) · sumber turunan penulis
- **DU-012-2** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun untuk kata kunci bertanda spasi di tengah: Account Code `CS2-{runId}` (11 kar), Account Name `Head Office Room {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Ruang Kantor {runId}` (20 kar) · sumber turunan penulis
- **DU-012-3** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun bernama memuat karakter pola %: Account Code `CS3-{runId}` (11 kar), Account Name `Biaya 10% {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Biaya Pokok {runId}` (19 kar) · sumber turunan penulis
- **DU-012-4** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Pembanding untuk karakter pola %: Account Code `CS4-{runId}` (11 kar), Account Name `Biaya 100 {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Biaya Lain {runId}` (18 kar) · sumber turunan penulis
- **DU-012-5** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun yang Old Value entrinya memuat Account Code akun lain: Account Code `CS5-{runId}` (11 kar), Account Name `Salin CS6-{runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Salin Akhir {runId}` (19 kar) · sumber turunan penulis
- **DU-012-6** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun yang Account Code-nya cocok dengan Old Value entri lain: Account Code `CS6-{runId}` (11 kar), Account Name `Akun Enam {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Akun Enam B {runId}` (19 kar) · sumber turunan penulis
- **DU-012-7** Account (awal; dimutasi TC-FA-FACO-E2E-012-changelog-search), Akun yang dihapus untuk entri Action Delete: Account Code `CS7-{runId}` (11 kar), Account Name `Akun Hapus {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-012-8** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `curement Cabang {runId}` (23 kar) · sumber turunan penulis
- **DU-012-9** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `PROCUREMENT Cabang {runId}` (26 kar) · sumber turunan penulis
- **DU-012-10** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search ` Procurement Cabang {runId} ` (28 kar) · sumber turunan penulis
- **DU-012-11** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `Procurement  Cabang {runId}` (27 kar) · sumber turunan penulis
- **DU-012-12** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `Head Room {runId}` (17 kar) · sumber turunan penulis
- **DU-012-13** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `<script>alert(1)</script> {runId}` (33 kar) · sumber turunan penulis
- **DU-012-14** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `Account Name` (12 kar) · sumber turunan penulis
- **DU-012-15** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `Delete` (6 kar) · sumber turunan penulis
- **DU-012-16** Search (dicoba), Kata kunci Search modal Changelog: Kata kunci Search `tidakada-{runId}` (16 kar) · sumber turunan penulis
- **DU-013-1** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E1, bernilai sama dengan E9 pada Old Value: Account Code `QS-{runId}-c` (12 kar), Account Name `Melati` (6 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Mawar` (5 kar) · sumber turunan penulis
- **DU-013-2** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E2, huruf kecil di awal nilai: Account Code `QS-{runId}-a` (12 kar), Account Name `anggur` (6 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `zebra` (5 kar) · sumber turunan penulis
- **DU-013-3** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E3: Account Code `QS-{runId}-h` (12 kar), Account Name `Apel` (4 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Bambu` (5 kar) · sumber turunan penulis
- **DU-013-4** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E4 dengan Old Value angka: Account Code `QS-{runId}-B` (12 kar), Account Name `500` (3 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `90` (2 kar) · sumber turunan penulis
- **DU-013-5** Account (dibuat; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri Create, Old Value kosong: Account Code `QS-{runId}-e` (12 kar), Account Name `Akun Baru Urut {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-013-6** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri Delete, New Value kosong: Account Code `QS-{runId}-j` (12 kar), Account Name `Akun Hapus Urut {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-013-7** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri Field Account Function: Account Code `QS-{runId}-D` (12 kar), Account Name `Akun Fungsi Urut {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Function sesudah Edit `Gain on Disposal` (16 kar) · sumber turunan penulis
- **DU-013-8** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri Field Status: Account Code `QS-{runId}-f` (12 kar), Account Name `Akun Status Urut {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Status sesudah Deactivate `Inactive` (8 kar) · sumber turunan penulis
- **DU-013-9** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E9 oleh Admin B: Account Code `QS-{runId}-i` (12 kar), Account Name `Melati` (6 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Mawar` (5 kar) · sumber turunan penulis
- **DU-013-10** Account (awal; dimutasi TC-FA-FACO-E2E-013-changelog-sort), Entri E10 oleh Admin C: Account Code `QS-{runId}-g` (12 kar), Account Name `70` (2 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `400` (3 kar) · sumber turunan penulis
- **DU-013-11** User (awal), Admin B untuk Modified By: Nama `Lina Adi` (8 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-013-12** User (awal), Admin C untuk Modified By: Nama `Lina Agus` (9 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-013-13** Search (dicoba), Kata kunci Search yang hanya mencocokkan kesepuluh entri milik spec ini lewat Account Code: Kata kunci Search `QS-{runId}` (10 kar) · sumber turunan penulis
- **DU-014-1** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Edit Account Name oleh aktor M: Account Code `FC-{runId}-a` (12 kar), Account Name `Filter Awal A {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Filter Akhir A {runId}` (22 kar) · sumber turunan penulis
- **DU-014-2** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Edit Account Name oleh aktor M: Account Code `FC-{runId}-b` (12 kar), Account Name `Filter Awal B {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Filter Akhir B {runId}` (22 kar), Account Function sesudah diubah Admin B `Loss on Disposal` (16 kar) · sumber turunan penulis
- **DU-014-3** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Edit Account Function oleh aktor M: Account Code `FC-{runId}-c` (12 kar), Account Name `Filter Fungsi C {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Function sesudah Edit `Gain on Disposal` (16 kar) · sumber turunan penulis
- **DU-014-4** Account (dibuat; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Create: Account Code `FC-{runId}-d` (12 kar), Account Name `Filter Buat D {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-014-5** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Delete, opsi Account Code tetap sesudah akun dihapus: Account Code `FC-{runId}-e` (12 kar), Account Name `Filter Hapus E {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-014-6** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Edit Account Name oleh Admin B: Account Code `FC-{runId}-f` (12 kar), Account Name `Filter Awal F {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Filter Akhir F {runId}` (22 kar) · sumber turunan penulis
- **DU-014-7** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Entri Edit Account Function oleh Admin B: Account Code `FC-{runId}-i` (12 kar), Account Name `Filter Fungsi I {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Function sesudah Edit `Gain on Disposal` (16 kar) · sumber turunan penulis
- **DU-014-8** Account (awal; dimutasi TC-FA-FACO-E2E-014-changelog-filter), Akun yang entrinya muncul sesudah modal pernah dibuka: Account Code `FC-{runId}-j` (12 kar), Account Name `Filter Baru J {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name sesudah Edit `Filter Baru Akhir J {runId}` (27 kar) · sumber turunan penulis
- **DU-014-9** User (awal), Admin B untuk Modified By: Nama `Rani Pratama` (12 kar), Nama depan `Rani` (4 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber matriks role PRD
- **DU-014-10** Search (dicoba), Kata kunci Search modal Changelog yang hanya mencocokkan entri milik spec ini lewat Account Code: Kata kunci Search `FC-{runId}` (10 kar) · sumber turunan penulis
- **DU-014-11** Search (dicoba), Kata kunci Search untuk satu entri: Kata kunci Search `FC-{runId}-a` (12 kar) · sumber turunan penulis
- **DU-014-12** Filter (dicoba), Rentang Date satu hari pada hari run: Rentang Date `T0 sampai T0` (12 kar) · sumber turunan penulis
- **DU-014-13** Filter (dicoba), Rentang Date sesudah hari run: Rentang Date `T0 + 1 hari sampai T0 + 7 hari` (30 kar) · sumber turunan penulis
- **DU-016-1** User (awal; dimutasi TC-FA-FACO-E2E-016-guided-tooltip-flag), Pengguna pertama: flag disetel lewat Skip, lalu diperiksa sesudah muat ulang dan di browser lain: Nama `Pengguna Tur A {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag tur `belum disetel` (13 kar) · sumber foundation guided-tooltip §16.1
- **DU-016-2** User (awal; dimutasi TC-FA-FACO-E2E-016-guided-tooltip-flag), Pengguna kedua: tur dilihat tanpa selesai, lalu diselesaikan lewat Done: Nama `Pengguna Tur B {runId}` (22 kar), Role `Total Control` (13 kar), Cakupan `seluruh client` (14 kar), Flag tur `belum disetel` (13 kar) · sumber foundation guided-tooltip §16.1
- **DU-017-1** Account (awal; 9 record), 9 akun Asset Cost untuk keadaan tabel: Account Code `LS{n}-{runId}` (13 kar), Account Name `0{n} Keadaan {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-017-2** Account (awal), Akun Asset Cost ke-10: Account Code `LS10-{runId}` (12 kar), Account Name `10 Keadaan {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-017-3** Account (awal), Akun Asset Cost ke-11: Account Code `LS11-{runId}` (12 kar), Account Name `11 Keadaan {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-017-4** Account (awal), Akun Asset Cost ke-12: Account Code `LS12-{runId}` (12 kar), Account Name `12 Keadaan {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-017-5** Account (awal), Akun yang tersaring keluar oleh Filter Function Asset Cost: Account Code `LS13-{runId}` (12 kar), Account Name `13 Keadaan {runId}` (18 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-017-6** Search (dicoba), Kata kunci Search yang hanya mencocokkan akun milik spec ini: Kata kunci Search `Keadaan {runId}` (15 kar) · sumber turunan penulis
- **DU-018-1** Account (awal), Akun yang form Edit-nya dibuka dan diubah tanpa disimpan: Account Code `FM1-{runId}` (11 kar), Account Name `Form Awal {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Account Name yang diketik tanpa disimpan `Form Ubah {runId}` (17 kar) · sumber turunan penulis
- **DU-018-2** Input (dicoba), Isian form Add Account yang tidak disimpan: Account Code `FM2-{runId}` (11 kar), Account Name `Form Kotor {runId}` (18 kar) · sumber turunan penulis
- **DU-020-1** Account (awal), Akun Active yang sudah ada: pembanding urutan dan sasaran Account Code duplikat: Account Code `1-1001-{runId}` (14 kar), Account Name `Fixed Assets Equipment {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-020-2** Account (dibuat), Input valid lengkap untuk Create dari toolbar, Account Name berspasi di tepi: Account Code `5-6001-{runId}` (14 kar), Account Name `  Depreciation Expense Admin {runId}  ` (38 kar), Account Function `Depreciation Expense` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-020-3** Account (dibuat), Akun kedua dengan Account Name yang sama seperti akun lain: Account Code `5-6002-{runId}` (14 kar), Account Name `Depreciation Expense Admin {runId}` (34 kar), Account Function `Depreciation Expense` (20 kar) · sumber §9.4.2#r37
- **DU-020-4** Account (dicoba), Account Code yang sudah dipakai DU-020-1: Account Code `1-1001-{runId}` (14 kar), Account Name `Fixed Assets Duplicate Code {runId}` (35 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-020-5** Account (awal; 26 record), Dua puluh enam akun Active yang mendahului Account Code akun baru pada urutan A-Z, lebih banyak daripada ukuran halaman 25: Account Code `1-3{n}-{runId}` (14 kar), Account Name `Cadangan Penyusutan Aset Tetap {n} {runId}` (42 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-022-1** Account (awal; dimutasi TC-FA-FACO-E2E-022-edit-account), Akun Active yang belum pernah diekspor, sasaran Edit Account Name dan Account Function: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense Admin {runId}` (34 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-022-2** Account (awal; dimutasi TC-FA-FACO-E2E-022-edit-account), Akun Active kedua: sasaran percobaan Account Code duplikat dan Account Name yang sama: Account Code `5-6002-{runId}` (14 kar), Account Name `Depreciation Expense Warehouse {runId}` (38 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-022-3** Account (dibuat), Nilai baru hasil Edit atas DU-022-1: Account Name `Depreciation Expense Admin Office {runId}` (41 kar), Account Function `Capitalization Offset` (21 kar) · sumber turunan penulis
- **DU-022-4** Account (dicoba), Account Code milik DU-022-1 yang dicoba dipakai DU-022-2: Account Code `5-6001-{runId}` (14 kar) · sumber V-04
- **DU-023-1** Account (awal), Akun Active yang dibuka di Edit lalu disimpan tanpa perubahan: Account Code `5-6003-{runId}` (14 kar), Account Name `Depreciation Expense Workshop {runId}` (37 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-024-1** Account (awal; dimutasi TC-FA-FACO-E2E-024-deactivate-single), Akun Active, Used By 0, belum pernah diekspor: lolos guard Deactivate: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense Admin {runId}` (34 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `5-6001-{runId} – Depreciation Expense Admin {runId}` (51 kar) · sumber PRD §4.1.1 Example Data
- **DU-025-1** Account (awal; dimutasi TC-FA-FACO-E2E-025-activate-single), Akun Inactive, tidak dipakai, belum pernah diekspor: dapat diaktifkan kembali: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `4-7001-{runId} – Gain on Disposal {runId}` (41 kar) · sumber PRD §4.1.1 Example Data
- **DU-026-1** Account (awal; dimutasi TC-FA-FACO-E2E-026-bulk-deactivate), Satu akun Active untuk Bulk Deactivate dengan seleksi satu akun: Account Code `GD-{runId}` (10 kar), Account Name `Gain on Disposal Kantor Pusat {runId}` (37 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `GD-{runId} – Gain on Disposal Kantor Pusat {runId}` (50 kar) · sumber turunan penulis
- **DU-026-2** Account (awal; dimutasi TC-FA-FACO-E2E-026-bulk-deactivate), Akun Active pertama dari tiga akun Bulk Deactivate: Account Code `LD1-{runId}` (11 kar), Account Name `Loss on Disposal Equipment {runId}` (34 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `LD1-{runId} – Loss on Disposal Equipment {runId}` (48 kar) · sumber turunan penulis
- **DU-026-3** Account (awal; dimutasi TC-FA-FACO-E2E-026-bulk-deactivate), Akun Active kedua dari tiga akun Bulk Deactivate: Account Code `LD2-{runId}` (11 kar), Account Name `Loss on Disposal Vehicles {runId}` (33 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `LD2-{runId} – Loss on Disposal Vehicles {runId}` (47 kar) · sumber turunan penulis
- **DU-026-4** Account (awal; dimutasi TC-FA-FACO-E2E-026-bulk-deactivate), Akun Active ketiga dari tiga akun Bulk Deactivate: Account Code `LD3-{runId}` (11 kar), Account Name `Loss on Disposal Buildings {runId}` (34 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `LD3-{runId} – Loss on Disposal Buildings {runId}` (48 kar) · sumber turunan penulis
- **DU-026-5** Account (awal), Akun Inactive yang ikut terpilih: sudah berstatus tujuan, tidak diproses: Account Code `LD4-{runId}` (11 kar), Account Name `Loss on Disposal Furniture {runId}` (34 kar), Account Function `Loss on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `LD4-{runId} – Loss on Disposal Furniture {runId}` (48 kar) · sumber turunan penulis
- **DU-026-6** Account (awal; 12 record; dimutasi TC-FA-FACO-E2E-026-bulk-deactivate), Dua belas akun Active bernama panjang sehingga daftar dialog bergulir: Account Code `DP{n}-{runId}` (13 kar), Account Name `Disposal Proceeds Clearing Cabang Pusat Distribusi Nasional Wilayah Jawa Barat Unit {n} {runId}` (95 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-027-1** Account (awal; dimutasi TC-FA-FACO-E2E-027-bulk-activate), Akun Inactive pertama yang valid diaktifkan: Account Code `RA1-{runId}` (11 kar), Account Name `Reaktivasi Peralatan Kantor {runId}` (35 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `RA1-{runId} – Reaktivasi Peralatan Kantor {runId}` (49 kar) · sumber turunan penulis
- **DU-027-2** Account (awal; dimutasi TC-FA-FACO-E2E-027-bulk-activate), Akun Inactive kedua yang valid diaktifkan: Account Code `RA2-{runId}` (11 kar), Account Name `Reaktivasi Kendaraan Operasional {runId}` (40 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `RA2-{runId} – Reaktivasi Kendaraan Operasional {runId}` (54 kar) · sumber turunan penulis
- **DU-027-3** Account (awal), Akun Active yang ikut terpilih: sudah berstatus tujuan, tidak diproses: Account Code `RA3-{runId}` (11 kar), Account Name `Peralatan Gudang Aktif {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `RA3-{runId} – Peralatan Gudang Aktif {runId}` (44 kar) · sumber turunan penulis
- **DU-028-1** Account (awal; dimutasi TC-FA-FACO-E2E-028-delete-single), Akun Active tanpa pemakaian, belum pernah diekspor, bukan default company: lolos kedua guard Delete: Account Code `5-6006-{runId}` (14 kar), Account Name `Depreciation Expense Cabang {runId}` (35 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `5-6006-{runId} – Depreciation Expense Cabang {runId}` (52 kar) · sumber PRD §4.1.1 Example Data
- **DU-028-2** Account (awal), Akun lain yang tidak dihapus: bukti tidak ada efek pada data lain: Account Code `5-6007-{runId}` (14 kar), Account Name `Depreciation Expense Pusat {runId}` (34 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-029-1** Account (awal; dimutasi TC-FA-FACO-E2E-029-bulk-delete), Satu akun Active yang lolos guard untuk Bulk Delete dengan seleksi satu akun: Account Code `HS-{runId}` (10 kar), Account Name `Prepaid Equipment Kantor Cabang {runId}` (39 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `HS-{runId} – Prepaid Equipment Kantor Cabang {runId}` (52 kar) · sumber turunan penulis
- **DU-029-2** Account (awal; dimutasi TC-FA-FACO-E2E-029-bulk-delete), Akun pertama dari tiga akun Bulk Delete: Account Code `HB1-{runId}` (11 kar), Account Name `Accumulated Depreciation Gudang {runId}` (39 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `HB1-{runId} – Accumulated Depreciation Gudang {runId}` (53 kar) · sumber turunan penulis
- **DU-029-3** Account (awal; dimutasi TC-FA-FACO-E2E-029-bulk-delete), Akun kedua dari tiga akun Bulk Delete: Account Code `HB2-{runId}` (11 kar), Account Name `Accumulated Depreciation Workshop {runId}` (41 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `HB2-{runId} – Accumulated Depreciation Workshop {runId}` (55 kar) · sumber turunan penulis
- **DU-029-4** Account (awal; dimutasi TC-FA-FACO-E2E-029-bulk-delete), Akun ketiga dari tiga akun Bulk Delete: Account Code `HB3-{runId}` (11 kar), Account Name `Accumulated Depreciation Showroom {runId}` (41 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Account Label `HB3-{runId} – Accumulated Depreciation Showroom {runId}` (55 kar) · sumber turunan penulis
- **DU-029-5** Account (awal; 12 record; dimutasi TC-FA-FACO-E2E-029-bulk-delete), Dua belas akun bernama panjang sehingga daftar dialog bergulir: Account Code `HV{n}-{runId}` (13 kar), Account Name `Depreciation Expense Cabang Pusat Distribusi Nasional Wilayah Jawa Barat Unit {n} {runId}` (89 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-030-1** Account (awal; dimutasi TC-FA-FACO-E2E-030-akun-dihapus-pihak-lain), Akun Active yang dihapus Admin B saat modal Edit terbuka: Account Code `5-6008-{runId}` (14 kar), Account Name `Depreciation Expense Gudang Timur {runId}` (41 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-030-2** Account (awal; dimutasi TC-FA-FACO-E2E-030-akun-dihapus-pihak-lain), Akun Inactive yang dihapus Admin B saat dialog Activate terbuka: Account Code `4-7003-{runId}` (14 kar), Account Name `Gain on Disposal Cabang Timur {runId}` (37 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-030-3** Account (awal; dimutasi TC-FA-FACO-E2E-030-akun-dihapus-pihak-lain), Akun Active yang dihapus Admin B saat dialog Deactivate terbuka: Account Code `5-6009-{runId}` (14 kar), Account Name `Depreciation Expense Showroom {runId}` (37 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-030-4** Account (awal; dimutasi TC-FA-FACO-E2E-030-akun-dihapus-pihak-lain), Akun Active yang dihapus Admin B saat dialog Delete terbuka: Account Code `5-6010-{runId}` (14 kar), Account Name `Depreciation Expense Kantor Timur {runId}` (41 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-030-5** Account (dicoba), Account Name baru yang diketik di modal Edit lalu tidak tersimpan: Account Name `Depreciation Expense Gudang Timur Baru {runId}` (46 kar) · sumber turunan penulis
- **DU-031-1** Account (awal; dimutasi TC-FA-FACO-E2E-031-status-usang-idempotent), Akun Inactive saat tabel dimuat, lalu diaktifkan Admin B setelah aktor membuka dialog Activate dan sebelum aktor mengonfirmasinya: Account Code `4-7004-{runId}` (14 kar), Account Name `Gain on Disposal Cabang Barat {runId}` (37 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-031-2** Account (awal; dimutasi TC-FA-FACO-E2E-031-status-usang-idempotent), Akun Active saat tabel dimuat, lalu dinonaktifkan Admin B setelah aktor membuka dialog Deactivate dan sebelum aktor mengonfirmasinya: Account Code `5-6011-{runId}` (14 kar), Account Name `Depreciation Expense Cabang Barat {runId}` (41 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-038-1** User (awal), User Manage accounting dengan huruf Create dan Delete tanpa Update: Name `Siti Rahma {runId}` (18 kar), Role `Global Role Manage accounting huruf Read, Create, dan Delete (Read baseline terkunci)` (85 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-038-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-038-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-040-1** User (awal), Default User dengan access level Total Control: Name `Bagus Prasetyo {runId}` (22 kar), Role `access level Default User (Total Control permanen)` (50 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-040-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-040-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-041-1** User (awal), User dengan access level Read Only: Name `Hendra Kusuma {runId}` (21 kar), Role `access level Read Only` (22 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-041-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-041-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-042-1** User (awal), User Manage accounting hanya huruf Read: Name `Maya Lestari {runId}` (20 kar), Role `Global Role Manage accounting huruf Read saja` (45 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-042-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-042-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-043-1** User (awal), User Manage accounting dengan huruf Create saja ditambah Read: Name `Rudi Hartono {runId}` (20 kar), Role `Global Role Manage accounting huruf Read dan Create (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-043-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-043-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-043-5** Account (dibuat), Akun baru yang dibuat dari toolbar: Account Code `7-2001-{runId}` (14 kar), Account Name `Office Equipment Cost {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-044-1** User (awal), User Manage accounting dengan huruf Update saja ditambah Read: Name `Dewi Anggraini {runId}` (22 kar), Role `Global Role Manage accounting huruf Read dan Update (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-044-2** Account (awal; dimutasi TC-FA-FACO-E2E-044-gating-update), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Account Name setelah Edit `Depreciation Expense – Admin Revisi {runId}` (43 kar) · sumber PRD §4.1.1 Example Data
- **DU-044-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-044-5** Account (awal; dimutasi TC-FA-FACO-E2E-044-gating-update), Akun Inactive untuk Activate single: Account Code `4-7101-{runId}` (14 kar), Account Name `Loss on Disposal {runId}` (24 kar), Account Function `Loss on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-044-6** Account (awal; dimutasi TC-FA-FACO-E2E-044-gating-update), Akun Active untuk Deactivate single: Account Code `5-6101-{runId}` (14 kar), Account Name `Depreciation Expense – Warehouse {runId}` (40 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-044-7** Account (awal; dimutasi TC-FA-FACO-E2E-044-gating-update), Akun Inactive pertama untuk Activate lalu Deactivate bulk: Account Code `2-1101-{runId}` (14 kar), Account Name `Accumulated Depreciation – Vehicles {runId}` (43 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-044-8** Account (awal; dimutasi TC-FA-FACO-E2E-044-gating-update), Akun Inactive kedua untuk Activate lalu Deactivate bulk: Account Code `2-1102-{runId}` (14 kar), Account Name `Accumulated Depreciation – Office {runId}` (41 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-045-1** User (awal), User Manage accounting dengan huruf Delete saja ditambah Read: Name `Agus Salim {runId}` (18 kar), Role `Global Role Manage accounting huruf Read dan Delete (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-045-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-045-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-045-5** Account (awal; dimutasi TC-FA-FACO-E2E-045-gating-delete), Akun Active untuk Delete single: Account Code `6-3101-{runId}` (14 kar), Account Name `Repairs & Maintenance Expense {runId}` (37 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-045-6** Account (awal; dimutasi TC-FA-FACO-E2E-045-gating-delete), Akun Inactive pertama untuk Bulk Delete: Account Code `6-3102-{runId}` (14 kar), Account Name `Disposal Proceeds Clearing {runId}` (34 kar), Account Function `Disposal Proceeds` (17 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-045-7** Account (awal; dimutasi TC-FA-FACO-E2E-045-gating-delete), Akun Active kedua untuk Bulk Delete: Account Code `4-7201-{runId}` (14 kar), Account Name `Loss on Disposal – Vehicles {runId}` (35 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-046-1** User (awal), User Group Manager tanpa capability Manage accounting: Name `Yoga Pratama {runId}` (20 kar), Role `access level Group Manager tanpa Manage accounting` (50 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-046-2** User (awal), User role lain (bukan Group Manager) tanpa capability Manage accounting: Name `Dewi Anggraini {runId}` (22 kar), Role `role lain (bukan Group Manager) tanpa Manage accounting` (55 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-047-1** User (awal), User Manage accounting dengan huruf Update ditambah Read yang capability Update-nya dicabut saat halaman terbuka: Name `Wulan Sari {runId}` (18 kar), Role `Global Role Manage accounting huruf Read dan Update (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-047-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-048-1** Entitas (awal), Entitas Active sebagai pembanding: Name `Client Aktif {runId}` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-048-2** Entitas (awal), Entitas Suspended: Name `Client Suspended {runId}` (24 kar), Status `Suspended` (9 kar) · sumber turunan penulis
- **DU-048-3** Entitas (awal), Entitas Expired: Name `Client Expired {runId}` (22 kar), Status `Expired` (7 kar) · sumber turunan penulis
- **DU-048-4** Account (awal), Akun Active di entitas Suspended: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Entitas `Client Suspended {runId}` (24 kar) · sumber PRD §4.1.1 Example Data
- **DU-048-5** Account (awal), Akun Active di entitas Expired: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Entitas `Client Expired {runId}` (22 kar) · sumber PRD §4.1.1 Example Data
- **DU-048-6** Account (dibuat), Akun baru yang dibuat di entitas Active: Account Code `7-2001-{runId}` (14 kar), Account Name `Office Equipment Cost {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-048-7** Account (dicoba), Akun baru yang dicoba dibuat di entitas Suspended: Account Code `8-1001-{runId}` (14 kar), Account Name `Land Improvement Cost {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-048-8** Account (dicoba), Akun baru yang dicoba dibuat di entitas Expired: Account Code `8-1002-{runId}` (14 kar), Account Name `Building Improvement Cost {runId}` (33 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-048-9** Account (dicoba), Account Name baru yang dicoba disimpan di entitas Suspended: Account Name `Depreciation Expense – Admin Revisi S {runId}` (45 kar) · sumber turunan penulis
- **DU-048-10** Account (dicoba), Account Name baru yang dicoba disimpan di entitas Expired: Account Name `Depreciation Expense – Admin Revisi E {runId}` (45 kar) · sumber turunan penulis
- **DU-048-11** Account (awal), Akun Inactive di entitas Suspended: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Entitas `Client Suspended {runId}` (24 kar) · sumber PRD §4.1.1 Example Data
- **DU-048-12** Account (awal), Akun Inactive di entitas Expired: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Entitas `Client Expired {runId}` (22 kar) · sumber PRD §4.1.1 Example Data
- **DU-050-1** Entitas (awal), Entitas dengan plan Starter (level None): Name `Client Starter {runId}` (22 kar), Status `Active` (6 kar), Plan `Starter` (7 kar) · sumber turunan penulis
- **DU-050-2** Account (awal), Akun Active tanpa pemakaian di entitas Starter: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-051-1** Entitas (awal), Entitas plan Growth level Full: Name `Client Growth {runId}` (21 kar), Status `Active` (6 kar), Plan `Growth` (6 kar) · sumber turunan penulis
- **DU-051-2** Entitas (awal), Entitas plan Professional level Full: Name `Client Professional {runId}` (27 kar), Status `Active` (6 kar), Plan `Professional` (12 kar) · sumber turunan penulis
- **DU-051-3** Entitas (awal), Entitas plan Enterprise level Full: Name `Client Enterprise {runId}` (25 kar), Status `Active` (6 kar), Plan `Enterprise` (10 kar) · sumber turunan penulis
- **DU-051-4** Account (dibuat; dimutasi TC-FA-FACO-E2E-051-plan-full-crud-identik), Akun yang dibuat, diedit, dan dihapus di plan Growth: Account Code `7-3001-{runId}` (14 kar), Account Name `Machinery Cost {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Account Name setelah Edit `Machinery Cost Revisi {runId}` (29 kar) · sumber turunan penulis
- **DU-051-5** Account (dibuat; dimutasi TC-FA-FACO-E2E-051-plan-full-crud-identik), Akun yang dibuat, diedit, dan dihapus di plan Professional: Account Code `7-3002-{runId}` (14 kar), Account Name `Furniture Cost {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Account Name setelah Edit `Furniture Cost Revisi {runId}` (29 kar) · sumber turunan penulis
- **DU-051-6** Account (dibuat; dimutasi TC-FA-FACO-E2E-051-plan-full-crud-identik), Akun yang dibuat, diedit, dan dihapus di plan Enterprise: Account Code `7-3003-{runId}` (14 kar), Account Name `Vehicle Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Account Name setelah Edit `Vehicle Cost Revisi {runId}` (27 kar) · sumber turunan penulis
- **DU-097-1** User (awal), User Manage accounting huruf Read dan Update di aplikasi Android: Name `Fajar Nugroho {runId}` (21 kar), Role `Global Role Manage accounting huruf Read dan Update (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-097-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-097-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-098-1** User (awal), Default User dengan access level Total Control di aplikasi Android: Name `Bagus Prasetyo {runId}` (22 kar), Role `access level Default User (Total Control permanen)` (50 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-098-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-098-3** Account (awal), Akun Inactive tanpa pemakaian: Account Code `4-7001-{runId}` (14 kar), Account Name `Gain on Disposal {runId}` (24 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-098-4** Account (awal), Akun Active dipakai 3 Asset Class: Account Code `1-1001-{runId}` (14 kar), Account Name `Fixed Assets – Equipment {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `3` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-098-5** Account (awal; dimutasi TC-FA-FACO-E2E-098-mobile-card-list), Akun Inactive untuk bulk Activate yang menutup selection mode: Account Code `4-7301-{runId}` (14 kar), Account Name `Gain on Disposal – Vehicles {runId}` (35 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-098-6** Account (awal; 8 record), Akun Active tambahan agar hasil Search melebihi card yang dimuat per halaman: Account Code `9-80{n}-{runId}` (15 kar), Account Name `Operating Expense Cabang {n} {runId}` (36 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-099-1** User (awal), User dengan access level Read Only di aplikasi Android: Name `Hendra Kusuma {runId}` (21 kar), Role `access level Read Only` (22 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-099-2** Account (awal), Akun Active tanpa pemakaian: Account Code `5-6001-{runId}` (14 kar), Account Name `Depreciation Expense – Admin {runId}` (36 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-052-1** User (awal), User dengan access level Read Only: Name `Hendra Kusuma {runId}` (21 kar), Role `access level Read Only` (22 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-052-2** Account (awal), Akun Active dipakai 2 Asset Class, sehingga Used By bernilai 2: Account Code `ROU-{runId}` (11 kar), Account Name `Fixed Assets – Vehicles {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-052-3** Asset Class (awal), Asset Class pertama yang merujuk akun pada field Asset Cost: Name `Light Vehicles {runId}` (22 kar), Asset Cost `ROU-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-052-4** Asset Class (awal), Asset Class kedua yang merujuk akun yang sama pada field Asset Cost: Name `Heavy Vehicles {runId}` (22 kar), Asset Cost `ROU-{runId}` (11 kar) · sumber FACO-LOGIC-02h
- **DU-053-1** User (awal), User Manage accounting hanya huruf Read: Name `Maya Lestari {runId}` (20 kar), Role `Global Role Manage accounting huruf Read saja` (45 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-053-2** Account (awal), Akun Active dipakai 2 Asset Class, sehingga Used By bernilai 2: Account Code `RDU-{runId}` (11 kar), Account Name `Fixed Assets – Buildings {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-053-3** Asset Class (awal), Asset Class pertama yang merujuk akun pada field Asset Cost: Name `Office Buildings {runId}` (24 kar), Asset Cost `RDU-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-053-4** Asset Class (awal), Asset Class kedua yang merujuk akun yang sama pada field Asset Cost: Name `Warehouse Buildings {runId}` (27 kar), Asset Cost `RDU-{runId}` (11 kar) · sumber FACO-LOGIC-02h
- **DU-054-1** User (awal), User Manage accounting dengan huruf Create saja ditambah Read: Name `Rudi Hartono {runId}` (20 kar), Role `Global Role Manage accounting huruf Read dan Create (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-054-2** Account (awal), Akun Active dipakai 2 Asset Class, sehingga Used By bernilai 2: Account Code `CRU-{runId}` (11 kar), Account Name `Fixed Assets – Machinery {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-054-3** Asset Class (awal), Asset Class pertama yang merujuk akun pada field Asset Cost: Name `Production Machinery {runId}` (28 kar), Asset Cost `CRU-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-054-4** Asset Class (awal), Asset Class kedua yang merujuk akun yang sama pada field Asset Cost: Name `Packaging Machinery {runId}` (27 kar), Asset Cost `CRU-{runId}` (11 kar) · sumber FACO-LOGIC-02h
- **DU-055-1** User (awal), User Manage accounting dengan huruf Update saja ditambah Read: Name `Dewi Anggraini {runId}` (22 kar), Role `Global Role Manage accounting huruf Read dan Update (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-055-2** Account (awal), Akun Active dipakai 2 Asset Class, sehingga Used By bernilai 2: Account Code `UPU-{runId}` (11 kar), Account Name `Fixed Assets – Equipment {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-055-3** Asset Class (awal), Asset Class pertama yang merujuk akun pada field Asset Cost: Name `Office Equipment {runId}` (24 kar), Asset Cost `UPU-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-055-4** Asset Class (awal), Asset Class kedua yang merujuk akun yang sama pada field Asset Cost: Name `Laboratory Equipment {runId}` (28 kar), Asset Cost `UPU-{runId}` (11 kar) · sumber FACO-LOGIC-02h
- **DU-056-1** User (awal), User Manage accounting dengan huruf Delete saja ditambah Read: Name `Agus Salim {runId}` (18 kar), Role `Global Role Manage accounting huruf Read dan Delete (Read baseline terkunci)` (76 kar), Scope `Seluruh client` (14 kar) · sumber matriks role PRD
- **DU-056-2** Account (awal), Akun Active dipakai 2 Asset Class, sehingga Used By bernilai 2: Account Code `DLU-{runId}` (11 kar), Account Name `Fixed Assets – Furniture {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-056-3** Asset Class (awal), Asset Class pertama yang merujuk akun pada field Asset Cost: Name `Meeting Furniture {runId}` (25 kar), Asset Cost `DLU-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-056-4** Asset Class (awal), Asset Class kedua yang merujuk akun yang sama pada field Asset Cost: Name `Staff Furniture {runId}` (23 kar), Asset Cost `DLU-{runId}` (11 kar) · sumber FACO-LOGIC-02h
- **DU-060-1** Account (awal), Akun Active dipakai 3 Asset Class berbeda, salah satunya Inactive: Account Code `UBC` (3 kar), Account Name `Equipment Cost` (14 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02h
- **DU-060-2** Account (awal), Akun Gain on Disposal dipakai satu Asset Class pada field Gain on Disposal dan Loss on Disposal: Account Code `UBG` (3 kar), Account Name `Gain and Loss on Disposal` (25 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02f
- **DU-060-3** Account (awal), Akun Accumulated Depreciation dipakai 2 Asset Class: Account Code `UBA` (3 kar), Account Name `Accumulated Depreciation Equipment` (34 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-060-4** Account (awal), Akun Depreciation Expense dipakai 1 Asset Class: Account Code `UBE` (3 kar), Account Name `Depreciation Expense Equipment` (30 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-060-5** Account (awal), Akun Active tidak dipakai Asset Class: Account Code `UBN` (3 kar), Account Name `Unused Account` (14 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.1.1#r5
- **DU-060-6** Account (awal), Akun Inactive tidak dipakai Asset Class: Account Code `UBI` (3 kar), Account Name `Legacy Unused Account` (21 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02g
- **DU-060-7** Asset Class (awal), Asset Class yang merujuk lima field akun, akun Gain on Disposal dipakai pada dua field, dibuat paling akhir: Name `Delivery Vehicles {runId}` (25 kar), Asset Name Count `3` (1 kar), Asset Cost `UBC` (3 kar), Accumulated Depreciation `UBA` (3 kar), Depreciation Expense `UBE` (3 kar), Gain on Disposal `UBG` (3 kar), Loss on Disposal `UBG` (3 kar) · sumber FACO-LOGIC-02a
- **DU-060-8** Asset Class (awal; dimutasi TC-FA-FACO-E2E-060-used-by-dan-popup-dep-asset-class), Asset Class dengan 12 Asset Name, merujuk akun Loss on Disposal UBL, dibuat sesudah DU-060-9 dan sebelum DU-060-7; satu Asset Name di-Unassign oleh spec: Name `Heavy Equipment {runId}` (23 kar), Asset Name Count `12` (2 kar), Asset Cost `UBC` (3 kar), Accumulated Depreciation `UBA` (3 kar), Loss on Disposal `UBL` (3 kar) · sumber PRD §4.1.4 Example Data
- **DU-060-9** Asset Class (awal), Asset Class Inactive dengan 1 Asset Name, merujuk akun Gain on Disposal UBP, dibuat paling dulu: Name `Office Equipment {runId}` (24 kar), Status `Inactive` (8 kar), Asset Name Count `1` (1 kar), Asset Cost `UBC` (3 kar), Gain on Disposal `UBP` (3 kar) · sumber PRD §4.1.4 Example Data
- **DU-060-10** Entitas (awal), Entitas khusus spec ini untuk Search atas kolom Used By pada seluruh daftar akun: Name `Entitas Uji Used By {runId}` (27 kar), Akun `DU-060-1 sampai DU-060-6, DU-060-11, DU-060-12` (46 kar), Digit 3 `hanya pada nilai Used By 3 milik DU-060-1; akun tanpa pengenal run dan tanpa digit 3 pada Account Code, Account Name, Account Function` (134 kar) · sumber turunan penulis
- **DU-060-11** Account (awal), Akun Loss on Disposal dipakai satu Asset Class hanya pada field Loss on Disposal: Account Code `UBL` (3 kar), Account Name `Vehicle Loss on Disposal` (24 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-060-12** Account (awal), Akun Gain on Disposal dipakai satu Asset Class hanya pada field Gain on Disposal: Account Code `UBP` (3 kar), Account Name `Equipment Gain on Disposal` (26 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02a
- **DU-061-1** Account (awal), Akun Active dengan Used By 1: Account Code `DAX-{runId}` (11 kar), Account Name `Mesin Bubut {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02c
- **DU-061-2** Account (awal), Akun Active dengan Used By 2: Account Code `DAY-{runId}` (11 kar), Account Name `Mesin Press {runId}` (19 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-02c
- **DU-061-3** Asset Class (awal), Asset Class pemakai akun: Name `Heavy Equipment {runId}` (23 kar), Asset Cost `DAX-{runId}` (11 kar), Accumulated Depreciation `DAY-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-061-4** Asset Class (awal), Asset Class pemakai akun: Name `Office Equipment {runId}` (24 kar), Accumulated Depreciation `DAY-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-062-1** Account (awal; dimutasi TC-FA-FACO-E2E-062-bulk-deactivate-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DBP1-{runId}` (12 kar), Account Name `Gudang Penyusutan Utara {runId}` (31 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r9
- **DU-062-2** Account (awal; dimutasi TC-FA-FACO-E2E-062-bulk-deactivate-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DBP2-{runId}` (12 kar), Account Name `Gudang Penyusutan Selatan {runId}` (33 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r9
- **DU-062-3** Account (awal), Akun Active dengan Used By 1: Account Code `DBB1-{runId}` (12 kar), Account Name `Armada Truk {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r9
- **DU-062-4** Account (awal; dimutasi TC-FA-FACO-E2E-062-bulk-deactivate-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DBP3-{runId}` (12 kar), Account Name `Gudang Penyusutan Barat {runId}` (31 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.2f#b2
- **DU-062-5** Account (awal), Akun Active dengan Used By 1: Account Code `DBB2-{runId}` (12 kar), Account Name `Armada Pickup {runId}` (21 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.2f#b2
- **DU-062-6** Asset Class (awal), Asset Class pemakai akun: Name `Armada Distribusi {runId}` (25 kar), Asset Cost `DBB1-{runId}` (12 kar), Accumulated Depreciation `DBB2-{runId}` (12 kar) · sumber FACO-LOGIC-02a
- **DU-063-1** Account (awal), Akun Active dengan Used By 1: Account Code `DLX-{runId}` (11 kar), Account Name `Mesin Cetak {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-03b
- **DU-063-2** Account (awal), Akun Active dengan Used By 2: Account Code `DLY-{runId}` (11 kar), Account Name `Mesin Potong {runId}` (20 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-03b
- **DU-063-3** Asset Class (awal), Asset Class pemakai akun: Name `Heavy Equipment {runId}` (23 kar), Asset Cost `DLX-{runId}` (11 kar), Accumulated Depreciation `DLY-{runId}` (11 kar) · sumber FACO-LOGIC-03b
- **DU-063-4** Asset Class (awal), Asset Class pemakai akun: Name `Office Equipment {runId}` (24 kar), Accumulated Depreciation `DLY-{runId}` (11 kar) · sumber FACO-LOGIC-03b
- **DU-064-1** Account (awal; dimutasi TC-FA-FACO-E2E-064-bulk-delete-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DLP1-{runId}` (12 kar), Account Name `Rak Gudang Utara {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r11
- **DU-064-2** Account (awal; dimutasi TC-FA-FACO-E2E-064-bulk-delete-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DLP2-{runId}` (12 kar), Account Name `Rak Gudang Selatan {runId}` (26 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r11
- **DU-064-3** Account (awal), Akun Active dengan Used By 1: Account Code `DLB1-{runId}` (12 kar), Account Name `Forklift Listrik {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r11
- **DU-064-4** Account (awal; dimutasi TC-FA-FACO-E2E-064-bulk-delete-campuran-dep-asset-class), Akun Active dengan Used By 0: Account Code `DLP3-{runId}` (12 kar), Account Name `Rak Gudang Barat {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.2f#b2
- **DU-064-5** Account (awal), Akun Active dengan Used By 1: Account Code `DLB2-{runId}` (12 kar), Account Name `Forklift Diesel {runId}` (23 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.2f#b2
- **DU-064-6** Asset Class (awal), Asset Class pemakai akun: Name `Armada Gudang {runId}` (21 kar), Asset Cost `DLB1-{runId}` (12 kar), Accumulated Depreciation `DLB2-{runId}` (12 kar) · sumber FACO-LOGIC-03b
- **DU-065-1** Account (awal), Akun Active dengan Used By 1: Account Code `LKA-{runId}` (11 kar), Account Name `Mesin Las {runId}` (17 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-04b
- **DU-065-2** Account (awal), Akun Active dengan Used By 2: Account Code `LKB-{runId}` (11 kar), Account Name `Mesin Bor {runId}` (17 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-04b
- **DU-065-3** Asset Class (awal), Asset Class pemakai akun: Name `Heavy Equipment {runId}` (23 kar), Asset Cost `LKA-{runId}` (11 kar), Accumulated Depreciation `LKB-{runId}` (11 kar) · sumber FACO-LOGIC-04b
- **DU-065-4** Asset Class (awal), Asset Class pemakai akun: Name `Office Equipment {runId}` (24 kar), Accumulated Depreciation `LKB-{runId}` (11 kar) · sumber FACO-LOGIC-04b
- **DU-066-1** Account (awal; dimutasi TC-FA-FACO-E2E-066-edit-kunci-berubah-dep-asset-class), Akun Active dengan Used By 0: Account Code `EDA-{runId}` (11 kar), Account Name `Mesin Gerinda {runId}` (21 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-02] Edit Account#r4
- **DU-066-2** Account (awal; dimutasi TC-FA-FACO-E2E-066-edit-kunci-berubah-dep-asset-class), Akun Active dengan Used By 0: Account Code `EDB-{runId}` (11 kar), Account Name `Mesin Frais {runId}` (19 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-02] Edit Account#r16
- **DU-066-3** Asset Class (awal; dimutasi TC-FA-FACO-E2E-066-edit-kunci-berubah-dep-asset-class), Asset Class pemicu pemakaian akun sesudah form Edit dibuka: Name `Armada Produksi {runId}` (23 kar) · sumber §[F-FACO-02] Edit Account#r4
- **DU-066-4** Account (dicoba), Perubahan yang ditolak karena Account Function terkunci: Account Name `Mesin Gerinda Baru {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r4
- **DU-066-5** Account (dibuat), Perubahan Account Name yang tersimpan: Account Name `Mesin Frais Baru {runId}` (24 kar) · sumber §[F-FACO-02] Edit Account#r16
- **DU-067-1** Account (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RCA-{runId}` (11 kar), Account Name `Lini Produksi A {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r7
- **DU-067-2** Account (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RCB-{runId}` (11 kar), Account Name `Lini Produksi B {runId}` (23 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r8
- **DU-067-3** Account (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RCC-{runId}` (11 kar), Account Name `Lini Produksi C {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-04] Deactivate Account#r8
- **DU-067-4** Account (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RCD-{runId}` (11 kar), Account Name `Lini Produksi D {runId}` (23 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §7.3#b7
- **DU-067-5** Account (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RCE-{runId}` (11 kar), Account Name `Lini Produksi E {runId}` (23 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §7.3#b7
- **DU-067-6** Asset Class (awal; dimutasi TC-FA-FACO-E2E-067-deactivate-cek-ulang-dep-asset-class), Asset Class pemicu pemakaian akun sesudah dialog dibuka: Name `Armada Perakitan {runId}` (24 kar) · sumber §[F-FACO-04] Deactivate Account#r7
- **DU-068-1** Account (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RDA-{runId}` (11 kar), Account Name `Cabang Medan {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r15
- **DU-068-2** Account (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RDB-{runId}` (11 kar), Account Name `Cabang Padang {runId}` (21 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r16
- **DU-068-3** Account (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RDC-{runId}` (11 kar), Account Name `Cabang Pekanbaru {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r16
- **DU-068-4** Account (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RDD-{runId}` (11 kar), Account Name `Cabang Jambi {runId}` (20 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §7.3#b7
- **DU-068-5** Account (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Akun Active dengan Used By 0: Account Code `RDE-{runId}` (11 kar), Account Name `Cabang Batam {runId}` (20 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §7.3#b7
- **DU-068-6** Asset Class (awal; dimutasi TC-FA-FACO-E2E-068-delete-cek-ulang-dep-asset-class), Asset Class pemicu pemakaian akun sesudah dialog dibuka: Name `Armada Cabang {runId}` (21 kar) · sumber §[F-FACO-05] Delete Account#r15
- **DU-069-1** Account (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Active dengan Used By 1: Account Code `KSA-{runId}` (11 kar), Account Name `Mesin Produksi {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §9.7#r18
- **DU-069-2** Account (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Active dengan Used By 0: Account Code `KSD-{runId}` (11 kar), Account Name `Mesin Cadangan {runId}` (22 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §9.7#r23
- **DU-069-3** Account (awal), Akun Active dengan Used By 0: Account Code `KSE-{runId}` (11 kar), Account Name `Mesin Utama Beban {runId}` (25 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §9.7#r23
- **DU-069-4** Account (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Inactive dengan Used By 0: Account Code `KSF-{runId}` (11 kar), Account Name `Akumulasi Lama {runId}` (22 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §9.7#r21
- **DU-069-5** Account (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Active dengan Used By 0: Account Code `KSG-{runId}` (11 kar), Account Name `Rugi Pelepasan Aset {runId}` (27 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §9.7#r26
- **DU-069-6** Account (awal), Akun Active dengan Used By 0: Account Code `KSL-{runId}` (11 kar), Account Name `Rugi Pelepasan Cadangan {runId}` (31 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-01b
- **DU-069-7** Account (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Active dengan Used By 1, bukan nilai default company: Account Code `KSH-{runId}` (11 kar), Account Name `Laba Lama {runId}` (17 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber S-12
- **DU-069-8** Asset Class (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Asset Class konsumen akun sebelum aksi pada akun: Name `Konsumen Utama {runId}` (22 kar), Asset Cost `KSA-{runId}` (11 kar), Gain on Disposal `KSH-{runId}` (11 kar) · sumber S-12
- **DU-069-9** Account (dibuat; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Akun Gain on Disposal yang dibuat dari tombol + Account: Account Code `KSC-{runId}` (11 kar), Account Name `Laba Pelepasan Aset {runId}` (27 kar), Account Function `Gain on Disposal` (16 kar) · sumber §9.7#r16
- **DU-069-10** Account (dibuat), Account Code baru hasil Edit: Account Code `KSI-{runId}` (11 kar) · sumber §9.7#p4
- **DU-069-11** Account (dibuat), Account Name baru hasil Edit: Account Name `Mesin Produksi Baru {runId}` (27 kar) · sumber §9.7#r18
- **DU-069-12** Account (dibuat), Account Code baru hasil Edit akun yang dipakai Asset Class: Account Code `KSJ-{runId}` (11 kar) · sumber §9.7#p4
- **DU-069-13** Account (awal), Akun Active dipakai 2 Asset Class, salah satunya melepas akun ini: Account Code `KSK-{runId}` (11 kar), Account Name `Laba Bersama {runId}` (20 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber S-12
- **DU-069-14** Asset Class (awal; dimutasi TC-FA-FACO-E2E-069-konsumen-opsi-akun-dep-asset-class), Asset Class yang melepas akun KSK dengan menggantinya ke KSL: Name `Konsumen Pelepas {runId}` (24 kar), Gain on Disposal `KSK-{runId}` (11 kar) · sumber S-12
- **DU-069-15** Asset Class (awal), Asset Class yang tetap memakai akun KSK: Name `Konsumen Tetap {runId}` (22 kar), Gain on Disposal `KSK-{runId}` (11 kar) · sumber S-12
- **DU-070-1** Asset Class (awal; dimutasi TC-FA-FACO-E2E-070-create-dari-shortcut-dep-asset-class), Asset Class asal shortcut Create Account: Name `Shortcut Class {runId}` (22 kar) · sumber FACO-LOGIC-12d
- **DU-070-2** Account (dibuat), Akun Asset Cost yang dibuat dari shortcut: Account Code `SCT-{runId}` (11 kar), Account Name `Peralatan Kantor {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber FACO-LOGIC-12b
- **DU-071-1** Account (awal), Akun Accumulated Depreciation dipakai 2 Asset Class; urutan Account Code-nya menempatkan Used By 2 paling atas pada urutan default: Account Code `SUA-{runId}` (11 kar), Account Name `Accumulated Depreciation Sort {runId}` (37 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.1.1#r5
- **DU-071-2** Account (awal), Akun Asset Cost dipakai 10 Asset Class, nilai dua digit untuk membedakan urutan numerik dari urutan teks: Account Code `SUB-{runId}` (11 kar), Account Name `Equipment Cost Sort {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `10` (2 kar), Last Used in Journal `—` (1 kar) · sumber foundation prd-conventions.md §9.7
- **DU-071-3** Account (awal), Akun Gain on Disposal tidak dipakai Asset Class, Used By 0: Account Code `SUC-{runId}` (11 kar), Account Name `Gain on Disposal Sort {runId}` (29 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.1.1#r5
- **DU-071-4** Account (awal), Akun Depreciation Expense dipakai 1 Asset Class: Account Code `SUD-{runId}` (11 kar), Account Name `Depreciation Expense Sort {runId}` (33 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.1.1#r5
- **DU-071-5** Asset Class (awal), Asset Class yang merujuk tiga akun uji pada tiga field berbeda: Name `Sort Class 1 {runId}` (20 kar), Status `Active` (6 kar), Asset Cost `SUB-{runId}` (11 kar), Accumulated Depreciation `SUA-{runId}` (11 kar), Depreciation Expense `SUD-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-071-6** Asset Class (awal), Asset Class yang merujuk akun Asset Cost dan Accumulated Depreciation uji: Name `Sort Class 2 {runId}` (20 kar), Status `Active` (6 kar), Asset Cost `SUB-{runId}` (11 kar), Accumulated Depreciation `SUA-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-071-7** Asset Class (awal; 8 record), Delapan Asset Class yang hanya merujuk akun Asset Cost uji, penggenap 10 pemakai: Name `Sort Class {n} {runId}` (22 kar), Status `Active` (6 kar), Asset Cost `SUB-{runId}` (11 kar) · sumber FACO-LOGIC-02a
- **DU-075-1** Account (awal; dimutasi TC-FA-FACO-E2E-075-last-used-in-journal-dep-export-journal), Akun Asset Cost pemakai Asset Class yang belum pernah diekspor, lalu diekspor beberapa kali dengan periode berbeda: Account Code `LUJ1-{runId}` (12 kar), Account Name `Equipment Cost Journal {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber F-FACO-08
- **DU-075-2** User (awal), Admin yang membuka tabel, berbeda dari pengekspor yang memajukan nilai, dan pengekspor Export Journal periode Jul 2026 dan Aug 2026 yang diulang: Full Name `Sari Kusuma {runId}` (19 kar), Access Level `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber turunan penulis
- **DU-075-5** User (awal), Admin pengekspor Export Journal periode Jun 2026 dan Aug 2026 yang memajukan nilai, namanya tampil sebagai User Name pada hover Last Used in Journal: Full Name `Budi Santoso {runId}` (20 kar), Access Level `Total Control` (13 kar), Cakupan `seluruh client` (14 kar) · sumber turunan penulis
- **DU-075-3** Asset Class (awal), Asset Class pemakai akun DU-075-1 sehingga akun ikut Export Journal: Name `Kelas Ekspor Jurnal {runId}` (27 kar), Status `Active` (6 kar), Asset Cost `LUJ1-{runId}` (12 kar) · sumber turunan penulis
- **DU-075-4** Entitas (awal), Entitas khusus dengan Date Format dan Time Format non-bawaan untuk hover Last Used in Journal: Name `Entitas Hover Journal {runId}` (29 kar), Date Format `dd MMM yy` (9 kar), Time Format `12h` (3 kar) · sumber foundation §32
- **DU-076-1** Account (awal), Akun diekspor satu bulan sebelum batas awal rentang filter: Account Code `LUS1-{runId}` (12 kar), Account Name `Building Cost {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 7 bulan` (12 kar) · sumber §4.1.1#b1
- **DU-076-2** Account (awal), Akun diekspor tepat di bulan akhir rentang filter: Account Code `LUS2-{runId}` (12 kar), Account Name `Vehicle Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 4 bulan` (12 kar) · sumber §4.1.1#b1
- **DU-076-3** Account (awal), Akun diekspor di dalam rentang filter dan menjadi satu-satunya bulan pada rentang satu bulan: Account Code `LUS3-{runId}` (12 kar), Account Name `Machinery Cost {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 5 bulan` (12 kar) · sumber §4.1.1#b1
- **DU-076-4** Account (awal), Akun diekspor tepat di bulan awal rentang filter: Account Code `LUS4-{runId}` (12 kar), Account Name `Furniture Cost {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 6 bulan` (12 kar) · sumber §4.1.1#b1
- **DU-076-5** Account (awal), Akun diekspor satu bulan sesudah batas akhir rentang filter: Account Code `LUS5-{runId}` (12 kar), Account Name `Equipment Cost {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 3 bulan` (12 kar) · sumber §4.1.1#b1
- **DU-076-6** Account (awal), Akun yang belum pernah diekspor sehingga Last Used in Journal kosong: Account Code `LUS6-{runId}` (12 kar), Account Name `Software Cost {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §4.1.1#r6
- **DU-077-1** Account (awal), Akun Capitalization Offset Active tanpa pemakai Asset Class, bukan nilai default company, belum pernah diekspor: Account Code `LKA1-{runId}` (12 kar), Account Name `Land Improvement Cost {runId}` (29 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-03a
- **DU-077-2** Account (awal), Akun Capitalization Offset Active tanpa pemakai Asset Class yang sudah pernah diekspor (Last Used in Journal terisi): Account Code `LKA2-{runId}` (12 kar), Account Name `Repairs Capitalization Offset {runId}` (37 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 2 bulan` (12 kar) · sumber PRD §4.1.1 Example Data (6-2001 Repairs & Maintenance Expense: Capitalization Offset, Used By 0, pernah diekspor)
- **DU-078-1** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan formnya dibuka sebelum export selesai: Account Code `LKB1-{runId}` (12 kar), Account Name `Rental Equipment Cost {runId}` (29 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-02] Edit Account#r14
- **DU-078-2** Account (dicoba), Perubahan Account Code dan Account Name yang dikirim sesudah kunci berubah: Account Code `LKB1X-{runId}` (13 kar), Account Name `Rental Equipment Cost Revised {runId}` (37 kar) · sumber §[F-FACO-02] Edit Account#r14
- **DU-078-3** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan hanya Account Name-nya diubah sesudah kunci berubah: Account Code `LKB2-{runId}` (12 kar), Account Name `Warehouse Racking Cost {runId}` (30 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-02] Edit Account#r16
- **DU-078-4** Account (dibuat), Account Name baru yang disimpan sesudah kunci berubah: Account Name `Warehouse Racking Cost Revised {runId}` (38 kar) · sumber §[F-FACO-02] Edit Account#r16
- **DU-078-5** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan dialog Delete-nya dibuka sebelum export selesai: Account Code `LKB3-{runId}` (12 kar), Account Name `Dock Leveler Cost {runId}` (25 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber §[F-FACO-05] Delete Account#r15
- **DU-078-6** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan menjadi diekspor sesudah dialog Bulk Delete dibuka; lolos dan terhapus: Account Code `LKB4-{runId}` (12 kar), Account Name `Pallet Jack Cost {runId}` (24 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `—` (1 kar) · sumber §9.4.2#r22
- **DU-078-7** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan menjadi diekspor sesudah dialog Bulk Delete dibuka; dilewati bersama akun yang lolos: Account Code `LKB5-{runId}` (12 kar), Account Name `Conveyor Belt Cost {runId}` (26 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `—` (1 kar) · sumber §9.4.2#r22
- **DU-078-8** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan menjadi diekspor sesudah dialog Bulk Delete dibuka; seluruh akun terpilih ditolak: Account Code `LKB6-{runId}` (12 kar), Account Name `Mezzanine Floor Cost {runId}` (28 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `—` (1 kar) · sumber §9.4.2#r22
- **DU-078-9** Account (awal; dimutasi TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal), Akun Capitalization Offset Active yang belum diekspor dan menjadi diekspor sesudah dialog Bulk Delete dibuka; seluruh akun terpilih ditolak: Account Code `LKB7-{runId}` (12 kar), Account Name `Cold Storage Fit-out Cost {runId}` (33 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `—` (1 kar) · sumber §9.4.2#r22
- **DU-079-1** Account (awal), Akun terekspor pertama yang ikut Bulk Delete seluruhnya diblokir: Account Code `BDX1-{runId}` (12 kar), Account Name `Plant Cost {runId}` (18 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 2 bulan` (12 kar) · sumber D-12
- **DU-079-2** Account (awal), Akun terekspor kedua yang ikut Bulk Delete seluruhnya diblokir: Account Code `BDX2-{runId}` (12 kar), Account Name `Tooling Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 3 bulan` (12 kar) · sumber D-12
- **DU-079-3** Account (awal), Akun terekspor yang dilewati pada Bulk Delete campuran: Account Code `BDX3-{runId}` (12 kar), Account Name `Fixture Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 4 bulan` (12 kar) · sumber D-09
- **DU-079-4** Account (awal; dimutasi TC-FA-FACO-E2E-079-bulk-delete-terekspor-dep-export-journal), Akun yang belum pernah diekspor dan terhapus pada Bulk Delete campuran: Account Code `BDF1-{runId}` (12 kar), Account Name `Scaffolding Cost {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber D-09
- **DU-080-1** Account (awal; dimutasi TC-FA-FACO-E2E-080-rename-berkas-export-dep-export-journal), Akun yang diekspor lalu Account Name-nya diubah: Account Code `RNX1-{runId}` (12 kar), Account Name `Plant Machinery Cost {runId}` (28 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber FACO-LOGIC-04d
- **DU-080-2** Account (dibuat), Akun baru yang dibuat sesudah export pertama dan harus muncul di export kedua: Account Code `RNX2-{runId}` (12 kar), Account Name `Conveyor Cost {runId}` (21 kar), Account Function `Capitalization Offset` (21 kar) · sumber PRD §11.1 Internal & Downstream Dependencies
- **DU-080-3** Account (dibuat), Account Name baru yang berlaku untuk export berikutnya: Account Name `Plant Machinery Cost Revised {runId}` (36 kar) · sumber FACO-LOGIC-04d
- **DU-081-1** Account (awal; dimutasi TC-FA-FACO-E2E-081-deactivate-akun-terekspor-dep-export-journal), Akun Active tanpa pemakai Asset Class yang sudah pernah diekspor lalu dinonaktifkan: Account Code `DXA1-{runId}` (12 kar), Account Name `Retired Fleet Cost {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 2 bulan` (12 kar) · sumber FACO-LOGIC-03a
- **DU-082-1** Account (awal), Akun Asset Cost Active yang pernah diekspor dan dipakai 1 Asset Class: Account Code `DEA1-{runId}` (12 kar), Account Name `Heavy Machinery Cost {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `M0 − 2 bulan` (12 kar) · sumber D-05
- **DU-082-2** Account (awal), Akun Accumulated Depreciation Active yang pernah diekspor dan dipakai 2 Asset Class: Account Code `DEB1-{runId}` (12 kar), Account Name `Fleet Accumulated Depreciation {runId}` (38 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar), Default Company `Bukan nilai default company` (27 kar), Last Used in Journal `M0 − 2 bulan` (12 kar) · sumber D-05
- **DU-082-3** Asset Class (awal), Asset Class pemakai kedua akun pada Asset Cost dan Accumulated Depreciation: Name `Kelas Alat Berat {runId}` (24 kar), Asset Cost `DEA1-{runId}` (12 kar), Accumulated Depreciation `DEB1-{runId}` (12 kar) · sumber D-05
- **DU-082-4** Asset Class (awal), Asset Class pemakai akun Accumulated Depreciation: Name `Kelas Armada {runId}` (20 kar), Accumulated Depreciation `DEB1-{runId}` (12 kar) · sumber D-05
- **DU-085-1** Account (awal), Akun default company yang tidak dipakai Asset Class dan tidak pernah diekspor: Account Code `DDC1-{runId}` (12 kar), Account Name `Gain Disposal Default {runId}` (29 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default company `Default Gain on Disposal` (24 kar) · sumber D-06
- **DU-085-2** Account (awal), Akun yang sekaligus dipakai 1 Asset Class dan menjadi default company: Account Code `DDC2-{runId}` (12 kar), Account Name `Loss Disposal Default {runId}` (29 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `1` (1 kar), Default company `Default Loss on Disposal` (24 kar) · sumber D-06
- **DU-086-1** Account (awal), Akun default company Default Capitalization Offset yang dilewati Bulk Delete: Account Code `DDM1-{runId}` (12 kar), Account Name `Offset Default {runId}` (22 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default company `Default Capitalization Offset` (29 kar) · sumber D-09
- **DU-086-2** Account (awal; dimutasi TC-FA-FACO-E2E-086-bulk-delete-default-company-dep-preferences), Akun bebas yang lolos Bulk Delete dan terhapus: Account Code `DDM2-{runId}` (12 kar), Account Name `Surplus Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber D-09
- **DU-087-1** Account (awal; dimutasi TC-FA-FACO-E2E-087-konsumen-default-akun-dep-preferences), Akun Disposal Proceeds yang menjadi default company lalu diubah Account Name-nya: Account Code `RFL1-{runId}` (12 kar), Account Name `Proceeds Clearing {runId}` (25 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar), Used By `0` (1 kar), Default company `Default Disposal Proceeds Account` (33 kar) · sumber FACO-LOGIC-01f
- **DU-087-2** Account (dibuat), Account Name baru yang tercermin di Preferences: Account Name `Proceeds Clearing Revised {runId}` (33 kar) · sumber PRD §9.2 Reflected consumers
- **DU-087-3** Account (dibuat; dimutasi TC-FA-FACO-E2E-087-konsumen-default-akun-dep-preferences), Akun Capitalization Offset yang dibuat lalu dihapus: Account Code `RFL2-{runId}` (12 kar), Account Name `Offset Created {runId}` (22 kar), Account Function `Capitalization Offset` (21 kar) · sumber FACO-LOGIC-01d
- **DU-087-4** Account (awal), Akun Capitalization Offset penanda yang tetap ada sebagai opsi: Account Code `RFL3-{runId}` (12 kar), Account Name `Offset Anchor {runId}` (21 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber FACO-LOGIC-01d
- **DU-088-1** Account (awal), Akun Capitalization Offset dengan Account Name terakhir menurut urutan A-Z: Account Code `SCA1-{runId}` (12 kar), Account Name `Zeta Offset {runId}` (19 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber FACO-LOGIC-12e
- **DU-088-2** Account (awal), Akun Capitalization Offset dengan Account Name pertama menurut urutan A-Z: Account Code `SCA2-{runId}` (12 kar), Account Name `Alpha Offset {runId}` (20 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber FACO-LOGIC-12e
- **DU-088-3** Account (dibuat), Akun yang dibuat dari shortcut dan tidak berada di urutan default Account Code: Account Code `SCA3-{runId}` (12 kar), Account Name `Beta Offset New {runId}` (23 kar), Account Function `Capitalization Offset` (21 kar) · sumber FACO-LOGIC-12d
- **DU-090-1** Account (awal; dimutasi TC-FA-FACO-E2E-090-konsumen-tab-accounts-dep-custom-asset-id), Akun awal yang Account Code-nya diubah dan dibaca tab Accounts Custom Asset ID: Account Code `CAI1-{runId}` (12 kar), Account Name `Pipeline Cost {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber §9.7#p4
- **DU-090-2** Account (dibuat; dimutasi TC-FA-FACO-E2E-090-konsumen-tab-accounts-dep-custom-asset-id), Akun yang dibuat lalu diubah Account Name-nya dan dihapus: Account Code `CAI2-{runId}` (12 kar), Account Name `Conduit Cost {runId}` (20 kar), Account Function `Asset Cost` (10 kar) · sumber PRD §11.1 Internal & Downstream Dependencies
- **DU-090-3** Account (dibuat), Account Code baru yang langsung tampil di tab Accounts: Account Code `CAI1R-{runId}` (13 kar) · sumber §9.7#p4
- **DU-090-4** Account (dibuat), Account Name baru yang tercermin di tab Accounts: Account Name `Conduit Cost Revised {runId}` (28 kar) · sumber PRD §11.1 Internal & Downstream Dependencies
- **DU-092-1** Account (awal; dimutasi TC-FA-FACO-E2E-092-akun-hasil-import-dep-import), Akun hasil Import yang di-Edit: Account Code `IMP1-{runId}` (12 kar), Account Name `Imported Cost {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber EB-XM-3
- **DU-092-2** Account (awal; dimutasi TC-FA-FACO-E2E-092-akun-hasil-import-dep-import), Akun hasil Import yang dihapus: Account Code `IMP2-{runId}` (12 kar), Account Name `Imported Surplus {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber EB-XM-3
- **DU-092-3** Account (dibuat), Account Name baru untuk akun hasil Import: Account Name `Imported Cost Revised {runId}` (29 kar) · sumber EB-XM-3
- **DU-093-1** Account (dibuat; dimutasi TC-FA-FACO-E2E-093-system-log-dep-user), Akun yang dibuat, diubah, dinonaktifkan, diaktifkan, dan dihapus untuk memicu log: Account Code `SYL1-{runId}` (12 kar), Account Name `Audit Trail Cost {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber §8.2#r1
- **DU-093-2** Account (dibuat), Account Name baru untuk baris log Edit field Account Name: Account Name `Audit Trail Cost Revised {runId}` (32 kar) · sumber §8.2#r1
- **DU-093-3** Account (dibuat), Account Code baru; Name pada baris log Edit Account Code berisi kode setelah perubahan: Account Code `SYL2-{runId}` (12 kar) · sumber PRD §8.1 Changelog
- **DU-094-1** Account (dibuat; dimutasi TC-FA-FACO-E2E-094-activity-log-dep-activity-log), Akun yang dibuat, diubah, dinonaktifkan, diaktifkan, dan dihapus untuk memicu log: Account Code `ACL1-{runId}` (12 kar), Account Name `Activity Trail Cost {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber §8.3#p1
- **DU-094-2** Account (dibuat), Account Name baru untuk baris log Edit field Account Name: Account Name `Activity Trail Cost Revised {runId}` (35 kar) · sumber §8.3#p1
- **DU-094-3** Account (dibuat), Account Code baru; Name pada baris log Edit Account Code berisi kode setelah perubahan: Account Code `ACL2-{runId}` (12 kar) · sumber PRD §8.1 Changelog
- **DU-095-1** Entitas (awal; dimutasi TC-FA-FACO-E2E-095-format-tanggal-dep-general-settings), Entitas khusus dengan Date Format, Time Format, dan Time Zone awal: Name `Entitas Format Tanggal {runId}` (30 kar), Date Format `dd/MM/yy` (8 kar), Time Format `24h` (3 kar), Time Zone `Asia/Jakarta` (12 kar) · sumber foundation §32
- **DU-095-2** Account (dibuat), Akun yang dibuat untuk membaca Last Updated dan Changelog: Account Code `FMT1-{runId}` (12 kar), Account Name `Format Probe Cost {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber foundation §32
- **DU-095-3** Setting General Settings (dibuat), Date Format yang diubah menjadi M/d/yy: Date Format `M/d/yy` (6 kar) · sumber foundation §32
- **DU-095-4** Setting General Settings (dibuat), Date Format yang diubah menjadi dd MMM yy: Date Format `dd MMM yy` (9 kar) · sumber foundation §32
- **DU-095-5** Setting General Settings (dibuat), Date Format yang diubah menjadi DDD, MMM dd, yy: Date Format `DDD, MMM dd, yy` (15 kar) · sumber foundation §32
- **DU-095-6** Setting General Settings (dibuat), Date Format yang diubah menjadi DDD, MMM dd, yyyy: Date Format `DDD, MMM dd, yyyy` (17 kar) · sumber foundation §32
- **DU-095-7** Setting General Settings (dibuat), Time Format yang diubah menjadi 12 jam: Time Format `12h` (3 kar) · sumber foundation §32
- **DU-095-8** Setting General Settings (dibuat), Time Zone non-default: Time Zone `Asia/Tokyo` (10 kar) · sumber foundation §32
- **DU-100-1** Account Function (awal), tujuh opsi Account Function pada dropdown: Opsi 1 `Asset Cost` (10 kar), Opsi 2 `Accumulated Depreciation` (24 kar), Opsi 3 `Depreciation Expense` (20 kar), Opsi 4 `Gain on Disposal` (16 kar), Opsi 5 `Loss on Disposal` (16 kar), Opsi 6 `Capitalization Offset` (21 kar), Opsi 7 `Disposal Proceeds` (17 kar) · sumber FACO-LOGIC-01a
- **DU-100-2** Account Function (dibuat), satu opsi Account Function dipilih: Account Function `Asset Cost` (10 kar) · sumber §4.1.2#r3
- **DU-101-1** Account (awal), akun yang sudah memakai Account Code FIN-OPS-01: Account Code `FIN-OPS-01` (10 kar), Account Name `Biaya Operasional Keuangan` (26 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-101-2** Account (dicoba), Account Code kosong: Account Code `` (0 kar) · sumber V-01
- **DU-101-3** Account (dicoba), Account Code hanya spasi: Account Code `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-101-4** Account (dibuat), Account Code tepat 15 karakter: Account Code `1-1001-EQUIP-01` (15 kar) · sumber V-02
- **DU-101-5** Account (dicoba), Account Code 16 karakter: Account Code `1-1001-EQUIP-016` (16 kar) · sumber V-02
- **DU-101-6** Account (dibuat), Account Code 15 karakter dengan spasi di tepi: Account Code `  1-2001-DEPRC-01  ` (19 kar) · sumber foundation prd-conventions.md §4
- **DU-101-7** Account (dibuat), Account Code dengan tanda hubung: Account Code `5-6001-A` (8 kar) · sumber V-03
- **DU-101-8** Account (dibuat), Account Code dengan garis bawah: Account Code `FIN_OPS` (7 kar) · sumber V-03
- **DU-101-9** Account (dibuat), Account Code dengan titik: Account Code `1.1001.A` (8 kar) · sumber V-03
- **DU-101-10** Account (dicoba), Account Code dengan spasi di tengah: Account Code `1-1001 EQUIP` (12 kar) · sumber V-03
- **DU-101-11** Account (dicoba), Account Code dengan emoji: Account Code `1-1001📊` (7 kar) · sumber V-03
- **DU-101-12** Account (dicoba), Account Code berisi emoji hasil tempel: Account Code `FIN📎OPS` (7 kar) · sumber V-03
- **DU-102-1** Account (awal), akun yang sudah ada dengan Account Name Peralatan Kantor Pusat: Account Code `ASET-EQP-01` (11 kar), Account Name `Peralatan Kantor Pusat` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-102-2** Account (dicoba), Account Name kosong: Account Name `` (0 kar) · sumber V-05
- **DU-102-3** Account (dicoba), Account Name hanya spasi: Account Name `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-102-4** Account (dibuat), Account Name tepat 120 karakter: Account Name `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku` (120 kar) · sumber V-06
- **DU-102-5** Account (dicoba), Account Name 121 karakter: Account Name `Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Bukus` (121 kar) · sumber V-06
- **DU-102-6** Account (dibuat), Account Name 120 karakter dengan spasi di tepi: Account Name `  Biaya Penyusutan Peralatan Kantor Pusat dan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Buku  ` (124 kar) · sumber foundation prd-conventions.md §4
- **DU-102-7** Account (dibuat), Account Name 120 karakter dengan spasi ganda di tengah: Account Name `Pusat  dan  Cabang  Seluruh  Wilayah  Operasional  Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Aset` (120 kar) · sumber foundation prd-conventions.md §4
- **DU-102-8** Account (dibuat), Account Name 120 code point dengan huruf beraksen dan karakter non-BMP: Account Name `Éan Cabang Seluruh Wilayah Operasional Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang𝒜` (120 kar) · sumber foundation prd-conventions.md §4
- **DU-102-9** Account (dicoba), Account Name dengan emoji yang diketik: Account Name `Biaya📊 Operasional` (18 kar), Isi field sesudah emoji diblok `Biaya Operasional` (17 kar) · sumber V-07
- **DU-102-10** Account (dicoba), Account Name dengan emoji yang ditempel: Account Name `Peralatan📎 Gudang` (17 kar), Isi field sesudah emoji dibuang `Peralatan Gudang` (16 kar) · sumber V-07
- **DU-102-11** Account (awal), Account Name berisi emoji yang lolos dari blok klien: Account Name `Gudang Pusat🔥` (13 kar) · sumber V-07
- **DU-102-12** Account (dicoba), Account Function belum dipilih: Account Function `Select account function` (23 kar) · sumber V-08
- **DU-102-13** Account (dibuat), akun baru dengan Account Name yang sama dengan DU-102-1: Account Code `ASET-EQP-02` (11 kar), Account Name `Peralatan Kantor Pusat` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-102-14** Account (dicoba), Account Name yang ditempel dari teks dua baris: Account Name `Peralatan
Gudang` (16 kar), Baris pertama `Peralatan` (9 kar), Baris kedua `Gudang` (6 kar) · sumber foundation prd-conventions.md §4
- **DU-102-15** Account (dicoba), Account Name yang diketik lalu Tab ditekan: Account Name `Gudang` (6 kar) · sumber foundation prd-conventions.md §4
- **DU-103-1** Account (dibuat), input valid lengkap untuk Submit berhasil dan Saving: Account Code `6-3001-GD` (9 kar), Account Name `Biaya Pemeliharaan Gedung {runId}` (33 kar), Account Function `Capitalization Offset` (21 kar) · sumber turunan penulis
- **DU-103-2** Account (dibuat), entri pertama untuk Stay on this form: Account Code `6-3002-GD` (9 kar), Account Name `Biaya Kebersihan Gedung {runId}` (31 kar), Account Function `Disposal Proceeds` (17 kar) · sumber turunan penulis
- **DU-103-3** Account (dibuat), entri kedua untuk Stay on this form: Account Code `6-3003-GD` (9 kar), Account Name `Biaya Keamanan Gedung {runId}` (29 kar), Account Function `Gain on Disposal` (16 kar) · sumber turunan penulis
- **DU-103-4** Account (dibuat), semua kontrol form Add terisi sebelum Clear Field: Account Code `6-3004-GD` (9 kar), Account Name `Biaya Asuransi Gedung {runId}` (29 kar), Account Function `Gain on Disposal` (16 kar), Stay on this form after submitting `tercentang` (10 kar) · sumber turunan penulis
- **DU-103-5** Account (dibuat), nilai Account Name untuk form yang sudah diisi: Account Name `Biaya Listrik Kantor` (20 kar) · sumber turunan penulis
- **DU-104-1** Account (dibuat), input valid untuk penyimpanan berhasil: Account Code `6-4001-PR` (9 kar), Account Name `Biaya Penyusutan Peralatan Produksi {runId}` (43 kar), Account Function `Loss on Disposal` (16 kar) · sumber turunan penulis
- **DU-104-2** Account (dicoba), input valid untuk penyimpanan gagal karena error server: Account Code `6-4002-PR` (9 kar), Account Name `Biaya Penyusutan Kendaraan Operasional {runId}` (46 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-104-3** Account (dicoba), input valid untuk penyimpanan gagal karena timeout: Account Code `6-4003-PR` (9 kar), Account Name `Biaya Penyusutan Mesin Cetak {runId}` (36 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-104-4** Account (dicoba), input valid yang ditolak karena batas jumlah akun: Account Code `6-4004-PR` (9 kar), Account Name `Biaya Penyusutan Bangunan Pabrik {runId}` (40 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-104-5** Account (dicoba), input valid untuk percobaan ulang sesudah pulih: Account Code `6-4005-PR` (9 kar), Account Name `Biaya Penyusutan Komputer Kantor {runId}` (40 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-104-6** Account (dicoba), akun yang disimpan saat koneksi terputus: Account Code `6-4006-PR` (9 kar), Account Name `Biaya Penyusutan Alat Berat {runId}` (35 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-110-1** Account (awal), akun terekspor dengan Last Used in Journal terisi: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Account Function `Asset Cost` (10 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar), Alasan Account Code terkunci `Account Code can't be changed because this account was used in a journal in Oct 2026. Create a new account if needed.` (117 kar), Alasan Account Function terkunci `Account Function can't be changed because this account was used in a journal in Oct 2026.` (89 kar) · sumber PRD §4.1.1 Example Data
- **DU-110-2** Account (awal), akun tanpa kunci: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-110-3** Account (awal), akun dipakai Asset Class dan belum diekspor: Account Code `5-6002` (6 kar), Account Name `Depreciation Expense – Warehouse` (32 kar), Account Function `Depreciation Expense` (20 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-111-1** Account (awal), akun tidak terkunci yang diedit: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-111-2** Account (awal), akun lain yang sudah memakai kode 5-6002: Account Code `5-6002` (6 kar), Account Name `Depreciation Expense – Warehouse` (32 kar), Account Function `Depreciation Expense` (20 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-111-3** Account (dicoba), Account Code dikosongkan lewat Clear Field: Account Code `` (0 kar) · sumber V-01
- **DU-111-4** Account (dicoba), Account Code hanya spasi: Account Code `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-111-5** Account (dibuat), Account Code tepat 15 karakter: Account Code `2-3001-REVAL-01` (15 kar) · sumber V-02
- **DU-111-6** Account (dicoba), Account Code 16 karakter: Account Code `2-3001-REVAL-016` (16 kar) · sumber V-02
- **DU-111-7** Account (dibuat), Account Code 15 karakter dengan spasi di tepi: Account Code `  2-3002-REVAL-02  ` (19 kar) · sumber foundation prd-conventions.md §4
- **DU-111-8** Account (dibuat), Account Code dengan tanda hubung: Account Code `7-1001-B` (8 kar) · sumber V-03
- **DU-111-9** Account (dibuat), Account Code dengan garis bawah: Account Code `ASET_BARU` (9 kar) · sumber V-03
- **DU-111-10** Account (dibuat), Account Code dengan titik: Account Code `2.3003.B` (8 kar) · sumber V-03
- **DU-111-11** Account (dicoba), Account Code dengan spasi di tengah: Account Code `2-3004 REVAL` (12 kar) · sumber V-03
- **DU-111-12** Account (dicoba), Account Code dengan emoji: Account Code `2-3004📈` (7 kar) · sumber V-03
- **DU-111-13** Account (dicoba), Account Code berisi emoji hasil tempel: Account Code `ASET📌BARU` (9 kar) · sumber V-03
- **DU-111-14** Account (dicoba), Account Name dikosongkan lewat Clear Field: Account Name `` (0 kar) · sumber V-05
- **DU-111-15** Account (dicoba), Account Name hanya spasi: Account Name `   ` (3 kar) · sumber foundation prd-conventions.md §4
- **DU-111-16** Account (dibuat), Account Name tepat 120 karakter: Account Name `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang` (120 kar) · sumber V-06
- **DU-111-17** Account (dicoba), Account Name 121 karakter: Account Name `Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabangs` (121 kar) · sumber V-06
- **DU-111-18** Account (dibuat), Account Name 120 karakter dengan spasi di tepi: Account Name `  Produksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Cabang  ` (124 kar) · sumber foundation prd-conventions.md §4
- **DU-111-19** Account (dibuat), Account Name 120 karakter dengan spasi ganda di tengah: Account Name `Perusahaan  untuk  Kelompok  Aset  Tetap  Berwujud  Tahun  Buku  Berjalan  Periode  Gudang  Alat  Kendaraan  Beban  Aset` (120 kar) · sumber foundation prd-conventions.md §4
- **DU-111-20** Account (dibuat), Account Name 120 code point dengan huruf beraksen dan karakter non-BMP: Account Name `Éroduksi Perusahaan untuk Kelompok Aset Tetap Berwujud Tahun Buku Berjalan Periode Gudang Alat Kendaraan Bangunan Beban𝒜` (120 kar) · sumber foundation prd-conventions.md §4
- **DU-111-21** Account (dicoba), Account Name dengan emoji yang diketik: Account Name `Beban📈 Penyusutan` (17 kar), Isi field sesudah emoji diblok `Beban Penyusutan` (16 kar) · sumber V-07
- **DU-111-22** Account (dicoba), Account Name dengan emoji yang ditempel: Account Name `Perawatan📌 Mesin` (16 kar), Isi field sesudah emoji dibuang `Perawatan Mesin` (15 kar) · sumber V-07
- **DU-111-23** Account (awal), Account Name berisi emoji yang lolos dari blok klien: Account Name `Gudang Cabang🔥` (14 kar) · sumber V-07
- **DU-111-24** Account (dicoba), Account Function dikosongkan lewat Clear Field: Account Function `Select account function` (23 kar) · sumber V-08
- **DU-111-25** Account (dicoba), Account Name yang ditempel dari teks dua baris: Account Name `Perawatan
Mesin` (15 kar), Baris pertama `Perawatan` (9 kar), Baris kedua `Mesin` (5 kar) · sumber foundation prd-conventions.md §4
- **DU-111-26** Account (dicoba), Account Name yang diganti lalu Tab ditekan: Account Name `Mesin` (5 kar) · sumber foundation prd-conventions.md §4
- **DU-112-1** Account (awal), akun tidak terkunci dengan semua field terisi: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-112-2** Account (awal), akun terkunci karena Last Used in Journal terisi: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Account Function `Asset Cost` (10 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-112-3** Account (dibuat), Account Name baru untuk Save berhasil: Account Name `Depreciation Expense – Admin Revisi {runId}` (43 kar) · sumber turunan penulis
- **DU-112-4** Account (dicoba), Account Name untuk Save yang gagal karena error server: Account Name `Depreciation Expense – Admin Gagal` (34 kar) · sumber turunan penulis
- **DU-112-5** Account (dicoba), Account Name untuk Save yang gagal karena timeout: Account Name `Depreciation Expense – Admin Putus` (34 kar) · sumber turunan penulis
- **DU-112-6** Account (dibuat), Account Name untuk Save ulang sesudah pulih: Account Name `Depreciation Expense – Admin Pulih {runId}` (42 kar) · sumber turunan penulis
- **DU-112-7** Account (dicoba), Account Name diubah sementara lalu dikembalikan: Account Name `Depreciation Expense – Admin` (28 kar), Nilai sementara `Depreciation Expense – Admin Sementara` (38 kar) · sumber turunan penulis
- **DU-112-8** Account (dicoba), Account Name untuk akun yang sudah terhapus: Account Name `Depreciation Expense – Admin Terhapus` (37 kar) · sumber turunan penulis
- **DU-112-9** Account (dicoba), Account Function dan Account Name untuk Save saat status kunci berubah: Account Function `Asset Cost` (10 kar), Account Name `Depreciation Expense – Admin Terkunci` (37 kar) · sumber turunan penulis
- **DU-112-10** Account (dicoba), semua field dikosongkan lewat Clear Field: Account Code `` (0 kar), Account Name `` (0 kar), Account Function `Select account function` (23 kar) · sumber turunan penulis
- **DU-112-11** Account (dicoba), Account Name untuk form Edit yang sudah diubah: Account Name `Depreciation Expense – Admin Draf` (33 kar) · sumber turunan penulis
- **DU-112-12** Account (dicoba), Account Name untuk Save dengan klik ganda: Account Name `Depreciation Expense – Admin Ganda` (34 kar) · sumber turunan penulis
- **DU-112-13** Account (dicoba), Account Name yang disimpan saat koneksi terputus: Account Name `Depreciation Expense – Admin Koneksi Putus` (42 kar) · sumber turunan penulis
- **DU-120-1** Account (awal), Akun Asset Cost dipakai 3 Asset Class, Modified By dua kata, Last Updated tanggal hari lebih dari 12: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar), Modified By `Rina Pratiwi` (12 kar), Last Updated `2026-03-25T09:15:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-2** Account (awal), Akun Accumulated Depreciation, Modified By satu kata, Last Updated dekat tengah malam: Account Code `1-2001` (6 kar), Account Name `Accumulated Depreciation – Equipment` (36 kar), Function `Accumulated Depreciation` (24 kar), Active `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `Sep 2026` (8 kar), Modified By `Budi` (4 kar), Last Updated `2026-03-24T23:30:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-3** Account (awal), Akun Depreciation Expense tanpa pemakaian dan belum pernah diekspor, Modified By tiga kata: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Function `Depreciation Expense` (20 kar), Active `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `null` (4 kar), Modified By `Alexander Graham Bell` (21 kar), Last Updated `2026-03-10T08:05:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-4** Account (awal), Akun Gain on Disposal Inactive dengan Last Used in Journal null, nama mirip pertama: Account Code `4-7001` (6 kar), Account Name `Gain on Disposal` (16 kar), Function `Gain on Disposal` (16 kar), Active `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `null` (4 kar), Modified By `Dewi Anggraini` (14 kar), Last Updated `2026-02-05T10:00:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-5** Account (awal), Akun Loss on Disposal, nama mirip kedua: Account Code `4-7002` (6 kar), Account Name `Gain and Loss on Disposal` (25 kar), Function `Loss on Disposal` (16 kar), Active `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `Jul 2026` (8 kar), Modified By `Dewi Anggreni` (13 kar), Last Updated `2026-02-12T13:20:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-6** Account (awal), Akun Capitalization Offset belum pernah diekspor dan tanpa entri Changelog, Modified By System: Account Code `6-2001` (6 kar), Account Name `Repairs & Maintenance Expense` (29 kar), Function `Capitalization Offset` (21 kar), Active `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `null` (4 kar), Modified By `System` (6 kar), Last Updated `2026-02-15T07:40:00Z` (20 kar) · sumber PRD §4.1.1 Example Data
- **DU-120-7** Account (awal), Akun Disposal Proceeds dengan Last Used in Journal string kosong, nama panjang: Account Code `1-3001` (6 kar), Account Name `Disposal Proceeds – Clearing` (28 kar), Function `Disposal Proceeds` (17 kar), Active `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `` (0 kar), Modified By `Buzzlightyear Sumardi` (21 kar), Last Updated `2026-01-20T16:45:00Z` (20 kar) · sumber turunan penulis
- **DU-120-8** Account (awal), Akun dengan Account Name panjang dan nilai berbeda di setiap kolom: Account Code `5-6002` (6 kar), Account Name `Regional Procurement and Vendor Management Office Jakarta` (57 kar), Function `Depreciation Expense` (20 kar), Active `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `Jun 2026` (8 kar), Modified By `Siti Nurbaya` (12 kar), Last Updated `2026-01-15T11:10:00Z` (20 kar) · sumber turunan penulis
- **DU-120-9** Account (awal), Akun dengan Account Name tersimpan ber-markup: Account Code `9-0001` (6 kar), Account Name `<b>Kas Besar</b>` (16 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `null` (4 kar), Modified By `Rina Pratiwi` (12 kar), Last Updated `2026-01-05T09:00:00Z` (20 kar) · sumber turunan penulis
- **DU-121-1** Account (awal), Akun terakhir yang dihapus sehingga daftar menjadi kosong: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Function `Depreciation Expense` (20 kar), Active `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `null` (4 kar) · sumber PRD §4.1.1 Example Data
- **DU-121-2** Account (awal), Daftar akun kosong: Jumlah Account `0` (1 kar) · sumber turunan penulis
- **DU-121-3** Account (awal), Akun tunggal pada daftar yang dicari tanpa hasil: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-121-4** Search (dicoba), Kata kunci Search yang tidak cocok dengan akun mana pun: Search `Zxqv Tidak Ada` (14 kar) · sumber turunan penulis
- **DU-122-1** Account (awal; 101 record), Volume 101 akun untuk uji ukuran halaman dan batas maksimum: Account Code `7-{n}` (5 kar), Account Name `Akun Uji {n}` (12 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §5 Global Table Rules (paginasi 10 / 25 / 50 / 100)
- **DU-122-2** Account (awal; 10 record), Tepat 10 akun, sebanyak ukuran halaman bawaan: Account Code `8-{n}` (5 kar), Account Name `Akun Pas {n}` (12 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §5 Global Table Rules (paginasi 10 / 25 / 50 / 100)
- **DU-122-3** Account (awal; 11 record), 11 akun, satu baris di halaman terakhir pada ukuran halaman 10: Account Code `9-{n}` (5 kar), Account Name `Akun Sisa {n}` (13 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber PRD §5 Global Table Rules (paginasi 10 / 25 / 50 / 100)
- **DU-122-4** Account (awal; 30 record), 30 akun Kas Cabang yang cocok dengan kata kunci Search sehingga hasil tersaring lebih dari satu halaman: Account Code `5-{n}` (5 kar), Account Name `Kas Cabang {n}` (14 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-122-5** Account (awal; 20 record), 20 akun Bank Cabang yang tidak cocok dengan kata kunci Search: Account Code `1-{n}` (5 kar), Account Name `Bank Cabang {n}` (15 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-122-6** Halaman (dicoba), Nomor halaman tidak valid pada tabel 101 akun berukuran halaman 10 (11 halaman): Nomor halaman bukan angka `abc` (3 kar), Nomor halaman nol `0` (1 kar), Nomor halaman negatif `-1` (2 kar), Nomor halaman terakhir ditambah satu `12` (2 kar) · sumber foundation prd-conventions.md §9.18
- **DU-122-7** Search (dicoba), Kata kunci Search yang cocok dengan Account Name Kas Cabang: Search `Kas Cabang` (10 kar) · sumber turunan penulis
- **DU-123-1** Account (awal), Akun Asset Cost, satu dari tujuh nilai Function berbeda: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `3` (1 kar), Modified By `Rina Pratiwi` (12 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-2** Account (awal), Akun Accumulated Depreciation: Account Code `1-2001` (6 kar), Account Name `Accumulated Depreciation – Equipment` (36 kar), Function `Accumulated Depreciation` (24 kar), Active `Active` (6 kar), Used By `2` (1 kar), Modified By `Budi` (4 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-3** Account (awal), Akun Depreciation Expense: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Function `Depreciation Expense` (20 kar), Active `Active` (6 kar), Used By `0` (1 kar), Modified By `Rina Pratiwi` (12 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-4** Account (awal), Akun Gain on Disposal berstatus Inactive: Account Code `4-7001` (6 kar), Account Name `Gain on Disposal` (16 kar), Function `Gain on Disposal` (16 kar), Active `Inactive` (8 kar), Used By `0` (1 kar), Modified By `Budi` (4 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-5** Account (awal), Akun Loss on Disposal: Account Code `4-7002` (6 kar), Account Name `Gain and Loss on Disposal` (25 kar), Function `Loss on Disposal` (16 kar), Active `Active` (6 kar), Used By `2` (1 kar), Modified By `Rina Pratiwi` (12 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-6** Account (awal), Akun Capitalization Offset: Account Code `6-2001` (6 kar), Account Name `Repairs & Maintenance Expense` (29 kar), Function `Capitalization Offset` (21 kar), Active `Active` (6 kar), Used By `0` (1 kar), Modified By `Budi` (4 kar) · sumber PRD §4.1.1 Example Data
- **DU-123-7** Account (awal), Akun Disposal Proceeds: Account Code `1-3001` (6 kar), Account Name `Disposal Proceeds – Clearing` (28 kar), Function `Disposal Proceeds` (17 kar), Active `Active` (6 kar), Used By `1` (1 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-123-8** Account (awal), Daftar akun kosong sebagai sumber opsi filter: Jumlah Account `0` (1 kar) · sumber turunan penulis
- **DU-123-9** Filter (dicoba), Kata cari di dalam dropdown Function: substring, beda kapital, tanpa hasil: Kata cari substring `Dep` (3 kar), Kata cari beda kapital `asset cost` (10 kar), Kata cari tanpa hasil `Zzz` (3 kar) · sumber turunan penulis
- **DU-124-1** Account (awal), Akun tunggal sebagai baris pratinjau Setup Column: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-124-2** Changelog (awal), Entri Changelog agar tabel modal Changelog memiliki baris: Action `Edit` (4 kar), Account Code `1-1001` (6 kar), Field `Account Name` (12 kar), Old Value `Fixed Asset Equipment` (21 kar), New Value `Fixed Assets – Equipment` (24 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-125-1** Account (awal; 12 record), 12 akun Active untuk seleksi satu baris, banyak baris, satu halaman penuh, dan lintas halaman: Account Code `A-{n}` (5 kar), Account Name `Akun Aktif {n}` (14 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber turunan penulis
- **DU-125-2** Account (awal; 3 record), 3 akun Inactive untuk seleksi homogen Inactive dan seleksi campuran: Account Code `I-{n}` (5 kar), Account Name `Akun Nonaktif {n}` (17 kar), Function `Asset Cost` (10 kar), Active `Inactive` (8 kar) · sumber turunan penulis
- **DU-125-3** Account (awal; 999 record), 999 akun, tepat satu di bawah Selection Limit: Account Code `L-{n}` (5 kar), Account Name `Akun Batas {n}` (14 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber foundation prd-conventions.md §8
- **DU-125-4** Account (awal; 1000 record), 1.000 akun, tepat sebanyak Selection Limit: Account Code `M-{n}` (5 kar), Account Name `Akun Pas Batas {n}` (18 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber foundation prd-conventions.md §8
- **DU-125-5** Account (awal; 1001 record), 1.001 akun, satu di atas Selection Limit: Account Code `N-{n}` (5 kar), Account Name `Akun Lebih Batas {n}` (20 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber foundation prd-conventions.md §8
- **DU-125-6** Account (awal; 1200 record), 1.200 akun yang cocok dengan Search sehingga hasil tersaring melebihi Selection Limit: Account Code `P-{n}` (5 kar), Account Name `Cabang Besar {n}` (16 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber turunan penulis
- **DU-125-7** Account (awal; 300 record), 300 akun yang tidak cocok dengan Search: Account Code `Q-{n}` (5 kar), Account Name `Cabang Kecil {n}` (16 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar) · sumber turunan penulis
- **DU-125-8** Search (dicoba), Kata kunci Search untuk menyaring akun Inactive dan akun Cabang Besar: Search Inactive `Nonaktif` (8 kar), Search Cabang `Cabang Besar` (12 kar) · sumber turunan penulis
- **DU-125-9** Account (awal; 2 record), 2 akun Active yang dipakai Asset Class sehingga Bulk Deactivate diblokir seluruhnya: Account Code `U-{n}` (5 kar), Account Name `Akun Terpakai {n}` (17 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `2` (1 kar) · sumber turunan penulis
- **DU-126-1** Account (awal), Akun Active tanpa pemakaian Asset Class agar Deactivate lolos guard: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-126-2** Account (awal), Akun Inactive untuk switch Off dan Activate: Account Code `1-2001` (6 kar), Account Name `Accumulated Depreciation – Equipment` (36 kar), Function `Asset Cost` (10 kar), Active `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-127-1** Account (awal), Akun Active yang lolos guard Deactivate dan Delete: Account Code `5-1001` (6 kar), Account Name `Kas Operasional` (15 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-127-2** Account (awal), Akun Active kedua yang lolos guard untuk seleksi bulk: Account Code `5-1002` (6 kar), Account Name `Bank Operasional` (16 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-127-3** Account (awal), Akun Inactive untuk Activate single dan bulk: Account Code `6-1001` (6 kar), Account Name `Beban Sewa` (10 kar), Function `Asset Cost` (10 kar), Active `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-127-4** Account (awal), Akun Inactive kedua untuk Activate bulk: Account Code `6-1002` (6 kar), Account Name `Beban Listrik` (13 kar), Function `Asset Cost` (10 kar), Active `Inactive` (8 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-127-5** Account (awal), Akun Active yang dipakai Asset Class sehingga dilewati pada Bulk Deactivate dan Bulk Delete: Account Code `7-1001` (6 kar), Account Name `Persediaan` (10 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `2` (1 kar) · sumber turunan penulis
- **DU-127-6** Account (awal), Akun yang pernah dipakai di jurnal sehingga dilewati pada Bulk Delete: Account Code `8-1001` (6 kar), Account Name `Pendapatan Jasa` (15 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber turunan penulis
- **DU-128-1** Account (awal; 3 record), 3 akun untuk popover Download dan gagal unduh: Account Code `D-{n}` (5 kar), Account Name `Akun Unduh {n}` (14 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-128-2** Account (awal; 4999 record), 4.999 akun, satu di bawah ambang Download 5.000 baris: Account Code `E-{n}` (5 kar), Account Name `Akun Di Bawah Ambang {n}` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation error-handling-convention.md §10.1
- **DU-128-3** Account (awal; 5000 record), 5.000 akun, tepat di ambang Download: Account Code `F-{n}` (5 kar), Account Name `Akun Tepat Ambang {n}` (21 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation error-handling-convention.md §10.1
- **DU-128-4** Account (awal; 5001 record), 5.001 akun, satu di atas ambang Download: Account Code `G-{n}` (5 kar), Account Name `Akun Lebih Ambang {n}` (21 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation error-handling-convention.md §10.1
- **DU-129-1** Account (awal; 999 record), 999 akun, tepat satu di bawah Master Data Count Limit 1000: Account Code `H-{n}` (5 kar), Account Name `Akun Batas {n}` (14 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation prd-conventions.md §8 (nilai kanonik plans-licensing-lifecycle-settings §9.9)
- **DU-129-2** Account (awal; 1000 record), 1000 akun, tepat sebanyak Master Data Count Limit: Account Code `J-{n}` (5 kar), Account Name `Akun Pas Batas {n}` (18 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation prd-conventions.md §8 (nilai kanonik plans-licensing-lifecycle-settings §9.9)
- **DU-129-3** Account (awal; 1001 record), 1001 akun, satu di atas Master Data Count Limit karena limit diturunkan: Account Code `K-{n}` (5 kar), Account Name `Akun Lebih Batas {n}` (20 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `0` (1 kar) · sumber foundation prd-conventions.md §8 (nilai kanonik plans-licensing-lifecycle-settings §9.9)
- **DU-130-1** Account (awal), Akun tunggal agar header kolom dan toolbar yang disorot tampil: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Function `Asset Cost` (10 kar), Active `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-130-2** Viewport (dicoba), Ukuran jendela baru untuk memicu penutupan tur saat resize: Ukuran jendela `1024 x 768` (10 kar) · sumber turunan penulis
- **DU-135-1** Changelog (awal), Entri Create untuk Old Value kosong dan Modified By dengan nama belakang: Date `2026-03-25T09:15:00Z` (20 kar), Action `Create` (6 kar), Account Code `1-1001` (6 kar), Field `Account Code` (12 kar), Old Value `None` (4 kar), New Value `1-1001` (6 kar), Modified By `Rina Pratiwi` (12 kar), Date tampil dd/MM/yy `25/03/26, 09:15` (15 kar), Date tampil dd MMM yy `25 Mar 26, 09:15` (16 kar) · sumber turunan penulis
- **DU-135-2** Changelog (awal), Entri Edit nama akun: Date `2026-03-26T10:30:00Z` (20 kar), Action `Edit` (4 kar), Account Code `1-1001` (6 kar), Field `Account Name` (12 kar), Old Value `Fixed Asset Equipment` (21 kar), New Value `Fixed Assets – Equipment` (24 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-135-3** Changelog (awal), Entri Edit Status dengan Modified By satu kata: Date `2026-03-27T23:30:00Z` (20 kar), Action `Edit` (4 kar), Account Code `1-1001` (6 kar), Field `Status` (6 kar), Old Value `Active` (6 kar), New Value `Inactive` (8 kar), Modified By `Budi` (4 kar) · sumber turunan penulis
- **DU-135-4** Changelog (awal), Entri Delete untuk New Value kosong dan Modified By tiga kata: Date `2026-03-28T08:05:00Z` (20 kar), Action `Delete` (6 kar), Account Code `4-7001` (6 kar), Field `Account Code` (12 kar), Old Value `4-7001` (6 kar), New Value `None` (4 kar), Modified By `Alexander Graham Bell` (21 kar) · sumber turunan penulis
- **DU-135-5** Changelog (dicoba), Entri Edit dengan teks bermarkup di Old Value dan New Value: Date `2026-03-29T07:45:00Z` (20 kar), Action `Edit` (4 kar), Account Code `9-0001` (6 kar), Field `Account Name` (12 kar), Old Value `<b>Kas</b>` (10 kar), New Value `<b>Kas Besar</b>` (16 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-135-6** Changelog (awal), Daftar entri Changelog kosong: Jumlah entri `0` (1 kar) · sumber turunan penulis
- **DU-135-7** Search (dicoba), Kata kunci Search yang tidak cocok dengan entri mana pun: Search `Zxqv Tidak Ada` (14 kar) · sumber turunan penulis
- **DU-136-1** Changelog (awal), Entri Create untuk opsi Action Create dan Account Code 1-1001: Action `Create` (6 kar), Account Code `1-1001` (6 kar), Field `Account Code` (12 kar), Old Value `None` (4 kar), New Value `1-1001` (6 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-2** Changelog (awal), Entri Edit nama akun: Action `Edit` (4 kar), Account Code `1-2001` (6 kar), Field `Account Name` (12 kar), Old Value `Accumulated Depreciation` (24 kar), New Value `Accumulated Depreciation – Equipment` (36 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-3** Changelog (awal), Entri Edit Status oleh Budi: Action `Edit` (4 kar), Account Code `1-3001` (6 kar), Field `Status` (6 kar), Old Value `Active` (6 kar), New Value `Inactive` (8 kar), Modified By `Budi` (4 kar) · sumber turunan penulis
- **DU-136-4** Changelog (awal), Entri Delete untuk opsi Action Delete: Action `Delete` (6 kar), Account Code `4-7001` (6 kar), Field `Account Code` (12 kar), Old Value `4-7001` (6 kar), New Value `None` (4 kar), Modified By `Alexander Graham Bell` (21 kar) · sumber turunan penulis
- **DU-136-5** Changelog (awal), Entri Edit nama akun oleh Budi: Action `Edit` (4 kar), Account Code `4-7002` (6 kar), Field `Account Name` (12 kar), Old Value `Gain Loss` (9 kar), New Value `Gain and Loss on Disposal` (25 kar), Modified By `Budi` (4 kar) · sumber turunan penulis
- **DU-136-6** Changelog (awal), Entri Edit Account Function: Action `Edit` (4 kar), Account Code `5-6001` (6 kar), Field `Account Function` (16 kar), Old Value `Asset Cost` (10 kar), New Value `Depreciation Expense` (20 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-7** Changelog (awal), Entri Edit Status Inactive ke Active: Action `Edit` (4 kar), Account Code `6-2001` (6 kar), Field `Status` (6 kar), Old Value `Inactive` (8 kar), New Value `Active` (6 kar), Modified By `Budi` (4 kar) · sumber turunan penulis
- **DU-136-8** Changelog (awal), Entri Edit Last Used in Journal: Action `Edit` (4 kar), Account Code `9-0001` (6 kar), Field `Last Used in Journal` (20 kar), Old Value `None` (4 kar), New Value `Aug 2026` (8 kar), Modified By `Alexander Graham Bell` (21 kar) · sumber turunan penulis
- **DU-136-9** Changelog (awal; 101 record), 101 entri Edit untuk 11 halaman pada ukuran halaman 10: Action `Edit` (4 kar), Account Code `7-{n}` (5 kar), Field `Account Name` (12 kar), Old Value `Akun Lama {n}` (13 kar), New Value `Akun Uji {n}` (12 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-10** Changelog (awal; 30 record), 30 entri yang cocok dengan Search Kas Cabang; entri New Value Kas Cabang 1 adalah entri terbaru dari seluruh daftar: Action `Edit` (4 kar), Account Code `8-{n}` (5 kar), Field `Account Name` (12 kar), Old Value `Kas Lama {n}` (12 kar), New Value `Kas Cabang {n}` (14 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-11** Changelog (awal; 20 record), 20 entri yang tidak cocok dengan Search Kas Cabang; entri New Value Bank Cabang 1 adalah entri terbaru kedua, tepat sesudah Kas Cabang 1: Action `Edit` (4 kar), Account Code `3-{n}` (5 kar), Field `Account Name` (12 kar), Old Value `Bank Lama {n}` (13 kar), New Value `Bank Cabang {n}` (15 kar), Modified By `Rina Pratiwi` (12 kar) · sumber turunan penulis
- **DU-136-12** Changelog (awal), Daftar entri Changelog kosong: Jumlah entri `0` (1 kar) · sumber turunan penulis
- **DU-136-13** Nomor halaman (dicoba), Nomor halaman yang diketik pada input Jump to page: Nomor halaman bukan angka `abc` (3 kar), Nomor halaman nol `0` (1 kar), Nomor halaman negatif `-1` (2 kar), Nomor halaman melebihi halaman terakhir `12` (2 kar) · sumber foundation prd-conventions.md §9.18
- **DU-136-14** Search (dicoba), Kata kunci Search yang hanya cocok dengan entri Kas Cabang: Search `Kas Cabang` (10 kar) · sumber turunan penulis
- **DU-136-15** Search (dicoba), Kata cari di dalam dropdown Modified By: Substring `bu` (2 kar), Beda kapital `RINA` (4 kar), Tanpa hasil `Zzz` (3 kar) · sumber turunan penulis
- **DU-140-1** Account (awal), Akun dengan tiga Asset Class pemakai: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Account Function `Asset Cost` (10 kar), Used By `3` (1 kar) · sumber PRD §4.1.4 Example Data
- **DU-140-2** Asset Class pemakai (awal), Asset Class dengan banyak Asset Name: Asset Class Name `Heavy Equipment` (15 kar), Asset Name Count `12` (2 kar) · sumber PRD §4.1.4 Example Data
- **DU-140-3** Asset Class pemakai (awal), Asset Class dengan satu Asset Name: Asset Class Name `Office Equipment` (16 kar), Asset Name Count `1` (1 kar) · sumber PRD §4.1.4 Example Data
- **DU-140-4** Asset Class pemakai (awal), Asset Class tanpa Asset Name: Asset Class Name `Vehicles` (8 kar), Asset Name Count `0` (1 kar) · sumber PRD §4.1.4 Example Data
- **DU-141-1** Account (awal), Depreciation Expense – Admin: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-141-2** Account (awal), Depreciation Expense – Warehouse: Account Code `5-6002` (6 kar), Account Name `Depreciation Expense – Warehouse` (32 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-141-3** Account (awal), Depreciation Expense – Branch: Account Code `5-6003` (6 kar), Account Name `Depreciation Expense – Branch` (29 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-142-1** Account (awal), Depreciation Expense – Warehouse: Account Code `5-6002` (6 kar), Account Name `Depreciation Expense – Warehouse` (32 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-142-2** Account (awal), Depreciation Expense – Branch: Account Code `5-6003` (6 kar), Account Name `Depreciation Expense – Branch` (29 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar) · sumber turunan penulis
- **DU-143-1** Account (awal), Repairs & Maintenance Expense: Account Code `6-2001` (6 kar), Account Name `Repairs & Maintenance Expense` (29 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `Aug 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-143-2** Account (awal), Fixed Assets – Equipment: Account Code `1-1001` (6 kar), Account Name `Fixed Assets – Equipment` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `3` (1 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-143-3** Account (awal), Accumulated Depreciation – Vehicles: Account Code `1-2002` (6 kar), Account Name `Accumulated Depreciation – Vehicles` (35 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `Sep 2026` (8 kar) · sumber turunan penulis
- **DU-143-4** Account (awal), Equipment – Legacy Code: Account Code `1-1002` (6 kar), Account Name `Equipment – Legacy Code` (23 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `Mar 2025` (8 kar) · sumber PRD §4.1.1 Example Data
- **DU-143-5** Account (awal), Depreciation Expense – Admin: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-144-1** Account (awal), Gain on Disposal – Machinery: Account Code `4-7003` (6 kar), Account Name `Gain on Disposal – Machinery` (28 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Setting default company `Default Gain on Disposal` (24 kar) · sumber turunan penulis
- **DU-144-2** Account (awal), Gain and Loss on Disposal – Vehicles: Account Code `4-7004` (6 kar), Account Name `Gain and Loss on Disposal – Vehicles` (36 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `—` (1 kar), Setting default company `Default Gain on Disposal, Default Loss on Disposal` (50 kar) · sumber turunan penulis
- **DU-144-3** Account (awal), Capitalization Offset – Repairs: Account Code `6-2003` (6 kar), Account Name `Capitalization Offset – Repairs` (31 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar), Setting default company `Default Capitalization Offset` (29 kar) · sumber turunan penulis
- **DU-144-4** Account (awal), Depreciation Expense – Admin: Account Code `5-6001` (6 kar), Account Name `Depreciation Expense – Admin` (28 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `—` (1 kar) · sumber PRD §4.1.1 Example Data
- **DU-145-1** Select akun konsumen (awal), Field asal yang menentukan Account Function: Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-150-1** Account (awal), akun pembanding sudah ada di client aktor: Account Code `KAS-{runId}` (11 kar), Account Name `Kas Operasional {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-150-2** Account (dicoba), Code sama persis dengan akun yang ada: Account Code `KAS-{runId}` (11 kar), Account Name `Kas Kecil {runId}` (17 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-150-3** Account (dicoba), Code hanya beda huruf besar-kecil: Account Code `kas-{runId}` (11 kar), Account Name `Kas Kecil Dua {runId}` (21 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-150-4** Account (dicoba), Code sama setelah trim: Account Code ` KAS-{runId} ` (13 kar), Account Name `Kas Kecil Tiga {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-150-5** Account (awal), akun dengan Code yang sama di client lain: Account Code `PTG-{runId}` (11 kar), Account Name `Piutang Usaha Cabang {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-150-6** Account (dibuat), Code sama dengan akun client lain, dibuat di client aktor: Account Code `PTG-{runId}` (11 kar), Account Name `Piutang Usaha Pusat {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-150-7** Account (dibuat), Code dengan spasi di awal dan akhir: Account Code ` TRM-{runId} ` (13 kar), Account Name `Kas Bank {runId}` (16 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-8** Account (dibuat), Name dengan spasi di awal dan akhir serta spasi tunggal di tengah: Account Code `LST-{runId}` (11 kar), Account Name `  Beban Listrik Kantor {runId}  ` (32 kar), Account Function `Depreciation Expense` (20 kar) · sumber foundation prd-conventions.md §4
- **DU-150-9** Account (dibuat), Code tepat 15 karakter: Account Code `BE150-LIMIT-A15` (15 kar), Account Name `Batas Code Lima Belas {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber V-02
- **DU-150-10** Account (dibuat), Code 15 karakter setelah trim dengan spasi tepi: Account Code ` BE150-TRIMM-B15 ` (17 kar), Account Name `Batas Setelah Trim {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-11** Account (dicoba), Code 16 karakter, satu di atas batas: Account Code `BE150-LIMIT-A16X` (16 kar), Account Name `Batas Code Enam Belas {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber V-02
- **DU-150-12** Account (dibuat), Name tepat 120 karakter: Account Code `NM120-{runId}` (13 kar), Account Name `Akumulasi Penyusutan Peralatan Kantor Cabang Utama Wilayah Jakarta Selatan Periode Tahunan Dua Ribu Dua Puluh Enam Final` (120 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber V-06
- **DU-150-13** Account (dicoba), Name 121 karakter, satu di atas batas: Account Code `NM121-{runId}` (13 kar), Account Name `Akumulasi Penyusutan Peralatan Kantor Cabang Utama Wilayah Jakarta Selatan Periode Tahunan Dua Ribu Dua Puluh Enam Revisi` (121 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber V-06
- **DU-150-14** Account (dicoba), Code memuat karakter di luar whitelist: Account Code `AKUN#{runId}` (12 kar), Account Name `Akun Karakter Khusus {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-150-15** Account (dicoba), Name memuat emoji: Account Code `EMJ-{runId}` (11 kar), Account Name `Kas 😊 {runId}` (13 kar), Account Function `Asset Cost` (10 kar) · sumber V-07
- **DU-150-16** Account (dicoba), Code kosong: Account Name `Akun Tanpa Code {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber V-01
- **DU-150-17** Account (dicoba), Name kosong: Account Code `NMK-{runId}` (11 kar), Account Function `Asset Cost` (10 kar) · sumber V-05
- **DU-150-18** Account (dicoba), Function kosong: Account Code `FNK-{runId}` (11 kar), Account Name `Akun Tanpa Function {runId}` (27 kar) · sumber V-08
- **DU-150-19** Account (dicoba), Name hanya berisi tiga spasi: Account Code `SPS-{runId}` (11 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-01] Create Account#r4
- **DU-150-20** Account (dibuat), akun ber-function Gain on Disposal: Account Code `FGD-{runId}` (11 kar), Account Name `Keuntungan Pelepasan Aset {runId}` (33 kar), Account Function `Gain on Disposal` (16 kar) · sumber FACO-LOGIC-01a
- **DU-150-21** Account (dibuat), akun ber-function Loss on Disposal: Account Code `FLD-{runId}` (11 kar), Account Name `Kerugian Pelepasan Aset {runId}` (31 kar), Account Function `Loss on Disposal` (16 kar) · sumber FACO-LOGIC-01a
- **DU-150-22** Account (dibuat), akun ber-function Capitalization Offset: Account Code `FCO-{runId}` (11 kar), Account Name `Beban Perbaikan Dikapitalisasi {runId}` (38 kar), Account Function `Capitalization Offset` (21 kar) · sumber FACO-LOGIC-01a
- **DU-150-23** Account (dibuat), akun ber-function Disposal Proceeds: Account Code `FDP-{runId}` (11 kar), Account Name `Kliring Hasil Pelepasan {runId}` (31 kar), Account Function `Disposal Proceeds` (17 kar) · sumber FACO-LOGIC-01a
- **DU-150-24** Account (dibuat), Name berisi payload XSS: Account Code `XSS-{runId}` (11 kar), Account Name `<script>alert(1)</script> {runId}` (33 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-25** Account (dibuat), Name berisi payload SQL injection: Account Code `SQL-{runId}` (11 kar), Account Name `' OR '1'='1 {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-26** Account (dibuat), Name berisi payload NoSQL injection: Account Code `NSQ-{runId}` (11 kar), Account Name `{"$ne": null} {runId}` (21 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-27** Account (dibuat), Name berisi markup HTML: Account Code `MRK-{runId}` (11 kar), Account Name `<b>Kas Kecil</b> {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-150-28** Account (dibuat), Code yang sama dikirim serentak oleh dua admin: Account Code `SRN-{runId}` (11 kar), Account Name `Kas Serentak {runId}` (20 kar), Account Function `Asset Cost` (10 kar) · sumber EB-CON-2
- **DU-150-29** Account (dibuat), Code ber-garis-bawah yang diizinkan whitelist: Account Code `BNK_{runId}` (11 kar), Account Name `Rekening Bank Operasional {runId}` (33 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-150-30** Account (dibuat), Code bertitik yang diizinkan whitelist: Account Code `BNK.{runId}` (11 kar), Account Name `Rekening Bank Cadangan {runId}` (30 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-150-31** Account (dicoba), Create langsung yang membawa Last Used in Journal: Account Code `LUJ-{runId}` (11 kar), Account Name `Kas Periode Jurnal {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber FACO-LOGIC-07d
- **DU-150-32** Account (dibuat), akun baru dari Create tanpa Last Used in Journal: Account Code `LUK-{runId}` (11 kar), Account Name `Kas Tanpa Periode {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber FACO-LOGIC-07d
- **DU-151-1** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit nilai baru: Account Code `SWA-{runId}` (11 kar), Account Name `Beban Sewa Kantor {runId}` (25 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-151-2** Account (dibuat), nilai baru hasil Edit pada ketiga field: Account Code `SWB-{runId}` (11 kar), Account Name `Beban Sewa Gedung {runId}` (25 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber F-FACO-02
- **DU-151-3** Account (awal), akun untuk Edit tanpa perubahan: Account Code `NOP-{runId}` (11 kar), Account Name `Kas Kecil Pusat {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber F-FACO-02
- **DU-151-4** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit Code hanya beda huruf besar-kecil: Account Code `KDB-{runId}` (11 kar), Account Name `Kas di Bank {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-5** Account (dibuat), Code hanya beda huruf besar-kecil dari nilai tersimpan: Account Code `kdb-{runId}` (11 kar), Account Name `Kas di Bank {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber §8#b1
- **DU-151-6** Account (awal), akun untuk Edit Name hanya beda spasi tepi: Account Code `SPT-{runId}` (11 kar), Account Name `Kas Cabang {runId}` (18 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-7** Account (dibuat), Name sama dengan nilai tersimpan, hanya ditambah spasi di awal dan akhir: Account Code `SPT-{runId}` (11 kar), Account Name ` Kas Cabang {runId} ` (20 kar), Account Function `Asset Cost` (10 kar) · sumber foundation prd-conventions.md §4
- **DU-151-8** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit perubahan nyata ditambah huruf besar-kecil: Account Code `NPK-{runId}` (11 kar), Account Name `Beban Gaji {runId}` (18 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-151-9** Account (dibuat), Name berubah nyata dan Code hanya beda huruf besar-kecil: Account Code `npk-{runId}` (11 kar), Account Name `Beban Gaji Karyawan {runId}` (27 kar), Account Function `Depreciation Expense` (20 kar) · sumber §8#b1
- **DU-151-10** Account (awal), akun pembanding untuk uji duplikat Code: Account Code `REF-{runId}` (11 kar), Account Name `Rekening Referensi {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-11** Account (awal), akun yang Edit-nya ditolak: Account Code `EDD-{runId}` (11 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-12** Account (dicoba), Code sama persis dengan akun lain: Account Code `REF-{runId}` (11 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-13** Account (dicoba), Code hanya beda huruf besar-kecil dari akun lain: Account Code `ref-{runId}` (11 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-14** Account (dicoba), Code sama dengan akun lain setelah trim: Account Code ` REF-{runId} ` (13 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-15** Account (dicoba), Code 16 karakter, satu di atas batas: Account Code `BE151-EDITT-A16X` (16 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-02
- **DU-151-16** Account (dicoba), Code memuat karakter di luar whitelist: Account Code `EDD#{runId}` (11 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-151-17** Account (dicoba), Name 121 karakter, satu di atas batas: Account Code `EDD-{runId}` (11 kar), Account Name `Beban Pemeliharaan Kendaraan Operasional Distribusi Barang Cabang Surabaya Timur Periode Semester Pertama Tahun Berjalan.` (121 kar), Account Function `Asset Cost` (10 kar) · sumber V-06
- **DU-151-18** Account (dicoba), Name memuat emoji: Account Code `EDD-{runId}` (11 kar), Account Name `Beban 😊 {runId}` (15 kar), Account Function `Asset Cost` (10 kar) · sumber V-07
- **DU-151-19** Account (dicoba), Code dikosongkan: Account Name `Beban Dibayar Dimuka {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber V-01
- **DU-151-20** Account (dicoba), Name dikosongkan: Account Code `EDD-{runId}` (11 kar), Account Function `Asset Cost` (10 kar) · sumber V-05
- **DU-151-21** Account (dicoba), Function dikosongkan: Account Code `EDD-{runId}` (11 kar), Account Name `Beban Dibayar Dimuka {runId}` (28 kar) · sumber V-08
- **DU-151-22** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit pada batas panjang dan Code luar scope: Account Code `BDY-{runId}` (11 kar), Account Name `Beban Batas {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-23** Account (dibuat), Code tepat 15 karakter: Account Code `BE151-EDITT-A15` (15 kar), Account Name `Beban Batas {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber V-02
- **DU-151-24** Account (dibuat), Name tepat 120 karakter: Account Code `BE151-EDITT-A15` (15 kar), Account Name `Beban Pemeliharaan Kendaraan Operasional Distribusi Barang Cabang Surabaya Timur Periode Semester Pertama Tahun Berjalan` (120 kar), Account Function `Asset Cost` (10 kar) · sumber V-06
- **DU-151-25** Account (awal), akun dengan Code yang sama di client lain: Account Code `UTG-{runId}` (11 kar), Account Name `Utang Usaha Cabang {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-26** Account (dibuat), Code sama dengan akun client lain, dipakai di client aktor: Account Code `UTG-{runId}` (11 kar), Account Name `Beban Batas {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber V-04
- **DU-151-27** Account (awal), akun untuk percobaan mengisi Last Used in Journal: Account Code `LUJ-{runId}` (11 kar), Account Name `Beban Audit {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-28** Account (dicoba), permintaan Edit yang memuat Last Used in Journal: Last Used in Journal `Oct 2026` (8 kar) · sumber FACO-LOGIC-07d
- **DU-151-29** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk dua Edit serentak: Account Code `CWL-{runId}` (11 kar), Account Name `Kas Besar Awal {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-30** Account (dibuat), Name dari Edit Admin A: Account Code `CWL-{runId}` (11 kar), Account Name `Kas Besar Pusat {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber EB-CON-1
- **DU-151-31** Account (dibuat), Name dari Edit Admin B: Account Code `CWL-{runId}` (11 kar), Account Name `Kas Besar Cabang {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber EB-CON-1
- **DU-151-32** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun yang berubah oleh Admin A setelah dibaca Admin B: Account Code `STL-{runId}` (11 kar), Account Name `Piutang Karyawan {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-33** Account (dibuat), Name dari Edit Admin A: Account Code `STL-{runId}` (11 kar), Account Name `Piutang Karyawan Tetap {runId}` (30 kar), Account Function `Asset Cost` (10 kar) · sumber EB-CON-1
- **DU-151-34** Account (dibuat), Name dari Edit Admin B sesudah akun berubah: Account Code `STL-{runId}` (11 kar), Account Name `Piutang Karyawan Kontrak {runId}` (32 kar), Account Function `Asset Cost` (10 kar) · sumber EB-CON-1
- **DU-151-35** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun yang dihapus Admin A: Account Code `DLP-{runId}` (11 kar), Account Name `Beban Promosi {runId}` (21 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-36** Account (dicoba), Edit Admin B atas akun yang sudah dihapus: Account Code `DLP-{runId}` (11 kar), Account Name `Beban Promosi Digital {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber PRD §7.3
- **DU-151-37** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun yang dinonaktifkan Admin A: Account Code `STS-{runId}` (11 kar), Account Name `Beban Asuransi {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-38** Account (dibuat), Name dari Edit Admin B atas akun yang sudah Inactive: Account Code `STS-{runId}` (11 kar), Account Name `Beban Asuransi Gedung {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber F-FACO-02
- **DU-151-39** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun pertama untuk Code serentak: Account Code `CN1-{runId}` (11 kar), Account Name `Kas Proyek Satu {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-40** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun kedua untuk Code serentak: Account Code `CN2-{runId}` (11 kar), Account Name `Kas Proyek Dua {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-41** Account (dibuat), Code unik baru yang dikirim dua admin serentak: Account Code `CNC-{runId}` (11 kar), Account Name `Kas Proyek Satu {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r17
- **DU-151-42** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit Code 15 karakter setelah trim: Account Code `TRB-{runId}` (11 kar), Account Name `Batas Setelah Trim {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-43** Account (dibuat), Code 15 karakter setelah trim dengan satu spasi di awal dan akhir: Account Code ` BE151-TRIMM-B15 ` (17 kar), Account Name `Batas Setelah Trim {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-02
- **DU-151-44** Account (dicoba), Name hanya berisi tiga spasi: Account Code `EDD-{runId}` (11 kar), Account Function `Asset Cost` (10 kar) · sumber EB-FRM-8@account-name
- **DU-151-45** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk dua Edit serentak, salah satunya memakai Code akun lain: Account Code `CSM-{runId}` (11 kar), Account Name `Kas Serentak {runId}` (20 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-151-46** Account (dicoba), Edit Admin A dengan Code milik akun lain: Account Code `REF-{runId}` (11 kar), Account Name `Kas Serentak {runId}` (20 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r17
- **DU-151-47** Account (dibuat), Name dari Edit Admin B yang diterima: Account Code `CSM-{runId}` (11 kar), Account Name `Kas Serentak Baru {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r17
- **DU-151-48** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun Inactive untuk Edit serentak dengan Activate: Account Code `EAC-{runId}` (11 kar), Account Name `Kas Edit Aktivasi {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber §[F-FACO-02] Edit Account#r21
- **DU-151-49** Account (dibuat), nilai Edit Admin A atas akun yang diaktifkan Admin B serentak: Account Code `EAC-{runId}` (11 kar), Account Name `Kas Edit Aktivasi Baru {runId}` (30 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r22
- **DU-151-50** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun Active untuk Edit serentak dengan Deactivate: Account Code `EDC-{runId}` (11 kar), Account Name `Kas Edit Deaktivasi {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §[F-FACO-02] Edit Account#r21
- **DU-151-51** Account (dibuat), nilai Edit Admin A atas akun yang dinonaktifkan Admin B serentak: Account Code `EDC-{runId}` (11 kar), Account Name `Kas Edit Deaktivasi {runId}` (27 kar), Account Function `Disposal Proceeds` (17 kar) · sumber §[F-FACO-02] Edit Account#r22
- **DU-151-52** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Delete serentak dengan Edit: Account Code `DED-{runId}` (11 kar), Account Name `Kas Hapus Edit Serentak {runId}` (31 kar), Account Function `Asset Cost` (10 kar) · sumber §9.4.2#r41
- **DU-151-53** Account (dicoba), nilai Edit Admin B yang serentak dengan Delete Admin A: Account Code `DED-{runId}` (11 kar), Account Name `Kas Hapus Edit Serentak Baru {runId}` (36 kar), Account Function `Asset Cost` (10 kar) · sumber §9.4.2#r41
- **DU-151-54** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk dua Edit serentak atas banyak field: Account Code `SEQ-{runId}` (11 kar), Account Name `Kas Berurutan Awal {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r20
- **DU-151-55** Account (dibuat), nilai Edit Admin A atas Account Name dan Account Function: Account Code `SEQ-{runId}` (11 kar), Account Name `Kas Berurutan Satu {runId}` (26 kar), Account Function `Gain on Disposal` (16 kar) · sumber §[F-FACO-02] Edit Account#r20
- **DU-151-56** Account (dibuat), nilai Edit Admin B atas Account Name dan Account Function: Account Code `SEQ-{runId}` (11 kar), Account Name `Kas Berurutan Dua {runId}` (25 kar), Account Function `Loss on Disposal` (16 kar) · sumber §[F-FACO-02] Edit Account#r20
- **DU-151-57** Account (awal; dimutasi TC-FA-FACO-BE-151-validasi-edit-dan-no-op), akun untuk Edit Account Code ke nilai ber-garis-bawah dan bertitik: Account Code `WLS-{runId}` (11 kar), Account Name `Kas Whitelist Edit {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-151-58** Account (dibuat), Code hasil Edit ber-garis-bawah yang diizinkan whitelist: Account Code `WLS_{runId}` (11 kar), Account Name `Kas Whitelist Edit {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-151-59** Account (dibuat), Code hasil Edit bertitik yang diizinkan whitelist: Account Code `WLS.{runId}` (11 kar), Account Name `Kas Whitelist Edit {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber V-03
- **DU-152-1** User (awal), aktor Total Control: Name `Budi Total {runId}` (18 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-152-2** User (awal), aktor Read Only: Name `Rina ReadOnly {runId}` (21 kar), Access Level `Read Only` (9 kar) · sumber matriks role PRD
- **DU-152-3** User (awal), aktor Manage accounting dengan semua huruf CRUD: Name `Dewi Akuntansi {runId}` (22 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Create, Update, Delete` (28 kar) · sumber matriks role PRD
- **DU-152-4** User (awal), aktor hanya Create ditambah Read: Name `Agus Pencatat {runId}` (21 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Create` (12 kar) · sumber matriks role PRD
- **DU-152-5** User (awal), aktor hanya Update ditambah Read: Name `Putri Pengubah {runId}` (22 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Update` (12 kar) · sumber matriks role PRD
- **DU-152-6** User (awal), aktor hanya Delete ditambah Read: Name `Hendra Penghapus {runId}` (24 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Delete` (12 kar) · sumber matriks role PRD
- **DU-152-7** User (awal), aktor Create dan Delete tanpa Update: Name `Joko Pencatat Penghapus {runId}` (31 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Create, Delete` (20 kar) · sumber matriks role PRD
- **DU-152-8** User (awal), aktor Update dan Delete tanpa Create: Name `Sari Pengubah Penghapus {runId}` (31 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Update, Delete` (20 kar) · sumber matriks role PRD
- **DU-152-9** User (awal), aktor Create dan Update tanpa Delete: Name `Tono Pencatat Pengubah {runId}` (30 kar), Global Role `Manage accounting` (17 kar), Capability `Read, Create, Update` (20 kar) · sumber matriks role PRD
- **DU-152-10** User (awal), aktor Group Manager tanpa Manage accounting: Name `Gilang Manajer {runId}` (22 kar), Access Level `Group Manager` (13 kar) · sumber matriks role PRD
- **DU-152-11** Account (awal), akun sasaran aksi tulis yang ditolak: Account Code `OTR-{runId}` (11 kar), Account Name `Kas Otorisasi {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-152-12** Account (awal), akun Inactive sasaran Activate yang ditolak: Account Code `OTI-{runId}` (11 kar), Account Name `Kas Nonaktif Otorisasi {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-152-13** Account (awal), akun milik client lain: Account Code `OTL-{runId}` (11 kar), Account Name `Kas Client Lain {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-14** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Edit Total Control: Account Code `EDT1-{runId}` (12 kar), Account Name `Beban Listrik {runId}` (21 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-15** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Activate Total Control: Account Code `ACT1-{runId}` (12 kar), Account Name `Kas Nonaktif Satu {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-152-16** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Deactivate Total Control: Account Code `DCT1-{runId}` (12 kar), Account Name `Kas Aktif Satu {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-152-17** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang dihapus Total Control: Account Code `DEL1-{runId}` (12 kar), Account Name `Kas Hapus Satu {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-18** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Edit aktor Manage accounting: Account Code `EDT3-{runId}` (12 kar), Account Name `Beban Air {runId}` (17 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-19** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Deactivate aktor Manage accounting: Account Code `DCT3-{runId}` (12 kar), Account Name `Kas Aktif Tiga {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-152-20** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang dihapus aktor Manage accounting: Account Code `DEL3-{runId}` (12 kar), Account Name `Kas Hapus Tiga {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-21** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Edit aktor Update saja: Account Code `EDT5-{runId}` (12 kar), Account Name `Beban Telepon {runId}` (21 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-22** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang di-Activate aktor Update saja: Account Code `ACT5-{runId}` (12 kar), Account Name `Kas Nonaktif Lima {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-152-23** Account (awal; dimutasi TC-FA-FACO-BE-152-otorisasi-capability), akun yang dihapus aktor Delete saja: Account Code `DEL6-{runId}` (12 kar), Account Name `Kas Hapus Enam {runId}` (22 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-24** Account (dibuat), akun yang dibuat Total Control: Account Code `CRT1-{runId}` (12 kar), Account Name `Kas Dibuat Total Control {runId}` (32 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-25** Account (dibuat), akun yang dibuat aktor Manage accounting: Account Code `CRT3-{runId}` (12 kar), Account Name `Kas Dibuat Manage Accounting {runId}` (36 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-26** Account (dibuat), akun yang dibuat aktor Create saja: Account Code `CRT4-{runId}` (12 kar), Account Name `Kas Dibuat Pencatat {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-27** Account (dibuat), akun yang dibuat aktor Create dan Delete: Account Code `CRT7-{runId}` (12 kar), Account Name `Kas Dibuat Kombinasi {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-28** Account (dibuat), nilai baru Edit Total Control: Account Code `EDT1-{runId}` (12 kar), Account Name `Beban Listrik Terbaru {runId}` (29 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-29** Account (dibuat), nilai baru Edit aktor Manage accounting: Account Code `EDT3-{runId}` (12 kar), Account Name `Beban Air Terbaru {runId}` (25 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-30** Account (dibuat), nilai baru Edit aktor Update saja: Account Code `EDT5-{runId}` (12 kar), Account Name `Beban Telepon Terbaru {runId}` (29 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-152-31** Account (dicoba), Create oleh aktor tanpa capability Create: Account Code `DNY-{runId}` (11 kar), Account Name `Akun Tanpa Izin {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-152-32** Account (dicoba), Edit oleh aktor tanpa capability Update: Account Code `OTR-{runId}` (11 kar), Account Name `Nilai Ditolak {runId}` (21 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-153-1** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Inactive yang di-Activate: Account Code `AKT-{runId}` (11 kar), Account Name `Kas Akan Diaktifkan {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-2** Account (awal), akun Active yang di-Activate lagi: Account Code `ACT-{runId}` (11 kar), Account Name `Kas Sudah Aktif {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-153-3** Account (awal), akun Inactive yang di-Deactivate lagi: Account Code `NAK-{runId}` (11 kar), Account Name `Kas Sudah Nonaktif {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-4** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Inactive pertama pada seleksi bulk campuran: Account Code `BLA-{runId}` (11 kar), Account Name `Kas Bulk Satu {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-5** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Inactive kedua pada seleksi bulk campuran: Account Code `BLB-{runId}` (11 kar), Account Name `Kas Bulk Dua {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-6** Account (awal), akun Active pada seleksi bulk campuran: Account Code `BLC-{runId}` (11 kar), Account Name `Kas Bulk Tiga {runId}` (21 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-153-7** Account (awal), akun Active pertama pada seleksi bulk yang seluruhnya Active: Account Code `CAA-{runId}` (11 kar), Account Name `Kas Aktif Semua Satu {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-153-8** Account (awal), akun Active kedua pada seleksi bulk yang seluruhnya Active: Account Code `CAB-{runId}` (11 kar), Account Name `Kas Aktif Semua Dua {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-153-9** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Inactive yang di-Activate dua admin serentak: Account Code `CNA-{runId}` (11 kar), Account Name `Kas Aktivasi Serentak {runId}` (29 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-10** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Active yang di-Deactivate dua admin serentak: Account Code `CND-{runId}` (11 kar), Account Name `Kas Deaktivasi Serentak {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-153-11** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Inactive yang dihapus Admin A sebelum Activate Admin B: Account Code `DLA-{runId}` (11 kar), Account Name `Kas Dihapus Lalu Diaktifkan {runId}` (35 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-153-12** Account (awal; dimutasi TC-FA-FACO-BE-153-status-activate-deactivate), akun Active yang dihapus Admin A sebelum Deactivate Admin B: Account Code `DLD-{runId}` (11 kar), Account Name `Kas Dihapus Lalu Dinonaktifkan {runId}` (38 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-154-1** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus dan lolos kedua guard: Account Code `HDA-{runId}` (11 kar), Account Name `Beban Bunga {runId}` (19 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-154-2** Account (awal), akun pembanding yang tidak boleh terdampak: Account Code `HDB-{runId}` (11 kar), Account Name `Beban Bunga Pembanding {runId}` (30 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-154-3** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus dua kali oleh admin yang sama: Account Code `RPT-{runId}` (11 kar), Account Name `Kas Hapus Ulang {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-4** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus Admin A sebelum Delete Admin B: Account Code `OTH-{runId}` (11 kar), Account Name `Kas Hapus Admin Lain {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-5** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun pertama pada Bulk Delete: Account Code `BDA-{runId}` (11 kar), Account Name `Kas Bulk Hapus Satu {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-6** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun kedua pada Bulk Delete: Account Code `BDB-{runId}` (11 kar), Account Name `Kas Bulk Hapus Dua {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-7** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun ketiga pada Bulk Delete yang sudah dihapus Admin A: Account Code `BDC-{runId}` (11 kar), Account Name `Kas Bulk Hapus Tiga {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-8** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun pertama pada Bulk Delete yang seluruhnya sudah terhapus: Account Code `ALA-{runId}` (11 kar), Account Name `Kas Terhapus Semua Satu {runId}` (31 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-9** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun kedua pada Bulk Delete yang seluruhnya sudah terhapus: Account Code `ALB-{runId}` (11 kar), Account Name `Kas Terhapus Semua Dua {runId}` (30 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-10** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus Admin A sebelum Save Edit Admin B: Account Code `EDX-{runId}` (11 kar), Account Name `Kas Edit Terhapus {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-154-11** Account (dicoba), nilai Edit Admin B atas akun yang sudah dihapus: Account Code `EDX-{runId}` (11 kar), Account Name `Kas Edit Terlambat {runId}` (26 kar) · sumber §7.3#b4
- **DU-154-12** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun Inactive yang dihapus Admin A sebelum Activate bulk: Account Code `AVD-{runId}` (11 kar), Account Name `Kas Aktivasi Terhapus {runId}` (29 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-154-13** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun Inactive target Activate bulk yang tetap diproses: Account Code `AVE-{runId}` (11 kar), Account Name `Kas Aktivasi Target {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-154-14** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun Active yang dihapus Admin A sebelum Deactivate bulk: Account Code `DVD-{runId}` (11 kar), Account Name `Kas Deaktivasi Terhapus {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-154-15** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun Active target Deactivate bulk yang tetap diproses: Account Code `DVE-{runId}` (11 kar), Account Name `Kas Deaktivasi Target {runId}` (29 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-154-16** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus sebelum Bulk Activate/Deactivate atas seluruh pilihan: Account Code `ZAA-{runId}` (11 kar), Account Name `Kas Aktivasi Semua Terhapus Satu {runId}` (40 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber §7.3#b4
- **DU-154-17** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus sebelum Bulk Activate/Deactivate atas seluruh pilihan: Account Code `ZAB-{runId}` (11 kar), Account Name `Kas Aktivasi Semua Terhapus Dua {runId}` (39 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber §7.3#b4
- **DU-154-18** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus sebelum Bulk Activate/Deactivate atas seluruh pilihan: Account Code `ZDA-{runId}` (11 kar), Account Name `Kas Deaktivasi Semua Terhapus Satu {runId}` (42 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §7.3#b4
- **DU-154-19** Account (awal; dimutasi TC-FA-FACO-BE-154-delete-account), akun yang dihapus sebelum Bulk Activate/Deactivate atas seluruh pilihan: Account Code `ZDB-{runId}` (11 kar), Account Name `Kas Deaktivasi Semua Terhapus Dua {runId}` (41 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §7.3#b4
- **DU-155-1** User (awal), aktor yang melakukan aksi lewat UI: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-155-2** User (awal), pemanggil terotorisasi untuk request langsung: Name `Rudi Integrasi {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-155-3** Account (dibuat), akun yang dibuat dan dicatat L-01: Account Code `LG1-{runId}` (11 kar), Account Name `Beban Pemasaran {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-155-4** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang Account Name-nya diubah: Account Code `LG2-{runId}` (11 kar), Account Name `Beban Transport {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-155-5** Account (dibuat), nilai baru Account Name: Account Code `LG2-{runId}` (11 kar), Account Name `Beban Transportasi Darat {runId}` (32 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-155-6** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang Account Function-nya diubah: Account Code `LG3-{runId}` (11 kar), Account Name `Beban Penyusutan Mesin {runId}` (30 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-155-7** Account (dibuat), nilai baru Account Function: Account Code `LG3-{runId}` (11 kar), Account Name `Beban Penyusutan Mesin {runId}` (30 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber turunan penulis
- **DU-155-8** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang Account Code-nya diubah: Account Code `LG4-{runId}` (11 kar), Account Name `Kas Cabang Utara {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-155-9** Account (dibuat), nilai baru Account Code: Account Code `LG4B-{runId}` (12 kar), Account Name `Kas Cabang Utara {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-155-10** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang dua field-nya diubah dalam satu Save: Account Code `LG5-{runId}` (11 kar), Account Name `Beban Asuransi Gedung {runId}` (29 kar), Account Function `Depreciation Expense` (20 kar) · sumber turunan penulis
- **DU-155-11** Account (dibuat), nilai baru Account Name dan Account Function: Account Code `LG5-{runId}` (11 kar), Account Name `Beban Asuransi Kendaraan {runId}` (32 kar), Account Function `Loss on Disposal` (16 kar) · sumber turunan penulis
- **DU-155-12** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun Inactive yang di-Activate: Account Code `LG6-{runId}` (11 kar), Account Name `Kas Cadangan {runId}` (20 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-155-13** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun Active yang di-Deactivate: Account Code `LG7-{runId}` (11 kar), Account Name `Kas Operasional Harian {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-155-14** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang dihapus dan dicatat L-04: Account Code `LG8-{runId}` (11 kar), Account Name `Kas Dihapus {runId}` (19 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-155-15** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun pertama pada Deactivate bulk: Account Code `LG9A-{runId}` (12 kar), Account Name `Kas Bulk Log Satu {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-155-16** Account (awal; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun kedua pada Deactivate bulk: Account Code `LG9B-{runId}` (12 kar), Account Name `Kas Bulk Log Dua {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-155-17** Account (dibuat; dimutasi TC-FA-FACO-BE-155-log-per-aksi), akun yang dibuat, diubah, dan dihapus lewat request langsung: Account Code `LG10-{runId}` (12 kar), Account Name `Kas Integrasi {runId}` (21 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-155-18** Account (dibuat), nilai baru Account Name lewat request langsung: Account Code `LG10-{runId}` (12 kar), Account Name `Kas Integrasi Terbarui {runId}` (30 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-156-1** User (awal), aktor yang melakukan aksi: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-156-2** Account (awal; dimutasi TC-FA-FACO-BE-156-bulk-dan-selection-limit), akun Active pertama pada Deactivate bulk: Account Code `BKA-{runId}` (11 kar), Account Name `Kas Bulk Nonaktif Satu {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-156-3** Account (awal; dimutasi TC-FA-FACO-BE-156-bulk-dan-selection-limit), akun Active kedua pada Deactivate bulk: Account Code `BKB-{runId}` (11 kar), Account Name `Kas Bulk Nonaktif Dua {runId}` (29 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-156-4** Account (awal), akun yang sudah Inactive pada seleksi bulk: Account Code `BKC-{runId}` (11 kar), Account Name `Kas Bulk Sudah Nonaktif {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-156-5** Account (awal), akun Active yang tidak ikut dipilih: Account Code `BKD-{runId}` (11 kar), Account Name `Kas Bulk Tidak Dipilih {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-156-6** Account (awal), akun yang di-Edit dengan nilai identik: Account Code `NOP-{runId}` (11 kar), Account Name `Kas Tanpa Perubahan {runId}` (27 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-156-7** Account (awal), akun pemilik kode yang diduplikasi oleh Create yang ditolak: Account Code `DUP-{runId}` (11 kar), Account Name `Kas Pemilik Kode {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-156-8** Account (awal; 1001 record; dimutasi TC-FA-FACO-BE-156-bulk-dan-selection-limit), akun volume untuk uji Selection Limit: Account Code `V{n}-{runId}` (12 kar), Account Name `Kas Volume {n} {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-156-9** Account (awal; dimutasi TC-FA-FACO-BE-156-bulk-dan-selection-limit), akun yang dihapus lewat Delete bulk untuk uji entri per akun: Account Code `BXA-{runId}` (11 kar), Account Name `Kas Bulk Hapus Log Satu {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §8.4#r3
- **DU-156-10** Account (awal; dimutasi TC-FA-FACO-BE-156-bulk-dan-selection-limit), akun yang dihapus lewat Delete bulk untuk uji entri per akun: Account Code `BXB-{runId}` (11 kar), Account Name `Kas Bulk Hapus Log Dua {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §8.4#r3
- **DU-157-1** User (awal), aktor yang mengunduh berkas: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-157-2** User (awal), pengubah akun yang tampil di kolom Modified By: Name `Siti Nur Rahmawati {runId}` (26 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-157-3** Account (awal), akun Active dengan periode jurnal terisi: Account Code `DLA-{runId}` (11 kar), Account Name `Kas Satu Unduh {runId}` (22 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Last Used in Journal `Oct 2026` (8 kar) · sumber turunan penulis
- **DU-157-4** Account (awal), akun Inactive dengan Last Used in Journal kosong: Account Code `DLB-{runId}` (11 kar), Account Name `Akumulasi Dua Unduh {runId}` (27 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-157-5** Account (awal), akun dengan koma pada Account Name: Account Code `DLC-{runId}` (11 kar), Account Name `Beban Sewa, Gedung Unduh {runId}` (32 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-6** Account (awal), akun dengan tanda kutip pada Account Name: Account Code `DLD-{runId}` (11 kar), Account Name `Laba "Lain" Pelepasan Unduh {runId}` (35 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-7** Account (awal), akun dengan karakter non-ASCII pada Account Name: Account Code `DLE-{runId}` (11 kar), Account Name `Café Élan Unduh {runId}` (23 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-8** Account (awal; dimutasi TC-FA-FACO-BE-157-download-isi-berkas-dep-export-journal), akun yang Account Name-nya diubah Siti Nur Rahmawati: Account Code `DLF-{runId}` (11 kar), Account Name `Lawan Kapitalisasi Unduh {runId}` (32 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-9** Account (dibuat), nilai baru Account Name setelah Edit: Account Code `DLF-{runId}` (11 kar), Account Name `Lawan Kapitalisasi Revisi Unduh {runId}` (39 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-10** Account (awal), akun Inactive dengan Function Disposal Proceeds: Account Code `DLG-{runId}` (11 kar), Account Name `Hasil Pelepasan Unduh {runId}` (29 kar), Account Function `Disposal Proceeds` (17 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-157-12** Account (awal; 5001 record), akun volume untuk berkas lebih dari 5000 baris: Account Code `W{n}-{runId}` (12 kar), Account Name `Volume Besar {runId} nomor {n}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-157-13** Entitas (awal), entitas khusus dengan Date Format dan Time Format non-bawaan: Name `Entitas Unduh Berkas {runId}` (28 kar), Date Format `dd MMM yy` (9 kar), Time Format `12h` (3 kar) · sumber foundation prd-conventions.md §32
- **DU-158-1** User (awal), aktor yang mengirim permintaan daftar: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-158-2** Account (awal), nama berhuruf kecil di awal: Account Code `SFA-{runId}` (11 kar), Account Name `anggur Kas Saring {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-158-3** Account (awal), nama berawalan Apel: Account Code `SFB-{runId}` (11 kar), Account Name `Apel Kas Saring {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-158-4** Account (awal), akun Inactive dengan Function Accumulated Depreciation: Account Code `SFC-{runId}` (11 kar), Account Name `Beban Kas Saring {runId}` (24 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-158-5** Account (awal), nama berhuruf kecil di awal dengan Function Asset Cost: Account Code `SFD-{runId}` (11 kar), Account Name `cabang Kas Saring {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-158-6** Account (awal), akun Inactive dengan Function Gain on Disposal: Account Code `SFE-{runId}` (11 kar), Account Name `Dana Kas Saring {runId}` (23 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-158-7** Account (awal), nama yang memuat Apel di tengah: Account Code `SFF-{runId}` (11 kar), Account Name `Kas Apel Lain Saring {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-158-8** Account (awal; 12 record), 12 akun untuk uji paginasi dengan ukuran halaman 10: Account Code `PG{n}-{runId}` (13 kar), Account Name `Kas Halaman {n} Paginasi {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber §5#b1
- **DU-158-9** Account (dibuat; dimutasi TC-FA-FACO-BE-158-search-sort-filter), akun yang dibuat sebagai entri Create pada Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-10** Account (dibuat), Edit Account Name ke-1 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 1 {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-11** Account (dibuat), Edit Account Name ke-2 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 2 {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-12** Account (dibuat), Edit Account Name ke-3 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 3 {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-13** Account (dibuat), Edit Account Name ke-4 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 4 {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-14** Account (dibuat), Edit Account Name ke-5 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Asset Cost` (10 kar) · sumber §5#b1
- **DU-158-15** Account (dibuat), Edit Account Function ke-1 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Depreciation Expense` (20 kar) · sumber §5#b1
- **DU-158-16** Account (dibuat), Edit Account Function ke-2 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber §5#b1
- **DU-158-17** Account (dibuat), Edit Account Function ke-3 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Gain on Disposal` (16 kar) · sumber §5#b1
- **DU-158-18** Account (dibuat), Edit Account Function ke-4 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Loss on Disposal` (16 kar) · sumber §5#b1
- **DU-158-19** Account (dibuat), Edit Account Function ke-5 pada akun Changelog uji server: Account Code `CLG-{runId}` (11 kar), Account Name `Kas Riwayat Log 5 {runId}` (25 kar), Account Function `Capitalization Offset` (21 kar) · sumber §5#b1
- **DU-159-1** User (awal), Admin A: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-159-2** User (awal), Admin B untuk berebut slot terakhir: Name `Budi Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-159-3** Account (awal; 997 record), akun pengisi Active; 997 akun, batas 1000 dikurangi tiga: Account Code `PGA{n}-{runId}` (14 kar), Account Name `Kas Pengisi Aktif {n} {runId}` (29 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber foundation prd-conventions.md §8 (nilai kanonik plans-licensing-lifecycle-settings §9.9)
- **DU-159-4** Account (awal; dimutasi TC-FA-FACO-BE-159-batas-jumlah-akun), akun yang dinonaktifkan lalu dihapus: Account Code `LIM3-{runId}` (12 kar), Account Name `Kas Calon Nonaktif {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-159-5** Account (awal), akun pengisi Inactive yang tetap dihitung: Account Code `PGI-{runId}` (11 kar), Account Name `Kas Pengisi Nonaktif {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-159-6** Account (dibuat; dimutasi TC-FA-FACO-BE-159-batas-jumlah-akun), akun yang dibuat saat total satu di bawah batas lalu mengisi slot terakhir: Account Code `LIM1-{runId}` (12 kar), Account Name `Kas Batas Terakhir {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-7** Account (dibuat), akun yang ditolak karena melebihi batas: Account Code `LIM2-{runId}` (12 kar), Account Name `Kas Melebihi Batas {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-8** Account (dibuat; dimutasi TC-FA-FACO-BE-159-batas-jumlah-akun), akun yang ditolak lalu dibuat setelah Delete membebaskan slot: Account Code `LIM4-{runId}` (12 kar), Account Name `Kas Setelah Nonaktif {runId}` (28 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-9** Account (dibuat), akun pertama yang diperebutkan untuk slot terakhir: Account Code `LIM5-{runId}` (12 kar), Account Name `Kas Rebutan Satu {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-10** Account (dibuat), akun kedua yang diperebutkan untuk slot terakhir: Account Code `LIM6-{runId}` (12 kar), Account Name `Kas Rebutan Dua {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-11** Account (dicoba), akun yang ditolak pada plan Growth karena total tepat sama dengan batas: Account Code `LIM7-{runId}` (12 kar), Account Name `Kas Plan Growth {runId}` (23 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-159-12** Account (dicoba), akun yang ditolak pada plan Professional karena total tepat sama dengan batas: Account Code `LIM8-{runId}` (12 kar), Account Name `Kas Plan Professional {runId}` (29 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-160-1** User (awal), aktor client Suspended: Name `Maya Tertangguh {runId}` (23 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-160-2** User (awal), aktor client Expired: Name `Budi Kedaluwarsa {runId}` (24 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-160-3** Client (awal), client berstatus Suspended: Name `Klien Suspended {runId}` (23 kar), Status `Suspended` (9 kar) · sumber turunan penulis
- **DU-160-4** Client (awal), client berstatus Expired: Name `Klien Expired {runId}` (21 kar), Status `Expired` (7 kar) · sumber turunan penulis
- **DU-160-11** Account (dibuat; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun yang Create-nya ditolak pada client Suspended: Account Code `SUN-{runId}` (11 kar), Account Name `Kas Baru Suspended {runId}` (26 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-160-12** Account (dibuat; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun yang Create-nya ditolak pada client Expired: Account Code `EXN-{runId}` (11 kar), Account Name `Kas Baru Expired {runId}` (24 kar), Account Function `Asset Cost` (10 kar) · sumber turunan penulis
- **DU-160-5** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Suspended: Account Code `SUA-{runId}` (11 kar), Account Name `Kas Awal Suspended {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-160-6** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Suspended: Account Code `SUB-{runId}` (11 kar), Account Name `Kas Nonaktif Suspended {runId}` (30 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-160-7** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Suspended: Account Code `SUC-{runId}` (11 kar), Account Name `Kas Ketiga Suspended {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-160-8** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Expired: Account Code `EXA-{runId}` (11 kar), Account Name `Kas Awal Expired {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-160-9** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Expired: Account Code `EXB-{runId}` (11 kar), Account Name `Kas Nonaktif Expired {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar) · sumber turunan penulis
- **DU-160-10** Account (awal; dimutasi TC-FA-FACO-BE-160-entitas-suspended-expired), akun pada client Expired: Account Code `EXC-{runId}` (11 kar), Account Name `Kas Ketiga Expired {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-165-1** User (awal), Admin A yang menonaktifkan: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-165-2** User (awal), pemanggil request langsung: Name `Rudi Integrasi {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-165-3** User (awal), Admin B yang memakai akun pada Asset Class: Name `Budi Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-165-4** Account (awal), akun yang dipakai satu Asset Class: Account Code `DGA-{runId}` (11 kar), Account Name `Mesin Bubut {runId}` (19 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-165-5** Account (awal), akun yang dipakai dua Asset Class: Account Code `DGB-{runId}` (11 kar), Account Name `Akumulasi Mesin {runId}` (23 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar) · sumber turunan penulis
- **DU-165-6** Account (awal), akun yang hanya dipakai Asset Class Inactive: Account Code `DGC-{runId}` (11 kar), Account Name `Beban Mesin Lama {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-165-7** Account (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), akun yang tidak dipakai dan dinonaktifkan: Account Code `DGD-{runId}` (11 kar), Account Name `Laba Pelepasan Tersedia {runId}` (31 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-165-8** Account (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), akun tidak dipakai pada seleksi bulk campuran: Account Code `DGF-{runId}` (11 kar), Account Name `Kas Bulk Terbuka {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-165-9** Asset Class (awal), Asset Class aktif pemakai DGA dan DGB: Name `Kelas Mesin {runId}` (19 kar), Status `Active` (6 kar), Asset Cost `DGA-{runId}` (11 kar), Accumulated Depreciation `DGB-{runId}` (11 kar) · sumber turunan penulis
- **DU-165-10** Asset Class (awal), Asset Class Inactive pemakai DGB dan DGC: Name `Kelas Kantor {runId}` (20 kar), Status `Inactive` (8 kar), Accumulated Depreciation `DGB-{runId}` (11 kar), Depreciation Expense `DGC-{runId}` (11 kar) · sumber turunan penulis
- **DU-165-11** Account (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), akun yang menjadi dipakai antara pengecekan awal dan Confirm: Account Code `RCK-{runId}` (11 kar), Account Name `Beban Cek Ulang {runId}` (23 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-165-12** Account (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), akun bulk yang menjadi dipakai sebelum Confirm: Account Code `RCL-{runId}` (11 kar), Account Name `Kas Cek Ulang Satu {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-165-13** Account (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), akun bulk yang tetap tidak dipakai: Account Code `RCM-{runId}` (11 kar), Account Name `Kas Cek Ulang Dua {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-165-14** Asset Class (awal; dimutasi TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class), Asset Class yang kemudian memakai RCK dan RCL: Name `Kelas Cek Ulang {runId}` (23 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-166-1** User (awal), Admin A yang menghapus dan mengubah: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-166-2** User (awal), pemanggil request langsung: Name `Rudi Integrasi {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-166-3** User (awal), Admin B yang memakai akun pada Asset Class: Name `Budi Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-166-4** Account (awal), akun yang dipakai satu Asset Class: Account Code `DHA-{runId}` (11 kar), Account Name `Kas Mesin Utama {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-166-5** Account (awal), akun yang dipakai dua Asset Class: Account Code `DHB-{runId}` (11 kar), Account Name `Akumulasi Mesin Utama {runId}` (29 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `2` (1 kar) · sumber turunan penulis
- **DU-166-6** Account (awal), akun yang hanya dipakai Asset Class Inactive: Account Code `DHC-{runId}` (11 kar), Account Name `Beban Mesin Lama {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-166-7** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun tidak dipakai yang dihapus: Account Code `DHD-{runId}` (11 kar), Account Name `Laba Pelepasan Terbuka {runId}` (30 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-8** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun tidak dipakai yang dihapus dalam bulk: Account Code `DHE-{runId}` (11 kar), Account Name `Rugi Pelepasan Terbuka {runId}` (30 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-9** Account (awal), akun dipakai yang Account Function-nya tidak boleh diubah: Account Code `LKA-{runId}` (11 kar), Account Name `Beban Kunci Pemakaian {runId}` (29 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-166-10** Asset Class (awal), Asset Class aktif pemakai DHA, DHB, dan LKA: Name `Kelas Mesin Utama {runId}` (25 kar), Status `Active` (6 kar), Asset Cost `DHA-{runId}` (11 kar), Accumulated Depreciation `DHB-{runId}` (11 kar), Depreciation Expense `LKA-{runId}` (11 kar) · sumber turunan penulis
- **DU-166-11** Asset Class (awal), Asset Class Inactive pemakai DHB dan DHC: Name `Kelas Kantor Lama {runId}` (25 kar), Status `Inactive` (8 kar), Accumulated Depreciation `DHB-{runId}` (11 kar), Depreciation Expense `DHC-{runId}` (11 kar) · sumber turunan penulis
- **DU-166-12** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun yang menjadi dipakai antara pengecekan dan Confirm Delete: Account Code `RDK-{runId}` (11 kar), Account Name `Kas Cek Ulang Hapus Satu {runId}` (32 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-13** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun bulk yang menjadi dipakai sebelum Confirm: Account Code `RDL-{runId}` (11 kar), Account Name `Akumulasi Cek Ulang Satu {runId}` (32 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-14** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun bulk yang tetap tidak dipakai dan dihapus: Account Code `RDM-{runId}` (11 kar), Account Name `Akumulasi Cek Ulang Dua {runId}` (31 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-15** Account (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), akun yang kuncinya berubah antara form dibuka dan Save: Account Code `LKB-{runId}` (11 kar), Account Name `Beban Kunci Berubah {runId}` (27 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-166-16** Asset Class (awal; dimutasi TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class), Asset Class yang kemudian memakai RDK, RDL, dan LKB: Name `Kelas Cek Ulang Hapus {runId}` (29 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-166-17** Account (dibuat), nilai input Save Edit yang tidak boleh tersimpan: Account Name `Beban Kunci Diubah {runId}` (26 kar) · sumber turunan penulis
- **DU-167-1** User (awal), Admin A yang menjalankan Export Journal dan aksi lain: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-167-2** User (awal), Admin B yang mengubah pemakaian akun dan mengekspor: Name `Budi Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-167-3** User (awal), pemanggil request langsung: Name `Rudi Integrasi {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-167-4** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun dengan Last Used in Journal kosong yang diekspor pertama kali: Account Code `XJA-{runId}` (11 kar), Account Name `Kas Perdana Ekspor {runId}` (26 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-167-5** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun yang diekspor pada periode lebih baru, lebih lama, lalu sama: Account Code `XJB-{runId}` (11 kar), Account Name `Akumulasi Maju Ekspor {runId}` (29 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `M0 − 6 bulan` (12 kar) · sumber turunan penulis
- **DU-167-6** Asset Class (awal), Asset Class pemakai XJA dan XJB: Name `Kelas Ekspor {runId}` (20 kar), Status `Active` (6 kar), Asset Cost `XJA-{runId}` (11 kar), Accumulated Depreciation `XJB-{runId}` (11 kar) · sumber turunan penulis
- **DU-167-7** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun yang tidak lagi ikut export: Account Code `XJC-{runId}` (11 kar), Account Name `Kas Lama Ekspor {runId}` (23 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `M0 − 11 bulan` (13 kar) · sumber turunan penulis
- **DU-167-8** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun pengganti yang kemudian ikut export: Account Code `XJD-{runId}` (11 kar), Account Name `Kas Pengganti Ekspor {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-167-9** Asset Class (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), Asset Class yang dialihkan dari XJC ke XJD: Name `Kelas Alih {runId}` (18 kar), Status `Active` (6 kar), Asset Cost `XJC-{runId}` (11 kar) · sumber turunan penulis
- **DU-167-10** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun terekspor Active tanpa pemakai untuk uji kunci dan Guard 1: Account Code `XJE-{runId}` (11 kar), Account Name `Kas Terkunci Ekspor {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 8 bulan` (12 kar) · sumber turunan penulis
- **DU-167-12** Account (awal), akun terekspor yang sudah Inactive: Account Code `XJF-{runId}` (11 kar), Account Name `Kas Nonaktif Terekspor Ekspor {runId}` (37 kar), Account Function `Asset Cost` (10 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `M0 − 8 bulan` (12 kar) · sumber turunan penulis
- **DU-167-13** Account (awal), akun terekspor yang juga dipakai Asset Class: Account Code `XJG-{runId}` (11 kar), Account Name `Beban Guard Ganda Ekspor {runId}` (32 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar), Last Used in Journal `M0 − 8 bulan` (12 kar) · sumber turunan penulis
- **DU-167-14** Asset Class (awal), Asset Class pemakai XJG: Name `Kelas Guard Ganda {runId}` (25 kar), Status `Active` (6 kar), Depreciation Expense `XJG-{runId}` (11 kar) · sumber turunan penulis
- **DU-167-15** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun yang menjadi terekspor antara pengecekan dan Confirm Delete: Account Code `XJH-{runId}` (11 kar), Account Name `Kas Cek Ulang Ekspor {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-167-16** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun tempat Asset Class dialihkan: Account Code `XJJ-{runId}` (11 kar), Account Name `Kas Pengalih Ekspor {runId}` (27 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-167-17** Asset Class (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), Asset Class yang memakai XJH lalu dialihkan ke XJJ: Name `Kelas Cek Ulang Ekspor {runId}` (30 kar), Status `Active` (6 kar) · sumber turunan penulis
- **DU-167-18** Account (awal; dimutasi TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal), akun yang menjadi terekspor antara form Edit dibuka dan Save: Account Code `XJI-{runId}` (11 kar), Account Name `Kas Kunci Ekspor {runId}` (24 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-167-19** Asset Class (awal), Asset Class pemakai XJI: Name `Kelas Edit Kunci {runId}` (24 kar), Status `Active` (6 kar), Depreciation Expense `XJI-{runId}` (11 kar) · sumber turunan penulis
- **DU-167-20** Account (dibuat), nilai input Edit Account Code yang ditolak: Account Code `XJE2-{runId}` (12 kar) · sumber turunan penulis
- **DU-167-21** Account (dibuat), nilai input Save Edit yang ditolak: Account Code `XJI2-{runId}` (12 kar), Account Name `Kas Kunci Diubah Ekspor {runId}` (31 kar) · sumber turunan penulis
- **DU-167-22** Export Journal (dibuat), Export Journal periode M0 − 6 bulan yang hanya memuat jurnal aset ber-Asset Class Kelas Ekspor (akun XJA dan XJB): Periode `M0 − 6 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-167-23** Export Journal (dibuat), Export Journal periode M0 − 4 bulan yang hanya memuat jurnal aset ber-Asset Class Kelas Ekspor (akun XJA dan XJB): Periode `M0 − 4 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-167-24** Export Journal (dibuat), Export Journal periode M0 − 5 bulan, lebih lama dari M0 − 4 bulan, yang hanya memuat jurnal aset ber-Asset Class Kelas Ekspor (akun XJA dan XJB): Periode `M0 − 5 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-167-25** Export Journal (dibuat), Export Journal periode M0 − 3 bulan yang hanya memuat jurnal aset ber-Asset Class Kelas Alih (akun XJD): Periode `M0 − 3 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-167-26** Export Journal (dibuat), Export Journal periode M0 − 2 bulan yang hanya memuat jurnal aset ber-Asset Class Kelas Cek Ulang Ekspor (akun XJH): Periode `M0 − 2 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-167-27** Export Journal (dibuat), Export Journal periode M0 − 3 bulan yang hanya memuat jurnal aset ber-Asset Class Kelas Edit Kunci (akun XJI): Periode `M0 − 3 bulan` (12 kar) · sumber §[F-FACO-08] Update Last Used in Journal#r1
- **DU-168-1** User (awal), Admin A yang menghapus: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-168-2** User (awal), Admin B yang mengganti nilai default: Name `Budi Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-168-3** Account (awal; dimutasi TC-FA-FACO-BE-168-default-company-dep-preferences), nilai Default Gain on Disposal (SET-05) yang dihapus setelah default diganti: Account Code `DCA-{runId}` (11 kar), Account Name `Laba Pelepasan Default {runId}` (30 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-4** Account (awal; dimutasi TC-FA-FACO-BE-168-default-company-dep-preferences), nilai Default Loss on Disposal (SET-06): Account Code `DCB-{runId}` (11 kar), Account Name `Rugi Pelepasan Default {runId}` (30 kar), Account Function `Loss on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-5** Account (awal), nilai Default Capitalization Offset (SET-08): Account Code `DCC-{runId}` (11 kar), Account Name `Lawan Kapitalisasi Default {runId}` (34 kar), Account Function `Capitalization Offset` (21 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-6** Account (awal; dimutasi TC-FA-FACO-BE-168-default-company-dep-preferences), nilai Found Asset Credit Account (SET-09): Account Code `DCD-{runId}` (11 kar), Account Name `Kredit Aset Ditemukan Default {runId}` (37 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-7** Account (awal), nilai Default Disposal Proceeds Account (SET-13): Account Code `DCE-{runId}` (11 kar), Account Name `Hasil Pelepasan Default {runId}` (31 kar), Account Function `Disposal Proceeds` (17 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-8** Account (awal; dimutasi TC-FA-FACO-BE-168-default-company-dep-preferences), akun biasa yang dihapus bersama akun default pada bulk: Account Code `DCH-{runId}` (11 kar), Account Name `Kas Biasa Tanpa Default {runId}` (31 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-9** Account (awal), nilai default baru setelah SET-05 diganti: Account Code `DCI-{runId}` (11 kar), Account Name `Laba Pelepasan Pengganti {runId}` (32 kar), Account Function `Gain on Disposal` (16 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber turunan penulis
- **DU-168-10** Accounting Preferences (awal; dimutasi TC-FA-FACO-BE-168-default-company-dep-preferences), nilai default company client ini: Default Gain on Disposal `DCA-{runId}` (11 kar), Default Loss on Disposal `DCB-{runId}` (11 kar), Default Capitalization Offset `DCC-{runId}` (11 kar), Found Asset Credit Account `DCD-{runId}` (11 kar), Default Disposal Proceeds Account `DCE-{runId}` (11 kar) · sumber §9.2#p2
- **DU-168-11** Account (dibuat), nilai Edit Account Function atas akun default company: Account Code `DCD-{runId}` (11 kar), Account Function `Loss on Disposal` (16 kar) · sumber §9.2#p2
- **DU-169-1** Account (awal; dimutasi TC-FA-FACO-BE-169-edit-serentak-field-terkunci-dep-asset-class), akun yang dipakai Asset Class sehingga Account Function terkunci: Account Code `LCK-{runId}` (11 kar), Account Name `Kas Terkunci Dipakai {runId}` (28 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-169-2** Asset Class (awal), Asset Class pemakai LCK: Name `Kelas Kunci Serentak {runId}` (28 kar), Status `Active` (6 kar), Asset Cost `LCK-{runId}` (11 kar) · sumber turunan penulis
- **DU-169-3** Account (dicoba), Edit Admin A yang mengubah Account Name dan Account Function terkunci: Account Code `LCK-{runId}` (11 kar), Account Name `Kas Terkunci Nama A {runId}` (27 kar), Account Function `Accumulated Depreciation` (24 kar) · sumber §[F-FACO-02] Edit Account#r19
- **DU-169-4** Account (dibuat), Edit Admin B yang hanya mengubah Account Name: Account Code `LCK-{runId}` (11 kar), Account Name `Kas Terkunci Dinamai Ulang {runId}` (34 kar), Account Function `Asset Cost` (10 kar) · sumber §[F-FACO-02] Edit Account#r19
- **DU-169-5** Account (awal), akun kedua yang dipakai Asset Class untuk dua Edit Function serentak: Account Code `LCL-{runId}` (11 kar), Account Name `Kas Terkunci Kedua {runId}` (26 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
- **DU-169-6** Asset Class (awal), Asset Class pemakai LCL: Name `Kelas Kunci Kedua {runId}` (25 kar), Status `Active` (6 kar), Depreciation Expense `LCL-{runId}` (11 kar) · sumber turunan penulis
- **DU-169-7** Account (dicoba), Edit Admin A yang mengubah Account Function terkunci menjadi Gain on Disposal: Account Code `LCL-{runId}` (11 kar), Account Name `Kas Terkunci Kedua {runId}` (26 kar), Account Function `Gain on Disposal` (16 kar) · sumber §[F-FACO-02] Edit Account#r20
- **DU-169-8** Account (dicoba), Edit Admin B yang mengubah Account Function terkunci menjadi Loss on Disposal: Account Code `LCL-{runId}` (11 kar), Account Name `Kas Terkunci Kedua {runId}` (26 kar), Account Function `Loss on Disposal` (16 kar) · sumber §[F-FACO-02] Edit Account#r20
- **DU-170-1** User (awal), aktor yang mengirim permintaan daftar: Name `Maya Pengelola {runId}` (22 kar), Access Level `Total Control` (13 kar) · sumber matriks role PRD
- **DU-170-2** Account (awal), Used By 0 dan Last Used in Journal kosong: Account Code `SDA-{runId}` (11 kar), Account Name `Kas Kecil Turunan {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `0` (1 kar) · sumber EB-SRT-2
- **DU-170-3** Account (awal), Used By 2 dengan periode terlama Sep 2025: Account Code `SDB-{runId}` (11 kar), Account Name `Beban Mesin Turunan {runId}` (27 kar), Account Function `Depreciation Expense` (20 kar), Status `Active` (6 kar), Used By `2` (1 kar), Last Used in Journal `Sep 2025` (8 kar) · sumber §4.1.1#r5
- **DU-170-4** Account (awal), Last Used in Journal Jan 2026 pada kolom bertipe Text: Account Code `SDC-{runId}` (11 kar), Account Name `Akumulasi Sewa Turunan {runId}` (30 kar), Account Function `Accumulated Depreciation` (24 kar), Status `Inactive` (8 kar), Used By `0` (1 kar), Last Used in Journal `Jan 2026` (8 kar) · sumber §4.1.1#r6
- **DU-170-5** Account (awal), Used By 10 untuk uji urutan angka natural: Account Code `SDD-{runId}` (11 kar), Account Name `Kas Besar Turunan {runId}` (25 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `10` (2 kar), Last Used in Journal `Mar 2026` (8 kar) · sumber §4.1.1#r5
- **DU-170-6** Account (awal), akun Inactive tanpa periode jurnal dan Used By 0: Account Code `SDE-{runId}` (11 kar), Account Name `Laba Pelepasan Turunan {runId}` (30 kar), Account Function `Gain on Disposal` (16 kar), Status `Inactive` (8 kar), Used By `0` (1 kar) · sumber EB-SRT-2
- **DU-170-7** Account (awal), Used By 1 tanpa periode jurnal: Account Code `SDF-{runId}` (11 kar), Account Name `Kas Bank Turunan {runId}` (24 kar), Account Function `Asset Cost` (10 kar), Status `Active` (6 kar), Used By `1` (1 kar) · sumber turunan penulis
