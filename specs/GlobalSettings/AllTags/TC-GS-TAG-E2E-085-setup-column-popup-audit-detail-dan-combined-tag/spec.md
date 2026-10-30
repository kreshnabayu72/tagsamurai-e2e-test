---
id: TC-GS-TAG-E2E-085-setup-column-popup-audit-detail-dan-combined-tag
title: "Column Visibility dan Setup Column Surface Sekunder: Popup Audit, Activate TAG Detail, Delete Detail, Audit Detail, dan Popup Combined TAG"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-168
coverage:
  web: automated
---

# Column Visibility dan Setup Column Surface Sekunder: Popup Audit, Activate TAG Detail, Delete Detail, Audit Detail, dan Popup Combined TAG

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A Sari Dewi (Tabel Data Uji Pre-setup TC). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip `gs-tag-registry` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip); pada spec mock, respons preferensi Guided Tooltip untuk flag itu di-mock `true`.
- Kebutuhan mock (respons yang dipaksa). Path dan metode mengikuti `global-settings/all-tags/TestCases/tc-all-tags-backend.md` (nomor bagian di sumber itu dalam kurung):
  - POST `/v2/hardware-tagging/tags/list` (bagian 1): mengembalikan Seed Registri A dengan tag `DD-11` (`E2801160600002054D8A0011`, RFID Combo Tag, `isCombined: true`) combined dengan `DD-13` (NFC `04A224B2C15E83`).
  - GET `/v2/hardware-tagging/tags/{tagId}/combined` (bagian 7), `tagId` = `_id` DD-11: mengembalikan satu baris sibling NFC `04A224B2C15E83` dengan `tagType`, `code`, dan `deviceName` (Popup Combined TAG).
  - POST `/v2/hardware-tagging/tags/audit/session` (bagian 12), body `tagType` `RFID`: mengembalikan `sessionId` dan baris eligible DD-31 sampai DD-38 dengan `deviceName`, `sku`, `code`, `status`, `auditStatus` `Not Scanned`, dan `isCombined` (Popup Audit TAG, RFID Client Audit).
  - POST `/v2/analytics-reporting/tag-activate-logs/list` (bagian 20): mengembalikan Seed Event Log `E-01` sampai `E-14` (Tab Activate TAG).
  - GET `/v2/analytics-reporting/tag-activate-logs/{sessionId}` (bagian 23): untuk `E-01` mengembalikan `activity` `Activate` dengan section `Activated` dan `Waiting for Approval` (baris berisi `tagType`, `code`, `deviceName`, `sku`); untuk `E-05` mengembalikan `activity` `Delete` dengan section `Deleted` dan `Failed` (baris berisi `tagType`, `code`, `statusBefore`). Sedikitnya satu baris per section.
  - POST `/v2/analytics-reporting/tag-audit-logs/list` (bagian 24): mengembalikan Seed Event Log `A-01` sampai `A-12` (Tab Audit TAG).
  - GET `/v2/analytics-reporting/tag-audit-logs/{sessionId}` (bagian 26): untuk `A-01` mengembalikan section `TAGs Found` dan `TAGs Not Found` (baris berisi `tagType`, `code`, `deviceName`, `sku`, `statusAfter`), sedikitnya satu baris per section.
  - API pendukung halaman (GET `/v2/hardware-tagging/tags/license-counters` bagian 2, GET `/v2/hardware-tagging/tags/health-counters` bagian 3, POST `/v2/hardware-tagging/tags/options` bagian 4, POST `/v2/analytics-reporting/tag-activate-logs/options` bagian 21, POST `/v2/analytics-reporting/tag-audit-logs/options` bagian 25), stream SSE registri bila halaman berlangganan (di-mock tanpa event), serta API di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Preferensi kolom (visibilitas) tersimpan per browser per tabel (PRD; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya.
- Suite serial (`parallel: false`): konfigurasi kolom adalah state browser yang dipakai spec lain. State yang dipulihkan di hook `after` (tetap jalan walau spec gagal): konfigurasi kolom semua surface dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; semua kolom tercentang, urutan default).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Tabel "Surface popup yang diuji" (parameter langkah 2 sampai 13):

