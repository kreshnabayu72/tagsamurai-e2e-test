---
id: TC-GS-NLU-E2E-017-create-trim-spasi-position-dan-employee-id-opsional-ukuran-foto
title: "Create: trim spasi, Position dan Employee ID opsional, ukuran foto, dan pembatalan perubahan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-68
  - TC-GS-NLU-77
  - TC-GS-NLU-88
  - TC-GS-NLU-89
  - TC-GS-NLU-91
coverage:
  web: automated
---

# Create: trim spasi, Position dan Employee ID opsional, ukuran foto, dan pembatalan perubahan

## Prerequisites

- Mode: FE+BE (backend nyata; foto dikompres dan record disimpan di backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By).
- Berkas di perangkat uji (disediakan tim FE): PNG 12 MB (TC-GS-NLU-88) dan JPG 5 MB (TC-GS-NLU-89).
- Data Dinamis, nilai field wajib lain milik spec: Division `Logistics`, Represented By `Ahmad Fauzi`.
  - TC-GS-NLU-77: First Name `Lia`, Last Name `Amelia {runId}-017`, Email `liaamelia+{runId}-017@qwertysystem.net`.
  - TC-GS-NLU-68: First Name `  Joko  ` (spasi tepi), Last Name `  Lestari {runId}-017  `, Employee ID `  NL-7001-{runId}-017  `, Email `  jokolestari+{runId}-017@qwertysystem.net  `.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-017` lewat API (mekanisme disediakan tim FE/BE).
- Kemampuan teknis: unggah berkas pada avatar.
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-88: Unggah foto lebih dari 10 MB ditolak dengan toast

1. Klik `[+ Non-Login User]`
2. Unggah berkas PNG 12 MB pada avatar
3. Verifikasi toast error `Error, failed to upload photo.`
4. Verifikasi foto tidak dipilih dan avatar tetap placeholder tanpa foto sebelumnya yang berubah

### TC-GS-NLU-89: Unggah foto 1 MB sampai 10 MB dikompres otomatis

5. Unggah berkas JPG 5 MB pada avatar
6. Verifikasi tidak ada pesan error
7. Verifikasi foto tampil sebagai avatar bulat
8. Klik `✕`
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`

### TC-GS-NLU-77: Position dan Employee ID boleh dikosongkan

11. Klik `[+ Non-Login User]`
12. Biarkan Position dan Employee ID kosong; isi First Name `Lia`, Last Name `Amelia {runId}-017`, Email `liaamelia+{runId}-017@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
13. Klik `[Submit]`
14. Verifikasi tersimpan sukses tanpa pesan error
15. Ketik Search `Lia Amelia {runId}-017`, tekan Enter
16. Verifikasi sel Position baris tersebut menampilkan `—`
17. Verifikasi sel Employee ID baris tersebut menampilkan `—`

### TC-GS-NLU-68: Spasi awal dan akhir di-trim saat Submit

18. Klik `[+ Non-Login User]`
19. Isi First Name `  Joko  `, Last Name `  Lestari {runId}-017  `, Employee ID `  NL-7001-{runId}-017  `, Email `  jokolestari+{runId}-017@qwertysystem.net  `
20. Pastikan Division dan Represented By terisi: pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
21. Klik `[Submit]`
22. Verifikasi tersimpan sukses
23. Ganti isi kotak search dengan `Joko Lestari {runId}-017`, tekan Enter
24. Buka Detail record `Joko Lestari {runId}-017`
25. Verifikasi Detail menampilkan Name `Joko Lestari {runId}-017` tanpa spasi tepi
26. Verifikasi Detail menampilkan Employee ID `NL-7001-{runId}-017` tanpa spasi tepi
27. Verifikasi Detail menampilkan Email `jokolestari+{runId}-017@qwertysystem.net` tanpa spasi tepi
28. Kembali ke User List sub-tab Non-Login User

### TC-GS-NLU-91: Mengubah field lalu mengembalikannya ke nilai awal dianggap belum diubah

29. Klik `[+ Non-Login User]`
30. Ubah First Name menjadi `Uji`, lalu kembalikan persis ke nilai awal (kosong)
31. Klik `✕`
32. Verifikasi Popup Create tertutup
33. Verifikasi dialog `Unsaved Changes` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan mengubah urutan TC: penolakan unggah (TC-GS-NLU-88) dan batas ukuran (TC-GS-NLU-89) mendahului aksi sukses (TC-GS-NLU-77, TC-GS-NLU-68), dan TC-GS-NLU-91 (menutup popup tanpa perubahan) terakhir (S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 sampai 10 (menutup form dirty berfoto secara deterministik; S-08), langkah 15 dan 23 (Search untuk menemukan baris target; R-16), langkah 28 (kembali ke daftar), langkah 30 (nilai `Uji` dipilih spec karena TC hanya menulis "Ubah First Name").
- Langkah 4 menggabungkan dua klausa Expected b TC-GS-NLU-88 ("foto tidak dipilih" dan "foto sebelumnya tidak berubah") karena popup baru tidak punya foto sebelumnya sehingga keduanya terlihat sebagai avatar placeholder tanpa perubahan.
- Langkah 32 dan 33 memetakan dua klausa Expected a TC-GS-NLU-91 ("langsung tertutup" dan "tanpa dialog").
- Temuan untuk QA:
  - TC-GS-NLU-88 menulis "foto sebelumnya (bila ada) tidak berubah" tetapi Popup Create tidak punya foto sebelumnya; spec hanya mengasersi avatar tetap placeholder.
  - TC-GS-NLU-89 Expected hanya menyebut "tidak ada pesan error"; spec mengasersi tidak ada pesan error sebelum foto tampil (langkah 6) tanpa menyebut toast tertentu.
  - TC-GS-NLU-77 Expected a ("tersimpan sukses tanpa pesan error") tidak menyebut teks toast; spec tidak mengasersi teks toast.
  - TC-GS-NLU-68 mencantumkan Email dengan spasi tepi `  jokolestari@qwertysystem.net  `; spec menambah suffix `+{runId}-017` pada Email, `{runId}-017` pada Last Name, dan Employee ID `NL-7001-{runId}-017` karena nilai unik (S-12).
  - TC-GS-NLU-77 dan TC-GS-NLU-68 tidak menyebut cara menemukan baris yang baru dibuat; spec mencari lewat Name bersuffix di langkah 15 dan 23 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
