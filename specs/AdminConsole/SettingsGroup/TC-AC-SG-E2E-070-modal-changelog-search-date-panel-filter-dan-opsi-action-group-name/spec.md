---
id: TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name
title: "Modal Changelog: Search Date, Panel Filter, dan Opsi Action serta Group Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-251
  - TC-AC-SG-252
  - TC-AC-SG-253
  - TC-AC-SG-254
coverage:
  web: automated
---

# Modal Changelog: Search Date, Panel Filter, dan Opsi Action serta Group Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan baca Fixture BE: nilai Group Name distinct dari seluruh baris Changelog entitas `Distributor Changelog` (dipakai asersi TC-AC-SG-253).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### Persiapan

1. Klik ikon Changelog pada toolbar
2. Ganti page size menjadi 25 agar seluruh baris seed tampil dalam satu halaman

### TC-AC-SG-251: Search Changelog tidak mencocokkan kolom Date

3. Salin teks Date baris pertama, tempel ke Search pada toolbar modal, tekan Enter
4. Verifikasi tidak ada baris yang cocok: empty state `No results found` dengan Description `Try adjusting your search or filter.`
5. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-252: Screening Filter Panel Changelog tanpa filter Field

6. Klik ikon Filter pada toolbar modal
7. Verifikasi urutan field Filter Panel dari atas: Date, Action, Group Name, Modified By
8. Verifikasi field Date berupa date range picker dengan placeholder `Select date`
9. Verifikasi field Action berupa multi-select searchable dengan placeholder `All actions`
10. Verifikasi field Group Name berupa multi-select searchable dengan placeholder `All groups`
11. Verifikasi field Modified By berupa multi-select searchable dengan placeholder `All users`
12. Verifikasi Filter Field tidak ditampilkan
13. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-AC-SG-253: Opsi filter Action dan Group Name diambil dari data tabel termasuk group terhapus

14. Buka dropdown Action
15. Verifikasi opsi Action menampilkan `Create`, `Edit`, dan `Delete`
16. Tutup dropdown Action
17. Buka dropdown Group Name
18. Verifikasi opsi Group Name memuat nilai distinct dari baris Changelog
19. Verifikasi opsi Group Name memuat `Branch 4` walau group sudah dihapus
20. Tutup dropdown Group Name

### TC-AC-SG-254: Filter Changelog by Action: satu dan dua opsi

21. Pilih Action `Create` lalu klik `[Apply]`
22. Verifikasi sedikitnya satu baris tampil
23. Verifikasi setiap baris yang tampil bernilai Action `Create`
24. Tambahkan Action `Delete` lalu klik `[Apply]`
25. Verifikasi baris Create dan baris Delete sama-sama tampil
26. Verifikasi tidak ada baris Edit yang tampil
27. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter
28. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 2 (baris seed terbaca tanpa Search; jumlah seed lebih kecil dari 25 dan entitas `Distributor Changelog` tidak ditulis spec lain, S-14), penutupan dropdown, klik `(←)` pada kotak Search, pembersihan filter di akhir (S-09), dan penutupan modal di akhir.
- Bagian Expected TC-AC-SG-251 "filter tanggal hanya lewat Filter Panel" adalah penjelasan desain tanpa perilaku yang bisa gagal sendiri; pencocokan Date lewat Filter Panel diasersi di spec 071 (TC-AC-SG-257).
- Temuan untuk QA:
  - TC-AC-SG-253 butir b menyebut "nilai distinct dari baris Changelog" tanpa daftar nilai; spec membandingkan opsi dengan nilai yang dibaca lewat Fixture BE dan mengasersi `Branch 4` secara eksplisit.
  - TC-AC-SG-252 butir b "Filter Field tidak ditampilkan" diasersi sebagai ketiadaan field berlabel Field di panel; empat field lain yang sudah tampil menjadi anchor.
  - TC-AC-SG-254: Expected b "tidak menampilkan Edit" diasersi sesudah baris Create dan Delete tampil (anchor).
