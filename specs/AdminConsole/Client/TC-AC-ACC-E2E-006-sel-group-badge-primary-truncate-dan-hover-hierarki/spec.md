---
id: TC-AC-ACC-E2E-006-sel-group-badge-primary-truncate-dan-hover-hierarki
title: "Sel Group List Client: Badge Primary, Truncate 25 Karakter, dan Hover Hierarki Penuh"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-11
coverage:
  web: automated
---

# Sel Group List Client: Badge Primary, Truncate 25 Karakter, dan Hover Hierarki Penuh

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Client `PT Grup Panjang Uji` (C-ISO-1; Direct, Group `Cabang Menteng`, belum pernah memiliki subscription; kelas Dipulihkan) adalah target aksi tulis; efek pada Client ini: Modified By, Last Updated, dan baris Changelog `Edit` bertambah, dan Group dikembalikan ke `Cabang Menteng` dalam spec.
- Group sementara `Cabang Pelayanan Pusat Jakarta Raya` (35 karakter, di bawah Area Jakarta, kelas Sementara) dibuat hook `before` lewat Fixture BE (TC menyebut pembuatan lewat Settings > Group) dan dihapus hook `after` lewat Fixture BE; nama literal karena asersi truncate bergantung pada panjang nama.
- Kemampuan teknis: Fixture BE untuk membuat dan menghapus Group sementara; pemulihan Group Client ke `Cabang Menteng` oleh langkah spec, dan hook `after` memulihkannya lewat Fixture BE bila spec gagal di tengah.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-11: Kolom Group berupa badge primary dengan truncate dan hover hierarki penuh

1. Ketik Search `PT Baru Daftar`, tekan Enter
2. Lihat badge Group baris `PT Baru Daftar`, lalu arahkan kursor ke badge tersebut
3. Verifikasi badge Group `PT Baru Daftar` severity primary bertuliskan `Cabang Menteng` (14 karakter, tampil utuh)
4. Verifikasi hover menampilkan hierarki penuh `Regional Barat > Area Jakarta > Cabang Menteng`
5. Ganti isi kotak Search dengan `PT Grup Panjang Uji`, tekan Enter
6. Buka `⋯` baris `PT Grup Panjang Uji`, lalu klik `Edit`
7. Pilih Group `Cabang Pelayanan Pusat Jakarta Raya` pada tree Select Group, lalu klik `[Save]`
8. Tunggu aksi `[Save]` selesai (popup Edit tertutup)
9. Muat ulang halaman (F5), ketik Search `PT Grup Panjang Uji`, tekan Enter
10. Lihat badge Group baris `PT Grup Panjang Uji`, lalu arahkan kursor ke badge tersebut
11. Verifikasi badge Group severity primary bertuliskan `Cabang Pelay..Jakarta Raya` (12 huruf pertama + `..` + 12 huruf terakhir)
12. Verifikasi hover menampilkan hierarki penuh `Regional Barat > Area Jakarta > Cabang Pelayanan Pusat Jakarta Raya`
13. Buka `⋯` baris `PT Grup Panjang Uji`, klik `Edit`, pilih Group `Cabang Menteng` pada tree Select Group, klik `[Save]`, lalu tunggu popup Edit tertutup
14. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 8, 13, 14. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Langkah 11–12 mengasersi truncate nama Group > 25 karakter (12 huruf pertama + `..` + 12 huruf terakhir) dan nama <= 25 karakter tampil utuh (aturan prd-conventions §9.14 yang dikutip TC).
- Temuan untuk QA:
  - TC-AC-ACC-11: Post Condition b ("Hapus Group ... lewat Settings > Group") dilakukan hook `after` lewat Fixture BE, bukan lewat UI Settings > Group; Precondition e menyebut pembuatan lewat Settings > Group yang di spec digantikan seeding hook `before`.
  - TC-AC-ACC-11: Expected tidak menyebut toast hasil `[Save]`; spec tidak mengasersi toast dan memakai langkah penghubung "Tunggu aksi selesai" sebelum muat ulang.
