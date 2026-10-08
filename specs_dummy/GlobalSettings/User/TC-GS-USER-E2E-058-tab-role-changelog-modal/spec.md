---
id: TC-GS-USER-E2E-058-tab-role-changelog-modal
title: 'Modal Changelog User > Role: kolom, Action, Filter, Search, Download, Setup Column, dan sinkron'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-568
  - TC-GS-USER-569
  - TC-GS-USER-570
  - TC-GS-USER-571
  - TC-GS-USER-572
  - TC-GS-USER-573
  - TC-GS-USER-574
coverage:
  web: automated
---

# Modal Changelog User > Role: kolom, Action, Filter, Search, Download, Setup Column, dan sinkron

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Ahmad Fauzi" punya riwayat Role: Edit `Manage TAG` Update, Assign `Manage TAG`, Remove `Manage files`, serta Assign dan Remove lewat Total Control dan lewat Read Only
- User "Wati Tanpa Riwayat" tanpa riwayat Role apa pun
- Spec ini mengubah role "Wati Tanpa Riwayat" pada langkah akhir dan mengembalikannya

## Test Steps

### Tampilan dan isi

1. Buka User Detail "Ahmad Fauzi" > Tab Role lalu klik ikon Changelog di toolbar
2. Verifikasi header "Changelog: Ahmad Fauzi > Role" dengan tombol tutup, toolbar Search, Filter, Download, kolom Date, Action, Role, Field, Old Value, New Value, Modified By, urutan Date terbaru dulu, dan pagination default 10
3. Verifikasi ada 7 jenis Action: `Edit` (Field [Permission], `Inactive` ke `Active`), `Assign` (Access, `—` ke `Assigned`), `Remove` (Access, `Assigned` ke `—`), `Assign (via Total Control)`, `Assign (via Read Only)`, `Remove (via Total Control)`, `Remove (via Read Only)`, dan kolom Role berisi nama role, serta tidak ada baris Auto-Revert

### Search

4. Verifikasi placeholder "Search action, role, field, or value..."
5. Cari kata kunci dari kolom Action, Role, Field, Old Value, New Value, Modified By, lalu cari teks tanggal
6. Verifikasi pencarian kolom teks menemukan baris terkait, sedangkan pencarian tanggal tidak menemukan apa pun

### Filter

7. Buka Filter dan verifikasi Action multi-select berisi 7 nilai serta Role multi-select berisi 6 role (Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role)
8. Terapkan filter Field, Modified By, dan rentang tanggal, lalu kombinasikan beberapa field
9. Verifikasi hasil memakai AND antar field dan OR dalam satu field

### Download dan Setup Column

10. Filter Action `Assign`, lalu Download CSV dan XLSX
11. Verifikasi nama berkas `Changelog-User-Ahmad-Fauzi-Role` (.csv dan .xlsx), isinya hanya baris hasil filter, dan tidak ada toast sukses
12. Buka Column Visibility, verifikasi 7 kolom bisa di-Hide, lalu Hide `Old Value` dan Pin `Date`
13. Buka modal Changelog User dari toolbar User List dan verifikasi pengaturan kolom di sana tidak terpengaruh, begitu pula sebaliknya

### Empty state dan sinkron dari edit

14. Buka modal Changelog Role untuk "Wati Tanpa Riwayat"
15. Verifikasi empty state "No changelog yet" dengan deskripsi "Activities and changes will appear here."
16. Tutup modal, centang `Update` pada baris `Manage TAG` di Tab Role, lalu buka modal lagi
17. Verifikasi ada baris `Edit` untuk `Manage TAG` dengan Field `Update`, `Inactive` ke `Active`, dan Modified By admin yang login
18. Cari kata yang tidak ada di riwayat dan verifikasi "No results found" dengan deskripsi "Try adjusting your search or filter."
19. Hapus centang `Update` untuk mengembalikan data awal

## Notes

- Sumber `user.md` bagian 4.2, 4.2a, 8.2a, dan 7.1. Baris Auto-Revert tidak tampil di modal ini dan diverifikasi di `TC-GS-USER-E2E-055-tab-role-auto-revert` (`TC-GS-USER-575`).
- Edit yang mengubah data ditaruh paling akhir.
