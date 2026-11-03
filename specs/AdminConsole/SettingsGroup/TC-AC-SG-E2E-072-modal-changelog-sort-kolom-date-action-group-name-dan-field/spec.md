---
id: TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field
title: "Modal Changelog: Sort Kolom Date, Action, Group Name, dan Field"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-260
  - TC-AC-SG-261
  - TC-AC-SG-262
  - TC-AC-SG-263
coverage:
  web: automated
---

# Modal Changelog: Sort Kolom Date, Action, Group Name, dan Field

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
2. Verifikasi sedikitnya dua baris tampil dan terdapat sedikitnya dua nilai distinct pada kolom Date, Action, dan Group Name di halaman pertama

### TC-AC-SG-260: Sort Changelog kolom Date: siklus tiga klik

3. Klik header Date sekali
4. Verifikasi klik pertama mengurutkan Date Oldest First
5. Klik header Date kedua kali
6. Verifikasi klik kedua mengurutkan Date Newest First
7. Klik header Date ketiga kali
8. Verifikasi klik ketiga netral kembali ke Newest First (default)

### TC-AC-SG-261: Sort Changelog kolom Action: siklus tiga klik

9. Klik header Action sekali
10. Verifikasi klik pertama mengurutkan Action ascending (A-Z)
11. Klik header Action kedua kali
12. Verifikasi klik kedua mengurutkan Action descending
13. Klik header Action ketiga kali
14. Verifikasi klik ketiga netral kembali ke Date terbaru di atas

### TC-AC-SG-262: Sort Changelog kolom Group Name: siklus tiga klik

15. Klik header Group Name sekali
16. Verifikasi klik pertama mengurutkan Group Name ascending (A-Z case-insensitive)
17. Klik header Group Name kedua kali
18. Verifikasi klik kedua mengurutkan Group Name descending
19. Klik header Group Name ketiga kali
20. Verifikasi klik ketiga netral kembali ke Date terbaru di atas

### TC-AC-SG-263: Sort Changelog kolom Field: siklus tiga klik

21. Klik header Field sekali
22. Verifikasi klik pertama mengurutkan Field ascending (A-Z)
23. Klik header Field kedua kali
24. Verifikasi klik kedua mengurutkan Field descending
25. Klik header Field ketiga kali
26. Verifikasi klik ketiga netral kembali ke Date terbaru di atas
27. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): penutupan modal di akhir dan pembukaan modal satu kali untuk keempat TC; tiap TC berakhir pada sort netral sehingga tidak perlu reset sort tambahan (S-09).
- Verifikasi pada Persiapan adalah pembanding generik dua nilai distinct (S-11, S-14, bagian 8b butir 2); bukan Expected TC.
- Temuan untuk QA:
  - Kolom Field hanya bernilai `Group Name` pada seluruh baris (TC-AC-SG-244, TC-AC-SG-247), sehingga hasil sort TC-AC-SG-263 tidak memiliki dua nilai distinct (S-11, S-14); spec mengasersi urutan sesuai Expected, tetapi urutan kolom Field tidak teruji secara bermakna. Usulan: TC-AC-SG-263 dibatasi pada asersi indikator sort.
  - Urutan sort kolom Action dan Group Name diasersi pada baris halaman pertama; tie-break antar baris bernilai sama tidak disebut TC.
