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

5. Ketik Search `{runId}-083`, tekan Enter
6. Centang hanya `Bulk E6`
7. Buka Bulk Action, pilih `Delete`
8. Verifikasi dialog singular dengan title "Delete Group", satu bullet `Bulk E6`, isi "Are you sure you want to delete it? This action cannot be undone."
9. Klik [Cancel], lalu klik (X)

### TC-FA-GRP-263: [Cancel] membatalkan

10. Centang `Bulk E4` dan `Bulk E5`
11. Buka Bulk Action, pilih `Delete`
12. Klik [Cancel] pada dialog
13. Verifikasi `Bulk E4` dan `Bulk E5` tetap ada di tabel
14. Verifikasi seleksi tetap (counter `2 groups selected`)
15. Klik (X)

### TC-FA-GRP-1034: Campuran, [Cancel] pada dialog

16. Centang `Bulk C1`
17. Ganti isi kotak Search dengan `Warehouse A`, tekan Enter
18. Centang `Warehouse A`
19. Buka Bulk Action, pilih `Delete`
20. Klik [Cancel] pada dialog `Delete Groups`
21. Verifikasi dialog `Delete Groups` tertutup
22. Verifikasi `Warehouse A` tetap ada di tabel
23. Ganti isi kotak Search dengan `{runId}-083`, tekan Enter
24. Verifikasi `Bulk C1` tetap ada di tabel
25. Verifikasi tidak ada toast yang tampil
26. Buka Modal Changelog: Group
27. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
28. Tutup Modal Changelog: Group
29. Klik (X)

### TC-FA-GRP-254: Dialog homogen dan commit

30. Centang `Bulk E1` dan `Bulk E2`
31. Buka Bulk Action, pilih `Delete`
32. Verifikasi dialog dengan title "Delete Groups", bullet `Bulk E1` dan `Bulk E2`, isi "Are you sure you want to delete them? This action cannot be undone.", tombol [Cancel] dan [Delete]
33. Klik [Delete]
34. Verifikasi toast sukses "Success, group has been deleted."
35. Verifikasi `Bulk E1` dan `Bulk E2` hilang dari tabel
36. Verifikasi seleksi dibersihkan
37. Verifikasi bar bulk action hilang

### TC-FA-GRP-255: Dialog homogen dengan kelompok bullet user ter-scope

38. Centang `Bulk E3` dan `Bulk U1`
39. Buka Bulk Action, pilih `Delete`
40. Verifikasi dialog `Delete Groups` memuat kelompok tambahan "The following have users whose group roles will be removed:" berisi `Bulk U1`
41. Klik [Delete]
42. Verifikasi toast sukses "Success, group has been deleted."
43. Verifikasi `Bulk E3` dan `Bulk U1` hilang dari tabel
44. Buka Settings > Role & Permission, pilih `User BU 1`
45. Verifikasi nama user `User BU 1` tampil pada detail user di Role & Permission
46. Verifikasi Group Role `User BU 1` di `Bulk U1` dicabut

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 dan 4, 9, 15, 26, 28 dan 29, 44: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 5 (Ketik Search `{runId}-083`, tekan Enter) menampilkan seluruh group seed spec ini (delapan baris, satu halaman) untuk langkah Centang dan Verifikasi; langkah 17 dan 23 (Ganti isi kotak Search dengan `Warehouse A` dan `{runId}-083`) menemukan `Warehouse A` Pre-setup lalu kembali ke group seed; centang dipertahankan saat Search berganti (TC-FA-GRP-251 dan 426); client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: dialog batal dan collapse lebih dulu (TC-261, TC-263, TC-1034), Delete yang menghapus data (TC-254, TC-255) paling akhir (S-10).
- Klausa "tanpa toast dan tanpa baris Delete baru di Changelog" TC-1034 diasersi pada langkah 25 dan 27 dengan baseline N0; anchor positif: langkah 2 (entri lain tampil) dan langkah sebelumnya (`Bulk C1` dan `Warehouse A` tetap ada). Asersi pencabutan Group Role pada langkah 46 didahului `Verifikasi` nama user tampil di Role & Permission (langkah 45) sebagai anchor permukaan (8b butir 2). Langkah 42 (toast sukses) adalah asersi tambahan sebagai anchor untuk baris hilang pada langkah 43; toast tidak ada di Expected TC-255 (S-03, 8b butir 2).
- Spec berisi lebih dari 35 langkah. Alasan: lima TC satu keluarga Bulk Delete homogen dengan dataset seed berbeda per TC, satu kelas (fungsional), tiap blok berdiri sendiri; blok baca-log berpola tidak dihitung (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-254 dan TC-255 Post Condition (Changelog Action Delete per group) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-1034 menyebut "icon Changelog" tanpa menyebut Changelog Group atau user; spec memakai Modal Changelog: Group.
  - TC-1034 Langkah 3 "Klik [Cancel] pada dialog" pada dialog campuran (tombol [Cancel] dan [Continue]).
