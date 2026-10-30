---
id: TC-GS-PROFILE-E2E-001-screening-navigasi-dan-header
title: "Screening halaman: buka My Profile dari tiga app, Breadcrumb, dan Header"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-1
  - TC-GS-PROFILE-2
  - TC-GS-PROFILE-3
  - TC-GS-PROFILE-4
  - TC-GS-PROFILE-5
  - TC-GS-PROFILE-6
  - TC-GS-PROFILE-9
  - TC-GS-PROFILE-21
coverage:
  web: automated
---

# Screening halaman: buka My Profile dari tiga app, Breadcrumb, dan Header

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #1 Andi Pratama (`totalControlProfile_automated_{namaCompany}@qwertysystem.net`), Total Control, Employee ID EMP-0001, Position Finance Manager, Division Finance, tanpa foto aktif, App Access Global Settings, Fixed Asset, dan Admin Console; password `Spectra.env.GS_PROFILE_TC_PASSWORD`.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Tabel "App asal" untuk perulangan TC-GS-PROFILE-1, 2, dan 3 (urutan baris = urutan iterasi):

| App asal |
|---|
| Global Settings |
| Admin Console |
| Fixed Asset |

- Data Dinamis: tidak ada. Spec ini hanya membaca dan tidak mengubah state, sehingga tidak ada pemulihan atau cleanup.

## Test Steps

### Screening halaman My Profile (TC-GS-PROFILE-4)

1. Verifikasi Breadcrumb `My Profile` tampil pada Header
2. Verifikasi Avatar berisi inisial `AP`
3. Verifikasi Full Name `Andi Pratama` tampil
4. Verifikasi Employee ID `EMP-0001` tampil
5. Verifikasi Product Selector `Viewing: Global Settings` tampil
6. Verifikasi tombol [Change Password] tampil di sisi kanan Header
7. Verifikasi Badge `Active` tampil
8. Verifikasi urutan Section dari atas ke bawah: Section Identity, Section Access & Status, Section Custom Field
9. Verifikasi footer halaman tidak memuat pagination dan tidak memuat tabel
10. Verifikasi tidak ada Toggle Active, menu [⋯], dan Tab pada halaman

### Breadcrumb tanpa Page Title (TC-GS-PROFILE-5)

11. Verifikasi Breadcrumb berupa satu segmen statis `My Profile` yang bukan link
12. Klik segmen `My Profile` pada Breadcrumb
13. Verifikasi klik tidak mengubah halaman
14. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
15. Verifikasi konten utama langsung dimulai di bawah Breadcrumb

### Tombol replay Guided Tooltip (TC-GS-PROFILE-6)

16. Verifikasi tombol [?] (icon question-mark) tampil tepat di kanan Breadcrumb `My Profile`
17. Hover tombol [?]
18. Verifikasi tooltip `Show guide` tampil

### Badge Active read-only (TC-GS-PROFILE-9)

19. Verifikasi Badge `Active` tampil di bawah Full Name
20. Klik Badge `Active`
21. Verifikasi klik tidak mengubah status: Badge masih `Active`
22. Verifikasi klik tidak membuka dialog

### Header tanpa aksi administratif (TC-GS-PROFILE-21)

23. Hover sisi kanan Header
24. Verifikasi tidak ada Toggle Active, menu [⋯], item Edit Profile, dan item Delete User
25. Verifikasi satu-satunya tombol aksi halaman adalah [Change Password]

### Buka My Profile dari tiga app (TC-GS-PROFILE-1, TC-GS-PROFILE-2, TC-GS-PROFILE-3)

26. Untuk setiap baris tabel App asal (langkah 26 sampai 31): pindah ke app pada baris tabel dan buka halaman mana pun di app itu (di Global Settings: halaman selain My Profile)
27. Klik icon Profile di navbar
28. Verifikasi account menu terbuka dan memuat item `My Profile`
29. Klik item `My Profile`
30. Verifikasi halaman My Profile terbuka sebagai destinasi tunggal Global Settings (bukan halaman per-app)
31. Verifikasi Breadcrumb halaman: `My Profile`

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-1, 2, 3, 4, 5, 6, 9, 21).
- Urutan TC di spec berbeda dari urutan sumber: screening halaman (TC-GS-PROFILE-4, 5, 6, 9, 21) di awal dan TC-GS-PROFILE-1, 2, 3 di akhir, karena ketiganya memindahkan app asal dan mengosongkan konteks halaman yang sudah dibuka hook `beforeEach`.
- Pengulangan: langkah 26 sampai 31 diulang untuk tiap baris tabel App asal. Parameter iterasi hanya app asal; `Verifikasi` tetap satu per klausa (S-01). TC-GS-PROFILE-1, 2, 3 beda hanya di app asal dan Expected-nya identik.
- Spec berisi 31 langkah nominal dan sekitar 43 langkah setelah ekspansi perulangan (25 langkah ditambah 6 langkah dikali 3 iterasi), di atas smell 35 langkah. Alasan: seluruh blok satu topik (screening halaman My Profile dan jalur buka halaman), satu kelas harness, tanpa mengubah data; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 12, 17, 20, dan 23 adalah aksi uji TC; langkah 26 memindahkan app asal dan membuka halaman awal sebelum membuka My Profile.
- Temuan untuk QA:
  - TC-GS-PROFILE-1, 2, dan 3 menulis Expected "destinasi tunggal Global Settings (bukan halaman per-app)" tanpa penanda yang dapat diamati (URL atau elemen). Spec menulis kalimat itu sebagai `Verifikasi` apa adanya; penanda observasinya perlu ditetapkan QA.
