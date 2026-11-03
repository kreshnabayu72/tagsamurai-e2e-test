---
id: TC-AC-SU-E2E-069-detail-group-assignment-nama-file-dan-sort-group
title: "Detail Group Assignment: Nama Berkas Download Dinormalisasi dan Sort Kolom Group"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-657
  - TC-AC-SU-662
coverage:
  web: automated
---

# Detail Group Assignment: Nama Berkas Download Dinormalisasi dan Sort Kolom Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-069` tanpa tingkat akses dan bukan Group Manager; `Manage wallet & pricing` aktif di `Region A {runId}-069`; `Manage distributor` aktif di `Region A {runId}-069` dan `Branch 1 {runId}-069`.
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-069`): `Region A {runId}-069` > `Branch 1 {runId}-069` > `Floor 1 {runId}-069`; `Region A {runId}-069` > `Branch 3 {runId}-069`; `Region B {runId}-069`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-069@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-069`.
- Kemampuan teknis tambahan (TC-657): membaca nama berkas unduhan XLSX.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-069` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-657: Download Detail Group Assignment: placeholder nama file dinormalisasi (spasi, &)

1. Ketik Search `Budi Santoso {runId}-069`, tekan Enter
2. Klik nama `Budi Santoso {runId}-069` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Detail]` baris `Manage wallet & pricing`
5. Klik Download → `Download as XLSX`
6. Verifikasi tidak ada toast sukses
7. Verifikasi file `Group-Assignment-Budi-Santoso-{runId}-069-Manage-wallet-pricing.xlsx` terunduh (spasi jadi `-`, `&` dibuang, `-` berurutan diringkas)
8. Tutup popup dengan `[×]`

### TC-AC-SU-662: Detail Group Assignment: kolom Group sortable A-Z

9. Klik `[Detail]` baris `Manage distributor`
10. Klik header `Group` sekali
11. Verifikasi urutan baris `Branch 1 {runId}-069`, `Region A {runId}-069` (A-Z)
12. Klik header `Group` lagi
13. Verifikasi urutan baris `Region A {runId}-069`, `Branch 1 {runId}-069` (Z-A)
14. Tutup popup dengan `[×]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 8, 14 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Bagian `{runId}-069` pada nama berkas diisi nilai runId aktif.
- Asersi tidak ada toast sukses (langkah 6) diletakkan tepat setelah klik Download dan sebelum Verifikasi berkas (bagian 8b butir 11); klik pilihan format menjadi anchor positif yang buktinya menyusul pada langkah 7.
- Pembagian TC: TC-AC-SU-245 sampai 247 ada di spec 068.
