---
id: TC-AC-DN-E2E-009-principal-tanpa-riwayat
title: "Principal Tanpa Riwayat: List Kosong, Opsi Filter Kosong, Changelog Tanpa Entri"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-25
  - TC-AC-DN-294
  - TC-AC-DN-403
  - TC-AC-DN-449
coverage:
  web: automated
---

# Principal Tanpa Riwayat: List Kosong, Opsi Filter Kosong, Changelog Tanpa Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal Tanpa Riwayat (Pre-setup #12) `Fixture.settings-device-name.totalControlFresh` (email `totalControlFresh_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.AC_DN_FRESH_PASSWORD` (nama env berkode modul sesuai `suite.md`, didaftarkan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_DN_FRESH_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah state apa pun.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Principal `Principal Tanpa Riwayat` (#12) yang belum memiliki Device Name dan belum memiliki entri Changelog. Baca-saja; tidak ada data Dinamis dan tidak ada aksi tulis.

## Test Steps

### TC-AC-DN-25: List kosong untuk Principal tanpa Device Name menampilkan empty state S-02

1. Verifikasi empty state dengan illustration, Title "No device names yet" dan Description "Get started by creating your first device name."
2. Verifikasi empty state tidak memuat tombol CTA
3. Verifikasi tombol `[+ Device Name]` tetap tampil di Table Tools
4. Verifikasi pesan error load tidak tampil

### TC-AC-DN-294: Dropdown filter menampilkan `No options available` saat tabel sumber kosong

5. Klik ikon Filter
6. Klik field `Brand`
7. Verifikasi dropdown menampilkan teks `No options available`
8. Verifikasi dropdown itu bukan error
9. Verifikasi tabel menampilkan empty state List kosong Title "No device names yet" dan Description "Get started by creating your first device name."
10. Tekan Esc untuk menutup dropdown dan Filter Panel

### TC-AC-DN-403: Popup Changelog pada Principal tanpa riwayat tidak menampilkan baris data

11. Klik ikon Changelog di toolbar
12. Verifikasi empty state popup Changelog tampil dengan teks `No changes recorded yet.`
13. Verifikasi tabel Changelog tidak menampilkan baris data
14. Verifikasi tampilan bukan state error pemuatan: tidak ada teks "Unable to load this data." dan tidak ada tombol `[Try Again]`
15. Verifikasi tampilan bukan empty state hasil pencarian: tidak ada teks "No results found"
16. Tutup popup `Changelog: Device Name`

### TC-AC-DN-449: Dropdown opsi filter pada Principal tanpa riwayat

17. Klik ikon Changelog di toolbar
18. Klik ikon Filter
19. Klik field `Device Name`
20. Verifikasi dropdown menampilkan teks "No options available"
21. Verifikasi dropdown itu bukan error
22. Tekan Esc untuk menutup dropdown, lalu tutup popup `Changelog: Device Name`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Tidak ada aksi tulis; akun Principal Tanpa Riwayat tidak membuat entri Changelog.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 10, 16, dan 22 menutup dropdown, Filter Panel, dan popup antar-TC.
- TC-AC-DN-403: empty state popup (langkah 12) diasersi lebih dulu daripada "tidak ada baris data" (langkah 13) karena asersi absence memerlukan anchor positif (bagian 8b butir 2); urutan Expected TC (a lalu b) dibalik.
- TC-AC-DN-449: popup `Changelog: Device Name` dibuka kembali sesuai langkah TC setelah ditutup di langkah 16.
- Nama env password akun Pre-setup #12 tidak tertulis di TC (hanya email); spec memakai `AC_DN_FRESH_PASSWORD` sesuai pola nama berkode modul di `suite.md`.
- Temuan untuk QA:
  - Pre-setup #12 hanya memberi email akun, tanpa nama env password; nama env di atas perlu didaftarkan tim FE.
