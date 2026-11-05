---
id: TC-FA-SU-E2E-117-tabel-user-list-sort-bagian-1
title: "Tabel User List: Sort (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-331
  - TC-FA-SU-332
  - TC-FA-SU-333
coverage:
  web: automated
---

# Tabel User List: Sort (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna) dan atribut User List (#43). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Urutan default (netral) Name ascending: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`.
- Tabel `Sort Teks Non-Eksak`:

| Kolom | Asc | Desc |
|---|---|---|
| Name | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari` | `Yuda Pratama`, `Wawan Setiawan`, `Vina Maharani`, `Umar Faruq`, `Teguh Prakoso` |
| Email | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari` | `Yuda Pratama`, `Wawan Setiawan`, `Vina Maharani`, `Umar Faruq`, `Teguh Prakoso` |
| Division | `Budi Santoso`, `Gita Permata`, `Mira Anggraini`, `Nanda Pratama`, `Putri Anggraeni` | `Eka Wulandari`, `Lukman Hakim`, `Umar Faruq`, `Wawan Setiawan`, `Doni Prasetyo` |
| Activation Status | `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari` | `Indra Wijaya`, `Lukman Hakim`, `Hana Kusuma`, `Kartika Sari`, `Ahmad Dahlan` |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-331: Sort kelas toggle Active

1. Klik header `Active` satu kali
2. Verifikasi `Active` ascending (↑): `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Eka Wulandari`, `Gita Permata`
3. Klik header `Active` kedua kali
4. Verifikasi `Active` descending (↓): `Doni Prasetyo`, `Fajar Nugroho`, `Kartika Sari`, `Lukman Hakim`, `Ahmad Dahlan`
5. Klik header `Active` ketiga kali
6. Verifikasi `Active` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-332: Sort kelas teks non-eksak

7. Klik header kolom Actions (⋯), klik `Setup Column...`
8. Centang `Activation Status`, klik `[Save]`
9. Untuk setiap baris tabel `Sort Teks Non-Eksak` di Prerequisites (langkah 10 sampai 15):
10. Klik header `<Kolom>` satu kali
11. Verifikasi `<Kolom>` ascending (↑): <Asc>
12. Klik header `<Kolom>` kedua kali
13. Verifikasi `<Kolom>` descending (↓): <Desc>
14. Klik header `<Kolom>` ketiga kali
15. Verifikasi `<Kolom>` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-333: Sort kelas role

16. Klik header `Role` satu kali
17. Verifikasi `Role` ascending (↑): `Doni Prasetyo`, `Fajar Nugroho`, `Hana Kusuma`, `Kartika Sari`, `Indra Wijaya`
18. Klik header `Role` kedua kali
19. Verifikasi `Role` descending (↓): `Ahmad Dahlan`, `Lina Marlina`, `Citra Lestari`, `Oscar Pranata` (48), `Qori Akbar` (25)
20. Klik header `Role` ketiga kali
21. Verifikasi `Role` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 7 dan 8 (menampilkan kolom `Activation Status` lewat Setup Column).
- Langkah yang diulang: langkah 10 sampai 15 (empat kolom), parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis. (2) Angka `48` dan `25` pada Expected TC-FA-SU-333 (label Role Oscar Pranata dan Qori Akbar) diturunkan dari baris pola Group Manager dan perilaku hitung belum diputuskan PM (Open Item 3 PRD settings-user); spec mengasersi urutan nama beserta angka sesuai TC.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 10 sampai 15) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman.
