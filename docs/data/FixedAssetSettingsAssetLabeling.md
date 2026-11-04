# Data uji FixedAssetSettingsAssetLabeling

Sumber PRD: `fixed-asset/settings-asset-labeling/PRD/settings-asset-labeling.md` · PRD sha256 `ef9368b7d5ffc9af`

Spec merujuk data hanya lewat `DU-nn`. Akun memakai env `FA_<ROLE>_EMAIL` / `FA_<ROLE>_PASSWORD`, tidak pernah literal. Baris `Sumber` = `turunan planner` adalah data yang tidak diberikan PRD dan disetujui bersama plan. Kolom `Dipakai spec` dihitung dari spec yang tertulis (bukan dari rencana).

| ID | Data | Nilai | Sumber | Lifecycle | Dipakai spec |
|---|---|---|---|---|---|
| `DU-01` | Akun Total Control Fixed Asset | env FA_TC_EMAIL, FA_TC_PASSWORD | PRD §2 matriks role | pre-setup | 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 016, 017, 018, 019, 020, 021, 023, 024, 026 |
| `DU-02` | Akun Read Only | env FA_RO_EMAIL, FA_RO_PASSWORD | PRD §2 matriks role | pre-setup | 005, 006 |
| `DU-03` | Akun Create Only (Permission Create pada Manage Asset Master Data) | env FA_CO_EMAIL, FA_CO_PASSWORD | PRD §2 matriks role | pre-setup | 006 |
| `DU-04` | Akun Update Only (Permission Update pada Manage Asset Master Data) | env FA_UO_EMAIL, FA_UO_PASSWORD | PRD §2 matriks role | pre-setup | 006 |
| `DU-05` | Akun Delete Only (Permission Delete pada Manage Asset Master Data) | env FA_DO_EMAIL, FA_DO_PASSWORD | PRD §2 matriks role | pre-setup | 006 |
| `DU-06` | Akun Role Lain tanpa capability | env FA_NOROLE_EMAIL, FA_NOROLE_PASSWORD | PRD §2 matriks role | pre-setup | 006 |
| `DU-07` | Population Labels List 6 baris (Total Asset: High Priority 45, Finance Department 120, Audit Ready 82, Executive Asset 14, Maintenance Due 28, Seasonal Event 0) | High Priority #EF4444; Finance Department #3B82F6; Audit Ready #10B981; Executive Asset #8B5CF6; Maintenance Due #F59E0B; Seasonal Event #EC4899 | PRD §4.1.1 Example Data | pre-setup | 001 |
| `DU-08` | Kata kunci Search tanpa hasil | zzz-{runId}-001 | turunan planner | dinamis | 001 |
| `DU-09` | Warna uji preset dan kanvas | Swatch preset pertama = `#EF4444` (palet preset baris 1 kolom 1); titik kanvas custom = klik di tengah area Kanvas Warna Kustom (50% lebar, 50% tinggi dari pojok kiri atas), hex hasilnya dibaca dari kolom Hex dan harus berbeda dari `#EF4444` | PRD §4.3 Palet Preset (swatch pertama, L505); turunan planner (titik kanvas) | pre-setup | 002 |
| `DU-10` | Kode hex custom valid huruf kecil | #a1b2c3 (ditampilkan kapital #A1B2C3) | turunan planner | pre-setup | 002, 003, 005, 009 |
| `DU-11` | Nama label uji Live Preview | Preview-{runId}-NNN | turunan planner | dinamis | 002, 003 |
| `DU-12` | Kode hex tidak valid | kurang dari 6 digit, lebih dari 6 digit, karakter non-heksadesimal, dan 6 digit tanpa awalan # (satu nilai per kategori) | E-FALB-28 (kurang dari 6 digit, lebih dari 6 digit, non-heksadesimal); F-FALB-06.k1 (bukan `#` diikuti 6 digit heksadesimal, termasuk 6 digit tanpa `#`) | pre-setup | 003, 005 |
| `DU-13` | Nama label Create berhasil | Create-{runId}-004 | turunan planner | dibuat spec 004 | 004 |
| `DU-14` | Nama dengan spasi depan dan belakang | spasi + Trim-{runId}-NNN + spasi | FALB-LOGIC-01c | dinamis | 004, 023 |
| `DU-15` | Nama duplikat berbeda huruf besar-kecil | nama dasar = label pembanding yang di-seed hook `before` (spec 004, 008); nilai ketikan = nama dasar dengan kapitalisasi dibalik | FALB-LOGIC-01a | dinamis | 004, 008 |
| `DU-16` | Nama hanya berisi spasi | beberapa spasi | E-FALB-18 | pre-setup | 008, 021 |
| `DU-17` | Nama 121 karakter setelah trim | pengisi + suffix {runId}-NNN, total 121 karakter | E-FALB-18 | dinamis | 008, 021 |
| `DU-18` | Label seed milik spec (di-seed hook) | pola `Seed-{runId}-NNN` dengan NNN = nomor spec pemakai (006, 007, 024), warna #3B82F6; dibuat lewat API di hook `before`, dihapus di hook `after`; sudah ada saat langkah pertama | turunan planner | dinamis | 006, 007, 024 |
| `DU-19` | Akun Manage Asset Master Data CRUD tanpa Update pada Manage Asset & TAG | env FA_AMDCRUD_EMAIL, FA_AMDCRUD_PASSWORD | turunan planner | pre-setup | 007 |
| `DU-20` | Akun Update pada Manage Asset & TAG tanpa Manage Asset Master Data | env FA_ATUPD_EMAIL, FA_ATUPD_PASSWORD; cakupan group Manage Asset & TAG hanya group pertama, bukan group kedua `DU-46` | turunan planner | pre-setup | 007 |
| `DU-21` | Aset seed untuk uji penugasan oleh role | 1 aset Active milik spec di group pertama (dalam cakupan `DU-20`), tanpa label | turunan planner | dinamis | 007 |
| `DU-22` | Nama label hasil ubah kapitalisasi | nama seed `DU-49` dengan kapitalisasi diubah (Urgent-{runId}-NNN menjadi URGENT-{runId}-NNN); nama baru yang diketik, bukan nama awal | E-FALB-07 | dinamis | 008, 023 |
| `DU-23` | Label pembanding untuk duplikat saat Edit | Other-{runId}-008 | E-FALB-17 | dinamis | 008 |
| `DU-24` | Nama label baru yang diketik pelaku utama sebelum Save pada Edit yang ditolak (tidak pernah tersimpan) | Renamed-{runId}-024 | turunan planner | dinamis | 024 |
| `DU-25` | Baseline jumlah entri log | jumlah entri Changelog, System Log, dan Activity Log sebelum aksi pemicu, dibaca lewat kemampuan baca BE; dicatat per run, bukan nilai tetap | turunan planner | dinamis | 004, 008, 009, 013, 021, 024 |
| `DU-26` | Aset seed Active milik spec | aset Active bersuffix, jumlah sesuai blok (maksimal 3) | turunan planner | dinamis | 010, 011, 012, 017, 026 |
| `DU-27` | Asset Name dengan Default Label | Asset Name bersuffix nomor spec pemakai (`{runId}-010`, `{runId}-012`) yang memakai label seed spec itu sebagai Default Label (`DU-53` di 010, `DU-50` di 012); ini nama Asset Name, bukan nama label | turunan planner | dinamis | 010, 012 |
| `DU-28` | Himpunan aset untuk Bulk Remove campuran | sebagian aset berelasi default, sebagian manual untuk label yang sama | E-FALB-06 | dinamis | 010, 012 |
| `DU-29` | Aset manual untuk skenario label manual sebelum dijadikan Default Label | aset Active dari Asset Name `{runId}-010-29` tanpa Default Label, dengan label seed `DU-54` menempel manual; Asset Name itu lalu menetapkan `DU-54` sebagai Default Label (bukan nama label) | E-FALB-13 | dinamis | 010 |
| `DU-30` | Nama baru label untuk uji refleksi | Critical-{runId}-011; nama baru yang diketik pada Edit, nama awal seed ada di `DU-49` | E-FALB-11 | dinamis | 011 |
| `DU-31` | Akun Total Control kedua (pelaku kedua) | env FA_TC2_EMAIL, FA_TC2_PASSWORD | turunan planner | pre-setup | 013, 026 |
| `DU-32` | Nama label sama untuk dua pembuat serentak | Race-{runId}-013 (dua pembuat serentak, E-FALB-19) | E-FALB-19 | dinamis | 013 |
| `DU-33` | Akun Total Control client Suspended | env FA_SUSP_TC_EMAIL, FA_SUSP_TC_PASSWORD | turunan planner | pre-setup | 014 |
| `DU-34` | Akun Total Control client Expired | env FA_EXP_TC_EMAIL, FA_EXP_TC_PASSWORD | turunan planner | pre-setup | 025 |
| `DU-35` | Label pre-setup di client Suspended (target aksi tulis yang ditolak, hanya dibaca) | tepat 1 label di client Suspended, bersih: satu-satunya baris Labels List, Total Asset 0, bukan Default Label; nilai ketikan aksi tulis = nama label + `-baru` / `-ubah` | turunan planner | pre-setup | 014 |
| `DU-36` | Akun Total Control client uji batas katalog Label | env FA_LIM_TC_EMAIL, FA_LIM_TC_PASSWORD; client ini punya katalog Label kosong di awal run dan katalog Asset Name yang belum mencapai ceiling (supaya `[+ Asset Name]` tidak diblok `D-07`); bukan client yang sudah di batas | turunan planner | pre-setup | 015 |
| `DU-37` | Katalog Label client `DU-36` diisi sampai batas Master Data Count Limit | hook `before` mengisi sampai batas minus 1 lewat fixture BE (batas dari System Limits, disediakan tim FE/BE); label ke-batas dibuat pelaku kedua sehingga total sama dengan batas; nama ketikan = Limit-{runId}-015 + `-baru` | turunan planner | dinamis | 015 |
| `DU-38` | Akun Total Control client tier Enterprise yang katalog Labelnya sudah di batas (total sama dengan batas) | env FA_LIM_ENT_TC_EMAIL, FA_LIM_ENT_TC_PASSWORD | turunan planner | pre-setup | 015 |
| `DU-39` | Respons mock Labels, Changelog, dan ekspor | daftar kosong, respons normal berisi baris, error 5xx, dan kegagalan ekspor per endpoint | turunan planner | dinamis | 016 |
| `DU-40` | Label dipakai Default Label oleh 3 Asset Name | label seed + 3 Asset Name bersuffix | E-FALB-03 | dinamis | 017 |
| `DU-41` | Label guard bersih yang menjadi dipakai antara buka dialog dan konfirmasi | label seed bersih bersuffix `{runId}-017`; aset dilabeli lewat sesi API setelah D-01 dibuka | E-FALB-14 | dinamis | 017 |
| `DU-42` | Label dipakai 500 aset | 1 label seed + 500 aset berlabel (fixture BE) | E-FALB-02 | dinamis | 018 |
| `DU-43` | Label bersih beserta aset berstatus Deleted yang masih menyimpan relasi | label seed, 1 aset Deleted berelasi label | E-FALB-24 | dinamis | 019 |
| `DU-44` | Label yang dihapus admin lain saat dialog terbuka | label seed dihapus lewat sesi API setelah D-01 dibuka | E-FALB-12 | dinamis | 019 |
| `DU-45` | Label campuran bersih dan dipakai | 2 label bersih + 1 label dipakai aset (bersuffix) | E-FALB-27 | dinamis | 020 |
| `DU-46` | Group, departemen, dan divisi kedua | satu group kedua beserta departemen dan divisi sendiri, berbeda dari group, departemen, dan divisi pertama milik `DU-01`, `DU-20`, dan `DU-21`; disiapkan tim FE/BE di client uji | turunan planner | pre-setup | 004, 007 |
| `DU-47` | Akun Read Only di group, departemen, dan divisi kedua `DU-46` | env FA_G2RO_EMAIL, FA_G2RO_PASSWORD | turunan planner | pre-setup | 004 |
| `DU-48` | Aset seed Active di group kedua (di luar cakupan group `DU-20`) | 1 aset Active milik spec di group kedua `DU-46`, tanpa label | turunan planner | dinamis | 007 |
| `DU-49` | Nama awal label seed yang di-Edit | pola `Urgent-{runId}-NNN` dengan NNN = nomor spec pemakai (008, 009, 011, 013, 023; di 013 hasil Edit memakai sufiks `-A` / `-B`), warna `#3B82F6` kecuali spec 009 (`#A1B2C3`); dibuat lewat API di hook `before`, dihapus di hook `after`; nama itu diketik ulang di Search, bukan nama hasil Edit | turunan planner | dinamis | 008, 009, 011, 013, 023 |
| `DU-50` | Label seed untuk penugasan ke aset (tidak di-Edit) | pola `Assign-{runId}-NNN` dengan NNN = nomor spec pemakai (012, 026), warna `#3B82F6`; dibuat lewat API di hook `before`, dihapus di hook `after` | turunan planner | dinamis | 012, 026 |
| `DU-51` | Label yang dibuat request Create langsung pada spec 005 | `Seed-{runId}-005`, warna `DU-10`; belum ada saat langkah pertama, tersimpan hanya bila request sukses | turunan planner | dibuat spec 005 | 005 |
| `DU-52` | Label pre-setup di client Expired (target aksi tulis yang ditolak, hanya dibaca) | tepat 1 label di client Expired, bersih: satu-satunya baris Labels List, Total Asset 0, bukan Default Label; nilai ketikan aksi tulis = nama label + `-baru` / `-ubah` | turunan planner | pre-setup | 025 |
| `DU-53` | Label seed utama spec 010 | pola `Seed-{runId}-010`, warna `#3B82F6`; Default Label Asset Name `DU-27`; ditempel manual pada aset manual `DU-28` | turunan planner | dinamis | 010 |
| `DU-54` | Label seed manual spec 010 (skenario E-FALB-13) | pola `Manual-{runId}-010`, warna `#3B82F6`; menempel manual pada aset `DU-29` sebelum dijadikan Default Label | turunan planner | dinamis | 010 |
| `DU-55` | Label hapus-dulu bersih spec 017 | label seed bersih bersuffix `{runId}-017`; dihapus lewat sesi API sebelum permintaan attach dikirim | E-FALB-14 | dinamis | 017 |
