---
id: TC-GS-GSET-E2E-026-resilience-changelog-loading-error-load-dan-download-gagal
title: "Resilience Modal Changelog: Loading, Error Load, Try Again, dan Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-62
  - TC-GS-GSET-64
  - TC-GS-GSET-101
coverage:
  web: automated
---

# Resilience Modal Changelog: Loading, Error Load, Try Again, dan Download Gagal

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness fault injection, prinsip 13b konvensi).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Seeding minimal (S-11; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10): satu `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) lewat sesi API akun Budi Santoso dengan `sessionIdleTimeout` 60 (nilai lain tetap baseline), sehingga Changelog memuat baris Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour`, Modified By `Budi S`; lalu `PUT` kedua dengan `sessionIdleTimeout` 30 (kembali ke baseline) yang menambah baris Old Value `1 hour`, New Value `30 minutes`. Kedua baris adalah baris terbaru sehingga tampil di halaman pertama Modal Changelog. Payload mengacu ke `Fixture.generalSettings.payloadIdle60` dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script).
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit. Endpoint Changelog General Settings tidak tercantum di `general-settings/API/openapi.yaml` maupun `low-level-design.md`; spec memakai kontrak Changelog Activity Log (`global-settings/activity-log/API/openapi.yaml`) dan tim FE mengonfirmasi path yang dipanggil Modal Changelog General Settings:
  - Respons list `POST /v2/analytics-reporting/change-logs/list`: tahan 5 detik lalu jawab normal (langkah 1 sampai 7, TC-GS-GSET-62; durasi tahan adalah data uji, bukan aturan PRD); jawab 500 (langkah 8 sampai 13, TC-GS-GSET-64), dilepas di langkah 13 sebelum `[Try Again]`.
  - Respons export `POST /v2/analytics-reporting/change-logs/export`: jawab 500 tanpa meneruskan request ke server (langkah 16 sampai 20, TC-GS-GSET-101), dilepas di langkah 20.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): semua intercept dilepas; Modal Changelog ditutup; record Client A dipastikan di baseline Pre-setup baris 10 (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-62: Modal Changelog menampilkan loading saat riwayat diambil

1. Pasang intercept pada respons list Changelog (`POST /v2/analytics-reporting/change-logs/list`): tahan 5 detik lalu jawab normal
2. Klik icon Changelog di pojok kanan atas halaman
3. Verifikasi Loading component tampil di dalam modal sebelum respons diterima
4. Tunggu respons diterima
5. Verifikasi tabel terisi: baris Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour`, Modified By `Budi S` tampil
6. Lepas intercept respons list Changelog
7. Tutup modal Changelog dengan tekan `Esc`

### TC-GS-GSET-64: Modal Changelog menampilkan error load

8. Pasang intercept pada respons list Changelog: jawab 500
9. Klik icon Changelog di pojok kanan atas halaman
10. Verifikasi teks `Unable to load this data.` tampil
11. Verifikasi tombol `[Try Again]` tampil
12. Verifikasi tampilan bukan empty state (teks `No changelog yet` tidak tampil)
13. Lepas intercept respons list Changelog (pulihkan respons normal)
14. Klik `[Try Again]`
15. Verifikasi tabel riwayat termuat: baris Field `Session Idle Timeout`, Old Value `30 minutes`, New Value `1 hour` tampil

### TC-GS-GSET-101: Download Changelog gagal

16. Pasang intercept pada respons export Changelog (`POST /v2/analytics-reporting/change-logs/export`): jawab 500
17. Klik Download di toolbar modal
18. Pilih `Download as CSV`
19. Verifikasi toast error `Error, failed to download Changelog-General-Settings.`
20. Lepas intercept respons export Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-GSET-62 menahan respons hanya untuk mengamati state Loading (bukan kegagalan yang dipaksa) dan ditempatkan di spec ini karena memakai permukaan, dataset, dan endpoint list yang sama dengan TC-GS-GSET-64. Disposisi nilai "5 detik" TC-62: durasi tahan adalah data uji (PRD §7 S-15 hanya menyebut Loading component).
- Urutan TC dalam spec: TC-62, 64, 101. TC-64 berakhir dengan tabel termuat sehingga Modal Changelog tetap terbuka untuk TC-101; langkah 17 memakai toolbar modal yang sama (tanpa membuka ulang modal).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (menunggu respons), 6, 13, dan 20 (melepas intercept segera setelah pemicu, S-09), dan 7 (menutup modal agar TC-64 membuka modal dari awal).
- Langkah 12 adalah asersi absence atas teks `No changelog yet`; anchor positifnya adalah langkah 10 dan 11 (teks error dan `[Try Again]` pada surface modal yang sama, bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-GSET-64 langkah 1 menyebut "Paksa GET changelog gagal (5xx)" dan Data Uji "Intercept GET respons 500", sedangkan kontrak list Changelog pada `activity-log/API/openapi.yaml` memakai `POST`; spec mengintercept request list apa pun metodenya sesuai path yang dikonfirmasi tim FE.
  - Endpoint list, options, dan export Modal Changelog General Settings tidak tertulis di `openapi.yaml` atau `low-level-design.md` General Settings; path di Prerequisites mengikuti kontrak Activity Log dan perlu dikonfirmasi.
  - TC-GS-GSET-101 Expected hanya toast error; tidak ada Expected untuk state modal sesudah gagal (modal tetap terbuka atau tidak) sehingga tidak diasersi.
