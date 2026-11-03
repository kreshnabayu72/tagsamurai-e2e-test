---
id: TC-AC-SG-E2E-069-modal-changelog-search-kolom-old-value-new-value-dan-modified-by
title: "Modal Changelog: Search Kolom Old Value, New Value, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-248
  - TC-AC-SG-249
  - TC-AC-SG-250
coverage:
  web: automated
---

# Modal Changelog: Search Kolom Old Value, New Value, dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Ketujuh kolom default Changelog (Date, Action, Group Name, Field, Old Value, New Value, Modified By) tampil secara default; preferensi kolom di browser bersih.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### Persiapan

1. Klik ikon Changelog pada toolbar
2. Verifikasi sedikitnya satu baris tampil pada tabel Changelog sebelum Search

### TC-AC-SG-248: Search Changelog by kolom Old Value

3. Ketik Search `region a1` pada toolbar modal, tekan Enter
4. Verifikasi baris Edit dengan Old Value `Region A1` dan New Value `Region A` tampil
5. Ganti isi kotak search dengan `REGION A1`, tekan Enter
6. Verifikasi daftar baris yang tampil identik dengan hasil Search `region a1`
7. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
8. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
9. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-249: Search Changelog by kolom New Value

10. Ketik Search `branch 3` pada toolbar modal, tekan Enter
11. Verifikasi baris Create dengan New Value `Branch 3` tampil
12. Ganti isi kotak search dengan `BRANCH 3`, tekan Enter
13. Verifikasi daftar baris yang tampil identik dengan hasil Search `branch 3`
14. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
15. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-250: Search Changelog by kolom Modified By

17. Ketik Search `admin b` pada toolbar modal, tekan Enter
18. Verifikasi baris dengan Modified By `Admin B` (pelaku `Admin Bravo`) tampil
19. Ganti isi kotak search dengan `ADMIN B`, tekan Enter
20. Verifikasi daftar baris yang tampil identik dengan hasil Search `admin b`
21. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
22. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
23. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
24. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap TC (S-09), penutupan modal di akhir, dan pembukaan modal satu kali untuk ketiga TC.
- Verifikasi sedikitnya satu baris tampil pada Persiapan adalah pembanding generik (bagian 8b butir 2); bukan Expected TC.
- Langkah "Pastikan kolom Old Value tampil", "Pastikan kolom New Value tampil", dan "Pastikan kolom Modified By tampil" (TC-AC-SG-248, TC-AC-SG-249, TC-AC-SG-250) dipenuhi oleh Prerequisites (tujuh kolom default Changelog tampil) dan tidak ditulis sebagai langkah terpisah.
- Temuan untuk QA:
  - TC-AC-SG-250 menulis Expected "baris yang dimodifikasi `Admin Bravo`" sedangkan kolom Modified By tampil `Admin B` (R-14); spec mengasersi nilai kolom `Admin B` dan menyebut pelaku `Admin Bravo` sebagai keterangan.
  - Expected b ("hasil identik untuk huruf kapital") tidak menyebut apa yang diperbandingkan; spec membandingkan daftar baris dengan hasil Search huruf kecil.
