---
id: TC-FA-LBL-E2E-016-mock-state-error-muat-kosong-dan-gagal-unduh-labels
title: "Mock: state error muat tabel dan popup, state Changelog kosong, dan gagal unduh"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - F-FALB-08.k2
  - F-FALB-08.k3
  - F-FALB-09.k1
  - F-FALB-09.k3
coverage:
  web: automated
---

# Mock: state error muat tabel dan popup, state Changelog kosong, dan gagal unduh

## Prerequisites

- Mode: mock
- Akun Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`); seluruh API di-mock, sehingga login memakai sesi dari tim FE.
- Login di hook `before` spec ini (sesi dari tim FE); halaman dibuka hook `beforeEach` suite.
- Data uji: `DU-39` (respons mock Labels, Changelog, dan ekspor: respons normal berisi baris, daftar kosong, error 5xx, dan kegagalan ekspor per endpoint).
- Endpoint yang di-mock lewat `Spectra.intercept()` (openapi.yaml modul): `POST /v2/master-asset-registry/labels/list` (post_label_list, daftar Labels List), `POST /v2/master-asset-registry/labels/options` (post_label_options, opsi Filter), dan `POST /v2/master-asset-registry/labels/export` (post_label_export, ekspor Labels List) dan `POST /v2/master-asset-registry/labels/{id}/assets/list` (post_label_tagged_assets_list, labels-tagged-assets.yaml, daftar Tagged Asset Drawer). Daftar dan ekspor Changelog: Labels dibaca dari change-log read contract analytics-reporting (low-level-design.md modul menyatakan modul ini tidak mendefinisikan route Changelog), sehingga endpoint itu serta API pendukung di luar sumber modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- State global: intercept dilepas pada langkah 28 dan di hook `after`.

## Test Steps

### F-FALB-08.k3: Gagal fetch data ekspor menampilkan toast error

1. Atur mock `POST /v2/master-asset-registry/labels/export` merespons gagal (`DU-39`).
2. Klik Download.
3. Klik `Download as CSV`.
4. Verifikasi toast `Error, failed to download Labels.` tampil.
5. Tunggu toast lama hilang otomatis.
6. Klik icon Changelog.
7. Atur mock ekspor Changelog merespons gagal (`DU-39`).
8. Klik Download pada toolbar modal Changelog: Labels.
9. Klik `Download as XLSX`.
10. Verifikasi toast `Error, failed to download Changelog-Labels.` tampil.
11. Klik `[✕]` pada modal Changelog: Labels.

### F-FALB-09.k1: Belum ada entri Changelog menampilkan empty state

12. Atur mock daftar Changelog merespons daftar kosong (`DU-39`).
13. Klik icon Changelog.
14. Verifikasi empty state modal Changelog: Labels menampilkan ilustrasi dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`.
15. Klik `[✕]` pada modal Changelog: Labels.

### F-FALB-09.k3: Gagal fetch data modal menampilkan error state inline

16. Atur mock daftar Changelog merespons error 5xx (`DU-39`).
17. Klik icon Changelog.
18. Verifikasi ErrorState inline di dalam modal Changelog: Labels menampilkan `Unable to load this data.` dan tombol `[Try Again]`.
19. Klik `[✕]` pada modal Changelog: Labels.
20. Atur mock `POST /v2/master-asset-registry/labels/{id}/assets/list` merespons error 5xx (`DU-39`).
21. Klik chip Label pada baris pertama tabel Labels List untuk membuka Drawer Tagged Asset.
22. Verifikasi ErrorState inline di dalam Drawer `Tagged Assets` menampilkan `Unable to load this data.` dan tombol `[Try Again]`.
23. Klik `[✕]` pada Drawer `Tagged Assets`.

### F-FALB-08.k2: Gagal fetch data tabel menampilkan error state

24. Atur mock `POST /v2/master-asset-registry/labels/list` merespons error 5xx (`DU-39`).
25. Muat ulang halaman (F5).
26. Klik tab `Labels`.
27. Verifikasi ErrorState tabel Labels List menampilkan `Unable to load this data.` dan tombol `[Try Again]`.
28. Lepas semua intercept.

## Notes

- Spec ini `Mode: mock`: seluruh API di-mock dan hanya perilaku FE atas respons mock yang diasersi (bagian 6, resilience `Mode: mock`).
- Langkah penghubung (S-03): langkah 5 (menunggu toast pertama hilang otomatis sebelum asersi toast kedua, R-12), 6, 11, 13, 15, 17, dan 19 (membuka dan menutup modal Changelog: Labels), 21 dan 23 (membuka dan menutup Drawer Tagged Asset), 25 (memuat ulang halaman agar daftar dimuat dengan mock error), 26 (klik tab `Labels` sesudah F5 pada halaman bertab, bagian 8b butir 9), dan 28 (pemulihan intercept).
- Langkah 21 memakai baris pertama respons mock Labels (`DU-39`); Search tidak dipakai karena tabel tidak berisi asersi atas baris tertentu.
