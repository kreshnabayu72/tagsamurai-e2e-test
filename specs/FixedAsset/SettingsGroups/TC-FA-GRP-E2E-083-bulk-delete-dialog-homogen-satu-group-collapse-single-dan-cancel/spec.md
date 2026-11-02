---
id: TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel
title: "Bulk Delete: Dialog Homogen, Kelompok Bullet User Ter-Scope, N=1 Collapse ke Dialog Single, dan [Cancel]"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-254
  - TC-FA-GRP-255
  - TC-FA-GRP-261
  - TC-FA-GRP-263
  - TC-FA-GRP-1034
coverage:
  web: automated
---

# Bulk Delete: Dialog Homogen, Kelompok Bullet User Ter-Scope, N=1 Collapse ke Dialog Single, dan [Cancel]

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Bulk E1` dan `Bulk E2` (TC-254), `Bulk E3` dan `Bulk U1` (TC-255; `Bulk U1` tanpa aset tapi punya `User BU 1` ber-Group Role, email `userBu1+{runId}-083@qwertysystem.net`), `Bulk E6` (TC-261), `Bulk E4` dan `Bulk E5` (TC-263), `Bulk C1` (TC-1034). Data Pre-setup `Warehouse A` (24 aset aktif; Tabel A No 9) hanya dibaca (TC-1034, dialog dibatalkan).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group sebelum dan sesudah aksi (audit trail permanen, tidak dapat diturunkan dari seeding; 8b butir 10) lewat fixture BE atau pembacaan UI.
- Baseline log: N0 = jumlah entri Modal Changelog: Group yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12).
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### Baseline Changelog

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group

### TC-FA-GRP-261: N=1 aman collapse ke dialog single

5. Centang hanya `Bulk E6`
6. Buka Bulk Action, pilih `Delete`
7. Verifikasi dialog singular dengan title "Delete Group", satu bullet `Bulk E6`, isi "Are you sure you want to delete it? This action cannot be undone."
8. Klik [Cancel], lalu klik (X)

### TC-FA-GRP-263: [Cancel] membatalkan

9. Centang `Bulk E4` dan `Bulk E5`
10. Buka Bulk Action, pilih `Delete`
11. Klik [Cancel] pada dialog
12. Verifikasi `Bulk E4` dan `Bulk E5` tetap ada di tabel
13. Verifikasi seleksi tetap (counter `2 groups selected`)
14. Klik (X)

### TC-FA-GRP-1034: Campuran, [Cancel] pada dialog

15. Centang `Bulk C1` dan `Warehouse A`
16. Buka Bulk Action, pilih `Delete`
17. Klik [Cancel] pada dialog `Delete Groups`
18. Verifikasi dialog `Delete Groups` tertutup
19. Verifikasi `Bulk C1` dan `Warehouse A` tetap ada di tabel
20. Verifikasi tidak ada toast yang tampil
21. Buka Modal Changelog: Group
22. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
23. Tutup Modal Changelog: Group
24. Klik (X)

### TC-FA-GRP-254: Dialog homogen dan commit

25. Centang `Bulk E1` dan `Bulk E2`
26. Buka Bulk Action, pilih `Delete`
27. Verifikasi dialog dengan title "Delete Groups", bullet `Bulk E1` dan `Bulk E2`, isi "Are you sure you want to delete them? This action cannot be undone.", tombol [Cancel] dan [Delete]
28. Klik [Delete]
29. Verifikasi toast sukses "Success, group has been deleted."
30. Verifikasi `Bulk E1` dan `Bulk E2` hilang dari tabel
31. Verifikasi seleksi dibersihkan
32. Verifikasi bar bulk action hilang

### TC-FA-GRP-255: Dialog homogen dengan kelompok bullet user ter-scope

33. Centang `Bulk E3` dan `Bulk U1`
34. Buka Bulk Action, pilih `Delete`
35. Verifikasi dialog `Delete Groups` memuat kelompok tambahan "The following have users whose group roles will be removed:" berisi `Bulk U1`
36. Klik [Delete]
37. Verifikasi toast sukses "Success, group has been deleted."
38. Verifikasi `Bulk E3` dan `Bulk U1` hilang dari tabel
39. Buka Settings > Role & Permission, pilih `User BU 1`
40. Verifikasi Group Role `User BU 1` di `Bulk U1` dicabut

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 8, 14, 21, 23 dan 24, 39: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Urutan: dialog batal dan collapse lebih dulu (TC-261, TC-263, TC-1034), Delete yang menghapus data (TC-254, TC-255) paling akhir (S-10).
- Klausa "tanpa toast dan tanpa baris Delete baru di Changelog" TC-1034 diasersi pada langkah 20 dan 22 dengan baseline N0; anchor positif: langkah 2 (entri lain tampil) dan langkah sebelumnya (`Bulk C1` dan `Warehouse A` tetap ada). Langkah 37 (toast sukses) adalah asersi tambahan sebagai anchor untuk baris hilang pada langkah 38; toast tidak ada di Expected TC-255 (S-03, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: lima TC satu keluarga Bulk Delete homogen dengan dataset seed berbeda per TC, satu kelas (fungsional), tiap blok berdiri sendiri; blok baca-log berpola tidak dihitung (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-254 dan TC-255 Post Condition (Changelog Action Delete per group) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-1034 menyebut "icon Changelog" tanpa menyebut Changelog Group atau user; spec memakai Modal Changelog: Group.
  - TC-1034 Langkah 3 "Klik [Cancel] pada dialog" pada dialog campuran (tombol [Cancel] dan [Continue]).
