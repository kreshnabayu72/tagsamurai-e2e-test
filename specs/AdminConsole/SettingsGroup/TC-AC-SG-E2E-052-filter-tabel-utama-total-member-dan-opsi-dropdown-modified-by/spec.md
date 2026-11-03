---
id: TC-AC-SG-E2E-052-filter-tabel-utama-total-member-dan-opsi-dropdown-modified-by
title: "Filter Tabel Utama: Filter Total Member dan Opsi Dropdown Modified By"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-187
  - TC-AC-SG-188
  - TC-AC-SG-189
coverage:
  web: automated
---

# Filter Tabel Utama: Filter Total Member dan Opsi Dropdown Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #19, #20), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z, page size bawaan 10 baris. Total Member per group: `Region A` 4, `Branch 1` 2, `Branch 2` 3, `Room 301` 1, `Region B` 1, `Region C` 1, node lain 0. Nilai Modified By distinct pada tabel: `Admin A`, `Admin B`, `Admin C`, `System` (nama lengkap pengubah: `Admin Alpha`, `Admin Bravo`, `Admin Charlie`).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-187: Filter tabel utama by Total Member: rentang Min–Max inklusif

1. Klik ikon Filter pada toolbar
2. Isi Total Member Min = 1 dan Max = 3
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan `Branch 1` (2), `Branch 2` (3), `Room 301` (1), `Region B` (1), dan `Region C` (1)
5. Verifikasi `Default Group` (Total Member 0) tidak tampil pada tabel
6. Verifikasi indikator filter aktif tampil pada ikon Filter
7. Ubah Total Member Min = 3 dan Max = 3
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan `Branch 2` (Total Member 3)

### TC-AC-SG-188: Filter tabel utama by Total Member: hanya Min atau hanya Max

10. Klik `[Clear Field]`
11. Isi hanya Total Member Min = 4
12. Klik `[Apply]`
13. Verifikasi tabel menampilkan baris dengan Total Member ≥ 4: `Region A` (4)
14. Kosongkan Min dan isi hanya Max = 1
15. Klik `[Apply]`
16. Verifikasi tabel menampilkan baris dengan Total Member ≤ 1: `Default Group` (0), `Region B` (1), `Region C` (1), dan `Room 301` (1)

### TC-AC-SG-189: Opsi dropdown filter Modified By diambil dari data tabel

17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Buka dropdown Modified By
20. Verifikasi opsi dropdown hanya nilai Modified By distinct pada tabel dengan label format sel: `Admin A`, `Admin B`, `Admin C`, `System`
21. Verifikasi dropdown berupa multi-select dengan kotak search internal
22. Verifikasi tidak ada opsi yang terpilih secara default
23. Tutup dropdown Modified By
24. Hover sel Modified By pada baris tabel yang menampilkan `Admin A`
25. Verifikasi tooltip sel menampilkan nama lengkap `Admin Alpha`

## Notes

- Langkah penghubung (S-03): langkah 23 (menutup dropdown Modified By sebelum hover supaya hover mengenai sel tabel), langkah 10 dan 17 (mengosongkan field filter), langkah 18 (menerapkan filter kosong supaya tabel pulih sebelum opsi dropdown dibaca, S-09). Filter Panel tetap terbuka dari langkah 1 sampai akhir; langkah "Klik ikon Filter" TC-188 dan TC-189 tidak diulang. Perilaku panel tetap terbuka sesudah `[Apply]` mengikuti TC-AC-SG-196.
- Langkah 7: TC-187 menulis "nilai tepat salah satu baris" tanpa nilai; spec memilih 3 (`Branch 2`, satu-satunya baris Total Member 3 menurut Pre-setup #19).
- Langkah 13 dan 16: Expected TC-188 menyebut "baris dengan nilai ≥ 4/≤ 1 tampil" tanpa nama; spec memakai baris menurut Pre-setup #19. Pada langkah 16 baris yang disebut berada pada halaman 1 menurut urutan bawaan Group A-Z (S-14).
- Langkah 24 dan 25: hover diarahkan ke baris tabel yang menampilkan `Admin A` (pemetaan nama lengkap menurut Pre-setup #20: `Admin A` = `Admin Alpha`; tabel sudah pulih tanpa filter sejak langkah 18).
- Langkah 20: daftar opsi dibandingkan dengan nilai Modified By distinct pada tabel menurut Pre-setup #20 (`Admin A`, `Admin B`, `Admin C`, `System`).
- Temuan untuk QA:
  - TC-AC-SG-189 Expected menyebut "nama lengkap tampil pada hover tabel" tanpa menyebut baris yang di-hover; spec memakai baris `Admin A` dan nama lengkap `Admin Alpha` menurut Pre-setup #20.
  - TC-AC-SG-187 langkah 5 dan TC-AC-SG-185 langkah 5: nilai Min = Max tidak ditulis TC.
