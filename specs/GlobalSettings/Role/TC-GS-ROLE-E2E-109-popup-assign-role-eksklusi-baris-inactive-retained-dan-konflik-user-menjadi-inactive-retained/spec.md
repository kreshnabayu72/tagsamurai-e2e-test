---
id: TC-GS-ROLE-E2E-109-popup-assign-role-eksklusi-baris-inactive-retained-dan-konflik-user-menjadi-inactive-retained
title: "Popup Assign Role: Eksklusi User dengan Baris Inactive-Retained dan Konflik User yang Menjadi Inactive-Retained Sejak Render"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-321
  - TC-GS-ROLE-322
coverage:
  web: automated
---

# Popup Assign Role: Eksklusi User dengan Baris Inactive-Retained dan Konflik User yang Menjadi Inactive-Retained Sejak Render

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah baris role user Pre-setup bersama.
- Akun Sesi A (UI): Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Akun Sesi B (pemicu): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, kredensial `Spectra.env.GS_TC2_PASSWORD` (terdaftar). Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B; cara memperoleh token disediakan tim FE.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang pada semua user): `Laras Wulandari` (Active; baris `Manage hardware` inactive-retained dengan Create, Read, Update tersimpan) untuk TC-321 dan `Rani Oktaviani` (Active; tanpa baris role) untuk TC-321 dan TC-322. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan baris inactive-retained disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Kemampuan teknis: satu konteks browser untuk Sesi A; Sesi B lewat sesi API; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): `Laras Wulandari` dikembalikan ke baris `Manage hardware` inactive-retained (Create, Read, Update) dan `Rani Oktaviani` dikembalikan tanpa baris role. Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-321: Popup Assign Role tidak menampilkan user dengan baris inactive-retained

1. [Sesi A] Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage hardware`
2. [Sesi A] Ketik Search `Laras Wulandari`, tekan Enter
3. [Sesi A] Verifikasi empty state `No results found` tampil pada hasil Search
4. [Sesi A] Verifikasi `Laras Wulandari` tidak tampil di Detail `Manage hardware`
5. [Sesi A] Klik `(←)` pada kotak Search
6. [Sesi A] Klik `[+ Assign]`
7. [Sesi A] Ketik Search `Laras`, tekan Enter
8. [Sesi A] Verifikasi empty state `No results found` tampil pada hasil Search popup
9. [Sesi A] Verifikasi `Laras Wulandari` tidak tampil di popup
10. [Sesi A] Ganti isi kotak search dengan `Rani`, tekan Enter
11. [Sesi A] Verifikasi `Rani Oktaviani` tampil di popup
12. [Sesi A] Centang `Rani Oktaviani`
13. [Sesi A] Verifikasi checkbox `Rani Oktaviani` tercentang
14. [Sesi A] Hapus centang `Rani Oktaviani`, tutup popup Assign dengan `✕`

### TC-GS-ROLE-322: Assign Role saat user terpilih menjadi inactive-retained sejak render ditolak

15. [Sesi A] Klik `[+ Assign]` pada Detail `Manage hardware`
16. [Sesi A] Ketik Search `Rani Oktaviani`, tekan Enter
17. [Sesi A] Centang `Rani Oktaviani` (belum klik `[Assign]`)
18. [Sesi B] Nyalakan lalu matikan switch `Manage hardware` milik `Rani Oktaviani` lewat sesi API hingga perubahan tersimpan
19. [Sesi A] Klik `[Assign]`
20. [Sesi A] Verifikasi alert inline `Rani Oktaviani is no longer eligible. Please select another.`
21. [Sesi A] Verifikasi centangan `Rani Oktaviani` hilang
22. [Sesi A] Verifikasi daftar picker di-refetch tanpa `Rani Oktaviani`
23. [Sesi A] Tutup popup Assign dengan `✕`
24. [Sesi A] Ketik Search `Rani Oktaviani` di Detail `Manage hardware`, tekan Enter
25. [Sesi A] Verifikasi empty state `No results found` tampil pada hasil Search
26. [Sesi A] Verifikasi `Rani Oktaviani` tidak tampil di Detail `Manage hardware`
27. [Sesi A] Klik `(←)` pada kotak Search
28. [Sesi A] Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Rani Oktaviani`, tekan Enter
29. [Sesi A] Klik Name `Rani Oktaviani`, buka Tab `Role`
30. [Sesi A] Verifikasi switch `Manage hardware` OFF (inactive-retained)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional untuk TC-321; TC-322 memakai pelaku kedua lewat sesi API sebagai pemicu sesuai keputusan 2026-10-30 pada `P-2` (pelaku kedua lewat sesi API bukan konteks kedua), sehingga tidak ada butir `P-2`. Subjudul `###` memetakan langkah ke id TC granular.
- Tabel Pre-setup/Dinamis TC menyebut `Rani Oktaviani` sebagai pemicu switch OFF yang diamati; sesudah TC-322 `Rani Oktaviani` tidak punya baris di Detail `Manage hardware` dan switch `Manage hardware` OFF (inactive-retained).
- Search untuk menemukan baris atau user target ditulis sebagai langkah penghubung (R-16): langkah 2, 7, 10, 16, 24, 28. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Detail, popup, dan Tab `Role` (langkah 1, 5, 6, 15, 27, 29), menghapus centang dan menutup popup (langkah 14 dan 23).
- Absence `Laras Wulandari` di Detail (langkah 4) dan popup (langkah 9), serta `Rani Oktaviani` di Detail (langkah 26), didahului empty state hasil Search sebagai anchor positif pada surface yang sama (langkah 3, 8, dan 25; bagian 8b butir 2); empty state dan absence ditulis sebagai `Verifikasi` terpisah per klausa (S-01). Absence picker pada langkah 22 terhubung ke pemicu `[Assign]` (langkah 19): alert inline (langkah 20) adalah respons server atas `[Assign]` yang sama dan centangan hilang (langkah 21) adalah hasil render popup yang sama sesudah refetch, sehingga keduanya membuktikan popup sudah memuat ulang sebelum absence langkah 22 diasersi; langkah 11 berada di popup TC-GS-ROLE-321 yang sudah ditutup (langkah 14) sehingga bukan pembanding untuk langkah 22.
- Expected c TC-322 menyebut "Sesi B: switch tetap OFF". Sesi B hanya sesi API tanpa tampilan; keadaan switch dibaca pada Tab `Role` `Rani Oktaviani` lewat Sesi A (langkah 30), data yang sama.
- Temuan untuk QA:
  - Mekanisme menyiapkan baris inactive-retained `Laras Wulandari` dan pelaku kedua Sesi B tidak didefinisikan di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-ROLE-321 tidak menyebut cara menutup popup sesudah centang `Rani Oktaviani`; spec menghapus centang lalu menutup dengan `✕` sebagai langkah penghubung (apakah dialog `Unsaved Changes` muncul tidak disebut).
  - TC-GS-ROLE-322 Expected c menyebut Sesi B sebagai surface asersi padahal pelaku kedua hanya memicu perubahan; spec membaca state yang sama dari Sesi A.
  - TC-GS-ROLE-322 bertanda `Manual Only (d)` karena dua sesi paralel; spec tetap memuatnya (hambatan teknis bukan alasan mengeluarkan TC).
