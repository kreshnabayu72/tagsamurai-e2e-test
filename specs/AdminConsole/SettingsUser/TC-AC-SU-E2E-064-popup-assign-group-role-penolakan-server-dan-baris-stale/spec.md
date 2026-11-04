---
id: TC-AC-SU-E2E-064-popup-assign-group-role-penolakan-server-dan-baris-stale
title: "Popup Assign Group Role: Penolakan Server atas Group Ter-assign dan Group yang Sudah Dihapus"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-230
  - TC-AC-SU-660
coverage:
  web: automated
---

# Popup Assign Group Role: Penolakan Server atas Group Ter-assign dan Group yang Sudah Dihapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE; tanpa tingkat akses dan bukan Group Manager): `Budi Santoso {runId}-064` (`Manage partner` aktif di `Region A {runId}-064`, TC-230), `Budi Santoso B {runId}-064` (`Manage partner` aktif di `Region A {runId}-064`, TC-660).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-064`): `Region A {runId}-064` > `Branch 1 {runId}-064` > `Floor 1 {runId}-064`; `Region A {runId}-064` > `Branch 3 {runId}-064`; `Region B {runId}-064`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-064@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-064`.
- Pelaku kedua (aktor Total Control kedua pada TC) memakai sesi API Total Control untuk assign group dan hapus group; langkah pemicu ditulis "... hingga ... tersimpan".
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku yang hanya memicu perubahan state (suite.md); disediakan tim BE/FE.
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-064` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-230: Server menolak group yang sudah ter-assign (V-01): toast error dan tree di-refresh

1. Ketik Search `Budi Santoso {runId}-064`, tekan Enter
2. Klik nama `Budi Santoso {runId}-064` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Tambah `Region B {runId}-064` via `[+ Assign Group]` → Popup Select Group → `[Select]`
6. Pemicu (sesi API Total Control kedua): assign `Region B {runId}-064` ke role `Manage partner` untuk `Budi Santoso {runId}-064` hingga assignment tersimpan
7. Klik `[Save]` di popup
8. Verifikasi muncul toast error: `"Error, failed to save group role. This group is already assigned to this role."` (copy V-01, bukan T-10)
9. Verifikasi popup tetap terbuka dengan isi utuh
10. Klik `[+ Assign Group]`
11. Verifikasi node `Region B {runId}-064` di Select Group kini disabled
12. Klik `[Cancel]` di Popup Select Group
13. Klik `✕` pada popup
14. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
15. Klik `[Leave]`
16. Klik segmen `User` pada Breadcrumb untuk kembali ke User List

### TC-AC-SU-660: Group dihapus di Settings > Group sebelum Save: seluruh Save ditolak, baris stale dibersihkan

17. Tunggu toast lama hilang otomatis
18. Ganti isi kotak Search dengan `Budi Santoso B {runId}-064`, tekan Enter
19. Klik nama `Budi Santoso B {runId}-064` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
20. Klik Sub-tab [Group Role]
21. Klik `[Assign Group]` baris `Manage partner`
22. Tambah `Region B {runId}-064` via Select Group
23. Pemicu (sesi API Total Control kedua): hapus group `Region B {runId}-064` dari Settings > Group hingga terhapus
24. Klik `[Save]` di popup
25. Verifikasi muncul toast error: `"Error, failed to save group role. One or more selected groups no longer exist. Please select another."` (tanpa nama group)
26. Verifikasi popup tetap terbuka
27. Verifikasi baris `Region B {runId}-064` dibersihkan dari tabel popup
28. Verifikasi baris `Region A {runId}-064` tetap ada di tabel popup
29. Klik `[×]` pada popup
30. Verifikasi kolom Group `Manage partner` tetap `Region A {runId}-064` (seluruh Save ditolak)
31. Tunggu toast lama hilang otomatis
32. Pemicu: seed ulang group `Region B {runId}-064` lewat Fixture BE hingga group tersimpan
33. Klik `[Assign Group]` baris `Manage partner`
34. Tambah `Region B {runId}-064` dan `Branch 3 {runId}-064` via Select Group
35. Pemicu (sesi API Total Control kedua): hapus group `Region B {runId}-064` dan `Branch 3 {runId}-064` dari Settings > Group hingga terhapus
36. Klik `[Save]` di popup
37. Verifikasi muncul satu toast error yang sama: `"Error, failed to save group role. One or more selected groups no longer exist. Please select another."` (tanpa nama group)
38. Verifikasi baris `Region B {runId}-064` dan `Branch 3 {runId}-064` dibersihkan dari tabel popup

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 12, 16, 17, 18, 23, 31, 32, 35 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC-660: kasus dasar (satu group stale) lebih dulu, lalu variasi dua group stale; `Region B {runId}-064` di-seed ulang sebelum variasi karena kasus dasar menghapusnya. `Branch 3 {runId}-064` dihapus pada variasi.
- Aktor kedua hanya pemicu perubahan state lewat sesi API dan bukan konteks kedua yang diasersi, sehingga TC ini tetap di spec fungsional.
- Temuan untuk QA:
  - TC-230 dan TC-660 menulis "di tab browser lain aktor Total Control kedua" tanpa menyatakan sesi UI atau API; spec memakai sesi API aktor Total Control sebagai pemicu.
  - Expected TC-230 menulis toast di "Langkah 5" padahal toast muncul sesudah `[Save]` (langkah 6); spec menaruh `Verifikasi` setelah `[Save]`.
  - Post Condition TC-230 ("Region B ter-assign sekali saja") dan TC-660 ("Tidak ada entri log") tidak punya langkah observasi dan tidak diasersi.
  - Dialog Unsaved Changes pada akhir TC-230 muncul karena popup masih memuat baris `Region B {runId}-064` baru (S-08).
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
