---
id: TC-GS-TAG-E2E-100-setup-column-tabel-staging-activate-tag
title: "Column Visibility dan Setup Column Tabel Staging Activate TAG GPS"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-168
coverage:
  web: automated
---

# Column Visibility dan Setup Column Tabel Staging Activate TAG GPS

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A Sari Dewi (Tabel Data Uji Pre-setup TC). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip); pada spec mock, respons preferensi Guided Tooltip untuk kedua flag di-mock `true`.
- Kebutuhan mock (respons yang dipaksa). Path dan metode mengikuti `global-settings/all-tags/TestCases/tc-all-tags-backend.md` (nomor bagian di sumber itu dalam kurung):
  - POST `/v2/hardware-tagging/tags/list` (bagian 1): mengembalikan Seed Registri A untuk Tab All (dipanggil saat registri dibuka, dan lagi sesudah `[Leave]`).
  - POST `/v2/hardware-tagging/tags/activate/session` (bagian 9), body `tagType` `GPS`: mengembalikan `sessionId` baru, `quota` (`used`, `quota`, `remaining`), `selfPurchasedEnabled` `true`, dan `handheldReader` `null`.
  - POST `/v2/hardware-tagging/tags/activate/scan` (bagian 10): untuk IMEI `356938035643001` (DD-S1) mengembalikan hasil `outcome` `official` dengan `snapshot` Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`, `alreadyActivated` `false`, `duplicateInSession` `false`, `errorReason` `null`, dan `pool` yang konsisten. Contoh respons di sumber memakai tipe NFC; kontrak entri manual GPS pada endpoint ini dikonfirmasi tim FE (lihat Temuan untuk QA).
  - API pendukung halaman (GET `/v2/hardware-tagging/tags/license-counters` bagian 2, GET `/v2/hardware-tagging/tags/health-counters` bagian 3, POST `/v2/hardware-tagging/tags/options` bagian 4), stream SSE registri bila halaman berlangganan (di-mock tanpa event), serta API di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Preferensi kolom (visibilitas) tersimpan per browser per tabel (PRD; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya.
- Suite serial (`parallel: false`): konfigurasi kolom adalah state browser yang dipakai spec lain. State yang dipulihkan di hook `after` (tetap jalan walau spec gagal): konfigurasi kolom tabel staging dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; semua kolom tercentang, urutan default).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Kemampuan teknis: `Spectra.intercept()` untuk respons mock di atas; entri manual GPS (input teks dan tombol `Add`; label dan placeholder menunggu desain, selektor disediakan tim FE); kolom tersisa dipilih spec (`Code`) karena TC tidak menyebut kolom tersisa pada uji guard.

## Test Steps

### TC-GS-TAG-168: Column Visibility dan Setup Column pada tabel staging Activate TAG

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik `Continue` pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual `356938035643001`
3. Klik header kolom Actions (⋯) pada tabel staging
4. Verifikasi overlay Column Visibility memuat kolom data tercentang `Device Name`, `SKU`, `Brand`, `Model/Type`, `Code`, `Status`
5. Hapus centang semua kolom pada overlay kecuali `Code`
6. Verifikasi checkbox `Code` tidak dapat di-uncheck (guard satu kolom tersisa berlaku)
7. Centang kembali semua kolom pada overlay
8. Klik `Setup Column...`, hapus centang `SKU`, klik `Save`
9. Verifikasi kolom `SKU` tersembunyi di tabel staging
10. Buka Global Settings > TAG lewat navigasi in-app
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Klik `+ Activate TAG`, pilih `GPS`, klik `Continue`, lalu tambahkan lewat entri manual `356938035643001`
14. Verifikasi kolom `SKU` tetap tersembunyi di tabel staging
15. Buka overlay Column Visibility, centang kembali `SKU`, lalu buka Global Settings > TAG lewat navigasi in-app dan klik `[Leave]`

## Notes

- Mode: mock. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Pola File Manager (keputusan D-3); Setup Column registri ada di spec 075, 076, dan 077.
- Pembagian TC lintas spec: TC-168 mencakup enam surface; surface staging Activate TAG ada di spec ini, lima surface popup (Popup Audit, Activate TAG Detail, Delete Detail, Audit Detail, Popup Combined TAG) di spec 085. Setup Column Event Log (TC-258) ada di spec 101. Staging berdiri sebagai spec sendiri karena dibuka dari halaman Activate dengan dialog `Unsaved Changes` saat ditutup, berbeda dari popup dan modal pada spec 085 dan 101.
- Spec ini 15 langkah tertulis tanpa langkah berulang dengan ekspansi.
- `Verifikasi` yang diulang tetap satu per klausa (S-01). Penutupan staging memakai `Unsaved Changes` dan `[Leave]` (langkah 10 sampai 12, S-08; dialog diasersi di langkah 11 sehingga tidak perlu dicatat lagi).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1 sampai 2 dan 13 (menyiapkan baris staging), langkah 5, 7, 15 (guard dan pemulihan kolom; hook `after` sebagai cadangan), langkah 12 (menutup halaman Activate).
- Pemilihan kolom tersisa `Code` pada uji guard (langkah 5) dan perilaku disabled checkbox sebagai bukti "tidak bisa di-uncheck" adalah pilihan spec (TC-168 hanya menyatakan "guard satu kolom tersisa berlaku").
- Temuan untuk QA:
  - Contoh respons `activate/scan` pada `tc-all-tags-backend.md` bagian 10 memakai tipe NFC dan tidak memuat varian GPS (unggah berkas GPS ditunda sumbernya); kontrak entri manual GPS pada endpoint ini dikonfirmasi tim FE.
  - TC-168 Expected a menyebut "guard satu kolom tersisa berlaku" tanpa menyebut pesan tooltip; spec mengasersi hanya state checkbox tidak dapat di-uncheck.
  - TC-168 tidak menyebut selektor header kolom Actions pada tabel staging; selektor disediakan tim FE (tidak ada ID di PRD).
