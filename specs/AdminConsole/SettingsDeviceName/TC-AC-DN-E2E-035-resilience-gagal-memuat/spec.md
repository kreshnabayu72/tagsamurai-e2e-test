---
id: TC-AC-DN-E2E-035-resilience-gagal-memuat
title: "Resilience: Gagal Memuat List, Usage by Company, dan Changelog, serta Try Again"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-29
  - TC-AC-DN-30
  - TC-AC-DN-618
  - TC-AC-DN-404
coverage:
  web: automated
---

# Resilience: Gagal Memuat List, Usage by Company, dan Changelog, serta Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-29, 30, 618, 404 |

- Env var password: `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (dibaca saja): Device Name inti (#16); Usage by Company `Gate Antenna` Company A sampai Company E (#18); Riwayat Changelog Uji (#19) dengan jumlah entri lebih dari 10 sehingga halaman 1 berisi 10 baris; General Settings entitas uji (#20).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menjawab request dengan status 500, menahan respons sampai batas waktu, dan menunda respons; intercept dilepas segera setelah pemicunya selesai (S-09).
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-AC-DN-29: Gagal memuat List menampilkan Unable to load this data dan tombol Try Again

1. Pasang intercept: respons list Device Name dijawab status 500
2. Buka halaman `Settings > Device > Device Name`
3. Verifikasi area tabel menampilkan "Unable to load this data." dan tombol `[Try Again]`
4. Verifikasi tampilan ini bukan empty state (tanpa "No device names yet" maupun "No results found")
5. Verifikasi tidak ada toast yang tampil untuk kegagalan pemuatan ini
6. Lepas intercept respons list Device Name

### TC-AC-DN-30: Klik Try Again setelah gagal memuat List berhasil memuat data

7. Pasang intercept: respons list Device Name dijawab status 500
8. Buka halaman `Settings > Device > Device Name`
9. Lepas intercept sehingga respons list kembali normal
10. Pasang intercept: respons list Device Name ditunda
11. Klik tombol `[Try Again]`
12. Verifikasi loading tampil
13. Lepas intercept penundaan respons list Device Name
14. Verifikasi baris Device Name tampil mulai dari Barcode Station
15. Verifikasi tampilan `Unable to load this data.` hilang

### TC-AC-DN-618: Gagal memuat tabel Usage by Company menampilkan Unable to load this data dan tombol Try Again

16. Pasang intercept: respons usage list Device Name dijawab status 500
17. Klik nama `Gate Antenna`
18. Verifikasi area tabel Usage menampilkan "Unable to load this data." dan tombol `[Try Again]`
19. Verifikasi tampilan ini bukan empty state (tanpa "No usage data yet" maupun "No results found")
20. Verifikasi tidak ada toast untuk kegagalan pemuatan ini
21. Lepas intercept respons usage list Device Name
22. Pasang intercept: respons usage list Device Name ditunda
23. Klik tombol `[Try Again]`
24. Verifikasi loading tampil
25. Lepas intercept penundaan respons usage list Device Name
26. Verifikasi lima baris `Company A` sampai `Company E` tampil
27. Verifikasi error-load hilang
28. Tutup dialog Detail

### TC-AC-DN-404: Popup Changelog saat pemuatan data gagal

29. Pasang intercept: request data Changelog dijawab respons server error
30. Klik ikon Changelog di toolbar
31. Verifikasi tabel tidak menampilkan baris data dan area tabel menampilkan error-load standar "Unable to load this data." dan tombol `[Try Again]`
32. Verifikasi tampilan bukan empty state: tidak ada teks `No changes recorded yet.` dan tidak ada "No results found"
33. Matikan intercept request data Changelog
34. Klik `[Try Again]`
35. Verifikasi error-load hilang
36. Verifikasi tabel menampilkan 10 baris halaman 1
37. Tutup popup "Changelog: Device Name"

## Notes

- Spec resilience (kelas b): kegagalan memuat yang dipaksa lewat intercept di atas backend nyata (bagian 6, `FE+BE`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): melepas intercept segera setelah asersi (langkah 6) dan menutup dialog Detail serta popup Changelog. Langkah penghubung penundaan respons (langkah 10 dan 22, S-03): `Spectra.intercept` menunda respons sebelum klik `[Try Again]` dan dilepas sesudah asersi loading (langkah 13 dan 25), agar loading teramati. Langkah "Pasang intercept" TC-AC-DN-30 mengulang langkah TC sendiri karena TC-AC-DN-29 melepas intercept sebelum TC berikutnya (S-09).
- Ukuran spec (37 langkah, di atas 35 langkah): tiga blok kegagalan memuat (List, Usage by Company, Changelog) satu kelas harness (b) dengan pola intercept yang sama; tiap blok berdiri sendiri dan memulihkan intercept sebelum blok berikutnya.
- Temuan untuk QA:
  - TC-AC-DN-404 Expected c menyebut "10 baris halaman 1 dari 11 entri"; total entri Changelog adalah audit trail yang tumbuh (S-12) sehingga angka 11 tidak diasersi, hanya 10 baris halaman 1.
  - TC-AC-DN-30 langkah 3 melepas intercept sebelum `[Try Again]`; urutan diikuti apa adanya.
