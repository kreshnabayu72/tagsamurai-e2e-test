---
id: TC-GS-PROFILE-E2E-033-resilience-halaman-dan-access-status
title: "Resilience (Mock): Fetch Awal 500, Kegagalan Access & Status, Timeout, Try Again, dan Banner Email Change Gagal Dibaca"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-28
  - TC-GS-PROFILE-188
  - TC-GS-PROFILE-189
  - TC-GS-PROFILE-305
  - TC-GS-PROFILE-310
coverage:
  web: automated
---

# Resilience (Mock): Fetch Awal 500, Kegagalan Access & Status, Timeout, Try Again, dan Banner Email Change Gagal Dibaca

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor dimodelkan lewat payload identitas mock, tanpa login nyata dan tanpa password: Pre-setup #1 (Andi Pratama, Total Control, `Fixture.myProfile.accounts.totalControl.email`) untuk TC-GS-PROFILE-28; Pre-setup #5 (Sinta Maharani, `Fixture.myProfile.accounts.multiAccess.email`; App Access Global Settings, Fixed Asset, Admin Console, Supply Asset, SIEM) untuk TC-GS-PROFILE-188, 189, dan 305; Pre-setup #8 (Citra Lestari, `Fixture.myProfile.accounts.pendingEmail.email`; permintaan Email change live ke `Fixture.myProfile.pendingEmail.newEmail`) untuk TC-GS-PROFILE-310. Pergantian akun adalah pergantian payload identitas mock (Step ganti akun eksplisit).
- Tidak ada `Spectra.env.<NAMA>` yang dipakai spec ini.
- Halaman My Profile dibuka hook `beforeEach` suite dengan mock normal. Lihat `suite.md`, Hook suite 2.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook suite 1, 3, 4, 6, dan 7 mengelola backend nyata dan tidak berlaku pada spec mock ini (lihat Temuan untuk QA). Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` dijawab seen oleh mock (disediakan tim FE).
- Endpoint yang dipanggil halaman pada kondisi tes: berkas `openapi.yaml` dan `low-level-design.md` tidak ada di folder modul `global-settings/my-profile/` (keduanya diperiksa), sehingga path dan bentuk respons tidak dikarang dan seluruhnya disediakan tim FE:
  - Fetch My Profile (Header, Section Identity, Section Custom Field): normal pada semua blok kecuali TC-GS-PROFILE-28 (respons 500, lalu dipulihkan normal).
  - Fetch Access & Status per produk: normal kecuali TC-GS-PROFILE-188 dan 189 (respons 500 untuk pilihan "Fixed Asset", lalu dipulihkan normal) dan TC-GS-PROFILE-305 (tanpa respons, timeout klien).
  - Baca permintaan Email change: respons 500 pada TC-GS-PROFILE-310, normal pada blok lain.
  - Pencatat jumlah request fetch Header dan Section Identity (dipakai TC-GS-PROFILE-189).
  - Stream SSE bila halaman berlangganan pada kondisi tes: koneksi dijawab terbuka tanpa event.
- API pendukung di luar sumber modul disediakan tim FE: identitas pengguna, menu, daftar App Access untuk Product Selector, dan flag Guided Tooltip.
- Tidak ada data backend atau state global yang diubah. Pemulihan: semua mock dilepas di hook `after` walau spec gagal di tengah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-PROFILE-28: Fetch awal gagal, error state seluruh halaman, dan Try Again (Pre-setup #1)

1. Pasang mock respons 500 untuk fetch My Profile
2. Muat ulang halaman My Profile (F5)
3. Verifikasi seluruh halaman menampilkan "Unable to load this data." dengan tombol [Try Again]
4. Pulihkan mock fetch My Profile ke respons normal
5. Klik [Try Again]
6. Verifikasi seluruh halaman dimuat ulang (error state hilang)
7. Verifikasi isi My Profile tampil

### Ganti akun ke Pre-setup #5

8. Ganti akun: ubah identitas mock ke Pre-setup #5 (Sinta Maharani) dengan semua mock normal, lalu muat ulang My Profile

### TC-GS-PROFILE-188: Fetch Access & Status gagal saat berganti produk (Pre-setup #5)

9. Pasang mock respons 500 untuk fetch Access & Status
10. Pilih opsi "Fixed Asset" pada Product Selector
11. Verifikasi Section Access & Status menampilkan "Unable to load this data." dengan tombol [Try Again]
12. Verifikasi Header, Section Identity, dan Section Custom Field tetap tampil
13. Verifikasi Product Selector menampilkan "Viewing: Fixed Asset"

### TC-GS-PROFILE-189: Try Again pada error state selector (Pre-setup #5)

14. Catat jumlah request fetch Header dan Section Identity yang sudah terkirim
15. Pulihkan mock fetch Access & Status ke respons normal
16. Klik [Try Again]
17. Verifikasi Section Access & Status memuat isi konteks Fixed Asset
18. Verifikasi Header dan Section Identity tidak dimuat ulang (tidak ada request fetch Header dan Section Identity baru sejak langkah 14)

### TC-GS-PROFILE-305: Fetch Access & Status timeout (Pre-setup #5)

19. Muat ulang halaman My Profile (F5)
20. Pasang mock fetch Access & Status tanpa respons (timeout)
21. Pilih opsi "Fixed Asset" pada Product Selector
22. Verifikasi Section Access & Status menampilkan "Unable to load this data." dengan tombol [Try Again]
23. Verifikasi bagian halaman lain (Header, Section Identity, Section Custom Field) tetap tampil
24. Pulihkan mock fetch Access & Status ke respons normal

### Ganti akun ke Pre-setup #8

25. Ganti akun: ubah identitas mock ke Pre-setup #8 (Citra Lestari) dengan permintaan Email change live

### TC-GS-PROFILE-310: Baca permintaan Email change gagal (Pre-setup #8)

26. Pasang mock respons 500 untuk baca permintaan Email change
27. Muat ulang halaman My Profile (F5)
28. Verifikasi Header, Section Identity, Section Access & Status, dan Section Custom Field tampil
29. Verifikasi banner Pending Email Change tidak tampil
30. Klik [Change Password]
31. Verifikasi modal Change Password terbuka
32. Tutup modal Change Password lewat [✕] (form kosong)
33. Lepas semua mock

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-28, 188, 189, 305, 310). Tidak ada TC hanya-BE.
- Kelas harness b (fault injection / resilience), seluruhnya perilaku FE atas respons mock (konvensi bagian 6, Resilience `Mode: mock`). Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2, 19, dan 27 (muat ulang halaman agar fetch memakai mock; halaman sudah dibuka hook `beforeEach`), langkah 4, 15, 24, dan 33 (memulihkan atau melepas mock), langkah 8 dan 25 (Step ganti akun), langkah 14 (pencatatan jumlah request sebagai baseline untuk langkah 18), dan langkah 32 (menutup modal kosong tanpa dialog).
- Urutan di TC-GS-PROFILE-310: langkah 28 (butir b Expected) ditaruh sebelum langkah 29 (butir a) karena asersi absence banner memakai halaman yang sudah termuat sebagai anchor (bagian 8b butir 2).
- TC-GS-PROFILE-189 melanjutkan error state dari TC-GS-PROFILE-188 (pilihan "Fixed Asset" sudah gagal), sehingga langkah 1 TC tidak diulang.
- Temuan untuk QA:
  - Hook suite 1 (login nyata), 3, 4, 6, dan 7 mengasumsikan backend nyata; spec `Mode: mock` memodelkan identitas lewat payload mock. Mekanisme hook suite untuk spec mock perlu dipastikan tim FE.
  - TC-GS-PROFILE-189 Expected "Header dan Section Identity tidak dimuat ulang" tidak menyebut cara mengamatinya; spec memakai pencatat jumlah request fetch (path disediakan tim FE).
  - TC-GS-PROFILE-305 tidak menyebut ambang timeout klien; ambang dan cara mock memutus respons ditetapkan tim FE.
  - TC-GS-PROFILE-310 menulis "Login sbg Role: Total Control" bersama akun Pre-setup #8; spec memakai akun Pre-setup #8 sebagai sumber.
