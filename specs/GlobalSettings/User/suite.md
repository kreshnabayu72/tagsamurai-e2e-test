---
name: Global Settings User
id: suite-global-settings-user
description: Spec e2e turunan tc-user.md untuk Global Settings > User > User List (Login User)
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings User

Suite ini mencakup tab User List (sub-tab Login User) dan User Detail pada Global Settings > User: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit, Remove Access, Pending Email Change, Toggle Active dan Temporary User, Delete single dan Bulk Action, Resend email, pairing TAG, Reset Authenticator, foto, Custom Field inline, Tab Role, Tab Responsibilities dan sub-tab asetnya, Tab Non-Login User, Modal Changelog User dan User > Role, Tab Changelog, System Log, dan User Log, Role Matrix, Guided Tooltip, pencatatan log di Changelog, System Log, User Log, dan Activity Log, sinkronisasi lintas modul, defense-in-depth, state tenant, ketahanan terhadap kegagalan server, serta konflik antar admin.

`parallel: false` karena spec mengubah state global (jam server dan jam browser, plan dan status Client, format tanggal General Settings, Master Data Count Limit dan Selection Limit, counter lock Change Password, Default User) dan men-seed populasi user yang tampil di tabel bersama. Spec yang menghapus data (Delete, Bulk Delete, Remove Access) dijalankan sesudah spec lain. Spec screening User List (001) dan spec pencatatan log dijalankan sebelum spec yang mengedit Default User, karena TC-GS-USER-1043 dan TC-GS-USER-1044 mengasersi Default User seed yang belum pernah diedit. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`) dan menyetel flag Guided Tooltip `gs-user` menjadi `seen` untuk akun aktor yang dipakai suite, supaya walkthrough otomatis tidak menutupi layar. Mekanisme penyetelan flag disediakan tim FE/BE. Spec Guided Tooltip (005 dan 006) mengatur flag sendiri sesudah hook ini.
- `after`: memulihkan flag Guided Tooltip ke nilai awal tiap akun dan mengembalikan sesi ke akun default suite.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya.
