---
id: TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard
title: "Interaksi Baris User List: Klik Area Non-Name, Hover Name, Warna Toggle, Overlay Row Action, Fokus Keyboard, dan Navigasi ke User Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-11
  - TC-GS-USER-12
  - TC-GS-USER-13
  - TC-GS-USER-24
  - TC-GS-USER-26
  - TC-GS-USER-27
  - TC-GS-USER-28
  - TC-GS-USER-40
coverage:
  web: automated
---

# Interaksi Baris User List: Klik Area Non-Name, Hover Name, Warna Toggle, Overlay Row Action, Fokus Keyboard, dan Navigasi ke User Detail

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Dewi Lestari (No. 12, Activated, Active ON), Jane Smith (No. 17, Inactive manual), Mike Tan (No. 14, Pending Activation), Rina Putri (No. 15, Activated dengan email pending), Hendra Gunawan (No. 1, Default User).
- Kemampuan teknis: hover elemen; tekan tombol Tab pada keyboard; membaca warna teks dan warna switch dari elemen; membaca jumlah tab browser untuk memastikan navigasi terjadi di tab yang sama.
- State global yang diubah: tidak ada.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-24: Toggle Active ON tampil warna primary Global Settings, OFF netral

3. Verifikasi switch Active baris Dewi Lestari berstate ON dengan warna primary Global Settings (hitam)
4. Verifikasi switch Active baris Jane Smith berstate OFF dengan warna abu-abu netral

### TC-GS-USER-13: Hover Name mengubah warna ke primary Global Settings tanpa underline

5. Arahkan kursor ke teks Name `Dewi Lestari`
6. Verifikasi warna teks Name `Dewi Lestari` berubah ke warna primary Global Settings (hitam)
7. Verifikasi teks Name `Dewi Lestari` tanpa underline
8. Arahkan kursor keluar dari teks Name `Dewi Lestari`
9. Verifikasi warna teks Name `Dewi Lestari` kembali netral

### TC-GS-USER-11: Klik baris di area selain Name tidak melakukan aksi apa pun

10. Klik sel Email pada baris Dewi Lestari
11. Klik sel Division pada baris Dewi Lestari
12. Verifikasi tidak ada navigasi (halaman tetap `User > User List > Login User`)
13. Verifikasi tidak ada popup yang terbuka
14. Verifikasi baris Dewi Lestari tidak terseleksi (checkbox baris tidak tercentang)

### TC-GS-USER-40: Accessibility tooltip disabled dapat dibuka via keyboard focus

15. Tekan Tab berulang sampai fokus berada di switch Active baris Default User (Hendra Gunawan), dimulai dari sel Division baris Dewi Lestari yang diklik di langkah 11
16. Verifikasi tooltip `Default User cannot be modified.` tampil saat switch Active baris Default User mendapat fokus

### TC-GS-USER-26: Screening overlay Row Action untuk baris Normal User oleh Total Control

17. Klik (⋯) pada baris Mike Tan (Pending Activation)
18. Verifikasi overlay Mike Tan memuat opsi `Detail` | `Edit` | `Resend Activation Email` | `Delete` berurutan, `Delete` paling akhir
19. Verifikasi ikon dan warna opsi overlay Mike Tan: `Detail` (FileInfoLine, dark), `Edit` (Edit2Line, dark), `Resend Activation Email` (MailSendLine, dark), `Delete` (DeleteBin6Line, danger)
20. Tutup overlay Mike Tan dengan menekan Esc
21. Klik (⋯) pada baris Dewi Lestari
22. Verifikasi overlay Dewi Lestari memuat opsi `Detail` | `Edit` | `Delete`
23. Verifikasi overlay Dewi Lestari tanpa opsi `Resend Activation Email`
24. Tutup overlay Dewi Lestari dengan menekan Esc

### TC-GS-USER-27: Row action Resend Confirmation Email muncul untuk user Activated dengan email pending

25. Klik (⋯) pada baris Rina Putri
26. Verifikasi overlay Rina Putri memuat opsi `Detail` | `Edit` | `Resend Confirmation Email` | `Delete`
27. Verifikasi ikon dan warna opsi `Resend Confirmation Email` adalah MailSendLine, dark
28. Verifikasi opsi `Resend Activation Email` tidak tampil di overlay Rina Putri
29. Tutup overlay Rina Putri dengan menekan Esc

### TC-GS-USER-28: Row action Detail membuka User Detail

30. Klik (⋯) pada baris Dewi Lestari
31. Klik `Detail`
32. Verifikasi navigasi di tab yang sama ke `User > Detail` milik Dewi Lestari

### TC-GS-USER-12: Klik Name membuka User Detail target

33. Klik menu User di sidebar Global Settings
34. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
35. Klik teks Name `Dewi Lestari`
36. Verifikasi navigasi di tab yang sama ke `User > Detail` milik Dewi Lestari
37. Verifikasi Breadcrumb `User > Detail`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (37 langkah) karena delapan TC interaksi baris berada di satu kelas harness (fungsional, baca saja, tanpa aksi yang mengubah data); tiap blok TC berdiri sendiri dan memakai satu pembukaan layar dan satu tampilan 100 baris per halaman.
- Urutan TC sumber diubah: TC-GS-USER-24, TC-GS-USER-13, TC-GS-USER-11, dan TC-GS-USER-40 mendahului TC-GS-USER-26 dan TC-GS-USER-27 supaya titik awal fokus keyboard TC-GS-USER-40 (sel Division baris Dewi Lestari, di atas baris Hendra Gunawan) tetap dari klik langkah 11. TC-GS-USER-28 dan TC-GS-USER-12 berada paling akhir karena keduanya meninggalkan User List menuju User Detail; TC-GS-USER-12 memakai Search setelah kembali ke User List karena tampilan 100 baris per halaman belum tentu dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 (memilih 100 baris per halaman), 8 (menggeser kursor keluar dari Name, Expected TC-GS-USER-13 c), 20, 24, dan 29 (menutup overlay row action sebelum TC berikutnya), 33 dan 34 (kembali ke User List dan mencari Dewi Lestari).
- Langkah 3 dan 4 mengamati tampilan hasil langkah 1 dan 2.
- Temuan untuk QA:
  - TC-GS-USER-40 menyebut "Tekan Tab sampai fokus di switch Active baris Default User" tanpa titik awal fokus; spec memulai dari sel yang diklik di langkah 11 (titik awal fokus sekuensial browser).
  - TC-GS-USER-24 dan TC-GS-USER-13 menyebut warna "primary Global Settings (hitam)" tanpa nilai warna; nilai warna acuan ditentukan tim FE.
  - TC-GS-USER-11 Expected a menyebut "tidak ada seleksi baris"; spec memeriksa checkbox baris tidak tercentang.
  - TC-GS-USER-12 dan TC-GS-USER-28 tidak punya Expected tentang isi User Detail selain breadcrumb (TC-GS-USER-12 b) dan nama target; spec mengasersi navigasi ke Detail Dewi Lestari tanpa menambah asersi isi.
