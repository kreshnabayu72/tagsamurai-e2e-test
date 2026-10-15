---
id: TC-AUTH-SES-E2E-035-popup-concurrent-dan-subscription-di-mobile
title: "Popup Concurrent Session Limit Reached dan Subscription Not Active di Aplikasi Mobile"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-302
  - TC-AUTH-SES-303
coverage:
  mobile: automated
---

# Popup Concurrent Session Limit Reached dan Subscription Not Active di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android), terpasang di perangkat Android uji A (Tabel Data Uji Pre-setup #10) yang dapat diketuk oleh driver otomasi.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) untuk user Client Q2 dan scope Client Expired/uji (Tabel Data Uji Pre-setup #31) untuk user Client Expired, kredensial `Spectra.env.GS_TC_PASSWORD`): user profil BASE (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Seed seat Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2): `Gunawan Prakoso` (`gunawanprakoso+{runId}-035@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-035@qwertysystem.net`), masing-masing dengan sesi platform web Active dan satu sesi-produk Fixed Asset Active sehingga seat terpakai 2 dari kuota 2 (seat penuh) selama TC-AUTH-SES-302
  - TC-AUTH-SES-302: `Nur Wibowo` (`nurwibowo+{runId}-035@qwertysystem.net`), milik Client Q2 dengan App Access Fixed Asset dan Supply Asset
  - TC-AUTH-SES-303: `Agus Nugroho` (`agusnugroho+{runId}-035@qwertysystem.net`), milik Client Expired (Tabel Data Uji Pre-setup #14: subscription Fixed Asset berstatus Expired) dengan App Access Fixed Asset
- Sesi mobile Active di perangkat Android uji A untuk tiap user dibuat pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena perangkat dipakai bergantian: login nyata di perangkat dengan email dan password user, pada Prompt Enable Biometric ketuk [Not now] (Tabel Data Uji Pre-setup #28), lalu aplikasi menampilkan Portal — Product Hub; data aplikasi akun sebelumnya dibersihkan.
- Hook `after`: akhiri semua sesi dan sesi-produk seed (web, mobile, termasuk dua seed seat); bersihkan data aplikasi mobile di perangkat Android uji A; hapus keempat user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (diisi penuh oleh dua seed), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native) untuk membuka card produk dan membaca popup; login nyata di perangkat dengan penanganan Prompt Enable Biometric ([Not now]); pembacaan status sesi-produk (ada atau tidak ada sesi-produk Fixed Asset milik user) dari BE oleh akun aktor.
- Akun yang dipakai: user uji masing-masing TC pada perangkat Android uji A; akun aktor Total Control (Global Settings) dengan scope Client Q2 (#26) dan Client Expired/uji (#31) hanya untuk seeding dan pembacaan BE.

## Test Steps

### TC-AUTH-SES-302: Popup Concurrent session limit reached tampil di aplikasi mobile saat seat penuh

1. Siapkan: sesi mobile Active milik `Nur Wibowo` di perangkat Android uji A lewat login nyata (aplikasi menampilkan Portal — Product Hub) dengan seat Fixed Asset Client Q2 penuh (2 sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan `Melati Anggun`)
2. Di perangkat Android uji A buka card Fixed Asset → Popup muncul
3. Verifikasi Popup "Concurrent session limit reached" tampil dengan Body "You've reached the concurrent session limit for this product. Try again later once a session becomes available."
4. Verifikasi Tidak ada sesi-produk Fixed Asset yang dibuat untuk `Nur Wibowo`
5. Ketuk [OK] pada popup

### TC-AUTH-SES-303: Popup Subscription Not Active tampil di aplikasi mobile saat subscription Expired

6. Siapkan: sesi mobile Active milik `Agus Nugroho` di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan; aplikasi menampilkan Portal — Product Hub)
7. Di perangkat Android uji A buka card Fixed Asset → Popup muncul
8. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
9. Verifikasi Tidak ada sesi-produk Fixed Asset yang dibuat untuk `Agus Nugroho`

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan mengikuti TC sumber (302, 303). Tiap TC memakai user sendiri dengan kondisi yang berbeda (seat penuh di Client Q2, subscription Expired di Client Expired) sehingga tidak saling bergantung; kondisi seat penuh dipasang dan dilepas oleh seed milik spec.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan sesi mobile lewat login nyata di awal tiap TC; mengetuk [OK] pada popup (langkah 5) agar aplikasi kembali ke Portal sebelum TC berikutnya.
- Layar popup di mobile dan perilaku tombol [OK] mengikuti PRD §4.2 (DO-10); TC sumber tidak memuat asersi tombol [OK] sehingga spec tidak menambahkannya.
- Temuan untuk QA: (1) TC-AUTH-SES-302 dan 303 hanya menyebut "tidak ada sesi-produk dibuat" tanpa menyebut permukaan baca; spec membacanya dari BE oleh akun aktor. (2) TC-AUTH-SES-303 memakai Client Expired (Tabel Data Uji Pre-setup #14) tanpa menyebut aktor yang berhak men-seed user pada Client itu; spec memakai akun aktor Total Control dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31).