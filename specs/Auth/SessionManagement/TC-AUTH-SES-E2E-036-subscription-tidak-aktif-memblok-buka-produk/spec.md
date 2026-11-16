---
id: TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk
title: "Subscription Tidak Aktif (Archive) Memblok Pembukaan Produk Baru"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-113
  - TC-AUTH-SES-116
  - TC-AUTH-SES-117
  - TC-AUTH-SES-118
coverage:
  web: automated
---

# Subscription Tidak Aktif (Archive) Memblok Pembukaan Produk Baru

## Prerequisites

- Mode: FE+BE.
- Client uji status subscription (Tabel Data Uji Pre-setup #14): satu Client dengan subscription Fixed Asset Active di awal spec; seluruh user uji milik Client ini. Status subscription Fixed Asset Client uji dikondisikan BE per TC lewat langkah eksplisit "Atur status subscription ..." oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD` (aksi Admin Console atau lifecycle subscription di-seed BE; jam server uji tidak digeser karena menggeser jam membuat sesi platform seluruh user uji melewati batas idle).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31), kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Tidak ada sesi-produk Active milik user mana pun:
  - TC-AUTH-SES-113: `Mega Permata` (`megapermata+{runId}-036@qwertysystem.net`)
  - TC-AUTH-SES-116: `Galih Ramadhan` (`galihramadhan+{runId}-036@qwertysystem.net`)
  - TC-AUTH-SES-117: `Nadia Wulandari` (`nadiawulandari+{runId}-036@qwertysystem.net`)
  - TC-AUTH-SES-118: `Irfan Hidayat` (`irfanhidayat+{runId}-036@qwertysystem.net`)
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di hook `before` lewat login API. Browser A pada tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuat di `before`).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client uji ke Active lewat seed yang disediakan tim BE (PRD tidak mendefinisikan pemulihan dari Archive), akhiri semua sesi seed, tutup semua konteks browser, hapus keempat user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client uji (Active, Archive), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant): pengaturan status subscription per langkah oleh akun principal Admin Console; satu konteks browser per user uji; pembacaan status HTTP response request pembukaan sesi-produk Fixed Asset di Browser A; pembacaan sesi-produk milik user uji dari sisi backend (ada atau tidak ada sesi-produk Fixed Asset untuk user itu).
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor principal Admin Console (langkah "Atur status subscription ..." dan hook `after`); akun aktor Total Control (Global Settings) dengan scope Client Expired/uji (#31, seeding di hook `before`).

## Test Steps

### TC-AUTH-SES-113: Buka produk baru saat subscription Archive memunculkan Popup Subscription Not Active

1. Atur status subscription Fixed Asset Client uji menjadi Archive
2. Di Browser A (sesi `Mega Permata`) klik card Fixed Asset → Popup muncul
3. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
4. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
5. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Mega Permata`
6. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-116: OK pada Popup Subscription Not Active mengarahkan ke Portal

7. Di Browser A (sesi `Galih Ramadhan`) klik card Fixed Asset → Popup Subscription Not Active muncul
8. Klik [OK]
9. Verifikasi Popup tertutup
10. Verifikasi Browser A diarahkan ke Portal — Product Hub
11. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-117: Escape dan klik backdrop pada Popup Subscription Not Active menutup popup dengan efek OK

12. Di Browser A (sesi `Nadia Wulandari`) klik card Fixed Asset → Popup Subscription Not Active muncul
13. Tekan tombol Escape
14. Verifikasi Popup tertutup
15. Verifikasi Browser A diarahkan ke Portal — Product Hub
16. Ulangi dari awal: di Browser A klik card Fixed Asset → Popup Subscription Not Active muncul
17. Klik area gelap di luar popup
18. Verifikasi Popup tertutup
19. Verifikasi Browser A diarahkan ke Portal — Product Hub

### TC-AUTH-SES-118: Deep-link ke produk saat subscription tidak aktif: OK ke Portal dan halaman produk tidak dimuat

20. Di Browser A (sesi `Irfan Hidayat`) buka langsung URL dashboard Fixed Asset → Popup muncul
21. Verifikasi Popup Subscription Not Active tampil
22. Verifikasi Halaman produk di belakang popup tidak dimuat
23. Klik [OK]
24. Verifikasi Browser A diarahkan ke Portal — Product Hub

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-113, 116, 117, 118 (urutan TC sumber 113, 116, 117, 118; tidak ada penyimpangan). Status Archive dipasang sekali di awal dan dipakai keempat TC. Pembukaan produk saat Expired dan Grace tidak ditolak dan diuji di spec `TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "Atur status subscription ..." (langkah 1) mengondisikan state tenant; "Ulangi dari awal" pada TC-AUTH-SES-117 (langkah 16) membuka popup kedua kalinya.
- Dependensi TC-AUTH-SES-116 dan 117 pada TC-AUTH-SES-113 (popup sedang tampil): langkah membuka popup (klik card Fixed Asset) disalin pada langkah 7 dan 12 (S-04). Asersi isi popup itu sendiri diuji di TC-AUTH-SES-113.
- Expected c TC-AUTH-SES-113 ("Tidak ada entri log baru di `Global Settings > Activity Log > Session` dan User Log") adalah asersi absence; tidak diasersikan di spec ini dan dirujuk ke spec absence `TC-AUTH-SES-E2E-068-absence-subscription-tidak-aktif` (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-113, 116, 117, 118 menyebut "Client dengan subscription ... berstatus X (Tabel Data Uji Pre-setup #14)" tanpa menyebut cara memicu status itu; spec memakai satu Client uji yang statusnya diatur oleh akun principal Admin Console per langkah. (2) TC-AUTH-SES-113 Expected b memuat tiga klausa (403, sesi-produk tidak dibuat, halaman tidak dimuat); spec memecahnya menjadi tiga `Verifikasi`. Cara membaca "sesi-produk tidak dibuat" tidak disebut TC; spec mengandalkan pembacaan dari sisi backend (Prerequisites). (3) TC-AUTH-SES-117 langkah 2 "Ulangi dari awal" tidak menyebut cara kembali ke Portal selain efek tutup popup; spec mengandalkan hasil langkah 15. (4) Pemulihan status subscription dari Archive ke Active tidak didefinisikan TC maupun PRD License Allocation Subscription (rantai status satu arah); spec menuliskannya sebagai seed yang disediakan tim BE di hook `after`.
