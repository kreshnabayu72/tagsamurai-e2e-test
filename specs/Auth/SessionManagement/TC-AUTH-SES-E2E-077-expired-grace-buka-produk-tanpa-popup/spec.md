---
id: TC-AUTH-SES-E2E-077-expired-grace-buka-produk-tanpa-popup
title: "Subscription Expired dan Grace: Pembukaan Produk Baru Membuat Sesi-Produk Tanpa Popup Subscription Not Active"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-111
  - TC-AUTH-SES-112
coverage:
  web: automated
---

# Subscription Expired dan Grace: Pembukaan Produk Baru Membuat Sesi-Produk Tanpa Popup Subscription Not Active

## Prerequisites

- Mode: FE+BE.
- Client uji status subscription (Tabel Data Uji Pre-setup #14): satu Client dengan subscription Fixed Asset Active di awal spec; seluruh user uji milik Client ini. Status subscription Fixed Asset Client uji dikondisikan BE per TC lewat langkah eksplisit "Atur status subscription ..." oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD` (aksi Admin Console atau lifecycle subscription di-seed BE; jam server uji tidak digeser karena menggeser jam membuat sesi platform seluruh user uji melewati batas idle). Client uji punya sisa seat concurrent Fixed Asset (limit belum tercapai).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31), kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Tidak ada sesi-produk Active milik user mana pun:
  - TC-AUTH-SES-111: `Ayu Santoso` (`ayusantoso+{runId}-077@qwertysystem.net`)
  - TC-AUTH-SES-112: `Taufik Kusuma` (`taufikkusuma+{runId}-077@qwertysystem.net`)
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di awal bagian TC masing-masing lewat login API (langkah penghubung), bukan di hook `before`, karena batas idle 15 menit berjalan selama spec berlangsung. Browser A pada tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuka pada langkah itu).
- Browser Admin: konteks browser yang memuat sesi akun aktor Total Control (Global Settings) scope Client uji (Tabel Data Uji Pre-setup #31) di atas (login pertama di hook `before`, sesudah seeding), dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`. Entri baru dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah klik card Fixed Asset pada TC itu yang dihitung.
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client uji ke Active lewat seed yang disediakan tim BE (PRD tidak mendefinisikan pemulihan dari Expired atau Grace), akhiri semua sesi seed dan sesi-produk Fixed Asset yang dibuat spec (milik `Ayu Santoso` dan `Taufik Kusuma`), tutup semua konteks browser, hapus kedua user.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client uji (Active, Expired, Grace), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant): pengaturan status subscription per langkah oleh akun principal Admin Console; satu konteks browser per user uji ditambah Browser Admin bersamaan; pembacaan status HTTP response request pembukaan sesi-produk Fixed Asset di Browser A; pembacaan sesi-produk milik user uji dari sisi backend; pembacaan stempel waktu entri log.
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor principal Admin Console (langkah "Atur status subscription ..." dan hook `after`); akun aktor Total Control (Global Settings) di Browser Admin (seeding di hook `before` dan pembacaan log).

## Test Steps

### TC-AUTH-SES-111: Buka produk baru saat subscription Expired membuat sesi-produk tanpa Popup Subscription Not Active

1. Atur status subscription Fixed Asset Client uji menjadi Expired
2. Buat sesi web Active milik `Ayu Santoso` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
3. Di Browser A (sesi `Ayu Santoso`) klik card Fixed Asset
4. Verifikasi Popup "Subscription Not Active" tidak tampil
5. Verifikasi Sesi-produk Fixed Asset baru dibuat untuk `Ayu Santoso` dan seat diambil
6. Verifikasi Halaman Fixed Asset dimuat
7. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Ayu Santoso` yang dibuat sesudah langkah 3 dimulai
8. Verifikasi Entri `Session started` untuk `Ayu Santoso` tercatat di `Global Settings > Activity Log > Session`
9. Buka `Global Settings > User > Detail > User Log` milik `Ayu Santoso` dan cari entri yang dibuat sesudah langkah 3 dimulai
10. Verifikasi Entri `Session started` untuk `Ayu Santoso` tercatat di `Global Settings > User > Detail > User Log`

### TC-AUTH-SES-112: Buka produk baru saat subscription Grace membuat sesi-produk tanpa Popup Subscription Not Active

11. Atur status subscription Fixed Asset Client uji menjadi Grace
12. Buat sesi web Active milik `Taufik Kusuma` di Browser A (konteks baru) lewat login API → Portal — Product Hub tampil
13. Di Browser A (sesi `Taufik Kusuma`) klik card Fixed Asset
14. Verifikasi Popup "Subscription Not Active" tidak tampil
15. Verifikasi Sesi-produk Fixed Asset baru dibuat untuk `Taufik Kusuma` dan seat diambil
16. Verifikasi Halaman Fixed Asset dimuat
17. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Taufik Kusuma` yang dibuat sesudah langkah 13 dimulai
18. Verifikasi Entri `Session started` untuk `Taufik Kusuma` tercatat di `Global Settings > Activity Log > Session`
19. Buka `Global Settings > User > Detail > User Log` milik `Taufik Kusuma` dan cari entri yang dibuat sesudah langkah 13 dimulai
20. Verifikasi Entri `Session started` untuk `Taufik Kusuma` tercatat di `Global Settings > User > Detail > User Log`

## Notes

- Mode: FE+BE. Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant).
- Expired dan Grace bukan penolak gerbang produk (`AUTHSES-LOGIC-03d`): pembukaan produk baru membuat sesi-produk dan mengambil seat seperti Active. Penolakan aksi tulis pada status ini dimiliki `entity-isolation.md` §18.8 dan diuji per modul; spec ini tidak mengasersinya. Status penolak gerbang (Archive dan seterusnya) diuji di spec `TC-AUTH-SES-E2E-036-subscription-tidak-aktif-memblok-buka-produk`, `TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk`, dan `TC-AUTH-SES-E2E-068-absence-subscription-tidak-aktif`.
- Urutan mengikuti TC sumber (111, 112); status diubah maju sekali (Expired, Grace) tanpa bolak-balik.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "Atur status subscription ..." (langkah 1 dan 11) mengondisikan state tenant; pembuatan sesi platform (langkah 2 dan 12); perpindahan ke Browser Admin, pembukaan surface log, dan pencarian entri (langkah 7, 9, 17, 19).
- Langkah 7 sampai 10 dan 17 sampai 20 menerjemahkan Expected c TC (`Session started` di Activity Log > Session dan User Log); entri baru dibedakan dari entri login seeding lewat stempel waktu sesudah klik card Fixed Asset.
- Temuan untuk QA: (1) TC-AUTH-SES-111 dan 112 menyebut "Client dengan subscription ... berstatus X (Tabel Data Uji Pre-setup #14)" tanpa menyebut cara memicu status itu; spec memakai satu Client uji yang statusnya diatur akun principal Admin Console per langkah (mengikuti spec 036). (2) TC-AUTH-SES-111 dan 112 Expected b memuat dua klausa (sesi-produk dibuat dan halaman dimuat) dan tidak menyebut seat; spec menambahkan "seat diambil" dari PRD `AUTHSES-LOGIC-03d`. (3) Pemulihan status subscription dari Expired dan Grace ke Active tidak didefinisikan PRD License Allocation Subscription; spec menuliskannya sebagai seed yang disediakan tim BE di hook `after`.
