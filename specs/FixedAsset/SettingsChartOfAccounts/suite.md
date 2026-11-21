---
name: Fixed Asset Settings Chart of Accounts
id: suite-fixed-asset-settings-chart-of-accounts
description: Spec e2e turunan PRD fixed-asset@9e5ae60 (stage spec-from-prd) untuk Fixed Asset > Settings > Accounting > Chart of Accounts
executionOrder: 8.0
parallel: false
---

# Suite: Fixed Asset Settings Chart of Accounts

Suite ini mencakup tab Chart of Accounts pada Settings > Accounting: tabel Account List (tampilan, Search, Filter, Sort, Setup Column, paginasi, Select All, Download), Modal Add Account dan Edit Account beserta validasi dan kunci Account Code serta Account Function, aksi Activate, Deactivate, Delete, dan bulk beserta dialog konfirmasi dan blok, Modal Changelog, popup Used By, Guided Tooltip, gating capability Manage accounting dan plan, state entitas (Suspended, Expired), batas jumlah akun dan Selection Limit, pencatatan log di Changelog, System Log, dan Activity Log, dependensi ke Asset Class, Accounting Preferences, Export Journal, Custom Asset ID, General Settings, dan User, tampilan Android, serta otorisasi dan validasi sisi server.

Lapisan spec: `ui-e2e` (`-E2E-`) berjalan di aplikasi nyata memakai hook suite di bawah; `ui-client` (`-UI-`) me-mount komponen dengan data yang dinyatakan spec itu sendiri dan tidak memakai tenant suite; `be-e2e` (`-BE-`, owner BE) adalah request langsung ke server dan tidak bergantung pada hook UI suite ini.

`parallel: false` karena spec `ui-e2e` berbagi satu tenant suite dan satu aktor default (satu sesi web per akun), membaca seed bersama yang sebagian diubah lalu dipulihkan spec (akun Pre-setup, Asset Class pemberi Used By, akun default company di Accounting Preferences), dan mengubah state yang dibaca spec lain: capability role, preferensi Setup Column, flag Guided Tooltip, batas jumlah akun, dan Selection Limit. Setiap spec menyiapkan dan membersihkan datanya sendiri; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

Hook suite ada di proyek e2e (`specs/FixedAsset/SettingsChartOfAccounts/hooks/<before|beforeEach|afterEach|after>/web.hook.ts`, platform web).

- `before` (sekali per suite): membuat tenant uji milik suite (berlangganan Fixed Asset) dan satu Division, lalu membuat aktor default suite: pengguna Fixed Asset Total Control di tenant itu (email tetap per tenant `facoa+{runId}-{clientCode}@…`, password lewat `Spectra.env`). Sebagai aktor itu, lewat API publik, hook menyeed akun Pre-setup bersama (idempotent: akun yang Account Code-nya sudah ada tidak dibuat ulang), delapan Asset Class (`E2E-AC-01` sampai `E2E-AC-08`) yang memberi akun Pre-setup nilai Used By, dan akun default company di Accounting Preferences (Gain on Disposal, Loss on Disposal, Capitalization Offset, Found Asset Credit, Disposal Proceeds). Hook gagal bila seed tidak menghasilkan akun sama sekali.
- `beforeEach` (tiap spec): mengembalikan tenant suite ke status Active dan memulihkan langganan Fixed Asset-nya (jaring pengaman bila spec sebelumnya gagal sebelum pemulihan), mengonfirmasi `beforeunload`, lalu memulai dari browser bersih: preferensi Setup Column dihapus di browser (bukan lewat `[Reset to Default]`), cookie, localStorage, dan sessionStorage (state tabel: Search, Filter, sort, rows per page) dikosongkan, semua guided tour ditandai seen termasuk `fa-settings-chart-of-accounts`, dan halaman dimuat ulang. Sesudahnya aktor default login dan hook membuka Fixed Asset > Settings > Accounting > Chart of Accounts (layar awal spec). Spec yang Prerequisites-nya menyebut aktor, client, atau layar awal lain (Beranda Fixed Asset, Asset Class, modal tertentu, aplikasi Android) berpindah sendiri dari keadaan ini.
- `afterEach` (tiap spec): menghapus setiap tenant tambahan yang dibuat spec (entitas kosong, Suspended, Expired, plan Starter, volume besar, client kedua), beserta akunnya. Hook gagal dan menyebut tenant yang tidak terhapus.
- `after` (sekali per suite, dijalankan walau `before` tidak selesai): mengonfirmasi `beforeunload`, menghapus preferensi Setup Column di browser, lalu menghapus tenant suite dan tenant tambahan yang tersisa; akun, Asset Class, dan pengguna ikut terhapus bersama tenant. Kegagalan tiap langkah dikumpulkan dan dilempar bersama.
- Aktor lain: spec dengan aktor role lain (Read Only, Manage accounting dengan sebagian huruf CRUD, Group Manager, Default User) atau beberapa aktor membuat pengguna itu sendiri dan berpindah sesi di langkahnya; hook tidak mengembalikan sesi karena `beforeEach` berikutnya selalu memulai dari browser bersih.
- State entitas: status Suspended dan Expired, plan Starter, entitas kosong, dan volume besar dibentuk pada tenant milik spec, tidak pada tenant suite; tenant itu dihapus `afterEach`.
- Guided Tooltip: flag tersimpan di browser, sehingga `beforeEach` menandainya seen pada setiap jendela baru dan tidak ada yang perlu dipulihkan. Spec Guided Tooltip (E2E-016, UI-130) membatalkan tanda seen itu sendiri.
- General Settings (Date Format, Time Format, Time Zone) tidak disetel hook suite; spec yang mensyaratkan nilai tertentu menyatakannya di Kondisi `## Prerequisites`.
- Gap yang diketahui (D-232): Last Used in Journal tidak bisa dibentuk lewat seed karena penulis export jurnal belum ada; akun Pre-setup yang membutuhkannya terbentuk tanpa nilai itu.

## Data bersama

- Identitas akun Pre-setup bersama (Account Code, Account Name, Account Function, status Active, Used By) ada di fixture proyek e2e `fixtures/settingsChartOfAccounts.json`, bersama rute layar dan nama aktor default.
- Data spec (`DU-<NNN>-<n>`) bersuffix `{runId}` dan dibuat spec itu sendiri di tenant suite atau di tenant milik spec; target aksi tulis dan hapus memakai data milik spec (S-06, S-12). Akun yang dibuat spec di tenant suite ikut terhapus bersama tenant di hook `after`.
- Asersi jumlah entri Changelog, System Log, dan Activity Log memakai baseline sebelum aksi, bukan angka absolut (S-12).
