---
name: Global Settings Division
id: suite-global-settings-division
description: E2E test cases derived from tc-division.md and division.md for Global Settings > User > Division
executionOrder: 1.4
parallel: false
---

# Suite: Global Settings Division

Suite ini mencakup tab `Division` di `Global Settings > User`: katalog divisi organisasi yang menyimpan atribut `Name` (wajib, unik, maks 120 karakter) dan `Code` (opsional, auto-generate saat kosong, whitelist `-_.`, maks 15 karakter), beserta tabel utama T-DIV-01, modal Changelog T-DIV-02, seluruh operasi CRUD (Create, Edit, Delete single, Bulk Delete) dengan proteksi ketat `DIV-LOGIC-02` (in-use delete guard), aturan tabel (search on Enter, filter Last Updated, sorting 3-state, pagination, download CSV/XLSX, Setup Column 3 fase), Role Matrix capability "Manage user and role", pencatatan audit log di Changelog dan Activity Log Global Settings, sinkronisasi dua arah ke dropdown form User & Non-Login User, serta matriks edge case, keamanan pertahanan mendalam (defense-in-depth), dan antarmuka responsif mobile Android.

Division bukan menu sidebar terpisah, melainkan sub-tab di dalam halaman `Global Settings > User > Division` (`User > Division`), sejajar dengan tab "User List", "Position", dan "Custom Field". Seluruh spec dalam suite ini dijalankan dengan asumsi aktor telah berada di konteks halaman tersebut.

Konfigurasi `parallel: false` ditetapkan karena:
- Data seed Division dipakai bersama oleh banyak spec: divisi in-use (`Human Resources`, `Operations`, `Compliance`) harus tetap ada untuk menguji dialog pemblokiran D-02, sementara divisi bebas relasi (`Finance`, `Legal`, `Treasury`) dipakai sebagai target pengujian edit dan delete.
- Spec 021 menjalankan populasi batch 26 divisi, dan spec 022 memvalidasi `Master Data Count Limit` yang bersifat global per entitas. Menjalankan spec secara paralel akan membuat spec lain terblokir oleh Dialog 6 "Limit Reached".
- Pengujian audit trail (Changelog dan Activity Log) memvalidasi urutan kronologis baris log. Mutasi data bersamaan dari spec lain akan mengacaukan assertion urutan log.
- Preferensi Setup Column disimpan di browser per pengguna per tabel. Perubahan urutan atau visibilitas kolom yang belum di-reset akan memengaruhi spec lain jika dieksekusi bersamaan.

## Mode Eksekusi

- **Spec FE+BE** (60 spec) — dijalankan terhadap backend nyata dengan database seeding terisolasi.
- **Spec `Mode: mock`** (16 spec) — dijalankan dengan intersep mock `Spectra.intercept()` untuk kondisi yang tidak dapat dipicu secara deterministik di live environment: loading skeleton 3s, error fetch 500, tooltip hover, guided tooltip walkthrough, server 500 / timeout resilience pada Create/Edit/Delete/Bulk Delete/Export, DOM injection sanitization, dan emulasi layout mobile Android (<768px). Kebutuhan mock dicatat eksplisit pada `## Prerequisites` masing-masing spec.
