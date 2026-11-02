---
id: TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning
title: "Delete Group: Dialog Warning User Ter-Scope, Warning User di Descendant, dan [Cancel] pada Dialog Warning"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-223
  - TC-FA-GRP-224
  - TC-FA-GRP-1033
coverage:
  web: automated
---

# Delete Group: Dialog Warning User Ter-Scope, Warning User di Descendant, dan [Cancel] pada Dialog Warning

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): `Del Users` (tanpa aset aktif, dua user ber-Group Role di node: `User GR 1` dan `User GR 2`, email `userGr1+{runId}-072@qwertysystem.net` dan `userGr2+{runId}-072@qwertysystem.net`); `Del Users Parent` dengan child `Del Users Child` (tanpa aset; di child: `User GR 3` ber-Group Role, `User GM 1` ber-tier Group Manager, dan `User TR 1` ber-Transaction Role approver, email bersuffix `{runId}-072`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog user pada Settings > Role & Permission sebelum dan sesudah aksi (audit trail permanen; 8b butir 10). Password user seed tidak dipakai (spec hanya membaca Role & Permission).
- Baseline log: N0 = jumlah entri Changelog `User GR 1` yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12).
- Cleanup di `after`: hapus data milik spec yang tersisa (`Del Users`, user seed) lewat API.

## Test Steps

### Baseline Changelog user

1. Buka Settings > Role & Permission, pilih `User GR 1`, klik icon Changelog
2. Verifikasi sedikitnya satu entri tampil di Changelog `User GR 1`
3. Catat jumlah entri Changelog `User GR 1` sebagai baseline N0
4. Tutup Changelog dan buka Fixed Asset > Settings > Groups

### TC-FA-GRP-223: Screening dialog Warning Delete, user ter-scope

5. Buka elipsis `⋯` baris `Del Users`, pilih `Delete`
6. Verifikasi dialog dengan title "Delete Group", bullet `Del Users`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?", tombol [Cancel] dan [Delete]

### TC-FA-GRP-1033: [Cancel] pada dialog Warning

7. Klik [Cancel] pada dialog
8. Verifikasi dialog tertutup
9. Verifikasi `Del Users` tetap ada di tabel
10. Verifikasi `Del Users` tetap ada di sidebar
11. Verifikasi tidak ada toast yang tampil
12. Buka Settings > Role & Permission, pilih `User GR 1`
13. Verifikasi Group Role `User GR 1` di `Del Users` tidak dicabut
14. Klik icon Changelog
15. Verifikasi jumlah entri Changelog `User GR 1` sama dengan baseline N0 (tanpa baris Delete baru)
16. Tutup Changelog dan buka Fixed Asset > Settings > Groups

### TC-FA-GRP-224: Warning untuk user ter-scope di descendant, lalu commit

17. Buka elipsis `⋯` baris `Del Users Parent`, pilih `Delete`
18. Verifikasi dialog varian warning memuat himpunan node dan descendant: title "Delete Group", bullet `Del Users Parent` dan `Del Users Child`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?"
19. Klik [Delete] pada dialog warning
20. Verifikasi toast sukses "Success, group has been deleted."
21. Verifikasi `Del Users Parent` dan `Del Users Child` terhapus dari tabel dan sidebar
22. Buka Settings > Role & Permission, pilih `User GR 3`
23. Verifikasi assignment Group Role `User GR 3` terlepas
24. Buka Settings > Role & Permission, pilih `User GM 1`
25. Verifikasi assignment Group Manager `User GM 1` terlepas
26. Buka Settings > Role & Permission, pilih `User TR 1`
27. Verifikasi assignment Transaction Role `User TR 1` terlepas

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 12, 14, 16, 22, 24, 26: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: TC-223 dan TC-1033 memakai satu pembukaan dialog `Del Users` (diasersi lalu dibatalkan); Delete yang menghapus data (TC-224) paling akhir (S-10).
- Klausa "tanpa toast dan tanpa baris Delete baru di Changelog" (TC-1033) diasersi pada langkah 11 dan 15; anchor positif: langkah 2 (entri lain tampil) dan langkah 9 (`Del Users` tetap ada). Baris hilang sesudah Delete memakai toast sukses sebagai anchor (8b butir 2).
- Temuan untuk QA:
  - TC-1033 langkah 5 ("Klik icon Changelog") tidak menyebut Changelog mana; spec memakai Changelog user pada Role & Permission sesuai langkah 4 TC. Changelog Group tidak diasersi.
  - TC-224 Expected c menyebut Transaction Role, sedangkan Precondition hanya menyebut user Group Role dan Group Manager; spec menambah `User TR 1` ber-Transaction Role di seeding supaya Expected c dapat diasersi.
  - TC-224 Post Condition (entri log pencabutan per assignment dan tidak ada notifikasi in-app) tidak punya langkah observasi; tidak diasersi (S-01).
