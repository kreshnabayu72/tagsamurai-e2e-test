---
id: TC-GS-IMPORT-E2E-106-sel-custom-field-phone-error-tanpa-kode-negara-country-code-default
title: "Sel Custom Field Phone error tanpa kode negara: Country Code default Indonesia lalu valid setelah Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-236
coverage:
  web: automated
---

# Sel Custom Field Phone error tanpa kode negara: Country Code default Indonesia lalu valid setelah Save

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec mengubah tipe Custom Field `Emergency Phone` Client Limit dan draft Import dibagikan ke seluruh admin satu client (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD` (nama env baru, didaftarkan pada tahap script). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client Limit.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-36 (Draft User Login 2 baris Client Limit dari `user-login-phone.csv`; Division `Engineering` dan Access `Global Settings` pada kedua baris): #1 Tono Wijaya (`tono.wijaya@example.com`) dan #2 Sari Utami (`sari.utami@example.com`) dengan Custom Field Emergency Phone berisi digit mentah (`081234567890` baris #1, `081298765432` baris #2) yang menjadi `error` setelah tipe Emergency Phone diubah dari Text ke Phone (fixture ubah tipe Custom Field, disediakan tim FE/BE); nama dan email literal karena asersi bergantung pada isi D-36; draft dibuat ulang sebelum spec dan 2 baris tidak termasuk kelas volume.
- Kemampuan teknis: fixture ubah tipe Custom Field `Emergency Phone` Text ke Phone dan pemulihannya, skrip seed D-36 (disediakan tim FE/BE).
- State global: tipe Custom Field `Emergency Phone` Client Limit diubah ke Phone; hook `after` memulihkan tipe ke Text (nilai awal dicatat di hook `before`) dan membuang draft walau spec gagal di tengah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan tipe Custom Field, buang draft User Login Client Limit, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-236: Sel Custom Field Phone error tanpa kode negara

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Verifikasi Country Code pada sel Emergency Phone baris #1 menampilkan `🇮🇩 +62`
3. Verifikasi Number pada sel Emergency Phone baris #1 menampilkan digit mentah `081234567890`
4. Ganti Number menjadi `81234567890`
5. Klik `[Save]`
6. Verifikasi muncul toast sukses: "Success, row has been updated."
7. Verifikasi sel Emergency Phone baris #1 menampilkan `+62 81234567890` tanpa border `danger`
8. Verifikasi baris #1 berstatus `pending`
9. Verifikasi sel Emergency Phone baris #2 tetap menampilkan `081298765432` berborder `danger`
10. Verifikasi baris #2 tetap berstatus `error`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Spec satu TC dengan satu alur; tidak digabung dengan spec Edit Mode lain karena memakai client dan perubahan tipe Custom Field yang berbeda.
- Temuan untuk QA:
  - TC-GS-IMPORT-236 Precondition c menyebut baris menjadi `error` setelah tipe Emergency Phone diubah lewat fixture, tetapi Kontrak Fixture tidak memuat fixture ubah tipe Custom Field; mekanisme disediakan tim FE/BE (S-13).
  - Post Condition kosong; tidak ada yang diasersi.
