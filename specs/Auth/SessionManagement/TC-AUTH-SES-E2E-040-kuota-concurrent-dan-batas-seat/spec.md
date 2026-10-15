---
id: TC-AUTH-SES-E2E-040-kuota-concurrent-dan-batas-seat
title: "Kuota Concurrent dan Batas Seat per Produk"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-124
  - TC-AUTH-SES-125
  - TC-AUTH-SES-126
  - TC-AUTH-SES-127
  - TC-AUTH-SES-128
  - TC-AUTH-SES-129
coverage:
  web: automated
---

# Kuota Concurrent dan Batas Seat per Produk

## Prerequisites

- Mode: FE+BE.
- Client uji (kelas harness e: volume data khusus, kuota seat):
  - Client Q0 (Tabel Data Uji Pre-setup #13): subscription Fixed Asset Active; kuota concurrent Fixed Asset dikondisikan per TC (diisi eksplisit 0 pada TC-AUTH-SES-125, tidak dikonfigurasi pada TC-AUTH-SES-126) lewat langkah eksplisit.
  - Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2 di awal spec; seat dikondisikan per TC lewat langkah "Siapkan state Client Q2".
- Akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`: mengubah kuota lewat `Admin Console > License Allocation` (Client Q0 dan Client Q2).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q0 (Tabel Data Uji Pre-setup #30) untuk user Client Q0 dan scope Client Q2 (Tabel Data Uji Pre-setup #26) untuk user Client Q2, kredensial `Spectra.env.GS_TC_PASSWORD`): user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Client Q0, TC-AUTH-SES-125: `Agus Wijaya` (`aguswijaya+{runId}-040@qwertysystem.net`)
  - Client Q0, TC-AUTH-SES-126: `Rina Setiawan` (`rinasetiawan+{runId}-040@qwertysystem.net`)
  - Client Q2, TC-AUTH-SES-124: `Rizky Nugroho` (`rizkynugroho+{runId}-040@qwertysystem.net`) dan `Nur Maulana` (`nurmaulana+{runId}-040@qwertysystem.net`)
  - Client Q2, TC-AUTH-SES-127: `Hendra Santoso` (`hendrasantoso+{runId}-040@qwertysystem.net`)
  - Client Q2, TC-AUTH-SES-128: `Fajar Permata` (`fajarpermata+{runId}-040@qwertysystem.net`)
  - Client Q2, TC-AUTH-SES-129: `Lestari Lestari` (`lestarilestari+{runId}-040@qwertysystem.net`)
  - Client Q2, user seat seed (Tabel Data Uji Pre-setup #7): `Gunawan Prakoso` (`gunawanprakoso+{runId}-040@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-040@qwertysystem.net`), dipakai pada TC-AUTH-SES-124, 127, 128, 129
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di hook `before` lewat login API. Browser A, Browser C, dan Browser Seed adalah konteks browser terpisah yang memuat sesi platform user tertentu (satu konteks per user, dibuat di `before`); Browser Seed memuat sesi platform `Gunawan Prakoso`. Sesi-produk seed `Gunawan Prakoso` dan `Melati Anggun` dibuka dan diakhiri lewat API Open Product Session dan End Product Session (Auth - Session Management) pada langkah "Siapkan state Client Q2", yang juga memastikan kuota Fixed Asset 2 dan membuat ulang sesi platform seed bila sudah berakhir.
- Akun aktor lain (login di hook `before`, satu konteks browser per akun):
  - Browser License: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License di Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser Admin: akun Total Control (Global Settings) dengan scope Client Q2 di atas (Tabel Data Uji Pre-setup #26, `Spectra.env.GS_TC_PASSWORD`), membaca `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log`.
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): kembalikan kuota Fixed Asset dan Supply Asset Client Q2 ke 2, kembalikan kuota Fixed Asset Client Q0 ke kondisi awal (tidak dikonfigurasi), akhiri semua sesi seed dan sesi-produk, tutup semua konteks browser, hapus semua user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: kuota concurrent Fixed Asset Client Q0 dan Client Q2, seat terpakai Fixed Asset dan Supply Asset Client Q2, dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: pengubahan kuota (nilai eksplisit, nilai tidak dikonfigurasi, naik, turun) lewat License Allocation oleh akun principal; API Open Product Session dan End Product Session oleh sesi platform user seed; pembacaan hitungan seat aktif Fixed Asset di License > Concurrent User dan hitungan seat Supply Asset dari sisi backend (TC tidak menyebut layar pembaca Supply Asset); pembacaan sesi-produk milik user uji dari sisi backend.
- Akun yang dipakai: user uji pada Browser A, Browser C, dan Browser Seed; Browser License dan Browser Admin memakai akun aktor di atas; akun aktor principal Admin Console untuk mengubah kuota; akun aktor Total Control (Global Settings) dengan scope Client Q0 (#30) dan Client Q2 (#26) untuk seeding di hook `before`.

## Test Steps

### TC-AUTH-SES-125: Kuota concurrent 0 yang dikonfigurasi memblok semua pembukaan produk

1. Atur kuota concurrent Fixed Asset Client Q0 menjadi 0 yang diisi eksplisit
2. Di Browser A (sesi `Agus Wijaya`) klik card Fixed Asset → Popup muncul
3. Verifikasi Popup "Concurrent session limit reached" tampil
4. Verifikasi Sesi-produk tidak dibuat untuk `Agus Wijaya`

### TC-AUTH-SES-126: Kuota concurrent yang belum dikonfigurasi diperlakukan sebagai 0 dan bukan unlimited

5. Kosongkan konfigurasi kuota concurrent Fixed Asset Client Q0 sehingga kuota tidak dikonfigurasi (subscription Fixed Asset tetap Active)
6. Di Browser A (sesi `Rina Setiawan`) klik card Fixed Asset → Popup muncul
7. Verifikasi Popup "Concurrent session limit reached" tampil
8. Verifikasi Sesi-produk tidak dibuat untuk `Rina Setiawan`
9. Verifikasi Pembukaan produk tidak diizinkan seolah-olah unlimited

### TC-AUTH-SES-124: Kuota diturunkan di bawah jumlah seat aktif tidak memutus sesi existing tetapi memblok sesi baru

10. Siapkan state Client Q2: kuota Fixed Asset 2; satu-satunya sesi-produk Fixed Asset Active milik `Gunawan Prakoso`
11. Di Browser A (sesi `Rizky Nugroho`) klik card Fixed Asset → Fixed Asset terbuka (seat aktif 2)
12. Turunkan kuota Fixed Asset Client Q2 dari 2 ke 1 lewat `Admin Console > License Allocation`
13. Di Browser A reload halaman Fixed Asset
14. Verifikasi Sesi-produk `Rizky Nugroho` tetap Active (grandfathered)
15. Verifikasi Sesi-produk `Gunawan Prakoso` tetap Active (grandfathered)
16. Di Browser C (sesi `Nur Maulana`, di Portal — Product Hub) klik card Fixed Asset → Popup muncul
17. Verifikasi Popup "Concurrent session limit reached" tampil untuk `Nur Maulana`
18. Verifikasi Sesi-produk tidak dibuat untuk `Nur Maulana`

### TC-AUTH-SES-127: Kuota dinaikkan memungkinkan pembukaan produk berikutnya berhasil

19. Siapkan state Client Q2: kuota Fixed Asset 2; sesi-produk Fixed Asset Active hanya milik `Gunawan Prakoso` dan `Melati Anggun` (seat aktif 2); catat penanda waktu dasar Activity Log (waktu server) sebelum membuka produk
20. Naikkan kuota Fixed Asset Client Q2 dari 2 ke 3 lewat `Admin Console > License Allocation`
21. Di Browser A (sesi `Hendra Santoso`, di Portal — Product Hub) klik card Fixed Asset
22. Verifikasi Browser A masuk Fixed Asset tanpa popup
23. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
24. Verifikasi Seat aktif Fixed Asset menjadi 3
25. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Hendra Santoso`, lalu cari entri `Hendra Santoso`
26. Verifikasi Entri `Session started` untuk `Hendra Santoso` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
27. Verifikasi Entri `Session started` untuk `Hendra Santoso` tercatat di `Global Settings > User > Detail > User Log` milik `Hendra Santoso` dengan waktu setelah penanda waktu dasar (dicari lewat Note, bukan lewat posisi teratas)

### TC-AUTH-SES-128: Seat yang dilepas karena sesi berakhir memungkinkan user lain membuka produk

28. Siapkan state Client Q2: kuota Fixed Asset 2; sesi-produk Fixed Asset Active hanya milik `Gunawan Prakoso` dan `Melati Anggun` (seat aktif 2); catat penanda waktu dasar Activity Log (waktu server) sebelum membuka produk
29. Di Browser Seed (sesi `Gunawan Prakoso`) klik menu Profile lalu pilih Log Out → seat `Gunawan Prakoso` dilepas (seat aktif 1)
30. Di Browser C (sesi `Fajar Permata`, di Portal — Product Hub) klik card Fixed Asset
31. Verifikasi Browser C masuk Fixed Asset tanpa popup
32. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
33. Verifikasi Seat aktif Fixed Asset kembali menjadi 2
34. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Fajar Permata`, lalu cari entri `Fajar Permata`
35. Verifikasi Entri `Session started` untuk `Fajar Permata` tercatat di `Activity Log > Session` milik Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
36. Verifikasi Entri `Session started` untuk `Fajar Permata` tercatat di `Global Settings > User > Detail > User Log` milik `Fajar Permata` dengan waktu setelah penanda waktu dasar (dicari lewat Note, bukan lewat posisi teratas)

### TC-AUTH-SES-129: Seat Fixed Asset penuh tidak memblok pembukaan Supply Asset karena concurrent dihitung per produk

37. Siapkan state Client Q2: kuota Fixed Asset 2 dan kuota Supply Asset 2; sesi-produk Fixed Asset Active hanya milik `Gunawan Prakoso` dan `Melati Anggun` (seat Fixed Asset 2); tidak ada sesi-produk Supply Asset Active (seat Supply Asset 0)
38. Di Browser A (sesi `Lestari Lestari`, di Portal — Product Hub) klik card Supply Asset
39. Verifikasi Browser A masuk Supply Asset tanpa popup
40. Verifikasi Seat Supply Asset terpakai 1
41. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
42. Verifikasi Seat Fixed Asset tetap 2

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness e (volume data khusus: kuota seat).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-125, 126, 124, 127, 128, 129, sama dengan rencana (urutan TC sumber 124 s.d. 129). TC 125 dan 126 (pemblokiran, Client Q0) dijalankan lebih dulu; TC 124 sebelum 127 karena TC 124 menurunkan kuota dan langkah "Siapkan state" TC berikutnya mengembalikan kuota ke 2.
- Ukuran: spec melewati sekitar 35 langkah karena enam TC kuota berdiri sendiri dengan user dan state Client masing-masing yang disiapkan ulang di awal bagiannya, sehingga bagian berikutnya tetap bermakna walau bagian sebelumnya gagal; blok baca log (langkah 25 sampai 27 dan 34 sampai 36) tidak dihitung ke batas.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "Siapkan state Client Q2" (langkah 10, 19, 28, 37) membentuk seat dan kuota awal tiap TC lewat API dan pada TC-AUTH-SES-127 dan 128 juga mencatat penanda waktu dasar log; langkah mengatur, mengosongkan, menurunkan, dan menaikkan kuota (langkah 1, 5, 12, 20) mengondisikan kuota lewat License Allocation; langkah 23, 32, dan 41 memuat ulang daftar Browser License sebelum seat dibaca (S-14); langkah 29 melakukan Manual Logout `Gunawan Prakoso` sebagai bagian precondition c TC-AUTH-SES-128 (logout manual sebagai penyebab seat dilepas).
- Expected TC-AUTH-SES-124, 125, 126 tidak menyebut Body popup "Concurrent session limit reached"; spec tidak mengasersikan Body (diasersikan di spec lain yang memuat dialog dan popup konkurensi).
- Temuan untuk QA: (1) TC-AUTH-SES-124 Precondition b menyebut kuota sudah diturunkan, sementara dua sesi-produk aktif hanya mungkin dibuka saat kuota masih 2; spec memuat penurunan kuota sebagai langkah 12 setelah seat dibuka. (2) TC-AUTH-SES-124 menyebut sesi-produk `Rizky Nugroho` dan `Gunawan Prakoso` sebagai seat awal, sedangkan TC-AUTH-SES-127, 128, 129 memakai `Gunawan Prakoso` dan `Melati Anggun`; spec membentuk seat per TC dengan langkah "Siapkan state". (3) TC-AUTH-SES-126 butir Expected b ("Pembukaan tidak diizinkan seolah-olah unlimited") mengulang butir a tanpa pengamatan tersendiri; spec tetap memuatnya sebagai `Verifikasi` terpisah. (4) TC-AUTH-SES-129 tidak menyebut layar pembaca seat Supply Asset; spec membacanya dari sisi backend (Prerequisites). (5) TC-AUTH-SES-125 dan 126 menyebut "Client Q0 (#13): kuota 0 atau tidak dikonfigurasi" sebagai satu data tetap; spec mengubah konfigurasi kuota Client Q0 antar-TC dan memulihkannya di `after`. (6) TC-AUTH-SES-127 dan 128 membaca `Activity Log > Session` milik Fixed Asset (surface forward-dependency, NC-15) tanpa tanda `[DEFERRED]`, sedangkan TC-AUTH-SES-95 dan 198 yang membaca surface yang sama bertanda `[DEFERRED]`; spec mengikuti TC dan membaca surface itu bersama User Log.
