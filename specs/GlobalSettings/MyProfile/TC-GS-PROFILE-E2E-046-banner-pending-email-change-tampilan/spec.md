---
id: TC-GS-PROFILE-E2E-046-banner-pending-email-change-tampilan
title: "Pending Email Change: Badge Header, Banner, Teks Bantu Email, Refresh, dan Email Tidak Berubah"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-24
  - TC-GS-PROFILE-205
  - TC-GS-PROFILE-206
  - TC-GS-PROFILE-207
  - TC-GS-PROFILE-211
  - TC-GS-PROFILE-216
coverage:
  web: automated
---

# Pending Email Change: Badge Header, Banner, Teks Bantu Email, Refresh, dan Email Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Akun aktor pertama spec: Pre-setup #8 (Citra Lestari, Activated, Email `citralestari@qwertysystem.net`) `pendingEmailProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_PENDING_PASSWORD`.
- Env var: `GS_PROFILE_PENDING_PASSWORD`.
- Data Dinamis #2: permintaan Email change live dari Citra Lestari ke `citra.baru@qwertysystem.net`, dibuat lewat fixture BE di hook `before` (dibuat segar, umur kurang dari 24 jam). Fixture dibuat dan dipulihkan oleh tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD (lihat Temuan untuk QA).
- Pemulihan (R-08): hook `after` membatalkan permintaan Email change yang dibuat spec dan memastikan Email Citra Lestari tetap `citralestari@qwertysystem.net`.
- Kemampuan teknis: hover elemen; muat ulang halaman; navigasi antar halaman lewat account menu navbar.
- State global yang diubah: tidak ada selain permintaan Email change di atas. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-24: Badge Pending Email Confirmation di Header

1. Verifikasi badge `Active` tampil di bawah Full Name pada Header
2. Verifikasi badge Activation `Pending Email Confirmation` tampil di bawah Full Name pada Header

### TC-GS-PROFILE-205: Banner tampil di bawah Header dan di atas Section Identity

3. Verifikasi banner tampil dengan teks `Pending email change to citra.baru@qwertysystem.net`
4. Verifikasi banner berada tepat di bawah Header dan di atas Section Identity

### TC-GS-PROFILE-206: Banner read-only

5. Hover banner
6. Verifikasi banner tidak memiliki tombol `[Resend]`, tombol `[Cancel]`, maupun tombol aksi lain

### TC-GS-PROFILE-207: Field Email dengan teks bantu

7. Verifikasi nilai field Email di Section Identity adalah `citralestari@qwertysystem.net`
8. Verifikasi teks bantu di bawah nilai Email adalah `Pending email change to citra.baru@qwertysystem.net`

### TC-GS-PROFILE-216: Email tidak berubah dari My Profile

9. Verifikasi nilai Email tetap `citralestari@qwertysystem.net`
10. Verifikasi tidak ada kontrol ubah Email di halaman

### TC-GS-PROFILE-211: Buka dan refresh menampilkan banner

11. Pindah dari My Profile ke halaman Global Settings
12. Buka My Profile dari account menu navbar
13. Verifikasi banner tampil setelah My Profile dibuka
14. Muat ulang halaman (F5)
15. Verifikasi banner tampil setelah muat ulang

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-PROFILE-211 berada paling akhir karena membuka ulang My Profile; screening TC-GS-PROFILE-24, 205, 206, 207, dan 216 memakai halaman yang dibuka hook `beforeEach`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 11 (precondition TC-GS-PROFILE-211: User berada di Global Settings).
- Temuan untuk QA:
  - Mekanisme fixture BE untuk membuat dan memulihkan permintaan Email change live tidak disebut TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13).
  - TC-GS-PROFILE-206 langkah 2 "Hover banner" tidak punya Expected (tidak ada tooltip yang diharapkan); spec menulis hover sebagai langkah tanpa `Verifikasi` tambahan.
  - TC-GS-PROFILE-211 menyebut precondition "User berada di Global Settings" tanpa cara berpindah dari My Profile; spec menambah langkah penghubung 11.
