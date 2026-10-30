---
id: TC-GS-TAG-E2E-101-setup-column-event-log-dua-tab
title: "Column Visibility dan Setup Column Event Log: Tab Activate TAG dan Tab Audit TAG"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-258
coverage:
  web: automated
---

# Column Visibility dan Setup Column Event Log: Tab Activate TAG dan Tab Audit TAG

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Akun: Total Control Client A Sari Dewi (Tabel Data Uji Pre-setup TC). Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Flag Guided Tooltip `gs-tag-registry` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip); pada spec mock, respons preferensi Guided Tooltip untuk flag itu di-mock `true`.
- Kebutuhan mock (respons yang dipaksa). Path dan metode mengikuti `global-settings/all-tags/TestCases/tc-all-tags-backend.md` (nomor bagian di sumber itu dalam kurung):
  - POST `/v2/hardware-tagging/tags/list` (bagian 1): mengembalikan Seed Registri A untuk Tab All.
  - POST `/v2/analytics-reporting/tag-activate-logs/list` (bagian 20): mengembalikan Seed Event Log `E-01` sampai `E-14` dengan kolom `createdAt`, `tagType`, `activity`, `success`, `waitingForApproval`, `failed`, `hardware`, `pic` (Tab Activate TAG).
  - POST `/v2/analytics-reporting/tag-audit-logs/list` (bagian 24): mengembalikan Seed Event Log `A-01` sampai `A-12` (Tab Audit TAG) dengan kolom Date, TAG Type, Found, Not Found, Not Found Action, Hardware, dan PIC.
  - API pendukung halaman (GET `/v2/hardware-tagging/tags/license-counters` bagian 2, GET `/v2/hardware-tagging/tags/health-counters` bagian 3, POST `/v2/hardware-tagging/tags/options` bagian 4, POST `/v2/analytics-reporting/tag-activate-logs/options` bagian 21, POST `/v2/analytics-reporting/tag-audit-logs/options` bagian 25), stream SSE registri bila halaman berlangganan (di-mock tanpa event), serta API di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE. Endpoint Detail sesi tidak dipanggil karena spec ini tidak membuka popup Detail.
- Preferensi kolom (visibilitas) tersimpan per browser per tabel dan per tab Event Log (PRD; prd-conventions.md §9.3), bukan lewat API, sehingga tidak ada endpoint yang di-mock untuknya.
- Suite serial (`parallel: false`): konfigurasi kolom adalah state browser yang dipakai spec lain. State yang dipulihkan di hook `after` (tetap jalan walau spec gagal): konfigurasi kolom kedua tab Event Log dikembalikan ke default (semua kolom tercentang, urutan default).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Kemampuan teknis: `Spectra.intercept()` untuk respons mock di atas.

## Test Steps

### TC-GS-TAG-258: Column Visibility dan Setup Column Event Log untuk kedua tab

1. Klik tombol `Event Log` di toolbar
2. Klik header kolom Actions (⋯) pada Tab Activate TAG
3. Verifikasi overlay Column Visibility memuat 8 kolom data `Date`, `TAG Type`, `Activity`, `Success`, `Waiting for Approval`, `Failed`, `Hardware`, `PIC`
4. Verifikasi kolom Actions tidak ada pada overlay Tab Activate TAG
5. Klik `Setup Column...`, hapus centang `Hardware`, klik `Save`
6. Verifikasi kolom `Hardware` tersembunyi di Tab Activate TAG
7. Klik tab `Audit TAG`
8. Verifikasi kolom `Hardware` tampil di Tab Audit TAG (konfigurasi tiap tab independen)
9. Klik header kolom Actions (⋯) pada Tab Audit TAG
10. Verifikasi overlay Column Visibility memuat 7 kolom data `Date`, `TAG Type`, `Found`, `Not Found`, `Not Found Action`, `Hardware`, `PIC`
11. Verifikasi kolom Actions tidak ada pada overlay Tab Audit TAG
12. Klik `Setup Column...`, hapus centang `Hardware`, klik `Save`
13. Verifikasi kolom `Hardware` tersembunyi di Tab Audit TAG
14. Tutup modal Event Log lewat `✕`, lalu klik tombol `Event Log` lagi
15. Verifikasi kolom `Hardware` tetap tersembunyi di Tab Activate TAG
16. Klik tab `Audit TAG`
17. Verifikasi kolom `Hardware` tetap tersembunyi di Tab Audit TAG
18. Buka overlay Column Visibility Tab Audit TAG, centang kembali `Hardware`, klik tab `Activate TAG`, buka overlay Column Visibility, centang kembali `Hardware`, lalu tutup modal Event Log lewat `✕`

## Notes

- Mode: mock. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Pola File Manager (keputusan D-3); Setup Column registri ada di spec 075, 076, dan 077.
- Pembagian TC lintas spec: TC-258 ada di spec ini; TC-168 (lima surface popup dan staging Activate TAG) ada di spec 085 dan 100. Event Log berdiri sebagai spec sendiri karena dibuka sebagai modal dengan dua tab yang masing-masing menyimpan konfigurasi kolom sendiri, berbeda dari popup dan halaman Activate pada spec 085 dan 100.
- Spec ini 18 langkah tertulis tanpa langkah berulang dengan ekspansi.
- `Verifikasi` yang diulang tetap satu per klausa (S-01).
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 14 dan 16 (penutupan dan pembukaan ulang modal, pindah tab), langkah 7 (pindah tab), langkah 18 (pemulihan kolom; hook `after` sebagai cadangan).
- Temuan untuk QA:
  - TC-258 langkah 5 ("ulangi untuk `Hardware`" pada Tab Audit TAG) tidak menyebut apakah overlay Tab Audit TAG diperiksa terpisah; spec mengasersi 7 kolom data dan tidak adanya kolom Actions sesuai Expected a.
  - TC-258 tidak menyebut selektor header kolom Actions pada tabel Event Log; selektor disediakan tim FE (tidak ada ID di PRD).
