---
id: TC-AUTH-LP-E2E-044-absence-policy-version-change
title: "Tidak Ada Pencatatan Log saat Konfirmasi Agreement Ditolak karena Versi Privacy Policy Berubah"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-122
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log saat Konfirmasi Agreement Ditolak karena Versi Privacy Policy Berubah

## Prerequisites

- Mode: FE+BE.
- Seeding: user Activated dan Active dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before`; browser kedua ditutup di hook `after`.
- Sesi Principal: dibuka di jendela privat pada langkah 7; hook `after` menutup jendela privat Principal dan mengakhiri sesinya (cadangan bila spec gagal di tengah).
- Aktor Principal: `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2; kredensial `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`) yang dapat mempublikasikan versi baru di `Admin Console > Settings > Privacy Policy`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: tiga konteks bersamaan (browser subjek, sesi Principal di jendela privat terpisah, browser observer); reCAPTCHA mode uji di environment; seeding user dengan versi Privacy Policy yang disetujui lebih lama dari versi aktif (relatif, lihat aturan State global Privacy Policy); konten versi Privacy Policy baru yang dipublikasikan Principal pada tiap run (langkah 8), yang menjadi versi aktif sesudahnya.
- State global Privacy Policy: publish bersifat append-only dan immutable tanpa restore (`ACPP-LOGIC-01`), sehingga versi aktif tidak dipulihkan dan naik pada setiap run; suite berjalan serial. Seeding user Agreement selalu relatif terhadap versi aktif saat hook `before` (versi yang disetujui user = versi sebelum versi aktif), tanpa nomor versi absolut. Versi baru yang dipublikasikan spec ini tetap menjadi versi aktif.
- TC-AUTH-LP-122: User `Umar Said` (`umarsaid+{runId}-044@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya; tidak memicu MFA; sudah ada baris log sebelumnya (anchor, fixture BE)
- TC-AUTH-LP-122 data: Email `umarsaid+{runId}-044@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-122: Penolakan Confirm Agreement karena versi Privacy Policy berubah tidak dicatat

1. Buka halaman Login with Password di browser pertama
2. Ketik "umarsaid+{runId}-044@qwertysystem.net" di field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in] sampai layar Confirm to Continue tampil
6. Centang checkbox persetujuan
7. Ganti akun: buka jendela privat baru dan login sebagai Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`, lalu buka `Admin Console > Settings > Privacy Policy`
8. Publikasikan versi Privacy Policy baru
9. Pindah ke browser pertama dan klik [Continue ➔] pada layar Confirm to Continue
10. Verifikasi layar Confirm to Continue dimuat ulang dengan versi baru
11. Verifikasi checkbox persetujuan unchecked
12. Pindah ke browser kedua (sesi aktor Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu cari baris untuk user "Umar S" yang dibuat sesudah langkah 1 dimulai
13. Verifikasi tidak ada baris baru untuk user "Umar S" di `Global Settings > Activity Log > Session` (anchor: baris login sebelumnya tetap tampil)
14. Buka `Global Settings > User > Detail > User Log` untuk user "Umar S", buka tab User Log, dan cari baris yang dibuat sesudah langkah 1 dimulai
15. Verifikasi tidak ada baris baru di `Global Settings > User > Detail > User Log` (anchor: baris sebelumnya tetap tampil)

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: asersi absence (prinsip 13g) dengan multi-konteks (Principal mempublikasikan versi dari sesi lain). Sengaja satu spec sendiri karena memakai harness publikasi Privacy Policy yang berbeda dari spec absence lain.
- TC-AUTH-LP-122 terbagi lintas spec: perilaku layar Confirm to Continue yang dimuat ulang saat versi berubah dan persetujuan tersimpan untuk versi baru diuji di spec `TC-AUTH-LP-E2E-026-agreement-policy-version-change` (TC-AUTH-LP-87); di spec ini diasersi Expected c TC-AUTH-LP-122 (layar dimuat ulang dengan versi baru pada langkah 10 dan checkbox unchecked pada langkah 11) serta tidak adanya entri log (S-05, prinsip 10); perilaku lengkapnya ada di spec 026. Langkah 7 dan 8 menguraikan langkah 4 TC (Principal mempublikasikan versi baru di sesi lain pada `Admin Console > Settings > Privacy Policy`); TC tidak merinci langkah UI publikasi, sehingga spec tidak mengarang tombol atau field di luar sumber.
- P-2: jendela privat Principal (konteks kedua) hanya berfungsi sebagai pemicu perubahan versi Privacy Policy pada langkah 7 dan 8 dan bukan objek asersi; objek asersi spec ini adalah layar yang dimuat ulang dan tidak adanya baris log (kelas g), dan asersi lintas konteks pada perilaku sesi Principal tidak ada.
- Langkah penghubung (S-03): login Principal di jendela privat, perpindahan antar konteks, dan pemuatan ulang daftar log hanya menyiapkan konteks.
- Temuan untuk QA:
  - TC-AUTH-LP-122 langkah 4 menyebut Principal "di sesi lain" mempublikasikan versi baru tanpa merinci langkah UI publikasi di `Admin Console > Settings > Privacy Policy`; langkah 7 sampai 8 spec ditulis setinggi tingkat itu.
