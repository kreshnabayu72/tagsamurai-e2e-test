---
id: TC-GS-PROFILE-E2E-015-gate-akses-sesi-dan-pemilik-record
title: "Gate akses My Profile: tanpa sesi, sesi habis, dan hanya record sendiri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-71
  - TC-GS-PROFILE-72
  - TC-GS-PROFILE-306
  - TC-GS-PROFILE-114
coverage:
  web: automated
---

# Gate akses My Profile: tanpa sesi, sesi habis, dan hanya record sendiri

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan = urutan blok):

| Blok | Pre-setup | Akun | Kondisi data | Env var password |
|---|---|---|---|---|
| 1 | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | TC-GS-PROFILE-72, 306, 71 | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| 2 | #7 | Maya Anggraini, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`, counter Change Password 0, counter Login 0, Time Format 24 jam, timezone Asia/Jakarta; TC-GS-PROFILE-114 | `Spectra.env.GS_PROFILE_PWD_PASSWORD` |

- Password baru `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3) diketik di New Password dan Confirm New Password pada langkah 15; nilai itu tidak pernah tersimpan karena sesi server dihapus sebelum [Save].
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya (Pre-setup #1) di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6. Spec ini tidak menguji counter.
- Kemampuan teknis (disediakan tim FE/BE): (a) menghapus cookie sesi browser (langkah 6); (b) fixture BE yang menghapus sesi login akun di server sementara tab browser tetap terbuka (langkah 3 dan 16), karena TC menyebut "sesi dihapus lewat fixture BE" tanpa mekanismenya.
- State yang diubah: sesi login akun Pre-setup #1 dan #7 dihapus di server. Akun login ulang pada langkah 9 dan 12; hook `after` mengembalikan sesi ke akun default. Password Pre-setup #7 tidak berubah (modal tidak berhasil disimpan).
- Data Dinamis: tidak ada.

## Test Steps

### Hanya record sendiri (TC-GS-PROFILE-72)

1. Verifikasi Header, Section Identity, Section Access & Status, dan Section Custom Field milik Andi Pratama tampil
2. Verifikasi tidak ada kontrol pemilihan user lain

### Sesi habis saat membuka My Profile (TC-GS-PROFILE-306)

3. Hapus sesi login Pre-setup #1 di server lewat fixture BE
4. Muat ulang data halaman My Profile pada tab yang sudah terbuka
5. Verifikasi pengguna diarahkan ke halaman Login

### Tanpa sesi aktif (TC-GS-PROFILE-71)

6. Hapus cookie sesi browser
7. Buka URL halaman My Profile langsung di address bar
8. Verifikasi pengguna diarahkan ke halaman Login
9. Login dengan akun Pre-setup #1 dengan `Spectra.env.GS_PROFILE_TC_PASSWORD`
10. Verifikasi setelah login berhasil pengguna diarahkan ke My Profile (intent tersimpan)

### Ganti akun ke Pre-setup #7

11. Logout
12. Login sebagai Pre-setup #7 (Maya Anggraini) dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
13. Buka My Profile dari account menu navbar

### Sesi habis saat submit Change Password (TC-GS-PROFILE-114)

14. Klik [Change Password]
15. Isi Current Password dari `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password dan Confirm New Password dari `Spectra.env.PROFILE_PASSWORD_NEW`
16. Hapus sesi login Pre-setup #7 di server lewat fixture BE sementara modal tetap terbuka
17. Klik [Save]
18. Verifikasi pengguna diarahkan ke halaman Login (bukan inline error Current Password salah)

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-71, 72, 306, 114).
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (langkah 11 sampai 13); blok 2 tetap bermakna walau blok 1 gagal.
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-PROFILE-72 (baca saja) di awal, lalu TC-GS-PROFILE-306 dan TC-GS-PROFILE-71 yang mengakhiri sesi, lalu TC-GS-PROFILE-114 pada akun lain.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 6 menghapus cookie sesi (precondition TC-GS-PROFILE-71 "Tidak ada sesi login aktif") dan membuka konteks tanpa sesi sehingga tidak memakai ulang sesi TC sebelumnya (R-05); langkah 11 sampai 13 adalah Step ganti akun dan pembuka halaman; langkah 16 menghapus sesi server sebagai precondition TC-GS-PROFILE-114 (tidak diasersi sebagai hasil).
- Langkah 2 (tidak ada kontrol pemilihan user lain) didahului `Verifikasi` elemen halaman tampil (langkah 1) sebagai anchor positif.
- Temuan untuk QA:
  - Post Condition TC-GS-PROFILE-114 ("Password akun tidak berubah") tidak punya langkah observasi di TC dan tidak diasersi di spec ini (S-01, R-18).
  - TC-GS-PROFILE-306 menulis langkah "Buka halaman My Profile pada tab yang sudah terbuka lalu muat ulang data" tanpa menyebut cara memuat ulang data (muat ulang browser atau tombol di halaman); spec memakai muat ulang data halaman.
  - TC-GS-PROFILE-71 memberi Precondition "cookie sesi dihapus" tanpa menyebut cara menghapus di environment automation; kemampuan hapus cookie ditulis sebagai kebutuhan teknis di Prerequisites.
