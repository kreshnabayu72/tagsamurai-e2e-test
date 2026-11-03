---
id: TC-AC-LCS-E2E-161-landing-page-subscription-expired-archive
title: "Landing Page Subscription Expired untuk Client yang Login pada Archive Period"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-570
coverage:
  web: automated
---

# Landing Page Subscription Expired untuk Client yang Login pada Archive Period

## Prerequisites

- Mode: FE+BE. Kelas harness h (state tenant: Subscription Archive).
- Akun aktor: Default User Client PT Maju Jaya `defaultUserClientMajuJaya_automated_{namaCompany}@qwertysystem.net` (Pre-setup 13, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); password dari `Spectra.env.AC_DUCLIENT_PASSWORD`. Login di hook `before` spec ini ke client console (spec ini dikecualikan dari pembukaan Lifecycle Settings oleh hook `beforeEach` suite; pengecualian dinyatakan di `suite.md`); hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: Client PT Maju Jaya (Direct, subscription Paid) diatur lewat Fixture BE ke status `Archive`; dipulihkan di hook `after` suite.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12).
- State global: status subscription PT Maju Jaya diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

1. Atur lewat Fixture BE: Subscription PT Maju Jaya berstatus `Archive` (data pada cold storage)
2. Buka client console sebagai Default User PT Maju Jaya (sesi login hook `before` spec ini)
3. Verifikasi Page Header tetap normal (breadcrumb, greeting, logout)
4. Verifikasi area konten utama diganti total oleh halaman dengan heading "Your Subscription Has Expired"
5. Verifikasi halaman menampilkan countdown menuju Hard Purge
6. Verifikasi halaman menampilkan instruksi menghubungi Support (email atau telepon) untuk retrieval data
7. Verifikasi tidak ada akses menu atau fitur produk selain logout (fully blocking)
8. Verifikasi tidak ada tombol atau form request retrieval di aplikasi

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness h.
- Expected a TC ditulis per klausa (header normal, heading, countdown, instruksi Support) dan Expected b ditulis dua `Verifikasi` (tanpa akses menu atau fitur, tanpa tombol atau form retrieval), sesuai S-01.
- Temuan untuk QA:
  - Akun Default User Client PT Maju Jaya kini tertulis di Pre-setup 13 sebagai usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE; password dari `Spectra.env.AC_DUCLIENT_PASSWORD`.
  - Langkah 1 TC 570 "Login ke client console" dipenuhi login di hook `before` spec ini; hook `beforeEach` suite membuka Lifecycle Settings milik Admin Console, sehingga spec client console dikecualikan darinya (pengecualian dinyatakan di `suite.md`).
  - TC 570 Expected a menyebut countdown tanpa nilai; spec hanya mengasersi keberadaannya.
  - Post Condition ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2.
