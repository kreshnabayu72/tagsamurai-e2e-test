---
name: Admin Console Settings Privacy Policy
id: suite-admin-console-settings-privacy-policy
description: Spec e2e turunan tc-settings-privacy-policy.md untuk Admin Console > Settings > Privacy Policy
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Settings Privacy Policy

Suite ini mencakup halaman Settings > Privacy Policy: tabel Version History (Search, Filter, Sort, Pagination, Setup Column, Download), Modal View dan Modal Edit dengan Rich Text Editor, first-time setup, Publish New Version beserta Dialog Publish Confirm, idempotency, no-op dan normalisasi, Role Matrix, pencatatan log di Activity Log dan System Log, sanitasi konten server-side, format tanggal General Settings, konkurensi dua admin, aturan khusus aplikasi Android, serta ketahanan terhadap kegagalan server.

`parallel: false` karena dokumen Privacy Policy bersifat tunggal platform-wide: setiap spec yang mem-publish, men-seed ulang Riwayat versi, mengubah General Settings (Date Format, Time Zone, Time Format), mengubah capability role, atau menggeser jam server memakai state global. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.
