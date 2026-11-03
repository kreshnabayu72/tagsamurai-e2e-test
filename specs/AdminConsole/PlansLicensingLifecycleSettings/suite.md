---
name: Admin Console Plans Licensing Lifecycle Settings
id: suite-admin-console-plans-licensing-lifecycle-settings
description: Spec e2e turunan tc-plans-licensing-lifecycle-settings.md untuk Admin Console > Plans & Licensing > Lifecycle Settings
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Plans Licensing Lifecycle Settings

Suite ini mencakup halaman Plans & Licensing > Lifecycle Settings dengan tujuh tab (Trial Settings, Free Plan Settings, License Timing, Client Lifecycle, Recycle Bin, Approval Settings, System Limits): navigasi tab dan deep link, nilai default instalasi baru, tooltip dan Guided Tooltip, visibilitas dan eksekusi per role, validasi field, Save dan Reset to Default, validasi relasi antar-field, warning note, dialog Unsaved Changes, modal Changelog (Search, Filter, Sort, Setup Column, Pagination, Download), pencatatan di Activity Log dan System Log, format tanggal General Settings, otorisasi dan validasi sisi server, konkurensi dua admin, serta perilaku konsumen lintas modul (Activate Trial, Approval timeout, job Client Lifecycle, email, Recycle Bin, System Limits).

`parallel: false` karena ketujuh tab adalah satu set pengaturan platform-wide (satu baris per tab): setiap spec yang menyimpan atau mereset konfigurasi, menyeed dataset Changelog, mengubah General Settings (Date Format, Time Format, Time Zone), menggeser jam server dan jam browser, atau memicu job lifecycle memakai state global. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `global-hooks/before`: health check environment (di luar suite ini).
- `hooks/before`: login akun aktor default suite Total Control (`AC_TC_PASSWORD`) lewat `seedSession`; menyatakan kemampuan sesi API aktor (login API password untuk akun yang sama tanpa mengusir sesi UI, disediakan tim BE/FE); menyetel flag Guided Tooltip halaman Lifecycle Settings (`guided_tooltip_seen_<page_key>`) true untuk akun aktor yang dipakai suite. Spec yang menguji flag itu sendiri menulis pengecualiannya dan mengaturnya sesudah hook. Spec dengan akun aktor lain login akun itu di hook `before` spec dan hook `after` spec mengembalikan sesi ke akun default suite.
- `hooks/beforeEach`: memulihkan ketujuh tab ke nilai default lewat Fixture BE (kemampuan disediakan tim FE/BE); memulihkan jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept; membuka Plans & Licensing > Lifecycle Settings (tab Trial Settings aktif); sebagai jaring pengaman mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` (bukan pengganti langkah pemulihan spec, S-09). Klik sidebar mereset Search, Sort, dan Filter modal Changelog. Pengecualian layar awal: spec 018 (Precondition TC 58 sampai 61: halaman utama setelah login), spec 019 dan 020 (akun aktor tanpa capability, layar awal halaman utama setelah login, atau akses langsung ke URL), dan spec 161 (akun Client, client console) tidak memakai langkah "membuka Lifecycle Settings" dari hook ini; ketiganya tetap memakai pemulihan nilai, jam, General Settings, dan intercept hook ini, dan membuka layar awalnya sendiri di hook `before` spec atau langkah spec.
- `hooks/after`: memulihkan ketujuh tab ke nilai default, jam, General Settings, dataset Changelog ke keadaan awal, antrean job, dan flag Guided Tooltip; menghapus preferensi kolom Setup Column modal Changelog di browser (bukan `[Reset to Default]`); mengembalikan sesi ke akun default suite.
- Entri Changelog, System Log, dan Activity Log bersifat permanen: spec memakai baseline jumlah entri sebelum aksi, bukan angka absolut (S-12).
