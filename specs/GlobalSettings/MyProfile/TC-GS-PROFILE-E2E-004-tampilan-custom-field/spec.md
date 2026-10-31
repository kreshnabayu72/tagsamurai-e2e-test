---
id: TC-GS-PROFILE-E2E-004-tampilan-custom-field
title: "Section Custom Field: urutan, format Phone, collapse, nilai kosong, dan alert Required"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-17
  - TC-GS-PROFILE-18
  - TC-GS-PROFILE-19
  - TC-GS-PROFILE-20
coverage:
  web: automated
---

# Section Custom Field: urutan, format Phone, collapse, nilai kosong, dan alert Required

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #1 Andi Pratama (`totalControlProfile_automated_{namaCompany}@qwertysystem.net`), Total Control; password `Spectra.env.GS_PROFILE_TC_PASSWORD`.
- Pelaku kedua: Pre-setup #6 Hendra Wijaya (`adminActor_automated_{namaCompany}@qwertysystem.net`), Total Control; password `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`; hanya dipakai lewat sesi API pada langkah 15.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Data Pre-setup #16 (tetap di environment): Custom Field User aktif berurutan Hobby (Text, tidak Required, nilai untuk Pre-setup #1 `Reading`), Emergency Contact (Phone, nilai `+62 81234567890`), dan Passport Number (Text, Required, kosong); Custom Field nonaktif Shoe Size.
- State yang diubah spec: nilai Hobby milik Pre-setup #1 dikosongkan pada langkah 15 (precondition TC-GS-PROFILE-19). Pemulihan ke `Reading` lewat sesi API admin Pre-setup #6 dilakukan di hook `after` spec ini (tidak berasumsi langkah 15 berhasil) dan oleh hook `after` fixture Pre-setup bila disediakan tim FE/BE.

## Test Steps

### Section Custom Field: nilai read-only dan format Phone (TC-GS-PROFILE-17)

1. Verifikasi isi Section Custom Field tersembunyi (collapsed secara default)
2. Klik header Section Custom Field untuk membuka Section
3. Verifikasi urutan field: Hobby, Emergency Contact, Passport Number
4. Verifikasi nilai Hobby `Reading`
5. Verifikasi nilai Emergency Contact `+62 81234567890`
6. Hover nilai tiap field (Hobby, Emergency Contact, Passport Number) satu per satu
7. Verifikasi tidak ada ikon edit saat hover dan tidak ada tombol Save/Cancel inline

### Collapse dan buka kembali (TC-GS-PROFILE-18)

8. Muat ulang halaman My Profile
9. Verifikasi isi Section Custom Field tersembunyi (collapsed secara default)
10. Klik header Section Custom Field
11. Verifikasi isi Section Custom Field tampil
12. Klik header Section Custom Field lagi
13. Verifikasi isi Section Custom Field tersembunyi kembali

### Nilai kosong tidak wajib dan alert Required (TC-GS-PROFILE-19, TC-GS-PROFILE-20)

14. Tunggu aksi selesai
15. Admin Pre-setup #6 mengosongkan nilai Hobby milik Pre-setup #1 lewat sesi API hingga perubahan tersimpan
16. Muat ulang halaman My Profile
17. Klik header Section Custom Field untuk membuka Section
18. Verifikasi nilai Hobby `—`
19. Verifikasi nilai Passport Number diganti alert `⚠ "Passport Number is required."` (menggantikan `—`)
20. Hover field Passport Number
21. Verifikasi tidak ada ikon edit saat hover pada field Passport Number

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-17, 18, 19, 20).
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-PROFILE-17 dan 18 memakai Hobby `Reading`, lalu nilai Hobby dikosongkan untuk TC-GS-PROFILE-19 dan 20 yang memakai kondisi Hobby kosong.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 6, 10, 12, dan 17 adalah aksi uji TC; langkah 8 dan 16 memuat ulang halaman supaya Section kembali ke keadaan collapsed default (TC-GS-PROFILE-18 mensyaratkan "saat halaman dibuka"); langkah 14 menunggu aksi selesai karena langkah 15 memicu pelaku kedua lewat sesi API.
- Temuan untuk QA:
  - TC-GS-PROFILE-19 menyebut Hobby kosong (Pre-setup #16) tetapi Pre-setup #16 menetapkan nilai Hobby `Reading` untuk Pre-setup #1 dan tidak menyebut akun lain; spec memakai akun Pre-setup #1 dengan nilai Hobby dikosongkan lewat sesi API admin dan dipulihkan. Akun dengan Hobby kosong perlu ditetapkan QA.
  - TC-GS-PROFILE-20 tidak menyebut akun; spec memakai Pre-setup #1 (Passport Number Required kosong sesuai Pre-setup #16).
