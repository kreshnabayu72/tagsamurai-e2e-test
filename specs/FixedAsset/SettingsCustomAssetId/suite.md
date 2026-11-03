---
name: Fixed Asset Settings Custom Asset ID
id: suite-fixed-asset-settings-custom-asset-id
description: Spec e2e turunan tc-settings-custom-asset-id.md untuk Fixed Asset > Settings > Asset Master > Custom Asset ID
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Custom Asset ID

Suite ini mencakup tab Custom Asset ID pada Fixed Asset > Settings > Asset Master: screening dan state awal, guided tooltip, Role Matrix dan gating capability, plan Starter dan state tenant (Suspended, Expired), konfigurasi singleton (Master Switch, Separator, Initial Company, daftar segmen, Live Preview, Save), Retroactive Mass Update, validasi V-07 (64 karakter), dialog Unsaved Changes, Modal View Code List dan Modal Changelog: Custom Asset ID (Search, Filter, Sort, Setup Column, Pagination, Download), pencatatan log di Changelog, System Log, dan Activity Log, penerbitan Asset ID saat registrasi, cascade Transfer, Purchase Date, dan Division, riwayat Asset ID, defense-in-depth, konkurensi, volume, dan ketahanan terhadap kegagalan server.

`parallel: false` karena konfigurasi Custom Asset ID bersifat singleton per Company dan counter Increment aset dipakai bersama oleh seluruh spec dalam Company yang sama; spec juga mengubah state global (plan tier, General Settings Date Format dan Time Zone, jam server, flag Guided Tooltip, preferensi kolom). Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Login: akun aktor pertama tiap spec login di hook `before` spec itu (akun dan env var tertulis di `## Prerequisites` spec); langkah login di `## Test Steps` hanya untuk ganti akun, dan hook `after` spec mengembalikan sesi ke akun default suite (Total Control Company Alpha, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` (page_key `fa-settings-custom-asset-id`, PRD §4.7): hook `before` suite mencatat nilai awal flag lalu menyetelnya `seen` (true) untuk setiap akun UI yang dipakai suite, dan hook `after` memulihkan nilai awal. Spec guided tooltip (TC 13 sampai 21) menulis pengecualiannya sendiri dan mengatur flag sesudah hook.
- Baseline konfigurasi Company Alpha (Pre-setup No 10, baseline B1: Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan aset A1 sampai A5 (Pre-setup No 11): hook `beforeEach` suite memulihkan konfigurasi dan aset ke baseline lewat seed API memakai sesi API Total Control Company Alpha (klien HTTP dan penangkapan token sesi API disediakan tim FE; token sesi API tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir), dan hook `after` suite memulihkan ulang walau spec gagal di tengah. Baseline lain (B2 sampai B6) dan company khusus (Pre-setup No 9, 12 sampai 24, 29 sampai 35) di-seed oleh hook `before` spec yang memakainya dan dinyatakan di `## Prerequisites` spec itu; seed company khusus dikembalikan tim FE/BE ke keadaan awal sebelum tiap run. Entri log yang bertambah karenanya tidak dihapus.
- Layar awal: hook `beforeEach` suite membuka Fixed Asset > Settings > Asset Master > Custom Asset ID untuk akun yang login di hook `before` spec itu, sehingga spec yang tidak menguji navigasi tidak mengulang langkah buka. Pengecualian: spec yang tidak berawal di tab itu (registrasi aset, daftar modul konsumen, spec akses tanpa capability) menyatakan layar awalnya sendiri di `## Prerequisites`.
- Konfirmasi bawaan browser `beforeunload`: reload atau navigasi pada form yang masih berisi perubahan belum tersimpan memunculkan konfirmasi bawaan browser. Kemampuan menanganinya (konfirmasi otomatis oleh harness, tanpa langkah bersyarat) ditulis di `## Prerequisites` spec yang membutuhkannya. Hook `beforeEach` suite menjadi jaring pengaman: ia mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` bila spec sebelumnya berakhir dengan form dirty; itu bukan pengganti langkah pemulihan eksplisit di spec yang mengubah form.
- Konfigurasi kolom Setup Column Modal View Code List dan Modal Changelog yang disimpan spec dipulihkan di hook `after` spec itu dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE.
- Entri Changelog yang diasersi spec Modal Changelog di-seed lewat API di hook `before` spec itu dengan nilai distinct per kolom yang di-search, difilter, atau di-sort (dataset Pre-setup No 15); asersi jumlah entri log memakai baseline jumlah entri sebelum aksi (S-12).
- Akun di luar Tabel Data Uji Pre-setup TC (staf tiap Company selain Company Alpha) dan semua nama env var password baru ditulis "disediakan tim FE" di `## Prerequisites` spec yang memakainya; pendaftaran env var di `spectra.config.ts` dan `.env.example` dikerjakan di tahap script.
- Env var password akun aktor (usulan, perlu konfirmasi tim FE): `FA_TC_PASSWORD` (Total Control), `FA_RO_PASSWORD` (Read Only), `FA_CFGUPD_PASSWORD` (Config-Update), `FA_CFGREAD_PASSWORD` (Config-Read), `FA_MDONLY_PASSWORD` (Master-Data-Only), `FA_CFGMASTER_PASSWORD` (Config-And-Master), `FA_NOROLE_PASSWORD` (Tanpa Role Terkait), `FA_TC2_PASSWORD` (Total Control sesi 2), dan satu env per Company khusus (mis. `FA_BETA_TC_PASSWORD`, `FA_STARTER_TC_PASSWORD`, `FA_KOSONG_TC_PASSWORD`).

## Usulan nama env var password (disediakan tim FE)

Akun dan password tiap nama di bawah disediakan tim FE; suite tidak mengarang akun. Nama adalah usulan yang perlu konfirmasi tim FE dan didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script. Dipakai sebagai `Spectra.env.<NAMA>`; kolom kanan memuat nomor spec yang memakainya.

| Env var | Spec |
|---|---|
| `FA_TC_PASSWORD` | akun default suite (Total Control Company Alpha) dan hampir seluruh spec |
| `FA_TC2_PASSWORD` | 044, 048, 084 |
| `FA_RO_PASSWORD` | 006, 007, 026, 098 |
| `FA_CFGUPD_PASSWORD` | 005, 006, 008, 009 |
| `FA_CFGREAD_PASSWORD` | 006, 008, 026, 098 |
| `FA_MDONLY_PASSWORD` | 006, 009, 026, 098 |
| `FA_CFGMASTER_PASSWORD` | 009 |
| `FA_NOROLE_PASSWORD` | 026, 098 |
| `FA_STARTER_TC_PASSWORD` | 010, 011, 014 |
| `FA_STARTER_RO_PASSWORD` | 010 |
| `FA_STARTER_CFGUPD_PASSWORD` | 010, 026, 098 |
| `FA_STARTER_MDONLY_PASSWORD` | 010 |
| `FA_GROWTH_TC_PASSWORD` | 010 |
| `FA_PROFESSIONAL_TC_PASSWORD` | 010 |
| `FA_ENTERPRISE_TC_PASSWORD` | 010 |
| `FA_DOWNGRADE_TC_PASSWORD` | 011, 012 |
| `FA_UPGRADE_TC_PASSWORD` | 011 |
| `FA_SUSPENDED_TC_PASSWORD` | 100 |
| `FA_EXPIRED_TC_PASSWORD` | 100 |
| `FA_KOSONG_TC_PASSWORD` | 003, 015, 030, 037 |
| `FA_BETA_TC_PASSWORD` | 043 |
| `FA_BIG_TC_PASSWORD` | 045, 046 |
| `FA_BIG_TC2_PASSWORD` | 045 |
| `FA_BIGTRG_TC_PASSWORD` | 045 |
| `FA_BIGTRG_TC2_PASSWORD` | 045 |
| `FA_VOLUME_TC_PASSWORD` | 054, 055 |
| `FA_CODELIST_TC_PASSWORD` | 050 |
| `FA_CODEEDITDIV_TC_PASSWORD` | 090 |
| `FA_CODEEDITCODE_TC_PASSWORD` | 091 |
| `FA_V0763_TC_PASSWORD` | 031 |
| `FA_V0764_TC_PASSWORD` | 031 |
| `FA_V0765_TC_PASSWORD` | 031, 032, 042, 047 |
| `FA_V07D_TC_PASSWORD` | 087 |
| `FA_V07R_TC_PASSWORD` | 086 |
| `FA_V07T_TC_PASSWORD` | 087 |
| `FA_CHANGELOG_TC_PASSWORD` | 059, 066 sampai 077, 079 |
| `FA_LOGVOL_TC_PASSWORD` | 078, 080 |
| `FA_EXPORT_TC_PASSWORD` | 080 |
| `FA_REGISTER_TC_PASSWORD` | 083, 084, 085, 096 |
| `FA_TARGETED_TC_PASSWORD` | 089, 090, 092, 097 |
| `FA_DIVDEL_TC_PASSWORD` | 093 |
| `FA_CONSUMERS_TC_PASSWORD` | 095 |

Akun Total Control Company Kosong Changelog (Pre-setup No 37, spec 003) memakai env var password yang disediakan tim FE; namanya tidak ditetapkan di suite ini.
