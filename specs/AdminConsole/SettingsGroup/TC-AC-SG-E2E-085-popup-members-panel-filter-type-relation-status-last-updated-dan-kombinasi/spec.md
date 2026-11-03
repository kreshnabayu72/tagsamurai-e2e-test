---
id: TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi
title: "Popup Members: Panel Filter, Type, Relation Status, Last Updated, dan Kombinasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-315
  - TC-AC-SG-316
  - TC-AC-SG-317
  - TC-AC-SG-318
  - TC-AC-SG-319
coverage:
  web: automated
---

# Popup Members: Panel Filter, Type, Relation Status, Last Updated, dan Kombinasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18), Total Member (#19), Last Updated dan Modified By (#20). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`); Total Member 4 bertipe Distributor (`Distributor Alpha` Active 14 Jul 2026, `Distributor Beta` Suspended 12 Jul 2026, `Distributor Delta` Active 11 Jul 2026, `Distributor Gamma` Suspended 10 Jul 2026). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini. Pre-setup #17 dan #18 dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total Member pada baris `Region A`

### TC-AC-SG-315: Screening Filter Panel popup Members

3. Klik ikon Filter pada toolbar popup
4. Verifikasi field Type berupa multi-select searchable dengan placeholder `All types`
5. Verifikasi field Relation Status berupa multi-select searchable dengan placeholder `All statuses`
6. Verifikasi field Last Updated berupa date range picker dengan placeholder `Select date`
7. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-AC-SG-316: Filter Type: opsi dari data node dan hasil filter

8. Buka dropdown Type
9. Verifikasi opsi Type hanya `Distributor` (tanpa `Partner` dan `Client`)
10. Pilih `Distributor` lalu klik `[Apply]`
11. Verifikasi keempat entitas `Region A` tampil: `Distributor Alpha`, `Distributor Beta`, `Distributor Delta`, dan `Distributor Gamma`
12. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-317: Filter Relation Status: opsi dari data node

13. Buka dropdown Relation Status
14. Verifikasi opsi Relation Status hanya status yang ada pada data node: `Active` dan `Suspended`
15. Pilih `Suspended` lalu klik `[Apply]`
16. Verifikasi baris `Distributor Beta` dan `Distributor Gamma` tampil
17. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-318: Filter Last Updated popup Members dengan rentang tanggal inklusif

18. Pilih rentang Last Updated 11 Jul 2026 sampai 12 Jul 2026 lalu klik `[Apply]`
19. Verifikasi baris `Distributor Beta` (12 Jul 2026) dan `Distributor Delta` (11 Jul 2026) tampil
20. Verifikasi `Distributor Alpha` (14 Jul 2026) dan `Distributor Gamma` (10 Jul 2026) tidak tampil
21. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-319: Kombinasi filter popup Members tanpa hasil menampilkan empty state dan Clear Field memulihkan

22. Pilih Relation Status `Suspended` dan Last Updated rentang 14 Jul 2026 sampai 14 Jul 2026, lalu klik `[Apply]`
23. Verifikasi empty state `No results found` dengan Description `Try adjusting your search or filter.`
24. Klik `[Clear Field]` lalu klik `[Apply]`
25. Verifikasi keempat entitas `Region A` tampil lagi
26. Tutup popup lewat `[✕]`
27. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), pembersihan filter (`[Clear Field]` lalu `[Apply]`) di akhir tiap TC (S-09), penutupan popup, dan klik `(←)` pada Search tabel utama di akhir. Popup dibuka satu kali untuk kelima TC.
- Asersi "tidak tampil" pada TC-AC-SG-318 didahului Verifikasi `Distributor Beta` dan `Distributor Delta` tampil pada surface yang sama (anchor, bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-SG-318 menulis Expected "hanya entitas dengan Last Updated dalam rentang" tanpa menyebut entitas yang tidak tampil; spec mengasersi `Distributor Alpha` dan `Distributor Gamma` tidak tampil berdasarkan Last Updated Pre-setup #19.
  - TC-AC-SG-319: langkah "Klik `[Clear Field]` lalu `[Apply]`" ditulis satu langkah mengikuti TC.
  - Perilaku panel Filter sesudah `[Apply]` di popup tidak dinyatakan PRD (T12); spec mengasumsikan panel tetap terbuka (pola spec 078 dan 079), sehingga klik ikon Filter berikutnya tidak diulang. Perlu konfirmasi FE.
