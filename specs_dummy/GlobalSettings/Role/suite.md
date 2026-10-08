---
name: Global Settings Role & Permission
id: suite-global-settings-role
description: E2E test cases derived from tc-role.md and role.md for Global Settings > Role & Permission
executionOrder: 1.4
parallel: false
---

# Suite: Global Settings Role & Permission

Suite ini mencakup modul `Role & Permission` di `Global Settings`: manajemen hak akses dan peran pengguna organisasi yang mencakup:
- **Tab Total Control:** Pengguna dengan hak penuh atas seluruh modul dan pengaturan (Default User selalu Total Control, tidak dapat dicabut/diedit).
- **Tab Read Only:** Pengguna dengan mode baca murni atas seluruh pengaturan Global Settings tanpa hak mutasi tulis.
- **Tab System:** Katalog 6 peran sistem tetap alfabetis (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) dengan hitungan pengguna aktif/nonaktif.
- **Halaman Detail Role:** Matriks penugasan peran granular dengan kolom CRUD dinamis (Create, Read, Update, Delete) yang auto-save instan, aturan ketergantungan (Read terkunci jika aksi lain aktif), proteksi peran Total Control/Read Only, dan alur Auto-Revert (Dialog D-02 / D-04 / D-06).
- **Table User Picker:** Pemilihan pengguna multi-seleksi dengan pencarian toolbar, filter panel multi-kriteria, pengurutan 3-state, paginasi, dan validasi kelayakan kandidat atomik (V-10 / V-11).
- **Bulk Action Bar & Bulk Remove:** Seleksi massal lintas halaman, penegakan batas kuota kupon Selection Limit 100 baris, dialog konfirmasi varian regular (D-05) vs auto-revert (D-06), dan penanganan konkurensi sukses parsial/nol.
- **Aturan Tabel & Setup Kolom:** Pencarian toolbar case-insensitive, filter panel date range Last Updated & Temporary Until, siklus pengurutan 3-state pada seluruh kolom data, paginasi 10/25/50/100, ekspor unduhan WYSIWYG CSV/XLSX, dan preferensi kolom Setup Kolom 3 fase terisolasi per tabel.
- **Modal Changelog & Audit Trail:** Riwayat aktivitas mutasi pada 4 surface, filter dinamis per role, ekspor log, sinkronisasi lintas modul ke System Log dan Activity Log, serta immutability snapshot relasional pasca-rename user.
- **Keamanan & Pertahanan Mendalam:** Penolakan API direct request HTTP 403 untuk self-edit, mutasi Default User, pembatasan wewenang aktor, isolasi tenant lintas client, dan pembekuan workspace Client Suspended.
- **Konkurensi Antar-Admin & Realtime:** Mekanisme Last-Write-Wins, penolakan stale reference 404/403, idempotency pencabutan, dan sinkronisasi realtime SSE.

Konfigurasi `parallel: false` ditetapkan karena:
- Data seed akun Default User (`Budi Santoso`) dan aktor Total Control (`Ahmad Fauzi`) dipakai bersama sebagai baseline lintas pengujian hak akses.
- Pengujian mutasi tier hak akses (upgrade Read Only ke Total Control, pencabutan access level, dan mutasi CRUD pemicu Auto-Revert) memodifikasi status peran global pengguna uji.
- Penegakan batas kuota Selection Limit (100 baris) dan pengujian konkurensi dual session (`sessionA` vs `sessionB`) memerlukan isolasi lingkungan eksekusi sekuensial agar tidak menimbulkan flakiness atau race condition antar-runner.
- Preferensi browser Setup Column disimpan di localStorage per pengguna per tabel dan harus diverifikasi secara deterministik.

## Mode Eksekusi

- **Spec FE+BE** (80 spec) — dijalankan terhadap antarmuka dan backend nyata dengan seeding database dan dual session context terisolasi.
- **Spec `Mode: mock`** (17 spec) — dijalankan dengan intersep mock `Spectra.intercept()` untuk skenario network resilience (error 500 / timeout pada load, assign, edit CRUD, remove, bulk remove, dan download), loading skeleton 3 detik, hover tooltip visual, Setup Column DnD/freeze pin, serta isolasi background job ekspor >5.000 baris.