| Surface | Pembuka | Kolom overlay (berurutan) | Kolom di-uncheck | Kolom tersisa | Penutup |
|---|---|---|---|---|---|
| Popup Audit TAG | klik `Audit TAG`, pilih `RFID` pada overlay `Select TAG Type` | `Device Name`, `SKU`, `Code`, `Status`, `Audit Status` | `SKU` | `Code` | `✕` popup |
| Activate TAG Detail | klik `Event Log`, klik `Detail` pada baris `E-01` | `TAG Type`, `Device Name`, `SKU`, `Code` | `SKU` | `Code` | `✕` popup, lalu `✕` modal Event Log |
| Delete Detail | klik `Event Log`, klik `Detail` pada baris `E-05` | `TAG Type`, `Code`, `Status Sebelum Dihapus` | `Status Sebelum Dihapus` | `Code` | `✕` popup, lalu `✕` modal Event Log |
| Audit Detail | klik `Event Log`, klik tab `Audit TAG`, klik `Detail` pada baris `A-01` | `TAG Type`, `Device Name`, `SKU`, `Code`, `Status After` | `SKU` | `Code` | `✕` popup, lalu `✕` modal Event Log |
| Popup Combined TAG | klik ikon 🔗 pada baris `DD-11` (`E2801160600002054D8A0011`) di registri | `TAG Type`, `Code`, `Device Name` | `Device Name` | `Code` | `✕` popup |

- Kemampuan teknis: `Spectra.intercept()` untuk respons mock di atas; kolom tersisa dipilih spec (`Code`) karena TC tidak menyebut kolom tersisa pada uji guard.

## Test Steps

### TC-GS-TAG-168: Column Visibility dan Setup Column pada Popup Audit, Detail, dan Combined TAG

1. Untuk setiap surface pada tabel Prerequisites, lakukan langkah 2 sampai 13
2. Buka surface sesuai kolom Pembuka
3. Klik header kolom Actions (⋯) pada tabel surface itu
4. Verifikasi overlay Column Visibility memuat kolom data tercentang sesuai kolom "Kolom overlay"
5. Hapus centang semua kolom pada overlay kecuali kolom pada "Kolom tersisa"
6. Verifikasi checkbox kolom tersisa tidak dapat di-uncheck (guard satu kolom tersisa berlaku)
7. Centang kembali semua kolom pada overlay
8. Klik `Setup Column...` pada overlay
9. Hapus centang kolom pada "Kolom di-uncheck", klik `Save`
10. Verifikasi kolom pada "Kolom di-uncheck" tersembunyi di tabel surface itu
11. Tutup surface sesuai kolom Penutup, lalu buka kembali sesuai kolom Pembuka
12. Verifikasi kolom pada "Kolom di-uncheck" tetap tersembunyi
13. Buka overlay Column Visibility lewat header kolom Actions (⋯), centang kembali kolom pada "Kolom di-uncheck", lalu tutup surface sesuai kolom Penutup

## Notes

- Mode: mock. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Pola File Manager (keputusan D-3); Setup Column registri ada di spec 075, 076, dan 077.
- Pembagian TC lintas spec: TC-168 mencakup enam surface; lima surface popup ada di spec ini, surface staging Activate TAG di spec 100. Setup Column Event Log (TC-258) ada di spec 101. Spec ini, 100, dan 101 sama-sama `Mode: mock` dengan komponen Setup Column yang identik, tetapi cara membuka dan menutup surface berbeda (popup dari registri atau modal Event Log; halaman Activate dengan dialog `Unsaved Changes`; dua tab pada modal Event Log), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Alasan spec di atas sekitar 35 langkah (13 langkah tertulis, 61 setelah ekspansi: 1 + 12 x 5): seluruh blok berkelas sama (komponen Setup Column yang identik di lima surface, Mode mock), langkah berulang per surface memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7), dan kegagalan satu surface tidak membuat blok surface lain kehilangan makna. Langkah yang diulang: 2 sampai 13 (lima iterasi).
- `Verifikasi` yang diulang tetap satu per klausa (S-01).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 5, 7, 13 (guard, pemulihan kolom; hook `after` sebagai cadangan).
- Pemilihan kolom tersisa `Code` pada uji guard (langkah 5) dan perilaku disabled checkbox sebagai bukti "tidak bisa di-uncheck" adalah pilihan spec (TC-168 hanya menyatakan "guard satu kolom tersisa berlaku").
- Temuan untuk QA:
  - TC-168 mencakup Popup Audit TAG dengan Client Audit sebagai sesi aktif, tetapi Pre-setup TC memberi Popup Audit di Client Audit sedangkan semua surface lain di Client A; pada spec mock perbedaan client tidak berlaku (respons di-mock).
  - TC-168 tidak menyebut perilaku menutup Popup Audit tanpa pemindaian (apakah dialog `Keep Auditing`/`Discard` tampil); spec menutup lewat `✕` tanpa asersi dialog.
  - TC-168 Expected a menyebut "guard satu kolom tersisa berlaku" tanpa menyebut pesan tooltip (TC File Manager menyebut "At least one column must remain visible."); spec mengasersi hanya state checkbox tidak dapat di-uncheck.
  - TC-168 tidak menyebut selektor ikon 🔗 Popup Combined TAG dan header kolom Actions pada tiap surface; selektor disediakan tim FE (tidak ada ID di PRD).
