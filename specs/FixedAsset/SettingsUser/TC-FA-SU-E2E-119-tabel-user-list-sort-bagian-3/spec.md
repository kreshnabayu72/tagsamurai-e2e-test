---
id: TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3
title: "Tabel User List: Sort (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-337
  - TC-FA-SU-338
  - TC-FA-SU-339
  - TC-FA-SU-1053
coverage:
  web: automated
---

# Tabel User List: Sort (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Urutan default (netral) Name ascending: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`.
- Division `Finance & Accounting` memuat tujuh pengguna pada default sort Name ascending: `Budi Santoso`, `Gita Permata`, `Mira Anggraini`, `Nanda Pratama`, `Putri Anggraeni`, `Sinta Dewi`, `Teguh Prakoso`.
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

1. Klik header kolom Actions (⋯), klik `Setup Column...`
2. Centang `Temporary User`, `Temporary Until`, dan `Shift`, klik `[Save]`

### TC-FA-SU-337: Sort kelas yesno Temporary User

3. Klik header `Temporary User` satu kali
4. Verifikasi `Temporary User` ascending (↑): `Fajar Nugroho`, `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`
5. Klik header `Temporary User` kedua kali
6. Verifikasi `Temporary User` descending (↓): `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`
7. Klik header `Temporary User` ketiga kali
8. Verifikasi `Temporary User` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-338: Sort kelas date Temporary Until

9. Klik header `Temporary Until` satu kali
10. Verifikasi `Temporary Until` ascending (↑): `Fajar Nugroho`, `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`
11. Klik header `Temporary Until` kedua kali
12. Verifikasi `Temporary Until` descending (↓): `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`
13. Klik header `Temporary Until` ketiga kali
14. Verifikasi `Temporary Until` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-339: Sort kelas cf Shift

15. Klik header `Shift` satu kali
16. Verifikasi `Shift` ascending (↑): `Ahmad Dahlan`, `Budi Santoso`, `Doni Prasetyo`, `Fajar Nugroho`, `Gita Permata`
17. Klik header `Shift` kedua kali
18. Verifikasi `Shift` descending (↓): `Hana Kusuma`, `Kartika Sari`, `Citra Lestari`, `Eka Wulandari`, `Indra Wijaya`
19. Klik header `Shift` ketiga kali
20. Verifikasi `Shift` netral kembali ke default: `Ahmad Dahlan`, `Budi Santoso`, `Citra Lestari`, `Doni Prasetyo`, `Eka Wulandari`

### TC-FA-SU-1053: Sort Division deterministik

21. Klik header `Division` satu kali (ascending)
22. Verifikasi baris `Finance & Accounting` paling atas dan berurutan menurut default sort (Name ascending): `Budi Santoso`, `Gita Permata`, `Mira Anggraini`, `Nanda Pratama`, `Putri Anggraeni`, `Sinta Dewi`, `Teguh Prakoso` (7 baris)
23. Pindah ke halaman 2 lalu kembali ke halaman 1
24. Verifikasi urutan halaman 1 tidak berubah
25. Muat ulang halaman (F5), klik header `Division` satu kali
26. Verifikasi urutan baris `Finance & Accounting` sama dengan sebelum muat ulang

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 dan 2 (menampilkan kolom curated lewat Setup Column sekali untuk tiga blok berikutnya).
- Temuan untuk QA (S-15): (1) Daftar nama pada Expected TC berupa baris teratas hasil (kurang dari jumlah baris yang disebut atau dari ukuran halaman); spec mengasersi daftar nama itu dan jumlah baris sebagaimana tertulis. (2) Expected b TC-FA-SU-1053 menyatakan urutan tidak berubah "setelah muat ulang", sedangkan langkah 4 mengklik header lagi sesudah muat ulang; spec mengasersi hasil sesudah klik itu.
