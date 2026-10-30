---
id: TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail
title: "State Tenant Suspended: Write-Lockdown Aksi Tulis pada Detail Manage TAG"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-267
  - TC-GS-ROLE-268
  - TC-GS-ROLE-269
  - TC-GS-ROLE-270
coverage:
  web: automated
---

# State Tenant Suspended: Write-Lockdown Aksi Tulis pada Detail Manage TAG

## Prerequisites

- Mode: FE+BE. Kelas harness: state tenant (h), write-lockdown Client Suspended. Suite `parallel: false`.
- Akun aktor: Total Control pada Client C suspended (Pre-setup #16), email disediakan tim FE, password `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Client C (disediakan tim FE sebelum status Suspended, mengikuti Pre-setup Role): `Wawan Setiawan` (Active, Access Global Settings dicentang, tanpa baris role), `Doni Pratama` (baris Manage TAG: Read checked, Update unchecked), `Rina Putri` (Read Only, punya baris Manage TAG). Status Suspended Client C disetel tim FE; spec tidak mengubah status Client maupun data.
- Semua aksi tulis di spec ini ditolak server sehingga data tidak berubah; tidak ada Given, seeding, atau pemulihan data.
- Kemampuan teknis: muat ulang halaman saat Popup Assign masih berisi centangan (penanganan dialog `beforeunload` bila muncul disediakan tim FE).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan

1. Klik Tab `System`
2. Klik baris `Manage TAG` untuk membuka Detail "Manage TAG"

### TC-GS-ROLE-267: Assign Role saat client suspended ditolak

3. Klik `[+ Assign]`
4. Centang `Wawan Setiawan` pada Popup Assign
5. Klik `[Assign]`
6. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
7. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
8. Muat ulang halaman
9. Verifikasi baris `Doni Pratama` tampil di Detail "Manage TAG"
10. Verifikasi baris `Wawan Setiawan` tidak ada di Detail "Manage TAG"

### TC-GS-ROLE-268: Edit CRUD saat client suspended ditolak

11. Centang Update pada baris `Doni Pratama`
12. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
13. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
14. Muat ulang halaman
15. Verifikasi Update pada baris `Doni Pratama` tidak tercentang

### TC-GS-ROLE-269: Remove baris role saat client suspended ditolak

16. Klik Remove pada baris `Doni Pratama`
17. Klik `[Remove]` pada dialog
18. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
19. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
20. Muat ulang halaman
21. Verifikasi baris `Doni Pratama` tetap ada di Detail "Manage TAG"

### TC-GS-ROLE-270: Bulk Remove saat client suspended ditolak

22. Centang baris `Doni Pratama`
23. Centang baris `Rina Putri`
24. Klik `Bulk Action`
25. Klik `Remove`
26. Klik `[Remove]` pada dialog
27. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
28. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
29. Muat ulang halaman
30. Verifikasi baris `Doni Pratama` tetap ada di Detail "Manage TAG"
31. Verifikasi baris `Rina Putri` tetap ada di Detail "Manage TAG"

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: state tenant (h), prinsip 13h bagian 3 konvensi; keempat TC berbagi akun, Client, dan Detail yang sama. Aksi tulis access level (Tab Total Control dan Read Only) ada di spec `TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level`; tampilan baca ada di spec `TC-GS-ROLE-E2E-097-state-tenant-suspended-tetap-dapat-melihat`.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail "Manage TAG" (langkah 1 dan 2) dan memuat ulang halaman (langkah 8, 14, 20, 29). Muat ulang mempertahankan Detail yang terbuka (Detail adalah halaman tersendiri), membuang toast supaya toast error identik berikutnya tidak tertukar (S-09), dan mengosongkan Popup Assign, centangan, serta Bulk Action Bar.
- Butir Expected TC (a. toast, b. data tidak berubah, c. tidak ada tampilan khusus suspend) dipecah satu `Verifikasi` per klausa; toast diasersi segera sesudah aksi (bagian 8b butir 5). Absence `Wawan Setiawan` didahului baris pembanding `Doni Pratama` di surface yang sama (bagian 8b butir 2). Nilai awal Update `Doni Pratama` adalah unchecked (Pre-setup #10: Manage TAG R saja).
- Temuan untuk QA:
  - TC-267 sampai TC-270 tidak menyebut data Client C; spec mengasumsikan Client C memakai data setara Pre-setup Role, disediakan tim FE.
  - TC-270 langkah "centang 2 baris" tidak menyebut baris; spec memakai `Doni Pratama` dan `Rina Putri` (keduanya punya baris Manage TAG).
  - TC-267 sampai TC-270 tidak menyebut apakah muat ulang halaman mempertahankan Detail; spec mengasumsikan Detail memiliki URL sendiri.
