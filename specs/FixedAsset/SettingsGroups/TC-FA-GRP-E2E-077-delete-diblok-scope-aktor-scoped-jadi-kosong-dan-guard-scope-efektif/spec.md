---
id: TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif
title: "Delete Diblok: Scope Aktor Scoped Menjadi Kosong, Aktor dengan Lebih dari Satu Node Scope, dan Scope Efektif Tidak Menghitung Role Non-Manage Group"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-236
  - TC-FA-GRP-237
  - TC-FA-GRP-961
  - TC-FA-GRP-1058
coverage:
  web: automated
---

# Delete Diblok: Scope Aktor Scoped Menjadi Kosong, Aktor dengan Lebih dari Satu Node Scope, dan Scope Efektif Tidak Menghitung Role Non-Manage Group

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Group Manager dengan scope hanya `Solo Scope` (akun client Pre-setup yang scope-nya diatur spec; email tidak tertulis di Pre-setup TC dan disediakan tim FE, `Spectra.env.FA_GM_SOLO_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Akun ganti (langkah 8, 17, 26; hook `after` mengembalikan sesi ke akun default suite; semua akun disediakan tim FE karena tidak tertulis di Pre-setup TC):

| TC | Role dan scope | Env var password |
|---|---|---|
| TC-236 | Group Manager, scope hanya `Solo Scope` | `Spectra.env.FA_GM_SOLO_PASSWORD` |
| TC-961 | Manage Group C/R/U/D hanya di `Solo Scope 2`; sekaligus Transaction Role approver (Transfer) di `Warehouse A`, tanpa Manage Group atau Group Manager di sana | `Spectra.env.FA_MGCRUD_SOLO2_PASSWORD` |
| TC-1058 | Manage Group C/R/U/D hanya di `Solo Scope 3`; sekaligus Group Role Asset Admin (tanpa capability Manage Group) di `Warehouse A` | `Spectra.env.FA_MGCRUD_SOLO3_PASSWORD` |
| TC-237 | Group Manager dengan dua node scope level 1 (Pre-setup No 23): `Head Office` dan `Del Scope Own` | `Spectra.env.FA_GM_WN_PASSWORD` |

- Flag Guided Tooltip `fa-settings-groups` untuk akun hasil ganti akun (langkah 8, 17, 26): disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); akun pertama mengikuti hook suite.
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset dan tanpa user lain): `Solo Scope`, `Solo Scope 2`, `Solo Scope 3` (masing-masing menjadi satu-satunya scope aktor TC-nya) dan `Del Scope Own` (group level 1 kosong milik spec ini, dibuat di `before` dan di-assign ke aktor TC-237 sebagai node scope kedua selain `Head Office`; target Delete TC-237). Penetapan scope tiap akun dan penetapan Transaction Role atau Group Role di `Warehouse A` dilakukan seeding API (disediakan tim FE/BE). `Warehouse A` (Pre-setup No 9) hanya dibaca.
- Cleanup di `after`: hapus data milik spec dan lepas assignment seed lewat API.

## Test Steps

### TC-FA-GRP-236: Scope aktor Group Manager menjadi kosong

1. Verifikasi `Solo Scope` tampil di tabel (group dalam scope aktor)
2. Buka elipsis `⋯` baris `Solo Scope`, pilih `Delete`
3. Verifikasi dialog dengan title "Cannot Delete Group"
4. Verifikasi isi dialog "You can't delete the only group you're assigned to. Ask an admin to assign you another group first."
5. Verifikasi dialog hanya memuat tombol [OK]
6. Klik [OK]
7. Verifikasi `Solo Scope` tetap ada di tabel (tidak ada yang terhapus)

### TC-FA-GRP-961: Scope-empty tetap berlaku walau aktor Transaction Role approver di node lain

8. Logout, lalu login sebagai Manage Group C/R/U/D `Solo Scope 2` (juga Transaction Role approver di `Warehouse A`)
9. Buka Fixed Asset > Settings > Groups
10. Verifikasi `Solo Scope 2` tampil di tabel (group dalam scope aktor)
11. Buka elipsis `⋯` baris `Solo Scope 2`, pilih `Delete`
12. Verifikasi dialog dengan title "Cannot Delete Group"
13. Verifikasi isi dialog "You can't delete the only group you're assigned to. Ask an admin to assign you another group first."
14. Verifikasi dialog hanya memuat tombol [OK]
15. Klik [OK]
16. Verifikasi `Solo Scope 2` tetap ada di tabel (tidak ada yang terhapus)

### TC-FA-GRP-1058: Scope-empty tidak menghitung Group Role non-Manage Group

17. Logout, lalu login sebagai Manage Group C/R/U/D `Solo Scope 3` (juga Group Role Asset Admin di `Warehouse A`)
18. Buka Fixed Asset > Settings > Groups
19. Verifikasi `Solo Scope 3` tampil di tabel (group dalam scope aktor)
20. Buka elipsis `⋯` baris `Solo Scope 3`, pilih `Delete`
21. Verifikasi dialog dengan title "Cannot Delete Group"
22. Verifikasi isi dialog "You can't delete the only group you're assigned to. Ask an admin to assign you another group first."
23. Verifikasi dialog hanya memuat tombol [OK]
24. Klik [OK]
25. Verifikasi `Solo Scope 3` tetap ada di tabel (tidak ada yang terhapus)

### TC-FA-GRP-237: Aktor dengan lebih dari satu node scope tidak kena guard scope-empty

26. Logout, lalu login sebagai Group Manager dengan dua node scope level 1 (`Head Office` dan `Del Scope Own`; Pre-setup No 23)
27. Buka Fixed Asset > Settings > Groups
28. Buka elipsis `⋯` baris `Del Scope Own`, pilih `Delete`
29. Verifikasi dialog konfirmasi normal dengan isi "Are you sure you want to delete it? This action cannot be undone."
30. Klik [Delete]
31. Verifikasi toast sukses "Success, group has been deleted."

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 8 dan 9, 17 dan 18, 26 dan 27: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Ganti akun ditulis eksplisit (langkah 8, 17, 26, S-07); akun pertama login di hook `before`. Urutan: TC-237 terakhir karena satu-satunya yang menghapus data (S-10).
- Verifikasi langkah 1, 10, 19 adalah anchor positif untuk asersi "tidak ada yang terhapus" (8b butir 2): group tampil sebelum aksi dan tetap tampil sesudah [OK] (langkah 7, 16, 25).
- Temuan untuk QA:
  - Akun TC-236, TC-961, dan TC-1058 tidak tertulis di Pre-setup TC; disediakan tim FE. Email akun TC-237 (Pre-setup No 23) disediakan tim FE/QA.
  - TC-961 dan TC-1058: penjelasan dalam kurung di Expected b (Transaction Role approver atau Group Role Asset Admin tidak dihitung ke scope efektif) adalah alasan, bukan asersi terpisah; teramati lewat dialog blokir.
