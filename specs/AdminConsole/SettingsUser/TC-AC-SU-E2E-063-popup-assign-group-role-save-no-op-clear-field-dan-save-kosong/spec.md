---
id: TC-AC-SU-E2E-063-popup-assign-group-role-save-no-op-clear-field-dan-save-kosong
title: "Popup Assign Group Role: Save Tanpa Perubahan, Clear Field, dan Save Tabel Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-226
  - TC-AC-SU-227
  - TC-AC-SU-228
coverage:
  web: automated
---

# Popup Assign Group Role: Save Tanpa Perubahan, Clear Field, dan Save Tabel Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE; masing-masing tanpa tingkat akses dan bukan Group Manager): `Budi Santoso {runId}-063` (`Manage partner` aktif di `Region A {runId}-063`, TC-226), `Budi Santoso {runId}-063 B` (`Manage partner` aktif di `Region A {runId}-063` dan `Region B {runId}-063`, TC-227), `Budi Santoso {runId}-063 C` (`Manage partner` aktif di `Region A {runId}-063`, TC-228).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-063`): `Region A {runId}-063` > `Branch 1 {runId}-063` > `Floor 1 {runId}-063`; `Region A {runId}-063` > `Branch 3 {runId}-063`; `Region B {runId}-063`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-063@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-063`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-063` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-226: Save tanpa perubahan apa pun: no-op

1. Ketik Search `Budi Santoso {runId}-063`, tekan Enter
2. Klik nama `Budi Santoso {runId}-063` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Klik `[Save]`
6. Verifikasi popup tertutup
7. Verifikasi muncul toast `"No changes to save."` (bukan toast sukses assigned/updated)
8. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-227: Clear Field mengosongkan tabel popup tanpa menutup

9. Ketik Search `Budi Santoso {runId}-063 B`, tekan Enter
10. Klik nama `Budi Santoso {runId}-063 B` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
11. Klik Sub-tab [Group Role]
12. Klik `[Assign Group]` baris `Manage partner`
13. Klik `[Clear Field]`
14. Verifikasi semua baris group terhapus dari tabel popup, empty state Title `No groups assigned yet` + Description `Click [+ Assign Group] to add a group.`
15. Verifikasi popup tetap terbuka
16. Verifikasi tidak ada dialog konfirmasi
17. Verifikasi belum ada toast
18. Klik `✕` pada popup
19. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
20. Klik `[Leave]`
21. Verifikasi kolom Group `Manage partner` tetap `Region A {runId}-063`, `Region B {runId}-063` (belum ada perubahan tersimpan)
22. Klik Breadcrumb Settings > User untuk kembali ke User List

### TC-AC-SU-228: Save saat tabel popup kosong: tersimpan tanpa dialog dan role dilepas

23. Ketik Search `Budi Santoso {runId}-063 C`, tekan Enter
24. Klik nama `Budi Santoso {runId}-063 C` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
25. Klik Sub-tab [Group Role]
26. Klik `[Assign Group]` baris `Manage partner`
27. Klik `[🗑]` baris `Region A {runId}-063`
28. Verifikasi `[Save]` enabled
29. Verifikasi tidak ada dialog konfirmasi maupun dialog blok
30. Klik `[Save]`
31. Verifikasi popup tertutup
32. Verifikasi muncul toast sukses: "Success, group role has been updated."
33. Verifikasi kolom Group `Manage partner` = `—`, menandai role tidak aktif
34. Klik Breadcrumb Settings > User untuk kembali ke User List

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 9, 22, 23, 34 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Pembagian TC: TC-AC-SU-222 sampai 225 ada di spec 062; TC-AC-SU-229 ada di spec 192 (`TC-AC-SU-E2E-192-popup-assign-group-role-clear-field-save-dan-changelog-remove`).
- Tiap TC memakai user sendiri (`Budi Santoso {runId}-063`, `Budi Santoso {runId}-063 B`, `Budi Santoso {runId}-063 C`) karena kondisi awal `Manage partner` berubah menurut TC sebelumnya (TC-228 melepas role).
- Observasi "belum ada perubahan tersimpan" pada TC-227 diamati sesudah popup ditutup lewat `[Leave]` (S-08), karena TC tidak memberi langkah observasi.
- Temuan untuk QA:
  - Expected TC-228 butir c memuat "role tidak aktif" tanpa elemen UI terpisah; spec memakai kolom Group `—` sebagai penanda.
  - Post Condition TC-226 (log tidak bertambah di Changelog, System Log, Activity Log) dan TC-228 tidak punya langkah observasi dan tidak diasersi.
