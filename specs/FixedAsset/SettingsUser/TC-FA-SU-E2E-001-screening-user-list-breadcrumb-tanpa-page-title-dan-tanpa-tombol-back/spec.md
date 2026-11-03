---
id: TC-FA-SU-E2E-001-screening-user-list-breadcrumb-tanpa-page-title-dan-tanpa-tombol-back
title: "Screening User List: Breadcrumb, Tanpa Page Title, dan Tanpa Tombol Back"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1
  - TC-FA-SU-2
  - TC-FA-SU-3
coverage:
  web: automated
---

# Screening User List: Breadcrumb, Tanpa Page Title, dan Tanpa Tombol Back

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan pohon grup (#21). Nilai nama pengguna dan grup dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: pembacaan urutan baris dan isi tiap halaman pagination User List.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1: Screening halaman User List saat pertama dibuka

1. Verifikasi Breadcrumb `Settings > User` tanpa nama produk dan tanpa Page Title
2. Verifikasi tombol `[?]` tampil di kanan Breadcrumb
3. Verifikasi Table Tools `Search`, `Filter`, `Download`, dan `Changelog` tampil
4. Verifikasi Table Tools tidak memuat tombol create
5. Verifikasi kolom tabel `Checkbox`, `Active` (sortable), `Name` (sortable), `Email` (sortable), `Role` (sortable), `Home Group` (sortable), `Position` (sortable), `Division` (sortable), `Employee ID` (sortable), `Modified By` (sortable), `Last Updated` (sortable), dan `Column Visibility (⋯)` (unsortable, header klik membuka overlay Column Visibility, body per baris berupa menu row action)
6. Verifikasi baris halaman 1 urut Name A-Z: Ahmad Dahlan, Budi Santoso, Citra Lestari, Doni Prasetyo, Eka Wulandari, Fajar Nugroho, Gita Permata, Hana Kusuma, Indra Wijaya, Kartika Sari
7. Verifikasi pagination default 10 data per halaman
8. Klik halaman 2 pada pagination
9. Verifikasi halaman 2 berisi Lina Marlina, Lukman Hakim, Mira Anggraini, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Qori Akbar, Rina Susanti, Rudi Hartono, Sinta Dewi
10. Klik halaman 3 pada pagination
11. Verifikasi halaman 3 berisi Teguh Prakoso, Umar Faruq, Vina Maharani, Wawan Setiawan, Yuda Pratama
12. Klik halaman 1 pada pagination
13. Verifikasi Sidebar Group Tree tampil di kanan dengan node `All Groups` aktif

### TC-FA-SU-2: Breadcrumb User List: teks path dan state tiap segmen

14. Verifikasi Breadcrumb tampil `Settings > User` (dua segmen, tanpa nama produk di depannya)
15. Hover segmen `Settings`
16. Klik segmen `Settings`
17. Verifikasi halaman tidak berpindah dan segmen `Settings` berupa label statis
18. Hover segmen `User`
19. Klik segmen `User`
20. Verifikasi halaman tidak berpindah dan segmen `User` berupa label statis
21. Verifikasi tidak ada segmen Breadcrumb yang dapat diklik karena Breadcrumb kurang dari tiga segmen

### TC-FA-SU-3: Halaman User List tanpa Page Title terpisah dan tanpa tombol Back to

22. Verifikasi Breadcrumb dan Table Tools tampil (anchor permukaan untuk asersi absence berikutnya)
23. Verifikasi tidak ada elemen Page Title (heading `User`) di bawah Breadcrumb
24. Verifikasi tidak ada tombol atau link `← Back to`
25. Verifikasi konten utama (SectionCard tabel) langsung dimulai di bawah Breadcrumb
26. Verifikasi Sidebar Group Tree berada di SectionCard terpisah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1 TC-FA-SU-1 ("Klik sidebar Fixed Asset > Settings > User") dipenuhi hook `beforeEach` suite yang membuka halaman; spec tidak mengulangnya (bagian 4 konvensi).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 10, dan 12 (pindah halaman pagination supaya isi halaman 2 dan 3 dapat diamati, S-14; kembali ke halaman 1). Langkah 22 adalah baris anchor permukaan untuk asersi absence langkah 23 dan 24 (bagian 8b butir 2); bukan Expected TC (S-03).
- Rujukan nomor langkah di spec ini: tidak ada.
- Temuan untuk QA:
  - TC-FA-SU-1 Expected b.ii dan c menyebut isi halaman 1, 2, dan 3 tetapi Langkah Uji TC hanya "Amati halaman dari atas ke bawah"; spec menambah klik pagination sebagai langkah penghubung.
  - TC-FA-SU-1 Expected a.i menulis "tanpa Page Title" dan TC-FA-SU-3 mengujinya lagi dari sisi lain; tumpang tindih antar TC, spec mengikuti keduanya.
