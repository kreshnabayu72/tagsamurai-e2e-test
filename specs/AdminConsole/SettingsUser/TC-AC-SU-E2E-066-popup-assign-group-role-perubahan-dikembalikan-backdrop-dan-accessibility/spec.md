---
id: TC-AC-SU-E2E-066-popup-assign-group-role-perubahan-dikembalikan-backdrop-dan-accessibility
title: "Popup Assign Group Role: Perubahan Dikembalikan, Backdrop Tidak Menutup, dan Accessibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-236
  - TC-AC-SU-237
  - TC-AC-SU-241
coverage:
  web: automated
---

# Popup Assign Group Role: Perubahan Dikembalikan, Backdrop Tidak Menutup, dan Accessibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-066` tanpa tingkat akses dan bukan Group Manager; `Manage partner` aktif di `Region A {runId}-066` (C ☐, U ☐, D ☐).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-066`): `Region A {runId}-066` > `Branch 1 {runId}-066` > `Floor 1 {runId}-066`; `Region A {runId}-066` > `Branch 3 {runId}-066`; `Region B {runId}-066`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-066@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-066`.
- Kemampuan teknis tambahan (TC-241): navigasi keyboard (Tab, Space) dan pembacaan nama aksesibel elemen; disediakan tim FE. Nama aksesibel `[×]` dan `[🗑]` tidak dinyatakan TC.
- Tabel "Checkbox yang di-toggle" (TC-241): `C`, `U`, `D` baris `Region A {runId}-066`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-066` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-236: Perubahan dikembalikan persis ke awal: tutup tanpa dialog

1. Ketik Search `Budi Santoso {runId}-066`, tekan Enter
2. Klik nama `Budi Santoso {runId}-066` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Centang C baris `Region A {runId}-066`
6. Uncheck lagi C baris `Region A {runId}-066`
7. Klik `[×]`
8. Verifikasi popup langsung tertutup tanpa dialog Unsaved Changes (dirty dihitung dari perbandingan nilai)

### TC-AC-SU-237: Klik backdrop di luar Popup Assign Group Role tidak menutup popup

9. Klik `[Assign Group]` baris `Manage partner`
10. Centang C baris `Region A {runId}-066`
11. Klik area backdrop di luar popup
12. Verifikasi popup tetap terbuka
13. Verifikasi C baris `Region A {runId}-066` tetap tercentang
14. Verifikasi dialog Unsaved Changes tidak muncul
15. Klik `✕` pada popup
16. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
17. Klik `[Leave]`

### TC-AC-SU-241: Accessibility Popup Assign Group Role: fokus terjebak dan tombol ikon berlabel

18. Klik `[Assign Group]` baris `Manage partner`
19. Tekan Tab berulang sampai melewati elemen terakhir
20. Verifikasi fokus berputar di dalam popup (tidak keluar ke halaman)
21. Verifikasi `[×]` punya label aksesibel
22. Verifikasi `[🗑]` punya label aksesibel
23. Untuk setiap checkbox pada tabel "Checkbox yang di-toggle" (langkah 23 sampai 24): fokuskan checkbox lewat Tab, tekan Space
24. Verifikasi checkbox tersebut ter-toggle (tercentang)
25. Klik `✕` pada popup
26. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
27. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah 23 sampai 24 diulang untuk checkbox `C`, `U`, `D` baris `Region A {runId}-066` (bagian 8b butir 7); `Verifikasi` tetap satu per iterasi.
- Pembagian TC: TC-AC-SU-232 sampai 235 ada di spec 065; TC-AC-SU-238 sampai 240 ada di spec 067.
- Temuan untuk QA:
  - Expected TC-241 butir c ("Checkbox C/U/D bisa di-toggle dengan Space") tidak menyebut kondisi hasil toggle; spec mengasersi tercentang karena nilai awal ☐.
  - Expected TC-241 butir b tidak menyebut teks label aksesibel; spec hanya mengasersi keberadaan label.
