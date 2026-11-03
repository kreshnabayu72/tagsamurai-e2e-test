---
id: TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor
title: "Role Matrix: Default User sebagai Aktor atas Target Bertier (Total Control, Read Only), Target Normal, dan Baris Sendiri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-60
  - TC-GS-USER-61
  - TC-GS-USER-62
  - TC-GS-USER-996
coverage:
  web: automated
---

# Role Matrix: Default User sebagai Aktor atas Target Bertier (Total Control, Read Only), Target Normal, dan Baris Sendiri

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). Flag disetel untuk akun Default User juga (mekanisme disediakan tim FE/BE).
- Role yang diuji (satu role):

| Role | Akun | Nama user | Env var password |
|---|---|---|---|
| Default User (tier Total Control, MFA Enrolled) | `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Hendra Gunawan (Tabel Pre-setup No. 1) | `Spectra.env.GS_DEFAULT_PASSWORD` |

- Login akun Default User (aktor pertama dan satu-satunya spec) dilakukan di hook `before`; tidak ada langkah ganti akun. Akun ini MFA Enrolled (Tabel Pre-setup No. 1); cara melewati MFA pada login hook disediakan tim FE/BE. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_DEFAULT_PASSWORD` (Default User Client A; bukan akun Default User client baru milik spec 004, yang memakai `GS_DEFAULT_NEW_PASSWORD`), `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Andi Wijaya (No. 10, tier Total Control), Doni Pratama (No. 11, tier Read Only), Dewi Lestari (No. 12, Normal), Hendra Gunawan (No. 1, Default User, akun yang login). Data Dinamis: tidak ada.
- Kemampuan teknis: hover elemen (checkbox, switch, opsi overlay) dan membaca tooltip; membaca state enabled atau disabled; menekan Esc.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).

## Test Steps

### Persiapan tabel

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-60: Default User dapat mengelola target bertier Total Control

2. Verifikasi checkbox dan switch Active baris Andi Wijaya enabled
3. Klik (⋯) pada baris Andi Wijaya
4. Verifikasi opsi `Edit` dan `Delete` enabled di overlay
5. Tutup overlay dengan menekan Esc

### TC-GS-USER-61: Default User dapat mengelola target bertier Read Only

6. Verifikasi checkbox dan switch Active baris Doni Pratama enabled
7. Klik (⋯) pada baris Doni Pratama
8. Verifikasi opsi `Edit` dan `Delete` enabled di overlay
9. Tutup overlay dengan menekan Esc

### TC-GS-USER-62: Default User terhadap target Normal: semua kontrol enabled

10. Verifikasi checkbox dan switch Active baris Dewi Lestari enabled
11. Klik (⋯) pada baris Dewi Lestari
12. Verifikasi opsi `Detail`, `Edit`, dan `Delete` enabled di overlay
13. Tutup overlay dengan menekan Esc

### TC-GS-USER-996: Default User melihat barisnya sendiri

14. Arahkan kursor ke checkbox baris Hendra Gunawan (akun sendiri)
15. Verifikasi checkbox baris Hendra Gunawan tampil namun disabled
16. Verifikasi tooltip `Default User cannot be modified.`
17. Arahkan kursor ke switch Active baris Hendra Gunawan
18. Verifikasi switch Active baris Hendra Gunawan tampil namun disabled
19. Verifikasi tooltip `Default User cannot be modified.`
20. Klik (⋯) pada baris Hendra Gunawan
21. Verifikasi opsi `Detail` dan `Edit` enabled di overlay
22. Arahkan kursor ke opsi `Delete`
23. Verifikasi opsi `Delete` tampil namun disabled
24. Verifikasi tooltip `Default User cannot be modified.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): satu role (Default User) atas tiga jenis target (bertier Total Control, bertier Read Only, Normal) dan baris sendiri; hasil enabled untuk target lain dan terlindungi untuk baris sendiri.
- Urutan TC sumber dipertahankan.
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (memilih 100 baris per halaman, supaya semua baris target tampil tanpa Search), serta langkah 5, 9, dan 13 (menutup overlay row action sebelum TC berikutnya).
- Langkah "Cari baris X" pada TC sumber dipenuhi dengan menemukan baris Name X di halaman 100 baris. Langkah "Amati checkbox, switch Active, overlay" dipecah menjadi satu `Verifikasi` untuk checkbox dan switch Active (daftar elemen berkeadaan sama) dan satu `Verifikasi` untuk opsi overlay.
- Temuan untuk QA:
  - TC-GS-USER-60, TC-GS-USER-61, dan TC-GS-USER-62 tidak menyebut cara Default User melewati MFA pada login; mekanisme disediakan tim FE/BE.
  - TC-GS-USER-996 langkah 2 berbunyi "Hover checkbox, switch Active; amati opsi `Edit`" tanpa Expected tentang tooltip `Edit`; spec mengasersi `Edit` enabled sesuai Expected c.
