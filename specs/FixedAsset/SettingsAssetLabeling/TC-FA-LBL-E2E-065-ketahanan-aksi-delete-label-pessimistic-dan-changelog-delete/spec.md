---
id: TC-FA-LBL-E2E-065-ketahanan-aksi-delete-label-pessimistic-dan-changelog-delete
title: "Action Resilience: Delete Label pessimistic (dialog, toast, baris, dan Changelog Delete)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:action-resilience-idempotensi-spec/delete-label-single
coverage:
  web: automated
---

# Action Resilience: Delete Label pessimistic (dialog, toast, baris, dan Changelog Delete)

## Prerequisites

- Mode: FE+BE (backend nyata) dengan intercept penahan respons di atas backend nyata (konvensi bagian 6).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Tidak ada ganti akun.
- Data uji `DU-72` (Label bersih untuk Delete pessimistic): `Res-{runId}-065`, Total Asset 0 dan bukan Default Label, dibuat lewat sesi API di hook `before`. Hook `after` menghapus label itu lewat sesi API bila masih ada.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label; `Spectra.intercept()` untuk menahan lalu melepas respons request Delete label di atas backend nyata (menahan respons untuk mengamati state UI, bukan kegagalan yang dipaksa); disediakan tim FE/BE.
- State global: spec menghapus label `DU-72` lewat UI; intercept dilepas di langkah 9. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:action-resilience-idempotensi-spec/delete-label-single: Delete Label (Single): pessimistic, dialog tertutup, toast sukses, baris dihapus, dan Changelog Delete

1. Ketik Search `DU-72`, tekan Enter
2. Verifikasi baris label `DU-72` tampil pada Labels List dengan Total Asset 0
3. Tahan respons request Delete label `DU-72` lewat intercept
4. Klik `[⋯]` pada baris label `DU-72`, pilih `Delete`
5. Verifikasi dialog `Delete Label` tampil dengan nama label `DU-72`
6. Klik `[Delete]`
7. Verifikasi dialog `Delete Label` masih tampil selama respons ditahan
8. Verifikasi baris label `DU-72` masih tampil pada Labels List selama respons ditahan
9. Lepas tahanan respons
10. Verifikasi toast `Success, label has been deleted.` tampil
11. Verifikasi dialog `Delete Label` tertutup
12. Verifikasi baris label `DU-72` tidak tampil pada Labels List
13. Klik ikon Changelog pada toolbar tabel
14. Ketik Search `DU-72`, tekan Enter
15. Verifikasi entri Delete dengan Field `Label Name`, Old Value `DU-72`, New Value `—`, dan Modified By `[First Name] [Last Initial]` akun `DU-01` tampil pada tabel Modal Changelog
16. Klik `[✕]` pada header Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 1 menemukan baris target di Labels List yang dapat memuat lebih dari satu halaman (R-16); langkah 3 menyiapkan intercept dan langkah 9 melepasnya (S-09); langkah 13 membuka Modal Changelog; langkah 14 mempersempit tabel ke entri `DU-72`; langkah 16 menutup modal.
- Asersi state sementara tepat waktu (bagian 8b butir 5): langkah 7 dan 8 diasersi sebelum respons dilepas (langkah 9), karena Update Mode Pessimistic berarti dialog dan baris tetap sampai server menjawab. Asersi dialog tertutup (langkah 11) dan baris hilang (langkah 12) ditulis sesudah toast sukses (langkah 10) yang menjadi anchor bahwa respons sudah diproses.
- Anchor positif: langkah 2 membuktikan baris `DU-72` termuat sebelum asersi baris hilang; langkah 5 membuktikan dialog terbuka sebelum asersi dialog masih tampil dan tertutup.
- Klausa baris `delete-label-single` yang diasersi: Pessimistic, On Success (dialog tertutup, toast sukses, baris dihapus), dan Logging (Changelog "Delete"). Klausa On Conflict (resource sudah tidak ada: `T-11`; label menjadi dipakai: `D-02`) dan transaksi atomik atas guard dan sisa relasi pada aset `Deleted` diasersi pada spec Delete lain suite ini yang mengutip `E-FALB-12`, `E-FALB-14`, dan `E-FALB-24`.
- Temuan PRD: klausa On Failure (5xx atau timeout: dialog `D-01` tetap terbuka, data tidak terhapus, toast `T-07` atau `T-12`) sama dengan `E-FALB-23` yang ditahan (`IGAP-0042`) sehingga tidak diasersi di spec ini.
