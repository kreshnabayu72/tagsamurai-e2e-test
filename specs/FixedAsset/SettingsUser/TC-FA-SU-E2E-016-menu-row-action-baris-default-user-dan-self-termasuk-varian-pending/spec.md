---
id: TC-FA-SU-E2E-016-menu-row-action-baris-default-user-dan-self-termasuk-varian-pending
title: "Menu Row Action Baris Default User dan Self Termasuk Varian Pending"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-15
coverage:
  web: automated
---

# Menu Row Action Baris Default User dan Self Termasuk Varian Pending

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup yang diubah: Ahmad Dahlan (Default User) dan Lina Marlina (Self) pada Client `FaUserMain` (#20, #38) dibentuk per varian lewat seed API pada langkah 1, 7, dan 20, lalu dipulihkan lewat seed API di hook `after` (Last Updated kedua pengguna berubah selama spec; dipulihkan oleh seed). Pengubahan Pre-setup dipakai karena Default User dan Self hanya satu per Client sehingga tidak dapat dimiliki spec (S-06). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Varian Data Uji (dibentuk lewat seed API, kemampuan disediakan tim BE/FE):
  - Varian A: Default User Pending Activation (Self tidak diuji pada varian ini karena aktor sudah login dan teraktivasi).
  - Varian B: Default User dan Self dalam keadaan ubah email (Pending Email Confirmation).
  - Varian C: Default User dan Self Activated.
- State global: status aktivasi dan email pending Ahmad Dahlan dan Lina Marlina; dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-15: Menu row action baris Default User dan Self (termasuk varian Pending)

1. Bentuk varian A (Default User Pending Activation) lewat seed API hingga tersimpan, lalu muat ulang User List
2. Klik `⋯` pada baris Ahmad Dahlan (Default User)
3. Verifikasi sakelar dan checkbox baris Ahmad Dahlan Disabled
4. Verifikasi menu memuat `Detail` dan `Resend Activation Email`
5. Verifikasi `Edit Home Group` Hidden pada menu
6. Tutup menu dengan Esc
7. Bentuk varian B (Default User dan Self ubah email) lewat seed API hingga tersimpan, lalu muat ulang User List
8. Klik `⋯` pada baris Ahmad Dahlan (Default User)
9. Verifikasi sakelar dan checkbox baris Ahmad Dahlan Disabled
10. Verifikasi menu memuat `Detail` dan `Resend Confirmation Email`
11. Verifikasi `Edit Home Group` Hidden pada menu
12. Tutup menu dengan Esc
13. Klik halaman 2 pada pagination
14. Klik `⋯` pada baris Lina Marlina (Self)
15. Verifikasi sakelar dan checkbox baris Lina Marlina Disabled
16. Verifikasi menu memuat `Detail` dan `Resend Confirmation Email`
17. Verifikasi `Edit Home Group` Hidden pada menu
18. Verifikasi `Resend Confirmation Email` tetap tampil pada Default User dan Self karena Resend tidak punya kunci target
19. Tutup menu dengan Esc
20. Bentuk varian C (Default User dan Self Activated) lewat seed API hingga tersimpan, lalu muat ulang User List
21. Klik `⋯` pada baris Ahmad Dahlan (Default User)
22. Verifikasi sakelar dan checkbox baris Ahmad Dahlan Disabled
23. Verifikasi menu memuat `Detail`
24. Verifikasi `Edit Home Group` Hidden pada menu
25. Tutup menu dengan Esc
26. Klik halaman 2 pada pagination
27. Klik `⋯` pada baris Lina Marlina (Self)
28. Verifikasi sakelar dan checkbox baris Lina Marlina Disabled
29. Verifikasi menu memuat `Detail`
30. Verifikasi `Edit Home Group` Hidden pada menu
31. Tutup menu dengan Esc
32. Klik halaman 1 pada pagination

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, dan 20 (membentuk varian lewat seed API dan memuat ulang), langkah 6, 12, 19, 25, dan 31 (menutup menu, S-09), langkah 13, 26, dan 32 (pindah halaman pagination: Ahmad Dahlan di halaman 1 dan Lina Marlina di halaman 2, S-14). Urutan varian di spec (A, B, C) mengikuti Data Uji TC; baris Self dan Default User diurut per halaman supaya klik halaman minimal.
- Menu "memuat" berarti tepat opsi yang disebut Expected TC (tidak ada opsi lain di luar daftar).
- Langkah 7 dan 20 menggeser Self (Lina Marlina) ke keadaan ubah email lalu Activated; aktor tetap login dan keadaan aktor dipulihkan seed di hook `after`.
- Temuan untuk QA:
  - TC-FA-SU-15 Langkah Uji 2 ("di tiap varian") mencakup Self pada varian Pending Activation, tetapi aktor yang sedang login tidak dapat berada pada keadaan Pending Activation; Expected b tidak menyebut varian Pending Activation untuk Self. Spec tidak menguji Self pada varian A.
  - TC-FA-SU-15 tidak menyebut cara membentuk ketiga varian pada Default User dan Self; spec menuliskannya sebagai kemampuan seed API "disediakan tim BE/FE" (S-13).
  - Pre-setup #1 (Lina Marlina) adalah akun aktor dan juga baris Self pada TC ini; pengubahan keadaan akun yang sedang login lewat seed dapat memengaruhi sesi, sehingga pelaksana skrip perlu memastikan seed tidak menutup sesi aktor.
