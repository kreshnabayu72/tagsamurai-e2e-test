---
id: TC-FA-SU-E2E-118-tabel-user-list-sort-bagian-2
title: "Tabel User List: Sort (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-334
  - TC-FA-SU-335
  - TC-FA-SU-336
coverage:
  web: automated
---

# Tabel User List: Sort (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Urutan default (netral) Name ascending: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`.
- Tabel `Sort Teks Eksak`:

| Kolom | Asc | Desc |
|---|---|---|
| Home Group | `Eka Wulandari`, `Fajar Nugroho`, `Lukman Hakim`, `Umar Faruq`, `Budi Santoso` | `Doni Prasetyo`, `Rina Susanti`, `Rudi Hartono`, `Ahmad Dahlan`, `Indra Wijaya` |
| Position | `Gita Permata`, `Putri Anggraeni`, `Eka Wulandari`, `Lukman Hakim`, `Teguh Prakoso` | `Rudi Hartono`, `Doni Prasetyo`, `Fajar Nugroho`, `Yuda Pratama`, `Umar Faruq` |
| Employee ID | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Fajar Nugroho` | `Doni Prasetyo`, `Yuda Pratama`, `Wawan Setiawan`, `Vina Maharani`, `Umar Faruq` |
| TAG | `Budi Santoso`, `Ahmad Dahlan`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari` | `Ahmad Dahlan`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`, `Fajar Nugroho` |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-334: Sort kelas teks eksak

1. Klik header kolom Actions (⋯), klik `Setup Column...`
2. Centang `TAG`, klik `[Save]`
3. Untuk setiap baris tabel `Sort Teks Eksak` di Prerequisites (langkah 4 sampai 9):
4. Klik header `<Kolom>` satu kali
5. Verifikasi `<Kolom>` ascending (↑): <Asc>
6. Klik header `<Kolom>` kedua kali
7. Verifikasi `<Kolom>` descending (↓): <Desc>
8. Klik header `<Kolom>` ketiga kali
9. Verifikasi `<Kolom>` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-335: Sort kelas user Modified By

10. Klik header `Modified By` satu kali
11. Verifikasi `Modified By` ascending (↑): `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`, `Hana Kusuma`
12. Klik header `Modified By` kedua kali
13. Verifikasi `Modified By` descending (↓): `Ahmad Dahlan`, `Doni Prasetyo`, `Fajar Nugroho`, `Indra Wijaya`, `Kartika Sari`
14. Klik header `Modified By` ketiga kali
15. Verifikasi `Modified By` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-336: Sort kelas date Last Updated

16. Klik header `Last Updated` satu kali
17. Verifikasi `Last Updated` ascending (↑): `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`
18. Klik header `Last Updated` kedua kali
19. Verifikasi `Last Updated` descending (↓): `Yuda Pratama`, `Wawan Setiawan`, `Vina Maharani`, `Umar Faruq`, `Teguh Prakoso`
20. Klik header `Last Updated` ketiga kali
21. Verifikasi `Last Updated` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 dan 2 (menampilkan kolom `TAG` lewat Setup Column).
- Langkah yang diulang: langkah 4 sampai 9 (empat kolom), parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 4 sampai 9) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman.
