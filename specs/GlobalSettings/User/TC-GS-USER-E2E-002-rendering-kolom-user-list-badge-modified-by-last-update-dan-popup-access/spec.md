---
id: TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access
title: "Rendering Kolom User List: Badge Name, Position Kosong, Modified By, Last Update, Access, dan Popup Access"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-14
  - TC-GS-USER-15
  - TC-GS-USER-16
  - TC-GS-USER-17
  - TC-GS-USER-18
  - TC-GS-USER-19
  - TC-GS-USER-20
  - TC-GS-USER-21
  - TC-GS-USER-22
coverage:
  web: automated
---

# Rendering Kolom User List: Badge Name, Position Kosong, Modified By, Last Update, Access, dan Popup Access

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data):
  - Mike Tan (No. 14): Pending Activation, avatar inisial.
  - John Doe (No. 18): Activated, avatar foto.
  - Rina Putri (No. 15): Activated dengan email pending `rinaputri.new@qwertysystem.net`.
  - Lilis Handayani, Login (No. 20): tanpa Position dan Employee ID.
  - Dewi Lestari (No. 12): terakhir diubah oleh Siti Nurhaliza (kondisi ini disediakan tim FE pada data Pre-setup; Tabel Pre-setup tidak menyebutnya).
  - Jane Smith (No. 17): Access `Supply Asset`.
  - Joko Susilo (No. 19): Access `Fixed Asset`, `Supply Asset`.
  - Hendra Gunawan (No. 1, Default User): Access `Fixed Asset`, `Global Settings`, `Supply Asset`.
- State global yang dibutuhkan (TC-GS-USER-18): General Settings Date Format `DD/MM/YYYY`, Time Format 24-hour, Timezone `Asia/Jakarta`. Hook `before` mencatat nilai awal lalu menyetelnya ke nilai itu; hook `after` memulihkan nilai awal walau spec gagal di tengah. Kemampuan membaca dan menyetel General Settings lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Suite berjalan serial.
- Kemampuan teknis: hover elemen; membaca nilai Last Update Dewi Lestari dari data backend (disediakan tim FE/BE; dipakai untuk asersi Timezone di langkah 21).

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-14: Kolom Name menampilkan Avatar, Full Name, dan badge Pending Activation

3. Verifikasi sel Name baris Mike Tan menampilkan avatar inisial
4. Verifikasi sel Name baris Mike Tan menampilkan teks `Mike Tan`
5. Verifikasi sel Name baris Mike Tan menampilkan badge `Pending Activation` dengan varian warning
6. Verifikasi sel Name baris John Doe menampilkan avatar foto
7. Verifikasi sel Name baris John Doe menampilkan teks `John Doe`
8. Verifikasi sel Name baris John Doe tanpa badge

### TC-GS-USER-15: Kolom Name menampilkan badge Pending Email Confirmation untuk user Activated dengan email pending

9. Verifikasi sel Name baris Rina Putri menampilkan avatar
10. Verifikasi sel Name baris Rina Putri menampilkan teks `Rina Putri`
11. Verifikasi sel Name baris Rina Putri menampilkan badge `Pending Email Confirmation` dengan varian warning
12. Verifikasi badge `Pending Activation` tidak tampil di baris Rina Putri

### TC-GS-USER-16: Kolom Position dan Employee ID menampilkan `—` saat kosong

13. Verifikasi sel Position baris Lilis Handayani menampilkan `—`
14. Verifikasi sel Employee ID baris Lilis Handayani menampilkan `—`
15. Verifikasi sel Division baris Lilis Handayani terisi
16. Verifikasi sel Access baris Lilis Handayani terisi

### TC-GS-USER-17: Kolom Modified By tampil format singkat dengan tooltip nama lengkap

17. Verifikasi sel Modified By baris Dewi Lestari menampilkan `Siti N`
18. Hover sel Modified By baris Dewi Lestari
19. Verifikasi tooltip `Siti Nurhaliza`

