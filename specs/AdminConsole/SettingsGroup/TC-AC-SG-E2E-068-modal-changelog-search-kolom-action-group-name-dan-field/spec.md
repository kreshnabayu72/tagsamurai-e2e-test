---
id: TC-AC-SG-E2E-068-modal-changelog-search-kolom-action-group-name-dan-field
title: "Modal Changelog: Search Kolom Action, Group Name, dan Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-245
  - TC-AC-SG-246
  - TC-AC-SG-247
coverage:
  web: automated
---

# Modal Changelog: Search Kolom Action, Group Name, dan Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### Persiapan

1. Klik ikon Changelog pada toolbar
2. Verifikasi sedikitnya satu baris tampil pada tabel Changelog sebelum Search
3. Catat jumlah baris pada halaman pertama dan jumlah halaman sebelum Search

### TC-AC-SG-245: Search Changelog by kolom Action

4. Pastikan kolom Action tampil di tabel
5. Ketik Search `edit` pada toolbar modal, tekan Enter
6. Verifikasi baris dengan Action `Edit` tampil
7. Ganti isi kotak search dengan `EDIT`, tekan Enter
8. Verifikasi daftar baris yang tampil identik dengan hasil Search `edit`
9. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
10. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
11. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-246: Search Changelog by kolom Group Name

12. Pastikan kolom Group Name tampil di tabel
13. Ketik Search `region b` pada toolbar modal, tekan Enter
14. Verifikasi baris dengan Group Name `Region B` tampil
15. Ganti isi kotak search dengan `REGION B`, tekan Enter
16. Verifikasi daftar baris yang tampil identik dengan hasil Search `region b`
17. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
18. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
19. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-247: Search Changelog by kolom Field

20. Pastikan kolom Field tampil di tabel
21. Ketik Search `group name` pada toolbar modal, tekan Enter
22. Verifikasi tabel menampilkan seluruh baris: jumlah baris pada halaman pertama dan jumlah halaman sama dengan yang dicatat pada langkah 3
23. Ganti isi kotak search dengan `GROUP NAME`, tekan Enter
24. Verifikasi daftar baris yang tampil identik dengan hasil Search `group name`
25. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
26. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
27. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
28. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 3 (baseline tampilan sebelum Search, dipakai asersi TC-AC-SG-247 "seluruh baris"), klik `(←)` pada kotak Search di akhir tiap TC (S-09), penutupan modal di akhir, dan pembukaan modal satu kali untuk ketiga TC.
- Verifikasi sedikitnya satu baris tampil pada Persiapan adalah pembanding generik sebelum asersi hasil Search (bagian 8b butir 2); bukan Expected TC.
- Temuan untuk QA:
  - Expected b ("hasil identik untuk huruf kapital") tidak menyebut apa yang diperbandingkan; spec membandingkan daftar baris dengan hasil Search huruf kecil.
  - TC-AC-SG-247 menyebut "seluruh baris" tanpa jumlah; total entri seed tidak diasersi absolut (S-12), jadi spec memakai baseline jumlah baris halaman pertama dan jumlah halaman.
