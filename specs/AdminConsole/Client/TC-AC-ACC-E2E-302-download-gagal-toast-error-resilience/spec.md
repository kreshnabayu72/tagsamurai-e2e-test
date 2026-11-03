---
id: TC-AC-ACC-E2E-302-download-gagal-toast-error-resilience
title: "Resilience Download: Kegagalan Ekspor List, Changelog Client, dan Tab Detail Menampilkan Toast Error dengan Nama Berkas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-410
  - TC-AC-ACC-411
  - TC-AC-ACC-412
coverage:
  web: automated
---

# Resilience Download: Kegagalan Ekspor List, Changelog Client, dan Tab Detail Menampilkan Toast Error dengan Nama Berkas

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx pada permintaan ekspor List, ekspor Changelog Client, dan ekspor tabel Quota TAG Detail `PT Sejahtera Abadi`; endpoint ekspor tidak tercantum di TC (disediakan tim FE). Intercept dilepas segera setelah tiap pemicu selesai (S-09). Tidak butuh klien HTTP atau jam server.
- Kelas b (fault injection): satu spec resilience untuk tiga surface Download.

## Test Steps

### Download List gagal (TC-AC-ACC-410)

1. Pasang intercept respons 5xx pada permintaan ekspor List
2. Klik ikon Download lalu klik `Download as CSV`
3. Verifikasi toast error `Error, failed to download Clients.`
4. Lepas intercept

### Download Changelog Client gagal (TC-AC-ACC-411)

5. Klik `[Changelog]` di toolbar List
6. Pasang intercept respons 5xx pada permintaan ekspor Changelog Client
7. Klik ikon Download pada modal Changelog: Client
8. Verifikasi toast error `Error, failed to download Changelog-Client.`
9. Lepas intercept, lalu tutup modal Changelog

### Download tab Detail gagal (TC-AC-ACC-412)

10. Ketik Search `PT Sejahtera Abadi`, tekan Enter, lalu klik Company Name `PT Sejahtera Abadi`
11. Pasang intercept respons 5xx pada permintaan ekspor Quota TAG
12. Klik Download pada tabel Quota TAG
13. Verifikasi toast error `Error, failed to download Client-TAG-PT Sejahtera Abadi.`
14. Lepas intercept

## Notes

- Langkah penghubung (S-03): membuka modal Changelog, membuka Detail `PT Sejahtera Abadi`, memasang dan melepas intercept.
- Temuan untuk QA
  - TC-AC-ACC-410, 411, 412: Langkah `Paksa export gagal` tidak menyebut endpoint atau mekanisme; spec tidak mengarang endpoint (S-13) dan menyerahkannya ke tim FE.
  - TC-AC-ACC-412: Langkah `Download Quota TAG` tidak menyebut tab/lokasi tombol Download; spec mengasumsikan tombol Download pada tabel Quota TAG di Detail.
