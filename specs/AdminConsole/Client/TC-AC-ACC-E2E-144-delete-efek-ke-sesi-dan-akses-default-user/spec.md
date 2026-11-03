---
id: TC-AC-ACC-E2E-144-delete-efek-ke-sesi-dan-akses-default-user
title: "Delete Client Archived: Efek ke Sesi Default User (Dialog Account no longer Active, Sesi Tetap Aktif) dan App Access Dicabut"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-229
  - TC-AC-ACC-230
  - TC-AC-ACC-658
coverage:
  web: automated
---

# Delete Client Archived: Efek ke Sesi Default User (Dialog Account no longer Active, Sesi Tetap Aktif) dan App Access Dicabut

## Prerequisites

- Mode: FE+BE.
- Konteks (kelas c, dua sesi paralel yang diasersi): Browser A (admin) dan Browser B (user Client) berjalan bersamaan pada TC-AC-ACC-230 dan 658.
- Akun aktor Browser A: Archived-Delete-Only A-10 `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ARCHIVED_DELETE_PASSWORD` (Manage archived client: Delete + Read, exact-match Area Jakarta). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Akun Browser B (login lewat langkah eksplisit, ditutup di akhir tiap blok; S-09):

| TC | Akun | Email | Env password | Client |
|---|---|---|---|---|
| TC-AC-ACC-230 | Client Default User A-LIF-2 | `clientDefaultUser_automated_ptPenggunaTunggal@qwertysystem.net` | `AC_CLIENT_LIF2_PASSWORD` | C-LIF-18 `PT Pengguna Tunggal` (Archived; 1 user ber-App Access; Default User tanpa peran di entitas lain; Dikonsumsi) |
| TC-AC-ACC-658 | Client Default User A-LIF-1 | `clientDefaultUser_automated_ptBerbagiPengguna@qwertysystem.net` | `AC_CLIENT_LIF1_PASSWORD` | C-LIF-17 `PT Berbagi Pengguna` (Archived; 1 user ber-App Access; email Default User juga terdaftar di entitas lain; Dikonsumsi) |

- Data lain: TC-AC-ACC-229 memakai Client Archived milik spec `PT Hapus Berbagi {runId}-144` (Archived, 1 user ber-App Access, email Default User juga terdaftar di entitas lain), di-seed lewat API di hook `before` (TC tidak menyebut Client; lihat Temuan). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-LIF-17 dan C-LIF-18 di hook `before` dan `after` (tanpa syarat; Client dihapus oleh TC).
- Kemampuan teknis: Browser B dengan sesi platform aktif (Portal) dan sesi produk Client; membaca state App Access dan keberadaan Default User di Global Settings lewat Fixture BE (kemampuan "disediakan tim FE/BE", tanpa endpoint karangan); login ke entitas lain tempat A-LIF-1 memiliki peran.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-229: Delete: Default User yang punya peran di entitas lain tidak ikut dihapus

1. [Browser A] Klik sub-tab Archived, ketik Search `PT Hapus Berbagi {runId}-144`, tekan Enter
2. [Browser A] Klik `[⋯]` pada baris `PT Hapus Berbagi {runId}-144` → klik `Delete`
3. [Browser A] Ketik nama persis `PT Hapus Berbagi {runId}-144` pada input "Type the client name to confirm", centang "I understand this action cannot be undone", klik `[Delete]`
4. [Browser A] Tunggu aksi selesai (toast sukses "Success, client has been deleted." tampil)
5. Verifikasi App Access user Client dicabut (dibaca lewat Fixture BE)
6. Verifikasi Default User tetap ada

### TC-AC-ACC-230: Delete Client yang Default User-nya ikut terhapus: sesi user Client berakhir dengan dialog "Account no longer Active"

7. [Browser B] Login sebagai A-LIF-2 dan buka halaman produk Client `PT Pengguna Tunggal`
8. [Browser A] Klik sub-tab Archived, ketik Search `PT Pengguna Tunggal`, tekan Enter
9. [Browser A] Klik `[⋯]` pada baris `PT Pengguna Tunggal` → klik `Delete`
10. [Browser A] Verifikasi dialog Delete menampilkan "This client has 1 user(s) with product access. This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
11. [Browser A] Ketik nama persis `PT Pengguna Tunggal`, centang "I understand this action cannot be undone", klik `[Delete]`
12. [Browser A] Verifikasi toast sukses "Success, client has been deleted."
13. [Browser B] Verifikasi dialog "Account no longer Active" tampil tanpa muat ulang halaman
14. [Browser B] Klik `[OK]` pada dialog "Account no longer Active"
15. [Browser B] Verifikasi Browser B diarahkan ke halaman Login
16. [Browser B] Login ulang sebagai A-LIF-2
17. [Browser B] Verifikasi login ulang ditolak
18. [Browser B] Tutup jendela Browser B dan hapus sesi login-nya

### TC-AC-ACC-658: Delete Client yang Default User-nya punya peran di entitas lain: sesi platform tetap aktif tanpa dialog dan login ke entitas lain berhasil

19. [Browser B] Login sebagai A-LIF-1 dan buka halaman Portal
20. [Browser A] Klik sub-tab Archived, ketik Search `PT Berbagi Pengguna`, tekan Enter
21. [Browser A] Klik `[⋯]` pada baris `PT Berbagi Pengguna` → klik `Delete`
22. [Browser A] Verifikasi dialog Delete menampilkan "This client has 1 user(s) with product access. This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
23. [Browser A] Ketik nama persis `PT Berbagi Pengguna`, centang "I understand this action cannot be undone", klik `[Delete]`
24. [Browser A] Verifikasi toast sukses "Success, client has been deleted."
25. [Browser B] Muat ulang halaman Portal
26. [Browser B] Verifikasi Portal termuat ulang tanpa dialog "Account no longer Active"
27. [Browser B] Verifikasi Browser B tidak dialihkan ke halaman Login
28. [Browser B] Login ke entitas lain tempat A-LIF-1 memiliki peran
29. [Browser B] Verifikasi login ke entitas lain berhasil
30. [Browser B] Tutup jendela Browser B dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Browser A]` dan `[Browser B]` menandai konteks.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tiga TC satu topik (efek Delete ke Default User dan sesinya); aksi Delete menghabisi data dan tiap blok memakai Client sendiri sehingga blok tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" (langkah 4), `[OK]` pada dialog Browser B (langkah 14), dan penutupan Browser B (langkah 18 dan 30; S-09). Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-229: `-`; TC-AC-ACC-230 butir a sampai c (App Access dicabut, Default User dihapus, seed ulang) dan TC-AC-ACC-658 butir a sampai c tanpa langkah observasi di TC tidak diasersi selain Expected (seed ulang dilakukan di hook).
- Temuan untuk QA:
  - TC-AC-ACC-229 tidak menyebut Client Archived, langkah Delete yang rinci, maupun cara mengamati "App Access dicabut" dan "Default User tetap ada"; spec memakai Client bersuffix milik spec dan kemampuan baca state BE "disediakan tim FE/BE" (S-11), dan menyalin langkah Delete dari TC-AC-ACC-230 dan 658 (S-04).
  - TC-AC-ACC-230 Expected c ("Browser B (tanpa muat ulang halaman)") bergantung pada mekanisme pembaruan sesi (event atau polling) yang tidak dijelaskan di TC.
