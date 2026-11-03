---
id: TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol
title: "Modal Changelog: Filter Group Name, Modified By, Date, Kombinasi AND, dan Independensi Kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-255
  - TC-AC-SG-256
  - TC-AC-SG-257
  - TC-AC-SG-258
  - TC-AC-SG-259
coverage:
  web: automated
---

# Modal Changelog: Filter Group Name, Modified By, Date, Kombinasi AND, dan Independensi Kontrol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Data seed tambahan (disediakan tim FE/BE): sedikitnya satu entri Edit oleh `Admin A`, sedikitnya satu entri Create yang memuat kata `region`, dan entri pada 14 Jul 2026. Pre-setup #42 hanya menyebut tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain tanpa pembagian per pengubah (lihat Temuan untuk QA).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### Persiapan

1. Klik ikon Changelog pada toolbar

### TC-AC-SG-255: Filter Changelog by Group Name

2. Klik ikon Filter pada toolbar modal
3. Pilih Group Name `Branch 4` lalu klik `[Apply]`
4. Verifikasi entri Delete `Branch 4` termasuk yang tampil
5. Verifikasi setiap baris yang tampil bernilai Group Name `Branch 4`
6. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-256: Filter Changelog by Modified By

7. Klik ikon Filter pada toolbar modal
8. Pilih Modified By `Admin A` lalu klik `[Apply]`
9. Verifikasi sedikitnya satu baris tampil
10. Verifikasi setiap baris yang tampil bernilai Modified By `Admin A`
11. Buka dropdown Modified By
12. Verifikasi opsi dropdown Modified By hanya user pengubah yang ada pada Changelog: `Admin A`, `Admin B`, dan `Admin C`
13. Tutup dropdown Modified By lalu klik `[Clear Field]` dan `[Apply]` untuk membersihkan filter

### TC-AC-SG-257: Filter Changelog by Date: rentang inklusif

14. Klik ikon Filter pada toolbar modal
15. Pilih rentang Date 14 Jul 2026 sampai 14 Jul 2026 lalu klik `[Apply]`
16. Verifikasi sedikitnya satu baris tampil
17. Verifikasi setiap baris yang tampil bertanggal 14 Jul 2026
18. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-258: Kombinasi filter Changelog memakai logika AND dan dapat di-clear

19. Klik ikon Filter pada toolbar modal
20. Pilih Action `Edit` dan Modified By `Admin A`, lalu klik `[Apply]`
21. Verifikasi sedikitnya satu baris tampil
22. Verifikasi setiap baris yang tampil bernilai Action `Edit` dan Modified By `Admin A`
23. Klik `[Clear Field]`
24. Verifikasi seluruh field Filter Panel kosong (Date, Action, Group Name, dan Modified By)
25. Klik `[Apply]` untuk memulihkan tabel tanpa filter

### TC-AC-SG-259: Kombinasi Search, Filter, Sort, dan Pagination Changelog saling independen

26. Ketik Search `region` pada toolbar modal, tekan Enter
27. Pilih Action `Create` lalu klik `[Apply]`
28. Verifikasi sedikitnya satu baris tampil
29. Verifikasi setiap baris yang tampil bernilai Action `Create` dan memuat `region` pada kolom yang dicari Search
30. Klik header Date sekali
31. Verifikasi baris terurut Date ascending (Oldest First)
32. Verifikasi kotak Search masih berisi `region` dan Filter Action `Create` masih aktif
33. Klik nomor halaman `1` pada Pagination
34. Verifikasi kotak Search masih berisi `region`, Filter Action `Create` masih aktif, dan sort Date ascending masih berlaku
35. Klik `(←)` pada kotak Search, lalu klik `[Clear Field]` dan `[Apply]` untuk membersihkan Search dan Filter
36. Klik header Date dua kali hingga sort kembali ke default (Date terbaru di atas)
37. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): pembersihan filter (`[Clear Field]` lalu `[Apply]`) di akhir tiap TC (S-09); pemulihan Search, Filter, dan sort pada akhir TC-AC-SG-259; serta penutupan modal di akhir.
- Verifikasi sedikitnya satu baris tampil sebelum asersi "setiap baris" adalah pembanding generik (bagian 8b butir 2); bukan Expected TC. Pada TC-AC-SG-255 baris Delete `Branch 4` yang tampil menjadi pembandingnya.
- Spec ini melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional Filter dan kontrol Modal Changelog) pada satu dataset seed baca-saja; tiap blok TC membersihkan filter di akhir dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Pre-setup #42 tidak membagi 12 entri seed per pengubah dan per Action; TC-AC-SG-256 dan TC-AC-SG-258 mengandaikan entri Edit oleh `Admin A`, dan TC-AC-SG-259 mengandaikan entri Create yang memuat `region`. Kebutuhan ini ditulis sebagai data seed tambahan yang disediakan tim FE/BE.
  - TC-AC-SG-259 menyuruh "pindah halaman" padahal hasil Search `region` dengan Filter Action `Create` pada seed 12 entri tidak dijamin lebih dari satu halaman; spec mengklik nomor halaman `1` dan mengasersi Search, Filter, dan sort tetap berlaku. Usulan: TC memakai kombinasi yang menghasilkan sedikitnya dua halaman.
  - TC-AC-SG-258 menyebut "setelah `[Clear Field]` seluruh field kosong" tanpa menyatakan tabel kembali tanpa filter sebelum `[Apply]`; spec hanya mengasersi field kosong dan menekan `[Apply]` sebagai langkah penghubung.
  - TC-AC-SG-259: frasa "hasil memenuhi Search AND Filter" tidak menyebut kolom yang dicocokkan Search; spec mengasersi kata `region` pada kolom mana pun yang dicari Search.
