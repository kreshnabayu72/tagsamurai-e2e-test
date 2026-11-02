---
id: TC-GS-PROFILE-E2E-008-aksesibilitas-keyboard-dan-aria
title: "Aksesibilitas: keyboard halaman, fokus modal Change Password, ARIA, dan show/hide via keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-42
  - TC-GS-PROFILE-43
  - TC-GS-PROFILE-313
  - TC-GS-PROFILE-318
coverage:
  web: automated
---

# Aksesibilitas: keyboard halaman, fokus modal Change Password, ARIA, dan show/hide via keyboard

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (urutan = urutan blok):

| Blok | Pre-setup | Akun | Kondisi data | Env var password |
|---|---|---|---|---|
| 1 | #1 | Andi Pratama, `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, Total Control, tanpa foto | App Access Global Settings dan Fixed Asset | `Spectra.env.GS_PROFILE_TC_PASSWORD` |
| 2 | #7 | Maya Anggraini, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, Total Control | password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`, counter Change Password 0, counter Login 0, Time Format 24 jam, timezone Asia/Jakarta | `Spectra.env.GS_PROFILE_PWD_PASSWORD` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6. Spec ini tidak menguji counter dan tidak mengubah password Pre-setup #7.
- Kemampuan teknis: menangani file picker native browser (membuka lalu menutupnya tanpa memilih file) pada langkah 12 dan 13, dan mengamati tooltip serta fokus keyboard.
- Data Dinamis: tidak ada. Nilai `Ab1!xyzw` diketik ke field Change Password pada blok 2 dan tidak pernah di-submit.

## Test Steps

### Keyboard halaman My Profile (TC-GS-PROFILE-42)

1. Tekan Tab sampai fokus di Product Selector, lalu tekan Enter
2. Verifikasi Product Selector terbuka
3. Pilih opsi dengan panah dan Enter
4. Verifikasi opsi terpilih tampil pada Product Selector (`Viewing: <opsi yang dipilih>`)
5. Tekan Tab sampai fokus di tombol [Change Password], lalu tekan Space
6. Verifikasi modal Change Password terbuka
7. Tutup modal dengan Esc
8. Tekan Tab sampai fokus di Avatar
9. Tekan Enter
10. Verifikasi overlay Avatar menampilkan [Edit]
11. Tekan Tab sampai fokus di [Edit] pada overlay, lalu tekan Enter
12. Verifikasi file picker terbuka
13. Tutup file picker tanpa memilih file

### Fokus modal Change Password (TC-GS-PROFILE-43)

14. Klik [Change Password]
15. Tekan Tab berulang sampai melewati elemen terakhir modal
16. Verifikasi fokus berputar di dalam modal dan tidak keluar ke halaman di belakang
17. Tekan Esc
18. Verifikasi modal tertutup tanpa dialog `Unsaved Changes`

### Ganti akun ke Pre-setup #7

19. Logout, lalu login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
20. Buka My Profile dari account menu navbar

### ARIA field Change Password (TC-GS-PROFILE-313)

21. Klik [Change Password]
22. Verifikasi Current Password, New Password, dan Confirm New Password beratribut aria-required bernilai true
23. Biarkan ketiga field kosong, lalu klik [Save]
24. Verifikasi tiap field memiliki aria-describedby yang menunjuk ke caption errornya masing-masing
25. Tutup modal dengan Esc

### Show/hide password lewat keyboard (TC-GS-PROFILE-318)

26. Klik [Change Password]
27. Untuk setiap baris tabel Field show/hide (langkah 27 sampai 35): klik field pada baris tabel lalu ketik `Ab1!xyzw`
28. Tekan Tab sampai fokus di ikon toggle field pada baris tabel
29. Verifikasi ikon toggle menerima keyboard focus
30. Verifikasi tooltip `Show password` tampil
31. Tekan Enter
32. Verifikasi field tampil sebagai teks `Ab1!xyzw`
33. Verifikasi tooltip berganti `Hide password`
34. Tekan Space
35. Verifikasi field tersamarkan kembali
36. Klik `✕` di header modal
37. Verifikasi dialog `Unsaved Changes` tampil
38. Klik [Leave]

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-42, 43, 313, 318).
- Tabel "Field show/hide" untuk langkah 27 sampai 35 (urutan baris = urutan TC-GS-PROFILE-318; urutan iterasi New Password, Current Password, Confirm New Password):

| Field show/hide |
|---|
| New Password |
| Current Password |
| Confirm New Password |

- Pengulangan: langkah 27 sampai 35 diulang untuk tiap baris tabel Field show/hide; parameter iterasi hanya field, tanpa langkah bersyarat, dan tiap `Verifikasi` tetap satu per klausa (S-01). TC-GS-PROFILE-318 menulis tiga siklus identik untuk ketiga field.
- Spec berisi 38 langkah nominal dan sekitar 56 langkah setelah ekspansi (langkah 27 sampai 35 dikali 3), di atas smell 35 langkah. Alasan: semua blok satu topik (aksesibilitas keyboard dan ARIA pada halaman My Profile), satu kelas harness, tanpa mengubah data; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (langkah 19). TC-GS-PROFILE-42 dan 43 tidak membutuhkan Pre-setup #7, sedangkan TC-GS-PROFILE-313 dan 318 membutuhkannya.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 7, 13, 25, dan 36 sampai 38 menutup modal atau file picker (langkah 36 sampai 38 mengikuti S-08: `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu [Leave]; karena form dirty, pemulihan memakai penutupan deterministik); langkah 19 dan 20 mengganti akun dan membuka My Profile.
- Langkah 23: ketiga field dibiarkan kosong, dan klik [Save] diblokir validasi V-01 sampai V-03 sebelum request, sehingga counter Change Password tidak berubah.
- Langkah 36 sampai 38 dijalankan sekali sesudah semua iterasi, pada form yang berisi ketiga field terisi.
- Temuan untuk QA:
  - TC-GS-PROFILE-42 menulis "opsi terpilih lewat keyboard" tanpa menyebut opsi yang dipilih; spec memverifikasi bahwa Product Selector menampilkan opsi yang dipilih.
  - TC-GS-PROFILE-318 tidak menyebut cara menutup modal sesudah ketiga field terisi; spec memakai `✕`, dialog `Unsaved Changes`, dan [Leave] sesuai S-08.
