---
id: TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom
title: "Modal Changelog: Screening, Empty State, dan Tampilan Data Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-241
  - TC-AC-SG-242
  - TC-AC-SG-243
  - TC-AC-SG-244
coverage:
  web: automated
---

# Modal Changelog: Screening, Empty State, dan Tampilan Data Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Akun kedua (ganti akun pada TC-AC-SG-242): Total Control entitas `Distributor Changelog Kosong` (Pre-setup #43, tanpa satu pun entri Changelog Group) `totalControlChangelogKosong_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOGKOSONG_PASSWORD`.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### TC-AC-SG-241: Screening Modal Changelog: Group

1. Hover ikon Changelog pada toolbar
2. Verifikasi tooltip ikon `Changelog` tampil
3. Klik ikon Changelog pada toolbar
4. Verifikasi Header modal: Title `Changelog: Group` tampil
5. Verifikasi Header modal: ikon close `[✕]` tampil
6. Verifikasi Body: toolbar Search, Filter, dan Download tampil
7. Verifikasi tabel memiliki 7 kolom berurutan Date, Action, Group Name, Field, Old Value, New Value, Modified By
8. Verifikasi kolom Actions kosong ada sebagai trigger Column Visibility
9. Verifikasi tabel tanpa row action
10. Verifikasi Footer: Pagination tampil dengan default 10 baris per halaman
11. Verifikasi sedikitnya dua baris tampil dan baris terurut Date terbaru di atas (sort default)
12. Ganti page size menjadi 25 agar seluruh baris seed tampil dalam satu halaman
13. Verifikasi baris Create `Region B` menampilkan Old Value `—`
14. Verifikasi baris Delete `Branch 4` menampilkan New Value `—`

### TC-AC-SG-243: Tampilan data kolom Changelog: tanda —, hover path, dan Modified By

15. Verifikasi baris Create `Region B` menampilkan Field `Group Name`, Old Value `—`, dan New Value `Region B`
16. Verifikasi baris Edit menampilkan Field `Group Name`, Old Value `Region A1`, dan New Value `Region A`
17. Verifikasi baris Delete menampilkan Field `Group Name`, Old Value `Branch 4`, dan New Value `—`
18. Verifikasi Group Name pada baris `Branch 3` berupa teks biasa (bukan link)
19. Hover nilai Group Name pada baris `Branch 3`
20. Verifikasi tooltip menampilkan snapshot full path breadcrumb node `Branch 3` saat entri ditulis
21. Verifikasi Modified By pada baris `Branch 3` tampil sebagai plain text berformat `[First Name] [Last Initial]`
22. Hover nilai Modified By pada baris `Branch 3`
23. Verifikasi tooltip menampilkan nama lengkap pengubah (`Admin A` menjadi `Admin Alpha`, `Admin B` menjadi `Admin Bravo`, `Admin C` menjadi `Admin Charlie`)

### TC-AC-SG-244: Kolom Field selalu berisi Group Name

24. Verifikasi sedikitnya satu baris tampil pada tabel Changelog
25. Verifikasi setiap baris (Create, Edit, dan Delete) menampilkan Field `Group Name`
26. Tutup modal Changelog lewat `[✕]`

### TC-AC-SG-242: Modal Changelog tanpa entri menampilkan empty state genuinely empty

27. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Changelog Kosong`
28. Buka halaman `Settings > Group` lewat sidebar
29. Klik ikon Changelog pada toolbar
30. Verifikasi empty state dengan Illustration, Title `No changelog yet`, dan Description `Activities and changes will appear here.`
31. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 12 (ukuran halaman 25 agar baris seed Create `Region B`, Edit `Region A1`, Delete `Branch 4`, dan `Branch 3` terbaca tanpa Search; jumlah seed lebih kecil dari 25 dan entitas `Distributor Changelog` tidak ditulis spec lain, S-14), penutupan modal sebelum ganti akun, dan penutupan modal di akhir.
- Urutan TC dalam spec: 241, 243, 244, 242 (TC-AC-SG-242 memakai akun lain sehingga ditaruh sesudah Step ganti akun di akhir, S-07/S-10). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal, jadi spec tidak dipisah.
- Asersi Create/Delete `—` ada di TC-AC-SG-241 butir c dan TC-AC-SG-243 butir a; keduanya memakai baris seed yang sama.
- Temuan untuk QA:
  - TC-AC-SG-241 butir c menyebut "default 10 baris" tanpa jumlah entri; spec memakai ketentuan bahwa seed berisi lebih dari 10 entri (Pre-setup #42 menyebut 12) dan tidak mengasersi total absolut.
  - TC-AC-SG-243 butir b tidak menulis nilai snapshot full path `Branch 3` (Pre-setup #42 hanya menulis path `Region B > Branch 4` untuk entri Delete); spec mengasersi tooltip sebagai snapshot path node tanpa menulis nilai literal.
  - TC-AC-SG-243 butir c tidak menyebut pengubah baris `Branch 3`; spec mengasersi format dan pemetaan nama lengkap dari Pre-setup #20 (`Admin A`, `Admin B`, `Admin C`).
  - Seed Changelog tidak menyebut jumlah entri Create/Edit/Delete per pengubah; asersi memakai baris yang disebut TC saja.
  - Env var password `AC_SG_CHANGELOG_PASSWORD` dan `AC_SG_CHANGELOGKOSONG_PASSWORD` didaftarkan pemilik repo (lihat `suite.md`).
