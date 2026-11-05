---
id: TC-FA-FAAC-E2E-026-role-matrix-negatif-read-only
title: "Role Matrix Negatif: Read Only (Tooltip Toggle Active dan Kontrol Tab Asset Names Tidak Tersedia)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-43
  - TC-FA-FAAC-633
  - TC-FA-FAAC-612
coverage:
  web: automated
---

# Role Matrix Negatif: Read Only (Tooltip Toggle Active dan Kontrol Tab Asset Names Tidak Tersedia)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Read Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-43, TC-FA-FAAC-633, TC-FA-FAAC-612 |

- Env var: `FA_AC_RO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class B-ANCHOR (Anchor Heavy Equipment, Active, tanpa Asset Name; seed Pre-setup, dependensi TC-FA-FAAC-87 dijalankan lewat seeding API); HEAVY-EQ memiliki tiga Asset Name ter-assign Excavator PC200, Wheel Loader, dan Crane Rental Unit (seed Pre-setup). Dibaca, tidak diubah. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: navigasi keyboard (Tab) dan membaca tooltip fokus, hover pada toggle.

## Test Steps

### TC-FA-FAAC-43

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Tekan Tab berulang hingga fokus keyboard mencapai toggle kolom Active baris HEAVY-EQ
3. Verifikasi tooltip "You don't have permission to edit." muncul saat toggle (Disabled) menerima keyboard focus
4. Pindahkan fokus keluar dari toggle dengan klik area kosong halaman

### TC-FA-FAAC-633

5. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
6. Arahkan kursor ke toggle Active baris B-ANCHOR
7. Verifikasi tooltip "You don't have permission to edit." tampil
8. Coba klik toggle Active baris B-ANCHOR
9. Verifikasi toggle Disabled dan tidak dapat diklik

### TC-FA-FAAC-612

10. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
11. Klik Class Code HEAVY-EQ untuk membuka Detail Asset Class Heavy Equipment
12. Klik tab Asset Names
13. Verifikasi tab Asset Names, Search, Filter, dan tabel dapat dilihat
14. Verifikasi link Asset Name pada baris tampil dan Enabled (dapat diklik)
15. Verifikasi tombol '+ Assign Asset Names', kolom checkbox, dan Bulk Action Bar: Hidden
16. Verifikasi row action 'Move' dan 'Unassign' Hidden (tombol ⋯ pada baris Crane Rental Unit tidak tampil)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a): satu role (Read Only) untuk tiga topik hak ubah yang ditolak secara UI (tooltip toggle Active lewat keyboard focus dan hover, kontrol tulis tab Asset Names); seluruhnya satu akun sehingga tidak ada langkah ganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (memindahkan fokus agar tooltip fokus tidak terbawa ke TC berikutnya, S-09), langkah 1 dan 10 (Search `HEAVY-EQ` untuk menemukan baris target karena tidak dijamin berada di halaman 1; R-16). Langkah 5 (Search `B-ANCHOR`) berasal dari TC-FA-FAAC-633 dan memakai "ganti isi" karena kotak Search masih berisi.
- TC-FA-FAAC-43 (aksesibilitas tooltip) ada di spec ini karena topiknya hak ubah Read Only; TC-FA-FAAC-633 bergantung pada Asset Class B-ANCHOR (dependensi TC-FA-FAAC-87) yang di-seed lewat API, tidak dibuat lewat UI (S-04).
- Asersi Hidden pada TC-FA-FAAC-612 didahului `Verifikasi` tab Asset Names, Search, Filter, dan tabel tampil sebagai anchor positif permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-612 menyebut "link Asset Name tetap berfungsi" tanpa Expected tujuan navigasi; spec mengasersi link tampil dan Enabled.
  - TC-FA-FAAC-612 langkah 3 menyebut menu baris pada Crane Rental Unit sedangkan Expected c menyebut tombol ⋯ baris tidak tampil; spec mengasersi tombol ⋯ tidak tampil.
