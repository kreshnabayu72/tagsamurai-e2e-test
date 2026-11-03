---
id: TC-AC-SU-E2E-067-popup-assign-group-role-reload-dan-navigasi-saat-dirty
title: "Popup Assign Group Role: Reload dan Navigasi Back saat Dirty"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-239
  - TC-AC-SU-238
  - TC-AC-SU-240
coverage:
  web: automated
---

# Popup Assign Group Role: Reload dan Navigasi Back saat Dirty

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-067` tanpa tingkat akses dan bukan Group Manager; `Manage partner` aktif di `Region A {runId}-067` (C ☐).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-067`): `Region A {runId}-067` > `Branch 1 {runId}-067` > `Floor 1 {runId}-067`; `Region A {runId}-067` > `Branch 3 {runId}-067`; `Region B {runId}-067`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-067@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-067`.
- Kemampuan teknis tambahan: menangani dialog bawaan browser `beforeunload` (menerima atau membatalkan reload) dan tombol Back browser; disediakan tim FE (S-08).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-067` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-239: Reload halaman saat Popup Assign Group Role bersih tanpa konfirmasi browser

1. Ketik Search `Budi Santoso {runId}-067`, tekan Enter
2. Klik nama `Budi Santoso {runId}-067` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Tekan F5
6. Verifikasi Breadcrumb `Settings > User > Detail` tampil kembali sesudah reload
7. Verifikasi halaman langsung reload tanpa konfirmasi browser (`beforeunload`)

### TC-AC-SU-238: Reload halaman saat Popup Assign Group Role dirty memicu konfirmasi browser

8. Klik Sub-tab [Group Role]
9. Klik `[Assign Group]` baris `Manage partner`
10. Centang C baris `Region A {runId}-067`
11. Tekan F5
12. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
13. Batalkan reload pada konfirmasi bawaan browser
14. Hapus centang C baris `Region A {runId}-067`
15. Klik `[×]`

### TC-AC-SU-240: Navigasi internal via breadcrumb saat Popup Assign Group Role dirty

16. Klik `[Assign Group]` baris `Manage partner`
17. Centang C baris `Region A {runId}-067`
18. Tekan tombol Back browser
19. Verifikasi navigasi dicegat: dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
20. Klik `[Cancel]`
21. Verifikasi tetap di popup dengan input utuh: C baris `Region A {runId}-067` tetap tercentang
22. Hapus centang C baris `Region A {runId}-067`
23. Klik `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 13 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah 6 (Verifikasi Detail tampil kembali sesudah reload) adalah anchor positif tambahan (S-03, dasar 8b.2) bagi absence dialog `beforeunload` pada langkah 7.
- Urutan TC di spec: 239, 238, 240 (reload bersih lebih dulu, lalu dua kasus dirty).
- Pada TC-238 dan TC-240 popup dikembalikan ke nilai tersimpan (hapus centang C) sebelum `[×]`, sehingga penutupan tanpa dialog (S-08, S-09); dialog `beforeunload` pada TC-238 dibatalkan oleh kemampuan penanganan dialog browser.
- Pembagian TC: TC-AC-SU-232 sampai 235 ada di spec 065; TC-AC-SU-236, 237, 241 ada di spec 066.
- Temuan untuk QA:
  - TC-239 langkah 3 menyebut sesudah F5 popup tidak muncul lagi; spec membuka kembali Sub-tab [Group Role] sebelum TC-238 karena F5 mengembalikan Detail ke Tab Role default.
  - TC-240 berjudul "via breadcrumb" tetapi langkahnya "Tekan tombol Back browser"; spec mengikuti langkah TC.
