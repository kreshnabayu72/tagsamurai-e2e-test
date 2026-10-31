---
id: TC-GS-GSET-E2E-006-record-belum-ada-seed-default-dan-save-pertama
title: "Record belum ada, Save pertama"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-117
coverage:
  web: automated
---

# Record belum ada, Save pertama

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen untuk akun aktor spec ini dan dipulihkan di `after`. Pemulihan record Client A tidak relevan karena spec memakai entitas lain.
- Akun aktor: Total Control staf `Client Tanpa Record` (Pre-setup No 24; akun tidak ada di Tabel Pre-setup TC, disediakan tim FE): email disediakan tim FE, kredensial `Spectra.env.GS_NORECORD_TC_PASSWORD` (nama env baru, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftaran di tahap script). Login di hook `before`; halaman General Settings dibuka di hook `beforeEach` setelah record dihapus.
- Kemampuan teknis (kolom Automation TC: Manual Only; dituliskan sebagai kebutuhan, bukan alasan mengeluarkan TC): record General Settings entitas `Client Tanpa Record` dihapus lewat database oleh tim BE di hook `before` (failure injection; disediakan tim BE, tidak ada endpoint di TC, PRD, atau LLD). Hook `after` memulihkan entitas ke keadaan record ada (pemulihan lewat Save yang dilakukan spec dan, bila spec gagal sebelum Save, lewat prosedur tim BE).
- Data: Session Idle Timeout `1 hour`. Seed default yang diasersi: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes` (dari `Fixture.generalSettings.<kunci>`; berkas `fixtures/generalSettings.json` belum ada, ditandai untuk tahap script).
- Baseline Changelog: total hasil Search `Session Idle Timeout` di Modal Changelog dicatat sebagai `{nIdle}` sebelum Save (langkah 8 sampai 10) karena audit trail permanen (S-12).
- State global: record entitas `Client Tanpa Record` berubah (dibuat oleh Save pertama) dan entri Changelog bertambah (audit trail permanen); entitas direset tim BE sebelum tiap run.

## Test Steps

1. Verifikasi Select "Currency Code" bernilai seed default `IDR`
2. Verifikasi Select "Date Format" bernilai seed default `dd/MM/yy`
3. Verifikasi Select "Time Format" bernilai seed default `HH:mm`
4. Verifikasi Select "Time Zone" bernilai seed default `Asia/Jakarta`
5. Verifikasi Select "Session Idle Timeout" bernilai seed default `30 minutes`
6. Verifikasi form tampil tanpa error server (tidak ada teks "Unable to load this data.")
7. Verifikasi Button "Save" disabled
8. Buka Modal Changelog
9. Ketik Search `Session Idle Timeout`, tekan Enter, lalu catat total hasil di Pagination sebagai `{nIdle}` (0 bila tampil "No results found")
10. Tutup Modal Changelog dengan `✕`
11. Pilih Session Idle Timeout `1 hour`
12. Klik `[Save]`
13. Verifikasi toast sukses "Success, general settings has been saved."
14. Muat ulang halaman (F5)
15. Verifikasi Select "Session Idle Timeout" bernilai `1 hour`
16. Verifikasi Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, dan Time Zone `Asia/Jakarta` tetap nilai seed default
17. Buka Modal Changelog
18. Ketik Search `Session Idle Timeout`, tekan Enter
19. Verifikasi total hasil Search sama dengan `{nIdle}` + 1
20. Verifikasi baris teratas memuat Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour`

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 20 langkah.
- Pecahan Expected: a menjadi langkah 1 sampai 7 (seed default per field, tanpa error server, Save disabled); b menjadi langkah 13; c menjadi langkah 15 dan 16; d menjadi langkah 19 dan 20.
- Langkah penghubung (tanpa `Verifikasi`): langkah 8, 9, 10 (membaca baseline `{nIdle}` sebelum Save) dan langkah 17, 18 (membuka Modal Changelog dan mencari `Session Idle Timeout` sebelum asersi).
- Langkah 6 (tanpa teks error) ditulis karena Expected a menyatakan "tanpa error server"; anchor positifnya langkah 1 sampai 5 (form terisi).
- Temuan untuk QA:
  - TC-GS-GSET-117 Expected d menyatakan "1 baris" Field `Session Idle Timeout`. Total baris Changelog tidak diasersi sebagai angka absolut (S-12, audit trail permanen); spec mengasersi total hasil Search `Session Idle Timeout` sebesar `{nIdle}` + 1 (satu baris bertambah oleh Save) dan baris teratas dengan Old Value `30 minutes` dan New Value `1 hour`. Bila jumlah tepat 1 dimaksudkan, TC perlu menyatakan bahwa riwayat entitas ikut dibersihkan.
  - Mekanisme penghapusan record lewat database dan reset entitas tiap run tidak didefinisikan di TC, PRD, atau LLD (disediakan tim BE; endpoint tidak dikarang).
  - Akun staf `Client Tanpa Record` tidak tertulis di Pre-setup TC (email disediakan tim FE).
