---
id: TC-AC-PF-E2E-178-modal-changelog-default-buka-screening-tutup
title: Modal Changelog Default dibuka dari sub-tab Active dan Archive, screening isi modal, dan penutupan lewat icon (X) atau Esc
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-454
  - TC-AC-PF-455
  - TC-AC-PF-456
coverage:
  web: automated
---

# Modal Changelog Default dibuka dari sub-tab Active dan Archive, screening isi modal, dan penutupan lewat icon (X) atau Esc

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu dan tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Buka modal dari sub-tab Active dan Archive (TC-AC-PF-454)

1. Klik ikon Changelog pada toolbar sub-tab Active
2. Verifikasi modal berjudul `Changelog: Plans & Features > Default` terbuka
3. Verifikasi modal memuat kelima entri riwayat Active dan Archive yang digabung (`Enterprise`, `Growth Plus (old)`, `PT Wahana Nusantara`, `Pilot Default`, `Growth`)
4. Tutup modal dengan icon (X)
5. Klik sub-tab Archive, lalu klik ikon Changelog pada toolbar
6. Verifikasi modal berjudul `Changelog: Plans & Features > Default` terbuka
7. Verifikasi modal memuat kelima entri yang sama dengan langkah 3
8. Tutup modal dengan icon (X)

### Screening isi modal (TC-AC-PF-455)

9. Klik ikon Changelog pada toolbar tab Default
10. Verifikasi Header: Title `Changelog: Plans & Features > Default`
11. Verifikasi Header: icon close `(X)` di kanan atas
12. Verifikasi Body: Table Tools `Search`, `Filter`, `Download` tampil
13. Verifikasi kolom `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By` bersifat sortable
14. Verifikasi kolom `Column Visibility (⋯)` tampil di ujung kanan header dan unsortable
15. Verifikasi baris pertama: `12 Aug 26, 09:00` | `Create` | `Enterprise` | `Plan Name` | `—` | `Enterprise` | `Jane S`
16. Verifikasi baris kedua: `01 Aug 26, 08:00` | `Archive` | `Growth Plus (old)` | `Status` | `Active` | `Archived` | `Jane S`
17. Verifikasi baris ketiga: `20 Jul 26, 10:00` | `Push Update` | `PT Wahana Nusantara` | `Plan Version` | `v1` | `v5` | `Sarah T`
18. Verifikasi baris keempat: `10 Jul 26, 12:00` | `Delete` | `Pilot Default` | `Plan Name` | `Pilot Default` | `—` | `John D`
19. Verifikasi baris kelima: `05 Jun 26, 15:40` | `Edit` | `Growth` | `Group count` | `3` | `5` | `Jane S`
20. Verifikasi kolom Action, Old Value, dan New Value berupa plain text (bukan badge)
21. Verifikasi Footer: pagination `Showing 1–5 of 5 entries`
22. Verifikasi Footer: `Rows per page: 10`

### Penutupan modal (TC-AC-PF-456)

23. Klik area gelap di luar modal
24. Verifikasi modal tidak tertutup
25. Klik icon (X)
26. Verifikasi modal tertutup
27. Klik ikon Changelog pada toolbar tab Default
28. Tekan Esc
29. Verifikasi modal tertutup

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) antara blok TC-AC-PF-454 dan TC-AC-PF-455; blok TC-AC-PF-456 dimulai dari modal yang masih terbuka dari blok sebelumnya.
- Verifikasi pada langkah 3 dan 7 memakai sub-tab Active dan Archive sebagai pemicu; baris pembanding (kelima entri) menjadi anchor bahwa modal sudah termuat.
- Temuan untuk QA:
  - TC menetapkan `Showing 1–5 of 5 entries` dan kelima entri sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi ini hanya benar bila fixture BE menyetel log Principal tepat sama dengan dataset. Fixture itu tidak tertulis di TC, PRD, atau LLD; spec menandainya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
  - TC-AC-PF-456 bertipe UI Only di kolom Dependensi TC, tetapi spec ini FE+BE karena dataset Changelog berasal dari backend nyata.
