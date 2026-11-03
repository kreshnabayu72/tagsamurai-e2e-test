---
id: TC-AC-SG-E2E-051-filter-tabel-utama-screening-panel-dan-total-user
title: "Filter Tabel Utama: Screening Filter Panel dan Filter Total User"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-184
  - TC-AC-SG-185
  - TC-AC-SG-186
coverage:
  web: automated
---

# Filter Tabel Utama: Screening Filter Panel dan Filter Total User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Total User per group: `Default Group` 5, `Region A` 5, `Branch 1` 4, `Warehouse Jakarta` 3, node lain 2. Nilai Total User berbeda-beda (2, 3, 4, 5) sehingga filter rentang bermakna (S-11).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-184: Screening Filter Panel tabel utama

1. Klik ikon Filter pada toolbar
2. Verifikasi field pertama Total User bertipe Range Min–Max dengan placeholder `Min` dan `Max`
3. Verifikasi field kedua Total Member bertipe Range Min–Max dengan placeholder `Min` dan `Max`
4. Verifikasi field ketiga Modified By berupa dropdown multi-select searchable dengan placeholder `All users`
5. Verifikasi field keempat Last Updated berupa date range picker dengan placeholder `Select date`
6. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi tidak ada field filter untuk kolom Group
8. Verifikasi ikon Filter berwarna gelap selama panel terbuka

### TC-AC-SG-185: Filter tabel utama by Total User: rentang Min–Max inklusif

9. Isi Total User Min = 3 dan Max = 5
10. Klik `[Apply]`
11. Verifikasi tabel menampilkan `Default Group` (5), `Region A` (5), `Branch 1` (4), dan `Warehouse Jakarta` (3)
12. Verifikasi indikator filter aktif tampil pada ikon Filter
13. Ubah Total User Min = 4 dan Max = 4
14. Klik `[Apply]`
15. Verifikasi tabel menampilkan `Branch 1` (Total User 4)

### TC-AC-SG-186: Filter tabel utama by Total User: hanya Min atau hanya Max

16. Klik `[Clear Field]`
17. Isi hanya Total User Min = 4
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan baris dengan Total User ≥ 4: `Default Group` (5), `Region A` (5), dan `Branch 1` (4)
20. Kosongkan Min dan isi hanya Max = 1
21. Klik `[Apply]`
22. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Langkah penghubung (S-03): langkah 16 (mengosongkan field filter sebelum mengisi hanya Min, S-09). Filter Panel tetap terbuka dari langkah 1 sampai akhir; TC-AC-SG-185 dan TC-AC-SG-186 melanjutkan panel yang sama sehingga langkah "Klik ikon Filter" TC tersebut tidak diulang. Perilaku panel tetap terbuka sesudah `[Apply]` mengikuti TC-AC-SG-196 (menutup panel dengan klik ikon Filter).
- Langkah 13: TC-185 menulis "nilai tepat salah satu baris" tanpa nilai; spec memilih 4 (`Branch 1`, satu-satunya baris Total User 4 menurut Pre-setup #17).
- Langkah 19: Expected TC-186 a menulis "baris dengan nilai ≥ 4 tampil" tanpa nama baris; spec memakai baris menurut Pre-setup #17.
- Temuan untuk QA:
  - TC-AC-SG-185 langkah 5 dan TC-AC-SG-187 langkah 5 tidak menyebut nilai Min = Max; spec memilih nilai dari Pre-setup #17/#19.
  - TC-AC-SG-186 Expected b: "tidak ada baris sehingga empty state" ditulis dalam kurung sebagai penjelasan Total User; spec mengasersi empty state sebagai hasil Max = 1.
