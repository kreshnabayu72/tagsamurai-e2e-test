---
id: TC-GS-USER-E2E-110-changelog-modal-filter
title: 'Modal Changelog User List: Filter Date, Action, Name, Modified By, Field, dan kombinasi'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-234
  - TC-GS-USER-235
  - TC-GS-USER-236
  - TC-GS-USER-237
  - TC-GS-USER-238
  - TC-GS-USER-239
  - TC-GS-USER-240
  - TC-GS-USER-241
  - TC-GS-USER-257
  - TC-GS-USER-558
coverage:
  web: automated
---

# Modal Changelog User List: Filter Date, Action, Name, Modified By, Field, dan kombinasi

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Riwayat Changelog memuat banyak jenis Action, Field beragam, tanggal tersebar, dan aktor `System` (Auto-Deactivate)
- User "Doni Pratama" belum punya riwayat apa pun
- Spec ini tidak mengubah data

## Test Steps

1. Klik ikon Changelog di toolbar User List lalu buka Filter
2. Ketik `abc123` di field Date
3. Verifikasi hanya date picker yang menerima input dan teks tidak masuk
4. Buka dropdown Action
5. Verifikasi opsi mencakup semua Action yang pernah tercatat (Create, Edit, Delete, Toggle Active, Remove Access, Resend Email, TAG Pair, TAG Unpair, Reset Authenticator, Photo Update, dan seterusnya)
6. Pilih "Deactivate" lalu Apply dan verifikasi hanya baris Action itu yang tampil
7. Ketik di pencarian dalam dropdown Action dan pilih dua opsi
8. Verifikasi opsi tersaring dan hasil Apply memakai OR dalam satu field
9. Pilih empat opsi Action atau lebih lalu Apply
10. Verifikasi chip terpilih tampil dengan overflow "+N more", lalu klik `(X)` pada satu chip dan verifikasi hanya satu opsi terlepas
11. Buka dropdown Action dan hapus centang satu opsi di dalam dropdown
12. Verifikasi chip yang bersangkutan langsung hilang
13. Buka dropdown Name
14. Verifikasi opsi hanya berisi user yang punya entri di Changelog ("Doni Pratama" tanpa riwayat tidak muncul)
15. Buka dropdown Modified By, pilih `System`, lalu Apply
16. Verifikasi opsi mencakup semua aktor termasuk `System` dan hanya baris beraktor `System` yang tampil
17. Pilih rentang tanggal lalu Apply
18. Verifikasi hanya baris dalam rentang itu yang tampil
19. Pilih Action `Edit` dan Modified By salah satu aktor lalu Apply
20. Verifikasi hasilnya irisan kedua kriteria (AND antar field)
21. Pilih Field dua nilai atau lebih (mis. `Position`, `Email`) lalu Apply
22. Verifikasi hanya baris dengan Field terpilih yang tampil (OR)

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.5 dan 9.6.
