---
id: TC-AC-SU-E2E-068-detail-group-assignment-screening-search-dan-download
title: "Detail Group Assignment: Screening Read Only, Interaksi Checkbox, serta Search dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-245
  - TC-AC-SU-246
  - TC-AC-SU-247
coverage:
  web: automated
---

# Detail Group Assignment: Screening Read Only, Interaksi Checkbox, serta Search dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Read Only, `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RO_PASSWORD`.
- Akun kedua (ganti akun eksplisit di tengah spec): Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-068` tanpa tingkat akses dan bukan Group Manager; `Manage distributor` aktif di `Region A {runId}-068` (C ☑ R ☑ U ☑ D ☐) dan `Branch 1 {runId}-068` (R saja).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-068`): `Region A {runId}-068` > `Branch 1 {runId}-068` > `Floor 1 {runId}-068`; `Region A {runId}-068` > `Branch 3 {runId}-068`; `Region B {runId}-068`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-068@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-068`.
- Kemampuan teknis tambahan (TC-247): membaca nama dan isi berkas unduhan XLSX/CSV (nama berkas, jumlah baris, dan nama group di kolom Group).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-068` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-245: Screening Popup Detail Group Assignment (read-only)

1. Ketik Search `Budi Santoso {runId}-068`, tekan Enter
2. Klik nama `Budi Santoso {runId}-068` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Detail]` baris `Manage distributor`
5. Verifikasi title popup `"Group Assignment"` + `[×]`
6. Verifikasi subtitle popup `Manage distributor`
7. Verifikasi toolbar popup: Search `"Search groups..."` | Download
8. Verifikasi kolom tabel: `Group | C | R | U | D | Actions (⋯)`, header Actions (⋯) = trigger Column Visibility, body kosong, tanpa pagination
9. Verifikasi baris `Region A {runId}-068`: C ☑ R ☑ U ☑ D ○
10. Verifikasi baris `Branch 1 {runId}-068`: C ○ R ☑ U ○ D ○
11. Verifikasi semua checkbox disabled
12. Verifikasi footer popup tidak punya tombol
13. Tutup popup dengan `[×]`
14. Logout dari akun Read Only
15. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
16. Buka Settings > User lewat sidebar

### TC-AC-SU-246: Detail Group Assignment: klik checkbox tidak mengubah apa pun dan tutup via ×

17. Ketik Search `Budi Santoso {runId}-068`, tekan Enter
18. Klik nama `Budi Santoso {runId}-068` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
19. Klik Sub-tab [Group Role]
20. Klik `[Detail]` baris `Manage distributor`
21. Klik checkbox C baris `Region A {runId}-068`
22. Verifikasi checkbox C baris `Region A {runId}-068` tidak berubah
23. Klik backdrop di luar popup
24. Verifikasi popup tidak tertutup oleh klik backdrop
25. Klik `[×]`
26. Verifikasi popup tertutup oleh `[×]`
27. Klik `[Detail]` baris `Manage distributor`
28. Tekan Esc
29. Verifikasi popup tertutup oleh Esc

### TC-AC-SU-247: Detail Group Assignment: Search dan Download mengikuti hasil Search

30. Klik `[Detail]` baris `Manage distributor`
31. Ketik Search `branch`, tekan Enter
32. Verifikasi hanya baris `Branch 1 {runId}-068` tampil
33. Klik Download → `Download as XLSX`
34. Verifikasi tidak ada toast sukses
35. Verifikasi file `Group-Assignment-Budi-Santoso-{runId}-068-Manage-distributor.xlsx` terunduh
36. Verifikasi file xlsx berisi baris `Branch 1 {runId}-068` saja
37. Klik Download → `Download as CSV`
38. Verifikasi file `Group-Assignment-Budi-Santoso-{runId}-068-Manage-distributor.csv` terunduh dengan nama yang sama
39. Tutup popup dengan `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 13, 17, 39 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Spec ditulis per blok role (bagian 3a): TC-245 sebagai Read Only (akun pertama, login di hook `before`), lalu ganti akun eksplisit ke Total Control untuk TC-246 dan TC-247. Hook `after` mengembalikan sesi ke Default User.
- Nama berkas memakai nama user bersuffix yang dinormalisasi (spasi menjadi `-`); Bagian `{runId}-068` pada nama berkas diisi nilai runId aktif.
- Asersi tidak ada toast sukses (langkah 34) diletakkan tepat setelah klik Download dan sebelum Verifikasi berkas (bagian 8b butir 11); klik pilihan format menjadi anchor positif yang buktinya menyusul pada langkah 35.
- Pembagian TC: TC-AC-SU-657 dan 662 ada di spec 069.
- P-10: TC-247 mencampur asersi UI popup (Search dan hasil tersaring) dengan isi berkas unduhan (langkah 36, baris `Branch 1 {runId}-068` saja). Alur unduh mengikuti hasil Search pada popup yang sama sehingga tidak dapat dipisah dari asersi UI; klausa isi berkas diletakkan sesudah klausa UI TC itu dan diasersi satu per klausa.
- Pembanding hasil Search TC-247 ("hanya `Branch 1`") adalah baris `Region A {runId}-068` yang tampil di tabel yang sama sebelum Search (data seed yang sama dengan TC-245).
- Temuan untuk QA:
  - Expected TC-247 butir a menyebut "hanya `Branch 1` tampil" tanpa pembanding; spec memakai `Region A {runId}-068` dari tabel sebelum Search sebagai pembanding implisit.
  - Aspek berkas TC-247 diasersi sebatas nama, jenis, dan baris yang ada (bukan nilai sel); nilai sel (kelas f) tidak diasersi.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
