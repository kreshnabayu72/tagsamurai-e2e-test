---
id: TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination
title: "Modal Changelog: Sort Kolom Old Value, New Value, Modified By, dan Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-264
  - TC-AC-SG-265
  - TC-AC-SG-266
  - TC-AC-SG-268
coverage:
  web: automated
---

# Modal Changelog: Sort Kolom Old Value, New Value, Modified By, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan baca Fixture BE: jumlah entri Changelog Group entitas `Distributor Changelog` sebelum aksi (N); seed Pre-setup #42 lebih dari 10 dan kurang dari 25 entri, sehingga default 10 baris menghasilkan dua halaman dan ukuran halaman 25 memuat seluruh entri dalam satu halaman.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### Persiapan

1. Klik ikon Changelog pada toolbar
2. Catat jumlah entri Changelog (N) lewat Fixture BE

### TC-AC-SG-268: Pagination Changelog default 10 dan pilihan 10/25/50/100

3. Verifikasi Pagination menampilkan default 10 baris per halaman pada halaman pertama
4. Verifikasi pilihan page size 10, 25, 50, dan 100 tersedia
5. Ganti page size menjadi 25
6. Verifikasi seluruh N entri (langkah 2) tampil dalam satu halaman

### TC-AC-SG-264: Sort Changelog kolom Old Value: siklus tiga klik

7. Klik header Old Value sekali
8. Verifikasi klik pertama mengurutkan Old Value ascending dengan nilai kosong `—` di akhir
9. Klik header Old Value kedua kali
10. Verifikasi klik kedua mengurutkan Old Value descending
11. Klik header Old Value ketiga kali
12. Verifikasi klik ketiga netral kembali ke Date terbaru di atas

### TC-AC-SG-265: Sort Changelog kolom New Value: siklus tiga klik

13. Klik header New Value sekali
14. Verifikasi klik pertama mengurutkan New Value ascending dengan nilai kosong `—` di akhir
15. Klik header New Value kedua kali
16. Verifikasi klik kedua mengurutkan New Value descending
17. Klik header New Value ketiga kali
18. Verifikasi klik ketiga netral kembali ke Date terbaru di atas

### TC-AC-SG-266: Sort Changelog kolom Modified By: siklus tiga klik

19. Klik header Modified By sekali
20. Verifikasi klik pertama mengurutkan Modified By ascending menurut nama lengkap A-Z
21. Klik header Modified By kedua kali
22. Verifikasi klik kedua mengurutkan Modified By descending
23. Klik header Modified By ketiga kali
24. Verifikasi klik ketiga netral kembali ke Date terbaru di atas
25. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 2 (baseline N), ukuran halaman 25 yang dipertahankan untuk sort Old Value, New Value, dan Modified By (seluruh baris tampil sehingga nilai kosong `—` di akhir teramati, S-14), dan penutupan modal di akhir. Tiap TC sort berakhir pada sort netral (S-09).
- Temuan untuk QA:
  - Expected TC-AC-SG-268 menyebut "12 entri dalam satu halaman" sebagai angka absolut seed; spec menulisnya relatif terhadap N yang dibaca sebelum aksi (S-12, bagian 8b butir 10).
  - Urutan Modified By ascending diasersi menurut nama lengkap (`Admin Alpha`, `Admin Bravo`, `Admin Charlie`) sementara kolom menampilkan format `Admin A`, `Admin B`, `Admin C` (R-14).
  - Urutan descending untuk nilai kosong `—` pada Old Value dan New Value tidak disebut TC; spec hanya mengasersi kebalikan urutan nilai terisi.
