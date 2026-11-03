---
name: Fixed Asset Settings Custom Fields
id: suite-fixed-asset-settings-custom-fields
description: Spec e2e turunan tc-settings-custom-fields.md untuk Fixed Asset > Settings > Custom Fields
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Custom Fields

Suite ini mencakup halaman Fixed Asset > Settings > Custom Fields (tab General, Purchasing, Accounting): tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit (termasuk ganti Data Type, Decimal Places terkunci, opsi Dropdown, Value Type, dan Scope), Toggle Active single dan Bulk Activate atau Deactivate, Delete single dan Bulk Delete, Popup All Values Preview, Modal Changelog, Role Matrix, Guided Tooltip, mobile Android, pencatatan log di tiga surface (Changelog, Activity Log, System Log aktor), sinkronisasi ke Asset Name, form registrasi aset, Detail Aset, dan Asset List, batas Master Data Count Limit, cap per Asset Name, dan Selection Limit, lisensi FA-7 (lapse dan Grace Period), state tenant (Suspended, Expired), plan tier, konkurensi dua sesi, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (Master Data Count Limit, Selection Limit, Max custom fields per asset name, format tanggal dan Currency General Settings, capability role, lisensi FA-7 dan waktu seed, status Client, flag Guided Tooltip, preferensi Setup Column). Spec yang menghapus data dijalankan sesudah spec lain dalam urutan folder.

## Hook suite

- **Login:** hook `before` tiap spec login sekali sebagai akun aktor pertama spec (password lewat `Spectra.env.*`, tidak ditulis di spec atau fixture); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Spec yang berganti akun atau Company mencantumkan akunnya di `## Prerequisites`.
- **Layar awal:** hook `beforeEach` membuka Fixed Asset > Settings > Custom Fields (tab General) kecuali spec yang menguji navigasi atau layar lain.
- **Sesi API aktor:** login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web. Dipakai pelaku kedua yang hanya memicu perubahan state (hapus Asset Name, field, atau opsi, cabut capability, isi nilai aset). Kemampuan disediakan tim BE/FE.
- **Guided Tooltip:** flag `guided_tooltip_seen_fa-settings-custom-fields`: hook `before` suite menyetel flag true untuk setiap akun aktor yang dipakai spec (nilai awal dicatat) dan hook `after` memulihkannya. Spec 008 dan 009 menguji flag itu sendiri dan menulis pengecualian di `## Prerequisites`. Mekanisme disediakan tim FE/BE.
- **Baseline Company:** hook `before` tiap spec memulihkan baseline Company yang dipakainya (seed reset Company, mengikuti Pre-setup TC: Company Alpha, Nilai, Kosong, Starter, Cap, Plafon, Changelog, Volume, Export, Suspended, Expired, License Lapse, Grace, Excess, Nama Khusus) dan hook `after` membersihkan data Dinamis milik spec. Baseline ini mencakup Asset Name Pre-setup #11 (Turbine, Boiler, Compressor, Pump, dan lainnya): spec yang menghapus atau mengubah Asset Name lewat sesi API (132, 134, 135, 167, 171) mengandalkan seed reset ini untuk memulihkannya. Mekanisme seed disediakan tim FE/BE; field Dinamis bernama bersuffix `{runId}-<NNN>`.
- **Setup Column:** hook `after` menghapus preferensi kolom yang disimpan spec di browser (bukan `[Reset to Default]`); spec yang menyimpan konfigurasi kolom: 097, 102, 107 sampai 111, 122, 138 sampai 141, dan 144 sampai 146.
- **State global:** hook `after` memulihkan state global yang diubah spec (limit, cap, format General Settings, capability role, lisensi FA-7 dan waktu seed, status Client, jam server bila digeser).

Setiap spec menyiapkan dan membersihkan datanya sendiri dan tidak bergantung pada hasil spec lain.
