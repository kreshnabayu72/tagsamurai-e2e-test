---
id: TC-GS-ROLE-E2E-043-remove-baris-auto-revert-dialog-konfirmasi-dan-cancel
title: "Remove Baris Role Target Total Control dan Read Only: Dialog Auto-Revert, Konfirmasi, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-114
  - TC-GS-ROLE-115
  - TC-GS-ROLE-116
coverage:
  web: automated
---

# Remove Baris Role Target Total Control dan Read Only: Dialog Auto-Revert, Konfirmasi, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Spec memakai satu akun; tidak ada ganti akun.
- Data Given (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE; dipakai sebagai precondition TC):
  - Rudi Hartono (Pre-setup #11, Pending Activation) di-assign Total Control dengan keenam role CRUD penuh (kondisi hasil TC-GS-ROLE-59, Tabel Data Uji Dinamis #2). Target TC-GS-ROLE-114.
  - Siti Nurhaliza (Pre-setup #4, Read Only dengan baris Manage TAG) di-assign Total Control (kondisi hasil TC-GS-ROLE-60, Tabel Data Uji Dinamis #3). Target TC-GS-ROLE-116.
- Data Pre-setup #4: Rina Putri (Read Only, Inactive, punya baris Manage TAG) dan baris `Manage files` Rina Putri sebagai Read Only. Target TC-GS-ROLE-115.
- Data yang diubah spec: Rudi Hartono kehilangan Total Control (TC-GS-ROLE-114) dan Rina Putri kehilangan Read Only (TC-GS-ROLE-115); baris `Manage files` keduanya dihapus. Hook `after` memulihkan ke kondisi Pre-setup lewat seeding API: Rudi Hartono menjadi kandidat Pre-setup #11 (tanpa access level, tanpa baris role), Rina Putri kembali Read Only dengan baris role Pre-setup #4, dan Siti Nurhaliza kembali Read Only dengan baris Manage TAG (mengikuti "Reset Pre-setup per TC" di `tc-role.md`).
- Kemampuan teknis: hover pada komponen user di dialog.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-116: Cancel dialog auto-revert dari Remove baris

1. Klik Role Name `Manage files`
2. Klik `(⋯)` baris Siti Nurhaliza
3. Klik `Remove`
4. Klik `[Cancel]`
5. Verifikasi tidak ada toast
6. Verifikasi baris Siti Nurhaliza tetap ada di Detail `Manage files`
7. Buka Tab Total Control
8. Ketik Search `Siti`, tekan Enter
9. Verifikasi baris Siti Nurhaliza tampil di Tab Total Control
10. Klik `(←)` pada kotak Search

### TC-GS-ROLE-114: Remove baris role target Total Control memicu dialog auto-revert

11. Buka Tab System
12. Klik Role Name `Manage files`
13. Klik `(⋯)` baris Rudi Hartono
14. Klik `Remove`
15. Verifikasi title dialog "Remove Access"
16. Verifikasi body dialog memuat komponen user (ikon user generik dan "Rudi H")
17. Arahkan kursor ke komponen user "Rudi H"
18. Verifikasi tooltip menampilkan nama lengkap "Rudi Hartono"
19. Verifikasi body dialog memuat teks "Editing this permission will remove Total Control access from this user. Are you sure you want to remove it?"
20. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
21. Klik `[Remove]`
22. Verifikasi toast sukses "Success, permissions have been updated. Rudi Hartono is no longer Total Control."
23. Verifikasi baris Rudi Hartono hilang dari Detail `Manage files`
24. Buka Tab Total Control
25. Ketik Search `Rudi`, tekan Enter
26. Verifikasi "No results found"
27. Klik `(←)` pada kotak Search
28. Buka Tab System
29. Klik Role Name `Manage TAG`
30. Verifikasi baris Rudi Hartono di Detail `Manage TAG` tetap ada
31. Verifikasi Read baris Rudi Hartono checked
32. Verifikasi Update baris Rudi Hartono checked

### TC-GS-ROLE-115: Remove baris role target Read Only memicu dialog auto-revert

33. Klik segmen `System` pada breadcrumb untuk membuka Tab System
34. Klik Role Name `Manage files`
35. Klik `(⋯)` baris Rina Putri
36. Klik `Remove`
37. Verifikasi body dialog menyebut "Read Only"
38. Klik `[Remove]`
39. Verifikasi toast sukses "Success, permissions have been updated. Rina Putri is no longer Read Only."
40. Buka Tab Read Only
41. Ketik Search `Rina`, tekan Enter
42. Verifikasi "No results found"
43. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Spec melewati sekitar 35 langkah (43 langkah) karena ketiga TC berada di satu kelas harness (fungsional, Remove baris target access level pada Detail `Manage files`) dengan akun aktor yang sama; tiap blok memakai user target sendiri (Siti Nurhaliza, Rudi Hartono, Rina Putri) dan dimulai dari Tab System, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: TC-GS-ROLE-116 (Cancel) dijalankan pertama karena tidak mengubah data, sedangkan TC-GS-ROLE-114 dan TC-GS-ROLE-115 mengubah access level target (prinsip 3 dan 5 bagian 3).
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka tab, Tab System, dan Detail yang dibutuhkan langkah berikutnya (langkah 1, 7, 11, 12, 24, 28, 29, 33, 34, 40), dan mengosongkan Search lewat `(←)` (langkah 10, 27, 43).
- Langkah 5 (tidak ada toast) diletakkan segera sesudah pemicu `[Cancel]` (butir 11 bagian 8b). Langkah 23 (baris hilang) memakai toast sukses langkah 22 sebagai anchor. Langkah 26 dan 42 ("No results found" dari Search) adalah anchor positif untuk absence di Tab Total Control dan Tab Read Only.
- Langkah 37 mengasersi body dialog hanya menyebut "Read Only" sesuai Expected a TC-GS-ROLE-115.
- Temuan untuk QA:
  - TC-GS-ROLE-114, TC-GS-ROLE-115, dan TC-GS-ROLE-116 tidak punya Post Condition.
  - TC-GS-ROLE-116 menyebut Siti Nurhaliza Total Control berdasarkan dependensi TC-GS-ROLE-60, sedangkan Pre-setup #4 menyebut Siti Nurhaliza Read Only; spec menyiapkan Total Control sebagai Given.
  - TC-GS-ROLE-114 Expected d menyebut "R,U checked" untuk baris Rudi Hartono di Detail `Manage TAG`; spec mengasersi Read dan Update checked sesuai teks tersebut.