### TC-GS-USER-18: Kolom Last Update mengikuti format General Settings

20. Verifikasi sel Last Update baris Dewi Lestari tampil dengan format `DD/MM/YYYY HH:mm`
21. Verifikasi tanggal dan jam sel Last Update baris Dewi Lestari sesuai Timezone Asia/Jakarta terhadap nilai Last Update Dewi Lestari dari data backend

### TC-GS-USER-19: Kolom Access menampilkan 1 produk

22. Verifikasi sel Access baris Jane Smith menampilkan 1 badge `Supply Asset`
23. Verifikasi sel Access baris Jane Smith tanpa chip `+N more`
24. Verifikasi badge Access baris Jane Smith bervarian BadgeGroup Dark dengan nama produk verbatim

### TC-GS-USER-20: Kolom Access menampilkan 2 produk

25. Verifikasi sel Access baris Joko Susilo menampilkan 2 badge `Fixed Asset` dan `Supply Asset` berurutan alfabetis
26. Verifikasi sel Access baris Joko Susilo tanpa chip `+N more`
27. Verifikasi badge Access baris Joko Susilo bervarian BadgeGroup Dark dengan nama produk verbatim

### TC-GS-USER-21: Kolom Access menampilkan 3 produk

28. Verifikasi sel Access baris Hendra Gunawan menampilkan 2 badge `Fixed Asset` dan `Global Settings`
29. Verifikasi sel Access baris Hendra Gunawan menampilkan chip `+1 more`
30. Verifikasi badge Access baris Hendra Gunawan bervarian BadgeGroup Dark dengan nama produk verbatim

### TC-GS-USER-22: Klik chip Access membuka Popup Access berisi seluruh produk urut alfabetis

31. Klik chip `+1 more` pada sel Access baris Default User (Hendra Gunawan)
32. Verifikasi Popup Access terbuka dengan Title `Access`
33. Verifikasi isi Popup: BadgeGroup Dark `Fixed Asset` | `Global Settings` | `Supply Asset` berurutan A-Z
34. Verifikasi Popup read-only: tanpa tombol aksi teks, hanya icon [✕]
35. Klik icon [✕]
36. Verifikasi Popup Access tertutup
37. Verifikasi halaman kembali ke User List

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (37 langkah) karena sembilan TC rendering kolom berada di satu kelas harness (fungsional, baca saja), memakai satu pembukaan layar dan satu tampilan 100 baris per halaman; tiap blok TC berdiri sendiri dan hanya membaca data.
- Urutan TC sumber dipertahankan. Tidak ada aksi yang mengubah data.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 (memilih 100 baris per halaman supaya seluruh baris Pre-setup berada di satu halaman dan tidak perlu Search per baris).
- Langkah 3 sampai 17, 20, dan 22 sampai 30 mengamati sel pada tampilan hasil langkah 1 dan 2.
- Temuan untuk QA:
  - TC-GS-USER-17 mensyaratkan Dewi Lestari terakhir diubah Siti Nurhaliza; Tabel Pre-setup (No. 12) tidak menyebut Modified By. Disediakan tim FE pada data Pre-setup.
  - TC-GS-USER-18 mensyaratkan General Settings tertentu tetapi tidak menyebut cara mengatur atau membaca nilai Last Update sebagai pembanding Timezone; spec menyetel General Settings di hook dan membaca nilai dari backend (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-14 Expected menyebut "avatar inisial" dan "avatar foto" tanpa selector atau atribut pembeda; ditentukan tim FE.
  - TC-GS-USER-16 menyebut "Cari baris Lilis Handayani" tanpa menyebut cara mencari; spec memakai 100 baris per halaman.
  - TC-GS-USER-22 menyebut baris Default User, sedangkan TC-GS-USER-21 menyebutnya Hendra Gunawan; spec memakai baris Hendra Gunawan (Default User) untuk kedua TC.
