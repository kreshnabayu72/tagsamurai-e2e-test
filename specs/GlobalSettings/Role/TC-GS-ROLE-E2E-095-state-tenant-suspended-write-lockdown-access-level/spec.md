---
id: TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level
title: "State Tenant Suspended: Write-Lockdown Aksi Access Level pada Tab Total Control dan Read Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-263
  - TC-GS-ROLE-264
  - TC-GS-ROLE-265
  - TC-GS-ROLE-266
coverage:
  web: automated
---

# State Tenant Suspended: Write-Lockdown Aksi Access Level pada Tab Total Control dan Read Only

## Prerequisites

- Mode: FE+BE. Kelas harness: state tenant (h), write-lockdown Client Suspended. Suite `parallel: false`.
- Akun aktor: Total Control pada Client C suspended (Pre-setup #16), email disediakan tim FE, password `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Client C (disediakan tim FE sebelum status Suspended, mengikuti Pre-setup Role): `Wawan Setiawan` (Active, Access Global Settings dicentang, tanpa access level), `Maya Anggraini` (Total Control), `Rina Putri` (Read Only). Status Suspended Client C disetel tim FE; spec tidak mengubah status Client maupun data.
- Semua aksi tulis di spec ini ditolak server sehingga data tidak berubah; tidak ada Given, seeding, atau pemulihan data.
- Kemampuan teknis: muat ulang halaman saat Popup Assign masih berisi centangan (penanganan dialog `beforeunload` bila muncul disediakan tim FE).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-263: Assign Total Control saat client suspended ditolak

1. Klik Tab `Total Control`
2. Klik `[+ Assign]`
3. Centang `Wawan Setiawan` pada Popup Assign
4. Klik `[Assign]`
5. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
6. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
7. Muat ulang halaman
8. Klik Tab `Total Control`
9. Verifikasi baris `Maya Anggraini` tampil di Tab Total Control
10. Verifikasi baris `Wawan Setiawan` tidak ada di Tab Total Control

### TC-GS-ROLE-264: Assign Read Only saat client suspended ditolak

11. Klik Tab `Read Only`
12. Klik `[+ Assign]`
13. Centang `Wawan Setiawan` pada Popup Assign
14. Klik `[Assign]`
15. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
17. Muat ulang halaman
18. Klik Tab `Read Only`
19. Verifikasi baris `Rina Putri` tampil di Tab Read Only
20. Verifikasi baris `Wawan Setiawan` tidak ada di Tab Read Only

### TC-GS-ROLE-265: Remove Total Control saat client suspended ditolak

21. Klik Tab `Total Control`
22. Klik `(⋯)` pada baris `Maya Anggraini`
23. Klik `Remove`
24. Klik `[Remove]` pada dialog
25. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
26. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
27. Muat ulang halaman
28. Klik Tab `Total Control`
29. Verifikasi baris `Maya Anggraini` tetap ada di Tab Total Control

### TC-GS-ROLE-266: Remove Read Only saat client suspended ditolak

30. Klik Tab `Read Only`
31. Klik `(⋯)` pada baris `Rina Putri`
32. Klik `Remove`
33. Klik `[Remove]` pada dialog
34. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
35. Verifikasi halaman tidak menampilkan tampilan khusus suspend (banner, halaman pengganti, atau elemen khusus suspend)
36. Muat ulang halaman
37. Klik Tab `Read Only`
38. Verifikasi baris `Rina Putri` tetap ada di Tab Read Only

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: state tenant (h), prinsip 13h bagian 3 konvensi; keempat TC berbagi akun, Client, dan topik yang sama (aksi tulis access level ditolak).
- Spec melewati sekitar 35 langkah (38 langkah) karena empat blok berurutan, satu kelas harness, satu akun, dan tiap blok berdiri sendiri (tab, aksi, dan baris pembanding sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Aksi tulis Detail ada di spec `TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail`.
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih tab (langkah 1, 8, 11, 18, 21, 28, 30, 37) dan memuat ulang halaman (langkah 7, 17, 27, 36). Muat ulang membuang toast sehingga toast error identik pada blok berikutnya tidak tertukar (S-09) dan mengosongkan Popup Assign sebelum data dibaca.
- Butir Expected TC (a. toast, b. data tidak berubah, c. tidak ada tampilan khusus suspend) dipecah satu `Verifikasi` per klausa. Toast (state sementara) diasersi segera sesudah aksi, lalu butir c, lalu muat ulang dan butir b (bagian 8b butir 5). Absence `Wawan Setiawan` didahului baris pembanding yang tampil di tab yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-263 sampai TC-266 tidak menyebut data Client C (apakah `Wawan Setiawan`, `Maya Anggraini`, dan `Rina Putri` ada di Client C). Spec mengasumsikan Client C memakai data setara Pre-setup Role; disediakan tim FE.
  - TC-263 dan TC-264 tidak menyebut state Popup Assign sesudah ditolak (tetap terbuka atau tertutup); spec memverifikasi "data tidak berubah" sesudah muat ulang halaman.
  - TC-263 sampai TC-266 tidak menyebut cara membuka dialog Remove untuk baris Tab (spec memakai `(⋯)` > `Remove` > `[Remove]` seperti pola TC-GS-ROLE-298).
