---
name: Global Settings Activity Log
id: suite-global-settings-activity-log
description: Spec e2e turunan tc-activity-log.md untuk Global Settings > Activity Log (Tab Session dan Tab User Action)
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Activity Log

Suite ini mencakup halaman Activity Log Global Settings yang read-only: Tab Session dan Tab User Action (tabel, Search, Filter Panel, Sort, Setup Column, Pagination, Download), isi kolom per Activity dan per modul sumber, snapshot beku, Role Matrix, isolasi entitas, Guided Tooltip, tampilan mobile dan bahasa, format tanggal General Settings, sinkronisasi realtime, state tenant, defense-in-depth, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (format tanggal dan zona waktu General Settings, status Client suspended, plan Client, flag Guided Tooltip, jam server) dan memicu aksi di modul sumber yang menambah baris log. Spec yang menghapus data sumber (spec 062) dijalankan paling akhir. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Guided Tooltip: hook `before` suite mencatat nilai awal flag `seen` halaman Activity Log untuk akun aktor yang dipakai suite lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal. Spec yang login dengan akun lain (Read Only, Principal, Distributor, entitas log-terbatas, Client Alfa/Beta, akun plan) menyetel dan memulihkan flag yang sama untuk akun itu di hook `before`/`after` spec-nya, dan spec yang membuka halaman lain (mis. `Global Settings > User`, `Master Reference`) menyetel flag halaman tujuan itu dengan cara yang sama; keduanya ditulis satu baris di `## Prerequisites` spec yang bersangkutan. Nama flag (usulan `guided_tooltip_seen_gs-activity-log`) dikonfirmasi tim FE/BE. Spec yang bukan spec Guided Tooltip merujuk hook ini dengan satu baris di `## Prerequisites`; spec 005 dan 006 mengatur flag sendiri sesudah hook.
- Login akun aktor suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`) dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun itu.
